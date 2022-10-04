from aws_cdk import (
    Aws,
    Duration,
    Stack,
    RemovalPolicy,
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
    aws_redshiftserverless as rs,
    aws_s3 as _s3,
    aws_secretsmanager as _sm,
)
from constructs import Construct

import json

from pathlib import Path

class MasterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        environment = self.node.try_get_context('environment')
        glue_config = self.node.try_get_context(f'{environment}_glue_config')
        kinesis_config = self.node.try_get_context(f'{environment}_kinesis_config')
        redshift_config = self.node.try_get_context(f'{environment}_redshift_config')
        sagemaker_config = self.node.try_get_context(f'{environment}_sagemaker_config')

        rs_role = _iam.Role(
            self, "redshiftClusterRole",
            assumed_by=_iam.ServicePrincipal(
                "redshift.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftAllCommandsFullAccess"
                )
            ],
            role_name="RedshiftServerlessRole-AWS-Workshop"
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

        vpc = _ec2.Vpc.from_lookup(
            self,
            "VpcId",
            is_default=True
        )

        rs_security_group = _ec2.SecurityGroup.from_lookup_by_name(
            self,
            "redshiftSecurityGroup",
            security_group_name=redshift_config['security_group_name'],
            vpc=vpc
        )

        sg_security_group = _ec2.SecurityGroup(
            self,
            "sagemakerSecurityGroup",
            vpc=vpc
        )

        rs_security_group.add_ingress_rule(sg_security_group, _ec2.Port.tcp(5439))
        rs_security_group.add_ingress_rule(rs_security_group, _ec2.Port.tcp(5439))
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

        rs_namespace = rs.CfnNamespace(
            self,
            "redshiftServerlessNamespace",
            namespace_name=redshift_config['namespace_name'],
            db_name=redshift_config['db_name'],
            default_iam_role_arn=rs_role.role_arn,
            iam_roles=[rs_role.role_arn],
            admin_username=redshift_config['admin_username'],
            admin_user_password='Password123',
        )

        rs_workgroup = rs.CfnWorkgroup(
            self,
            "redshiftServerlessWorkgroup",
            workgroup_name=redshift_config['workgroup_name'],
            base_capacity=32,
            publicly_accessible=True,
            namespace_name=rs_namespace.ref,
            security_group_ids=[rs_security_group.security_group_id],
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
            ).subnet_ids[1]
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

        order_stream = _kinesis.Stream(
            self,
            "order-stream",
            stream_name="order_stream",
            retention_period=Duration.hours(kinesis_config['retention_period']),
            stream_mode=_kinesis.StreamMode.ON_DEMAND,
            encryption=_kinesis.StreamEncryption.UNENCRYPTED
        )

        s3_bucket_raw.grant_read_write(rs_role)
        order_stream.grant_read(rs_role)

        dynamodb_table = _dynamodb.Table(
            self, "Table",
            table_name='latest_key',
            partition_key=_dynamodb.Attribute(name="id", type=_dynamodb.AttributeType.NUMBER),
            billing_mode=_dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )

        lambda_layer = _lambda.LayerVersion(self, 
            'lambda-layer',
            code = _lambda.AssetCode('lambda/layer/python.zip'),
            compatible_runtimes = [_lambda.Runtime.PYTHON_3_8],
        )

        order_lambda = _lambda.Function(
            self, 'order-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='order-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/order'),
            handler='order_producer.lambda_handler',
            layers = [lambda_layer],
            environment={
                "LOG_LEVEL": "INFO",
                "STREAM_NAME": f"order_stream"
            },
            timeout=Duration.seconds(60),
            reserved_concurrent_executions=1,
        )

        order_stream.grant_read_write(order_lambda)
        dynamodb_table.grant_read_write_data(order_lambda)


        step_trigger = _events.Rule(
            self, 'StepTrigger',
            schedule=_events.Schedule.rate(Duration.seconds(60))
        )
        
        step_trigger.add_target(
            _events_targets.LambdaFunction(order_lambda)
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

        csv_classifier = _glue.CfnClassifier(self, "csv_Classifier",
            csv_classifier=_glue.CfnClassifier.CsvClassifierProperty(
                allow_single_column=False,
                contains_header="PRESENT",
                delimiter=",",
                quote_symbol='"'
            )
        )

        # glue database for the tables
        database = _glue.CfnDatabase(
            self,
            "database",
            catalog_id=Aws.ACCOUNT_ID,
            database_input=_glue.CfnDatabase.DatabaseInputProperty(
                name=glue_config['glue_db']
            ),
        )
        database.apply_removal_policy(policy=RemovalPolicy.DESTROY)

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
            database_name=glue_config['glue_db'],
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