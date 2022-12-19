'''
# AWS::Scheduler Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_scheduler as scheduler
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Scheduler construct libraries](https://constructs.dev/search?q=scheduler)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Scheduler resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Scheduler.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Scheduler](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Scheduler.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnSchedule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule",
):
    '''A CloudFormation ``AWS::Scheduler::Schedule``.

    :cloudformationResource: AWS::Scheduler::Schedule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_scheduler as scheduler
        
        # tags: Any
        
        cfn_schedule = scheduler.CfnSchedule(self, "MyCfnSchedule",
            flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                mode="mode",
        
                # the properties below are optional
                maximum_window_in_minutes=123
            ),
            schedule_expression="scheduleExpression",
            target=scheduler.CfnSchedule.TargetProperty(
                arn="arn",
                role_arn="roleArn",
        
                # the properties below are optional
                dead_letter_config=scheduler.CfnSchedule.DeadLetterConfigProperty(
                    arn="arn"
                ),
                ecs_parameters=scheduler.CfnSchedule.EcsParametersProperty(
                    task_definition_arn="taskDefinitionArn",
        
                    # the properties below are optional
                    capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                        capacity_provider="capacityProvider",
        
                        # the properties below are optional
                        base=123,
                        weight=123
                    )],
                    enable_ecs_managed_tags=False,
                    enable_execute_command=False,
                    group="group",
                    launch_type="launchType",
                    network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                        awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                            subnets=["subnets"],
        
                            # the properties below are optional
                            assign_public_ip="assignPublicIp",
                            security_groups=["securityGroups"]
                        )
                    ),
                    placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                        expression="expression",
                        type="type"
                    )],
                    placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                        field="field",
                        type="type"
                    )],
                    platform_version="platformVersion",
                    propagate_tags="propagateTags",
                    reference_id="referenceId",
                    tags=tags,
                    task_count=123
                ),
                event_bridge_parameters=scheduler.CfnSchedule.EventBridgeParametersProperty(
                    detail_type="detailType",
                    source="source"
                ),
                input="input",
                kinesis_parameters=scheduler.CfnSchedule.KinesisParametersProperty(
                    partition_key="partitionKey"
                ),
                retry_policy=scheduler.CfnSchedule.RetryPolicyProperty(
                    maximum_event_age_in_seconds=123,
                    maximum_retry_attempts=123
                ),
                sage_maker_pipeline_parameters=scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                    pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                        name="name",
                        value="value"
                    )]
                ),
                sqs_parameters=scheduler.CfnSchedule.SqsParametersProperty(
                    message_group_id="messageGroupId"
                )
            ),
        
            # the properties below are optional
            description="description",
            end_date="endDate",
            group_name="groupName",
            kms_key_arn="kmsKeyArn",
            name="name",
            schedule_expression_timezone="scheduleExpressionTimezone",
            start_date="startDate",
            state="state"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        flexible_time_window: typing.Union[typing.Union["CfnSchedule.FlexibleTimeWindowProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        schedule_expression: builtins.str,
        target: typing.Union[typing.Union["CfnSchedule.TargetProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        schedule_expression_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Scheduler::Schedule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param flexible_time_window: ``AWS::Scheduler::Schedule.FlexibleTimeWindow``.
        :param schedule_expression: ``AWS::Scheduler::Schedule.ScheduleExpression``.
        :param target: ``AWS::Scheduler::Schedule.Target``.
        :param description: ``AWS::Scheduler::Schedule.Description``.
        :param end_date: ``AWS::Scheduler::Schedule.EndDate``.
        :param group_name: ``AWS::Scheduler::Schedule.GroupName``.
        :param kms_key_arn: ``AWS::Scheduler::Schedule.KmsKeyArn``.
        :param name: ``AWS::Scheduler::Schedule.Name``.
        :param schedule_expression_timezone: ``AWS::Scheduler::Schedule.ScheduleExpressionTimezone``.
        :param start_date: ``AWS::Scheduler::Schedule.StartDate``.
        :param state: ``AWS::Scheduler::Schedule.State``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__503b74ac170f15626de2456b6f8c40d2cdc1ab21574c821e051517099f516ea4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduleProps(
            flexible_time_window=flexible_time_window,
            schedule_expression=schedule_expression,
            target=target,
            description=description,
            end_date=end_date,
            group_name=group_name,
            kms_key_arn=kms_key_arn,
            name=name,
            schedule_expression_timezone=schedule_expression_timezone,
            start_date=start_date,
            state=state,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__859c33780944a757aa0069dfe861a7f9ee3aaa6d51b1881276590d23b3cbc11d)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c9dd58f37a9f244d09bdbca3ac4ea0869a0855a2cb760325d51c0d8beed730d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flexibleTimeWindow")
    def flexible_time_window(
        self,
    ) -> typing.Union["CfnSchedule.FlexibleTimeWindowProperty", _IResolvable_da3f097b]:
        '''``AWS::Scheduler::Schedule.FlexibleTimeWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-flexibletimewindow
        '''
        return typing.cast(typing.Union["CfnSchedule.FlexibleTimeWindowProperty", _IResolvable_da3f097b], jsii.get(self, "flexibleTimeWindow"))

    @flexible_time_window.setter
    def flexible_time_window(
        self,
        value: typing.Union["CfnSchedule.FlexibleTimeWindowProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__596e14fe3c5d30f5608996086027eaf3ff49cf0205d5a551a9e0895e2be75f2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flexibleTimeWindow", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> builtins.str:
        '''``AWS::Scheduler::Schedule.ScheduleExpression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-scheduleexpression
        '''
        return typing.cast(builtins.str, jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a3656a00e3dadf75b2e58b2162ed9850cd46df81630349120c362c216f94db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpression", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> typing.Union["CfnSchedule.TargetProperty", _IResolvable_da3f097b]:
        '''``AWS::Scheduler::Schedule.Target``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-target
        '''
        return typing.cast(typing.Union["CfnSchedule.TargetProperty", _IResolvable_da3f097b], jsii.get(self, "target"))

    @target.setter
    def target(
        self,
        value: typing.Union["CfnSchedule.TargetProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9658077cef2602ca00d25f391105ce442d6a0a3efef1ca5be55db053ede80a78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5864139b51db95ec1c3e6c947b577675bb4f83133b1f5476864d71c4009c2386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.EndDate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-enddate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endDate"))

    @end_date.setter
    def end_date(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3d0ae7ef525e3a588544a09eb7ec3271c357974ae47f41180a7aeb9086e2594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endDate", value)

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.GroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-groupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1860ec4ad4204d90b7f2756ff633582f92f7f97d174b16a7da8e36811ebdc98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.KmsKeyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-kmskeyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c65947df9a6be40d839d971ea07ff6a85493b9cfbab03c61fc17e54bdd0e9276)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb6bd8d80ac829e96128e011c87e852bfea080bdcd859bfdf98c7874542dc1b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.ScheduleExpressionTimezone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-scheduleexpressiontimezone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpressionTimezone"))

    @schedule_expression_timezone.setter
    def schedule_expression_timezone(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb337d25b9d34da19dbe88b72514ea1e1e7a235cd91b7597abecd038498e11a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpressionTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.StartDate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-startdate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startDate"))

    @start_date.setter
    def start_date(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38fc94567c401ce05bf3ed2461327df25f05b71764228be5a3f95fec0573d007)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startDate", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986ef975482735e4fbf46592da626ebfd4ca9636ad053fe886d40f9856d1483e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.AwsVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "subnets": "subnets",
            "assign_public_ip": "assignPublicIp",
            "security_groups": "securityGroups",
        },
    )
    class AwsVpcConfigurationProperty:
        def __init__(
            self,
            *,
            subnets: typing.Sequence[builtins.str],
            assign_public_ip: typing.Optional[builtins.str] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param subnets: ``CfnSchedule.AwsVpcConfigurationProperty.Subnets``.
            :param assign_public_ip: ``CfnSchedule.AwsVpcConfigurationProperty.AssignPublicIp``.
            :param security_groups: ``CfnSchedule.AwsVpcConfigurationProperty.SecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                aws_vpc_configuration_property = scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                    subnets=["subnets"],
                
                    # the properties below are optional
                    assign_public_ip="assignPublicIp",
                    security_groups=["securityGroups"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4be9629f7b1d55fb08861d6713480d5fa198e6e40012bcf701a627e532032afb)
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
                check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnets": subnets,
            }
            if assign_public_ip is not None:
                self._values["assign_public_ip"] = assign_public_ip
            if security_groups is not None:
                self._values["security_groups"] = security_groups

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnSchedule.AwsVpcConfigurationProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def assign_public_ip(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.AwsVpcConfigurationProperty.AssignPublicIp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-assignpublicip
            '''
            result = self._values.get("assign_public_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSchedule.AwsVpcConfigurationProperty.SecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.CapacityProviderStrategyItemProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capacity_provider": "capacityProvider",
            "base": "base",
            "weight": "weight",
        },
    )
    class CapacityProviderStrategyItemProperty:
        def __init__(
            self,
            *,
            capacity_provider: builtins.str,
            base: typing.Optional[jsii.Number] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param capacity_provider: ``CfnSchedule.CapacityProviderStrategyItemProperty.CapacityProvider``.
            :param base: ``CfnSchedule.CapacityProviderStrategyItemProperty.Base``.
            :param weight: ``CfnSchedule.CapacityProviderStrategyItemProperty.Weight``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                capacity_provider_strategy_item_property = scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                    capacity_provider="capacityProvider",
                
                    # the properties below are optional
                    base=123,
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d8897162eaa13dfb81dc83e782d5936ed604f09ed623574ad9d0fabc4a1ab7e)
                check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
                check_type(argname="argument base", value=base, expected_type=type_hints["base"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "capacity_provider": capacity_provider,
            }
            if base is not None:
                self._values["base"] = base
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def capacity_provider(self) -> builtins.str:
            '''``CfnSchedule.CapacityProviderStrategyItemProperty.CapacityProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-capacityprovider
            '''
            result = self._values.get("capacity_provider")
            assert result is not None, "Required property 'capacity_provider' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base(self) -> typing.Optional[jsii.Number]:
            '''``CfnSchedule.CapacityProviderStrategyItemProperty.Base``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-base
            '''
            result = self._values.get("base")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''``CfnSchedule.CapacityProviderStrategyItemProperty.Weight``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityProviderStrategyItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.DeadLetterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class DeadLetterConfigProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''
            :param arn: ``CfnSchedule.DeadLetterConfigProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                dead_letter_config_property = scheduler.CfnSchedule.DeadLetterConfigProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__147909ee33401019ceeec9c9c260dd3ac0812db04c597e1b63c26f0608f61069)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.DeadLetterConfigProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html#cfn-scheduler-schedule-deadletterconfig-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeadLetterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.EcsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "task_definition_arn": "taskDefinitionArn",
            "capacity_provider_strategy": "capacityProviderStrategy",
            "enable_ecs_managed_tags": "enableEcsManagedTags",
            "enable_execute_command": "enableExecuteCommand",
            "group": "group",
            "launch_type": "launchType",
            "network_configuration": "networkConfiguration",
            "placement_constraints": "placementConstraints",
            "placement_strategy": "placementStrategy",
            "platform_version": "platformVersion",
            "propagate_tags": "propagateTags",
            "reference_id": "referenceId",
            "tags": "tags",
            "task_count": "taskCount",
        },
    )
    class EcsParametersProperty:
        def __init__(
            self,
            *,
            task_definition_arn: builtins.str,
            capacity_provider_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnSchedule.CapacityProviderStrategyItemProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enable_execute_command: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            group: typing.Optional[builtins.str] = None,
            launch_type: typing.Optional[builtins.str] = None,
            network_configuration: typing.Optional[typing.Union[typing.Union["CfnSchedule.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            placement_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnSchedule.PlacementConstraintProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            placement_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnSchedule.PlacementStrategyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            platform_version: typing.Optional[builtins.str] = None,
            propagate_tags: typing.Optional[builtins.str] = None,
            reference_id: typing.Optional[builtins.str] = None,
            tags: typing.Any = None,
            task_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param task_definition_arn: ``CfnSchedule.EcsParametersProperty.TaskDefinitionArn``.
            :param capacity_provider_strategy: ``CfnSchedule.EcsParametersProperty.CapacityProviderStrategy``.
            :param enable_ecs_managed_tags: ``CfnSchedule.EcsParametersProperty.EnableECSManagedTags``.
            :param enable_execute_command: ``CfnSchedule.EcsParametersProperty.EnableExecuteCommand``.
            :param group: ``CfnSchedule.EcsParametersProperty.Group``.
            :param launch_type: ``CfnSchedule.EcsParametersProperty.LaunchType``.
            :param network_configuration: ``CfnSchedule.EcsParametersProperty.NetworkConfiguration``.
            :param placement_constraints: ``CfnSchedule.EcsParametersProperty.PlacementConstraints``.
            :param placement_strategy: ``CfnSchedule.EcsParametersProperty.PlacementStrategy``.
            :param platform_version: ``CfnSchedule.EcsParametersProperty.PlatformVersion``.
            :param propagate_tags: ``CfnSchedule.EcsParametersProperty.PropagateTags``.
            :param reference_id: ``CfnSchedule.EcsParametersProperty.ReferenceId``.
            :param tags: ``CfnSchedule.EcsParametersProperty.Tags``.
            :param task_count: ``CfnSchedule.EcsParametersProperty.TaskCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                # tags: Any
                
                ecs_parameters_property = scheduler.CfnSchedule.EcsParametersProperty(
                    task_definition_arn="taskDefinitionArn",
                
                    # the properties below are optional
                    capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                        capacity_provider="capacityProvider",
                
                        # the properties below are optional
                        base=123,
                        weight=123
                    )],
                    enable_ecs_managed_tags=False,
                    enable_execute_command=False,
                    group="group",
                    launch_type="launchType",
                    network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                        awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                            subnets=["subnets"],
                
                            # the properties below are optional
                            assign_public_ip="assignPublicIp",
                            security_groups=["securityGroups"]
                        )
                    ),
                    placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                        expression="expression",
                        type="type"
                    )],
                    placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                        field="field",
                        type="type"
                    )],
                    platform_version="platformVersion",
                    propagate_tags="propagateTags",
                    reference_id="referenceId",
                    tags=tags,
                    task_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9dc612a243a7e6a4107ac15e844d139b177440cb37d514af299c8365e71f4cf1)
                check_type(argname="argument task_definition_arn", value=task_definition_arn, expected_type=type_hints["task_definition_arn"])
                check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
                check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
                check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
                check_type(argname="argument group", value=group, expected_type=type_hints["group"])
                check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
                check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
                check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
                check_type(argname="argument placement_strategy", value=placement_strategy, expected_type=type_hints["placement_strategy"])
                check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
                check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
                check_type(argname="argument reference_id", value=reference_id, expected_type=type_hints["reference_id"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
                check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "task_definition_arn": task_definition_arn,
            }
            if capacity_provider_strategy is not None:
                self._values["capacity_provider_strategy"] = capacity_provider_strategy
            if enable_ecs_managed_tags is not None:
                self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
            if enable_execute_command is not None:
                self._values["enable_execute_command"] = enable_execute_command
            if group is not None:
                self._values["group"] = group
            if launch_type is not None:
                self._values["launch_type"] = launch_type
            if network_configuration is not None:
                self._values["network_configuration"] = network_configuration
            if placement_constraints is not None:
                self._values["placement_constraints"] = placement_constraints
            if placement_strategy is not None:
                self._values["placement_strategy"] = placement_strategy
            if platform_version is not None:
                self._values["platform_version"] = platform_version
            if propagate_tags is not None:
                self._values["propagate_tags"] = propagate_tags
            if reference_id is not None:
                self._values["reference_id"] = reference_id
            if tags is not None:
                self._values["tags"] = tags
            if task_count is not None:
                self._values["task_count"] = task_count

        @builtins.property
        def task_definition_arn(self) -> builtins.str:
            '''``CfnSchedule.EcsParametersProperty.TaskDefinitionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-taskdefinitionarn
            '''
            result = self._values.get("task_definition_arn")
            assert result is not None, "Required property 'task_definition_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def capacity_provider_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedule.CapacityProviderStrategyItemProperty", _IResolvable_da3f097b]]]]:
            '''``CfnSchedule.EcsParametersProperty.CapacityProviderStrategy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-capacityproviderstrategy
            '''
            result = self._values.get("capacity_provider_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedule.CapacityProviderStrategyItemProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def enable_ecs_managed_tags(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnSchedule.EcsParametersProperty.EnableECSManagedTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-enableecsmanagedtags
            '''
            result = self._values.get("enable_ecs_managed_tags")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_execute_command(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnSchedule.EcsParametersProperty.EnableExecuteCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-enableexecutecommand
            '''
            result = self._values.get("enable_execute_command")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def group(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.EcsParametersProperty.Group``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-group
            '''
            result = self._values.get("group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_type(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.EcsParametersProperty.LaunchType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-launchtype
            '''
            result = self._values.get("launch_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.NetworkConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.EcsParametersProperty.NetworkConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-networkconfiguration
            '''
            result = self._values.get("network_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.NetworkConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def placement_constraints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedule.PlacementConstraintProperty", _IResolvable_da3f097b]]]]:
            '''``CfnSchedule.EcsParametersProperty.PlacementConstraints``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-placementconstraints
            '''
            result = self._values.get("placement_constraints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedule.PlacementConstraintProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def placement_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedule.PlacementStrategyProperty", _IResolvable_da3f097b]]]]:
            '''``CfnSchedule.EcsParametersProperty.PlacementStrategy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-placementstrategy
            '''
            result = self._values.get("placement_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedule.PlacementStrategyProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def platform_version(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.EcsParametersProperty.PlatformVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-platformversion
            '''
            result = self._values.get("platform_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def propagate_tags(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.EcsParametersProperty.PropagateTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-propagatetags
            '''
            result = self._values.get("propagate_tags")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reference_id(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.EcsParametersProperty.ReferenceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-referenceid
            '''
            result = self._values.get("reference_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Any:
            '''``CfnSchedule.EcsParametersProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Any, result)

        @builtins.property
        def task_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnSchedule.EcsParametersProperty.TaskCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-taskcount
            '''
            result = self._values.get("task_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.EventBridgeParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"detail_type": "detailType", "source": "source"},
    )
    class EventBridgeParametersProperty:
        def __init__(self, *, detail_type: builtins.str, source: builtins.str) -> None:
            '''
            :param detail_type: ``CfnSchedule.EventBridgeParametersProperty.DetailType``.
            :param source: ``CfnSchedule.EventBridgeParametersProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                event_bridge_parameters_property = scheduler.CfnSchedule.EventBridgeParametersProperty(
                    detail_type="detailType",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0e0c05434c8347bffb5179e8c9bc22fdc3ff4fdae681d5b9d995e0f7c8c1900)
                check_type(argname="argument detail_type", value=detail_type, expected_type=type_hints["detail_type"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "detail_type": detail_type,
                "source": source,
            }

        @builtins.property
        def detail_type(self) -> builtins.str:
            '''``CfnSchedule.EventBridgeParametersProperty.DetailType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html#cfn-scheduler-schedule-eventbridgeparameters-detailtype
            '''
            result = self._values.get("detail_type")
            assert result is not None, "Required property 'detail_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''``CfnSchedule.EventBridgeParametersProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html#cfn-scheduler-schedule-eventbridgeparameters-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventBridgeParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.FlexibleTimeWindowProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mode": "mode",
            "maximum_window_in_minutes": "maximumWindowInMinutes",
        },
    )
    class FlexibleTimeWindowProperty:
        def __init__(
            self,
            *,
            mode: builtins.str,
            maximum_window_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param mode: ``CfnSchedule.FlexibleTimeWindowProperty.Mode``.
            :param maximum_window_in_minutes: ``CfnSchedule.FlexibleTimeWindowProperty.MaximumWindowInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                flexible_time_window_property = scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="mode",
                
                    # the properties below are optional
                    maximum_window_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d4dffb710d1a3208f37cc6de0f2cddceb53e1178391bdc54cfedb8ca6626ec4)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument maximum_window_in_minutes", value=maximum_window_in_minutes, expected_type=type_hints["maximum_window_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }
            if maximum_window_in_minutes is not None:
                self._values["maximum_window_in_minutes"] = maximum_window_in_minutes

        @builtins.property
        def mode(self) -> builtins.str:
            '''``CfnSchedule.FlexibleTimeWindowProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html#cfn-scheduler-schedule-flexibletimewindow-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maximum_window_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''``CfnSchedule.FlexibleTimeWindowProperty.MaximumWindowInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html#cfn-scheduler-schedule-flexibletimewindow-maximumwindowinminutes
            '''
            result = self._values.get("maximum_window_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlexibleTimeWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.KinesisParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"partition_key": "partitionKey"},
    )
    class KinesisParametersProperty:
        def __init__(self, *, partition_key: builtins.str) -> None:
            '''
            :param partition_key: ``CfnSchedule.KinesisParametersProperty.PartitionKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                kinesis_parameters_property = scheduler.CfnSchedule.KinesisParametersProperty(
                    partition_key="partitionKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__21a3b10246bef07a2f7fc56bf58e08c66b0fd77f7770804a87bf867fa8541cbb)
                check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "partition_key": partition_key,
            }

        @builtins.property
        def partition_key(self) -> builtins.str:
            '''``CfnSchedule.KinesisParametersProperty.PartitionKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html#cfn-scheduler-schedule-kinesisparameters-partitionkey
            '''
            result = self._values.get("partition_key")
            assert result is not None, "Required property 'partition_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"awsvpc_configuration": "awsvpcConfiguration"},
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            awsvpc_configuration: typing.Optional[typing.Union[typing.Union["CfnSchedule.AwsVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param awsvpc_configuration: ``CfnSchedule.NetworkConfigurationProperty.AwsvpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                network_configuration_property = scheduler.CfnSchedule.NetworkConfigurationProperty(
                    awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                        subnets=["subnets"],
                
                        # the properties below are optional
                        assign_public_ip="assignPublicIp",
                        security_groups=["securityGroups"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__428ddbfd1435a3560f182001dfcf151c620cba65c309e87341f84eb7d60ba492)
                check_type(argname="argument awsvpc_configuration", value=awsvpc_configuration, expected_type=type_hints["awsvpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if awsvpc_configuration is not None:
                self._values["awsvpc_configuration"] = awsvpc_configuration

        @builtins.property
        def awsvpc_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.AwsVpcConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.NetworkConfigurationProperty.AwsvpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html#cfn-scheduler-schedule-networkconfiguration-awsvpcconfiguration
            '''
            result = self._values.get("awsvpc_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.AwsVpcConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.PlacementConstraintProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression", "type": "type"},
    )
    class PlacementConstraintProperty:
        def __init__(
            self,
            *,
            expression: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param expression: ``CfnSchedule.PlacementConstraintProperty.Expression``.
            :param type: ``CfnSchedule.PlacementConstraintProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                placement_constraint_property = scheduler.CfnSchedule.PlacementConstraintProperty(
                    expression="expression",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb19941ef1169a4cc78daf82b7ea64663f5a28f890fbeded34448dd3f0a3c16f)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if expression is not None:
                self._values["expression"] = expression
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.PlacementConstraintProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html#cfn-scheduler-schedule-placementconstraint-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.PlacementConstraintProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html#cfn-scheduler-schedule-placementconstraint-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementConstraintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.PlacementStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"field": "field", "type": "type"},
    )
    class PlacementStrategyProperty:
        def __init__(
            self,
            *,
            field: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param field: ``CfnSchedule.PlacementStrategyProperty.Field``.
            :param type: ``CfnSchedule.PlacementStrategyProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                placement_strategy_property = scheduler.CfnSchedule.PlacementStrategyProperty(
                    field="field",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d9dc80c7a08a059d79aa3db1c44bcc28c84872422d6fd991bbca1124a384865)
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if field is not None:
                self._values["field"] = field
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.PlacementStrategyProperty.Field``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html#cfn-scheduler-schedule-placementstrategy-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.PlacementStrategyProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html#cfn-scheduler-schedule-placementstrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.RetryPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maximum_event_age_in_seconds": "maximumEventAgeInSeconds",
            "maximum_retry_attempts": "maximumRetryAttempts",
        },
    )
    class RetryPolicyProperty:
        def __init__(
            self,
            *,
            maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param maximum_event_age_in_seconds: ``CfnSchedule.RetryPolicyProperty.MaximumEventAgeInSeconds``.
            :param maximum_retry_attempts: ``CfnSchedule.RetryPolicyProperty.MaximumRetryAttempts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                retry_policy_property = scheduler.CfnSchedule.RetryPolicyProperty(
                    maximum_event_age_in_seconds=123,
                    maximum_retry_attempts=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb66e495a2f0291cd0e58a71fc127fa67ed8d10f2d977b132a1770f7b3a1f92d)
                check_type(argname="argument maximum_event_age_in_seconds", value=maximum_event_age_in_seconds, expected_type=type_hints["maximum_event_age_in_seconds"])
                check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if maximum_event_age_in_seconds is not None:
                self._values["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
            if maximum_retry_attempts is not None:
                self._values["maximum_retry_attempts"] = maximum_retry_attempts

        @builtins.property
        def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnSchedule.RetryPolicyProperty.MaximumEventAgeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html#cfn-scheduler-schedule-retrypolicy-maximumeventageinseconds
            '''
            result = self._values.get("maximum_event_age_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
            '''``CfnSchedule.RetryPolicyProperty.MaximumRetryAttempts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html#cfn-scheduler-schedule-retrypolicy-maximumretryattempts
            '''
            result = self._values.get("maximum_retry_attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetryPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.SageMakerPipelineParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class SageMakerPipelineParameterProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''
            :param name: ``CfnSchedule.SageMakerPipelineParameterProperty.Name``.
            :param value: ``CfnSchedule.SageMakerPipelineParameterProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                sage_maker_pipeline_parameter_property = scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c29c10cb7c0592826b32a3dc5e923a7c8d2f8b6bd9a0fe45759d650269d9f4d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnSchedule.SageMakerPipelineParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html#cfn-scheduler-schedule-sagemakerpipelineparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnSchedule.SageMakerPipelineParameterProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html#cfn-scheduler-schedule-sagemakerpipelineparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SageMakerPipelineParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.SageMakerPipelineParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"pipeline_parameter_list": "pipelineParameterList"},
    )
    class SageMakerPipelineParametersProperty:
        def __init__(
            self,
            *,
            pipeline_parameter_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnSchedule.SageMakerPipelineParameterProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param pipeline_parameter_list: ``CfnSchedule.SageMakerPipelineParametersProperty.PipelineParameterList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                sage_maker_pipeline_parameters_property = scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                    pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                        name="name",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0de727f226b2279098ba22fdf1aa02e57d81187ed9063acc8d789604e1a7f88)
                check_type(argname="argument pipeline_parameter_list", value=pipeline_parameter_list, expected_type=type_hints["pipeline_parameter_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pipeline_parameter_list is not None:
                self._values["pipeline_parameter_list"] = pipeline_parameter_list

        @builtins.property
        def pipeline_parameter_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedule.SageMakerPipelineParameterProperty", _IResolvable_da3f097b]]]]:
            '''``CfnSchedule.SageMakerPipelineParametersProperty.PipelineParameterList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html#cfn-scheduler-schedule-sagemakerpipelineparameters-pipelineparameterlist
            '''
            result = self._values.get("pipeline_parameter_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedule.SageMakerPipelineParameterProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SageMakerPipelineParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.SqsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"message_group_id": "messageGroupId"},
    )
    class SqsParametersProperty:
        def __init__(
            self,
            *,
            message_group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param message_group_id: ``CfnSchedule.SqsParametersProperty.MessageGroupId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                sqs_parameters_property = scheduler.CfnSchedule.SqsParametersProperty(
                    message_group_id="messageGroupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__13762215f810c9b64aba5ce7769b7babcff69eaa35d5d19f712b7515022da7fb)
                check_type(argname="argument message_group_id", value=message_group_id, expected_type=type_hints["message_group_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message_group_id is not None:
                self._values["message_group_id"] = message_group_id

        @builtins.property
        def message_group_id(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.SqsParametersProperty.MessageGroupId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html#cfn-scheduler-schedule-sqsparameters-messagegroupid
            '''
            result = self._values.get("message_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "role_arn": "roleArn",
            "dead_letter_config": "deadLetterConfig",
            "ecs_parameters": "ecsParameters",
            "event_bridge_parameters": "eventBridgeParameters",
            "input": "input",
            "kinesis_parameters": "kinesisParameters",
            "retry_policy": "retryPolicy",
            "sage_maker_pipeline_parameters": "sageMakerPipelineParameters",
            "sqs_parameters": "sqsParameters",
        },
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            role_arn: builtins.str,
            dead_letter_config: typing.Optional[typing.Union[typing.Union["CfnSchedule.DeadLetterConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            ecs_parameters: typing.Optional[typing.Union[typing.Union["CfnSchedule.EcsParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            event_bridge_parameters: typing.Optional[typing.Union[typing.Union["CfnSchedule.EventBridgeParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            input: typing.Optional[builtins.str] = None,
            kinesis_parameters: typing.Optional[typing.Union[typing.Union["CfnSchedule.KinesisParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            retry_policy: typing.Optional[typing.Union[typing.Union["CfnSchedule.RetryPolicyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            sage_maker_pipeline_parameters: typing.Optional[typing.Union[typing.Union["CfnSchedule.SageMakerPipelineParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            sqs_parameters: typing.Optional[typing.Union[typing.Union["CfnSchedule.SqsParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param arn: ``CfnSchedule.TargetProperty.Arn``.
            :param role_arn: ``CfnSchedule.TargetProperty.RoleArn``.
            :param dead_letter_config: ``CfnSchedule.TargetProperty.DeadLetterConfig``.
            :param ecs_parameters: ``CfnSchedule.TargetProperty.EcsParameters``.
            :param event_bridge_parameters: ``CfnSchedule.TargetProperty.EventBridgeParameters``.
            :param input: ``CfnSchedule.TargetProperty.Input``.
            :param kinesis_parameters: ``CfnSchedule.TargetProperty.KinesisParameters``.
            :param retry_policy: ``CfnSchedule.TargetProperty.RetryPolicy``.
            :param sage_maker_pipeline_parameters: ``CfnSchedule.TargetProperty.SageMakerPipelineParameters``.
            :param sqs_parameters: ``CfnSchedule.TargetProperty.SqsParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                # tags: Any
                
                target_property = scheduler.CfnSchedule.TargetProperty(
                    arn="arn",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    dead_letter_config=scheduler.CfnSchedule.DeadLetterConfigProperty(
                        arn="arn"
                    ),
                    ecs_parameters=scheduler.CfnSchedule.EcsParametersProperty(
                        task_definition_arn="taskDefinitionArn",
                
                        # the properties below are optional
                        capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                            capacity_provider="capacityProvider",
                
                            # the properties below are optional
                            base=123,
                            weight=123
                        )],
                        enable_ecs_managed_tags=False,
                        enable_execute_command=False,
                        group="group",
                        launch_type="launchType",
                        network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                            awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                                subnets=["subnets"],
                
                                # the properties below are optional
                                assign_public_ip="assignPublicIp",
                                security_groups=["securityGroups"]
                            )
                        ),
                        placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                            expression="expression",
                            type="type"
                        )],
                        placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                            field="field",
                            type="type"
                        )],
                        platform_version="platformVersion",
                        propagate_tags="propagateTags",
                        reference_id="referenceId",
                        tags=tags,
                        task_count=123
                    ),
                    event_bridge_parameters=scheduler.CfnSchedule.EventBridgeParametersProperty(
                        detail_type="detailType",
                        source="source"
                    ),
                    input="input",
                    kinesis_parameters=scheduler.CfnSchedule.KinesisParametersProperty(
                        partition_key="partitionKey"
                    ),
                    retry_policy=scheduler.CfnSchedule.RetryPolicyProperty(
                        maximum_event_age_in_seconds=123,
                        maximum_retry_attempts=123
                    ),
                    sage_maker_pipeline_parameters=scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                        pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                            name="name",
                            value="value"
                        )]
                    ),
                    sqs_parameters=scheduler.CfnSchedule.SqsParametersProperty(
                        message_group_id="messageGroupId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd5d0419478021d0554d24683f11134f17bb914856367055c32d004d8348a516)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument dead_letter_config", value=dead_letter_config, expected_type=type_hints["dead_letter_config"])
                check_type(argname="argument ecs_parameters", value=ecs_parameters, expected_type=type_hints["ecs_parameters"])
                check_type(argname="argument event_bridge_parameters", value=event_bridge_parameters, expected_type=type_hints["event_bridge_parameters"])
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument kinesis_parameters", value=kinesis_parameters, expected_type=type_hints["kinesis_parameters"])
                check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
                check_type(argname="argument sage_maker_pipeline_parameters", value=sage_maker_pipeline_parameters, expected_type=type_hints["sage_maker_pipeline_parameters"])
                check_type(argname="argument sqs_parameters", value=sqs_parameters, expected_type=type_hints["sqs_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
                "role_arn": role_arn,
            }
            if dead_letter_config is not None:
                self._values["dead_letter_config"] = dead_letter_config
            if ecs_parameters is not None:
                self._values["ecs_parameters"] = ecs_parameters
            if event_bridge_parameters is not None:
                self._values["event_bridge_parameters"] = event_bridge_parameters
            if input is not None:
                self._values["input"] = input
            if kinesis_parameters is not None:
                self._values["kinesis_parameters"] = kinesis_parameters
            if retry_policy is not None:
                self._values["retry_policy"] = retry_policy
            if sage_maker_pipeline_parameters is not None:
                self._values["sage_maker_pipeline_parameters"] = sage_maker_pipeline_parameters
            if sqs_parameters is not None:
                self._values["sqs_parameters"] = sqs_parameters

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnSchedule.TargetProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnSchedule.TargetProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dead_letter_config(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.DeadLetterConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.TargetProperty.DeadLetterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-deadletterconfig
            '''
            result = self._values.get("dead_letter_config")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.DeadLetterConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def ecs_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.EcsParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.TargetProperty.EcsParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-ecsparameters
            '''
            result = self._values.get("ecs_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.EcsParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def event_bridge_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.EventBridgeParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.TargetProperty.EventBridgeParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-eventbridgeparameters
            '''
            result = self._values.get("event_bridge_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.EventBridgeParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''``CfnSchedule.TargetProperty.Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kinesis_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.KinesisParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.TargetProperty.KinesisParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-kinesisparameters
            '''
            result = self._values.get("kinesis_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.KinesisParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def retry_policy(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.RetryPolicyProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.TargetProperty.RetryPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-retrypolicy
            '''
            result = self._values.get("retry_policy")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.RetryPolicyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sage_maker_pipeline_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.SageMakerPipelineParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.TargetProperty.SageMakerPipelineParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-sagemakerpipelineparameters
            '''
            result = self._values.get("sage_maker_pipeline_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.SageMakerPipelineParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sqs_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnSchedule.SqsParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnSchedule.TargetProperty.SqsParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-sqsparameters
            '''
            result = self._values.get("sqs_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnSchedule.SqsParametersProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnScheduleGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler.CfnScheduleGroup",
):
    '''A CloudFormation ``AWS::Scheduler::ScheduleGroup``.

    :cloudformationResource: AWS::Scheduler::ScheduleGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_scheduler as scheduler
        
        cfn_schedule_group = scheduler.CfnScheduleGroup(self, "MyCfnScheduleGroup",
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Scheduler::ScheduleGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Scheduler::ScheduleGroup.Name``.
        :param tags: ``AWS::Scheduler::ScheduleGroup.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55d5637c9b973d98ef3a23b13bf274e0a35bc07dfc27542f9b7185600a26a15e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduleGroupProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e179ed3a5ae801985e05b869adcf8daec39217aada45fa23844dd021dea92bda)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a163f755c33c470bd9bc8ba9ec2282566382000d7a5adbc8bba7aa9bd8e707d3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationDate")
    def attr_last_modification_date(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''
        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::Scheduler::ScheduleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html#cfn-scheduler-schedulegroup-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::ScheduleGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html#cfn-scheduler-schedulegroup-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e895b806668d11dd73b56d4fec496161e9b77b48c3e3475d06f4798d8a636529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler.CfnScheduleGroupProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnScheduleGroupProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScheduleGroup``.

        :param name: ``AWS::Scheduler::ScheduleGroup.Name``.
        :param tags: ``AWS::Scheduler::ScheduleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scheduler as scheduler
            
            cfn_schedule_group_props = scheduler.CfnScheduleGroupProps(
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9ebba0a3ae0883796e2ff900e8a82e62b8e0870420b26e180905979808a13e7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::ScheduleGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html#cfn-scheduler-schedulegroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::Scheduler::ScheduleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html#cfn-scheduler-schedulegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler.CfnScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "flexible_time_window": "flexibleTimeWindow",
        "schedule_expression": "scheduleExpression",
        "target": "target",
        "description": "description",
        "end_date": "endDate",
        "group_name": "groupName",
        "kms_key_arn": "kmsKeyArn",
        "name": "name",
        "schedule_expression_timezone": "scheduleExpressionTimezone",
        "start_date": "startDate",
        "state": "state",
    },
)
class CfnScheduleProps:
    def __init__(
        self,
        *,
        flexible_time_window: typing.Union[typing.Union[CfnSchedule.FlexibleTimeWindowProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        schedule_expression: builtins.str,
        target: typing.Union[typing.Union[CfnSchedule.TargetProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        schedule_expression_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchedule``.

        :param flexible_time_window: ``AWS::Scheduler::Schedule.FlexibleTimeWindow``.
        :param schedule_expression: ``AWS::Scheduler::Schedule.ScheduleExpression``.
        :param target: ``AWS::Scheduler::Schedule.Target``.
        :param description: ``AWS::Scheduler::Schedule.Description``.
        :param end_date: ``AWS::Scheduler::Schedule.EndDate``.
        :param group_name: ``AWS::Scheduler::Schedule.GroupName``.
        :param kms_key_arn: ``AWS::Scheduler::Schedule.KmsKeyArn``.
        :param name: ``AWS::Scheduler::Schedule.Name``.
        :param schedule_expression_timezone: ``AWS::Scheduler::Schedule.ScheduleExpressionTimezone``.
        :param start_date: ``AWS::Scheduler::Schedule.StartDate``.
        :param state: ``AWS::Scheduler::Schedule.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scheduler as scheduler
            
            # tags: Any
            
            cfn_schedule_props = scheduler.CfnScheduleProps(
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="mode",
            
                    # the properties below are optional
                    maximum_window_in_minutes=123
                ),
                schedule_expression="scheduleExpression",
                target=scheduler.CfnSchedule.TargetProperty(
                    arn="arn",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    dead_letter_config=scheduler.CfnSchedule.DeadLetterConfigProperty(
                        arn="arn"
                    ),
                    ecs_parameters=scheduler.CfnSchedule.EcsParametersProperty(
                        task_definition_arn="taskDefinitionArn",
            
                        # the properties below are optional
                        capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                            capacity_provider="capacityProvider",
            
                            # the properties below are optional
                            base=123,
                            weight=123
                        )],
                        enable_ecs_managed_tags=False,
                        enable_execute_command=False,
                        group="group",
                        launch_type="launchType",
                        network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                            awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                                subnets=["subnets"],
            
                                # the properties below are optional
                                assign_public_ip="assignPublicIp",
                                security_groups=["securityGroups"]
                            )
                        ),
                        placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                            expression="expression",
                            type="type"
                        )],
                        placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                            field="field",
                            type="type"
                        )],
                        platform_version="platformVersion",
                        propagate_tags="propagateTags",
                        reference_id="referenceId",
                        tags=tags,
                        task_count=123
                    ),
                    event_bridge_parameters=scheduler.CfnSchedule.EventBridgeParametersProperty(
                        detail_type="detailType",
                        source="source"
                    ),
                    input="input",
                    kinesis_parameters=scheduler.CfnSchedule.KinesisParametersProperty(
                        partition_key="partitionKey"
                    ),
                    retry_policy=scheduler.CfnSchedule.RetryPolicyProperty(
                        maximum_event_age_in_seconds=123,
                        maximum_retry_attempts=123
                    ),
                    sage_maker_pipeline_parameters=scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                        pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                            name="name",
                            value="value"
                        )]
                    ),
                    sqs_parameters=scheduler.CfnSchedule.SqsParametersProperty(
                        message_group_id="messageGroupId"
                    )
                ),
            
                # the properties below are optional
                description="description",
                end_date="endDate",
                group_name="groupName",
                kms_key_arn="kmsKeyArn",
                name="name",
                schedule_expression_timezone="scheduleExpressionTimezone",
                start_date="startDate",
                state="state"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7259f3f17d67e55e8ad4459f637d0d8aa80d57d58cb928f6b0403a6097a4ecf1)
            check_type(argname="argument flexible_time_window", value=flexible_time_window, expected_type=type_hints["flexible_time_window"])
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule_expression_timezone", value=schedule_expression_timezone, expected_type=type_hints["schedule_expression_timezone"])
            check_type(argname="argument start_date", value=start_date, expected_type=type_hints["start_date"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flexible_time_window": flexible_time_window,
            "schedule_expression": schedule_expression,
            "target": target,
        }
        if description is not None:
            self._values["description"] = description
        if end_date is not None:
            self._values["end_date"] = end_date
        if group_name is not None:
            self._values["group_name"] = group_name
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if name is not None:
            self._values["name"] = name
        if schedule_expression_timezone is not None:
            self._values["schedule_expression_timezone"] = schedule_expression_timezone
        if start_date is not None:
            self._values["start_date"] = start_date
        if state is not None:
            self._values["state"] = state

    @builtins.property
    def flexible_time_window(
        self,
    ) -> typing.Union[CfnSchedule.FlexibleTimeWindowProperty, _IResolvable_da3f097b]:
        '''``AWS::Scheduler::Schedule.FlexibleTimeWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-flexibletimewindow
        '''
        result = self._values.get("flexible_time_window")
        assert result is not None, "Required property 'flexible_time_window' is missing"
        return typing.cast(typing.Union[CfnSchedule.FlexibleTimeWindowProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def schedule_expression(self) -> builtins.str:
        '''``AWS::Scheduler::Schedule.ScheduleExpression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-scheduleexpression
        '''
        result = self._values.get("schedule_expression")
        assert result is not None, "Required property 'schedule_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> typing.Union[CfnSchedule.TargetProperty, _IResolvable_da3f097b]:
        '''``AWS::Scheduler::Schedule.Target``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-target
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(typing.Union[CfnSchedule.TargetProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_date(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.EndDate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-enddate
        '''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.GroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-groupname
        '''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.KmsKeyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_expression_timezone(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.ScheduleExpressionTimezone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-scheduleexpressiontimezone
        '''
        result = self._values.get("schedule_expression_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_date(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.StartDate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-startdate
        '''
        result = self._values.get("start_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::Scheduler::Schedule.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSchedule",
    "CfnScheduleGroup",
    "CfnScheduleGroupProps",
    "CfnScheduleProps",
]

publication.publish()

def _typecheckingstub__503b74ac170f15626de2456b6f8c40d2cdc1ab21574c821e051517099f516ea4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    flexible_time_window: typing.Union[typing.Union[CfnSchedule.FlexibleTimeWindowProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    schedule_expression: builtins.str,
    target: typing.Union[typing.Union[CfnSchedule.TargetProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    description: typing.Optional[builtins.str] = None,
    end_date: typing.Optional[builtins.str] = None,
    group_name: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    schedule_expression_timezone: typing.Optional[builtins.str] = None,
    start_date: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859c33780944a757aa0069dfe861a7f9ee3aaa6d51b1881276590d23b3cbc11d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c9dd58f37a9f244d09bdbca3ac4ea0869a0855a2cb760325d51c0d8beed730d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__596e14fe3c5d30f5608996086027eaf3ff49cf0205d5a551a9e0895e2be75f2a(
    value: typing.Union[CfnSchedule.FlexibleTimeWindowProperty, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a3656a00e3dadf75b2e58b2162ed9850cd46df81630349120c362c216f94db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9658077cef2602ca00d25f391105ce442d6a0a3efef1ca5be55db053ede80a78(
    value: typing.Union[CfnSchedule.TargetProperty, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5864139b51db95ec1c3e6c947b577675bb4f83133b1f5476864d71c4009c2386(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d0ae7ef525e3a588544a09eb7ec3271c357974ae47f41180a7aeb9086e2594(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1860ec4ad4204d90b7f2756ff633582f92f7f97d174b16a7da8e36811ebdc98(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c65947df9a6be40d839d971ea07ff6a85493b9cfbab03c61fc17e54bdd0e9276(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb6bd8d80ac829e96128e011c87e852bfea080bdcd859bfdf98c7874542dc1b5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb337d25b9d34da19dbe88b72514ea1e1e7a235cd91b7597abecd038498e11a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38fc94567c401ce05bf3ed2461327df25f05b71764228be5a3f95fec0573d007(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986ef975482735e4fbf46592da626ebfd4ca9636ad053fe886d40f9856d1483e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be9629f7b1d55fb08861d6713480d5fa198e6e40012bcf701a627e532032afb(
    *,
    subnets: typing.Sequence[builtins.str],
    assign_public_ip: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d8897162eaa13dfb81dc83e782d5936ed604f09ed623574ad9d0fabc4a1ab7e(
    *,
    capacity_provider: builtins.str,
    base: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__147909ee33401019ceeec9c9c260dd3ac0812db04c597e1b63c26f0608f61069(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dc612a243a7e6a4107ac15e844d139b177440cb37d514af299c8365e71f4cf1(
    *,
    task_definition_arn: builtins.str,
    capacity_provider_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSchedule.CapacityProviderStrategyItemProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_execute_command: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    group: typing.Optional[builtins.str] = None,
    launch_type: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[typing.Union[CfnSchedule.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    placement_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSchedule.PlacementConstraintProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    placement_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSchedule.PlacementStrategyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    platform_version: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.str] = None,
    reference_id: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    task_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e0c05434c8347bffb5179e8c9bc22fdc3ff4fdae681d5b9d995e0f7c8c1900(
    *,
    detail_type: builtins.str,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d4dffb710d1a3208f37cc6de0f2cddceb53e1178391bdc54cfedb8ca6626ec4(
    *,
    mode: builtins.str,
    maximum_window_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a3b10246bef07a2f7fc56bf58e08c66b0fd77f7770804a87bf867fa8541cbb(
    *,
    partition_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428ddbfd1435a3560f182001dfcf151c620cba65c309e87341f84eb7d60ba492(
    *,
    awsvpc_configuration: typing.Optional[typing.Union[typing.Union[CfnSchedule.AwsVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb19941ef1169a4cc78daf82b7ea64663f5a28f890fbeded34448dd3f0a3c16f(
    *,
    expression: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d9dc80c7a08a059d79aa3db1c44bcc28c84872422d6fd991bbca1124a384865(
    *,
    field: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb66e495a2f0291cd0e58a71fc127fa67ed8d10f2d977b132a1770f7b3a1f92d(
    *,
    maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c29c10cb7c0592826b32a3dc5e923a7c8d2f8b6bd9a0fe45759d650269d9f4d(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0de727f226b2279098ba22fdf1aa02e57d81187ed9063acc8d789604e1a7f88(
    *,
    pipeline_parameter_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSchedule.SageMakerPipelineParameterProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13762215f810c9b64aba5ce7769b7babcff69eaa35d5d19f712b7515022da7fb(
    *,
    message_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd5d0419478021d0554d24683f11134f17bb914856367055c32d004d8348a516(
    *,
    arn: builtins.str,
    role_arn: builtins.str,
    dead_letter_config: typing.Optional[typing.Union[typing.Union[CfnSchedule.DeadLetterConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    ecs_parameters: typing.Optional[typing.Union[typing.Union[CfnSchedule.EcsParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    event_bridge_parameters: typing.Optional[typing.Union[typing.Union[CfnSchedule.EventBridgeParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    input: typing.Optional[builtins.str] = None,
    kinesis_parameters: typing.Optional[typing.Union[typing.Union[CfnSchedule.KinesisParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    retry_policy: typing.Optional[typing.Union[typing.Union[CfnSchedule.RetryPolicyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    sage_maker_pipeline_parameters: typing.Optional[typing.Union[typing.Union[CfnSchedule.SageMakerPipelineParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    sqs_parameters: typing.Optional[typing.Union[typing.Union[CfnSchedule.SqsParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d5637c9b973d98ef3a23b13bf274e0a35bc07dfc27542f9b7185600a26a15e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e179ed3a5ae801985e05b869adcf8daec39217aada45fa23844dd021dea92bda(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a163f755c33c470bd9bc8ba9ec2282566382000d7a5adbc8bba7aa9bd8e707d3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e895b806668d11dd73b56d4fec496161e9b77b48c3e3475d06f4798d8a636529(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ebba0a3ae0883796e2ff900e8a82e62b8e0870420b26e180905979808a13e7(
    *,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7259f3f17d67e55e8ad4459f637d0d8aa80d57d58cb928f6b0403a6097a4ecf1(
    *,
    flexible_time_window: typing.Union[typing.Union[CfnSchedule.FlexibleTimeWindowProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    schedule_expression: builtins.str,
    target: typing.Union[typing.Union[CfnSchedule.TargetProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    description: typing.Optional[builtins.str] = None,
    end_date: typing.Optional[builtins.str] = None,
    group_name: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    schedule_expression_timezone: typing.Optional[builtins.str] = None,
    start_date: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
