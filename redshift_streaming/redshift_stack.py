import json
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
    aws_lambda as _lambda,
    Duration,
    aws_events as _events,
    aws_events_targets as _events_targets,
)

from constructs import Construct

class RedshiftStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, ingestion_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        environment = self.node.try_get_context('environment')
        redshift_config = self.node.try_get_context(f'{environment}_redshift_config')
        sagemaker_config = self.node.try_get_context(f'{environment}_sagemaker_config')

        vpc = _ec2.Vpc.from_lookup(
            self,
            "VpcId",
            is_default=True
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
        rs_security_group.add_ingress_rule(rs_security_group, _ec2.Port.tcp(5439))

        # redshift_password = _sm.Secret(
        #     self,
        #     "redshift_password",
        #     description="Redshift password",
        #     secret_name=redshift_config['secret_name'],
        #     generate_secret_string=_sm.SecretStringGenerator(
        #         secret_string_template=json.dumps({"username": redshift_config['admin_username']}),
        #         generate_string_key="password",
        #         exclude_punctuation=True
        #     ),
        #     removal_policy=RemovalPolicy.DESTROY,
        # )

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
        
        # self.rs_namespace = _rs.CfnNamespace(
        #     self,
        #     "redshiftServerlessNamespace",
        #     namespace_name=redshift_config['namespace_name'],
        #     default_iam_role_arn=rs_role.role_arn,
        #     iam_roles=[rs_role.role_arn],
        #     admin_username=redshift_config['admin_username'],
        #     admin_user_password=redshift_password.secret_value_from_json("password").unsafe_unwrap(),
        # )

        # self.rs_workgroup = _rs.CfnWorkgroup(
        #     self,
        #     "redshiftServerlessWorkgroup",
        #     workgroup_name=redshift_config['workgroup_name'],
        #     base_capacity=32,
        #     namespace_name=self.rs_namespace.ref,
        #     security_group_ids=[rs_security_group.security_group_id],
        #     subnet_ids=vpc.select_subnets(
        #         subnet_type=_ec2.SubnetType.PUBLIC
        #     ).subnet_ids,
        # )

        lambda_layer = _lambda.LayerVersion(self, 
            'refreshmv-lambda-layer',
            code = _lambda.AssetCode('lambda/layer/python.zip'),
            compatible_runtimes = [_lambda.Runtime.PYTHON_3_8],
        )

        refreshmv_lambda = _lambda.Function(
            self, 'refreshmv-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='refreshmv-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/refreshmv'),
            handler='refreshmv.lambda_handler',
            layers = [lambda_layer],
            environment={
                "WORKGROUP_NAME" : redshift_config['workgroup_name'],
                "DB_NAME" : redshift_config['db_name'],
                "REFRESHMV" : redshift_config['refreshmv'],
                "SECRET_NAME": redshift_config['secret_name']

            },
            timeout=Duration.seconds(60),
            reserved_concurrent_executions=1,
        )

        refreshmv_lambda.add_to_role_policy(
            statement=_iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["redshift-data:*", "secretsmanager:GetSecretValue"],
                resources=["*"],
            )
        )

        step_trigger = _events.Rule(
            self, 'refreshmv-StepTrigger',
            schedule=_events.Schedule.rate(Duration.seconds(60))
        )

        step_trigger.add_target(
            _events_targets.LambdaFunction(refreshmv_lambda)
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
            platform_identifier=sagemaker_config['platform_identifier'],
            security_group_ids=[sg_security_group.security_group_id],
            subnet_id=vpc.select_subnets(
                subnet_type=_ec2.SubnetType.PUBLIC
            ).subnet_ids[0]
        )

        

