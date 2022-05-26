from aws_cdk import (
    Duration,
    Stack,
    aws_stepfunctions as _sfn,
    aws_stepfunctions_tasks as _sfn_tasks,
    custom_resources as _cr,
    aws_iam as _iam,
    aws_events as _events,
    aws_events_targets as _events_targets
)
from constructs import Construct


class StepFunctionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, redshift_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        rs_cluster = redshift_stack.get_rs_cluster

        sql = '''REFRESH MATERIALIZED VIEW customer_stream;
            REFRESH MATERIALIZED VIEW order_stream;'''

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

        definition = sfn_execute_statement \
            .next(sfn_wait) \
            .next(sfn_status) \
            .next(sfn_complete
                 .when(_sfn.Condition.string_equals('$.Result.Status', 'FAILED'), sfn_execute_statement)
                 .when(_sfn.Condition.string_equals('$.Result.Status', 'NA'), sfn_failed)
                 .when(_sfn.Condition.string_equals('$.Result.Status', 'FINISHED'), sfn_execute_statement)
                 .otherwise(sfn_wait))

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
