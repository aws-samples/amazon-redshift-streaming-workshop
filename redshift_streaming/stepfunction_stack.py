from aws_cdk import (
    Duration,
    Stack,
    aws_stepfunctions as _sfn,
    aws_stepfunctions_tasks as _sfn_tasks,
    custom_resources as _cr,
    aws_iam as _iam,
    aws_events as _events,
    aws_events_targets as _events_targets,
    aws_lambda as _lambda
)
from constructs import Construct


class StepFunctionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, redshift_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaLayer = _lambda.LayerVersion(self, 'lambda-layer',
                  code = _lambda.AssetCode('lambda/layer/'),
                  compatible_runtimes = [_lambda.Runtime.PYTHON_3_8],
        )

        timer_lambda_function = _lambda.Function(
            self, 'step-function-timer-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='step-function-timer-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/stepfunction_timer'),
            handler='timer.lambda_handler',
            layers = [lambdaLayer],
            environment={
                "LOG_LEVEL": "INFO"
            },
            timeout=Duration.seconds(60),
            reserved_concurrent_executions=1,
        )

        rs_cluster = redshift_stack.get_rs_cluster

        sql = '''REFRESH MATERIALIZED VIEW order_stream;'''

        sfn_execute_statement = _sfn_tasks.CallAwsService(
            self, 'Submit',
            service='redshiftdata',
            action='executeStatement',
            result_path="$.sql_output",
            parameters={
                "ClusterIdentifier": rs_cluster.ref,
                "Database": rs_cluster.db_name,
                "DbUser": rs_cluster.master_username,
                "Sql": sql,
                "StatementName": "LoadDatatoRedshift",
                "WithEvent": True
            },
            iam_action="redshift-data:*",
            iam_resources=["*"]
        )

        sfn_wait = _sfn.Wait(
            self, 'Wait',
            time=_sfn.WaitTime.duration(Duration.seconds(5))
        )

        sfn_complete = _sfn.Choice(
            self, 'Complete'
        )

        sfn_status = _sfn_tasks.CallAwsService(
            self, 'Status',
            service='redshiftdata',
            action='describeStatement',
            result_path="$.Result",
            parameters={
                "Id.$": "$.sql_output.Id"
            },
            iam_action="redshift-data:*",
            iam_resources=["*"]
        )

        sfn_failed = _sfn.Fail(
            self, 'Fail',
            cause="Redshift Data API statement failed",
            error="$.Result.Error"
        )

        sfn_timer = _sfn_tasks.LambdaInvoke(
            self, 'Invoke Runtime Check',
            lambda_function=timer_lambda_function,
            payload=_sfn.TaskInput.from_object({
                "time": _sfn.JsonPath.string_at("$.time"),
                "desiredRuntimeSec": 50
            }),
            result_path="$.RuntimeCheckResult"
        )

        sfn_timeout = _sfn.Choice(
            self, 'Check timeout'
        )

        sfn_pass = _sfn.Succeed(
            self, 'Succeed',
            comment="Step Function ran for desired amount of time"
        )

        definition = sfn_execute_statement \
            .next(sfn_wait) \
            .next(sfn_status) \
            .next(sfn_complete
                 .when(_sfn.Condition.string_equals('$.Result.Status', 'FAILED'), sfn_timer)
                 .when(_sfn.Condition.string_equals('$.Result.Status', 'NA'), sfn_failed)
                 .when(_sfn.Condition.string_equals('$.Result.Status', 'FINISHED'), sfn_timer)
                 .otherwise(sfn_timer))
        
        sfn_timer.next(sfn_timeout
                 .when(_sfn.Condition.boolean_equals('$.RuntimeCheckResult.Payload.completeFlag', True), sfn_pass)
                 .when(_sfn.Condition.boolean_equals('$.RuntimeCheckResult.Payload.completeFlag', False), sfn_execute_statement)
                 .otherwise(sfn_execute_statement))

        refreshmv_stepfunctions = _sfn.StateMachine(
            self, 'StepFunctions',
            definition=definition,
            timeout=Duration.seconds(60),
        )

        step_trigger = _events.Rule(
            self, 'StepTrigger',
            schedule=_events.Schedule.rate(Duration.seconds(60))
        )

        step_trigger.add_target(
            _events_targets.SfnStateMachine(refreshmv_stepfunctions)
        )

        refreshmv_stepfunctions.add_to_role_policy(
            statement=_iam.PolicyStatement(
                actions=["redshift:GetClusterCredentials"],
                resources=["*"]
            )
        )

        # aws_custom = _cr.AwsCustomResource(
        #     self, "aws-custom",
        #     on_create=_cr.AwsSdkCall(
        #         service="StepFunctions",
        #         action="startExecution",
        #         parameters={
        #             "stateMachineArn": refreshmv_stepfunctions.state_machine_arn
        #         },
        #         physical_resource_id=_cr.PhysicalResourceId.of("physicalResourceStateMachine")
        #     ),
        #     policy=_cr.AwsCustomResourcePolicy.from_sdk_calls(
        #         resources=_cr.AwsCustomResourcePolicy.ANY_RESOURCE
        #     )
        # )
