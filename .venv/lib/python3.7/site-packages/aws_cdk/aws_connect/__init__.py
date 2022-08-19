'''
# AWS::Connect Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_connect as connect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Connect construct libraries](https://constructs.dev/search?q=connect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Connect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Connect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Connect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Connect.html).

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
class CfnContactFlow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnContactFlow",
):
    '''A CloudFormation ``AWS::Connect::ContactFlow``.

    The ``AWS::Connect::ContactFlow`` resource specifies a contact flow for the specified Amazon Connect instance.

    :cloudformationResource: AWS::Connect::ContactFlow
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_contact_flow = connect.CfnContactFlow(self, "MyCfnContactFlow",
            content="content",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            description="description",
            state="state",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        content: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::ContactFlow``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: The content of the contact flow.
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param name: The name of the contact flow.
        :param description: The description of the contact flow.
        :param state: The state of the contact flow.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param type: The type of the contact flow. For descriptions of the available types, see `Choose a Contact Flow Type <https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types>`_ in the *Amazon Connect Administrator Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactFlow.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContactFlowProps(
            content=content,
            instance_arn=instance_arn,
            name=name,
            description=description,
            state=state,
            tags=tags,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactFlow.inspect)
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
            type_hints = typing.get_type_hints(CfnContactFlow._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrContactFlowArn")
    def attr_contact_flow_arn(self) -> builtins.str:
        '''``Ref`` returns the contact flow Amazon Resource Name (ARN). For example:.

        ``{ "Ref": "myContactFlowArn" }``

        :cloudformationAttribute: ContactFlowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContactFlowArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the contact flow.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-content
        '''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlow, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlow, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the contact flow.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlow, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the contact flow.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlow, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the contact flow.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlow, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the contact flow.

        For descriptions of the available types, see `Choose a Contact Flow Type <https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types>`_ in the *Amazon Connect Administrator Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlow, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.implements(_IInspectable_c2943556)
class CfnContactFlowModule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnContactFlowModule",
):
    '''A CloudFormation ``AWS::Connect::ContactFlowModule``.

    The ``AWS::Connect::ContactFlowModule`` resource specifies a contact flow module for the specified Amazon Connect instance.

    :cloudformationResource: AWS::Connect::ContactFlowModule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_contact_flow_module = connect.CfnContactFlowModule(self, "MyCfnContactFlowModule",
            content="content",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            description="description",
            state="state",
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
        content: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::ContactFlowModule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: The content of the contact flow module.
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param name: The name of the contact flow module.
        :param description: The description of the contact flow module.
        :param state: The state of the contact flow module.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactFlowModule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContactFlowModuleProps(
            content=content,
            instance_arn=instance_arn,
            name=name,
            description=description,
            state=state,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactFlowModule.inspect)
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
            type_hints = typing.get_type_hints(CfnContactFlowModule._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrContactFlowModuleArn")
    def attr_contact_flow_module_arn(self) -> builtins.str:
        '''``Ref`` returns the contact flow module Amazon Resource Name (ARN). For example:.

        ``{ "Ref": "myContactFlowModuleArn" }``

        :cloudformationAttribute: ContactFlowModuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContactFlowModuleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the contact flow module.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-content
        '''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlowModule, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlowModule, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the contact flow module.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlowModule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the contact flow module.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlowModule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the contact flow module.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactFlowModule, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnContactFlowModuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "instance_arn": "instanceArn",
        "name": "name",
        "description": "description",
        "state": "state",
        "tags": "tags",
    },
)
class CfnContactFlowModuleProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContactFlowModule``.

        :param content: The content of the contact flow module.
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param name: The name of the contact flow module.
        :param description: The description of the contact flow module.
        :param state: The state of the contact flow module.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_contact_flow_module_props = connect.CfnContactFlowModuleProps(
                content="content",
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                description="description",
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactFlowModuleProps.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(self) -> builtins.str:
        '''The content of the contact flow module.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the contact flow module.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the contact flow module.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the contact flow module.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactFlowModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnContactFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "instance_arn": "instanceArn",
        "name": "name",
        "description": "description",
        "state": "state",
        "tags": "tags",
        "type": "type",
    },
)
class CfnContactFlowProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnContactFlow``.

        :param content: The content of the contact flow.
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param name: The name of the contact flow.
        :param description: The description of the contact flow.
        :param state: The state of the contact flow.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param type: The type of the contact flow. For descriptions of the available types, see `Choose a Contact Flow Type <https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types>`_ in the *Amazon Connect Administrator Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_contact_flow_props = connect.CfnContactFlowProps(
                content="content",
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                description="description",
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactFlowProps.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def content(self) -> builtins.str:
        '''The content of the contact flow.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the contact flow.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the contact flow.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the contact flow.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the contact flow.

        For descriptions of the available types, see `Choose a Contact Flow Type <https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types>`_ in the *Amazon Connect Administrator Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnHoursOfOperation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnHoursOfOperation",
):
    '''A CloudFormation ``AWS::Connect::HoursOfOperation``.

    Creates hours of operation.

    :cloudformationResource: AWS::Connect::HoursOfOperation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_hours_of_operation = connect.CfnHoursOfOperation(self, "MyCfnHoursOfOperation",
            config=[connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                day="day",
                end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                ),
                start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                )
            )],
            instance_arn="instanceArn",
            name="name",
            time_zone="timeZone",
        
            # the properties below are optional
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
        config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        instance_arn: builtins.str,
        name: builtins.str,
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::HoursOfOperation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param config: Configuration information for the hours of operation.
        :param instance_arn: The Amazon Resource Name (ARN) for the instance.
        :param name: The name for the hours of operation.
        :param time_zone: The time zone for the hours of operation.
        :param description: The description for the hours of operation.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnHoursOfOperation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHoursOfOperationProps(
            config=config,
            instance_arn=instance_arn,
            name=name,
            time_zone=time_zone,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnHoursOfOperation.inspect)
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
            type_hints = typing.get_type_hints(CfnHoursOfOperation._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHoursOfOperationArn")
    def attr_hours_of_operation_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the hours of operation.

        :cloudformationAttribute: HoursOfOperationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHoursOfOperationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", _IResolvable_da3f097b]]]:
        '''Configuration information for the hours of operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-config
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", _IResolvable_da3f097b]]], jsii.get(self, "config"))

    @config.setter
    def config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnHoursOfOperation, "config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "config", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnHoursOfOperation, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the hours of operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnHoursOfOperation, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        '''The time zone for the hours of operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-timezone
        '''
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnHoursOfOperation, "time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the hours of operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnHoursOfOperation, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnHoursOfOperation.HoursOfOperationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"day": "day", "end_time": "endTime", "start_time": "startTime"},
    )
    class HoursOfOperationConfigProperty:
        def __init__(
            self,
            *,
            day: builtins.str,
            end_time: typing.Union[typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            start_time: typing.Union[typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''Contains information about the hours of operation.

            :param day: The day that the hours of operation applies to.
            :param end_time: The end time that your contact center closes.
            :param start_time: The start time that your contact center opens.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                hours_of_operation_config_property = connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                    day="day",
                    end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    ),
                    start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnHoursOfOperation.HoursOfOperationConfigProperty.__init__)
                check_type(argname="argument day", value=day, expected_type=type_hints["day"])
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[str, typing.Any] = {
                "day": day,
                "end_time": end_time,
                "start_time": start_time,
            }

        @builtins.property
        def day(self) -> builtins.str:
            '''The day that the hours of operation applies to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-day
            '''
            result = self._values.get("day")
            assert result is not None, "Required property 'day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time(
            self,
        ) -> typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_da3f097b]:
            '''The end time that your contact center closes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_da3f097b]:
            '''The start time that your contact center opens.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HoursOfOperationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty",
        jsii_struct_bases=[],
        name_mapping={"hours": "hours", "minutes": "minutes"},
    )
    class HoursOfOperationTimeSliceProperty:
        def __init__(self, *, hours: jsii.Number, minutes: jsii.Number) -> None:
            '''The start time or end time for an hours of operation.

            :param hours: The hours.
            :param minutes: The minutes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                hours_of_operation_time_slice_property = connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnHoursOfOperation.HoursOfOperationTimeSliceProperty.__init__)
                check_type(argname="argument hours", value=hours, expected_type=type_hints["hours"])
                check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
            self._values: typing.Dict[str, typing.Any] = {
                "hours": hours,
                "minutes": minutes,
            }

        @builtins.property
        def hours(self) -> jsii.Number:
            '''The hours.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html#cfn-connect-hoursofoperation-hoursofoperationtimeslice-hours
            '''
            result = self._values.get("hours")
            assert result is not None, "Required property 'hours' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def minutes(self) -> jsii.Number:
            '''The minutes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html#cfn-connect-hoursofoperation-hoursofoperationtimeslice-minutes
            '''
            result = self._values.get("minutes")
            assert result is not None, "Required property 'minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HoursOfOperationTimeSliceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnHoursOfOperationProps",
    jsii_struct_bases=[],
    name_mapping={
        "config": "config",
        "instance_arn": "instanceArn",
        "name": "name",
        "time_zone": "timeZone",
        "description": "description",
        "tags": "tags",
    },
)
class CfnHoursOfOperationProps:
    def __init__(
        self,
        *,
        config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        instance_arn: builtins.str,
        name: builtins.str,
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnHoursOfOperation``.

        :param config: Configuration information for the hours of operation.
        :param instance_arn: The Amazon Resource Name (ARN) for the instance.
        :param name: The name for the hours of operation.
        :param time_zone: The time zone for the hours of operation.
        :param description: The description for the hours of operation.
        :param tags: The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_hours_of_operation_props = connect.CfnHoursOfOperationProps(
                config=[connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                    day="day",
                    end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    ),
                    start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    )
                )],
                instance_arn="instanceArn",
                name="name",
                time_zone="timeZone",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnHoursOfOperationProps.__init__)
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "config": config,
            "instance_arn": instance_arn,
            "name": name,
            "time_zone": time_zone,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, _IResolvable_da3f097b]]]:
        '''Configuration information for the hours of operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-config
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the hours of operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_zone(self) -> builtins.str:
        '''The time zone for the hours of operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-timezone
        '''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the hours of operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHoursOfOperationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPhoneNumber(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnPhoneNumber",
):
    '''A CloudFormation ``AWS::Connect::PhoneNumber``.

    Claims a phone number to the specified Amazon Connect instance.

    :cloudformationResource: AWS::Connect::PhoneNumber
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_phone_number = connect.CfnPhoneNumber(self, "MyCfnPhoneNumber",
            country_code="countryCode",
            target_arn="targetArn",
            type="type",
        
            # the properties below are optional
            description="description",
            prefix="prefix",
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
        country_code: builtins.str,
        target_arn: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::PhoneNumber``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param country_code: The ISO country code.
        :param target_arn: The Amazon Resource Name (ARN) for Amazon Connect instances that phone numbers are claimed to.
        :param type: The type of phone number.
        :param description: The description of the phone number.
        :param prefix: The prefix of the phone number. If provided, it must contain ``+`` as part of the country code. *Pattern* : ``^\\\\+[0-9]{1,15}``
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPhoneNumber.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPhoneNumberProps(
            country_code=country_code,
            target_arn=target_arn,
            type=type,
            description=description,
            prefix=prefix,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPhoneNumber.inspect)
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
            type_hints = typing.get_type_hints(CfnPhoneNumber._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAddress")
    def attr_address(self) -> builtins.str:
        '''The phone number, in E.164 format.

        :cloudformationAttribute: Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPhoneNumberArn")
    def attr_phone_number_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the phone number.

        :cloudformationAttribute: PhoneNumberArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPhoneNumberArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        '''The ISO country code.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-countrycode
        '''
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPhoneNumber, "country_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for Amazon Connect instances that phone numbers are claimed to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-targetarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPhoneNumber, "target_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of phone number.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPhoneNumber, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the phone number.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPhoneNumber, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix of the phone number. If provided, it must contain ``+`` as part of the country code.

        *Pattern* : ``^\\\\+[0-9]{1,15}``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-prefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPhoneNumber, "prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnPhoneNumberProps",
    jsii_struct_bases=[],
    name_mapping={
        "country_code": "countryCode",
        "target_arn": "targetArn",
        "type": "type",
        "description": "description",
        "prefix": "prefix",
        "tags": "tags",
    },
)
class CfnPhoneNumberProps:
    def __init__(
        self,
        *,
        country_code: builtins.str,
        target_arn: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPhoneNumber``.

        :param country_code: The ISO country code.
        :param target_arn: The Amazon Resource Name (ARN) for Amazon Connect instances that phone numbers are claimed to.
        :param type: The type of phone number.
        :param description: The description of the phone number.
        :param prefix: The prefix of the phone number. If provided, it must contain ``+`` as part of the country code. *Pattern* : ``^\\\\+[0-9]{1,15}``
        :param tags: The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_phone_number_props = connect.CfnPhoneNumberProps(
                country_code="countryCode",
                target_arn="targetArn",
                type="type",
            
                # the properties below are optional
                description="description",
                prefix="prefix",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPhoneNumberProps.__init__)
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "country_code": country_code,
            "target_arn": target_arn,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def country_code(self) -> builtins.str:
        '''The ISO country code.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-countrycode
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for Amazon Connect instances that phone numbers are claimed to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of phone number.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the phone number.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix of the phone number. If provided, it must contain ``+`` as part of the country code.

        *Pattern* : ``^\\\\+[0-9]{1,15}``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPhoneNumberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnQuickConnect(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect",
):
    '''A CloudFormation ``AWS::Connect::QuickConnect``.

    The ``AWS::Connect::QuickConnnect`` resource specifies a quick connect for the specified Amazon Connect instance.

    :cloudformationResource: AWS::Connect::QuickConnect
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_quick_connect = connect.CfnQuickConnect(self, "MyCfnQuickConnect",
            instance_arn="instanceArn",
            name="name",
            quick_connect_config=connect.CfnQuickConnect.QuickConnectConfigProperty(
                quick_connect_type="quickConnectType",
        
                # the properties below are optional
                phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                    phone_number="phoneNumber"
                ),
                queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    queue_arn="queueArn"
                ),
                user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    user_arn="userArn"
                )
            ),
        
            # the properties below are optional
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
        instance_arn: builtins.str,
        name: builtins.str,
        quick_connect_config: typing.Union[typing.Union["CfnQuickConnect.QuickConnectConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::QuickConnect``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the quick connect.
        :param quick_connect_config: Contains information about the quick connect.
        :param description: The description of the quick connect.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnQuickConnect.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQuickConnectProps(
            instance_arn=instance_arn,
            name=name,
            quick_connect_config=quick_connect_config,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnQuickConnect.inspect)
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
            type_hints = typing.get_type_hints(CfnQuickConnect._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrQuickConnectArn")
    def attr_quick_connect_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the quick connect.

        :cloudformationAttribute: QuickConnectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQuickConnectArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnQuickConnect, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the quick connect.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnQuickConnect, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectConfig")
    def quick_connect_config(
        self,
    ) -> typing.Union["CfnQuickConnect.QuickConnectConfigProperty", _IResolvable_da3f097b]:
        '''Contains information about the quick connect.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-quickconnectconfig
        '''
        return typing.cast(typing.Union["CfnQuickConnect.QuickConnectConfigProperty", _IResolvable_da3f097b], jsii.get(self, "quickConnectConfig"))

    @quick_connect_config.setter
    def quick_connect_config(
        self,
        value: typing.Union["CfnQuickConnect.QuickConnectConfigProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnQuickConnect, "quick_connect_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quickConnectConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the quick connect.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnQuickConnect, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"phone_number": "phoneNumber"},
    )
    class PhoneNumberQuickConnectConfigProperty:
        def __init__(self, *, phone_number: builtins.str) -> None:
            '''Contains information about a phone number for a quick connect.

            :param phone_number: The phone number in E.164 format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                phone_number_quick_connect_config_property = connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                    phone_number="phoneNumber"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnQuickConnect.PhoneNumberQuickConnectConfigProperty.__init__)
                check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
            self._values: typing.Dict[str, typing.Any] = {
                "phone_number": phone_number,
            }

        @builtins.property
        def phone_number(self) -> builtins.str:
            '''The phone number in E.164 format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html#cfn-connect-quickconnect-phonenumberquickconnectconfig-phonenumber
            '''
            result = self._values.get("phone_number")
            assert result is not None, "Required property 'phone_number' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhoneNumberQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect.QueueQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_flow_arn": "contactFlowArn", "queue_arn": "queueArn"},
    )
    class QueueQuickConnectConfigProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            queue_arn: builtins.str,
        ) -> None:
            '''Contains information about a queue for a quick connect.

            The contact flow must be of type Transfer to Queue.

            :param contact_flow_arn: The Amazon Resource Name (ARN) of the contact flow.
            :param queue_arn: The Amazon Resource Name (ARN) of the queue.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                queue_quick_connect_config_property = connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    queue_arn="queueArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnQuickConnect.QueueQuickConnectConfigProperty.__init__)
                check_type(argname="argument contact_flow_arn", value=contact_flow_arn, expected_type=type_hints["contact_flow_arn"])
                check_type(argname="argument queue_arn", value=queue_arn, expected_type=type_hints["queue_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "queue_arn": queue_arn,
            }

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the contact flow.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def queue_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the queue.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-queuearn
            '''
            result = self._values.get("queue_arn")
            assert result is not None, "Required property 'queue_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueueQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect.QuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "quick_connect_type": "quickConnectType",
            "phone_config": "phoneConfig",
            "queue_config": "queueConfig",
            "user_config": "userConfig",
        },
    )
    class QuickConnectConfigProperty:
        def __init__(
            self,
            *,
            quick_connect_type: builtins.str,
            phone_config: typing.Optional[typing.Union[typing.Union["CfnQuickConnect.PhoneNumberQuickConnectConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            queue_config: typing.Optional[typing.Union[typing.Union["CfnQuickConnect.QueueQuickConnectConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            user_config: typing.Optional[typing.Union[typing.Union["CfnQuickConnect.UserQuickConnectConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains configuration settings for a quick connect.

            :param quick_connect_type: The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).
            :param phone_config: The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.
            :param queue_config: The queue configuration. This is required only if QuickConnectType is QUEUE.
            :param user_config: The user configuration. This is required only if QuickConnectType is USER.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                quick_connect_config_property = connect.CfnQuickConnect.QuickConnectConfigProperty(
                    quick_connect_type="quickConnectType",
                
                    # the properties below are optional
                    phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                        phone_number="phoneNumber"
                    ),
                    queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        queue_arn="queueArn"
                    ),
                    user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        user_arn="userArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnQuickConnect.QuickConnectConfigProperty.__init__)
                check_type(argname="argument quick_connect_type", value=quick_connect_type, expected_type=type_hints["quick_connect_type"])
                check_type(argname="argument phone_config", value=phone_config, expected_type=type_hints["phone_config"])
                check_type(argname="argument queue_config", value=queue_config, expected_type=type_hints["queue_config"])
                check_type(argname="argument user_config", value=user_config, expected_type=type_hints["user_config"])
            self._values: typing.Dict[str, typing.Any] = {
                "quick_connect_type": quick_connect_type,
            }
            if phone_config is not None:
                self._values["phone_config"] = phone_config
            if queue_config is not None:
                self._values["queue_config"] = queue_config
            if user_config is not None:
                self._values["user_config"] = user_config

        @builtins.property
        def quick_connect_type(self) -> builtins.str:
            '''The type of quick connect.

            In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-quickconnecttype
            '''
            result = self._values.get("quick_connect_type")
            assert result is not None, "Required property 'quick_connect_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def phone_config(
            self,
        ) -> typing.Optional[typing.Union["CfnQuickConnect.PhoneNumberQuickConnectConfigProperty", _IResolvable_da3f097b]]:
            '''The phone configuration.

            This is required only if QuickConnectType is PHONE_NUMBER.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-phoneconfig
            '''
            result = self._values.get("phone_config")
            return typing.cast(typing.Optional[typing.Union["CfnQuickConnect.PhoneNumberQuickConnectConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def queue_config(
            self,
        ) -> typing.Optional[typing.Union["CfnQuickConnect.QueueQuickConnectConfigProperty", _IResolvable_da3f097b]]:
            '''The queue configuration.

            This is required only if QuickConnectType is QUEUE.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-queueconfig
            '''
            result = self._values.get("queue_config")
            return typing.cast(typing.Optional[typing.Union["CfnQuickConnect.QueueQuickConnectConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def user_config(
            self,
        ) -> typing.Optional[typing.Union["CfnQuickConnect.UserQuickConnectConfigProperty", _IResolvable_da3f097b]]:
            '''The user configuration.

            This is required only if QuickConnectType is USER.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-userconfig
            '''
            result = self._values.get("user_config")
            return typing.cast(typing.Optional[typing.Union["CfnQuickConnect.UserQuickConnectConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect.UserQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_flow_arn": "contactFlowArn", "user_arn": "userArn"},
    )
    class UserQuickConnectConfigProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            user_arn: builtins.str,
        ) -> None:
            '''Contains information about the quick connect configuration settings for a user.

            The contact flow must be of type Transfer to Agent.

            :param contact_flow_arn: The Amazon Resource Name (ARN) of the contact flow.
            :param user_arn: The Amazon Resource Name (ARN) of the user.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                user_quick_connect_config_property = connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    user_arn="userArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnQuickConnect.UserQuickConnectConfigProperty.__init__)
                check_type(argname="argument contact_flow_arn", value=contact_flow_arn, expected_type=type_hints["contact_flow_arn"])
                check_type(argname="argument user_arn", value=user_arn, expected_type=type_hints["user_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "user_arn": user_arn,
            }

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the contact flow.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the user.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-userarn
            '''
            result = self._values.get("user_arn")
            assert result is not None, "Required property 'user_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnectProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "quick_connect_config": "quickConnectConfig",
        "description": "description",
        "tags": "tags",
    },
)
class CfnQuickConnectProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        quick_connect_config: typing.Union[typing.Union[CfnQuickConnect.QuickConnectConfigProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnQuickConnect``.

        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the quick connect.
        :param quick_connect_config: Contains information about the quick connect.
        :param description: The description of the quick connect.
        :param tags: The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_quick_connect_props = connect.CfnQuickConnectProps(
                instance_arn="instanceArn",
                name="name",
                quick_connect_config=connect.CfnQuickConnect.QuickConnectConfigProperty(
                    quick_connect_type="quickConnectType",
            
                    # the properties below are optional
                    phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                        phone_number="phoneNumber"
                    ),
                    queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        queue_arn="queueArn"
                    ),
                    user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        user_arn="userArn"
                    )
                ),
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnQuickConnectProps.__init__)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument quick_connect_config", value=quick_connect_config, expected_type=type_hints["quick_connect_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
            "quick_connect_config": quick_connect_config,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the quick connect.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def quick_connect_config(
        self,
    ) -> typing.Union[CfnQuickConnect.QuickConnectConfigProperty, _IResolvable_da3f097b]:
        '''Contains information about the quick connect.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-quickconnectconfig
        '''
        result = self._values.get("quick_connect_config")
        assert result is not None, "Required property 'quick_connect_config' is missing"
        return typing.cast(typing.Union[CfnQuickConnect.QuickConnectConfigProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the quick connect.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickConnectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTaskTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate",
):
    '''A CloudFormation ``AWS::Connect::TaskTemplate``.

    :cloudformationResource: AWS::Connect::TaskTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        # constraints: Any
        
        cfn_task_template = connect.CfnTaskTemplate(self, "MyCfnTaskTemplate",
            instance_arn="instanceArn",
        
            # the properties below are optional
            client_token="clientToken",
            constraints=constraints,
            contact_flow_arn="contactFlowArn",
            defaults=[connect.CfnTaskTemplate.DefaultFieldValueProperty(
                default_value="defaultValue",
                id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                    name="name"
                )
            )],
            description="description",
            fields=[connect.CfnTaskTemplate.FieldProperty(
                id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                    name="name"
                ),
                type="type",
        
                # the properties below are optional
                description="description",
                single_select_options=["singleSelectOptions"]
            )],
            name="name",
            status="status",
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
        instance_arn: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        constraints: typing.Any = None,
        contact_flow_arn: typing.Optional[builtins.str] = None,
        defaults: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTaskTemplate.DefaultFieldValueProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        description: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTaskTemplate.FieldProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::TaskTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: ``AWS::Connect::TaskTemplate.InstanceArn``.
        :param client_token: ``AWS::Connect::TaskTemplate.ClientToken``.
        :param constraints: ``AWS::Connect::TaskTemplate.Constraints``.
        :param contact_flow_arn: ``AWS::Connect::TaskTemplate.ContactFlowArn``.
        :param defaults: ``AWS::Connect::TaskTemplate.Defaults``.
        :param description: ``AWS::Connect::TaskTemplate.Description``.
        :param fields: ``AWS::Connect::TaskTemplate.Fields``.
        :param name: ``AWS::Connect::TaskTemplate.Name``.
        :param status: ``AWS::Connect::TaskTemplate.Status``.
        :param tags: ``AWS::Connect::TaskTemplate.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTaskTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTaskTemplateProps(
            instance_arn=instance_arn,
            client_token=client_token,
            constraints=constraints,
            contact_flow_arn=contact_flow_arn,
            defaults=defaults,
            description=description,
            fields=fields,
            name=name,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTaskTemplate.inspect)
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
            type_hints = typing.get_type_hints(CfnTaskTemplate._render_properties)
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
        '''``AWS::Connect::TaskTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="constraints")
    def constraints(self) -> typing.Any:
        '''``AWS::Connect::TaskTemplate.Constraints``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-constraints
        '''
        return typing.cast(typing.Any, jsii.get(self, "constraints"))

    @constraints.setter
    def constraints(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "constraints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constraints", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::TaskTemplate.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.ClientToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-clienttoken
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "client_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowArn")
    def contact_flow_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.ContactFlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-contactflowarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactFlowArn"))

    @contact_flow_arn.setter
    def contact_flow_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "contact_flow_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactFlowArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaults")
    def defaults(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTaskTemplate.DefaultFieldValueProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::Connect::TaskTemplate.Defaults``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-defaults
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTaskTemplate.DefaultFieldValueProperty", _IResolvable_da3f097b]]]], jsii.get(self, "defaults"))

    @defaults.setter
    def defaults(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTaskTemplate.DefaultFieldValueProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "defaults").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaults", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fields")
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTaskTemplate.FieldProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::Connect::TaskTemplate.Fields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-fields
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTaskTemplate.FieldProperty", _IResolvable_da3f097b]]]], jsii.get(self, "fields"))

    @fields.setter
    def fields(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTaskTemplate.FieldProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTaskTemplate, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.DefaultFieldValueProperty",
        jsii_struct_bases=[],
        name_mapping={"default_value": "defaultValue", "id": "id"},
    )
    class DefaultFieldValueProperty:
        def __init__(
            self,
            *,
            default_value: builtins.str,
            id: typing.Union[typing.Union["CfnTaskTemplate.FieldIdentifierProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''
            :param default_value: ``CfnTaskTemplate.DefaultFieldValueProperty.DefaultValue``.
            :param id: ``CfnTaskTemplate.DefaultFieldValueProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                default_field_value_property = connect.CfnTaskTemplate.DefaultFieldValueProperty(
                    default_value="defaultValue",
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTaskTemplate.DefaultFieldValueProperty.__init__)
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[str, typing.Any] = {
                "default_value": default_value,
                "id": id,
            }

        @builtins.property
        def default_value(self) -> builtins.str:
            '''``CfnTaskTemplate.DefaultFieldValueProperty.DefaultValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html#cfn-connect-tasktemplate-defaultfieldvalue-defaultvalue
            '''
            result = self._values.get("default_value")
            assert result is not None, "Required property 'default_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(
            self,
        ) -> typing.Union["CfnTaskTemplate.FieldIdentifierProperty", _IResolvable_da3f097b]:
            '''``CfnTaskTemplate.DefaultFieldValueProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html#cfn-connect-tasktemplate-defaultfieldvalue-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(typing.Union["CfnTaskTemplate.FieldIdentifierProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultFieldValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.FieldIdentifierProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class FieldIdentifierProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''
            :param name: ``CfnTaskTemplate.FieldIdentifierProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-fieldidentifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                field_identifier_property = connect.CfnTaskTemplate.FieldIdentifierProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTaskTemplate.FieldIdentifierProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnTaskTemplate.FieldIdentifierProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-fieldidentifier.html#cfn-connect-tasktemplate-fieldidentifier-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldIdentifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.FieldProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "type": "type",
            "description": "description",
            "single_select_options": "singleSelectOptions",
        },
    )
    class FieldProperty:
        def __init__(
            self,
            *,
            id: typing.Union[typing.Union["CfnTaskTemplate.FieldIdentifierProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            type: builtins.str,
            description: typing.Optional[builtins.str] = None,
            single_select_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param id: ``CfnTaskTemplate.FieldProperty.Id``.
            :param type: ``CfnTaskTemplate.FieldProperty.Type``.
            :param description: ``CfnTaskTemplate.FieldProperty.Description``.
            :param single_select_options: ``CfnTaskTemplate.FieldProperty.SingleSelectOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                field_property = connect.CfnTaskTemplate.FieldProperty(
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    ),
                    type="type",
                
                    # the properties below are optional
                    description="description",
                    single_select_options=["singleSelectOptions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTaskTemplate.FieldProperty.__init__)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument single_select_options", value=single_select_options, expected_type=type_hints["single_select_options"])
            self._values: typing.Dict[str, typing.Any] = {
                "id": id,
                "type": type,
            }
            if description is not None:
                self._values["description"] = description
            if single_select_options is not None:
                self._values["single_select_options"] = single_select_options

        @builtins.property
        def id(
            self,
        ) -> typing.Union["CfnTaskTemplate.FieldIdentifierProperty", _IResolvable_da3f097b]:
            '''``CfnTaskTemplate.FieldProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(typing.Union["CfnTaskTemplate.FieldIdentifierProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnTaskTemplate.FieldProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnTaskTemplate.FieldProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def single_select_options(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnTaskTemplate.FieldProperty.SingleSelectOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-singleselectoptions
            '''
            result = self._values.get("single_select_options")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "client_token": "clientToken",
        "constraints": "constraints",
        "contact_flow_arn": "contactFlowArn",
        "defaults": "defaults",
        "description": "description",
        "fields": "fields",
        "name": "name",
        "status": "status",
        "tags": "tags",
    },
)
class CfnTaskTemplateProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        constraints: typing.Any = None,
        contact_flow_arn: typing.Optional[builtins.str] = None,
        defaults: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTaskTemplate.DefaultFieldValueProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        description: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTaskTemplate.FieldProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTaskTemplate``.

        :param instance_arn: ``AWS::Connect::TaskTemplate.InstanceArn``.
        :param client_token: ``AWS::Connect::TaskTemplate.ClientToken``.
        :param constraints: ``AWS::Connect::TaskTemplate.Constraints``.
        :param contact_flow_arn: ``AWS::Connect::TaskTemplate.ContactFlowArn``.
        :param defaults: ``AWS::Connect::TaskTemplate.Defaults``.
        :param description: ``AWS::Connect::TaskTemplate.Description``.
        :param fields: ``AWS::Connect::TaskTemplate.Fields``.
        :param name: ``AWS::Connect::TaskTemplate.Name``.
        :param status: ``AWS::Connect::TaskTemplate.Status``.
        :param tags: ``AWS::Connect::TaskTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            # constraints: Any
            
            cfn_task_template_props = connect.CfnTaskTemplateProps(
                instance_arn="instanceArn",
            
                # the properties below are optional
                client_token="clientToken",
                constraints=constraints,
                contact_flow_arn="contactFlowArn",
                defaults=[connect.CfnTaskTemplate.DefaultFieldValueProperty(
                    default_value="defaultValue",
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    )
                )],
                description="description",
                fields=[connect.CfnTaskTemplate.FieldProperty(
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    ),
                    type="type",
            
                    # the properties below are optional
                    description="description",
                    single_select_options=["singleSelectOptions"]
                )],
                name="name",
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTaskTemplateProps.__init__)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument constraints", value=constraints, expected_type=type_hints["constraints"])
            check_type(argname="argument contact_flow_arn", value=contact_flow_arn, expected_type=type_hints["contact_flow_arn"])
            check_type(argname="argument defaults", value=defaults, expected_type=type_hints["defaults"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if constraints is not None:
            self._values["constraints"] = constraints
        if contact_flow_arn is not None:
            self._values["contact_flow_arn"] = contact_flow_arn
        if defaults is not None:
            self._values["defaults"] = defaults
        if description is not None:
            self._values["description"] = description
        if fields is not None:
            self._values["fields"] = fields
        if name is not None:
            self._values["name"] = name
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::TaskTemplate.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.ClientToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def constraints(self) -> typing.Any:
        '''``AWS::Connect::TaskTemplate.Constraints``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-constraints
        '''
        result = self._values.get("constraints")
        return typing.cast(typing.Any, result)

    @builtins.property
    def contact_flow_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.ContactFlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-contactflowarn
        '''
        result = self._values.get("contact_flow_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def defaults(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTaskTemplate.DefaultFieldValueProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::Connect::TaskTemplate.Defaults``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-defaults
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTaskTemplate.DefaultFieldValueProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTaskTemplate.FieldProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::Connect::TaskTemplate.Fields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-fields
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTaskTemplate.FieldProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::TaskTemplate.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::Connect::TaskTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTaskTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnUser(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnUser",
):
    '''A CloudFormation ``AWS::Connect::User``.

    Creates a user account for the specified Amazon Connect instance.

    For information about how to create user accounts using the Amazon Connect console, see `Add Users <https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html>`_ in the *Amazon Connect Administrator Guide* .

    :cloudformationResource: AWS::Connect::User
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_user = connect.CfnUser(self, "MyCfnUser",
            instance_arn="instanceArn",
            phone_config=connect.CfnUser.UserPhoneConfigProperty(
                phone_type="phoneType",
        
                # the properties below are optional
                after_contact_work_time_limit=123,
                auto_accept=False,
                desk_phone_number="deskPhoneNumber"
            ),
            routing_profile_arn="routingProfileArn",
            security_profile_arns=["securityProfileArns"],
            username="username",
        
            # the properties below are optional
            directory_user_id="directoryUserId",
            hierarchy_group_arn="hierarchyGroupArn",
            identity_info=connect.CfnUser.UserIdentityInfoProperty(
                email="email",
                first_name="firstName",
                last_name="lastName"
            ),
            password="password",
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
        instance_arn: builtins.str,
        phone_config: typing.Union[typing.Union["CfnUser.UserPhoneConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        routing_profile_arn: builtins.str,
        security_profile_arns: typing.Sequence[builtins.str],
        username: builtins.str,
        directory_user_id: typing.Optional[builtins.str] = None,
        hierarchy_group_arn: typing.Optional[builtins.str] = None,
        identity_info: typing.Optional[typing.Union[typing.Union["CfnUser.UserIdentityInfoProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param phone_config: Information about the phone configuration for the user.
        :param routing_profile_arn: The Amazon Resource Name (ARN) of the user's routing profile.
        :param security_profile_arns: The Amazon Resource Name (ARN) of the user's security profile.
        :param username: The user name assigned to the user account.
        :param directory_user_id: The identifier of the user account in the directory used for identity management.
        :param hierarchy_group_arn: The Amazon Resource Name (ARN) of the user's hierarchy group.
        :param identity_info: Information about the user identity.
        :param password: The user's password.
        :param tags: The tags.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnUser.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            instance_arn=instance_arn,
            phone_config=phone_config,
            routing_profile_arn=routing_profile_arn,
            security_profile_arns=security_profile_arns,
            username=username,
            directory_user_id=directory_user_id,
            hierarchy_group_arn=hierarchy_group_arn,
            identity_info=identity_info,
            password=password,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnUser.inspect)
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
            type_hints = typing.get_type_hints(CfnUser._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserArn")
    def attr_user_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user.

        :cloudformationAttribute: UserArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="phoneConfig")
    def phone_config(
        self,
    ) -> typing.Union["CfnUser.UserPhoneConfigProperty", _IResolvable_da3f097b]:
        '''Information about the phone configuration for the user.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-phoneconfig
        '''
        return typing.cast(typing.Union["CfnUser.UserPhoneConfigProperty", _IResolvable_da3f097b], jsii.get(self, "phoneConfig"))

    @phone_config.setter
    def phone_config(
        self,
        value: typing.Union["CfnUser.UserPhoneConfigProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "phone_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routingProfileArn")
    def routing_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user's routing profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-routingprofilearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "routingProfileArn"))

    @routing_profile_arn.setter
    def routing_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "routing_profile_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingProfileArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityProfileArns")
    def security_profile_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Name (ARN) of the user's security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-securityprofilearns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityProfileArns"))

    @security_profile_arns.setter
    def security_profile_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "security_profile_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProfileArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        '''The user name assigned to the user account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-username
        '''
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="directoryUserId")
    def directory_user_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the user account in the directory used for identity management.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-directoryuserid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryUserId"))

    @directory_user_id.setter
    def directory_user_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "directory_user_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryUserId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hierarchyGroupArn")
    def hierarchy_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the user's hierarchy group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-hierarchygrouparn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hierarchyGroupArn"))

    @hierarchy_group_arn.setter
    def hierarchy_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "hierarchy_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hierarchyGroupArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityInfo")
    def identity_info(
        self,
    ) -> typing.Optional[typing.Union["CfnUser.UserIdentityInfoProperty", _IResolvable_da3f097b]]:
        '''Information about the user identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-identityinfo
        '''
        return typing.cast(typing.Optional[typing.Union["CfnUser.UserIdentityInfoProperty", _IResolvable_da3f097b]], jsii.get(self, "identityInfo"))

    @identity_info.setter
    def identity_info(
        self,
        value: typing.Optional[typing.Union["CfnUser.UserIdentityInfoProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "identity_info").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityInfo", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The user's password.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-password
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUser, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnUser.UserIdentityInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "email": "email",
            "first_name": "firstName",
            "last_name": "lastName",
        },
    )
    class UserIdentityInfoProperty:
        def __init__(
            self,
            *,
            email: typing.Optional[builtins.str] = None,
            first_name: typing.Optional[builtins.str] = None,
            last_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the identity of a user.

            :param email: The email address. If you are using SAML for identity management and include this parameter, an error is returned.
            :param first_name: The first name. This is required if you are using Amazon Connect or SAML for identity management.
            :param last_name: The last name. This is required if you are using Amazon Connect or SAML for identity management.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                user_identity_info_property = connect.CfnUser.UserIdentityInfoProperty(
                    email="email",
                    first_name="firstName",
                    last_name="lastName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnUser.UserIdentityInfoProperty.__init__)
                check_type(argname="argument email", value=email, expected_type=type_hints["email"])
                check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
                check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if email is not None:
                self._values["email"] = email
            if first_name is not None:
                self._values["first_name"] = first_name
            if last_name is not None:
                self._values["last_name"] = last_name

        @builtins.property
        def email(self) -> typing.Optional[builtins.str]:
            '''The email address.

            If you are using SAML for identity management and include this parameter, an error is returned.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-email
            '''
            result = self._values.get("email")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_name(self) -> typing.Optional[builtins.str]:
            '''The first name.

            This is required if you are using Amazon Connect or SAML for identity management.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_name(self) -> typing.Optional[builtins.str]:
            '''The last name.

            This is required if you are using Amazon Connect or SAML for identity management.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserIdentityInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnUser.UserPhoneConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "phone_type": "phoneType",
            "after_contact_work_time_limit": "afterContactWorkTimeLimit",
            "auto_accept": "autoAccept",
            "desk_phone_number": "deskPhoneNumber",
        },
    )
    class UserPhoneConfigProperty:
        def __init__(
            self,
            *,
            phone_type: builtins.str,
            after_contact_work_time_limit: typing.Optional[jsii.Number] = None,
            auto_accept: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            desk_phone_number: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the phone configuration settings for a user.

            :param phone_type: The phone type.
            :param after_contact_work_time_limit: The After Call Work (ACW) timeout setting, in seconds.
            :param auto_accept: The Auto accept setting.
            :param desk_phone_number: The phone number for the user's desk phone.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                user_phone_config_property = connect.CfnUser.UserPhoneConfigProperty(
                    phone_type="phoneType",
                
                    # the properties below are optional
                    after_contact_work_time_limit=123,
                    auto_accept=False,
                    desk_phone_number="deskPhoneNumber"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnUser.UserPhoneConfigProperty.__init__)
                check_type(argname="argument phone_type", value=phone_type, expected_type=type_hints["phone_type"])
                check_type(argname="argument after_contact_work_time_limit", value=after_contact_work_time_limit, expected_type=type_hints["after_contact_work_time_limit"])
                check_type(argname="argument auto_accept", value=auto_accept, expected_type=type_hints["auto_accept"])
                check_type(argname="argument desk_phone_number", value=desk_phone_number, expected_type=type_hints["desk_phone_number"])
            self._values: typing.Dict[str, typing.Any] = {
                "phone_type": phone_type,
            }
            if after_contact_work_time_limit is not None:
                self._values["after_contact_work_time_limit"] = after_contact_work_time_limit
            if auto_accept is not None:
                self._values["auto_accept"] = auto_accept
            if desk_phone_number is not None:
                self._values["desk_phone_number"] = desk_phone_number

        @builtins.property
        def phone_type(self) -> builtins.str:
            '''The phone type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-phonetype
            '''
            result = self._values.get("phone_type")
            assert result is not None, "Required property 'phone_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def after_contact_work_time_limit(self) -> typing.Optional[jsii.Number]:
            '''The After Call Work (ACW) timeout setting, in seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-aftercontactworktimelimit
            '''
            result = self._values.get("after_contact_work_time_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def auto_accept(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The Auto accept setting.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-autoaccept
            '''
            result = self._values.get("auto_accept")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def desk_phone_number(self) -> typing.Optional[builtins.str]:
            '''The phone number for the user's desk phone.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-deskphonenumber
            '''
            result = self._values.get("desk_phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPhoneConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnUserHierarchyGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnUserHierarchyGroup",
):
    '''A CloudFormation ``AWS::Connect::UserHierarchyGroup``.

    Creates a new user hierarchy group.

    :cloudformationResource: AWS::Connect::UserHierarchyGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_user_hierarchy_group = connect.CfnUserHierarchyGroup(self, "MyCfnUserHierarchyGroup",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            parent_group_arn="parentGroupArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        parent_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::UserHierarchyGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The Amazon Resource Name (ARN) of the user hierarchy group.
        :param name: The name of the user hierarchy group.
        :param parent_group_arn: The Amazon Resource Name (ARN) of the parent group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnUserHierarchyGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserHierarchyGroupProps(
            instance_arn=instance_arn, name=name, parent_group_arn=parent_group_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnUserHierarchyGroup.inspect)
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
            type_hints = typing.get_type_hints(CfnUserHierarchyGroup._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserHierarchyGroupArn")
    def attr_user_hierarchy_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the user hierarchy group.

        :cloudformationAttribute: UserHierarchyGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserHierarchyGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user hierarchy group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUserHierarchyGroup, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the user hierarchy group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUserHierarchyGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parentGroupArn")
    def parent_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the parent group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-parentgrouparn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentGroupArn"))

    @parent_group_arn.setter
    def parent_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnUserHierarchyGroup, "parent_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentGroupArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnUserHierarchyGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "parent_group_arn": "parentGroupArn",
    },
)
class CfnUserHierarchyGroupProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        parent_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnUserHierarchyGroup``.

        :param instance_arn: The Amazon Resource Name (ARN) of the user hierarchy group.
        :param name: The name of the user hierarchy group.
        :param parent_group_arn: The Amazon Resource Name (ARN) of the parent group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_user_hierarchy_group_props = connect.CfnUserHierarchyGroupProps(
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                parent_group_arn="parentGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnUserHierarchyGroupProps.__init__)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_group_arn", value=parent_group_arn, expected_type=type_hints["parent_group_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if parent_group_arn is not None:
            self._values["parent_group_arn"] = parent_group_arn

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user hierarchy group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the user hierarchy group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the parent group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-parentgrouparn
        '''
        result = self._values.get("parent_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserHierarchyGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "phone_config": "phoneConfig",
        "routing_profile_arn": "routingProfileArn",
        "security_profile_arns": "securityProfileArns",
        "username": "username",
        "directory_user_id": "directoryUserId",
        "hierarchy_group_arn": "hierarchyGroupArn",
        "identity_info": "identityInfo",
        "password": "password",
        "tags": "tags",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        phone_config: typing.Union[typing.Union[CfnUser.UserPhoneConfigProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        routing_profile_arn: builtins.str,
        security_profile_arns: typing.Sequence[builtins.str],
        username: builtins.str,
        directory_user_id: typing.Optional[builtins.str] = None,
        hierarchy_group_arn: typing.Optional[builtins.str] = None,
        identity_info: typing.Optional[typing.Union[typing.Union[CfnUser.UserIdentityInfoProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUser``.

        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param phone_config: Information about the phone configuration for the user.
        :param routing_profile_arn: The Amazon Resource Name (ARN) of the user's routing profile.
        :param security_profile_arns: The Amazon Resource Name (ARN) of the user's security profile.
        :param username: The user name assigned to the user account.
        :param directory_user_id: The identifier of the user account in the directory used for identity management.
        :param hierarchy_group_arn: The Amazon Resource Name (ARN) of the user's hierarchy group.
        :param identity_info: Information about the user identity.
        :param password: The user's password.
        :param tags: The tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_user_props = connect.CfnUserProps(
                instance_arn="instanceArn",
                phone_config=connect.CfnUser.UserPhoneConfigProperty(
                    phone_type="phoneType",
            
                    # the properties below are optional
                    after_contact_work_time_limit=123,
                    auto_accept=False,
                    desk_phone_number="deskPhoneNumber"
                ),
                routing_profile_arn="routingProfileArn",
                security_profile_arns=["securityProfileArns"],
                username="username",
            
                # the properties below are optional
                directory_user_id="directoryUserId",
                hierarchy_group_arn="hierarchyGroupArn",
                identity_info=connect.CfnUser.UserIdentityInfoProperty(
                    email="email",
                    first_name="firstName",
                    last_name="lastName"
                ),
                password="password",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnUserProps.__init__)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument phone_config", value=phone_config, expected_type=type_hints["phone_config"])
            check_type(argname="argument routing_profile_arn", value=routing_profile_arn, expected_type=type_hints["routing_profile_arn"])
            check_type(argname="argument security_profile_arns", value=security_profile_arns, expected_type=type_hints["security_profile_arns"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument directory_user_id", value=directory_user_id, expected_type=type_hints["directory_user_id"])
            check_type(argname="argument hierarchy_group_arn", value=hierarchy_group_arn, expected_type=type_hints["hierarchy_group_arn"])
            check_type(argname="argument identity_info", value=identity_info, expected_type=type_hints["identity_info"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "phone_config": phone_config,
            "routing_profile_arn": routing_profile_arn,
            "security_profile_arns": security_profile_arns,
            "username": username,
        }
        if directory_user_id is not None:
            self._values["directory_user_id"] = directory_user_id
        if hierarchy_group_arn is not None:
            self._values["hierarchy_group_arn"] = hierarchy_group_arn
        if identity_info is not None:
            self._values["identity_info"] = identity_info
        if password is not None:
            self._values["password"] = password
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_config(
        self,
    ) -> typing.Union[CfnUser.UserPhoneConfigProperty, _IResolvable_da3f097b]:
        '''Information about the phone configuration for the user.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-phoneconfig
        '''
        result = self._values.get("phone_config")
        assert result is not None, "Required property 'phone_config' is missing"
        return typing.cast(typing.Union[CfnUser.UserPhoneConfigProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def routing_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user's routing profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-routingprofilearn
        '''
        result = self._values.get("routing_profile_arn")
        assert result is not None, "Required property 'routing_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_profile_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Name (ARN) of the user's security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-securityprofilearns
        '''
        result = self._values.get("security_profile_arns")
        assert result is not None, "Required property 'security_profile_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The user name assigned to the user account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-username
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_user_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the user account in the directory used for identity management.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-directoryuserid
        '''
        result = self._values.get("directory_user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hierarchy_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the user's hierarchy group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-hierarchygrouparn
        '''
        result = self._values.get("hierarchy_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_info(
        self,
    ) -> typing.Optional[typing.Union[CfnUser.UserIdentityInfoProperty, _IResolvable_da3f097b]]:
        '''Information about the user identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-identityinfo
        '''
        result = self._values.get("identity_info")
        return typing.cast(typing.Optional[typing.Union[CfnUser.UserIdentityInfoProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The user's password.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnContactFlow",
    "CfnContactFlowModule",
    "CfnContactFlowModuleProps",
    "CfnContactFlowProps",
    "CfnHoursOfOperation",
    "CfnHoursOfOperationProps",
    "CfnPhoneNumber",
    "CfnPhoneNumberProps",
    "CfnQuickConnect",
    "CfnQuickConnectProps",
    "CfnTaskTemplate",
    "CfnTaskTemplateProps",
    "CfnUser",
    "CfnUserHierarchyGroup",
    "CfnUserHierarchyGroupProps",
    "CfnUserProps",
]

publication.publish()
