from aws_cdk import (
    Duration,
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb,
    aws_kinesis as _kinesis,
    aws_logs as _logs,
    aws_events as _events,
    aws_events_targets as _events_targets,
    aws_s3 as _s3,
    aws_s3_deployment as _s3_deploy,
)
from constructs import Construct

from pathlib import Path

class IngestionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        environment = self.node.try_get_context('environment')
        kinesis_config = self.node.try_get_context(f'{environment}_kinesis_config')

        self.order_stream = _kinesis.Stream(
            self,
            "order-stream",
            stream_name="order_stream",
            retention_period=Duration.hours(kinesis_config['retention_period']),
            stream_mode=_kinesis.StreamMode.ON_DEMAND,
            encryption=_kinesis.StreamEncryption.UNENCRYPTED
        )

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
                "STREAM_NAME": f"{self.order_stream.stream_name}"
            },
            timeout=Duration.seconds(60),
            reserved_concurrent_executions=1,
        )

        self.order_stream.grant_read_write(order_lambda)
        dynamodb_table.grant_read_write_data(order_lambda)

        

        step_trigger = _events.Rule(
            self, 'StepTrigger',
            schedule=_events.Schedule.rate(Duration.seconds(60))
        )
        
        step_trigger.add_target(
            _events_targets.LambdaFunction(order_lambda)
        )

        self.s3_bucket_raw = _s3.Bucket(
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
            destination_bucket=self.s3_bucket_raw,
            sources=[
                _s3_deploy.Source.asset(
                    str(Path(__file__).parent.parent.joinpath("assets/data"))
                )
            ],
        )

    @property
    def get_s3_bucket_raw(self):
        return self.s3_bucket_raw 
    
    @property
    def get_order_stream(self):
        return self.order_stream


