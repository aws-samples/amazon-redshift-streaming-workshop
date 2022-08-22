import base64
from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    Aws,
    aws_ec2 as _ec2,
    aws_iam as _iam,
    aws_redshift as _redshift,
    aws_secretsmanager as _sm,
    aws_redshiftserverless as _rs,
    aws_sagemaker as _sg,
)

from constructs import Construct

class RedshiftStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, ingestion_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        environment = self.node.try_get_context('environment')
        redshift_config = self.node.try_get_context(f'{environment}_redshift_config')
        sagemaker_config = self.node.try_get_context(f'{environment}_sagemaker_config')

        vpc = _ec2.Vpc(
            self,
            "VpcId",
            max_azs=redshift_config['max_azs']
        )

        # Create new security group to be used by redshift
        rs_security_group = _ec2.SecurityGroup(
            self,
            "redshiftSecurityGroup",
            vpc=vpc
        )

        sg_security_group = _ec2.SecurityGroup(
            self,
            "sagemakerSecurityGroup",
            vpc=vpc
        )

        rs_security_group.add_ingress_rule(sg_security_group, _ec2.Port.tcp(5439))

        redshift_password = _sm.Secret(
            self,
            "redshift_password",
            description="Redshift password",
            secret_name="REDSHIFT_PASSWORD",
            generate_secret_string=_sm.SecretStringGenerator(exclude_punctuation=True),
            removal_policy=RemovalPolicy.DESTROY,
        )

        rs_role = _iam.Role(
            self, "redshiftClusterRole",
            assumed_by=_iam.ServicePrincipal(
                "redshift.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftAllCommandsFullAccess"
                )
            ]
        )

        _iam.ManagedPolicy(
            self,
            "spectrum_lake_formation_policy",
            description="Provide access between Redshift Spectrum and Lake Formation",
            statements=[
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=[
                        "glue:CreateDatabase",
                        "glue:DeleteDatabase",
                        "glue:GetDatabase",
                        "glue:GetDatabases",
                        "glue:UpdateDatabase",
                        "glue:CreateTable",
                        "glue:DeleteTable",
                        "glue:BatchDeleteTable",
                        "glue:UpdateTable",
                        "glue:GetTable",
                        "glue:GetTables",
                        "glue:BatchCreatePartition",
                        "glue:CreatePartition",
                        "glue:DeletePartition",
                        "glue:BatchDeletePartition",
                        "glue:UpdatePartition",
                        "glue:GetPartition",
                        "glue:GetPartitions",
                        "glue:BatchGetPartition",
                        "lakeformation:GetDataAccess",
                    ],
                    resources=["*"],
                )
            ],
            roles=[rs_role],
        )

        s3_bucket_raw = ingestion_stack.get_s3_bucket_raw
        s3_bucket_raw.grant_read_write(rs_role)

        order_stream = ingestion_stack.get_order_stream
        order_stream.grant_read_write(rs_role)
        
        self.rs_namespace = _rs.CfnNamespace(
            self,
            "redshiftServerlessNamespace",
            namespace_name="ns-streaming",
            default_iam_role_arn=rs_role.role_arn,
            iam_roles=[rs_role.role_arn],
            admin_username=redshift_config['master_username'],
            admin_user_password=redshift_password.secret_value.unsafe_unwrap(),
        )

        self.rs_workgroup = _rs.CfnWorkgroup(
            self,
            "redshiftServerlessWorkgroup",
            workgroup_name="wg-streaming",
            base_capacity=32,
            namespace_name=self.rs_namespace.ref,
            security_group_ids=[rs_security_group.security_group_id],
            subnet_ids=vpc.select_subnets(
                subnet_type=_ec2.SubnetType.PRIVATE_WITH_NAT
            ).subnet_ids,
        )


        sg_role = _iam.Role(
            self, "sagemakerRole",
            assumed_by=_iam.ServicePrincipal(
                "sagemaker.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSageMakerFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftDataFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "SecretsManagerReadWrite"
                ),
            ]
        )

        cfn_notebook_instance_lifecycle_config = _sg.CfnNotebookInstanceLifecycleConfig(
            self, 
            "sagemakerLifecycleConfig",
            notebook_instance_lifecycle_config_name=sagemaker_config['lifecycle_config_name'],
            on_create=[_sg.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty(
                content=sagemaker_config['content']
            )]
        )

        cfn_notebook_instance = _sg.CfnNotebookInstance(
            self, 
            "sagemakerNotebook",
            instance_type=sagemaker_config['instance_type'],
            role_arn=sg_role.role_arn,
            lifecycle_config_name=cfn_notebook_instance_lifecycle_config.notebook_instance_lifecycle_config_name,
            notebook_instance_name=sagemaker_config['notebook_instance_name'],
            security_group_ids=[sg_security_group.security_group_id],
            subnet_id=vpc.select_subnets(
                subnet_type=_ec2.SubnetType.PRIVATE_WITH_NAT
            ).subnet_ids[0]
        )

