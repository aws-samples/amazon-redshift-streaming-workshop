'''
# AWS::Macie Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_macie as macie
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Macie construct libraries](https://constructs.dev/search?q=macie)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Macie resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Macie.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Macie](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Macie.html).

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
class CfnAllowList(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_macie.CfnAllowList",
):
    '''A CloudFormation ``AWS::Macie::AllowList``.

    :cloudformationResource: AWS::Macie::AllowList
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_macie as macie
        
        cfn_allow_list = macie.CfnAllowList(self, "MyCfnAllowList",
            criteria=macie.CfnAllowList.CriteriaProperty(
                regex="regex",
                s3_words_list=macie.CfnAllowList.S3WordsListProperty(
                    bucket_name="bucketName",
                    object_key="objectKey"
                )
            ),
            name="name",
        
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
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        criteria: typing.Union[typing.Union["CfnAllowList.CriteriaProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Macie::AllowList``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param criteria: ``AWS::Macie::AllowList.Criteria``.
        :param name: ``AWS::Macie::AllowList.Name``.
        :param description: ``AWS::Macie::AllowList.Description``.
        :param tags: ``AWS::Macie::AllowList.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef55cb8aaca32dcf264ac0e8768dc1c5a0b1471c41c8de3c9575f20000ca4bd9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAllowListProps(
            criteria=criteria, name=name, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de89a42feae1bdccf1b7fb468bda2c5700b1aa71c5c523cb2c69a8c666ae8e2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7369f7a4bca5c49d764dbf34faf902a40c52828d8fba955e4eca05e9adcaff7a)
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::Macie::AllowList.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="criteria")
    def criteria(
        self,
    ) -> typing.Union["CfnAllowList.CriteriaProperty", _IResolvable_da3f097b]:
        '''``AWS::Macie::AllowList.Criteria``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-criteria
        '''
        return typing.cast(typing.Union["CfnAllowList.CriteriaProperty", _IResolvable_da3f097b], jsii.get(self, "criteria"))

    @criteria.setter
    def criteria(
        self,
        value: typing.Union["CfnAllowList.CriteriaProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e4ae58b4636b7db31b0fa3adc3410ae3d14049fa02c2bd307123f1749460647)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "criteria", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Macie::AllowList.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d690571d1b7ea81f4eaac91920c04dab927cd0ddc18b3539a84afdcb50cfdc4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::AllowList.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eff0733233420991a19ec573286f220cf810fc8bd281a542a9fa2c82daf4c241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnAllowList.CriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"regex": "regex", "s3_words_list": "s3WordsList"},
    )
    class CriteriaProperty:
        def __init__(
            self,
            *,
            regex: typing.Optional[builtins.str] = None,
            s3_words_list: typing.Optional[typing.Union[typing.Union["CfnAllowList.S3WordsListProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param regex: ``CfnAllowList.CriteriaProperty.Regex``.
            :param s3_words_list: ``CfnAllowList.CriteriaProperty.S3WordsList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                criteria_property = macie.CfnAllowList.CriteriaProperty(
                    regex="regex",
                    s3_words_list=macie.CfnAllowList.S3WordsListProperty(
                        bucket_name="bucketName",
                        object_key="objectKey"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__916c849be567db5e8b2d28b4262b1b5e6cc4efa0cc6749b882394480f94b0f1a)
                check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
                check_type(argname="argument s3_words_list", value=s3_words_list, expected_type=type_hints["s3_words_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if regex is not None:
                self._values["regex"] = regex
            if s3_words_list is not None:
                self._values["s3_words_list"] = s3_words_list

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''``CfnAllowList.CriteriaProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html#cfn-macie-allowlist-criteria-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_words_list(
            self,
        ) -> typing.Optional[typing.Union["CfnAllowList.S3WordsListProperty", _IResolvable_da3f097b]]:
            '''``CfnAllowList.CriteriaProperty.S3WordsList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html#cfn-macie-allowlist-criteria-s3wordslist
            '''
            result = self._values.get("s3_words_list")
            return typing.cast(typing.Optional[typing.Union["CfnAllowList.S3WordsListProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnAllowList.S3WordsListProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "object_key": "objectKey"},
    )
    class S3WordsListProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            object_key: builtins.str,
        ) -> None:
            '''
            :param bucket_name: ``CfnAllowList.S3WordsListProperty.BucketName``.
            :param object_key: ``CfnAllowList.S3WordsListProperty.ObjectKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                s3_words_list_property = macie.CfnAllowList.S3WordsListProperty(
                    bucket_name="bucketName",
                    object_key="objectKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6728338d9836f378990a221bfcb5d4ebc176286721060379316cb044250d5933)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "object_key": object_key,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''``CfnAllowList.S3WordsListProperty.BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html#cfn-macie-allowlist-s3wordslist-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_key(self) -> builtins.str:
            '''``CfnAllowList.S3WordsListProperty.ObjectKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html#cfn-macie-allowlist-s3wordslist-objectkey
            '''
            result = self._values.get("object_key")
            assert result is not None, "Required property 'object_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3WordsListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_macie.CfnAllowListProps",
    jsii_struct_bases=[],
    name_mapping={
        "criteria": "criteria",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnAllowListProps:
    def __init__(
        self,
        *,
        criteria: typing.Union[typing.Union[CfnAllowList.CriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAllowList``.

        :param criteria: ``AWS::Macie::AllowList.Criteria``.
        :param name: ``AWS::Macie::AllowList.Name``.
        :param description: ``AWS::Macie::AllowList.Description``.
        :param tags: ``AWS::Macie::AllowList.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_macie as macie
            
            cfn_allow_list_props = macie.CfnAllowListProps(
                criteria=macie.CfnAllowList.CriteriaProperty(
                    regex="regex",
                    s3_words_list=macie.CfnAllowList.S3WordsListProperty(
                        bucket_name="bucketName",
                        object_key="objectKey"
                    )
                ),
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cde4980d3f47e6973fbc0136f9a40cf0f5706f781fb45f3cc0aad4b99e96d39)
            check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "criteria": criteria,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def criteria(
        self,
    ) -> typing.Union[CfnAllowList.CriteriaProperty, _IResolvable_da3f097b]:
        '''``AWS::Macie::AllowList.Criteria``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-criteria
        '''
        result = self._values.get("criteria")
        assert result is not None, "Required property 'criteria' is missing"
        return typing.cast(typing.Union[CfnAllowList.CriteriaProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Macie::AllowList.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::AllowList.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::Macie::AllowList.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAllowListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCustomDataIdentifier(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_macie.CfnCustomDataIdentifier",
):
    '''A CloudFormation ``AWS::Macie::CustomDataIdentifier``.

    The ``AWS::Macie::CustomDataIdentifier`` resource is a set of criteria that you define to detect sensitive data in one or more data sources. Each identifier specifies a regular expression ( *regex* ) that defines a text pattern to match in the data. It can also specify character sequences, such as words and phrases, and a proximity rule that refine the analysis of a data source. By using custom data identifiers, you can tailor your analysis to meet your organization's specific needs and supplement the built-in, managed data identifiers that Amazon Macie provides.

    A ``Session`` must exist for the account before you can create a ``CustomDataIdentifier`` . Use a `DependsOn attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ to ensure that the ``Session`` is created before the other resources. For example, ``"DependsOn: Session"`` .

    :cloudformationResource: AWS::Macie::CustomDataIdentifier
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_macie as macie
        
        cfn_custom_data_identifier = macie.CfnCustomDataIdentifier(self, "MyCfnCustomDataIdentifier",
            name="name",
            regex="regex",
        
            # the properties below are optional
            description="description",
            ignore_words=["ignoreWords"],
            keywords=["keywords"],
            maximum_match_distance=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        regex: builtins.str,
        description: typing.Optional[builtins.str] = None,
        ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
        keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_match_distance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::Macie::CustomDataIdentifier``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: A custom name for the custom data identifier. The name can contain as many as 128 characters. We strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to see the identifier's name, depending on the actions that they're allowed to perform in Amazon Macie .
        :param regex: The regular expression ( *regex* ) that defines the pattern to match. The expression can contain as many as 512 characters.
        :param description: The description of the custom data identifier. The description can contain as many as 512 characters.
        :param ignore_words: An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 characters. Ignore words are case sensitive.
        :param keywords: An array that lists specific character sequences (keywords), one of which must be within proximity ( ``MaximumMatchDistance`` ) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 characters. Keywords aren't case sensitive.
        :param maximum_match_distance: The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the ``Keywords`` array. Amazon Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1-300 characters. The default value is 50.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8462f70ed2396867e691499b8338ee06166375569e4774b35cad18418587284c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomDataIdentifierProps(
            name=name,
            regex=regex,
            description=description,
            ignore_words=ignore_words,
            keywords=keywords,
            maximum_match_distance=maximum_match_distance,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75e9300d86a3080fc43c5b9e06f708ec6e0be23ca1a8b8c548c28f04d4a38b47)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c2273c82378b08a1921a6584b6eafca3f9442f8236c8797614cdc38e93f50a4)
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
        '''The Amazon Resource Name (ARN) of the custom data identifier.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier for the custom data identifier.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A custom name for the custom data identifier. The name can contain as many as 128 characters.

        We strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to see the identifier's name, depending on the actions that they're allowed to perform in Amazon Macie .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56bafc0e98388f95c36a25cdb08ac16d1b32e9b68fc70fc559070e909e26043f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        '''The regular expression ( *regex* ) that defines the pattern to match.

        The expression can contain as many as 512 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex
        '''
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1a88698a8e31c22c8a96936b106ec14252c0df95a0c621ffc59448549cfe4f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the custom data identifier.

        The description can contain as many as 512 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4eac22a0be7a58617fc706b4a6f4df1d7c10d4fd1bcb1bc7c87ecb091280ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreWords")
    def ignore_words(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array that lists specific character sequences (ignore words) to exclude from the results.

        If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 characters. Ignore words are case sensitive.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreWords"))

    @ignore_words.setter
    def ignore_words(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35dff10296c96b79146377714bebc3cb572a5fc32fda7088add5e2e9c20cfb52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreWords", value)

    @builtins.property
    @jsii.member(jsii_name="keywords")
    def keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array that lists specific character sequences (keywords), one of which must be within proximity ( ``MaximumMatchDistance`` ) of the regular expression to match.

        The array can contain as many as 50 keywords. Each keyword can contain 3-90 characters. Keywords aren't case sensitive.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keywords"))

    @keywords.setter
    def keywords(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1910816738c1d222482ca791d3639f1eb091753a7bef0627a18c8298817c4083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keywords", value)

    @builtins.property
    @jsii.member(jsii_name="maximumMatchDistance")
    def maximum_match_distance(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the ``Keywords`` array.

        Amazon Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1-300 characters. The default value is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumMatchDistance"))

    @maximum_match_distance.setter
    def maximum_match_distance(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baadf50a05df72179523cc44ce07f1d05939df835131681e825e51b9a74778eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumMatchDistance", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_macie.CfnCustomDataIdentifierProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "regex": "regex",
        "description": "description",
        "ignore_words": "ignoreWords",
        "keywords": "keywords",
        "maximum_match_distance": "maximumMatchDistance",
    },
)
class CfnCustomDataIdentifierProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        regex: builtins.str,
        description: typing.Optional[builtins.str] = None,
        ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
        keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_match_distance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomDataIdentifier``.

        :param name: A custom name for the custom data identifier. The name can contain as many as 128 characters. We strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to see the identifier's name, depending on the actions that they're allowed to perform in Amazon Macie .
        :param regex: The regular expression ( *regex* ) that defines the pattern to match. The expression can contain as many as 512 characters.
        :param description: The description of the custom data identifier. The description can contain as many as 512 characters.
        :param ignore_words: An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 characters. Ignore words are case sensitive.
        :param keywords: An array that lists specific character sequences (keywords), one of which must be within proximity ( ``MaximumMatchDistance`` ) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 characters. Keywords aren't case sensitive.
        :param maximum_match_distance: The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the ``Keywords`` array. Amazon Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1-300 characters. The default value is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_macie as macie
            
            cfn_custom_data_identifier_props = macie.CfnCustomDataIdentifierProps(
                name="name",
                regex="regex",
            
                # the properties below are optional
                description="description",
                ignore_words=["ignoreWords"],
                keywords=["keywords"],
                maximum_match_distance=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b153bc4a75175074214978bb8d0954e3d477b6896260fae9394ce3a3f3ef2463)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument ignore_words", value=ignore_words, expected_type=type_hints["ignore_words"])
            check_type(argname="argument keywords", value=keywords, expected_type=type_hints["keywords"])
            check_type(argname="argument maximum_match_distance", value=maximum_match_distance, expected_type=type_hints["maximum_match_distance"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "regex": regex,
        }
        if description is not None:
            self._values["description"] = description
        if ignore_words is not None:
            self._values["ignore_words"] = ignore_words
        if keywords is not None:
            self._values["keywords"] = keywords
        if maximum_match_distance is not None:
            self._values["maximum_match_distance"] = maximum_match_distance

    @builtins.property
    def name(self) -> builtins.str:
        '''A custom name for the custom data identifier. The name can contain as many as 128 characters.

        We strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to see the identifier's name, depending on the actions that they're allowed to perform in Amazon Macie .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regex(self) -> builtins.str:
        '''The regular expression ( *regex* ) that defines the pattern to match.

        The expression can contain as many as 512 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex
        '''
        result = self._values.get("regex")
        assert result is not None, "Required property 'regex' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the custom data identifier.

        The description can contain as many as 512 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_words(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array that lists specific character sequences (ignore words) to exclude from the results.

        If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 characters. Ignore words are case sensitive.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords
        '''
        result = self._values.get("ignore_words")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array that lists specific character sequences (keywords), one of which must be within proximity ( ``MaximumMatchDistance`` ) of the regular expression to match.

        The array can contain as many as 50 keywords. Each keyword can contain 3-90 characters. Keywords aren't case sensitive.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords
        '''
        result = self._values.get("keywords")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def maximum_match_distance(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the ``Keywords`` array.

        Amazon Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1-300 characters. The default value is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance
        '''
        result = self._values.get("maximum_match_distance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomDataIdentifierProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFindingsFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilter",
):
    '''A CloudFormation ``AWS::Macie::FindingsFilter``.

    The ``AWS::Macie::FindingsFilter`` resource represents an individual findings filter that you create and save to view, analyze, and manage findings. A *findings filter* is a set of criteria that specifies which findings to include in the results of a query for findings. A findings filter can also perform specific actions on findings that meet the filter's criteria.

    A ``Session`` must exist for the account before you can create a ``FindingsFilter`` . Use a `DependsOn attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ to ensure that the ``Session`` is created before the other resources. For example, ``"DependsOn: Session"`` .

    :cloudformationResource: AWS::Macie::FindingsFilter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_macie as macie
        
        cfn_findings_filter = macie.CfnFindingsFilter(self, "MyCfnFindingsFilter",
            finding_criteria=macie.CfnFindingsFilter.FindingCriteriaProperty(
                criterion={
                    "criterion_key": macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty(
                        eq=["eq"],
                        gt=123,
                        gte=123,
                        lt=123,
                        lte=123,
                        neq=["neq"]
                    )
                }
            ),
            name="name",
        
            # the properties below are optional
            action="action",
            description="description",
            position=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        finding_criteria: typing.Union[typing.Union["CfnFindingsFilter.FindingCriteriaProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::Macie::FindingsFilter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param finding_criteria: The criteria to use to filter findings.
        :param name: A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters. We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users might be able to see the filter's name, depending on the actions that they're allowed to perform in Amazon Macie .
        :param action: The action to perform on findings that meet the filter criteria ( ``FindingCriteria`` ). Valid values are:. - ARCHIVE - Suppress (automatically archive) the findings. - NOOP - Don't perform any action on the findings.
        :param description: A custom description of the filter. The description can contain as many as 512 characters. We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users might be able to see the filter's description, depending on the actions that they're allowed to perform in Amazon Macie .
        :param position: The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11b08ade332eec06142e65a0667c3f977a9418dbb1685fc4d53acba74840039e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFindingsFilterProps(
            finding_criteria=finding_criteria,
            name=name,
            action=action,
            description=description,
            position=position,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a93c27322ef7d4277d7a472e492eca4e1a6e853c53d3268dc2ece902bef2ea0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70f86624cef1fb49b3b96cefbc1b1ef17881bea27e106666e69078116a2c0ce5)
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
        '''The Amazon Resource Name (ARN) of the filter.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFindingsFilterListItems")
    def attr_findings_filter_list_items(self) -> _IResolvable_da3f097b:
        '''An array of ``FindingsFilterListItem`` objects, one for each findings filter that's associated with the account.

        :cloudformationAttribute: FindingsFilterListItems
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrFindingsFilterListItems"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier for the filter.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(
        self,
    ) -> typing.Union["CfnFindingsFilter.FindingCriteriaProperty", _IResolvable_da3f097b]:
        '''The criteria to use to filter findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria
        '''
        return typing.cast(typing.Union["CfnFindingsFilter.FindingCriteriaProperty", _IResolvable_da3f097b], jsii.get(self, "findingCriteria"))

    @finding_criteria.setter
    def finding_criteria(
        self,
        value: typing.Union["CfnFindingsFilter.FindingCriteriaProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca4bea48d84a530685d7cefc7aab036a382728b48d306044f2a518d375e31af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A custom name for the filter.

        The name must contain at least 3 characters and can contain as many as 64 characters.

        We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users might be able to see the filter's name, depending on the actions that they're allowed to perform in Amazon Macie .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d67d6558f4b26d340cf216d4866559bbaf532c9defe9a11eb199af1a7d2433c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> typing.Optional[builtins.str]:
        '''The action to perform on findings that meet the filter criteria ( ``FindingCriteria`` ). Valid values are:.

        - ARCHIVE - Suppress (automatically archive) the findings.
        - NOOP - Don't perform any action on the findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "action"))

    @action.setter
    def action(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41dfbe847eece32f936f8bf3bb5d835d163ba85d1ce1a626fe00a0cb995afaa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the filter. The description can contain as many as 512 characters.

        We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users might be able to see the filter's description, depending on the actions that they're allowed to perform in Amazon Macie .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03fc2464c8c604a167f22170fbed859036b5124a2e5d8b3f089b061f6bf605cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> typing.Optional[jsii.Number]:
        '''The position of the filter in the list of saved filters on the Amazon Macie console.

        This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "position"))

    @position.setter
    def position(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c60836229071347a8b3064cb2b271455290f497cd552169c6180768b3a67ea2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "position", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "eq": "eq",
            "gt": "gt",
            "gte": "gte",
            "lt": "lt",
            "lte": "lte",
            "neq": "neq",
        },
    )
    class CriterionAdditionalPropertiesProperty:
        def __init__(
            self,
            *,
            eq: typing.Optional[typing.Sequence[builtins.str]] = None,
            gt: typing.Optional[jsii.Number] = None,
            gte: typing.Optional[jsii.Number] = None,
            lt: typing.Optional[jsii.Number] = None,
            lte: typing.Optional[jsii.Number] = None,
            neq: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param eq: ``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.eq``.
            :param gt: ``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.gt``.
            :param gte: ``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.gte``.
            :param lt: ``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.lt``.
            :param lte: ``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.lte``.
            :param neq: ``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.neq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                criterion_additional_properties_property = macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty(
                    eq=["eq"],
                    gt=123,
                    gte=123,
                    lt=123,
                    lte=123,
                    neq=["neq"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3cc0e94f951064d75bcef2cb73a1a20831df93d286eb235e35e3f7f153419f00)
                check_type(argname="argument eq", value=eq, expected_type=type_hints["eq"])
                check_type(argname="argument gt", value=gt, expected_type=type_hints["gt"])
                check_type(argname="argument gte", value=gte, expected_type=type_hints["gte"])
                check_type(argname="argument lt", value=lt, expected_type=type_hints["lt"])
                check_type(argname="argument lte", value=lte, expected_type=type_hints["lte"])
                check_type(argname="argument neq", value=neq, expected_type=type_hints["neq"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if eq is not None:
                self._values["eq"] = eq
            if gt is not None:
                self._values["gt"] = gt
            if gte is not None:
                self._values["gte"] = gte
            if lt is not None:
                self._values["lt"] = lt
            if lte is not None:
                self._values["lte"] = lte
            if neq is not None:
                self._values["neq"] = neq

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.eq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def gt(self) -> typing.Optional[jsii.Number]:
            '''``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.gt``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-gt
            '''
            result = self._values.get("gt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gte(self) -> typing.Optional[jsii.Number]:
            '''``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.gte``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-gte
            '''
            result = self._values.get("gte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lt(self) -> typing.Optional[jsii.Number]:
            '''``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.lt``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-lt
            '''
            result = self._values.get("lt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lte(self) -> typing.Optional[jsii.Number]:
            '''``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.lte``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-lte
            '''
            result = self._values.get("lte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnFindingsFilter.CriterionAdditionalPropertiesProperty.neq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-neq
            '''
            result = self._values.get("neq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CriterionAdditionalPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilter.FindingCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"criterion": "criterion"},
    )
    class FindingCriteriaProperty:
        def __init__(
            self,
            *,
            criterion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnFindingsFilter.CriterionAdditionalPropertiesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Specifies, as a map, one or more property-based conditions that filter the results of a query for findings.

            :param criterion: Specifies a condition that defines the property, operator, and value to use to filter the results.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                finding_criteria_property = macie.CfnFindingsFilter.FindingCriteriaProperty(
                    criterion={
                        "criterion_key": macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty(
                            eq=["eq"],
                            gt=123,
                            gte=123,
                            lt=123,
                            lte=123,
                            neq=["neq"]
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bfa11a0d6136e31dcc0f57ce160cc975d2fd8978372183978096da64d7bb37e8)
                check_type(argname="argument criterion", value=criterion, expected_type=type_hints["criterion"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if criterion is not None:
                self._values["criterion"] = criterion

        @builtins.property
        def criterion(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnFindingsFilter.CriterionAdditionalPropertiesProperty", _IResolvable_da3f097b]]]]:
            '''Specifies a condition that defines the property, operator, and value to use to filter the results.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html#cfn-macie-findingsfilter-findingcriteria-criterion
            '''
            result = self._values.get("criterion")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnFindingsFilter.CriterionAdditionalPropertiesProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilter.FindingsFilterListItemProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "name": "name"},
    )
    class FindingsFilterListItemProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the unique identifier and custom name of a findings filter.

            :param id: The unique identifier for the filter.
            :param name: The custom name of the filter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                findings_filter_list_item_property = macie.CfnFindingsFilter.FindingsFilterListItemProperty(
                    id="id",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7156e20d45f08aa3f36cbd419e31b5c99ba4fc02173fd094581cde0ddf8a628)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for the filter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The custom name of the filter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingsFilterListItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "finding_criteria": "findingCriteria",
        "name": "name",
        "action": "action",
        "description": "description",
        "position": "position",
    },
)
class CfnFindingsFilterProps:
    def __init__(
        self,
        *,
        finding_criteria: typing.Union[typing.Union[CfnFindingsFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnFindingsFilter``.

        :param finding_criteria: The criteria to use to filter findings.
        :param name: A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters. We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users might be able to see the filter's name, depending on the actions that they're allowed to perform in Amazon Macie .
        :param action: The action to perform on findings that meet the filter criteria ( ``FindingCriteria`` ). Valid values are:. - ARCHIVE - Suppress (automatically archive) the findings. - NOOP - Don't perform any action on the findings.
        :param description: A custom description of the filter. The description can contain as many as 512 characters. We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users might be able to see the filter's description, depending on the actions that they're allowed to perform in Amazon Macie .
        :param position: The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_macie as macie
            
            cfn_findings_filter_props = macie.CfnFindingsFilterProps(
                finding_criteria=macie.CfnFindingsFilter.FindingCriteriaProperty(
                    criterion={
                        "criterion_key": macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty(
                            eq=["eq"],
                            gt=123,
                            gte=123,
                            lt=123,
                            lte=123,
                            neq=["neq"]
                        )
                    }
                ),
                name="name",
            
                # the properties below are optional
                action="action",
                description="description",
                position=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4769b70b8b409b7293b4cfb98a775272d6996bc39a6b96c3ad8c76c7aae51f1)
            check_type(argname="argument finding_criteria", value=finding_criteria, expected_type=type_hints["finding_criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "finding_criteria": finding_criteria,
            "name": name,
        }
        if action is not None:
            self._values["action"] = action
        if description is not None:
            self._values["description"] = description
        if position is not None:
            self._values["position"] = position

    @builtins.property
    def finding_criteria(
        self,
    ) -> typing.Union[CfnFindingsFilter.FindingCriteriaProperty, _IResolvable_da3f097b]:
        '''The criteria to use to filter findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria
        '''
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return typing.cast(typing.Union[CfnFindingsFilter.FindingCriteriaProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A custom name for the filter.

        The name must contain at least 3 characters and can contain as many as 64 characters.

        We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users might be able to see the filter's name, depending on the actions that they're allowed to perform in Amazon Macie .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''The action to perform on findings that meet the filter criteria ( ``FindingCriteria`` ). Valid values are:.

        - ARCHIVE - Suppress (automatically archive) the findings.
        - NOOP - Don't perform any action on the findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the filter. The description can contain as many as 512 characters.

        We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users might be able to see the filter's description, depending on the actions that they're allowed to perform in Amazon Macie .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def position(self) -> typing.Optional[jsii.Number]:
        '''The position of the filter in the list of saved filters on the Amazon Macie console.

        This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position
        '''
        result = self._values.get("position")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFindingsFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSession(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_macie.CfnSession",
):
    '''A CloudFormation ``AWS::Macie::Session``.

    The ``AWS::Macie::Session`` resource represents the Amazon Macie service and configuration settings for an account. A ``Session`` is created for each AWS Region in which you enable Macie .

    You must create a ``Session`` for an account before you can create an ``AWS::Macie::FindingsFilter`` or ``AWS::Macie::CustomDataIdentifier`` resource. Use a `DependsOn attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ to ensure that the ``Session`` is created before the other resources. For example, ``"DependsOn: Session"`` .

    :cloudformationResource: AWS::Macie::Session
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_macie as macie
        
        cfn_session = macie.CfnSession(self, "MyCfnSession",
            finding_publishing_frequency="findingPublishingFrequency",
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Macie::Session``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param finding_publishing_frequency: The frequency with which Amazon Macie publishes updates to policy findings for an account. This includes publishing updates to AWS Security Hub and Amazon EventBridge (formerly called Amazon CloudWatch Events ). Valid values are: - FIFTEEN_MINUTES - ONE_HOUR - SIX_HOURS
        :param status: The ``MacieStatus`` of the ``Session`` . Valid values include ``ENABLED`` and ``PAUSED`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__459832705822182508c6f2e0693fc53e3b0d82a4e148ecfdd93f163e3afc3417)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSessionProps(
            finding_publishing_frequency=finding_publishing_frequency, status=status
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a78d5968f4acb7046cb1b0be5462b857c06e6bc787c27f94c2f393e3f681e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e43074ce924e3f898d598fd4b912046beaaf89bc693c659909791046eca7b32)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''The account ID for the AWS account in which the ``Session`` is created.

        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceRole")
    def attr_service_role(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the service-linked role that allows Amazon Macie to monitor and analyze data in AWS resources for the account.

        :cloudformationAttribute: ServiceRole
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceRole"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''The frequency with which Amazon Macie publishes updates to policy findings for an account.

        This includes publishing updates to AWS Security Hub and Amazon EventBridge (formerly called Amazon CloudWatch Events ). Valid values are:

        - FIFTEEN_MINUTES
        - ONE_HOUR
        - SIX_HOURS

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "findingPublishingFrequency"))

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbab990e35f30e653778479d30de4521365d972399b5f819c47f60195a95dab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingPublishingFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The ``MacieStatus`` of the ``Session`` .

        Valid values include ``ENABLED`` and ``PAUSED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e25551195a36935d5b88ee54046aee0f17d2de93fdfb0eaa1a2571fd568ef3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_macie.CfnSessionProps",
    jsii_struct_bases=[],
    name_mapping={
        "finding_publishing_frequency": "findingPublishingFrequency",
        "status": "status",
    },
)
class CfnSessionProps:
    def __init__(
        self,
        *,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSession``.

        :param finding_publishing_frequency: The frequency with which Amazon Macie publishes updates to policy findings for an account. This includes publishing updates to AWS Security Hub and Amazon EventBridge (formerly called Amazon CloudWatch Events ). Valid values are: - FIFTEEN_MINUTES - ONE_HOUR - SIX_HOURS
        :param status: The ``MacieStatus`` of the ``Session`` . Valid values include ``ENABLED`` and ``PAUSED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_macie as macie
            
            cfn_session_props = macie.CfnSessionProps(
                finding_publishing_frequency="findingPublishingFrequency",
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b2377975304db82e025e7e966713f33964f9e33889db82b2e26a095d3fb3f14)
            check_type(argname="argument finding_publishing_frequency", value=finding_publishing_frequency, expected_type=type_hints["finding_publishing_frequency"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if finding_publishing_frequency is not None:
            self._values["finding_publishing_frequency"] = finding_publishing_frequency
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''The frequency with which Amazon Macie publishes updates to policy findings for an account.

        This includes publishing updates to AWS Security Hub and Amazon EventBridge (formerly called Amazon CloudWatch Events ). Valid values are:

        - FIFTEEN_MINUTES
        - ONE_HOUR
        - SIX_HOURS

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency
        '''
        result = self._values.get("finding_publishing_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The ``MacieStatus`` of the ``Session`` .

        Valid values include ``ENABLED`` and ``PAUSED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSessionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAllowList",
    "CfnAllowListProps",
    "CfnCustomDataIdentifier",
    "CfnCustomDataIdentifierProps",
    "CfnFindingsFilter",
    "CfnFindingsFilterProps",
    "CfnSession",
    "CfnSessionProps",
]

publication.publish()

def _typecheckingstub__ef55cb8aaca32dcf264ac0e8768dc1c5a0b1471c41c8de3c9575f20000ca4bd9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    criteria: typing.Union[typing.Union[CfnAllowList.CriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de89a42feae1bdccf1b7fb468bda2c5700b1aa71c5c523cb2c69a8c666ae8e2a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7369f7a4bca5c49d764dbf34faf902a40c52828d8fba955e4eca05e9adcaff7a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e4ae58b4636b7db31b0fa3adc3410ae3d14049fa02c2bd307123f1749460647(
    value: typing.Union[CfnAllowList.CriteriaProperty, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d690571d1b7ea81f4eaac91920c04dab927cd0ddc18b3539a84afdcb50cfdc4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff0733233420991a19ec573286f220cf810fc8bd281a542a9fa2c82daf4c241(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916c849be567db5e8b2d28b4262b1b5e6cc4efa0cc6749b882394480f94b0f1a(
    *,
    regex: typing.Optional[builtins.str] = None,
    s3_words_list: typing.Optional[typing.Union[typing.Union[CfnAllowList.S3WordsListProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6728338d9836f378990a221bfcb5d4ebc176286721060379316cb044250d5933(
    *,
    bucket_name: builtins.str,
    object_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cde4980d3f47e6973fbc0136f9a40cf0f5706f781fb45f3cc0aad4b99e96d39(
    *,
    criteria: typing.Union[typing.Union[CfnAllowList.CriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8462f70ed2396867e691499b8338ee06166375569e4774b35cad18418587284c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    regex: builtins.str,
    description: typing.Optional[builtins.str] = None,
    ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
    keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
    maximum_match_distance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e9300d86a3080fc43c5b9e06f708ec6e0be23ca1a8b8c548c28f04d4a38b47(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2273c82378b08a1921a6584b6eafca3f9442f8236c8797614cdc38e93f50a4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56bafc0e98388f95c36a25cdb08ac16d1b32e9b68fc70fc559070e909e26043f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a88698a8e31c22c8a96936b106ec14252c0df95a0c621ffc59448549cfe4f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4eac22a0be7a58617fc706b4a6f4df1d7c10d4fd1bcb1bc7c87ecb091280ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35dff10296c96b79146377714bebc3cb572a5fc32fda7088add5e2e9c20cfb52(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1910816738c1d222482ca791d3639f1eb091753a7bef0627a18c8298817c4083(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baadf50a05df72179523cc44ce07f1d05939df835131681e825e51b9a74778eb(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b153bc4a75175074214978bb8d0954e3d477b6896260fae9394ce3a3f3ef2463(
    *,
    name: builtins.str,
    regex: builtins.str,
    description: typing.Optional[builtins.str] = None,
    ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
    keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
    maximum_match_distance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11b08ade332eec06142e65a0667c3f977a9418dbb1685fc4d53acba74840039e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    finding_criteria: typing.Union[typing.Union[CfnFindingsFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    name: builtins.str,
    action: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    position: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a93c27322ef7d4277d7a472e492eca4e1a6e853c53d3268dc2ece902bef2ea0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f86624cef1fb49b3b96cefbc1b1ef17881bea27e106666e69078116a2c0ce5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca4bea48d84a530685d7cefc7aab036a382728b48d306044f2a518d375e31af(
    value: typing.Union[CfnFindingsFilter.FindingCriteriaProperty, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d67d6558f4b26d340cf216d4866559bbaf532c9defe9a11eb199af1a7d2433c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41dfbe847eece32f936f8bf3bb5d835d163ba85d1ce1a626fe00a0cb995afaa0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03fc2464c8c604a167f22170fbed859036b5124a2e5d8b3f089b061f6bf605cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60836229071347a8b3064cb2b271455290f497cd552169c6180768b3a67ea2e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc0e94f951064d75bcef2cb73a1a20831df93d286eb235e35e3f7f153419f00(
    *,
    eq: typing.Optional[typing.Sequence[builtins.str]] = None,
    gt: typing.Optional[jsii.Number] = None,
    gte: typing.Optional[jsii.Number] = None,
    lt: typing.Optional[jsii.Number] = None,
    lte: typing.Optional[jsii.Number] = None,
    neq: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa11a0d6136e31dcc0f57ce160cc975d2fd8978372183978096da64d7bb37e8(
    *,
    criterion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnFindingsFilter.CriterionAdditionalPropertiesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7156e20d45f08aa3f36cbd419e31b5c99ba4fc02173fd094581cde0ddf8a628(
    *,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4769b70b8b409b7293b4cfb98a775272d6996bc39a6b96c3ad8c76c7aae51f1(
    *,
    finding_criteria: typing.Union[typing.Union[CfnFindingsFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    name: builtins.str,
    action: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    position: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__459832705822182508c6f2e0693fc53e3b0d82a4e148ecfdd93f163e3afc3417(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    finding_publishing_frequency: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a78d5968f4acb7046cb1b0be5462b857c06e6bc787c27f94c2f393e3f681e9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e43074ce924e3f898d598fd4b912046beaaf89bc693c659909791046eca7b32(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbab990e35f30e653778479d30de4521365d972399b5f819c47f60195a95dab3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e25551195a36935d5b88ee54046aee0f17d2de93fdfb0eaa1a2571fd568ef3f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2377975304db82e025e7e966713f33964f9e33889db82b2e26a095d3fb3f14(
    *,
    finding_publishing_frequency: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
