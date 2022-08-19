'''
# AWS::SSO Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_sso as sso
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SSO construct libraries](https://constructs.dev/search?q=sso)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SSO resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSO.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSO](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSO.html).

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
class CfnAssignment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sso.CfnAssignment",
):
    '''A CloudFormation ``AWS::SSO::Assignment``.

    Assigns access to a Principal for a specified AWS account using a specified permission set.
    .. epigraph::

       The term *principal* here refers to a user or group that is defined in AWS SSO .

    :cloudformationResource: AWS::SSO::Assignment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sso as sso
        
        cfn_assignment = sso.CfnAssignment(self, "MyCfnAssignment",
            instance_arn="instanceArn",
            permission_set_arn="permissionSetArn",
            principal_id="principalId",
            principal_type="principalType",
            target_id="targetId",
            target_type="targetType"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SSO::Assignment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param permission_set_arn: The ARN of the permission set.
        :param principal_id: An identifier for an object in AWS SSO , such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in AWS SSO , see the `AWS SSO Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .
        :param principal_type: The entity type for which the assignment will be created.
        :param target_id: TargetID is an AWS account identifier, typically a 10-12 digit string (For example, 123456789012).
        :param target_type: The entity type for which the assignment will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAssignment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssignmentProps(
            instance_arn=instance_arn,
            permission_set_arn=permission_set_arn,
            principal_id=principal_id,
            principal_type=principal_type,
            target_id=target_id,
            target_type=target_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAssignment.inspect)
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
            type_hints = typing.get_type_hints(CfnAssignment._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The ARN of the SSO instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAssignment, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionSetArn")
    def permission_set_arn(self) -> builtins.str:
        '''The ARN of the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "permissionSetArn"))

    @permission_set_arn.setter
    def permission_set_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAssignment, "permission_set_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionSetArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        '''An identifier for an object in AWS SSO , such as a user or group.

        PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in AWS SSO , see the `AWS SSO Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        '''
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @principal_id.setter
    def principal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAssignment, "principal_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="principalType")
    def principal_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        '''
        return typing.cast(builtins.str, jsii.get(self, "principalType"))

    @principal_type.setter
    def principal_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAssignment, "principal_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        '''TargetID is an AWS account identifier, typically a 10-12 digit string (For example, 123456789012).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAssignment, "target_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAssignment, "target_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sso.CfnAssignmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "permission_set_arn": "permissionSetArn",
        "principal_id": "principalId",
        "principal_type": "principalType",
        "target_id": "targetId",
        "target_type": "targetType",
    },
)
class CfnAssignmentProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnAssignment``.

        :param instance_arn: The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param permission_set_arn: The ARN of the permission set.
        :param principal_id: An identifier for an object in AWS SSO , such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in AWS SSO , see the `AWS SSO Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .
        :param principal_type: The entity type for which the assignment will be created.
        :param target_id: TargetID is an AWS account identifier, typically a 10-12 digit string (For example, 123456789012).
        :param target_type: The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sso as sso
            
            cfn_assignment_props = sso.CfnAssignmentProps(
                instance_arn="instanceArn",
                permission_set_arn="permissionSetArn",
                principal_id="principalId",
                principal_type="principalType",
                target_id="targetId",
                target_type="targetType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAssignmentProps.__init__)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument permission_set_arn", value=permission_set_arn, expected_type=type_hints["permission_set_arn"])
            check_type(argname="argument principal_id", value=principal_id, expected_type=type_hints["principal_id"])
            check_type(argname="argument principal_type", value=principal_type, expected_type=type_hints["principal_type"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "permission_set_arn": permission_set_arn,
            "principal_id": principal_id,
            "principal_type": principal_type,
            "target_id": target_id,
            "target_type": target_type,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the SSO instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission_set_arn(self) -> builtins.str:
        '''The ARN of the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        '''
        result = self._values.get("permission_set_arn")
        assert result is not None, "Required property 'permission_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''An identifier for an object in AWS SSO , such as a user or group.

        PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in AWS SSO , see the `AWS SSO Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        '''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        '''
        result = self._values.get("principal_type")
        assert result is not None, "Required property 'principal_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''TargetID is an AWS account identifier, typically a 10-12 digit string (For example, 123456789012).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        '''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssignmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnInstanceAccessControlAttributeConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfiguration",
):
    '''A CloudFormation ``AWS::SSO::InstanceAccessControlAttributeConfiguration``.

    Enables the attribute-based access control (ABAC) feature for the specified AWS SSO instance. You can also specify new attributes to add to your ABAC configuration during the enabling process. For more information about ABAC, see `Attribute-Based Access Control <https://docs.aws.amazon.com//singlesignon/latest/userguide/abac.html>`_ in the *AWS SSO User Guide* .
    .. epigraph::

       The ``InstanceAccessControlAttributeConfiguration`` property has been deprecated but is still supported for backwards compatibility purposes. We recommend that you use the ``AccessControlAttributes`` property instead.

    :cloudformationResource: AWS::SSO::InstanceAccessControlAttributeConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sso as sso
        
        cfn_instance_access_control_attribute_configuration = sso.CfnInstanceAccessControlAttributeConfiguration(self, "MyCfnInstanceAccessControlAttributeConfiguration",
            instance_arn="instanceArn",
        
            # the properties below are optional
            access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                key="key",
                value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                    source=["source"]
                )
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        access_control_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SSO::InstanceAccessControlAttributeConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The ARN of the AWS SSO instance under which the operation will be executed.
        :param access_control_attributes: Lists the attributes that are configured for ABAC in the specified AWS SSO instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnInstanceAccessControlAttributeConfiguration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceAccessControlAttributeConfigurationProps(
            instance_arn=instance_arn,
            access_control_attributes=access_control_attributes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnInstanceAccessControlAttributeConfiguration.inspect)
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
            type_hints = typing.get_type_hints(CfnInstanceAccessControlAttributeConfiguration._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The ARN of the AWS SSO instance under which the operation will be executed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnInstanceAccessControlAttributeConfiguration, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessControlAttributes")
    def access_control_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", _IResolvable_da3f097b]]]]:
        '''Lists the attributes that are configured for ABAC in the specified AWS SSO instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", _IResolvable_da3f097b]]]], jsii.get(self, "accessControlAttributes"))

    @access_control_attributes.setter
    def access_control_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnInstanceAccessControlAttributeConfiguration, "access_control_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessControlAttributes", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class AccessControlAttributeProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Union[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''These are AWS SSO identity store attributes that you can configure for use in attributes-based access control (ABAC).

            You can create permissions policies that determine who can access your AWS resources based upon the configured attribute values. When you enable ABAC and specify ``AccessControlAttributes`` , AWS SSO passes the attribute values of the authenticated user into IAM for use in policy evaluation.

            :param key: The name of the attribute associated with your identities in your identity source. This is used to map a specified attribute in your identity source with an attribute in AWS SSO .
            :param value: The value used for mapping a specified attribute to an identity source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                access_control_attribute_property = sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                    key="key",
                    value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                        source=["source"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty.__init__)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the attribute associated with your identities in your identity source.

            This is used to map a specified attribute in your identity source with an attribute in AWS SSO .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty", _IResolvable_da3f097b]:
            '''The value used for mapping a specified attribute to an identity source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class AccessControlAttributeValueProperty:
        def __init__(self, *, source: typing.Sequence[builtins.str]) -> None:
            '''The value used for mapping a specified attribute to an identity source.

            :param source: The identity source to use when mapping a specified attribute to AWS SSO .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                access_control_attribute_value_property = sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                    source=["source"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty.__init__)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[str, typing.Any] = {
                "source": source,
            }

        @builtins.property
        def source(self) -> typing.List[builtins.str]:
            '''The identity source to use when mapping a specified attribute to AWS SSO .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlAttributeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "access_control_attributes": "accessControlAttributes",
    },
)
class CfnInstanceAccessControlAttributeConfigurationProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        access_control_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceAccessControlAttributeConfiguration``.

        :param instance_arn: The ARN of the AWS SSO instance under which the operation will be executed.
        :param access_control_attributes: Lists the attributes that are configured for ABAC in the specified AWS SSO instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sso as sso
            
            cfn_instance_access_control_attribute_configuration_props = sso.CfnInstanceAccessControlAttributeConfigurationProps(
                instance_arn="instanceArn",
            
                # the properties below are optional
                access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                    key="key",
                    value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                        source=["source"]
                    )
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnInstanceAccessControlAttributeConfigurationProps.__init__)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument access_control_attributes", value=access_control_attributes, expected_type=type_hints["access_control_attributes"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
        }
        if access_control_attributes is not None:
            self._values["access_control_attributes"] = access_control_attributes

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the AWS SSO instance under which the operation will be executed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, _IResolvable_da3f097b]]]]:
        '''Lists the attributes that are configured for ABAC in the specified AWS SSO instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
        '''
        result = self._values.get("access_control_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, _IResolvable_da3f097b]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceAccessControlAttributeConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPermissionSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sso.CfnPermissionSet",
):
    '''A CloudFormation ``AWS::SSO::PermissionSet``.

    Specifies a permission set within a specified SSO instance.

    :cloudformationResource: AWS::SSO::PermissionSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sso as sso
        
        # inline_policy: Any
        
        cfn_permission_set = sso.CfnPermissionSet(self, "MyCfnPermissionSet",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            customer_managed_policy_references=[sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                name="name",
        
                # the properties below are optional
                path="path"
            )],
            description="description",
            inline_policy=inline_policy,
            managed_policies=["managedPolicies"],
            permissions_boundary=sso.CfnPermissionSet.PermissionsBoundaryProperty(
                customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
        
                    # the properties below are optional
                    path="path"
                ),
                managed_policy_arn="managedPolicyArn"
            ),
            relay_state_type="relayStateType",
            session_duration="sessionDuration",
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
        customer_managed_policy_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        description: typing.Optional[builtins.str] = None,
        inline_policy: typing.Any = None,
        managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_boundary: typing.Optional[typing.Union[typing.Union["CfnPermissionSet.PermissionsBoundaryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        relay_state_type: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::SSO::PermissionSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param name: The name of the permission set.
        :param customer_managed_policy_references: ``AWS::SSO::PermissionSet.CustomerManagedPolicyReferences``.
        :param description: The description of the ``PermissionSet`` .
        :param inline_policy: The IAM inline policy that is attached to the permission set.
        :param managed_policies: A structure that stores the details of the IAM managed policy.
        :param permissions_boundary: ``AWS::SSO::PermissionSet.PermissionsBoundary``.
        :param relay_state_type: Used to redirect users within the application during the federation authentication process.
        :param session_duration: The length of time that the application user sessions are valid for in the ISO-8601 standard.
        :param tags: The tags to attach to the new ``PermissionSet`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPermissionSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionSetProps(
            instance_arn=instance_arn,
            name=name,
            customer_managed_policy_references=customer_managed_policy_references,
            description=description,
            inline_policy=inline_policy,
            managed_policies=managed_policies,
            permissions_boundary=permissions_boundary,
            relay_state_type=relay_state_type,
            session_duration=session_duration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPermissionSet.inspect)
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
            type_hints = typing.get_type_hints(CfnPermissionSet._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPermissionSetArn")
    def attr_permission_set_arn(self) -> builtins.str:
        '''The permission set ARN of the permission set, such as ``arn:aws:sso:::permissionSet/ins-instanceid/ps-permissionsetid`` .

        :cloudformationAttribute: PermissionSetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPermissionSetArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags to attach to the new ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inlinePolicy")
    def inline_policy(self) -> typing.Any:
        '''The IAM inline policy that is attached to the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        '''
        return typing.cast(typing.Any, jsii.get(self, "inlinePolicy"))

    @inline_policy.setter
    def inline_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "inline_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inlinePolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The ARN of the SSO instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customerManagedPolicyReferences")
    def customer_managed_policy_references(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::SSO::PermissionSet.CustomerManagedPolicyReferences``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-customermanagedpolicyreferences
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", _IResolvable_da3f097b]]]], jsii.get(self, "customerManagedPolicyReferences"))

    @customer_managed_policy_references.setter
    def customer_managed_policy_references(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "customer_managed_policy_references").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedPolicyReferences", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="managedPolicies")
    def managed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A structure that stores the details of the IAM managed policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managedPolicies"))

    @managed_policies.setter
    def managed_policies(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "managed_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(
        self,
    ) -> typing.Optional[typing.Union["CfnPermissionSet.PermissionsBoundaryProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSO::PermissionSet.PermissionsBoundary``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-permissionsboundary
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPermissionSet.PermissionsBoundaryProperty", _IResolvable_da3f097b]], jsii.get(self, "permissionsBoundary"))

    @permissions_boundary.setter
    def permissions_boundary(
        self,
        value: typing.Optional[typing.Union["CfnPermissionSet.PermissionsBoundaryProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "permissions_boundary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsBoundary", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relayStateType")
    def relay_state_type(self) -> typing.Optional[builtins.str]:
        '''Used to redirect users within the application during the federation authentication process.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relayStateType"))

    @relay_state_type.setter
    def relay_state_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "relay_state_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relayStateType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sessionDuration")
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''The length of time that the application user sessions are valid for in the ISO-8601 standard.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionDuration"))

    @session_duration.setter
    def session_duration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissionSet, "session_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionDuration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "path": "path"},
    )
    class CustomerManagedPolicyReferenceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnPermissionSet.CustomerManagedPolicyReferenceProperty.Name``.
            :param path: ``CfnPermissionSet.CustomerManagedPolicyReferenceProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                customer_managed_policy_reference_property = sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
                
                    # the properties below are optional
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissionSet.CustomerManagedPolicyReferenceProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnPermissionSet.CustomerManagedPolicyReferenceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html#cfn-sso-permissionset-customermanagedpolicyreference-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissionSet.CustomerManagedPolicyReferenceProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html#cfn-sso-permissionset-customermanagedpolicyreference-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedPolicyReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnPermissionSet.PermissionsBoundaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_managed_policy_reference": "customerManagedPolicyReference",
            "managed_policy_arn": "managedPolicyArn",
        },
    )
    class PermissionsBoundaryProperty:
        def __init__(
            self,
            *,
            customer_managed_policy_reference: typing.Optional[typing.Union[typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            managed_policy_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param customer_managed_policy_reference: ``CfnPermissionSet.PermissionsBoundaryProperty.CustomerManagedPolicyReference``.
            :param managed_policy_arn: ``CfnPermissionSet.PermissionsBoundaryProperty.ManagedPolicyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                permissions_boundary_property = sso.CfnPermissionSet.PermissionsBoundaryProperty(
                    customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                        name="name",
                
                        # the properties below are optional
                        path="path"
                    ),
                    managed_policy_arn="managedPolicyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissionSet.PermissionsBoundaryProperty.__init__)
                check_type(argname="argument customer_managed_policy_reference", value=customer_managed_policy_reference, expected_type=type_hints["customer_managed_policy_reference"])
                check_type(argname="argument managed_policy_arn", value=managed_policy_arn, expected_type=type_hints["managed_policy_arn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if customer_managed_policy_reference is not None:
                self._values["customer_managed_policy_reference"] = customer_managed_policy_reference
            if managed_policy_arn is not None:
                self._values["managed_policy_arn"] = managed_policy_arn

        @builtins.property
        def customer_managed_policy_reference(
            self,
        ) -> typing.Optional[typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", _IResolvable_da3f097b]]:
            '''``CfnPermissionSet.PermissionsBoundaryProperty.CustomerManagedPolicyReference``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html#cfn-sso-permissionset-permissionsboundary-customermanagedpolicyreference
            '''
            result = self._values.get("customer_managed_policy_reference")
            return typing.cast(typing.Optional[typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def managed_policy_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissionSet.PermissionsBoundaryProperty.ManagedPolicyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html#cfn-sso-permissionset-permissionsboundary-managedpolicyarn
            '''
            result = self._values.get("managed_policy_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PermissionsBoundaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sso.CfnPermissionSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "customer_managed_policy_references": "customerManagedPolicyReferences",
        "description": "description",
        "inline_policy": "inlinePolicy",
        "managed_policies": "managedPolicies",
        "permissions_boundary": "permissionsBoundary",
        "relay_state_type": "relayStateType",
        "session_duration": "sessionDuration",
        "tags": "tags",
    },
)
class CfnPermissionSetProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        customer_managed_policy_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        description: typing.Optional[builtins.str] = None,
        inline_policy: typing.Any = None,
        managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_boundary: typing.Optional[typing.Union[typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        relay_state_type: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermissionSet``.

        :param instance_arn: The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param name: The name of the permission set.
        :param customer_managed_policy_references: ``AWS::SSO::PermissionSet.CustomerManagedPolicyReferences``.
        :param description: The description of the ``PermissionSet`` .
        :param inline_policy: The IAM inline policy that is attached to the permission set.
        :param managed_policies: A structure that stores the details of the IAM managed policy.
        :param permissions_boundary: ``AWS::SSO::PermissionSet.PermissionsBoundary``.
        :param relay_state_type: Used to redirect users within the application during the federation authentication process.
        :param session_duration: The length of time that the application user sessions are valid for in the ISO-8601 standard.
        :param tags: The tags to attach to the new ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sso as sso
            
            # inline_policy: Any
            
            cfn_permission_set_props = sso.CfnPermissionSetProps(
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                customer_managed_policy_references=[sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
            
                    # the properties below are optional
                    path="path"
                )],
                description="description",
                inline_policy=inline_policy,
                managed_policies=["managedPolicies"],
                permissions_boundary=sso.CfnPermissionSet.PermissionsBoundaryProperty(
                    customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                        name="name",
            
                        # the properties below are optional
                        path="path"
                    ),
                    managed_policy_arn="managedPolicyArn"
                ),
                relay_state_type="relayStateType",
                session_duration="sessionDuration",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPermissionSetProps.__init__)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument customer_managed_policy_references", value=customer_managed_policy_references, expected_type=type_hints["customer_managed_policy_references"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument inline_policy", value=inline_policy, expected_type=type_hints["inline_policy"])
            check_type(argname="argument managed_policies", value=managed_policies, expected_type=type_hints["managed_policies"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument relay_state_type", value=relay_state_type, expected_type=type_hints["relay_state_type"])
            check_type(argname="argument session_duration", value=session_duration, expected_type=type_hints["session_duration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if customer_managed_policy_references is not None:
            self._values["customer_managed_policy_references"] = customer_managed_policy_references
        if description is not None:
            self._values["description"] = description
        if inline_policy is not None:
            self._values["inline_policy"] = inline_policy
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if relay_state_type is not None:
            self._values["relay_state_type"] = relay_state_type
        if session_duration is not None:
            self._values["session_duration"] = session_duration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the SSO instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def customer_managed_policy_references(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::SSO::PermissionSet.CustomerManagedPolicyReferences``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-customermanagedpolicyreferences
        '''
        result = self._values.get("customer_managed_policy_references")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inline_policy(self) -> typing.Any:
        '''The IAM inline policy that is attached to the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        '''
        result = self._values.get("inline_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A structure that stores the details of the IAM managed policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        '''
        result = self._values.get("managed_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions_boundary(
        self,
    ) -> typing.Optional[typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSO::PermissionSet.PermissionsBoundary``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-permissionsboundary
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def relay_state_type(self) -> typing.Optional[builtins.str]:
        '''Used to redirect users within the application during the federation authentication process.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        '''
        result = self._values.get("relay_state_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''The length of time that the application user sessions are valid for in the ISO-8601 standard.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        '''
        result = self._values.get("session_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the new ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssignment",
    "CfnAssignmentProps",
    "CfnInstanceAccessControlAttributeConfiguration",
    "CfnInstanceAccessControlAttributeConfigurationProps",
    "CfnPermissionSet",
    "CfnPermissionSetProps",
]

publication.publish()
