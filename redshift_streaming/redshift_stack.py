from aws_cdk import (
    Stack,
    CfnOutput,
    CfnTag,
    RemovalPolicy,
    Aws,
    aws_ec2 as _ec2,
    aws_iam as _iam,
    aws_redshift as _redshift,
    aws_secretsmanager as _sm,
    custom_resources as _cr,
)

from constructs import Construct


class RedshiftStack(Stack):

    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 consignment_stream,
                 s3_bucket_raw,
                 redshift_max_azs,
                 redshift_cluster_type,
                 redshift_number_of_nodes,
                 redshift_db_name,
                 redshift_master_username,
                 redshift_node_type,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = _ec2.Vpc(
            self,
            "VpcId",
            max_azs=redshift_max_azs,
        )

        # Create new security group to be used by redshift
        rs_security_group = _ec2.SecurityGroup(
            self,
            "redshiftSecurityGroup",
            vpc=vpc
        )

        rs_cluster_role = _iam.Role(
            self, "redshiftClusterRole",
            assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("sagemaker.amazonaws.com")),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftAllCommandsFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "SecretsManagerReadWrite"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSageMakerFullAccess"
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

        consignment_stream.grant_read_write(rs_cluster_role)
        s3_bucket_raw.grant_read_write(rs_cluster_role)

        rs_cluster_subnet_group = _redshift.CfnClusterSubnetGroup(
            self,
            "redshiftSubnetGroup",
            subnet_ids=vpc.select_subnets(
                subnet_type=_ec2.SubnetType.PRIVATE_WITH_NAT
            ).subnet_ids,
            description="Redshift Subnet Group"
        )

        rs_cluster = _redshift.CfnCluster(
            self,
            "redshiftStreamingCluster",
            cluster_type=redshift_cluster_type,
            number_of_nodes=redshift_number_of_nodes,
            db_name=redshift_db_name,
            master_username=redshift_master_username,
            master_user_password=rs_cluster_secret.secret_value.unsafe_unwrap(),
            iam_roles=[rs_cluster_role.role_arn],
            node_type=redshift_node_type,
            publicly_accessible=False,
            cluster_subnet_group_name=rs_cluster_subnet_group.ref,
            vpc_security_group_ids=[
                rs_security_group.security_group_id],
            tags=[CfnTag(
                key="GrafanaDataSource",
                value=" "
            )],
        )

        aws_custom_default_iam = _cr.AwsCustomResource(
            self, "aws-custom",
            on_create=_cr.AwsSdkCall(
                service="Redshift",
                action="modifyClusterIamRoles",
                parameters={
                    "ClusterIdentifier": rs_cluster.ref,
                    "DefaultIamRoleArn": rs_cluster_role.role_arn
                },
                physical_resource_id=_cr.PhysicalResourceId.of("physicalResourceStateMachine")
            ),
            policy=_cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=_cr.AwsCustomResourcePolicy.ANY_RESOURCE
            )
        )

        sql = f'''
        CREATE EXTERNAL SCHEMA IF NOT EXISTS ext_s3
        FROM DATA CATALOG
        DATABASE 'ext_s3'
        IAM_ROLE default;

        CREATE MODEL ml_delay_prediction
        FROM (SELECT * FROM ext_s3.consignment_train)
        TARGET probability
        FUNCTION fnc_delay_probability
        IAM_ROLE default
        SETTINGS (
            MAX_RUNTIME 1800, --seconds
            S3_BUCKET '{s3_bucket_raw.bucket_name}' 
        );

        CREATE MATERIALIZED VIEW fleet_summary AS
        SELECT vehicle_location, 
        COUNT(CASE WHEN vehicle_status = 'On the move' THEN 1 END) on_the_move, 
        COUNT(CASE WHEN vehicle_status = 'Scheduled maintenance' THEN 1 END) scheduled_maintenance,
        COUNT(CASE WHEN vehicle_status = 'Unscheduled maintenance' THEN 1 END) unscheduled_maintenance
        FROM ext_s3.fleet
        GROUP BY 1
        ;
        '''

        aws_custom_create_model = _cr.AwsCustomResource(
            self, "aws-custom-redshift-ml",
            on_create=_cr.AwsSdkCall(
                service="RedshiftData",
                action="executeStatement",
                parameters={
                    "ClusterIdentifier": rs_cluster.ref,
                    "Database": rs_cluster.db_name,
                    "DbUser": rs_cluster.master_username,
                    "Sql": sql,
                    "StatementName": "CreateRedshiftMLModel",
                    "WithEvent": True
                },
                physical_resource_id=_cr.PhysicalResourceId.of("physicalResourceStateMachine")
            ),
            policy=_cr.AwsCustomResourcePolicy.from_statements(
                statements=[_iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=[
                        "redshift:GetClusterCredentials",
                        "redshift-serverless:GetCredentials",
                        "redshift-data:ExecuteStatement",
                    ],
                    resources=["*"]
                )]
            )
            
        )

        aws_custom_create_model.node.add_dependency(aws_custom_default_iam)

        self.rs_cluster = rs_cluster
        self.rs_security_group = rs_security_group
        self.rs_cluster_role = rs_cluster_role
        self.vpc = vpc

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
