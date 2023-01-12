from aws_cdk import (
    Aws,
    Duration,
    Stack,
    RemovalPolicy,
    CfnOutput,
    aws_s3 as _s3,
    aws_s3_deployment as _s3_deploy,
    custom_resources as _cr,
    aws_glue as _glue,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb,
    aws_kinesis as _kinesis,
    aws_logs as _logs,
    aws_events as _events,
    aws_events_targets as _events_targets
)
from constructs import Construct

from pathlib import Path

class IngestionStack(Stack):

    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 glue_database_name,
                 kinesis_retention_period,
                 kinesis_stream_mode,
                 kinesis_encryption,
                 dynamodb_billing_mode,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        consignment_stream = _kinesis.Stream(
            self,
            "consignment_stream",
            stream_name="consignment_stream",
            retention_period=Duration.hours(kinesis_retention_period),
            stream_mode=kinesis_stream_mode,
            encryption=kinesis_encryption,
        )

        dynamodb_table = _dynamodb.Table(
            self, "Table",
            table_name='latest_key',
            partition_key=_dynamodb.Attribute(
                name="id", type=_dynamodb.AttributeType.NUMBER),
            billing_mode=dynamodb_billing_mode,
            removal_policy=RemovalPolicy.DESTROY
        )

        lambdaLayer = _lambda.LayerVersion(self, 'lambda-layer',
                                           code=_lambda.AssetCode(
                                               'lambda/layer/'),
                                           compatible_runtimes=[
                                               _lambda.Runtime.PYTHON_3_8],
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
            layers=[lambdaLayer],
            environment={
                "LOG_LEVEL": "INFO",
                "STREAM_NAME": f"{consignment_stream.stream_name}"
            },
            timeout=Duration.seconds(60),
        )

        consignment_stream.grant_read_write(order_lambda)
        dynamodb_table.grant_read_write_data(order_lambda)

        step_trigger.add_target(
            _events_targets.LambdaFunction(order_lambda)
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
                name=glue_database_name
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

        self.consignment_stream = consignment_stream
        self.s3_bucket_raw = s3_bucket_raw

        CfnOutput(
            self,
            "S3BucketOutput",
            value=(
                f"{s3_bucket_raw.bucket_name}"
            ),
            description=f"S3 Bucket"
        )
