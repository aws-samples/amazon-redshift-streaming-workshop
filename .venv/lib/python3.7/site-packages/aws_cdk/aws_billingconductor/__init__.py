'''
# AWS::BillingConductor Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_billingconductor as billingconductor
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for BillingConductor construct libraries](https://constructs.dev/search?q=billingconductor)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::BillingConductor resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BillingConductor.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::BillingConductor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BillingConductor.html).

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
class CfnBillingGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnBillingGroup",
):
    '''A CloudFormation ``AWS::BillingConductor::BillingGroup``.

    Creates a billing group that resembles a consolidated billing family that AWS charges, based off of the predefined pricing plan computation.

    :cloudformationResource: AWS::BillingConductor::BillingGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_billingconductor as billingconductor
        
        cfn_billing_group = billingconductor.CfnBillingGroup(self, "MyCfnBillingGroup",
            account_grouping=billingconductor.CfnBillingGroup.AccountGroupingProperty(
                linked_account_ids=["linkedAccountIds"]
            ),
            computation_preference=billingconductor.CfnBillingGroup.ComputationPreferenceProperty(
                pricing_plan_arn="pricingPlanArn"
            ),
            name="name",
            primary_account_id="primaryAccountId",
        
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
        account_grouping: typing.Union[typing.Union["CfnBillingGroup.AccountGroupingProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        computation_preference: typing.Union[typing.Union["CfnBillingGroup.ComputationPreferenceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        primary_account_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::BillingConductor::BillingGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_grouping: The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated family.
        :param computation_preference: The preferences and settings that will be used to compute the AWS charges for a billing group.
        :param name: The billing group's name.
        :param primary_account_id: The account ID that serves as the main account in a billing group.
        :param description: The billing group description.
        :param tags: ``AWS::BillingConductor::BillingGroup.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnBillingGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBillingGroupProps(
            account_grouping=account_grouping,
            computation_preference=computation_preference,
            name=name,
            primary_account_id=primary_account_id,
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
            type_hints = typing.get_type_hints(CfnBillingGroup.inspect)
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
            type_hints = typing.get_type_hints(CfnBillingGroup._render_properties)
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
        '''The Amazon Resource Name (ARN) of the created billing group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> jsii.Number:
        '''The time the billing group was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> jsii.Number:
        '''The most recent time the billing group was modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSize")
    def attr_size(self) -> jsii.Number:
        '''The number of accounts in the particular billing group.

        :cloudformationAttribute: Size
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrSize"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The billing group status.

        Only one of the valid values can be used.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''The reason why the billing group is in its current status.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::BillingConductor::BillingGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accountGrouping")
    def account_grouping(
        self,
    ) -> typing.Union["CfnBillingGroup.AccountGroupingProperty", _IResolvable_da3f097b]:
        '''The set of accounts that will be under the billing group.

        The set of accounts resemble the linked accounts in a consolidated family.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-accountgrouping
        '''
        return typing.cast(typing.Union["CfnBillingGroup.AccountGroupingProperty", _IResolvable_da3f097b], jsii.get(self, "accountGrouping"))

    @account_grouping.setter
    def account_grouping(
        self,
        value: typing.Union["CfnBillingGroup.AccountGroupingProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnBillingGroup, "account_grouping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountGrouping", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="computationPreference")
    def computation_preference(
        self,
    ) -> typing.Union["CfnBillingGroup.ComputationPreferenceProperty", _IResolvable_da3f097b]:
        '''The preferences and settings that will be used to compute the AWS charges for a billing group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-computationpreference
        '''
        return typing.cast(typing.Union["CfnBillingGroup.ComputationPreferenceProperty", _IResolvable_da3f097b], jsii.get(self, "computationPreference"))

    @computation_preference.setter
    def computation_preference(
        self,
        value: typing.Union["CfnBillingGroup.ComputationPreferenceProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnBillingGroup, "computation_preference").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computationPreference", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The billing group's name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnBillingGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="primaryAccountId")
    def primary_account_id(self) -> builtins.str:
        '''The account ID that serves as the main account in a billing group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-primaryaccountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "primaryAccountId"))

    @primary_account_id.setter
    def primary_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnBillingGroup, "primary_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryAccountId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The billing group description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnBillingGroup, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnBillingGroup.AccountGroupingProperty",
        jsii_struct_bases=[],
        name_mapping={"linked_account_ids": "linkedAccountIds"},
    )
    class AccountGroupingProperty:
        def __init__(
            self,
            *,
            linked_account_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''The set of accounts that will be under the billing group.

            The set of accounts resemble the linked accounts in a consolidated family.

            :param linked_account_ids: The account IDs that make up the billing group. Account IDs must be a part of the consolidated billing family, and not associated with another billing group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                account_grouping_property = billingconductor.CfnBillingGroup.AccountGroupingProperty(
                    linked_account_ids=["linkedAccountIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnBillingGroup.AccountGroupingProperty.__init__)
                check_type(argname="argument linked_account_ids", value=linked_account_ids, expected_type=type_hints["linked_account_ids"])
            self._values: typing.Dict[str, typing.Any] = {
                "linked_account_ids": linked_account_ids,
            }

        @builtins.property
        def linked_account_ids(self) -> typing.List[builtins.str]:
            '''The account IDs that make up the billing group.

            Account IDs must be a part of the consolidated billing family, and not associated with another billing group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html#cfn-billingconductor-billinggroup-accountgrouping-linkedaccountids
            '''
            result = self._values.get("linked_account_ids")
            assert result is not None, "Required property 'linked_account_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccountGroupingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnBillingGroup.ComputationPreferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"pricing_plan_arn": "pricingPlanArn"},
    )
    class ComputationPreferenceProperty:
        def __init__(self, *, pricing_plan_arn: builtins.str) -> None:
            '''The preferences and settings that will be used to compute the AWS charges for a billing group.

            :param pricing_plan_arn: The Amazon Resource Name (ARN) of the pricing plan used to compute the AWS charges for a billing group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-computationpreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                computation_preference_property = billingconductor.CfnBillingGroup.ComputationPreferenceProperty(
                    pricing_plan_arn="pricingPlanArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnBillingGroup.ComputationPreferenceProperty.__init__)
                check_type(argname="argument pricing_plan_arn", value=pricing_plan_arn, expected_type=type_hints["pricing_plan_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "pricing_plan_arn": pricing_plan_arn,
            }

        @builtins.property
        def pricing_plan_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the pricing plan used to compute the AWS charges for a billing group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-computationpreference.html#cfn-billingconductor-billinggroup-computationpreference-pricingplanarn
            '''
            result = self._values.get("pricing_plan_arn")
            assert result is not None, "Required property 'pricing_plan_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputationPreferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnBillingGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_grouping": "accountGrouping",
        "computation_preference": "computationPreference",
        "name": "name",
        "primary_account_id": "primaryAccountId",
        "description": "description",
        "tags": "tags",
    },
)
class CfnBillingGroupProps:
    def __init__(
        self,
        *,
        account_grouping: typing.Union[typing.Union[CfnBillingGroup.AccountGroupingProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        computation_preference: typing.Union[typing.Union[CfnBillingGroup.ComputationPreferenceProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        primary_account_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBillingGroup``.

        :param account_grouping: The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated family.
        :param computation_preference: The preferences and settings that will be used to compute the AWS charges for a billing group.
        :param name: The billing group's name.
        :param primary_account_id: The account ID that serves as the main account in a billing group.
        :param description: The billing group description.
        :param tags: ``AWS::BillingConductor::BillingGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_billingconductor as billingconductor
            
            cfn_billing_group_props = billingconductor.CfnBillingGroupProps(
                account_grouping=billingconductor.CfnBillingGroup.AccountGroupingProperty(
                    linked_account_ids=["linkedAccountIds"]
                ),
                computation_preference=billingconductor.CfnBillingGroup.ComputationPreferenceProperty(
                    pricing_plan_arn="pricingPlanArn"
                ),
                name="name",
                primary_account_id="primaryAccountId",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnBillingGroupProps.__init__)
            check_type(argname="argument account_grouping", value=account_grouping, expected_type=type_hints["account_grouping"])
            check_type(argname="argument computation_preference", value=computation_preference, expected_type=type_hints["computation_preference"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument primary_account_id", value=primary_account_id, expected_type=type_hints["primary_account_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_grouping": account_grouping,
            "computation_preference": computation_preference,
            "name": name,
            "primary_account_id": primary_account_id,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_grouping(
        self,
    ) -> typing.Union[CfnBillingGroup.AccountGroupingProperty, _IResolvable_da3f097b]:
        '''The set of accounts that will be under the billing group.

        The set of accounts resemble the linked accounts in a consolidated family.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-accountgrouping
        '''
        result = self._values.get("account_grouping")
        assert result is not None, "Required property 'account_grouping' is missing"
        return typing.cast(typing.Union[CfnBillingGroup.AccountGroupingProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def computation_preference(
        self,
    ) -> typing.Union[CfnBillingGroup.ComputationPreferenceProperty, _IResolvable_da3f097b]:
        '''The preferences and settings that will be used to compute the AWS charges for a billing group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-computationpreference
        '''
        result = self._values.get("computation_preference")
        assert result is not None, "Required property 'computation_preference' is missing"
        return typing.cast(typing.Union[CfnBillingGroup.ComputationPreferenceProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The billing group's name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary_account_id(self) -> builtins.str:
        '''The account ID that serves as the main account in a billing group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-primaryaccountid
        '''
        result = self._values.get("primary_account_id")
        assert result is not None, "Required property 'primary_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The billing group description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::BillingConductor::BillingGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBillingGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCustomLineItem(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem",
):
    '''A CloudFormation ``AWS::BillingConductor::CustomLineItem``.

    Creates a custom line item that can be used to create a one-time fixed charge that can be applied to a single billing group for the current or previous billing period. The one-time fixed charge is either a fee or discount.

    :cloudformationResource: AWS::BillingConductor::CustomLineItem
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_billingconductor as billingconductor
        
        cfn_custom_line_item = billingconductor.CfnCustomLineItem(self, "MyCfnCustomLineItem",
            billing_group_arn="billingGroupArn",
            name="name",
        
            # the properties below are optional
            billing_period_range=billingconductor.CfnCustomLineItem.BillingPeriodRangeProperty(
                exclusive_end_billing_period="exclusiveEndBillingPeriod",
                inclusive_start_billing_period="inclusiveStartBillingPeriod"
            ),
            custom_line_item_charge_details=billingconductor.CfnCustomLineItem.CustomLineItemChargeDetailsProperty(
                type="type",
        
                # the properties below are optional
                flat=billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty(
                    charge_value=123
                ),
                percentage=billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty(
                    percentage_value=123,
        
                    # the properties below are optional
                    child_associated_resources=["childAssociatedResources"]
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
        billing_group_arn: builtins.str,
        name: builtins.str,
        billing_period_range: typing.Optional[typing.Union[typing.Union["CfnCustomLineItem.BillingPeriodRangeProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        custom_line_item_charge_details: typing.Optional[typing.Union[typing.Union["CfnCustomLineItem.CustomLineItemChargeDetailsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::BillingConductor::CustomLineItem``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param billing_group_arn: The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.
        :param name: The custom line item's name.
        :param billing_period_range: A time range for which the custom line item is effective.
        :param custom_line_item_charge_details: The charge details of a custom line item. It should contain only one of ``Flat`` or ``Percentage`` .
        :param description: The custom line item's description. This is shown on the Bills page in association with the charge value.
        :param tags: ``AWS::BillingConductor::CustomLineItem.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCustomLineItem.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomLineItemProps(
            billing_group_arn=billing_group_arn,
            name=name,
            billing_period_range=billing_period_range,
            custom_line_item_charge_details=custom_line_item_charge_details,
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
            type_hints = typing.get_type_hints(CfnCustomLineItem.inspect)
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
            type_hints = typing.get_type_hints(CfnCustomLineItem._render_properties)
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
        '''The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAssociationSize")
    def attr_association_size(self) -> jsii.Number:
        '''The number of resources that are associated to the custom line item.

        :cloudformationAttribute: AssociationSize
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAssociationSize"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> jsii.Number:
        '''The time created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCurrencyCode")
    def attr_currency_code(self) -> builtins.str:
        '''The custom line item's charge value currency.

        Only one of the valid values can be used.

        :cloudformationAttribute: CurrencyCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCurrencyCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> jsii.Number:
        '''The most recent time the custom line item was modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProductCode")
    def attr_product_code(self) -> builtins.str:
        '''The product code associated with the custom line item.

        :cloudformationAttribute: ProductCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProductCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::BillingConductor::CustomLineItem.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="billingGroupArn")
    def billing_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-billinggrouparn
        '''
        return typing.cast(builtins.str, jsii.get(self, "billingGroupArn"))

    @billing_group_arn.setter
    def billing_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomLineItem, "billing_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingGroupArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The custom line item's name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomLineItem, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="billingPeriodRange")
    def billing_period_range(
        self,
    ) -> typing.Optional[typing.Union["CfnCustomLineItem.BillingPeriodRangeProperty", _IResolvable_da3f097b]]:
        '''A time range for which the custom line item is effective.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-billingperiodrange
        '''
        return typing.cast(typing.Optional[typing.Union["CfnCustomLineItem.BillingPeriodRangeProperty", _IResolvable_da3f097b]], jsii.get(self, "billingPeriodRange"))

    @billing_period_range.setter
    def billing_period_range(
        self,
        value: typing.Optional[typing.Union["CfnCustomLineItem.BillingPeriodRangeProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomLineItem, "billing_period_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingPeriodRange", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customLineItemChargeDetails")
    def custom_line_item_charge_details(
        self,
    ) -> typing.Optional[typing.Union["CfnCustomLineItem.CustomLineItemChargeDetailsProperty", _IResolvable_da3f097b]]:
        '''The charge details of a custom line item.

        It should contain only one of ``Flat`` or ``Percentage`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-customlineitemchargedetails
        '''
        return typing.cast(typing.Optional[typing.Union["CfnCustomLineItem.CustomLineItemChargeDetailsProperty", _IResolvable_da3f097b]], jsii.get(self, "customLineItemChargeDetails"))

    @custom_line_item_charge_details.setter
    def custom_line_item_charge_details(
        self,
        value: typing.Optional[typing.Union["CfnCustomLineItem.CustomLineItemChargeDetailsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomLineItem, "custom_line_item_charge_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customLineItemChargeDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The custom line item's description.

        This is shown on the Bills page in association with the charge value.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomLineItem, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.BillingPeriodRangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exclusive_end_billing_period": "exclusiveEndBillingPeriod",
            "inclusive_start_billing_period": "inclusiveStartBillingPeriod",
        },
    )
    class BillingPeriodRangeProperty:
        def __init__(
            self,
            *,
            exclusive_end_billing_period: typing.Optional[builtins.str] = None,
            inclusive_start_billing_period: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The billing period range in which the custom line item request will be applied.

            :param exclusive_end_billing_period: The inclusive end billing period that defines a billing period range where a custom line is applied.
            :param inclusive_start_billing_period: The inclusive start billing period that defines a billing period range where a custom line is applied.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                billing_period_range_property = billingconductor.CfnCustomLineItem.BillingPeriodRangeProperty(
                    exclusive_end_billing_period="exclusiveEndBillingPeriod",
                    inclusive_start_billing_period="inclusiveStartBillingPeriod"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCustomLineItem.BillingPeriodRangeProperty.__init__)
                check_type(argname="argument exclusive_end_billing_period", value=exclusive_end_billing_period, expected_type=type_hints["exclusive_end_billing_period"])
                check_type(argname="argument inclusive_start_billing_period", value=inclusive_start_billing_period, expected_type=type_hints["inclusive_start_billing_period"])
            self._values: typing.Dict[str, typing.Any] = {}
            if exclusive_end_billing_period is not None:
                self._values["exclusive_end_billing_period"] = exclusive_end_billing_period
            if inclusive_start_billing_period is not None:
                self._values["inclusive_start_billing_period"] = inclusive_start_billing_period

        @builtins.property
        def exclusive_end_billing_period(self) -> typing.Optional[builtins.str]:
            '''The inclusive end billing period that defines a billing period range where a custom line is applied.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html#cfn-billingconductor-customlineitem-billingperiodrange-exclusiveendbillingperiod
            '''
            result = self._values.get("exclusive_end_billing_period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inclusive_start_billing_period(self) -> typing.Optional[builtins.str]:
            '''The inclusive start billing period that defines a billing period range where a custom line is applied.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html#cfn-billingconductor-customlineitem-billingperiodrange-inclusivestartbillingperiod
            '''
            result = self._values.get("inclusive_start_billing_period")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BillingPeriodRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.CustomLineItemChargeDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "flat": "flat", "percentage": "percentage"},
    )
    class CustomLineItemChargeDetailsProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            flat: typing.Optional[typing.Union[typing.Union["CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            percentage: typing.Optional[typing.Union[typing.Union["CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The charge details of a custom line item.

            It should contain only one of ``Flat`` or ``Percentage`` .

            :param type: The type of the custom line item that indicates whether the charge is a fee or credit.
            :param flat: A ``CustomLineItemFlatChargeDetails`` that describes the charge details of a flat custom line item.
            :param percentage: A ``CustomLineItemPercentageChargeDetails`` that describes the charge details of a percentage custom line item.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                custom_line_item_charge_details_property = billingconductor.CfnCustomLineItem.CustomLineItemChargeDetailsProperty(
                    type="type",
                
                    # the properties below are optional
                    flat=billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty(
                        charge_value=123
                    ),
                    percentage=billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty(
                        percentage_value=123,
                
                        # the properties below are optional
                        child_associated_resources=["childAssociatedResources"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCustomLineItem.CustomLineItemChargeDetailsProperty.__init__)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument flat", value=flat, expected_type=type_hints["flat"])
                check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if flat is not None:
                self._values["flat"] = flat
            if percentage is not None:
                self._values["percentage"] = percentage

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the custom line item that indicates whether the charge is a fee or credit.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def flat(
            self,
        ) -> typing.Optional[typing.Union["CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty", _IResolvable_da3f097b]]:
            '''A ``CustomLineItemFlatChargeDetails`` that describes the charge details of a flat custom line item.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-flat
            '''
            result = self._values.get("flat")
            return typing.cast(typing.Optional[typing.Union["CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def percentage(
            self,
        ) -> typing.Optional[typing.Union["CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty", _IResolvable_da3f097b]]:
            '''A ``CustomLineItemPercentageChargeDetails`` that describes the charge details of a percentage custom line item.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-percentage
            '''
            result = self._values.get("percentage")
            return typing.cast(typing.Optional[typing.Union["CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomLineItemChargeDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"charge_value": "chargeValue"},
    )
    class CustomLineItemFlatChargeDetailsProperty:
        def __init__(self, *, charge_value: jsii.Number) -> None:
            '''The charge details of a custom line item.

            It should contain only one of ``Flat`` or ``Percentage`` .

            :param charge_value: The custom line item's fixed charge value in USD.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                custom_line_item_flat_charge_details_property = billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty(
                    charge_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty.__init__)
                check_type(argname="argument charge_value", value=charge_value, expected_type=type_hints["charge_value"])
            self._values: typing.Dict[str, typing.Any] = {
                "charge_value": charge_value,
            }

        @builtins.property
        def charge_value(self) -> jsii.Number:
            '''The custom line item's fixed charge value in USD.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.html#cfn-billingconductor-customlineitem-customlineitemflatchargedetails-chargevalue
            '''
            result = self._values.get("charge_value")
            assert result is not None, "Required property 'charge_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomLineItemFlatChargeDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "percentage_value": "percentageValue",
            "child_associated_resources": "childAssociatedResources",
        },
    )
    class CustomLineItemPercentageChargeDetailsProperty:
        def __init__(
            self,
            *,
            percentage_value: jsii.Number,
            child_associated_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A representation of the charge details associated with a percentage custom line item.

            :param percentage_value: The custom line item's percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value.
            :param child_associated_resources: A list of resource ARNs to associate to the percentage custom line item.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                custom_line_item_percentage_charge_details_property = billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty(
                    percentage_value=123,
                
                    # the properties below are optional
                    child_associated_resources=["childAssociatedResources"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty.__init__)
                check_type(argname="argument percentage_value", value=percentage_value, expected_type=type_hints["percentage_value"])
                check_type(argname="argument child_associated_resources", value=child_associated_resources, expected_type=type_hints["child_associated_resources"])
            self._values: typing.Dict[str, typing.Any] = {
                "percentage_value": percentage_value,
            }
            if child_associated_resources is not None:
                self._values["child_associated_resources"] = child_associated_resources

        @builtins.property
        def percentage_value(self) -> jsii.Number:
            '''The custom line item's percentage value.

            This will be multiplied against the combined value of its associated resources to determine its charge value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html#cfn-billingconductor-customlineitem-customlineitempercentagechargedetails-percentagevalue
            '''
            result = self._values.get("percentage_value")
            assert result is not None, "Required property 'percentage_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def child_associated_resources(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of resource ARNs to associate to the percentage custom line item.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html#cfn-billingconductor-customlineitem-customlineitempercentagechargedetails-childassociatedresources
            '''
            result = self._values.get("child_associated_resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomLineItemPercentageChargeDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItemProps",
    jsii_struct_bases=[],
    name_mapping={
        "billing_group_arn": "billingGroupArn",
        "name": "name",
        "billing_period_range": "billingPeriodRange",
        "custom_line_item_charge_details": "customLineItemChargeDetails",
        "description": "description",
        "tags": "tags",
    },
)
class CfnCustomLineItemProps:
    def __init__(
        self,
        *,
        billing_group_arn: builtins.str,
        name: builtins.str,
        billing_period_range: typing.Optional[typing.Union[typing.Union[CfnCustomLineItem.BillingPeriodRangeProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        custom_line_item_charge_details: typing.Optional[typing.Union[typing.Union[CfnCustomLineItem.CustomLineItemChargeDetailsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomLineItem``.

        :param billing_group_arn: The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.
        :param name: The custom line item's name.
        :param billing_period_range: A time range for which the custom line item is effective.
        :param custom_line_item_charge_details: The charge details of a custom line item. It should contain only one of ``Flat`` or ``Percentage`` .
        :param description: The custom line item's description. This is shown on the Bills page in association with the charge value.
        :param tags: ``AWS::BillingConductor::CustomLineItem.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_billingconductor as billingconductor
            
            cfn_custom_line_item_props = billingconductor.CfnCustomLineItemProps(
                billing_group_arn="billingGroupArn",
                name="name",
            
                # the properties below are optional
                billing_period_range=billingconductor.CfnCustomLineItem.BillingPeriodRangeProperty(
                    exclusive_end_billing_period="exclusiveEndBillingPeriod",
                    inclusive_start_billing_period="inclusiveStartBillingPeriod"
                ),
                custom_line_item_charge_details=billingconductor.CfnCustomLineItem.CustomLineItemChargeDetailsProperty(
                    type="type",
            
                    # the properties below are optional
                    flat=billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty(
                        charge_value=123
                    ),
                    percentage=billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty(
                        percentage_value=123,
            
                        # the properties below are optional
                        child_associated_resources=["childAssociatedResources"]
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
            type_hints = typing.get_type_hints(CfnCustomLineItemProps.__init__)
            check_type(argname="argument billing_group_arn", value=billing_group_arn, expected_type=type_hints["billing_group_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument billing_period_range", value=billing_period_range, expected_type=type_hints["billing_period_range"])
            check_type(argname="argument custom_line_item_charge_details", value=custom_line_item_charge_details, expected_type=type_hints["custom_line_item_charge_details"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "billing_group_arn": billing_group_arn,
            "name": name,
        }
        if billing_period_range is not None:
            self._values["billing_period_range"] = billing_period_range
        if custom_line_item_charge_details is not None:
            self._values["custom_line_item_charge_details"] = custom_line_item_charge_details
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def billing_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-billinggrouparn
        '''
        result = self._values.get("billing_group_arn")
        assert result is not None, "Required property 'billing_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The custom line item's name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def billing_period_range(
        self,
    ) -> typing.Optional[typing.Union[CfnCustomLineItem.BillingPeriodRangeProperty, _IResolvable_da3f097b]]:
        '''A time range for which the custom line item is effective.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-billingperiodrange
        '''
        result = self._values.get("billing_period_range")
        return typing.cast(typing.Optional[typing.Union[CfnCustomLineItem.BillingPeriodRangeProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def custom_line_item_charge_details(
        self,
    ) -> typing.Optional[typing.Union[CfnCustomLineItem.CustomLineItemChargeDetailsProperty, _IResolvable_da3f097b]]:
        '''The charge details of a custom line item.

        It should contain only one of ``Flat`` or ``Percentage`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-customlineitemchargedetails
        '''
        result = self._values.get("custom_line_item_charge_details")
        return typing.cast(typing.Optional[typing.Union[CfnCustomLineItem.CustomLineItemChargeDetailsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The custom line item's description.

        This is shown on the Bills page in association with the charge value.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::BillingConductor::CustomLineItem.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomLineItemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPricingPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingPlan",
):
    '''A CloudFormation ``AWS::BillingConductor::PricingPlan``.

    Creates a pricing plan that is used for computing AWS charges for billing groups.

    :cloudformationResource: AWS::BillingConductor::PricingPlan
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_billingconductor as billingconductor
        
        cfn_pricing_plan = billingconductor.CfnPricingPlan(self, "MyCfnPricingPlan",
            name="name",
        
            # the properties below are optional
            description="description",
            pricing_rule_arns=["pricingRuleArns"],
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
        pricing_rule_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::BillingConductor::PricingPlan``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of a pricing plan.
        :param description: The pricing plan description.
        :param pricing_rule_arns: The ``PricingRuleArns`` that are associated with the Pricing Plan.
        :param tags: ``AWS::BillingConductor::PricingPlan.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPricingPlan.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPricingPlanProps(
            name=name,
            description=description,
            pricing_rule_arns=pricing_rule_arns,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPricingPlan.inspect)
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
            type_hints = typing.get_type_hints(CfnPricingPlan._render_properties)
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
        '''The Amazon Resource Name (ARN) of the created pricing plan.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> jsii.Number:
        '''The time the pricing plan was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> jsii.Number:
        '''The most recent time the pricing plan was modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSize")
    def attr_size(self) -> jsii.Number:
        '''The pricing rules count currently associated with this pricing plan list element.

        :cloudformationAttribute: Size
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrSize"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::BillingConductor::PricingPlan.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of a pricing plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingPlan, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The pricing plan description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingPlan, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pricingRuleArns")
    def pricing_rule_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ``PricingRuleArns`` that are associated with the Pricing Plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-pricingrulearns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pricingRuleArns"))

    @pricing_rule_arns.setter
    def pricing_rule_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingPlan, "pricing_rule_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingRuleArns", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "pricing_rule_arns": "pricingRuleArns",
        "tags": "tags",
    },
)
class CfnPricingPlanProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pricing_rule_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPricingPlan``.

        :param name: The name of a pricing plan.
        :param description: The pricing plan description.
        :param pricing_rule_arns: The ``PricingRuleArns`` that are associated with the Pricing Plan.
        :param tags: ``AWS::BillingConductor::PricingPlan.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_billingconductor as billingconductor
            
            cfn_pricing_plan_props = billingconductor.CfnPricingPlanProps(
                name="name",
            
                # the properties below are optional
                description="description",
                pricing_rule_arns=["pricingRuleArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPricingPlanProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument pricing_rule_arns", value=pricing_rule_arns, expected_type=type_hints["pricing_rule_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if pricing_rule_arns is not None:
            self._values["pricing_rule_arns"] = pricing_rule_arns
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a pricing plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The pricing plan description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_rule_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ``PricingRuleArns`` that are associated with the Pricing Plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-pricingrulearns
        '''
        result = self._values.get("pricing_rule_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::BillingConductor::PricingPlan.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPricingPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPricingRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingRule",
):
    '''A CloudFormation ``AWS::BillingConductor::PricingRule``.

    Creates a pricing rule can be associated to a pricing plan, or a set of pricing plans.

    :cloudformationResource: AWS::BillingConductor::PricingRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_billingconductor as billingconductor
        
        cfn_pricing_rule = billingconductor.CfnPricingRule(self, "MyCfnPricingRule",
            modifier_percentage=123,
            name="name",
            scope="scope",
            type="type",
        
            # the properties below are optional
            description="description",
            service="service",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope_: constructs.Construct,
        id: builtins.str,
        *,
        modifier_percentage: jsii.Number,
        name: builtins.str,
        scope: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::BillingConductor::PricingRule``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param modifier_percentage: A percentage modifier applied on the public pricing rates.
        :param name: The name of a pricing rule.
        :param scope: The scope of pricing rule that indicates if it is globally applicable, or if it is service-specific.
        :param type: The type of pricing rule.
        :param description: The pricing rule description.
        :param service: If the ``Scope`` attribute is ``SERVICE`` , this attribute indicates which service the ``PricingRule`` is applicable for.
        :param tags: ``AWS::BillingConductor::PricingRule.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPricingRule.__init__)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPricingRuleProps(
            modifier_percentage=modifier_percentage,
            name=name,
            scope=scope,
            type=type,
            description=description,
            service=service,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPricingRule.inspect)
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
            type_hints = typing.get_type_hints(CfnPricingRule._render_properties)
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
        '''The Amazon Resource Name (ARN) used to uniquely identify a pricing rule.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAssociatedPricingPlanCount")
    def attr_associated_pricing_plan_count(self) -> jsii.Number:
        '''The pricing plans count that this pricing rule is associated with.

        :cloudformationAttribute: AssociatedPricingPlanCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAssociatedPricingPlanCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> jsii.Number:
        '''The time the pricing rule was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> jsii.Number:
        '''The most recent time the pricing rule was modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::BillingConductor::PricingRule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modifierPercentage")
    def modifier_percentage(self) -> jsii.Number:
        '''A percentage modifier applied on the public pricing rates.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-modifierpercentage
        '''
        return typing.cast(jsii.Number, jsii.get(self, "modifierPercentage"))

    @modifier_percentage.setter
    def modifier_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingRule, "modifier_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modifierPercentage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of a pricing rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        '''The scope of pricing rule that indicates if it is globally applicable, or if it is service-specific.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-scope
        '''
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingRule, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of pricing rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingRule, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The pricing rule description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    def service(self) -> typing.Optional[builtins.str]:
        '''If the ``Scope`` attribute is ``SERVICE`` , this attribute indicates which service the ``PricingRule`` is applicable for.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-service
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "service"))

    @service.setter
    def service(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPricingRule, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "modifier_percentage": "modifierPercentage",
        "name": "name",
        "scope": "scope",
        "type": "type",
        "description": "description",
        "service": "service",
        "tags": "tags",
    },
)
class CfnPricingRuleProps:
    def __init__(
        self,
        *,
        modifier_percentage: jsii.Number,
        name: builtins.str,
        scope: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPricingRule``.

        :param modifier_percentage: A percentage modifier applied on the public pricing rates.
        :param name: The name of a pricing rule.
        :param scope: The scope of pricing rule that indicates if it is globally applicable, or if it is service-specific.
        :param type: The type of pricing rule.
        :param description: The pricing rule description.
        :param service: If the ``Scope`` attribute is ``SERVICE`` , this attribute indicates which service the ``PricingRule`` is applicable for.
        :param tags: ``AWS::BillingConductor::PricingRule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_billingconductor as billingconductor
            
            cfn_pricing_rule_props = billingconductor.CfnPricingRuleProps(
                modifier_percentage=123,
                name="name",
                scope="scope",
                type="type",
            
                # the properties below are optional
                description="description",
                service="service",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPricingRuleProps.__init__)
            check_type(argname="argument modifier_percentage", value=modifier_percentage, expected_type=type_hints["modifier_percentage"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "modifier_percentage": modifier_percentage,
            "name": name,
            "scope": scope,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if service is not None:
            self._values["service"] = service
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def modifier_percentage(self) -> jsii.Number:
        '''A percentage modifier applied on the public pricing rates.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-modifierpercentage
        '''
        result = self._values.get("modifier_percentage")
        assert result is not None, "Required property 'modifier_percentage' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a pricing rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''The scope of pricing rule that indicates if it is globally applicable, or if it is service-specific.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of pricing rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The pricing rule description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''If the ``Scope`` attribute is ``SERVICE`` , this attribute indicates which service the ``PricingRule`` is applicable for.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::BillingConductor::PricingRule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPricingRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBillingGroup",
    "CfnBillingGroupProps",
    "CfnCustomLineItem",
    "CfnCustomLineItemProps",
    "CfnPricingPlan",
    "CfnPricingPlanProps",
    "CfnPricingRule",
    "CfnPricingRuleProps",
]

publication.publish()
