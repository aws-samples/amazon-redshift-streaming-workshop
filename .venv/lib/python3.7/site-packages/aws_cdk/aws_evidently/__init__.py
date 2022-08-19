'''
# AWS::Evidently Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_evidently as evidently
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Evidently construct libraries](https://constructs.dev/search?q=evidently)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Evidently resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Evidently.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Evidently](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Evidently.html).

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

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnExperiment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment",
):
    '''A CloudFormation ``AWS::Evidently::Experiment``.

    Creates or updates an Evidently *experiment* . Before you create an experiment, you must create the feature to use for the experiment.

    An experiment helps you make feature design decisions based on evidence and data. An experiment can test as many as five variations at once. Evidently collects experiment data and analyzes it by statistical methods, and provides clear recommendations about which variations perform better.

    :cloudformationResource: AWS::Evidently::Experiment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_experiment = evidently.CfnExperiment(self, "MyCfnExperiment",
            metric_goals=[evidently.CfnExperiment.MetricGoalObjectProperty(
                desired_change="desiredChange",
                entity_id_key="entityIdKey",
                event_pattern="eventPattern",
                metric_name="metricName",
                value_key="valueKey",
        
                # the properties below are optional
                unit_label="unitLabel"
            )],
            name="name",
            online_ab_config=evidently.CfnExperiment.OnlineAbConfigObjectProperty(
                control_treatment_name="controlTreatmentName",
                treatment_weights=[evidently.CfnExperiment.TreatmentToWeightProperty(
                    split_weight=123,
                    treatment="treatment"
                )]
            ),
            project="project",
            treatments=[evidently.CfnExperiment.TreatmentObjectProperty(
                feature="feature",
                treatment_name="treatmentName",
                variation="variation",
        
                # the properties below are optional
                description="description"
            )],
        
            # the properties below are optional
            description="description",
            randomization_salt="randomizationSalt",
            remove_segment=False,
            running_status=evidently.CfnExperiment.RunningStatusObjectProperty(
                analysis_complete_time="analysisCompleteTime",
                desired_state="desiredState",
                reason="reason",
                status="status"
            ),
            sampling_rate=123,
            segment="segment",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metric_goals: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnExperiment.MetricGoalObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        name: builtins.str,
        online_ab_config: typing.Union[typing.Union["CfnExperiment.OnlineAbConfigObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        project: builtins.str,
        treatments: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnExperiment.TreatmentObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        description: typing.Optional[builtins.str] = None,
        randomization_salt: typing.Optional[builtins.str] = None,
        remove_segment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        running_status: typing.Optional[typing.Union[typing.Union["CfnExperiment.RunningStatusObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        sampling_rate: typing.Optional[jsii.Number] = None,
        segment: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Evidently::Experiment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param metric_goals: An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal. You can use up to three metrics in an experiment.
        :param name: A name for the new experiment.
        :param online_ab_config: A structure that contains the configuration of which variation to use as the "control" version. The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.
        :param project: The name or the ARN of the project where this experiment is to be created.
        :param treatments: An array of structures that describe the configuration of each feature variation used in the experiment.
        :param description: An optional description of the experiment.
        :param randomization_salt: When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the experiment name as the ``randomizationSalt`` .
        :param remove_segment: ``AWS::Evidently::Experiment.RemoveSegment``.
        :param running_status: A structure that you can use to start and stop the experiment.
        :param sampling_rate: The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent. The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature. This is represented in thousandths of a percent. For example, specify 10,000 to allocate 10% of the available audience.
        :param segment: ``AWS::Evidently::Experiment.Segment``.
        :param tags: Assigns one or more tags (key-value pairs) to the experiment. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with an experiment. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnExperiment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnExperimentProps(
            metric_goals=metric_goals,
            name=name,
            online_ab_config=online_ab_config,
            project=project,
            treatments=treatments,
            description=description,
            randomization_salt=randomization_salt,
            remove_segment=remove_segment,
            running_status=running_status,
            sampling_rate=sampling_rate,
            segment=segment,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnExperiment.inspect)
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
            type_hints = typing.get_type_hints(CfnExperiment._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the experiment.

        For example, ``arn:aws:evidently:us-west-2:0123455678912:project/myProject/experiment/myExperiment``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Assigns one or more tags (key-value pairs) to the experiment.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with an experiment.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metricGoals")
    def metric_goals(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnExperiment.MetricGoalObjectProperty", _IResolvable_da3f097b]]]:
        '''An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal.

        You can use up to three metrics in an experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-metricgoals
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnExperiment.MetricGoalObjectProperty", _IResolvable_da3f097b]]], jsii.get(self, "metricGoals"))

    @metric_goals.setter
    def metric_goals(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnExperiment.MetricGoalObjectProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "metric_goals").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricGoals", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the new experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onlineAbConfig")
    def online_ab_config(
        self,
    ) -> typing.Union["CfnExperiment.OnlineAbConfigObjectProperty", _IResolvable_da3f097b]:
        '''A structure that contains the configuration of which variation to use as the "control" version.

        The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-onlineabconfig
        '''
        return typing.cast(typing.Union["CfnExperiment.OnlineAbConfigObjectProperty", _IResolvable_da3f097b], jsii.get(self, "onlineAbConfig"))

    @online_ab_config.setter
    def online_ab_config(
        self,
        value: typing.Union["CfnExperiment.OnlineAbConfigObjectProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "online_ab_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlineAbConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        '''The name or the ARN of the project where this experiment is to be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-project
        '''
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="treatments")
    def treatments(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnExperiment.TreatmentObjectProperty", _IResolvable_da3f097b]]]:
        '''An array of structures that describe the configuration of each feature variation used in the experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-treatments
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnExperiment.TreatmentObjectProperty", _IResolvable_da3f097b]]], jsii.get(self, "treatments"))

    @treatments.setter
    def treatments(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnExperiment.TreatmentObjectProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "treatments").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatments", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="randomizationSalt")
    def randomization_salt(self) -> typing.Optional[builtins.str]:
        '''When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served.

        This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the experiment name as the ``randomizationSalt`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-randomizationsalt
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "randomizationSalt"))

    @randomization_salt.setter
    def randomization_salt(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "randomization_salt").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "randomizationSalt", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="removeSegment")
    def remove_segment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::Evidently::Experiment.RemoveSegment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-removesegment
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "removeSegment"))

    @remove_segment.setter
    def remove_segment(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "remove_segment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeSegment", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="runningStatus")
    def running_status(
        self,
    ) -> typing.Optional[typing.Union["CfnExperiment.RunningStatusObjectProperty", _IResolvable_da3f097b]]:
        '''A structure that you can use to start and stop the experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-runningstatus
        '''
        return typing.cast(typing.Optional[typing.Union["CfnExperiment.RunningStatusObjectProperty", _IResolvable_da3f097b]], jsii.get(self, "runningStatus"))

    @running_status.setter
    def running_status(
        self,
        value: typing.Optional[typing.Union["CfnExperiment.RunningStatusObjectProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "running_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runningStatus", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="samplingRate")
    def sampling_rate(self) -> typing.Optional[jsii.Number]:
        '''The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent.

        The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature.

        This is represented in thousandths of a percent. For example, specify 10,000 to allocate 10% of the available audience.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-samplingrate
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingRate"))

    @sampling_rate.setter
    def sampling_rate(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "sampling_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingRate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="segment")
    def segment(self) -> typing.Optional[builtins.str]:
        '''``AWS::Evidently::Experiment.Segment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-segment
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "segment"))

    @segment.setter
    def segment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnExperiment, "segment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segment", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.MetricGoalObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "desired_change": "desiredChange",
            "entity_id_key": "entityIdKey",
            "event_pattern": "eventPattern",
            "metric_name": "metricName",
            "value_key": "valueKey",
            "unit_label": "unitLabel",
        },
    )
    class MetricGoalObjectProperty:
        def __init__(
            self,
            *,
            desired_change: builtins.str,
            entity_id_key: builtins.str,
            event_pattern: builtins.str,
            metric_name: builtins.str,
            value_key: builtins.str,
            unit_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to tell Evidently whether higher or lower values are desired for a metric that is used in an experiment.

            :param desired_change: ``INCREASE`` means that a variation with a higher number for this metric is performing better. ``DECREASE`` means that a variation with a lower number for this metric is performing better.
            :param entity_id_key: The entity, such as a user or session, that does an action that causes a metric value to be recorded. An example is ``userDetails.userID`` .
            :param event_pattern: The EventBridge event pattern that defines how the metric is recorded. For more information about EventBridge event patterns, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ .
            :param metric_name: A name for the metric. It can include up to 255 characters.
            :param value_key: The JSON path to reference the numerical metric value in the event.
            :param unit_label: A label for the units that the metric is measuring.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                metric_goal_object_property = evidently.CfnExperiment.MetricGoalObjectProperty(
                    desired_change="desiredChange",
                    entity_id_key="entityIdKey",
                    event_pattern="eventPattern",
                    metric_name="metricName",
                    value_key="valueKey",
                
                    # the properties below are optional
                    unit_label="unitLabel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnExperiment.MetricGoalObjectProperty.__init__)
                check_type(argname="argument desired_change", value=desired_change, expected_type=type_hints["desired_change"])
                check_type(argname="argument entity_id_key", value=entity_id_key, expected_type=type_hints["entity_id_key"])
                check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument value_key", value=value_key, expected_type=type_hints["value_key"])
                check_type(argname="argument unit_label", value=unit_label, expected_type=type_hints["unit_label"])
            self._values: typing.Dict[str, typing.Any] = {
                "desired_change": desired_change,
                "entity_id_key": entity_id_key,
                "event_pattern": event_pattern,
                "metric_name": metric_name,
                "value_key": value_key,
            }
            if unit_label is not None:
                self._values["unit_label"] = unit_label

        @builtins.property
        def desired_change(self) -> builtins.str:
            '''``INCREASE`` means that a variation with a higher number for this metric is performing better.

            ``DECREASE`` means that a variation with a lower number for this metric is performing better.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-desiredchange
            '''
            result = self._values.get("desired_change")
            assert result is not None, "Required property 'desired_change' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def entity_id_key(self) -> builtins.str:
            '''The entity, such as a user or session, that does an action that causes a metric value to be recorded.

            An example is ``userDetails.userID`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-entityidkey
            '''
            result = self._values.get("entity_id_key")
            assert result is not None, "Required property 'entity_id_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def event_pattern(self) -> builtins.str:
            '''The EventBridge event pattern that defines how the metric is recorded.

            For more information about EventBridge event patterns, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-eventpattern
            '''
            result = self._values.get("event_pattern")
            assert result is not None, "Required property 'event_pattern' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''A name for the metric.

            It can include up to 255 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_key(self) -> builtins.str:
            '''The JSON path to reference the numerical metric value in the event.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-valuekey
            '''
            result = self._values.get("value_key")
            assert result is not None, "Required property 'value_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit_label(self) -> typing.Optional[builtins.str]:
            '''A label for the units that the metric is measuring.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-unitlabel
            '''
            result = self._values.get("unit_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricGoalObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.OnlineAbConfigObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "control_treatment_name": "controlTreatmentName",
            "treatment_weights": "treatmentWeights",
        },
    )
    class OnlineAbConfigObjectProperty:
        def __init__(
            self,
            *,
            control_treatment_name: typing.Optional[builtins.str] = None,
            treatment_weights: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnExperiment.TreatmentToWeightProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''A structure that contains the configuration of which variation to use as the "control" version.

            The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.

            :param control_treatment_name: The name of the variation that is to be the default variation that the other variations are compared to.
            :param treatment_weights: A set of key-value pairs. The keys are treatment names, and the values are the portion of experiment traffic to be assigned to that treatment. Specify the traffic portion in thousandths of a percent, so 20,000 for a variation would allocate 20% of the experiment traffic to that variation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                online_ab_config_object_property = evidently.CfnExperiment.OnlineAbConfigObjectProperty(
                    control_treatment_name="controlTreatmentName",
                    treatment_weights=[evidently.CfnExperiment.TreatmentToWeightProperty(
                        split_weight=123,
                        treatment="treatment"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnExperiment.OnlineAbConfigObjectProperty.__init__)
                check_type(argname="argument control_treatment_name", value=control_treatment_name, expected_type=type_hints["control_treatment_name"])
                check_type(argname="argument treatment_weights", value=treatment_weights, expected_type=type_hints["treatment_weights"])
            self._values: typing.Dict[str, typing.Any] = {}
            if control_treatment_name is not None:
                self._values["control_treatment_name"] = control_treatment_name
            if treatment_weights is not None:
                self._values["treatment_weights"] = treatment_weights

        @builtins.property
        def control_treatment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the variation that is to be the default variation that the other variations are compared to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html#cfn-evidently-experiment-onlineabconfigobject-controltreatmentname
            '''
            result = self._values.get("control_treatment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def treatment_weights(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnExperiment.TreatmentToWeightProperty", _IResolvable_da3f097b]]]]:
            '''A set of key-value pairs.

            The keys are treatment names, and the values are the portion of experiment traffic to be assigned to that treatment. Specify the traffic portion in thousandths of a percent, so 20,000 for a variation would allocate 20% of the experiment traffic to that variation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html#cfn-evidently-experiment-onlineabconfigobject-treatmentweights
            '''
            result = self._values.get("treatment_weights")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnExperiment.TreatmentToWeightProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnlineAbConfigObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.RunningStatusObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "analysis_complete_time": "analysisCompleteTime",
            "desired_state": "desiredState",
            "reason": "reason",
            "status": "status",
        },
    )
    class RunningStatusObjectProperty:
        def __init__(
            self,
            *,
            analysis_complete_time: typing.Optional[builtins.str] = None,
            desired_state: typing.Optional[builtins.str] = None,
            reason: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to start and stop the experiment.

            :param analysis_complete_time: If you are using AWS CloudFormation to start the experiment, use this field to specify when the experiment is to end. The format is as a UNIX timestamp. For more information about this format, see `The Current Epoch Unix Timestamp <https://docs.aws.amazon.com/https://www.unixtimestamp.com/index.php>`_ .
            :param desired_state: If you are using AWS CloudFormation to stop this experiment, specify either ``COMPLETED`` or ``CANCELLED`` here to indicate how to classify this experiment.
            :param reason: If you are using AWS CloudFormation to stop this experiment, this is an optional field that you can use to record why the experiment is being stopped or cancelled.
            :param status: To start the experiment now, specify ``START`` for this parameter. If this experiment is currently running and you want to stop it now, specify ``STOP`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                running_status_object_property = evidently.CfnExperiment.RunningStatusObjectProperty(
                    analysis_complete_time="analysisCompleteTime",
                    desired_state="desiredState",
                    reason="reason",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnExperiment.RunningStatusObjectProperty.__init__)
                check_type(argname="argument analysis_complete_time", value=analysis_complete_time, expected_type=type_hints["analysis_complete_time"])
                check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
                check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[str, typing.Any] = {}
            if analysis_complete_time is not None:
                self._values["analysis_complete_time"] = analysis_complete_time
            if desired_state is not None:
                self._values["desired_state"] = desired_state
            if reason is not None:
                self._values["reason"] = reason
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def analysis_complete_time(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to start the experiment, use this field to specify when the experiment is to end.

            The format is as a UNIX timestamp. For more information about this format, see `The Current Epoch Unix Timestamp <https://docs.aws.amazon.com/https://www.unixtimestamp.com/index.php>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-analysiscompletetime
            '''
            result = self._values.get("analysis_complete_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def desired_state(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to stop this experiment, specify either ``COMPLETED`` or ``CANCELLED`` here to indicate how to classify this experiment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-desiredstate
            '''
            result = self._values.get("desired_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reason(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to stop this experiment, this is an optional field that you can use to record why the experiment is being stopped or cancelled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-reason
            '''
            result = self._values.get("reason")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''To start the experiment now, specify ``START`` for this parameter.

            If this experiment is currently running and you want to stop it now, specify ``STOP`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunningStatusObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.TreatmentObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "feature": "feature",
            "treatment_name": "treatmentName",
            "variation": "variation",
            "description": "description",
        },
    )
    class TreatmentObjectProperty:
        def __init__(
            self,
            *,
            feature: builtins.str,
            treatment_name: builtins.str,
            variation: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that defines one treatment in an experiment.

            A treatment is a variation of the feature that you are including in the experiment.

            :param feature: The name of the feature for this experiment.
            :param treatment_name: A name for this treatment. It can include up to 127 characters.
            :param variation: The name of the variation to use for this treatment.
            :param description: The description of the treatment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                treatment_object_property = evidently.CfnExperiment.TreatmentObjectProperty(
                    feature="feature",
                    treatment_name="treatmentName",
                    variation="variation",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnExperiment.TreatmentObjectProperty.__init__)
                check_type(argname="argument feature", value=feature, expected_type=type_hints["feature"])
                check_type(argname="argument treatment_name", value=treatment_name, expected_type=type_hints["treatment_name"])
                check_type(argname="argument variation", value=variation, expected_type=type_hints["variation"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[str, typing.Any] = {
                "feature": feature,
                "treatment_name": treatment_name,
                "variation": variation,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def feature(self) -> builtins.str:
            '''The name of the feature for this experiment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-feature
            '''
            result = self._values.get("feature")
            assert result is not None, "Required property 'feature' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def treatment_name(self) -> builtins.str:
            '''A name for this treatment.

            It can include up to 127 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-treatmentname
            '''
            result = self._values.get("treatment_name")
            assert result is not None, "Required property 'treatment_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variation(self) -> builtins.str:
            '''The name of the variation to use for this treatment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-variation
            '''
            result = self._values.get("variation")
            assert result is not None, "Required property 'variation' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the treatment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TreatmentObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.TreatmentToWeightProperty",
        jsii_struct_bases=[],
        name_mapping={"split_weight": "splitWeight", "treatment": "treatment"},
    )
    class TreatmentToWeightProperty:
        def __init__(
            self,
            *,
            split_weight: jsii.Number,
            treatment: builtins.str,
        ) -> None:
            '''This structure defines how much experiment traffic to allocate to one treatment used in the experiment.

            :param split_weight: The portion of experiment traffic to allocate to this treatment. Specify the traffic portion in thousandths of a percent, so 20,000 allocated to a treatment would allocate 20% of the experiment traffic to that treatment.
            :param treatment: The name of the treatment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                treatment_to_weight_property = evidently.CfnExperiment.TreatmentToWeightProperty(
                    split_weight=123,
                    treatment="treatment"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnExperiment.TreatmentToWeightProperty.__init__)
                check_type(argname="argument split_weight", value=split_weight, expected_type=type_hints["split_weight"])
                check_type(argname="argument treatment", value=treatment, expected_type=type_hints["treatment"])
            self._values: typing.Dict[str, typing.Any] = {
                "split_weight": split_weight,
                "treatment": treatment,
            }

        @builtins.property
        def split_weight(self) -> jsii.Number:
            '''The portion of experiment traffic to allocate to this treatment.

            Specify the traffic portion in thousandths of a percent, so 20,000 allocated to a treatment would allocate 20% of the experiment traffic to that treatment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html#cfn-evidently-experiment-treatmenttoweight-splitweight
            '''
            result = self._values.get("split_weight")
            assert result is not None, "Required property 'split_weight' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def treatment(self) -> builtins.str:
            '''The name of the treatment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html#cfn-evidently-experiment-treatmenttoweight-treatment
            '''
            result = self._values.get("treatment")
            assert result is not None, "Required property 'treatment' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TreatmentToWeightProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnExperimentProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_goals": "metricGoals",
        "name": "name",
        "online_ab_config": "onlineAbConfig",
        "project": "project",
        "treatments": "treatments",
        "description": "description",
        "randomization_salt": "randomizationSalt",
        "remove_segment": "removeSegment",
        "running_status": "runningStatus",
        "sampling_rate": "samplingRate",
        "segment": "segment",
        "tags": "tags",
    },
)
class CfnExperimentProps:
    def __init__(
        self,
        *,
        metric_goals: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnExperiment.MetricGoalObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        name: builtins.str,
        online_ab_config: typing.Union[typing.Union[CfnExperiment.OnlineAbConfigObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        project: builtins.str,
        treatments: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnExperiment.TreatmentObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        description: typing.Optional[builtins.str] = None,
        randomization_salt: typing.Optional[builtins.str] = None,
        remove_segment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        running_status: typing.Optional[typing.Union[typing.Union[CfnExperiment.RunningStatusObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        sampling_rate: typing.Optional[jsii.Number] = None,
        segment: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnExperiment``.

        :param metric_goals: An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal. You can use up to three metrics in an experiment.
        :param name: A name for the new experiment.
        :param online_ab_config: A structure that contains the configuration of which variation to use as the "control" version. The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.
        :param project: The name or the ARN of the project where this experiment is to be created.
        :param treatments: An array of structures that describe the configuration of each feature variation used in the experiment.
        :param description: An optional description of the experiment.
        :param randomization_salt: When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the experiment name as the ``randomizationSalt`` .
        :param remove_segment: ``AWS::Evidently::Experiment.RemoveSegment``.
        :param running_status: A structure that you can use to start and stop the experiment.
        :param sampling_rate: The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent. The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature. This is represented in thousandths of a percent. For example, specify 10,000 to allocate 10% of the available audience.
        :param segment: ``AWS::Evidently::Experiment.Segment``.
        :param tags: Assigns one or more tags (key-value pairs) to the experiment. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with an experiment. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_experiment_props = evidently.CfnExperimentProps(
                metric_goals=[evidently.CfnExperiment.MetricGoalObjectProperty(
                    desired_change="desiredChange",
                    entity_id_key="entityIdKey",
                    event_pattern="eventPattern",
                    metric_name="metricName",
                    value_key="valueKey",
            
                    # the properties below are optional
                    unit_label="unitLabel"
                )],
                name="name",
                online_ab_config=evidently.CfnExperiment.OnlineAbConfigObjectProperty(
                    control_treatment_name="controlTreatmentName",
                    treatment_weights=[evidently.CfnExperiment.TreatmentToWeightProperty(
                        split_weight=123,
                        treatment="treatment"
                    )]
                ),
                project="project",
                treatments=[evidently.CfnExperiment.TreatmentObjectProperty(
                    feature="feature",
                    treatment_name="treatmentName",
                    variation="variation",
            
                    # the properties below are optional
                    description="description"
                )],
            
                # the properties below are optional
                description="description",
                randomization_salt="randomizationSalt",
                remove_segment=False,
                running_status=evidently.CfnExperiment.RunningStatusObjectProperty(
                    analysis_complete_time="analysisCompleteTime",
                    desired_state="desiredState",
                    reason="reason",
                    status="status"
                ),
                sampling_rate=123,
                segment="segment",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnExperimentProps.__init__)
            check_type(argname="argument metric_goals", value=metric_goals, expected_type=type_hints["metric_goals"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument online_ab_config", value=online_ab_config, expected_type=type_hints["online_ab_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument treatments", value=treatments, expected_type=type_hints["treatments"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument randomization_salt", value=randomization_salt, expected_type=type_hints["randomization_salt"])
            check_type(argname="argument remove_segment", value=remove_segment, expected_type=type_hints["remove_segment"])
            check_type(argname="argument running_status", value=running_status, expected_type=type_hints["running_status"])
            check_type(argname="argument sampling_rate", value=sampling_rate, expected_type=type_hints["sampling_rate"])
            check_type(argname="argument segment", value=segment, expected_type=type_hints["segment"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_goals": metric_goals,
            "name": name,
            "online_ab_config": online_ab_config,
            "project": project,
            "treatments": treatments,
        }
        if description is not None:
            self._values["description"] = description
        if randomization_salt is not None:
            self._values["randomization_salt"] = randomization_salt
        if remove_segment is not None:
            self._values["remove_segment"] = remove_segment
        if running_status is not None:
            self._values["running_status"] = running_status
        if sampling_rate is not None:
            self._values["sampling_rate"] = sampling_rate
        if segment is not None:
            self._values["segment"] = segment
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def metric_goals(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnExperiment.MetricGoalObjectProperty, _IResolvable_da3f097b]]]:
        '''An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal.

        You can use up to three metrics in an experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-metricgoals
        '''
        result = self._values.get("metric_goals")
        assert result is not None, "Required property 'metric_goals' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnExperiment.MetricGoalObjectProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the new experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def online_ab_config(
        self,
    ) -> typing.Union[CfnExperiment.OnlineAbConfigObjectProperty, _IResolvable_da3f097b]:
        '''A structure that contains the configuration of which variation to use as the "control" version.

        The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-onlineabconfig
        '''
        result = self._values.get("online_ab_config")
        assert result is not None, "Required property 'online_ab_config' is missing"
        return typing.cast(typing.Union[CfnExperiment.OnlineAbConfigObjectProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or the ARN of the project where this experiment is to be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-project
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def treatments(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnExperiment.TreatmentObjectProperty, _IResolvable_da3f097b]]]:
        '''An array of structures that describe the configuration of each feature variation used in the experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-treatments
        '''
        result = self._values.get("treatments")
        assert result is not None, "Required property 'treatments' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnExperiment.TreatmentObjectProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def randomization_salt(self) -> typing.Optional[builtins.str]:
        '''When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served.

        This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the experiment name as the ``randomizationSalt`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-randomizationsalt
        '''
        result = self._values.get("randomization_salt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remove_segment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::Evidently::Experiment.RemoveSegment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-removesegment
        '''
        result = self._values.get("remove_segment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def running_status(
        self,
    ) -> typing.Optional[typing.Union[CfnExperiment.RunningStatusObjectProperty, _IResolvable_da3f097b]]:
        '''A structure that you can use to start and stop the experiment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-runningstatus
        '''
        result = self._values.get("running_status")
        return typing.cast(typing.Optional[typing.Union[CfnExperiment.RunningStatusObjectProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def sampling_rate(self) -> typing.Optional[jsii.Number]:
        '''The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent.

        The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature.

        This is represented in thousandths of a percent. For example, specify 10,000 to allocate 10% of the available audience.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-samplingrate
        '''
        result = self._values.get("sampling_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def segment(self) -> typing.Optional[builtins.str]:
        '''``AWS::Evidently::Experiment.Segment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-segment
        '''
        result = self._values.get("segment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the experiment.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with an experiment.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExperimentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFeature(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnFeature",
):
    '''A CloudFormation ``AWS::Evidently::Feature``.

    Creates or updates an Evidently *feature* that you want to launch or test. You can define up to five variations of a feature, and use these variations in your launches and experiments. A feature must be created in a project. For information about creating a project, see `CreateProject <https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateProject.html>`_ .

    :cloudformationResource: AWS::Evidently::Feature
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_feature = evidently.CfnFeature(self, "MyCfnFeature",
            name="name",
            project="project",
            variations=[evidently.CfnFeature.VariationObjectProperty(
                boolean_value=False,
                double_value=123,
                long_value=123,
                string_value="stringValue",
                variation_name="variationName"
            )],
        
            # the properties below are optional
            default_variation="defaultVariation",
            description="description",
            entity_overrides=[evidently.CfnFeature.EntityOverrideProperty(
                entity_id="entityId",
                variation="variation"
            )],
            evaluation_strategy="evaluationStrategy",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        project: builtins.str,
        variations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnFeature.VariationObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        default_variation: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        entity_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnFeature.EntityOverrideProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        evaluation_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Evidently::Feature``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name for the feature. It can include up to 127 characters.
        :param project: The name or ARN of the project that is to contain the new feature.
        :param variations: An array of structures that contain the configuration of the feature's different variations. Each ``VariationObject`` in the ``Variations`` array for a feature must have the same type of value ( ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` ).
        :param default_variation: The name of the variation to use as the default variation. The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature. This variation must also be listed in the ``Variations`` structure. If you omit ``DefaultVariation`` , the first variation listed in the ``Variations`` structure is used as the default variation.
        :param description: An optional description of the feature.
        :param entity_overrides: Specify users that should always be served a specific variation of a feature. Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.
        :param evaluation_strategy: Specify ``ALL_RULES`` to activate the traffic allocation specified by any ongoing launches or experiments. Specify ``DEFAULT_VARIATION`` to serve the default variation to all users instead.
        :param tags: Assigns one or more tags (key-value pairs) to the feature. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a feature. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFeature.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFeatureProps(
            name=name,
            project=project,
            variations=variations,
            default_variation=default_variation,
            description=description,
            entity_overrides=entity_overrides,
            evaluation_strategy=evaluation_strategy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFeature.inspect)
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
            type_hints = typing.get_type_hints(CfnFeature._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the feature.

        For example, ``arn:aws:evidently:us-west-2:0123455678912:project/myProject/feature/myFeature`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Assigns one or more tags (key-value pairs) to the feature.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a feature.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the feature.

        It can include up to 127 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFeature, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        '''The name or ARN of the project that is to contain the new feature.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-project
        '''
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFeature, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="variations")
    def variations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFeature.VariationObjectProperty", _IResolvable_da3f097b]]]:
        '''An array of structures that contain the configuration of the feature's different variations.

        Each ``VariationObject`` in the ``Variations`` array for a feature must have the same type of value ( ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-variations
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFeature.VariationObjectProperty", _IResolvable_da3f097b]]], jsii.get(self, "variations"))

    @variations.setter
    def variations(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFeature.VariationObjectProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFeature, "variations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultVariation")
    def default_variation(self) -> typing.Optional[builtins.str]:
        '''The name of the variation to use as the default variation.

        The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature.

        This variation must also be listed in the ``Variations`` structure.

        If you omit ``DefaultVariation`` , the first variation listed in the ``Variations`` structure is used as the default variation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-defaultvariation
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultVariation"))

    @default_variation.setter
    def default_variation(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFeature, "default_variation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultVariation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the feature.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFeature, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="entityOverrides")
    def entity_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFeature.EntityOverrideProperty", _IResolvable_da3f097b]]]]:
        '''Specify users that should always be served a specific variation of a feature.

        Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-entityoverrides
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFeature.EntityOverrideProperty", _IResolvable_da3f097b]]]], jsii.get(self, "entityOverrides"))

    @entity_overrides.setter
    def entity_overrides(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFeature.EntityOverrideProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFeature, "entity_overrides").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityOverrides", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="evaluationStrategy")
    def evaluation_strategy(self) -> typing.Optional[builtins.str]:
        '''Specify ``ALL_RULES`` to activate the traffic allocation specified by any ongoing launches or experiments.

        Specify ``DEFAULT_VARIATION`` to serve the default variation to all users instead.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-evaluationstrategy
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationStrategy"))

    @evaluation_strategy.setter
    def evaluation_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFeature, "evaluation_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationStrategy", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnFeature.EntityOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"entity_id": "entityId", "variation": "variation"},
    )
    class EntityOverrideProperty:
        def __init__(
            self,
            *,
            entity_id: typing.Optional[builtins.str] = None,
            variation: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A set of key-value pairs that specify users who should always be served a specific variation of a feature.

            Each key specifies a user using their user ID, account ID, or some other identifier. The value specifies the name of the variation that the user is to be served.

            :param entity_id: The entity ID to be served the variation specified in ``Variation`` .
            :param variation: The name of the variation to serve to the user session that matches the ``EntityId`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                entity_override_property = evidently.CfnFeature.EntityOverrideProperty(
                    entity_id="entityId",
                    variation="variation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFeature.EntityOverrideProperty.__init__)
                check_type(argname="argument entity_id", value=entity_id, expected_type=type_hints["entity_id"])
                check_type(argname="argument variation", value=variation, expected_type=type_hints["variation"])
            self._values: typing.Dict[str, typing.Any] = {}
            if entity_id is not None:
                self._values["entity_id"] = entity_id
            if variation is not None:
                self._values["variation"] = variation

        @builtins.property
        def entity_id(self) -> typing.Optional[builtins.str]:
            '''The entity ID to be served the variation specified in ``Variation`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html#cfn-evidently-feature-entityoverride-entityid
            '''
            result = self._values.get("entity_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def variation(self) -> typing.Optional[builtins.str]:
            '''The name of the variation to serve to the user session that matches the ``EntityId`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html#cfn-evidently-feature-entityoverride-variation
            '''
            result = self._values.get("variation")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnFeature.VariationObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "long_value": "longValue",
            "string_value": "stringValue",
            "variation_name": "variationName",
        },
    )
    class VariationObjectProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            double_value: typing.Optional[jsii.Number] = None,
            long_value: typing.Optional[jsii.Number] = None,
            string_value: typing.Optional[builtins.str] = None,
            variation_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure contains the name and variation value of one variation of a feature.

            It can contain only one of the following parameters: ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` .

            :param boolean_value: The value assigned to this variation, if the variation type is boolean.
            :param double_value: The value assigned to this variation, if the variation type is a double.
            :param long_value: The value assigned to this variation, if the variation type is a long.
            :param string_value: The value assigned to this variation, if the variation type is a string.
            :param variation_name: A name for the variation. It can include up to 127 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                variation_object_property = evidently.CfnFeature.VariationObjectProperty(
                    boolean_value=False,
                    double_value=123,
                    long_value=123,
                    string_value="stringValue",
                    variation_name="variationName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFeature.VariationObjectProperty.__init__)
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
                check_type(argname="argument variation_name", value=variation_name, expected_type=type_hints["variation_name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if long_value is not None:
                self._values["long_value"] = long_value
            if string_value is not None:
                self._values["string_value"] = string_value
            if variation_name is not None:
                self._values["variation_name"] = variation_name

        @builtins.property
        def boolean_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The value assigned to this variation, if the variation type is boolean.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def double_value(self) -> typing.Optional[jsii.Number]:
            '''The value assigned to this variation, if the variation type is a double.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def long_value(self) -> typing.Optional[jsii.Number]:
            '''The value assigned to this variation, if the variation type is a long.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-longvalue
            '''
            result = self._values.get("long_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''The value assigned to this variation, if the variation type is a string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def variation_name(self) -> typing.Optional[builtins.str]:
            '''A name for the variation.

            It can include up to 127 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-variationname
            '''
            result = self._values.get("variation_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariationObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnFeatureProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "project": "project",
        "variations": "variations",
        "default_variation": "defaultVariation",
        "description": "description",
        "entity_overrides": "entityOverrides",
        "evaluation_strategy": "evaluationStrategy",
        "tags": "tags",
    },
)
class CfnFeatureProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        project: builtins.str,
        variations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnFeature.VariationObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        default_variation: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        entity_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnFeature.EntityOverrideProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        evaluation_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFeature``.

        :param name: The name for the feature. It can include up to 127 characters.
        :param project: The name or ARN of the project that is to contain the new feature.
        :param variations: An array of structures that contain the configuration of the feature's different variations. Each ``VariationObject`` in the ``Variations`` array for a feature must have the same type of value ( ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` ).
        :param default_variation: The name of the variation to use as the default variation. The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature. This variation must also be listed in the ``Variations`` structure. If you omit ``DefaultVariation`` , the first variation listed in the ``Variations`` structure is used as the default variation.
        :param description: An optional description of the feature.
        :param entity_overrides: Specify users that should always be served a specific variation of a feature. Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.
        :param evaluation_strategy: Specify ``ALL_RULES`` to activate the traffic allocation specified by any ongoing launches or experiments. Specify ``DEFAULT_VARIATION`` to serve the default variation to all users instead.
        :param tags: Assigns one or more tags (key-value pairs) to the feature. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a feature. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_feature_props = evidently.CfnFeatureProps(
                name="name",
                project="project",
                variations=[evidently.CfnFeature.VariationObjectProperty(
                    boolean_value=False,
                    double_value=123,
                    long_value=123,
                    string_value="stringValue",
                    variation_name="variationName"
                )],
            
                # the properties below are optional
                default_variation="defaultVariation",
                description="description",
                entity_overrides=[evidently.CfnFeature.EntityOverrideProperty(
                    entity_id="entityId",
                    variation="variation"
                )],
                evaluation_strategy="evaluationStrategy",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFeatureProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument variations", value=variations, expected_type=type_hints["variations"])
            check_type(argname="argument default_variation", value=default_variation, expected_type=type_hints["default_variation"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument entity_overrides", value=entity_overrides, expected_type=type_hints["entity_overrides"])
            check_type(argname="argument evaluation_strategy", value=evaluation_strategy, expected_type=type_hints["evaluation_strategy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "project": project,
            "variations": variations,
        }
        if default_variation is not None:
            self._values["default_variation"] = default_variation
        if description is not None:
            self._values["description"] = description
        if entity_overrides is not None:
            self._values["entity_overrides"] = entity_overrides
        if evaluation_strategy is not None:
            self._values["evaluation_strategy"] = evaluation_strategy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the feature.

        It can include up to 127 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or ARN of the project that is to contain the new feature.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-project
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def variations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnFeature.VariationObjectProperty, _IResolvable_da3f097b]]]:
        '''An array of structures that contain the configuration of the feature's different variations.

        Each ``VariationObject`` in the ``Variations`` array for a feature must have the same type of value ( ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-variations
        '''
        result = self._values.get("variations")
        assert result is not None, "Required property 'variations' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnFeature.VariationObjectProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def default_variation(self) -> typing.Optional[builtins.str]:
        '''The name of the variation to use as the default variation.

        The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature.

        This variation must also be listed in the ``Variations`` structure.

        If you omit ``DefaultVariation`` , the first variation listed in the ``Variations`` structure is used as the default variation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-defaultvariation
        '''
        result = self._values.get("default_variation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the feature.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entity_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnFeature.EntityOverrideProperty, _IResolvable_da3f097b]]]]:
        '''Specify users that should always be served a specific variation of a feature.

        Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-entityoverrides
        '''
        result = self._values.get("entity_overrides")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnFeature.EntityOverrideProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def evaluation_strategy(self) -> typing.Optional[builtins.str]:
        '''Specify ``ALL_RULES`` to activate the traffic allocation specified by any ongoing launches or experiments.

        Specify ``DEFAULT_VARIATION`` to serve the default variation to all users instead.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-evaluationstrategy
        '''
        result = self._values.get("evaluation_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the feature.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a feature.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFeatureProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLaunch(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch",
):
    '''A CloudFormation ``AWS::Evidently::Launch``.

    Creates or updates a *launch* of a given feature. Before you create a launch, you must create the feature to use for the launch.

    You can use a launch to safely validate new features by serving them to a specified percentage of your users while you roll out the feature. You can monitor the performance of the new feature to help you decide when to ramp up traffic to more users. This helps you reduce risk and identify unintended consequences before you fully launch the feature.

    :cloudformationResource: AWS::Evidently::Launch
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_launch = evidently.CfnLaunch(self, "MyCfnLaunch",
            groups=[evidently.CfnLaunch.LaunchGroupObjectProperty(
                feature="feature",
                group_name="groupName",
                variation="variation",
        
                # the properties below are optional
                description="description"
            )],
            name="name",
            project="project",
            scheduled_splits_config=[evidently.CfnLaunch.StepConfigProperty(
                group_weights=[evidently.CfnLaunch.GroupToWeightProperty(
                    group_name="groupName",
                    split_weight=123
                )],
                start_time="startTime",
        
                # the properties below are optional
                segment_overrides=[evidently.CfnLaunch.SegmentOverrideProperty(
                    evaluation_order=123,
                    segment="segment",
                    weights=[evidently.CfnLaunch.GroupToWeightProperty(
                        group_name="groupName",
                        split_weight=123
                    )]
                )]
            )],
        
            # the properties below are optional
            description="description",
            execution_status=evidently.CfnLaunch.ExecutionStatusObjectProperty(
                status="status",
        
                # the properties below are optional
                desired_state="desiredState",
                reason="reason"
            ),
            metric_monitors=[evidently.CfnLaunch.MetricDefinitionObjectProperty(
                entity_id_key="entityIdKey",
                event_pattern="eventPattern",
                metric_name="metricName",
                value_key="valueKey",
        
                # the properties below are optional
                unit_label="unitLabel"
            )],
            randomization_salt="randomizationSalt",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnLaunch.LaunchGroupObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        name: builtins.str,
        project: builtins.str,
        scheduled_splits_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnLaunch.StepConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        description: typing.Optional[builtins.str] = None,
        execution_status: typing.Optional[typing.Union[typing.Union["CfnLaunch.ExecutionStatusObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        metric_monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnLaunch.MetricDefinitionObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        randomization_salt: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Evidently::Launch``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param groups: An array of structures that contains the feature and variations that are to be used for the launch. You can up to five launch groups in a launch.
        :param name: The name for the launch. It can include up to 127 characters.
        :param project: The name or ARN of the project that you want to create the launch in.
        :param scheduled_splits_config: An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.
        :param description: An optional description for the launch.
        :param execution_status: A structure that you can use to start and stop the launch.
        :param metric_monitors: An array of structures that define the metrics that will be used to monitor the launch performance. You can have up to three metric monitors in the array.
        :param randomization_salt: When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the launch name as the ``randomizationsSalt`` .
        :param tags: Assigns one or more tags (key-value pairs) to the launch. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a launch. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunch.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLaunchProps(
            groups=groups,
            name=name,
            project=project,
            scheduled_splits_config=scheduled_splits_config,
            description=description,
            execution_status=execution_status,
            metric_monitors=metric_monitors,
            randomization_salt=randomization_salt,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunch.inspect)
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
            type_hints = typing.get_type_hints(CfnLaunch._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the launch.

        For example, ``arn:aws:evidently:us-west-2:0123455678912:project/myProject/launch/myLaunch``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Assigns one or more tags (key-value pairs) to the launch.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a launch.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="groups")
    def groups(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.LaunchGroupObjectProperty", _IResolvable_da3f097b]]]:
        '''An array of structures that contains the feature and variations that are to be used for the launch.

        You can up to five launch groups in a launch.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-groups
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.LaunchGroupObjectProperty", _IResolvable_da3f097b]]], jsii.get(self, "groups"))

    @groups.setter
    def groups(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.LaunchGroupObjectProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunch, "groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the launch.

        It can include up to 127 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunch, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        '''The name or ARN of the project that you want to create the launch in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-project
        '''
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunch, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scheduledSplitsConfig")
    def scheduled_splits_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.StepConfigProperty", _IResolvable_da3f097b]]]:
        '''An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-scheduledsplitsconfig
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.StepConfigProperty", _IResolvable_da3f097b]]], jsii.get(self, "scheduledSplitsConfig"))

    @scheduled_splits_config.setter
    def scheduled_splits_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.StepConfigProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunch, "scheduled_splits_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledSplitsConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the launch.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunch, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionStatus")
    def execution_status(
        self,
    ) -> typing.Optional[typing.Union["CfnLaunch.ExecutionStatusObjectProperty", _IResolvable_da3f097b]]:
        '''A structure that you can use to start and stop the launch.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-executionstatus
        '''
        return typing.cast(typing.Optional[typing.Union["CfnLaunch.ExecutionStatusObjectProperty", _IResolvable_da3f097b]], jsii.get(self, "executionStatus"))

    @execution_status.setter
    def execution_status(
        self,
        value: typing.Optional[typing.Union["CfnLaunch.ExecutionStatusObjectProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunch, "execution_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionStatus", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metricMonitors")
    def metric_monitors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.MetricDefinitionObjectProperty", _IResolvable_da3f097b]]]]:
        '''An array of structures that define the metrics that will be used to monitor the launch performance.

        You can have up to three metric monitors in the array.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-metricmonitors
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.MetricDefinitionObjectProperty", _IResolvable_da3f097b]]]], jsii.get(self, "metricMonitors"))

    @metric_monitors.setter
    def metric_monitors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.MetricDefinitionObjectProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunch, "metric_monitors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricMonitors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="randomizationSalt")
    def randomization_salt(self) -> typing.Optional[builtins.str]:
        '''When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served.

        This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the launch name as the ``randomizationsSalt`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-randomizationsalt
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "randomizationSalt"))

    @randomization_salt.setter
    def randomization_salt(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunch, "randomization_salt").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "randomizationSalt", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.ExecutionStatusObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "status": "status",
            "desired_state": "desiredState",
            "reason": "reason",
        },
    )
    class ExecutionStatusObjectProperty:
        def __init__(
            self,
            *,
            status: builtins.str,
            desired_state: typing.Optional[builtins.str] = None,
            reason: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to start and stop the launch.

            :param status: To start the launch now, specify ``START`` for this parameter. If this launch is currently running and you want to stop it now, specify ``STOP`` .
            :param desired_state: If you are using AWS CloudFormation to stop this launch, specify either ``COMPLETED`` or ``CANCELLED`` here to indicate how to classify this experiment. If you omit this parameter, the default of ``COMPLETED`` is used.
            :param reason: If you are using AWS CloudFormation to stop this launch, this is an optional field that you can use to record why the launch is being stopped or cancelled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                execution_status_object_property = evidently.CfnLaunch.ExecutionStatusObjectProperty(
                    status="status",
                
                    # the properties below are optional
                    desired_state="desiredState",
                    reason="reason"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnLaunch.ExecutionStatusObjectProperty.__init__)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
                check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
            self._values: typing.Dict[str, typing.Any] = {
                "status": status,
            }
            if desired_state is not None:
                self._values["desired_state"] = desired_state
            if reason is not None:
                self._values["reason"] = reason

        @builtins.property
        def status(self) -> builtins.str:
            '''To start the launch now, specify ``START`` for this parameter.

            If this launch is currently running and you want to stop it now, specify ``STOP`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def desired_state(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to stop this launch, specify either ``COMPLETED`` or ``CANCELLED`` here to indicate how to classify this experiment.

            If you omit this parameter, the default of ``COMPLETED`` is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-desiredstate
            '''
            result = self._values.get("desired_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reason(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to stop this launch, this is an optional field that you can use to record why the launch is being stopped or cancelled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-reason
            '''
            result = self._values.get("reason")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionStatusObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.GroupToWeightProperty",
        jsii_struct_bases=[],
        name_mapping={"group_name": "groupName", "split_weight": "splitWeight"},
    )
    class GroupToWeightProperty:
        def __init__(
            self,
            *,
            group_name: builtins.str,
            split_weight: jsii.Number,
        ) -> None:
            '''A structure containing the percentage of launch traffic to allocate to one launch group.

            :param group_name: The name of the launch group. It can include up to 127 characters.
            :param split_weight: The portion of launch traffic to allocate to this launch group. This is represented in thousandths of a percent. For example, specify 20,000 to allocate 20% of the launch audience to this launch group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                group_to_weight_property = evidently.CfnLaunch.GroupToWeightProperty(
                    group_name="groupName",
                    split_weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnLaunch.GroupToWeightProperty.__init__)
                check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
                check_type(argname="argument split_weight", value=split_weight, expected_type=type_hints["split_weight"])
            self._values: typing.Dict[str, typing.Any] = {
                "group_name": group_name,
                "split_weight": split_weight,
            }

        @builtins.property
        def group_name(self) -> builtins.str:
            '''The name of the launch group.

            It can include up to 127 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html#cfn-evidently-launch-grouptoweight-groupname
            '''
            result = self._values.get("group_name")
            assert result is not None, "Required property 'group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def split_weight(self) -> jsii.Number:
            '''The portion of launch traffic to allocate to this launch group.

            This is represented in thousandths of a percent. For example, specify 20,000 to allocate 20% of the launch audience to this launch group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html#cfn-evidently-launch-grouptoweight-splitweight
            '''
            result = self._values.get("split_weight")
            assert result is not None, "Required property 'split_weight' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupToWeightProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.LaunchGroupObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "feature": "feature",
            "group_name": "groupName",
            "variation": "variation",
            "description": "description",
        },
    )
    class LaunchGroupObjectProperty:
        def __init__(
            self,
            *,
            feature: builtins.str,
            group_name: builtins.str,
            variation: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that defines one launch group in a launch.

            A launch group is a variation of the feature that you are including in the launch.

            :param feature: The feature that this launch is using.
            :param group_name: A name for this launch group. It can include up to 127 characters.
            :param variation: The feature variation to use for this launch group.
            :param description: A description of the launch group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                launch_group_object_property = evidently.CfnLaunch.LaunchGroupObjectProperty(
                    feature="feature",
                    group_name="groupName",
                    variation="variation",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnLaunch.LaunchGroupObjectProperty.__init__)
                check_type(argname="argument feature", value=feature, expected_type=type_hints["feature"])
                check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
                check_type(argname="argument variation", value=variation, expected_type=type_hints["variation"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[str, typing.Any] = {
                "feature": feature,
                "group_name": group_name,
                "variation": variation,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def feature(self) -> builtins.str:
            '''The feature that this launch is using.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-feature
            '''
            result = self._values.get("feature")
            assert result is not None, "Required property 'feature' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_name(self) -> builtins.str:
            '''A name for this launch group.

            It can include up to 127 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-groupname
            '''
            result = self._values.get("group_name")
            assert result is not None, "Required property 'group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variation(self) -> builtins.str:
            '''The feature variation to use for this launch group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-variation
            '''
            result = self._values.get("variation")
            assert result is not None, "Required property 'variation' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the launch group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchGroupObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.MetricDefinitionObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entity_id_key": "entityIdKey",
            "event_pattern": "eventPattern",
            "metric_name": "metricName",
            "value_key": "valueKey",
            "unit_label": "unitLabel",
        },
    )
    class MetricDefinitionObjectProperty:
        def __init__(
            self,
            *,
            entity_id_key: builtins.str,
            event_pattern: builtins.str,
            metric_name: builtins.str,
            value_key: builtins.str,
            unit_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines a metric that you want to use to evaluate the variations during a launch or experiment.

            :param entity_id_key: The entity, such as a user or session, that does an action that causes a metric value to be recorded. An example is ``userDetails.userID`` .
            :param event_pattern: The EventBridge event pattern that defines how the metric is recorded. For more information about EventBridge event patterns, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ .
            :param metric_name: A name for the metric. It can include up to 255 characters.
            :param value_key: The value that is tracked to produce the metric.
            :param unit_label: A label for the units that the metric is measuring.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                metric_definition_object_property = evidently.CfnLaunch.MetricDefinitionObjectProperty(
                    entity_id_key="entityIdKey",
                    event_pattern="eventPattern",
                    metric_name="metricName",
                    value_key="valueKey",
                
                    # the properties below are optional
                    unit_label="unitLabel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnLaunch.MetricDefinitionObjectProperty.__init__)
                check_type(argname="argument entity_id_key", value=entity_id_key, expected_type=type_hints["entity_id_key"])
                check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument value_key", value=value_key, expected_type=type_hints["value_key"])
                check_type(argname="argument unit_label", value=unit_label, expected_type=type_hints["unit_label"])
            self._values: typing.Dict[str, typing.Any] = {
                "entity_id_key": entity_id_key,
                "event_pattern": event_pattern,
                "metric_name": metric_name,
                "value_key": value_key,
            }
            if unit_label is not None:
                self._values["unit_label"] = unit_label

        @builtins.property
        def entity_id_key(self) -> builtins.str:
            '''The entity, such as a user or session, that does an action that causes a metric value to be recorded.

            An example is ``userDetails.userID`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-entityidkey
            '''
            result = self._values.get("entity_id_key")
            assert result is not None, "Required property 'entity_id_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def event_pattern(self) -> builtins.str:
            '''The EventBridge event pattern that defines how the metric is recorded.

            For more information about EventBridge event patterns, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-eventpattern
            '''
            result = self._values.get("event_pattern")
            assert result is not None, "Required property 'event_pattern' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''A name for the metric.

            It can include up to 255 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_key(self) -> builtins.str:
            '''The value that is tracked to produce the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-valuekey
            '''
            result = self._values.get("value_key")
            assert result is not None, "Required property 'value_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit_label(self) -> typing.Optional[builtins.str]:
            '''A label for the units that the metric is measuring.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-unitlabel
            '''
            result = self._values.get("unit_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDefinitionObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.SegmentOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "evaluation_order": "evaluationOrder",
            "segment": "segment",
            "weights": "weights",
        },
    )
    class SegmentOverrideProperty:
        def __init__(
            self,
            *,
            evaluation_order: jsii.Number,
            segment: builtins.str,
            weights: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnLaunch.GroupToWeightProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        ) -> None:
            '''
            :param evaluation_order: ``CfnLaunch.SegmentOverrideProperty.EvaluationOrder``.
            :param segment: ``CfnLaunch.SegmentOverrideProperty.Segment``.
            :param weights: ``CfnLaunch.SegmentOverrideProperty.Weights``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                segment_override_property = evidently.CfnLaunch.SegmentOverrideProperty(
                    evaluation_order=123,
                    segment="segment",
                    weights=[evidently.CfnLaunch.GroupToWeightProperty(
                        group_name="groupName",
                        split_weight=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnLaunch.SegmentOverrideProperty.__init__)
                check_type(argname="argument evaluation_order", value=evaluation_order, expected_type=type_hints["evaluation_order"])
                check_type(argname="argument segment", value=segment, expected_type=type_hints["segment"])
                check_type(argname="argument weights", value=weights, expected_type=type_hints["weights"])
            self._values: typing.Dict[str, typing.Any] = {
                "evaluation_order": evaluation_order,
                "segment": segment,
                "weights": weights,
            }

        @builtins.property
        def evaluation_order(self) -> jsii.Number:
            '''``CfnLaunch.SegmentOverrideProperty.EvaluationOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-evaluationorder
            '''
            result = self._values.get("evaluation_order")
            assert result is not None, "Required property 'evaluation_order' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def segment(self) -> builtins.str:
            '''``CfnLaunch.SegmentOverrideProperty.Segment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-segment
            '''
            result = self._values.get("segment")
            assert result is not None, "Required property 'segment' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def weights(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.GroupToWeightProperty", _IResolvable_da3f097b]]]:
            '''``CfnLaunch.SegmentOverrideProperty.Weights``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-weights
            '''
            result = self._values.get("weights")
            assert result is not None, "Required property 'weights' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.GroupToWeightProperty", _IResolvable_da3f097b]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.StepConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "group_weights": "groupWeights",
            "start_time": "startTime",
            "segment_overrides": "segmentOverrides",
        },
    )
    class StepConfigProperty:
        def __init__(
            self,
            *,
            group_weights: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnLaunch.GroupToWeightProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            start_time: builtins.str,
            segment_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnLaunch.SegmentOverrideProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''A structure that defines when each step of the launch is to start, and how much launch traffic is to be allocated to each variation during each step.

            :param group_weights: An array of structures that define how much launch traffic to allocate to each launch group during this step of the launch.
            :param start_time: The date and time to start this step of the launch. Use UTC format, ``yyyy-MM-ddTHH:mm:ssZ`` . For example, ``2025-11-25T23:59:59Z``
            :param segment_overrides: ``CfnLaunch.StepConfigProperty.SegmentOverrides``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                step_config_property = evidently.CfnLaunch.StepConfigProperty(
                    group_weights=[evidently.CfnLaunch.GroupToWeightProperty(
                        group_name="groupName",
                        split_weight=123
                    )],
                    start_time="startTime",
                
                    # the properties below are optional
                    segment_overrides=[evidently.CfnLaunch.SegmentOverrideProperty(
                        evaluation_order=123,
                        segment="segment",
                        weights=[evidently.CfnLaunch.GroupToWeightProperty(
                            group_name="groupName",
                            split_weight=123
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnLaunch.StepConfigProperty.__init__)
                check_type(argname="argument group_weights", value=group_weights, expected_type=type_hints["group_weights"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
                check_type(argname="argument segment_overrides", value=segment_overrides, expected_type=type_hints["segment_overrides"])
            self._values: typing.Dict[str, typing.Any] = {
                "group_weights": group_weights,
                "start_time": start_time,
            }
            if segment_overrides is not None:
                self._values["segment_overrides"] = segment_overrides

        @builtins.property
        def group_weights(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.GroupToWeightProperty", _IResolvable_da3f097b]]]:
            '''An array of structures that define how much launch traffic to allocate to each launch group during this step of the launch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-groupweights
            '''
            result = self._values.get("group_weights")
            assert result is not None, "Required property 'group_weights' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.GroupToWeightProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def start_time(self) -> builtins.str:
            '''The date and time to start this step of the launch.

            Use UTC format, ``yyyy-MM-ddTHH:mm:ssZ`` . For example, ``2025-11-25T23:59:59Z``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def segment_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.SegmentOverrideProperty", _IResolvable_da3f097b]]]]:
            '''``CfnLaunch.StepConfigProperty.SegmentOverrides``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-segmentoverrides
            '''
            result = self._values.get("segment_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnLaunch.SegmentOverrideProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnLaunchProps",
    jsii_struct_bases=[],
    name_mapping={
        "groups": "groups",
        "name": "name",
        "project": "project",
        "scheduled_splits_config": "scheduledSplitsConfig",
        "description": "description",
        "execution_status": "executionStatus",
        "metric_monitors": "metricMonitors",
        "randomization_salt": "randomizationSalt",
        "tags": "tags",
    },
)
class CfnLaunchProps:
    def __init__(
        self,
        *,
        groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnLaunch.LaunchGroupObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        name: builtins.str,
        project: builtins.str,
        scheduled_splits_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnLaunch.StepConfigProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        description: typing.Optional[builtins.str] = None,
        execution_status: typing.Optional[typing.Union[typing.Union[CfnLaunch.ExecutionStatusObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        metric_monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnLaunch.MetricDefinitionObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        randomization_salt: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLaunch``.

        :param groups: An array of structures that contains the feature and variations that are to be used for the launch. You can up to five launch groups in a launch.
        :param name: The name for the launch. It can include up to 127 characters.
        :param project: The name or ARN of the project that you want to create the launch in.
        :param scheduled_splits_config: An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.
        :param description: An optional description for the launch.
        :param execution_status: A structure that you can use to start and stop the launch.
        :param metric_monitors: An array of structures that define the metrics that will be used to monitor the launch performance. You can have up to three metric monitors in the array.
        :param randomization_salt: When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the launch name as the ``randomizationsSalt`` .
        :param tags: Assigns one or more tags (key-value pairs) to the launch. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a launch. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_launch_props = evidently.CfnLaunchProps(
                groups=[evidently.CfnLaunch.LaunchGroupObjectProperty(
                    feature="feature",
                    group_name="groupName",
                    variation="variation",
            
                    # the properties below are optional
                    description="description"
                )],
                name="name",
                project="project",
                scheduled_splits_config=[evidently.CfnLaunch.StepConfigProperty(
                    group_weights=[evidently.CfnLaunch.GroupToWeightProperty(
                        group_name="groupName",
                        split_weight=123
                    )],
                    start_time="startTime",
            
                    # the properties below are optional
                    segment_overrides=[evidently.CfnLaunch.SegmentOverrideProperty(
                        evaluation_order=123,
                        segment="segment",
                        weights=[evidently.CfnLaunch.GroupToWeightProperty(
                            group_name="groupName",
                            split_weight=123
                        )]
                    )]
                )],
            
                # the properties below are optional
                description="description",
                execution_status=evidently.CfnLaunch.ExecutionStatusObjectProperty(
                    status="status",
            
                    # the properties below are optional
                    desired_state="desiredState",
                    reason="reason"
                ),
                metric_monitors=[evidently.CfnLaunch.MetricDefinitionObjectProperty(
                    entity_id_key="entityIdKey",
                    event_pattern="eventPattern",
                    metric_name="metricName",
                    value_key="valueKey",
            
                    # the properties below are optional
                    unit_label="unitLabel"
                )],
                randomization_salt="randomizationSalt",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchProps.__init__)
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument scheduled_splits_config", value=scheduled_splits_config, expected_type=type_hints["scheduled_splits_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_status", value=execution_status, expected_type=type_hints["execution_status"])
            check_type(argname="argument metric_monitors", value=metric_monitors, expected_type=type_hints["metric_monitors"])
            check_type(argname="argument randomization_salt", value=randomization_salt, expected_type=type_hints["randomization_salt"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "groups": groups,
            "name": name,
            "project": project,
            "scheduled_splits_config": scheduled_splits_config,
        }
        if description is not None:
            self._values["description"] = description
        if execution_status is not None:
            self._values["execution_status"] = execution_status
        if metric_monitors is not None:
            self._values["metric_monitors"] = metric_monitors
        if randomization_salt is not None:
            self._values["randomization_salt"] = randomization_salt
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def groups(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnLaunch.LaunchGroupObjectProperty, _IResolvable_da3f097b]]]:
        '''An array of structures that contains the feature and variations that are to be used for the launch.

        You can up to five launch groups in a launch.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-groups
        '''
        result = self._values.get("groups")
        assert result is not None, "Required property 'groups' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnLaunch.LaunchGroupObjectProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the launch.

        It can include up to 127 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or ARN of the project that you want to create the launch in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-project
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scheduled_splits_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnLaunch.StepConfigProperty, _IResolvable_da3f097b]]]:
        '''An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-scheduledsplitsconfig
        '''
        result = self._values.get("scheduled_splits_config")
        assert result is not None, "Required property 'scheduled_splits_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnLaunch.StepConfigProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the launch.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_status(
        self,
    ) -> typing.Optional[typing.Union[CfnLaunch.ExecutionStatusObjectProperty, _IResolvable_da3f097b]]:
        '''A structure that you can use to start and stop the launch.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-executionstatus
        '''
        result = self._values.get("execution_status")
        return typing.cast(typing.Optional[typing.Union[CfnLaunch.ExecutionStatusObjectProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def metric_monitors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnLaunch.MetricDefinitionObjectProperty, _IResolvable_da3f097b]]]]:
        '''An array of structures that define the metrics that will be used to monitor the launch performance.

        You can have up to three metric monitors in the array.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-metricmonitors
        '''
        result = self._values.get("metric_monitors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnLaunch.MetricDefinitionObjectProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def randomization_salt(self) -> typing.Optional[builtins.str]:
        '''When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served.

        This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the launch name as the ``randomizationsSalt`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-randomizationsalt
        '''
        result = self._values.get("randomization_salt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the launch.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a launch.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnProject",
):
    '''A CloudFormation ``AWS::Evidently::Project``.

    Creates a project, which is the logical object in Evidently that can contain features, launches, and experiments. Use projects to group similar features together.

    :cloudformationResource: AWS::Evidently::Project
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_project = evidently.CfnProject(self, "MyCfnProject",
            name="name",
        
            # the properties below are optional
            data_delivery=evidently.CfnProject.DataDeliveryObjectProperty(
                log_group="logGroup",
                s3=evidently.CfnProject.S3DestinationProperty(
                    bucket_name="bucketName",
        
                    # the properties below are optional
                    prefix="prefix"
                )
            ),
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        data_delivery: typing.Optional[typing.Union[typing.Union["CfnProject.DataDeliveryObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Evidently::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name for the project. It can include up to 127 characters.
        :param data_delivery: A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so. If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view. You can't specify both ``CloudWatchLogs`` and ``S3Destination`` in the same operation.
        :param description: An optional description of the project.
        :param tags: Assigns one or more tags (key-value pairs) to the project. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a project. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnProject.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(
            name=name, data_delivery=data_delivery, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnProject.inspect)
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
            type_hints = typing.get_type_hints(CfnProject._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the project.

        For example, ``arn:aws:evidently:us-west-2:0123455678912:project/myProject``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Assigns one or more tags (key-value pairs) to the project.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a project.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the project.

        It can include up to 127 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProject, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataDelivery")
    def data_delivery(
        self,
    ) -> typing.Optional[typing.Union["CfnProject.DataDeliveryObjectProperty", _IResolvable_da3f097b]]:
        '''A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so.

        If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.

        You can't specify both ``CloudWatchLogs`` and ``S3Destination`` in the same operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-datadelivery
        '''
        return typing.cast(typing.Optional[typing.Union["CfnProject.DataDeliveryObjectProperty", _IResolvable_da3f097b]], jsii.get(self, "dataDelivery"))

    @data_delivery.setter
    def data_delivery(
        self,
        value: typing.Optional[typing.Union["CfnProject.DataDeliveryObjectProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProject, "data_delivery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDelivery", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProject, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnProject.DataDeliveryObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group": "logGroup", "s3": "s3"},
    )
    class DataDeliveryObjectProperty:
        def __init__(
            self,
            *,
            log_group: typing.Optional[builtins.str] = None,
            s3: typing.Optional[typing.Union[typing.Union["CfnProject.S3DestinationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A structure that contains information about where Evidently is to store evaluation events for longer term storage.

            :param log_group: If the project stores evaluation events in CloudWatch Logs , this structure stores the log group name.
            :param s3: If the project stores evaluation events in an Amazon S3 bucket, this structure stores the bucket name and bucket prefix.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                data_delivery_object_property = evidently.CfnProject.DataDeliveryObjectProperty(
                    log_group="logGroup",
                    s3=evidently.CfnProject.S3DestinationProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnProject.DataDeliveryObjectProperty.__init__)
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[str, typing.Any] = {}
            if log_group is not None:
                self._values["log_group"] = log_group
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def log_group(self) -> typing.Optional[builtins.str]:
            '''If the project stores evaluation events in CloudWatch Logs , this structure stores the log group name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html#cfn-evidently-project-datadeliveryobject-loggroup
            '''
            result = self._values.get("log_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union["CfnProject.S3DestinationProperty", _IResolvable_da3f097b]]:
            '''If the project stores evaluation events in an Amazon S3 bucket, this structure stores the bucket name and bucket prefix.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html#cfn-evidently-project-datadeliveryobject-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union["CfnProject.S3DestinationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataDeliveryObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnProject.S3DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "prefix": "prefix"},
    )
    class S3DestinationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''If the project stores evaluation events in an Amazon S3 bucket, this structure stores the bucket name and bucket prefix.

            :param bucket_name: The name of the bucket in which Evidently stores evaluation events.
            :param prefix: The bucket prefix in which Evidently stores evaluation events.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                s3_destination_property = evidently.CfnProject.S3DestinationProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnProject.S3DestinationProperty.__init__)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the bucket in which Evidently stores evaluation events.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html#cfn-evidently-project-s3destination-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The bucket prefix in which Evidently stores evaluation events.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html#cfn-evidently-project-s3destination-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "data_delivery": "dataDelivery",
        "description": "description",
        "tags": "tags",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        data_delivery: typing.Optional[typing.Union[typing.Union[CfnProject.DataDeliveryObjectProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProject``.

        :param name: The name for the project. It can include up to 127 characters.
        :param data_delivery: A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so. If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view. You can't specify both ``CloudWatchLogs`` and ``S3Destination`` in the same operation.
        :param description: An optional description of the project.
        :param tags: Assigns one or more tags (key-value pairs) to the project. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a project. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_project_props = evidently.CfnProjectProps(
                name="name",
            
                # the properties below are optional
                data_delivery=evidently.CfnProject.DataDeliveryObjectProperty(
                    log_group="logGroup",
                    s3=evidently.CfnProject.S3DestinationProperty(
                        bucket_name="bucketName",
            
                        # the properties below are optional
                        prefix="prefix"
                    )
                ),
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnProjectProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument data_delivery", value=data_delivery, expected_type=type_hints["data_delivery"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if data_delivery is not None:
            self._values["data_delivery"] = data_delivery
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the project.

        It can include up to 127 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_delivery(
        self,
    ) -> typing.Optional[typing.Union[CfnProject.DataDeliveryObjectProperty, _IResolvable_da3f097b]]:
        '''A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so.

        If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.

        You can't specify both ``CloudWatchLogs`` and ``S3Destination`` in the same operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-datadelivery
        '''
        result = self._values.get("data_delivery")
        return typing.cast(typing.Optional[typing.Union[CfnProject.DataDeliveryObjectProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the project.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a project.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSegment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnSegment",
):
    '''A CloudFormation ``AWS::Evidently::Segment``.

    :cloudformationResource: AWS::Evidently::Segment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_segment = evidently.CfnSegment(self, "MyCfnSegment",
            name="name",
        
            # the properties below are optional
            description="description",
            pattern="pattern",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pattern: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Evidently::Segment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Evidently::Segment.Name``.
        :param description: ``AWS::Evidently::Segment.Description``.
        :param pattern: ``AWS::Evidently::Segment.Pattern``.
        :param tags: ``AWS::Evidently::Segment.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSegment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSegmentProps(
            name=name, description=description, pattern=pattern, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSegment.inspect)
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
            type_hints = typing.get_type_hints(CfnSegment._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::Evidently::Segment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Evidently::Segment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSegment, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Evidently::Segment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSegment, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> typing.Optional[builtins.str]:
        '''``AWS::Evidently::Segment.Pattern``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-pattern
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSegment, "pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnSegmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "pattern": "pattern",
        "tags": "tags",
    },
)
class CfnSegmentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pattern: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSegment``.

        :param name: ``AWS::Evidently::Segment.Name``.
        :param description: ``AWS::Evidently::Segment.Description``.
        :param pattern: ``AWS::Evidently::Segment.Pattern``.
        :param tags: ``AWS::Evidently::Segment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_segment_props = evidently.CfnSegmentProps(
                name="name",
            
                # the properties below are optional
                description="description",
                pattern="pattern",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSegmentProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if pattern is not None:
            self._values["pattern"] = pattern
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Evidently::Segment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Evidently::Segment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pattern(self) -> typing.Optional[builtins.str]:
        '''``AWS::Evidently::Segment.Pattern``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-pattern
        '''
        result = self._values.get("pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::Evidently::Segment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSegmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnExperiment",
    "CfnExperimentProps",
    "CfnFeature",
    "CfnFeatureProps",
    "CfnLaunch",
    "CfnLaunchProps",
    "CfnProject",
    "CfnProjectProps",
    "CfnSegment",
    "CfnSegmentProps",
]

publication.publish()
