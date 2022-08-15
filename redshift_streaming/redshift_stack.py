from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    Aws,
    aws_ec2 as _ec2,
    aws_iam as _iam,
    aws_redshift as _redshift,
    aws_secretsmanager as _sm,
)

from constructs import Construct

class RedshiftStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, ingestion_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        redshift_config = self.node.try_get_context('redshift_config')

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

        rs_cluster_role = _iam.Role(
            self, "redshiftClusterRole",
            assumed_by=_iam.ServicePrincipal(
                "redshift.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftAllCommandsFullAccess"
                )
            ]
        )

        rs_cluster_secret = _sm.Secret(
            self,
            "RedshiftSecretPassword",
            description="Redshift admin credentials",
            secret_name="RedshiftSecret",
            generate_secret_string=_sm.SecretStringGenerator(
                exclude_punctuation=True),
            removal_policy=RemovalPolicy.DESTROY
        )

        _iam.ManagedPolicy(
            self,
            "redshiftSpectrumPolicy",
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
                        "lakeformation:GetDataAccess"
                    ],
                    resources=["*"]
                )
            ],
            roles=[
                rs_cluster_role
            ]
        )

        customer_stream = ingestion_stack.get_customer_stream
        order_stream = ingestion_stack.get_order_stream

        order_stream.grant_read_write(rs_cluster_role)
        customer_stream.grant_read_write(rs_cluster_role)

        rs_cluster_subnet_group = _redshift.CfnClusterSubnetGroup(
            self,
            "redshiftSubnetGroup",
            subnet_ids=vpc.select_subnets(
                subnet_type=_ec2.SubnetType.PRIVATE_WITH_NAT
            ).subnet_ids,
            description="Redshift Subnet Group"
        )

        self.rs_cluster = _redshift.CfnCluster(
            self,
            "redshiftStreamingCluster",
            cluster_type=redshift_config['cluster_type'],
            number_of_nodes=redshift_config['number_of_nodes'],
            db_name=redshift_config['db_name'],
            master_username=redshift_config['master_username'],
            master_user_password=rs_cluster_secret.secret_value.unsafe_unwrap(),
            iam_roles=[rs_cluster_role.role_arn],
            node_type=redshift_config['node_type'],
            publicly_accessible=False,
            cluster_subnet_group_name=rs_cluster_subnet_group.ref,
            vpc_security_group_ids=[
                rs_security_group.security_group_id]
        )

        CfnOutput(
            self,
            "RedshiftCluster",
            value=f"{self.rs_cluster.attr_endpoint_address}",
            description=f"RedshiftCluster Endpoint"
        )
        CfnOutput(
            self,
            "RedshiftClusterPassword",
            value=(
                f"https://console.aws.amazon.com/secretsmanager/home?region="
                f"{Aws.REGION}"
                f"#/secret?name="
                f"{rs_cluster_secret.secret_arn}"
            ),
            description=f"Redshift Cluster Password in Secrets Manager"
        )
        CfnOutput(
            self,
            "RedshiftIAMRole",
            value=(
                f"{rs_cluster_role.role_arn}"
            ),
            description=f"Redshift Cluster IAM Role Arn"
        )

    @property
    def get_rs_cluster(self):
        return self.rs_cluster
