from aws_cdk import (
    Aws,
    Duration,
    Stack,
    RemovalPolicy,
    aws_cloud9 as _c9,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb,
    aws_logs as _logs,
    aws_ec2 as _ec2,
    aws_sagemaker as _sg,
    custom_resources as _cr,
    aws_events as _events,
    aws_glue as _glue,
    aws_events_targets as _events_targets,
    aws_s3_deployment as _s3_deploy,
    aws_kinesis as _kinesis,
    aws_redshiftserverless as _rss,
    aws_redshift as _rs,
    aws_s3 as _s3,
    aws_rds as _rds,
    aws_secretsmanager as _sm,
    aws_msk as _msk,
    SecretValue
)
from constructs import Construct

import json

from pathlib import Path

class MasterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        environment = self.node.try_get_context('environment')
        redshift_config = self.node.try_get_context(f'{environment}_redshift_config')
        kinesis_retention_period=72
        kinesis_stream_mode=_kinesis.StreamMode.ON_DEMAND
        kinesis_encryption=_kinesis.StreamEncryption.UNENCRYPTED
        kinesis_stream_name="consignment_stream"
        dynamodb_billing_mode=_dynamodb.BillingMode.PAY_PER_REQUEST
        glue_database_name="ext_s3"
        rs_security_group_name="default"
        rs_admin_username="admin"
        rs_workgroup_name="default-wg"
        rs_namespace_name="default-ns"
        rs_db_name="dev"
        rs_admin_password="Welcome!123"
        msk_cluster_name = "workshop-cluster"
        
        vpc = _ec2.Vpc.from_lookup(
            self,
            "VpcId",
            is_default=True
        )

        rs_security_group = _ec2.SecurityGroup.from_lookup_by_name(
            self,
            "redshiftSecurityGroup",
            security_group_name=rs_security_group_name,
            vpc=vpc
        )

        sg_security_group = _ec2.SecurityGroup(
            self,
            "sagemakerSecurityGroup",
            vpc=vpc
        )

        pg_security_group = _ec2.SecurityGroup(
            self,
            "postgresSecurityGroup",
            vpc=vpc
        )

        qs_security_group = _ec2.SecurityGroup(
            self,
            "QuicksightSecurityGroup",
            vpc=vpc
        )
        
        qs_security_group.add_ingress_rule(
            peer=rs_security_group,
            connection=_ec2.Port.all_traffic()
        )

        pg_security_group.add_ingress_rule(rs_security_group,_ec2.Port.all_traffic())
        pg_security_group.add_ingress_rule(pg_security_group,_ec2.Port.all_traffic())
        pg_security_group.add_ingress_rule(sg_security_group,_ec2.Port.tcp(5432))

        rs_security_group.add_ingress_rule(rs_security_group, _ec2.Port.all_traffic())
        rs_security_group.add_ingress_rule(pg_security_group, _ec2.Port.all_traffic())
        rs_security_group.add_ingress_rule(sg_security_group, _ec2.Port.tcp(5439))
        rs_security_group.add_ingress_rule(qs_security_group, _ec2.Port.tcp(5439))

        #us-east-2
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4('52.15.247.160/27'), 
            _ec2.Port.tcp(5439)
        )
        #us-east-1
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4('52.23.63.224/27'), 
            _ec2.Port.tcp(5439)
        )
        #us-west-2
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4('54.70.204.128/27'), 
            _ec2.Port.tcp(5439)
        )
        #ap-southeast-2
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4('54.153.249.96/27'), 
            _ec2.Port.tcp(5439)
        )
        #ap-northeast-1
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4('13.113.244.32/27'), 
            _ec2.Port.tcp(5439)
        )
        #eu-west-1
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4('52.210.255.224/27'), 
            _ec2.Port.tcp(5439)
        )
        #eu-west-2
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4('35.177.218.0/27'), 
            _ec2.Port.tcp(5439)
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

        redshift_credentials = _sm.Secret(
            self,
            "redshift_credentials",
            description="Redshift credentials",
            secret_string_value=SecretValue.unsafe_plain_text(
                json.dumps({'username':rs_admin_username, 
                'password':rs_admin_password})
                ),
            removal_policy=RemovalPolicy.DESTROY,
        )
        
        rs_role = _iam.Role(
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

        rs_namespace = _rss.CfnNamespace(
            self,
            "redshiftServerlessNamespace",
            namespace_name=rs_namespace_name,
            db_name=rs_db_name,
            default_iam_role_arn=rs_role.role_arn,
            iam_roles=[rs_role.role_arn],
            admin_username=rs_admin_username,
            admin_user_password=rs_admin_password,
        )

        rs_workgroup = _rss.CfnWorkgroup(
            self,
            "redshiftServerlessWorkgroup",
            workgroup_name=rs_workgroup_name,
            base_capacity=32,
            publicly_accessible=True,
            namespace_name=rs_namespace.ref,
            security_group_ids=[rs_security_group.security_group_id],
        )
        
        s3_bucket_raw = _s3.Bucket(
            self,
            "s3_raw",
            encryption=_s3.BucketEncryption.S3_MANAGED,
            public_read_access=False,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        _s3_deploy.BucketDeployment(
            self,
            "s3_deploy_raw",
            destination_bucket=s3_bucket_raw,
            sources=[
                _s3_deploy.Source.asset(
                    str(Path(__file__).parent.parent.joinpath("assets/data"))
                )
            ],
        )
        
        s3_bucket_raw.grant_read_write(rs_role)
        
        # glue database for the tables
        database = _glue.CfnDatabase(
            self,
            "database",
            catalog_id=Aws.ACCOUNT_ID,
            database_input=_glue.CfnDatabase.DatabaseInputProperty(
                name=glue_database_name
            ),
        )
        database.apply_removal_policy(policy=RemovalPolicy.DESTROY)
        
        init_sql = f'''
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
        lambda_layer = _lambda.LayerVersion(self, 
            'lambda-layer',
            code = _lambda.AssetCode('lambda/layer/python.zip'),
            compatible_runtimes = [_lambda.Runtime.PYTHON_3_8],
        )
        
        initsql_lambda = _lambda.Function(
            self, 'initsql-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='initsql-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/initsql'),
            handler='initsql.lambda_handler',
            layers = [lambda_layer],
            environment={
                "WORKGROUP_NAME" : rs_workgroup_name,
                "DB_NAME" : rs_db_name,
                "SQL" : init_sql,
                "SECRET_ARN": redshift_credentials.secret_full_arn,
            },
            timeout=Duration.seconds(60),
            reserved_concurrent_executions=1,
        )

        initsql_lambda.add_to_role_policy(
            statement=_iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["redshift-data:*", "secretsmanager:*"],
                resources=["*"],
            )
        )
        
        aws_custom_initsql = _cr.AwsCustomResource(
            self, "aws-custom-initsql",
            on_create=_cr.AwsSdkCall(
                service="Lambda",
                action="invoke",
                parameters={
                    "FunctionName": initsql_lambda.function_name
                },
                physical_resource_id=_cr.PhysicalResourceId.of("physicalResourceStateMachine")
            ),
            policy=_cr.AwsCustomResourcePolicy.from_statements(
                statements=[_iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=["lambda:InvokeFunction"],
                    resources=["*"]
                )]
            )
        ) 
        
        
        aws_custom_initsql.node.add_dependency(rs_workgroup)
        aws_custom_initsql.node.add_dependency(database)
        
        # aws_custom_create_model = _cr.AwsCustomResource(
        #     self, "aws-custom-redshift-ml",
        #     install_latest_aws_sdk=True,
        #     on_create=_cr.AwsSdkCall(
        #         service="RedshiftData",
        #         action="executeStatement",
        #         parameters={
        #             "WorkgroupName": rs_workgroup_name,
        #             "SecretArn": redshift_credentials.secret_arn,
        #             "Database": rs_db_name,
        #             "Sql": init_sql,
        #         },
        #         physical_resource_id=_cr.PhysicalResourceId.of("physicalResourceStateMachine")
        #     ),
        #     policy=_cr.AwsCustomResourcePolicy.from_statements(
        #         statements=[_iam.PolicyStatement(
        #             effect=_iam.Effect.ALLOW,
        #             actions=[
        #                 "secretsmanager:*",
        #                 "redshift-data:*",
        #             ],
        #             resources=["*"]
        #         )]
        #     )
            
        # )
        
        # aws_custom_create_model.node.add_dependency(rs_workgroup)
        # aws_custom_create_model.node.add_dependency(database)

        consignment_stream = _kinesis.Stream(
            self,
            "consignment_stream",
            stream_name=kinesis_stream_name,
            retention_period=Duration.hours(kinesis_retention_period),
            stream_mode=kinesis_stream_mode,
            encryption=kinesis_encryption,
        )
        
        consignment_stream.grant_read(rs_role)

        dynamodb_table = _dynamodb.Table(
            self, "Table",
            table_name='latest_key',
            partition_key=_dynamodb.Attribute(
                name="id", type=_dynamodb.AttributeType.NUMBER),
            billing_mode=dynamodb_billing_mode,
            removal_policy=RemovalPolicy.DESTROY
        )

        
        step_trigger = _events.Rule(
            self, 'StepTrigger',
            schedule=_events.Schedule.rate(Duration.seconds(60))
        )

        order_lambda = _lambda.Function(
            self, 'order-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='order-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/order'),
            handler='order_producer.lambda_handler',
            layers=[lambda_layer],
            environment={
                "LOG_LEVEL": "INFO",
                "STREAM_NAME": kinesis_stream_name
            },
            timeout=Duration.seconds(60),
        )

        consignment_stream.grant_read_write(order_lambda)
        dynamodb_table.grant_read_write_data(order_lambda)

        step_trigger.add_target(
            _events_targets.LambdaFunction(order_lambda)
        )

        csv_classifier = _glue.CfnClassifier(self, "csv_Classifier",
            csv_classifier=_glue.CfnClassifier.CsvClassifierProperty(
                allow_single_column=False,
                contains_header="PRESENT",
                delimiter=",",
                quote_symbol='"'
            )
        )
        # glue crawler role
        crawler_role = _iam.Role(
            self,
            "crawler_role",
            assumed_by=_iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSGlueServiceRole"
                )
            ],
        )

        s3_bucket_raw.grant_read_write(crawler_role)
        
        # the raw bucket crawler
        crawler_raw = _glue.CfnCrawler(
            self,
            "crawler_raw",
            targets=_glue.CfnCrawler.TargetsProperty(
                s3_targets=[
                    _glue.CfnCrawler.S3TargetProperty(path=s3_bucket_raw.bucket_name)
                ],
            ),
            database_name=glue_database_name,
            role=crawler_role.role_name,
            classifiers=[csv_classifier.ref]
        )

        aws_custom = _cr.AwsCustomResource(
            self, "aws-custom",
            on_update=_cr.AwsSdkCall(
                service="Glue",
                action="startCrawler",
                parameters={
                    "Name": crawler_raw.ref
                },
                physical_resource_id=_cr.PhysicalResourceId.of("physicalResourceStateMachine")
            ),
            policy=_cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=_cr.AwsCustomResourcePolicy.ANY_RESOURCE
            )
        ) 
        
        
        rs_sql = '''REFRESH MATERIALIZED VIEW consignment_stream;
        REFRESH MATERIALIZED VIEW consignment_transformed;
        INSERT INTO consignment_predictions
        WITH consignment_delta as (
            SELECT ct.*
            FROM consignment_transformed ct
            LEFT JOIN consignment_predictions cp 
            ON ct.consignment_id = cp.consignment_id 
            WHERE cp.consignment_id IS NULL
        )
        SELECT *, fnc_delay_probability(
        day_of_week, "hour", days_to_deliver, delivery_distance) delay_probability
        FROM consignment_delta;
        '''
        
        
        
        refreshmv_lambda = _lambda.Function(
            self, 'refreshmv-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='refreshmv-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/refreshmv'),
            handler='refreshmv.lambda_handler',
            layers = [lambda_layer],
            environment={
                "WORKGROUP_NAME" : rs_workgroup_name,
                "DB_NAME" : rs_db_name,
                "SQL" : rs_sql,
                "SECRET_ARN": redshift_credentials.secret_full_arn,
            },
            timeout=Duration.seconds(60),
            reserved_concurrent_executions=1,
        )

        refreshmv_lambda.add_to_role_policy(
            statement=_iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["redshift-data:*", "secretsmanager:*"],
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
        
        
        
        
        # Create MSK Serverless cluster
        msk_serverless_cluster = _msk.CfnServerlessCluster(self, "MSKServerlessCluster",
            client_authentication = _msk.CfnServerlessCluster.ClientAuthenticationProperty(
                sasl=_msk.CfnServerlessCluster.SaslProperty(
                    iam=_msk.CfnServerlessCluster.IamProperty(
                        enabled=True
                    )
                 )
            ),
            cluster_name=msk_cluster_name,
            vpc_configs=[_msk.CfnServerlessCluster.VpcConfigProperty(
                subnet_ids=vpc.select_subnets(subnet_type=_ec2.SubnetType.PUBLIC).subnet_ids
            )]
        )

        # Create IAM policy for MSK
        msk_serverless_policy = _iam.ManagedPolicy(self, "MskServerlessWorkshopPolicy",
            statements=[
                _iam.PolicyStatement(
                    effect = _iam.Effect.ALLOW,
                    actions=["kafka-cluster:Connect", "kafka-cluster:AlterCluster", "kafka-cluster:DescribeCluster"],
                    resources=[f"arn:aws:kafka:{Aws.REGION}:{Aws.ACCOUNT_ID}:cluster/{msk_cluster_name}/*"]
                ),
                _iam.PolicyStatement(
                    effect = _iam.Effect.ALLOW,
                    actions=["kafka-cluster:*Topic*", "kafka-cluster:WriteData", "kafka-cluster:ReadData"],
                    resources=[f"arn:aws:kafka:{Aws.REGION}:{Aws.ACCOUNT_ID}:topic/{msk_cluster_name}/*"]
                ),
                _iam.PolicyStatement(
                    effect = _iam.Effect.ALLOW,
                    actions=["kafka-cluster:AlterGroup", "kafka-cluster:DescribeGroup"],
                    resources=[f"arn:aws:kafka:{Aws.REGION}:{Aws.ACCOUNT_ID}:group/{msk_cluster_name}/*"]
                ),
                
            ]
        )
            
        # Create IAM role
        msk_serverless_role = _iam.Role(
            self, "MskServerlessRole",
            assumed_by=_iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[msk_serverless_policy]
        )
