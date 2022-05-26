from aws_cdk import (
    Duration,
    Stack,
    RemovalPolicy,
    aws_ec2 as _ec2,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb,
    aws_kinesis as _kinesis,
    aws_logs as _logs,
    aws_events as _events,
    aws_events_targets as _events_targets
)
from constructs import Construct


class IngestionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ingestion_config = self.node.try_get_context('ingestion_config')

        self.order_stream = _kinesis.Stream(
            self,
            "order-stream",
            stream_name="order_stream",
            retention_period=Duration.hours(ingestion_config['retention_period']),
            stream_mode=_kinesis.StreamMode.ON_DEMAND,
            encryption=_kinesis.StreamEncryption.UNENCRYPTED
        )

        self.customer_stream = _kinesis.Stream(
            self,
            "customer-stream",
            stream_name="customer_stream",
            retention_period=Duration.hours(ingestion_config['retention_period']),
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

        lambdaLayer = _lambda.LayerVersion(self, 'lambda-layer',
                  code = _lambda.AssetCode('lambda/layer/'),
                  compatible_runtimes = [_lambda.Runtime.PYTHON_3_8],
        )

        customer_lambda = _lambda.Function(
            self, 'customer-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='customer-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/customer'),
            handler='customer_producer.lambda_handler',
            layers = [lambdaLayer],
            environment={
                "LOG_LEVEL": "INFO",
                "STREAM_NAME": f"{self.customer_stream.stream_name}"
            },
            timeout=Duration.seconds(60),
            reserved_concurrent_executions=1,
        )

        self.customer_stream.grant_read_write(customer_lambda)
        dynamodb_table.grant_read_write_data(customer_lambda)


        step_trigger = _events.Rule(
            self, 'StepTrigger',
            schedule=_events.Schedule.rate(Duration.seconds(60))
        )


        step_trigger.add_target(
            _events_targets.LambdaFunction(customer_lambda)
        )

        order_lambda = _lambda.Function(
            self, 'order-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='order-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/order'),
            handler='order_producer.lambda_handler',
            layers = [lambdaLayer],
            environment={
                "LOG_LEVEL": "INFO",
                "STREAM_NAME": f"{self.order_stream.stream_name}"
            },
            timeout=Duration.seconds(5),
            reserved_concurrent_executions=1,
        )

        self.order_stream.grant_read_write(order_lambda)
        dynamodb_table.grant_read_write_data(order_lambda)

        step_trigger.add_target(
            _events_targets.LambdaFunction(order_lambda)
        )

    @property
    def get_customer_stream(self):
        return self.customer_stream
    
    @property
    def get_order_stream(self):
        return self.order_stream


