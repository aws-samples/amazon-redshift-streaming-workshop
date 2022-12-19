'''
# AWS AppSync Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_appsync as appsync
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppSync construct libraries](https://constructs.dev/search?q=appsync)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppSync resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppSync.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-appsync-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppSync](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppSync.html).

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
class CfnApiCache(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnApiCache",
):
    '''A CloudFormation ``AWS::AppSync::ApiCache``.

    The ``AWS::AppSync::ApiCache`` resource represents the input of a ``CreateApiCache`` operation.

    :cloudformationResource: AWS::AppSync::ApiCache
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_api_cache = appsync.CfnApiCache(self, "MyCfnApiCache",
            api_caching_behavior="apiCachingBehavior",
            api_id="apiId",
            ttl=123,
            type="type",
        
            # the properties below are optional
            at_rest_encryption_enabled=False,
            transit_encryption_enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_caching_behavior: builtins.str,
        api_id: builtins.str,
        ttl: jsii.Number,
        type: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::AppSync::ApiCache``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_caching_behavior: Caching behavior. - *FULL_REQUEST_CACHING* : All requests are fully cached. - *PER_RESOLVER_CACHING* : Individual resolvers that you specify are cached.
        :param api_id: The GraphQL API ID.
        :param ttl: TTL in seconds for cache entries. Valid values are 1–3,600 seconds.
        :param type: The cache instance type. Valid values are. - ``SMALL`` - ``MEDIUM`` - ``LARGE`` - ``XLARGE`` - ``LARGE_2X`` - ``LARGE_4X`` - ``LARGE_8X`` (not available in all regions) - ``LARGE_12X`` Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used. The following legacy instance types are available, but their use is discouraged: - *T2_SMALL* : A t2.small instance type. - *T2_MEDIUM* : A t2.medium instance type. - *R4_LARGE* : A r4.large instance type. - *R4_XLARGE* : A r4.xlarge instance type. - *R4_2XLARGE* : A r4.2xlarge instance type. - *R4_4XLARGE* : A r4.4xlarge instance type. - *R4_8XLARGE* : A r4.8xlarge instance type.
        :param at_rest_encryption_enabled: At-rest encryption flag for cache. You cannot update this setting after creation.
        :param transit_encryption_enabled: Transit encryption flag when connecting to cache. You cannot update this setting after creation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9d92b7b2abdac7341eb92f7ac10d2d67dd2700af68eaf42c72c47ffdaacc344)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiCacheProps(
            api_caching_behavior=api_caching_behavior,
            api_id=api_id,
            ttl=ttl,
            type=type,
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            transit_encryption_enabled=transit_encryption_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142193172b7ee1304f3b8fd949531b4cfa950ea62d0dc10f9ed5a184a603132d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ce863b5f21a86ce886458054cd4de0550269c18eb7c4f3fb37884dc2869845e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiCachingBehavior")
    def api_caching_behavior(self) -> builtins.str:
        '''Caching behavior.

        - *FULL_REQUEST_CACHING* : All requests are fully cached.
        - *PER_RESOLVER_CACHING* : Individual resolvers that you specify are cached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apicachingbehavior
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiCachingBehavior"))

    @api_caching_behavior.setter
    def api_caching_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aee6b3576fbf654864dae4f55fe292d210bf01534f16f80af0ac225f8fa338c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiCachingBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The GraphQL API ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apiid
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c2fdac623dbaddb2a0226d75e6f3ca84c058f3f46b9c9a1289820c1cf0827e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        '''TTL in seconds for cache entries.

        Valid values are 1–3,600 seconds.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-ttl
        '''
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1893b7ba08236941b8e5bb4704e7fe53f8819086085796443b5d68f513e66eaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The cache instance type. Valid values are.

        - ``SMALL``
        - ``MEDIUM``
        - ``LARGE``
        - ``XLARGE``
        - ``LARGE_2X``
        - ``LARGE_4X``
        - ``LARGE_8X`` (not available in all regions)
        - ``LARGE_12X``

        Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.

        The following legacy instance types are available, but their use is discouraged:

        - *T2_SMALL* : A t2.small instance type.
        - *T2_MEDIUM* : A t2.medium instance type.
        - *R4_LARGE* : A r4.large instance type.
        - *R4_XLARGE* : A r4.xlarge instance type.
        - *R4_2XLARGE* : A r4.2xlarge instance type.
        - *R4_4XLARGE* : A r4.4xlarge instance type.
        - *R4_8XLARGE* : A r4.8xlarge instance type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45dc491e21920c6cd0ddecd9aada80283ac759d9eaca52c45a6ce35197166e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''At-rest encryption flag for cache.

        You cannot update this setting after creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-atrestencryptionenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "atRestEncryptionEnabled"))

    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93a4abe242f634763c1f128b7e17017d1176924c9b032d5536f4caa3b3fc3bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "atRestEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Transit encryption flag when connecting to cache.

        You cannot update this setting after creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-transitencryptionenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "transitEncryptionEnabled"))

    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb39499095e917401c885f7c77781744d09df071b1ed62c6f2c32cbbc6fbdb33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionEnabled", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnApiCacheProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_caching_behavior": "apiCachingBehavior",
        "api_id": "apiId",
        "ttl": "ttl",
        "type": "type",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "transit_encryption_enabled": "transitEncryptionEnabled",
    },
)
class CfnApiCacheProps:
    def __init__(
        self,
        *,
        api_caching_behavior: builtins.str,
        api_id: builtins.str,
        ttl: jsii.Number,
        type: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApiCache``.

        :param api_caching_behavior: Caching behavior. - *FULL_REQUEST_CACHING* : All requests are fully cached. - *PER_RESOLVER_CACHING* : Individual resolvers that you specify are cached.
        :param api_id: The GraphQL API ID.
        :param ttl: TTL in seconds for cache entries. Valid values are 1–3,600 seconds.
        :param type: The cache instance type. Valid values are. - ``SMALL`` - ``MEDIUM`` - ``LARGE`` - ``XLARGE`` - ``LARGE_2X`` - ``LARGE_4X`` - ``LARGE_8X`` (not available in all regions) - ``LARGE_12X`` Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used. The following legacy instance types are available, but their use is discouraged: - *T2_SMALL* : A t2.small instance type. - *T2_MEDIUM* : A t2.medium instance type. - *R4_LARGE* : A r4.large instance type. - *R4_XLARGE* : A r4.xlarge instance type. - *R4_2XLARGE* : A r4.2xlarge instance type. - *R4_4XLARGE* : A r4.4xlarge instance type. - *R4_8XLARGE* : A r4.8xlarge instance type.
        :param at_rest_encryption_enabled: At-rest encryption flag for cache. You cannot update this setting after creation.
        :param transit_encryption_enabled: Transit encryption flag when connecting to cache. You cannot update this setting after creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_api_cache_props = appsync.CfnApiCacheProps(
                api_caching_behavior="apiCachingBehavior",
                api_id="apiId",
                ttl=123,
                type="type",
            
                # the properties below are optional
                at_rest_encryption_enabled=False,
                transit_encryption_enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f054fa3186eb5f122c20e523bed485713c72511ee3ee94be25733ecad9a348c)
            check_type(argname="argument api_caching_behavior", value=api_caching_behavior, expected_type=type_hints["api_caching_behavior"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument at_rest_encryption_enabled", value=at_rest_encryption_enabled, expected_type=type_hints["at_rest_encryption_enabled"])
            check_type(argname="argument transit_encryption_enabled", value=transit_encryption_enabled, expected_type=type_hints["transit_encryption_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_caching_behavior": api_caching_behavior,
            "api_id": api_id,
            "ttl": ttl,
            "type": type,
        }
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled

    @builtins.property
    def api_caching_behavior(self) -> builtins.str:
        '''Caching behavior.

        - *FULL_REQUEST_CACHING* : All requests are fully cached.
        - *PER_RESOLVER_CACHING* : Individual resolvers that you specify are cached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apicachingbehavior
        '''
        result = self._values.get("api_caching_behavior")
        assert result is not None, "Required property 'api_caching_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The GraphQL API ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ttl(self) -> jsii.Number:
        '''TTL in seconds for cache entries.

        Valid values are 1–3,600 seconds.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-ttl
        '''
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The cache instance type. Valid values are.

        - ``SMALL``
        - ``MEDIUM``
        - ``LARGE``
        - ``XLARGE``
        - ``LARGE_2X``
        - ``LARGE_4X``
        - ``LARGE_8X`` (not available in all regions)
        - ``LARGE_12X``

        Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.

        The following legacy instance types are available, but their use is discouraged:

        - *T2_SMALL* : A t2.small instance type.
        - *T2_MEDIUM* : A t2.medium instance type.
        - *R4_LARGE* : A r4.large instance type.
        - *R4_XLARGE* : A r4.xlarge instance type.
        - *R4_2XLARGE* : A r4.2xlarge instance type.
        - *R4_4XLARGE* : A r4.4xlarge instance type.
        - *R4_8XLARGE* : A r4.8xlarge instance type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''At-rest encryption flag for cache.

        You cannot update this setting after creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-atrestencryptionenabled
        '''
        result = self._values.get("at_rest_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Transit encryption flag when connecting to cache.

        You cannot update this setting after creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-transitencryptionenabled
        '''
        result = self._values.get("transit_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiCacheProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnApiKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnApiKey",
):
    '''A CloudFormation ``AWS::AppSync::ApiKey``.

    The ``AWS::AppSync::ApiKey`` resource creates a unique key that you can distribute to clients who are executing GraphQL operations with AWS AppSync that require an API key.

    :cloudformationResource: AWS::AppSync::ApiKey
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_api_key = appsync.CfnApiKey(self, "MyCfnApiKey",
            api_id="apiId",
        
            # the properties below are optional
            api_key_id="apiKeyId",
            description="description",
            expires=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        api_key_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::AppSync::ApiKey``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: Unique AWS AppSync GraphQL API ID for this API key.
        :param api_key_id: The API key ID.
        :param description: Unique description of your API key.
        :param expires: The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6065dd18c9d420fd4fcd70aced8416006f044f82aecff54150165e832539a8e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiKeyProps(
            api_id=api_id,
            api_key_id=api_key_id,
            description=description,
            expires=expires,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8f02bc91fc0b32c990b8d08a5d7a0ef78a88363920fa69d4196dcc7f2ecfb3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a844b496712966f29aae49f2f831e6a85c7acf03c2ce61c94162ccf13c5efd6d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiKey")
    def attr_api_key(self) -> builtins.str:
        '''The API key.

        :cloudformationAttribute: ApiKey
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiKey"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the API key, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/apikey/apikeya1bzhi`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API ID for this API key.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apiid
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c1cce5f76a6037620e1cc2e57750c81cc5161ff526ce78123f0cd9f25c8e856)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="apiKeyId")
    def api_key_id(self) -> typing.Optional[builtins.str]:
        '''The API key ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apikeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyId"))

    @api_key_id.setter
    def api_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f5d6818eefb673237292bb9320e2134ad0c799f70d17a7cba2de3f4298ccf5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Unique description of your API key.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08afa042939638da41f04c7165f811f5081bd3c8943f787591f098aa4a3b8699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expires")
    def expires(self) -> typing.Optional[jsii.Number]:
        '''The time after which the API key expires.

        The date is represented as seconds since the epoch, rounded down to the nearest hour.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expires"))

    @expires.setter
    def expires(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b034facb88dea82241969fd1a22a5bbaccf03068403021106e073c92112ab45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expires", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnApiKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "api_key_id": "apiKeyId",
        "description": "description",
        "expires": "expires",
    },
)
class CfnApiKeyProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        api_key_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnApiKey``.

        :param api_id: Unique AWS AppSync GraphQL API ID for this API key.
        :param api_key_id: The API key ID.
        :param description: Unique description of your API key.
        :param expires: The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_api_key_props = appsync.CfnApiKeyProps(
                api_id="apiId",
            
                # the properties below are optional
                api_key_id="apiKeyId",
                description="description",
                expires=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1688db2b7835c85b4e2cd69655b5d25321ff2aa2ea9e1b2a0612caff34184549)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument api_key_id", value=api_key_id, expected_type=type_hints["api_key_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expires", value=expires, expected_type=type_hints["expires"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
        }
        if api_key_id is not None:
            self._values["api_key_id"] = api_key_id
        if description is not None:
            self._values["description"] = description
        if expires is not None:
            self._values["expires"] = expires

    @builtins.property
    def api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API ID for this API key.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_key_id(self) -> typing.Optional[builtins.str]:
        '''The API key ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apikeyid
        '''
        result = self._values.get("api_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Unique description of your API key.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires(self) -> typing.Optional[jsii.Number]:
        '''The time after which the API key expires.

        The date is represented as seconds since the epoch, rounded down to the nearest hour.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires
        '''
        result = self._values.get("expires")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDataSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource",
):
    '''A CloudFormation ``AWS::AppSync::DataSource``.

    The ``AWS::AppSync::DataSource`` resource creates data sources for resolvers in AWS AppSync to connect to, such as Amazon DynamoDB , AWS Lambda , and Amazon OpenSearch Service . Resolvers use these data sources to fetch data when clients make GraphQL calls.

    :cloudformationResource: AWS::AppSync::DataSource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_data_source = appsync.CfnDataSource(self, "MyCfnDataSource",
            api_id="apiId",
            name="name",
            type="type",
        
            # the properties below are optional
            description="description",
            dynamo_db_config=appsync.CfnDataSource.DynamoDBConfigProperty(
                aws_region="awsRegion",
                table_name="tableName",
        
                # the properties below are optional
                delta_sync_config=appsync.CfnDataSource.DeltaSyncConfigProperty(
                    base_table_ttl="baseTableTtl",
                    delta_sync_table_name="deltaSyncTableName",
                    delta_sync_table_ttl="deltaSyncTableTtl"
                ),
                use_caller_credentials=False,
                versioned=False
            ),
            elasticsearch_config=appsync.CfnDataSource.ElasticsearchConfigProperty(
                aws_region="awsRegion",
                endpoint="endpoint"
            ),
            http_config=appsync.CfnDataSource.HttpConfigProperty(
                endpoint="endpoint",
        
                # the properties below are optional
                authorization_config=appsync.CfnDataSource.AuthorizationConfigProperty(
                    authorization_type="authorizationType",
        
                    # the properties below are optional
                    aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                        signing_region="signingRegion",
                        signing_service_name="signingServiceName"
                    )
                )
            ),
            lambda_config=appsync.CfnDataSource.LambdaConfigProperty(
                lambda_function_arn="lambdaFunctionArn"
            ),
            open_search_service_config=appsync.CfnDataSource.OpenSearchServiceConfigProperty(
                aws_region="awsRegion",
                endpoint="endpoint"
            ),
            relational_database_config=appsync.CfnDataSource.RelationalDatabaseConfigProperty(
                relational_database_source_type="relationalDatabaseSourceType",
        
                # the properties below are optional
                rds_http_endpoint_config=appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                    aws_region="awsRegion",
                    aws_secret_store_arn="awsSecretStoreArn",
                    db_cluster_identifier="dbClusterIdentifier",
        
                    # the properties below are optional
                    database_name="databaseName",
                    schema="schema"
                )
            ),
            service_role_arn="serviceRoleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamo_db_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.DynamoDBConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        elasticsearch_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.ElasticsearchConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        http_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.HttpConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        lambda_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.LambdaConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        open_search_service_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.OpenSearchServiceConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        relational_database_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::AppSync::DataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: Unique AWS AppSync GraphQL API identifier where this data source will be created.
        :param name: Friendly name for you to identify your AppSync data source after creation.
        :param type: The type of the data source. - *AWS_LAMBDA* : The data source is an AWS Lambda function. - *AMAZON_DYNAMODB* : The data source is an Amazon DynamoDB table. - *AMAZON_ELASTICSEARCH* : The data source is an Amazon OpenSearch Service domain. - *AMAZON_OPENSEARCH_SERVICE* : The data source is an Amazon OpenSearch Service domain. - *NONE* : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation. - *HTTP* : The data source is an HTTP endpoint. - *RELATIONAL_DATABASE* : The data source is a relational database.
        :param description: The description of the data source.
        :param dynamo_db_config: AWS Region and TableName for an Amazon DynamoDB table in your account.
        :param elasticsearch_config: AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account. As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.
        :param http_config: Endpoints for an HTTP data source.
        :param lambda_config: An ARN of a Lambda function in valid ARN format. This can be the ARN of a Lambda function that exists in the current account or in another account.
        :param open_search_service_config: AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.
        :param relational_database_config: Relational Database configuration of the relational database data source.
        :param service_role_arn: The AWS Identity and Access Management service role ARN for the data source. The system assumes this role when accessing the data source. Required if ``Type`` is specified as ``AWS_LAMBDA`` , ``AMAZON_DYNAMODB`` , ``AMAZON_ELASTICSEARCH`` , or ``AMAZON_OPENSEARCH_SERVICE`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2dc8968068d09d9cb599cea5efad1a18016c4eca4fcc6c15e6169a0891e2678)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataSourceProps(
            api_id=api_id,
            name=name,
            type=type,
            description=description,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            open_search_service_config=open_search_service_config,
            relational_database_config=relational_database_config,
            service_role_arn=service_role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844d45e22564aca7d878e00ff3e6a39f30d70312a9d2fcf8bb2f587b070069f7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb33982b2405feec8337a5b841ef30f58e28ed8058a2e3d003d09ee8aac516a9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDataSourceArn")
    def attr_data_source_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the API key, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/datasources/datasourcename`` .

        :cloudformationAttribute: DataSourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataSourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Friendly name for you to identify your AWS AppSync data source after creation.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API identifier where this data source will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-apiid
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7863787830eb114a9c03188cb3a3bfd0b865645dac5dd0d3cf0b374c0a1af6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Friendly name for you to identify your AppSync data source after creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba82e0d60919163b242fed29c81421c4160f75a79249e58ce74b20f6b7d0f03d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the data source.

        - *AWS_LAMBDA* : The data source is an AWS Lambda function.
        - *AMAZON_DYNAMODB* : The data source is an Amazon DynamoDB table.
        - *AMAZON_ELASTICSEARCH* : The data source is an Amazon OpenSearch Service domain.
        - *AMAZON_OPENSEARCH_SERVICE* : The data source is an Amazon OpenSearch Service domain.
        - *NONE* : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
        - *HTTP* : The data source is an HTTP endpoint.
        - *RELATIONAL_DATABASE* : The data source is a relational database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aae6a5f086f2d2c36e8dff3cce5906d962da71d7148d7feec996abb025fb8f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29cebb36b12bc9cd3423d5991aeea26c635c2541d63fc9c3309a2177c24f1118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dynamoDbConfig")
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_da3f097b]]:
        '''AWS Region and TableName for an Amazon DynamoDB table in your account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-dynamodbconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "dynamoDbConfig"))

    @dynamo_db_config.setter
    def dynamo_db_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffaca3e4a18d434a01277621d6792259ab70047809af34a6cb0bab3eb7886a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamoDbConfig", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_da3f097b]]:
        '''AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.

        As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-elasticsearchconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "elasticsearchConfig"))

    @elasticsearch_config.setter
    def elasticsearch_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5323c0bb4d330a2f6b24616dd2b47847aa913d75611ddeae3cc451eda7ebb774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchConfig", value)

    @builtins.property
    @jsii.member(jsii_name="httpConfig")
    def http_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_da3f097b]]:
        '''Endpoints for an HTTP data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-httpconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "httpConfig"))

    @http_config.setter
    def http_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2b1129f048e5b946eceb4eb9c372f68c9a28e32ebe6091b611c3b1b82e3e83d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpConfig", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_da3f097b]]:
        '''An ARN of a Lambda function in valid ARN format.

        This can be the ARN of a Lambda function that exists in the current account or in another account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-lambdaconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "lambdaConfig"))

    @lambda_config.setter
    def lambda_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ff8b510d0035620c1325857ec673c802695c9f3c8dd8fa109d1b44e652a641)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaConfig", value)

    @builtins.property
    @jsii.member(jsii_name="openSearchServiceConfig")
    def open_search_service_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.OpenSearchServiceConfigProperty", _IResolvable_da3f097b]]:
        '''AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-opensearchserviceconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.OpenSearchServiceConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "openSearchServiceConfig"))

    @open_search_service_config.setter
    def open_search_service_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.OpenSearchServiceConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__876dd6f7515f1b03442f4aa7a0d78d1d6e5eef401db8d851e96b713bd30f989e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openSearchServiceConfig", value)

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_da3f097b]]:
        '''Relational Database configuration of the relational database data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-relationaldatabaseconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "relationalDatabaseConfig"))

    @relational_database_config.setter
    def relational_database_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72a1c504ec56f95938bf0b2a05d96acc7eb4b1190dc7285e9c33b6b194318386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relationalDatabaseConfig", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''The AWS Identity and Access Management service role ARN for the data source.

        The system assumes this role when accessing the data source.

        Required if ``Type`` is specified as ``AWS_LAMBDA`` , ``AMAZON_DYNAMODB`` , ``AMAZON_ELASTICSEARCH`` , or ``AMAZON_OPENSEARCH_SERVICE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8d23554bf1b07da4d8bb262596b409805d205b461615d34726f3323315abb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.AuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_type": "authorizationType",
            "aws_iam_config": "awsIamConfig",
        },
    )
    class AuthorizationConfigProperty:
        def __init__(
            self,
            *,
            authorization_type: builtins.str,
            aws_iam_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.AwsIamConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``AuthorizationConfig`` property type specifies the authorization type and configuration for an AWS AppSync http data source.

            ``AuthorizationConfig`` is a property of the `AWS AppSync DataSource HttpConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html>`_ property type.

            :param authorization_type: The authorization type that the HTTP endpoint requires. - *AWS_IAM* : The authorization type is Signature Version 4 (SigV4).
            :param aws_iam_config: The AWS Identity and Access Management settings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                authorization_config_property = appsync.CfnDataSource.AuthorizationConfigProperty(
                    authorization_type="authorizationType",
                
                    # the properties below are optional
                    aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                        signing_region="signingRegion",
                        signing_service_name="signingServiceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b40b2b6b828a39a91cb37d699b9dccbe36d457b235d0c89f8d63a8c926a5443)
                check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
                check_type(argname="argument aws_iam_config", value=aws_iam_config, expected_type=type_hints["aws_iam_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorization_type": authorization_type,
            }
            if aws_iam_config is not None:
                self._values["aws_iam_config"] = aws_iam_config

        @builtins.property
        def authorization_type(self) -> builtins.str:
            '''The authorization type that the HTTP endpoint requires.

            - *AWS_IAM* : The authorization type is Signature Version 4 (SigV4).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-authorizationtype
            '''
            result = self._values.get("authorization_type")
            assert result is not None, "Required property 'authorization_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_iam_config(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.AwsIamConfigProperty", _IResolvable_da3f097b]]:
            '''The AWS Identity and Access Management settings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-awsiamconfig
            '''
            result = self._values.get("aws_iam_config")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.AwsIamConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.AwsIamConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "signing_region": "signingRegion",
            "signing_service_name": "signingServiceName",
        },
    )
    class AwsIamConfigProperty:
        def __init__(
            self,
            *,
            signing_region: typing.Optional[builtins.str] = None,
            signing_service_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the ``AwsIamConfig`` property type to specify ``AwsIamConfig`` for a AWS AppSync authorizaton.

            ``AwsIamConfig`` is a property of the `AWS AppSync DataSource AuthorizationConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig-authorizationconfig.html>`_ resource.

            :param signing_region: The signing Region for AWS Identity and Access Management authorization.
            :param signing_service_name: The signing service name for AWS Identity and Access Management authorization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                aws_iam_config_property = appsync.CfnDataSource.AwsIamConfigProperty(
                    signing_region="signingRegion",
                    signing_service_name="signingServiceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63d3d6847bbd8b570bb51728b12402301a578fc159522a9bb797a8042b7c43dd)
                check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
                check_type(argname="argument signing_service_name", value=signing_service_name, expected_type=type_hints["signing_service_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if signing_region is not None:
                self._values["signing_region"] = signing_region
            if signing_service_name is not None:
                self._values["signing_service_name"] = signing_service_name

        @builtins.property
        def signing_region(self) -> typing.Optional[builtins.str]:
            '''The signing Region for AWS Identity and Access Management authorization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingregion
            '''
            result = self._values.get("signing_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def signing_service_name(self) -> typing.Optional[builtins.str]:
            '''The signing service name for AWS Identity and Access Management authorization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingservicename
            '''
            result = self._values.get("signing_service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsIamConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.DeltaSyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_table_ttl": "baseTableTtl",
            "delta_sync_table_name": "deltaSyncTableName",
            "delta_sync_table_ttl": "deltaSyncTableTtl",
        },
    )
    class DeltaSyncConfigProperty:
        def __init__(
            self,
            *,
            base_table_ttl: builtins.str,
            delta_sync_table_name: builtins.str,
            delta_sync_table_ttl: builtins.str,
        ) -> None:
            '''Describes a Delta Sync configuration.

            :param base_table_ttl: The number of minutes that an Item is stored in the data source.
            :param delta_sync_table_name: The Delta Sync table name.
            :param delta_sync_table_ttl: The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                delta_sync_config_property = appsync.CfnDataSource.DeltaSyncConfigProperty(
                    base_table_ttl="baseTableTtl",
                    delta_sync_table_name="deltaSyncTableName",
                    delta_sync_table_ttl="deltaSyncTableTtl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d8409bee2e379adfba84b9eedc28876ceca73a2b15ec9ad3045f33dc08a849c)
                check_type(argname="argument base_table_ttl", value=base_table_ttl, expected_type=type_hints["base_table_ttl"])
                check_type(argname="argument delta_sync_table_name", value=delta_sync_table_name, expected_type=type_hints["delta_sync_table_name"])
                check_type(argname="argument delta_sync_table_ttl", value=delta_sync_table_ttl, expected_type=type_hints["delta_sync_table_ttl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "base_table_ttl": base_table_ttl,
                "delta_sync_table_name": delta_sync_table_name,
                "delta_sync_table_ttl": delta_sync_table_ttl,
            }

        @builtins.property
        def base_table_ttl(self) -> builtins.str:
            '''The number of minutes that an Item is stored in the data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-basetablettl
            '''
            result = self._values.get("base_table_ttl")
            assert result is not None, "Required property 'base_table_ttl' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def delta_sync_table_name(self) -> builtins.str:
            '''The Delta Sync table name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablename
            '''
            result = self._values.get("delta_sync_table_name")
            assert result is not None, "Required property 'delta_sync_table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def delta_sync_table_ttl(self) -> builtins.str:
            '''The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablettl
            '''
            result = self._values.get("delta_sync_table_ttl")
            assert result is not None, "Required property 'delta_sync_table_ttl' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaSyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.DynamoDBConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "table_name": "tableName",
            "delta_sync_config": "deltaSyncConfig",
            "use_caller_credentials": "useCallerCredentials",
            "versioned": "versioned",
        },
    )
    class DynamoDBConfigProperty:
        def __init__(
            self,
            *,
            aws_region: builtins.str,
            table_name: builtins.str,
            delta_sync_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.DeltaSyncConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            use_caller_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            versioned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``DynamoDBConfig`` property type specifies the ``AwsRegion`` and ``TableName`` for an Amazon DynamoDB table in your account for an AWS AppSync data source.

            ``DynamoDBConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            :param aws_region: The AWS Region.
            :param table_name: The table name.
            :param delta_sync_config: The ``DeltaSyncConfig`` for a versioned datasource.
            :param use_caller_credentials: Set to ``TRUE`` to use AWS Identity and Access Management with this data source.
            :param versioned: Set to TRUE to use Conflict Detection and Resolution with this data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                dynamo_dBConfig_property = appsync.CfnDataSource.DynamoDBConfigProperty(
                    aws_region="awsRegion",
                    table_name="tableName",
                
                    # the properties below are optional
                    delta_sync_config=appsync.CfnDataSource.DeltaSyncConfigProperty(
                        base_table_ttl="baseTableTtl",
                        delta_sync_table_name="deltaSyncTableName",
                        delta_sync_table_ttl="deltaSyncTableTtl"
                    ),
                    use_caller_credentials=False,
                    versioned=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__66016c117898c1cc0dc84bb648ce56335f475ea29f1590882ca3229c1e8ffe3f)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument delta_sync_config", value=delta_sync_config, expected_type=type_hints["delta_sync_config"])
                check_type(argname="argument use_caller_credentials", value=use_caller_credentials, expected_type=type_hints["use_caller_credentials"])
                check_type(argname="argument versioned", value=versioned, expected_type=type_hints["versioned"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "table_name": table_name,
            }
            if delta_sync_config is not None:
                self._values["delta_sync_config"] = delta_sync_config
            if use_caller_credentials is not None:
                self._values["use_caller_credentials"] = use_caller_credentials
            if versioned is not None:
                self._values["versioned"] = versioned

        @builtins.property
        def aws_region(self) -> builtins.str:
            '''The AWS Region.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The table name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def delta_sync_config(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.DeltaSyncConfigProperty", _IResolvable_da3f097b]]:
            '''The ``DeltaSyncConfig`` for a versioned datasource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-deltasyncconfig
            '''
            result = self._values.get("delta_sync_config")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.DeltaSyncConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def use_caller_credentials(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set to ``TRUE`` to use AWS Identity and Access Management with this data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-usecallercredentials
            '''
            result = self._values.get("use_caller_credentials")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def versioned(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set to TRUE to use Conflict Detection and Resolution with this data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-versioned
            '''
            result = self._values.get("versioned")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.ElasticsearchConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_region": "awsRegion", "endpoint": "endpoint"},
    )
    class ElasticsearchConfigProperty:
        def __init__(self, *, aws_region: builtins.str, endpoint: builtins.str) -> None:
            '''The ``ElasticsearchConfig`` property type specifies the ``AwsRegion`` and ``Endpoints`` for an Amazon OpenSearch Service domain in your account for an AWS AppSync data source.

            ElasticsearchConfig is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.

            :param aws_region: The AWS Region.
            :param endpoint: The endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                elasticsearch_config_property = appsync.CfnDataSource.ElasticsearchConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7385ec04703540fe726bf7efc36f7ea05ba851b02e63ee657ec6cba21c5e805)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "endpoint": endpoint,
            }

        @builtins.property
        def aws_region(self) -> builtins.str:
            '''The AWS Region.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.HttpConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "authorization_config": "authorizationConfig",
        },
    )
    class HttpConfigProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            authorization_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.AuthorizationConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Use the ``HttpConfig`` property type to specify ``HttpConfig`` for an AWS AppSync data source.

            ``HttpConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ resource.

            :param endpoint: The endpoint.
            :param authorization_config: The authorization configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                http_config_property = appsync.CfnDataSource.HttpConfigProperty(
                    endpoint="endpoint",
                
                    # the properties below are optional
                    authorization_config=appsync.CfnDataSource.AuthorizationConfigProperty(
                        authorization_type="authorizationType",
                
                        # the properties below are optional
                        aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                            signing_region="signingRegion",
                            signing_service_name="signingServiceName"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d4a6ece9757475b2fd78d8a95bd18c7fd68758c889cf5d07cea125e31a32258)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
            }
            if authorization_config is not None:
                self._values["authorization_config"] = authorization_config

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.AuthorizationConfigProperty", _IResolvable_da3f097b]]:
            '''The authorization configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.AuthorizationConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.LambdaConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_function_arn": "lambdaFunctionArn"},
    )
    class LambdaConfigProperty:
        def __init__(self, *, lambda_function_arn: builtins.str) -> None:
            '''The ``LambdaConfig`` property type specifies the Lambda function ARN for an AWS AppSync data source.

            ``LambdaConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            :param lambda_function_arn: The ARN for the Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                lambda_config_property = appsync.CfnDataSource.LambdaConfigProperty(
                    lambda_function_arn="lambdaFunctionArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47ae7467c676f94be4511c7fb68e47ed5c3c90dde218c9a12592924c98f7837e)
                check_type(argname="argument lambda_function_arn", value=lambda_function_arn, expected_type=type_hints["lambda_function_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_function_arn": lambda_function_arn,
            }

        @builtins.property
        def lambda_function_arn(self) -> builtins.str:
            '''The ARN for the Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html#cfn-appsync-datasource-lambdaconfig-lambdafunctionarn
            '''
            result = self._values.get("lambda_function_arn")
            assert result is not None, "Required property 'lambda_function_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.OpenSearchServiceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_region": "awsRegion", "endpoint": "endpoint"},
    )
    class OpenSearchServiceConfigProperty:
        def __init__(self, *, aws_region: builtins.str, endpoint: builtins.str) -> None:
            '''The ``OpenSearchServiceConfig`` property type specifies the ``AwsRegion`` and ``Endpoints`` for an Amazon OpenSearch Service domain in your account for an AWS AppSync data source.

            ``OpenSearchServiceConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            :param aws_region: The AWS Region.
            :param endpoint: The endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                open_search_service_config_property = appsync.CfnDataSource.OpenSearchServiceConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fecf5845831a0e0a203174a1662e533c942ecf67ea1e85e246e7a029865de49)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "endpoint": endpoint,
            }

        @builtins.property
        def aws_region(self) -> builtins.str:
            '''The AWS Region.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html#cfn-appsync-datasource-opensearchserviceconfig-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html#cfn-appsync-datasource-opensearchserviceconfig-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenSearchServiceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.RdsHttpEndpointConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "aws_secret_store_arn": "awsSecretStoreArn",
            "db_cluster_identifier": "dbClusterIdentifier",
            "database_name": "databaseName",
            "schema": "schema",
        },
    )
    class RdsHttpEndpointConfigProperty:
        def __init__(
            self,
            *,
            aws_region: builtins.str,
            aws_secret_store_arn: builtins.str,
            db_cluster_identifier: builtins.str,
            database_name: typing.Optional[builtins.str] = None,
            schema: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the ``RdsHttpEndpointConfig`` property type to specify the ``RdsHttpEndpoint`` for an AWS AppSync relational database.

            ``RdsHttpEndpointConfig`` is a property of the `AWS AppSync DataSource RelationalDatabaseConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html>`_ resource.

            :param aws_region: AWS Region for RDS HTTP endpoint.
            :param aws_secret_store_arn: The ARN for database credentials stored in AWS Secrets Manager .
            :param db_cluster_identifier: Amazon RDS cluster Amazon Resource Name (ARN).
            :param database_name: Logical database name.
            :param schema: Logical schema name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                rds_http_endpoint_config_property = appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                    aws_region="awsRegion",
                    aws_secret_store_arn="awsSecretStoreArn",
                    db_cluster_identifier="dbClusterIdentifier",
                
                    # the properties below are optional
                    database_name="databaseName",
                    schema="schema"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__348849422fd4d08e7490da175f7a5ffa84cad62dcd8d49557a3436740b3dffd5)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument aws_secret_store_arn", value=aws_secret_store_arn, expected_type=type_hints["aws_secret_store_arn"])
                check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "aws_secret_store_arn": aws_secret_store_arn,
                "db_cluster_identifier": db_cluster_identifier,
            }
            if database_name is not None:
                self._values["database_name"] = database_name
            if schema is not None:
                self._values["schema"] = schema

        @builtins.property
        def aws_region(self) -> builtins.str:
            '''AWS Region for RDS HTTP endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_secret_store_arn(self) -> builtins.str:
            '''The ARN for database credentials stored in AWS Secrets Manager .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awssecretstorearn
            '''
            result = self._values.get("aws_secret_store_arn")
            assert result is not None, "Required property 'aws_secret_store_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def db_cluster_identifier(self) -> builtins.str:
            '''Amazon RDS cluster Amazon Resource Name (ARN).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-dbclusteridentifier
            '''
            result = self._values.get("db_cluster_identifier")
            assert result is not None, "Required property 'db_cluster_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''Logical database name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema(self) -> typing.Optional[builtins.str]:
            '''Logical schema name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-schema
            '''
            result = self._values.get("schema")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RdsHttpEndpointConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.RelationalDatabaseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "relational_database_source_type": "relationalDatabaseSourceType",
            "rds_http_endpoint_config": "rdsHttpEndpointConfig",
        },
    )
    class RelationalDatabaseConfigProperty:
        def __init__(
            self,
            *,
            relational_database_source_type: builtins.str,
            rds_http_endpoint_config: typing.Optional[typing.Union[typing.Union["CfnDataSource.RdsHttpEndpointConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Use the ``RelationalDatabaseConfig`` property type to specify ``RelationalDatabaseConfig`` for an AWS AppSync data source.

            ``RelationalDatabaseConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            :param relational_database_source_type: The type of relational data source.
            :param rds_http_endpoint_config: Information about the Amazon RDS resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                relational_database_config_property = appsync.CfnDataSource.RelationalDatabaseConfigProperty(
                    relational_database_source_type="relationalDatabaseSourceType",
                
                    # the properties below are optional
                    rds_http_endpoint_config=appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                        aws_region="awsRegion",
                        aws_secret_store_arn="awsSecretStoreArn",
                        db_cluster_identifier="dbClusterIdentifier",
                
                        # the properties below are optional
                        database_name="databaseName",
                        schema="schema"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4357a1467126648487c710ab6683bf4d3954927d7c54c51b699c6f185a943236)
                check_type(argname="argument relational_database_source_type", value=relational_database_source_type, expected_type=type_hints["relational_database_source_type"])
                check_type(argname="argument rds_http_endpoint_config", value=rds_http_endpoint_config, expected_type=type_hints["rds_http_endpoint_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "relational_database_source_type": relational_database_source_type,
            }
            if rds_http_endpoint_config is not None:
                self._values["rds_http_endpoint_config"] = rds_http_endpoint_config

        @builtins.property
        def relational_database_source_type(self) -> builtins.str:
            '''The type of relational data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-relationaldatabasesourcetype
            '''
            result = self._values.get("relational_database_source_type")
            assert result is not None, "Required property 'relational_database_source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rds_http_endpoint_config(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.RdsHttpEndpointConfigProperty", _IResolvable_da3f097b]]:
            '''Information about the Amazon RDS resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-rdshttpendpointconfig
            '''
            result = self._values.get("rds_http_endpoint_config")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.RdsHttpEndpointConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalDatabaseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "name": "name",
        "type": "type",
        "description": "description",
        "dynamo_db_config": "dynamoDbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "lambda_config": "lambdaConfig",
        "open_search_service_config": "openSearchServiceConfig",
        "relational_database_config": "relationalDatabaseConfig",
        "service_role_arn": "serviceRoleArn",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamo_db_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        elasticsearch_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        http_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        lambda_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        open_search_service_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        relational_database_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataSource``.

        :param api_id: Unique AWS AppSync GraphQL API identifier where this data source will be created.
        :param name: Friendly name for you to identify your AppSync data source after creation.
        :param type: The type of the data source. - *AWS_LAMBDA* : The data source is an AWS Lambda function. - *AMAZON_DYNAMODB* : The data source is an Amazon DynamoDB table. - *AMAZON_ELASTICSEARCH* : The data source is an Amazon OpenSearch Service domain. - *AMAZON_OPENSEARCH_SERVICE* : The data source is an Amazon OpenSearch Service domain. - *NONE* : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation. - *HTTP* : The data source is an HTTP endpoint. - *RELATIONAL_DATABASE* : The data source is a relational database.
        :param description: The description of the data source.
        :param dynamo_db_config: AWS Region and TableName for an Amazon DynamoDB table in your account.
        :param elasticsearch_config: AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account. As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.
        :param http_config: Endpoints for an HTTP data source.
        :param lambda_config: An ARN of a Lambda function in valid ARN format. This can be the ARN of a Lambda function that exists in the current account or in another account.
        :param open_search_service_config: AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.
        :param relational_database_config: Relational Database configuration of the relational database data source.
        :param service_role_arn: The AWS Identity and Access Management service role ARN for the data source. The system assumes this role when accessing the data source. Required if ``Type`` is specified as ``AWS_LAMBDA`` , ``AMAZON_DYNAMODB`` , ``AMAZON_ELASTICSEARCH`` , or ``AMAZON_OPENSEARCH_SERVICE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_data_source_props = appsync.CfnDataSourceProps(
                api_id="apiId",
                name="name",
                type="type",
            
                # the properties below are optional
                description="description",
                dynamo_db_config=appsync.CfnDataSource.DynamoDBConfigProperty(
                    aws_region="awsRegion",
                    table_name="tableName",
            
                    # the properties below are optional
                    delta_sync_config=appsync.CfnDataSource.DeltaSyncConfigProperty(
                        base_table_ttl="baseTableTtl",
                        delta_sync_table_name="deltaSyncTableName",
                        delta_sync_table_ttl="deltaSyncTableTtl"
                    ),
                    use_caller_credentials=False,
                    versioned=False
                ),
                elasticsearch_config=appsync.CfnDataSource.ElasticsearchConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                ),
                http_config=appsync.CfnDataSource.HttpConfigProperty(
                    endpoint="endpoint",
            
                    # the properties below are optional
                    authorization_config=appsync.CfnDataSource.AuthorizationConfigProperty(
                        authorization_type="authorizationType",
            
                        # the properties below are optional
                        aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                            signing_region="signingRegion",
                            signing_service_name="signingServiceName"
                        )
                    )
                ),
                lambda_config=appsync.CfnDataSource.LambdaConfigProperty(
                    lambda_function_arn="lambdaFunctionArn"
                ),
                open_search_service_config=appsync.CfnDataSource.OpenSearchServiceConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                ),
                relational_database_config=appsync.CfnDataSource.RelationalDatabaseConfigProperty(
                    relational_database_source_type="relationalDatabaseSourceType",
            
                    # the properties below are optional
                    rds_http_endpoint_config=appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                        aws_region="awsRegion",
                        aws_secret_store_arn="awsSecretStoreArn",
                        db_cluster_identifier="dbClusterIdentifier",
            
                        # the properties below are optional
                        database_name="databaseName",
                        schema="schema"
                    )
                ),
                service_role_arn="serviceRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a27321db4878d92375c672ad2fd1de24e61150d04b9a9b7f544b60bf81d6d7)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamo_db_config", value=dynamo_db_config, expected_type=type_hints["dynamo_db_config"])
            check_type(argname="argument elasticsearch_config", value=elasticsearch_config, expected_type=type_hints["elasticsearch_config"])
            check_type(argname="argument http_config", value=http_config, expected_type=type_hints["http_config"])
            check_type(argname="argument lambda_config", value=lambda_config, expected_type=type_hints["lambda_config"])
            check_type(argname="argument open_search_service_config", value=open_search_service_config, expected_type=type_hints["open_search_service_config"])
            check_type(argname="argument relational_database_config", value=relational_database_config, expected_type=type_hints["relational_database_config"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if dynamo_db_config is not None:
            self._values["dynamo_db_config"] = dynamo_db_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if open_search_service_config is not None:
            self._values["open_search_service_config"] = open_search_service_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn

    @builtins.property
    def api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API identifier where this data source will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Friendly name for you to identify your AppSync data source after creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the data source.

        - *AWS_LAMBDA* : The data source is an AWS Lambda function.
        - *AMAZON_DYNAMODB* : The data source is an Amazon DynamoDB table.
        - *AMAZON_ELASTICSEARCH* : The data source is an Amazon OpenSearch Service domain.
        - *AMAZON_OPENSEARCH_SERVICE* : The data source is an Amazon OpenSearch Service domain.
        - *NONE* : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
        - *HTTP* : The data source is an HTTP endpoint.
        - *RELATIONAL_DATABASE* : The data source is a relational database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.DynamoDBConfigProperty, _IResolvable_da3f097b]]:
        '''AWS Region and TableName for an Amazon DynamoDB table in your account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-dynamodbconfig
        '''
        result = self._values.get("dynamo_db_config")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.DynamoDBConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.ElasticsearchConfigProperty, _IResolvable_da3f097b]]:
        '''AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.

        As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-elasticsearchconfig
        '''
        result = self._values.get("elasticsearch_config")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.ElasticsearchConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.HttpConfigProperty, _IResolvable_da3f097b]]:
        '''Endpoints for an HTTP data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-httpconfig
        '''
        result = self._values.get("http_config")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.HttpConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.LambdaConfigProperty, _IResolvable_da3f097b]]:
        '''An ARN of a Lambda function in valid ARN format.

        This can be the ARN of a Lambda function that exists in the current account or in another account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-lambdaconfig
        '''
        result = self._values.get("lambda_config")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.LambdaConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def open_search_service_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, _IResolvable_da3f097b]]:
        '''AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-opensearchserviceconfig
        '''
        result = self._values.get("open_search_service_config")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, _IResolvable_da3f097b]]:
        '''Relational Database configuration of the relational database data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-relationaldatabaseconfig
        '''
        result = self._values.get("relational_database_config")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''The AWS Identity and Access Management service role ARN for the data source.

        The system assumes this role when accessing the data source.

        Required if ``Type`` is specified as ``AWS_LAMBDA`` , ``AMAZON_DYNAMODB`` , ``AMAZON_ELASTICSEARCH`` , or ``AMAZON_OPENSEARCH_SERVICE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDomainName(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnDomainName",
):
    '''A CloudFormation ``AWS::AppSync::DomainName``.

    The ``AWS::AppSync::DomainName`` resource creates a ``DomainNameConfig`` object to configure a custom domain.

    :cloudformationResource: AWS::AppSync::DomainName
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_domain_name = appsync.CfnDomainName(self, "MyCfnDomainName",
            certificate_arn="certificateArn",
            domain_name="domainName",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        certificate_arn: builtins.str,
        domain_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::AppSync::DomainName``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate. This will be an AWS Certificate Manager certificate.
        :param domain_name: The domain name.
        :param description: The decription for your domain name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678693553586e835af6ffdc6ac5860f81ffd96791de73368d44d41d3a220fa5b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainNameProps(
            certificate_arn=certificate_arn,
            domain_name=domain_name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1bb36f58b6037c649f6de5b27bf9555b52f554bb5fe4108f80d1e6143cb6f24)
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
            type_hints = typing.get_type_hints(_typecheckingstub__45a3cf8beadfc199c9c9d148139af66f311d5dbd310ca59a7062e7f26c40c037)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAppSyncDomainName")
    def attr_app_sync_domain_name(self) -> builtins.str:
        '''The domain name provided by AWS AppSync .

        :cloudformationAttribute: AppSyncDomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppSyncDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrHostedZoneId")
    def attr_hosted_zone_id(self) -> builtins.str:
        '''The ID of your Amazon Route 53 hosted zone.

        :cloudformationAttribute: HostedZoneId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate.

        This will be an AWS Certificate Manager certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-certificatearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21881e6a0cbde3bc434364c90ea094d149b2b6df42d7fc1beaa6dc2b7dfe9eca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d87464e3fb9b21e5511a8f5b32d36667e3c9d7faaf4d9cd05b6f5a75145649f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The decription for your domain name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc72a5388fe698c3e3240ed821a6e614471584c2ffb80f06028269bf9d78d46e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.implements(_IInspectable_c2943556)
class CfnDomainNameApiAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnDomainNameApiAssociation",
):
    '''A CloudFormation ``AWS::AppSync::DomainNameApiAssociation``.

    The ``AWS::AppSync::DomainNameApiAssociation`` resource represents the mapping of your custom domain name to the assigned API URL.

    :cloudformationResource: AWS::AppSync::DomainNameApiAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_domain_name_api_association = appsync.CfnDomainNameApiAssociation(self, "MyCfnDomainNameApiAssociation",
            api_id="apiId",
            domain_name="domainName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        domain_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::AppSync::DomainNameApiAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: The API ID.
        :param domain_name: The domain name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053707dba2452392a89bf081ac7d866beeff7c348bacbfe351a815a6372a43d5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainNameApiAssociationProps(
            api_id=api_id, domain_name=domain_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__942757d7ea72d07c8e5e78524b0a4e08dae920c7a26e14bfd77a565345201d36)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03652b1dc4a3294dad3ea732f92fa774dc0eda1cb1fe6263bac9fe9718f6e63b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiAssociationIdentifier")
    def attr_api_association_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApiAssociationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiAssociationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html#cfn-appsync-domainnameapiassociation-apiid
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1373752dfc88f0800245faefb7696b22aadcc994b58e7c2c57cd7f058ad814b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html#cfn-appsync-domainnameapiassociation-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dd7f18cf3cb236d2ffa804f6505477d416e7b844f92f9ba86f74aea18663216)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnDomainNameApiAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"api_id": "apiId", "domain_name": "domainName"},
)
class CfnDomainNameApiAssociationProps:
    def __init__(self, *, api_id: builtins.str, domain_name: builtins.str) -> None:
        '''Properties for defining a ``CfnDomainNameApiAssociation``.

        :param api_id: The API ID.
        :param domain_name: The domain name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_domain_name_api_association_props = appsync.CfnDomainNameApiAssociationProps(
                api_id="apiId",
                domain_name="domainName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a899ca55570211a5da411a83f28448dd1e54a82a4e83cb8d8ca2b1f292ebf5)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "domain_name": domain_name,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html#cfn-appsync-domainnameapiassociation-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html#cfn-appsync-domainnameapiassociation-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainNameApiAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnDomainNameProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_arn": "certificateArn",
        "domain_name": "domainName",
        "description": "description",
    },
)
class CfnDomainNameProps:
    def __init__(
        self,
        *,
        certificate_arn: builtins.str,
        domain_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomainName``.

        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate. This will be an AWS Certificate Manager certificate.
        :param domain_name: The domain name.
        :param description: The decription for your domain name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_domain_name_props = appsync.CfnDomainNameProps(
                certificate_arn="certificateArn",
                domain_name="domainName",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b0d09d8c1a97bdb5c0b0b95b798fbeb11f45abb25769bdb71d1903471361a5c)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
            "domain_name": domain_name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate.

        This will be an AWS Certificate Manager certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-certificatearn
        '''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The decription for your domain name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainNameProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFunctionConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfiguration",
):
    '''A CloudFormation ``AWS::AppSync::FunctionConfiguration``.

    The ``AWS::AppSync::FunctionConfiguration`` resource defines the functions in GraphQL APIs to perform certain operations. You can use pipeline resolvers to attach functions. For more information, see `Pipeline Resolvers <https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html>`_ in the *AWS AppSync Developer Guide* .
    .. epigraph::

       When you submit an update, AWS CloudFormation updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the AWS CloudFormation template. Changing the Amazon S3 file content without changing a property value will not result in an update operation.

       See `Update Behaviors of Stack Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html>`_ in the *AWS CloudFormation User Guide* .

    :cloudformationResource: AWS::AppSync::FunctionConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_function_configuration = appsync.CfnFunctionConfiguration(self, "MyCfnFunctionConfiguration",
            api_id="apiId",
            data_source_name="dataSourceName",
            name="name",
        
            # the properties below are optional
            code="code",
            code_s3_location="codeS3Location",
            description="description",
            function_version="functionVersion",
            max_batch_size=123,
            request_mapping_template="requestMappingTemplate",
            request_mapping_template_s3_location="requestMappingTemplateS3Location",
            response_mapping_template="responseMappingTemplate",
            response_mapping_template_s3_location="responseMappingTemplateS3Location",
            runtime=appsync.CfnFunctionConfiguration.AppSyncRuntimeProperty(
                name="name",
                runtime_version="runtimeVersion"
            ),
            sync_config=appsync.CfnFunctionConfiguration.SyncConfigProperty(
                conflict_detection="conflictDetection",
        
                # the properties below are optional
                conflict_handler="conflictHandler",
                lambda_conflict_handler_config=appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty(
                    lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        data_source_name: builtins.str,
        name: builtins.str,
        code: typing.Optional[builtins.str] = None,
        code_s3_location: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        function_version: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union[typing.Union["CfnFunctionConfiguration.AppSyncRuntimeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        sync_config: typing.Optional[typing.Union[typing.Union["CfnFunctionConfiguration.SyncConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::AppSync::FunctionConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: The AWS AppSync GraphQL API that you want to attach using this function.
        :param data_source_name: The name of data source this function will attach.
        :param name: The name of the function.
        :param code: ``AWS::AppSync::FunctionConfiguration.Code``.
        :param code_s3_location: ``AWS::AppSync::FunctionConfiguration.CodeS3Location``.
        :param description: The ``Function`` description.
        :param function_version: The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.
        :param max_batch_size: The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.
        :param request_mapping_template: The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
        :param request_mapping_template_s3_location: Describes a Sync configuration for a resolver. Contains information on which Conflict Detection, as well as Resolution strategy, should be performed when the resolver is invoked.
        :param response_mapping_template: The ``Function`` response mapping template.
        :param response_mapping_template_s3_location: The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param runtime: ``AWS::AppSync::FunctionConfiguration.Runtime``.
        :param sync_config: Describes a Sync configuration for a resolver. Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a4866dafc094db4e3a18f26e71e3f210828f39f8958d47fe2d4c085adc6ff8f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFunctionConfigurationProps(
            api_id=api_id,
            data_source_name=data_source_name,
            name=name,
            code=code,
            code_s3_location=code_s3_location,
            description=description,
            function_version=function_version,
            max_batch_size=max_batch_size,
            request_mapping_template=request_mapping_template,
            request_mapping_template_s3_location=request_mapping_template_s3_location,
            response_mapping_template=response_mapping_template,
            response_mapping_template_s3_location=response_mapping_template_s3_location,
            runtime=runtime,
            sync_config=sync_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b5daa219cb13e40ed1b20203fde593fe20c2c92bd36d7a071b49bcec839439b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__36f15942d1b688b5a1072d376a057d8302c1e87743f5a5200ad9fc3b45987f7a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDataSourceName")
    def attr_data_source_name(self) -> builtins.str:
        '''The name of data source this function will attach.

        :cloudformationAttribute: DataSourceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataSourceName"))

    @builtins.property
    @jsii.member(jsii_name="attrFunctionArn")
    def attr_function_arn(self) -> builtins.str:
        '''ARN of the function, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/functions/functionId`` .

        :cloudformationAttribute: FunctionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFunctionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFunctionId")
    def attr_function_id(self) -> builtins.str:
        '''The unique ID of this function.

        :cloudformationAttribute: FunctionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFunctionId"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the function.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API that you want to attach using this function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-apiid
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddada6f46239ab33eec4921b4ac0cf9484ba0c89258d9ca8117a0ecf69c7631a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> builtins.str:
        '''The name of data source this function will attach.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataSourceName"))

    @data_source_name.setter
    def data_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9493c684f0dde1a9223d5146974c138d33dbf89e0c56ed8d6d23f69b357bcde1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bcf772bf0a6d98d280769ee4b3e0c374a4881be9dfcc56425285f343d8c9a87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppSync::FunctionConfiguration.Code``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-code
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "code"))

    @code.setter
    def code(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f176cd8f4e930d504d5f35fb87b141d2a2d197149a0763d630b94186516de330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="codeS3Location")
    def code_s3_location(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppSync::FunctionConfiguration.CodeS3Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-codes3location
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeS3Location"))

    @code_s3_location.setter
    def code_s3_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e20f51155c39c20c83124659b8133fc87948adf8035794534cadf37a3e7265e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e87fe0dd6ec9c662347f3659e76d0bd6308df654c93fd61f384e0c29e5eb24b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> typing.Optional[builtins.str]:
        '''The version of the request mapping template.

        Currently, only the 2018-05-29 version of the template is supported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-functionversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionVersion"))

    @function_version.setter
    def function_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b218cd4f3808007654247768d1242189a48a8632f1621b5b37ab5e4ccc0f4a9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionVersion", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchSize")
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-maxbatchsize
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchSize"))

    @max_batch_size.setter
    def max_batch_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9abf526bb6e39ee9360616d137b1625f90523f036a39b05e1cf79037baad4f63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchSize", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` request mapping template.

        Functions support only the 2018-05-29 version of the request mapping template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplate"))

    @request_mapping_template.setter
    def request_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96a54d609ccde1c57b832776c4db93d393395273ac718e900a8503eaeb43283e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''Describes a Sync configuration for a resolver.

        Contains information on which Conflict Detection, as well as Resolution strategy, should be performed when the resolver is invoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplates3location
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplateS3Location"))

    @request_mapping_template_s3_location.setter
    def request_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1031c7b0aa54c899315716446946b7d1e3385d7b3fb6f6d1d31ea4f653ad3cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` response mapping template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplate"))

    @response_mapping_template.setter
    def response_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45788eaccf27f4038c701605c623bce576d7990af5337245691eb20581091c26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a response mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplates3location
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplateS3Location"))

    @response_mapping_template_s3_location.setter
    def response_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b40fcc0e01043cbd9cdf55c416d462b00a65d35ca5fdef3bfa9d0b412afbb19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(
        self,
    ) -> typing.Optional[typing.Union["CfnFunctionConfiguration.AppSyncRuntimeProperty", _IResolvable_da3f097b]]:
        '''``AWS::AppSync::FunctionConfiguration.Runtime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-runtime
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFunctionConfiguration.AppSyncRuntimeProperty", _IResolvable_da3f097b]], jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(
        self,
        value: typing.Optional[typing.Union["CfnFunctionConfiguration.AppSyncRuntimeProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__143abf7cef16b0a5749a28fb00575ff2cb3a1f027e142a59f5e914c1776d09fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union["CfnFunctionConfiguration.SyncConfigProperty", _IResolvable_da3f097b]]:
        '''Describes a Sync configuration for a resolver.

        Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-syncconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFunctionConfiguration.SyncConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "syncConfig"))

    @sync_config.setter
    def sync_config(
        self,
        value: typing.Optional[typing.Union["CfnFunctionConfiguration.SyncConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d1624e61da41b1be885253dc0b667a61deba82d80481d4d6a6b5430b507b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfiguration.AppSyncRuntimeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "runtime_version": "runtimeVersion"},
    )
    class AppSyncRuntimeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            runtime_version: builtins.str,
        ) -> None:
            '''
            :param name: ``CfnFunctionConfiguration.AppSyncRuntimeProperty.Name``.
            :param runtime_version: ``CfnFunctionConfiguration.AppSyncRuntimeProperty.RuntimeVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                app_sync_runtime_property = appsync.CfnFunctionConfiguration.AppSyncRuntimeProperty(
                    name="name",
                    runtime_version="runtimeVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b82405295f439f31600277f9055bf514ac45e79afd73f5b14450b84beac6e5c)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "runtime_version": runtime_version,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnFunctionConfiguration.AppSyncRuntimeProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html#cfn-appsync-functionconfiguration-appsyncruntime-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def runtime_version(self) -> builtins.str:
            '''``CfnFunctionConfiguration.AppSyncRuntimeProperty.RuntimeVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html#cfn-appsync-functionconfiguration-appsyncruntime-runtimeversion
            '''
            result = self._values.get("runtime_version")
            assert result is not None, "Required property 'runtime_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppSyncRuntimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
    )
    class LambdaConflictHandlerConfigProperty:
        def __init__(
            self,
            *,
            lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LambdaConflictHandlerConfig`` object when configuring ``LAMBDA`` as the Conflict Handler.

            :param lambda_conflict_handler_arn: The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                lambda_conflict_handler_config_property = appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty(
                    lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e67576fdd79515010563035ffc15df29a57e00be079931631598d07f7178f0c3)
                check_type(argname="argument lambda_conflict_handler_arn", value=lambda_conflict_handler_arn, expected_type=type_hints["lambda_conflict_handler_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_conflict_handler_arn is not None:
                self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

        @builtins.property
        def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html#cfn-appsync-functionconfiguration-lambdaconflicthandlerconfig-lambdaconflicthandlerarn
            '''
            result = self._values.get("lambda_conflict_handler_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConflictHandlerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfiguration.SyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conflict_detection": "conflictDetection",
            "conflict_handler": "conflictHandler",
            "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
        },
    )
    class SyncConfigProperty:
        def __init__(
            self,
            *,
            conflict_detection: builtins.str,
            conflict_handler: typing.Optional[builtins.str] = None,
            lambda_conflict_handler_config: typing.Optional[typing.Union[typing.Union["CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes a Sync configuration for a resolver.

            Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

            :param conflict_detection: The Conflict Detection strategy to use. - *VERSION* : Detect conflicts based on object versions for this resolver. - *NONE* : Do not detect conflicts when invoking this resolver.
            :param conflict_handler: The Conflict Resolution strategy to perform in the event of a conflict. - *OPTIMISTIC_CONCURRENCY* : Resolve conflicts by rejecting mutations when versions don't match the latest version at the server. - *AUTOMERGE* : Resolve conflicts with the Automerge conflict resolution strategy. - *LAMBDA* : Resolve conflicts with an AWS Lambda function supplied in the ``LambdaConflictHandlerConfig`` .
            :param lambda_conflict_handler_config: The ``LambdaConflictHandlerConfig`` when configuring ``LAMBDA`` as the Conflict Handler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                sync_config_property = appsync.CfnFunctionConfiguration.SyncConfigProperty(
                    conflict_detection="conflictDetection",
                
                    # the properties below are optional
                    conflict_handler="conflictHandler",
                    lambda_conflict_handler_config=appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty(
                        lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__441bd762beaec70fd67cf86d84e674beae78bf0e9f78d94f1b683b403e7b47f1)
                check_type(argname="argument conflict_detection", value=conflict_detection, expected_type=type_hints["conflict_detection"])
                check_type(argname="argument conflict_handler", value=conflict_handler, expected_type=type_hints["conflict_handler"])
                check_type(argname="argument lambda_conflict_handler_config", value=lambda_conflict_handler_config, expected_type=type_hints["lambda_conflict_handler_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "conflict_detection": conflict_detection,
            }
            if conflict_handler is not None:
                self._values["conflict_handler"] = conflict_handler
            if lambda_conflict_handler_config is not None:
                self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

        @builtins.property
        def conflict_detection(self) -> builtins.str:
            '''The Conflict Detection strategy to use.

            - *VERSION* : Detect conflicts based on object versions for this resolver.
            - *NONE* : Do not detect conflicts when invoking this resolver.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-conflictdetection
            '''
            result = self._values.get("conflict_detection")
            assert result is not None, "Required property 'conflict_detection' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def conflict_handler(self) -> typing.Optional[builtins.str]:
            '''The Conflict Resolution strategy to perform in the event of a conflict.

            - *OPTIMISTIC_CONCURRENCY* : Resolve conflicts by rejecting mutations when versions don't match the latest version at the server.
            - *AUTOMERGE* : Resolve conflicts with the Automerge conflict resolution strategy.
            - *LAMBDA* : Resolve conflicts with an AWS Lambda function supplied in the ``LambdaConflictHandlerConfig`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-conflicthandler
            '''
            result = self._values.get("conflict_handler")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lambda_conflict_handler_config(
            self,
        ) -> typing.Optional[typing.Union["CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty", _IResolvable_da3f097b]]:
            '''The ``LambdaConflictHandlerConfig`` when configuring ``LAMBDA`` as the Conflict Handler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-lambdaconflicthandlerconfig
            '''
            result = self._values.get("lambda_conflict_handler_config")
            return typing.cast(typing.Optional[typing.Union["CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "data_source_name": "dataSourceName",
        "name": "name",
        "code": "code",
        "code_s3_location": "codeS3Location",
        "description": "description",
        "function_version": "functionVersion",
        "max_batch_size": "maxBatchSize",
        "request_mapping_template": "requestMappingTemplate",
        "request_mapping_template_s3_location": "requestMappingTemplateS3Location",
        "response_mapping_template": "responseMappingTemplate",
        "response_mapping_template_s3_location": "responseMappingTemplateS3Location",
        "runtime": "runtime",
        "sync_config": "syncConfig",
    },
)
class CfnFunctionConfigurationProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        data_source_name: builtins.str,
        name: builtins.str,
        code: typing.Optional[builtins.str] = None,
        code_s3_location: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        function_version: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union[typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        sync_config: typing.Optional[typing.Union[typing.Union[CfnFunctionConfiguration.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFunctionConfiguration``.

        :param api_id: The AWS AppSync GraphQL API that you want to attach using this function.
        :param data_source_name: The name of data source this function will attach.
        :param name: The name of the function.
        :param code: ``AWS::AppSync::FunctionConfiguration.Code``.
        :param code_s3_location: ``AWS::AppSync::FunctionConfiguration.CodeS3Location``.
        :param description: The ``Function`` description.
        :param function_version: The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.
        :param max_batch_size: The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.
        :param request_mapping_template: The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
        :param request_mapping_template_s3_location: Describes a Sync configuration for a resolver. Contains information on which Conflict Detection, as well as Resolution strategy, should be performed when the resolver is invoked.
        :param response_mapping_template: The ``Function`` response mapping template.
        :param response_mapping_template_s3_location: The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param runtime: ``AWS::AppSync::FunctionConfiguration.Runtime``.
        :param sync_config: Describes a Sync configuration for a resolver. Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_function_configuration_props = appsync.CfnFunctionConfigurationProps(
                api_id="apiId",
                data_source_name="dataSourceName",
                name="name",
            
                # the properties below are optional
                code="code",
                code_s3_location="codeS3Location",
                description="description",
                function_version="functionVersion",
                max_batch_size=123,
                request_mapping_template="requestMappingTemplate",
                request_mapping_template_s3_location="requestMappingTemplateS3Location",
                response_mapping_template="responseMappingTemplate",
                response_mapping_template_s3_location="responseMappingTemplateS3Location",
                runtime=appsync.CfnFunctionConfiguration.AppSyncRuntimeProperty(
                    name="name",
                    runtime_version="runtimeVersion"
                ),
                sync_config=appsync.CfnFunctionConfiguration.SyncConfigProperty(
                    conflict_detection="conflictDetection",
            
                    # the properties below are optional
                    conflict_handler="conflictHandler",
                    lambda_conflict_handler_config=appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty(
                        lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68fb3836c61478b4bf652995d052fa027e6b2f6b9606529969b49a74037c3061)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument data_source_name", value=data_source_name, expected_type=type_hints["data_source_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument code_s3_location", value=code_s3_location, expected_type=type_hints["code_s3_location"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument function_version", value=function_version, expected_type=type_hints["function_version"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument request_mapping_template_s3_location", value=request_mapping_template_s3_location, expected_type=type_hints["request_mapping_template_s3_location"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument response_mapping_template_s3_location", value=response_mapping_template_s3_location, expected_type=type_hints["response_mapping_template_s3_location"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument sync_config", value=sync_config, expected_type=type_hints["sync_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "data_source_name": data_source_name,
            "name": name,
        }
        if code is not None:
            self._values["code"] = code
        if code_s3_location is not None:
            self._values["code_s3_location"] = code_s3_location
        if description is not None:
            self._values["description"] = description
        if function_version is not None:
            self._values["function_version"] = function_version
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if request_mapping_template_s3_location is not None:
            self._values["request_mapping_template_s3_location"] = request_mapping_template_s3_location
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if response_mapping_template_s3_location is not None:
            self._values["response_mapping_template_s3_location"] = response_mapping_template_s3_location
        if runtime is not None:
            self._values["runtime"] = runtime
        if sync_config is not None:
            self._values["sync_config"] = sync_config

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API that you want to attach using this function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_name(self) -> builtins.str:
        '''The name of data source this function will attach.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename
        '''
        result = self._values.get("data_source_name")
        assert result is not None, "Required property 'data_source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppSync::FunctionConfiguration.Code``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-code
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_s3_location(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppSync::FunctionConfiguration.CodeS3Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-codes3location
        '''
        result = self._values.get("code_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_version(self) -> typing.Optional[builtins.str]:
        '''The version of the request mapping template.

        Currently, only the 2018-05-29 version of the template is supported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-functionversion
        '''
        result = self._values.get("function_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-maxbatchsize
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` request mapping template.

        Functions support only the 2018-05-29 version of the request mapping template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplate
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''Describes a Sync configuration for a resolver.

        Contains information on which Conflict Detection, as well as Resolution strategy, should be performed when the resolver is invoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplates3location
        '''
        result = self._values.get("request_mapping_template_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` response mapping template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplate
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a response mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplates3location
        '''
        result = self._values.get("response_mapping_template_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(
        self,
    ) -> typing.Optional[typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, _IResolvable_da3f097b]]:
        '''``AWS::AppSync::FunctionConfiguration.Runtime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-runtime
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union[CfnFunctionConfiguration.SyncConfigProperty, _IResolvable_da3f097b]]:
        '''Describes a Sync configuration for a resolver.

        Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-syncconfig
        '''
        result = self._values.get("sync_config")
        return typing.cast(typing.Optional[typing.Union[CfnFunctionConfiguration.SyncConfigProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGraphQLApi(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi",
):
    '''A CloudFormation ``AWS::AppSync::GraphQLApi``.

    The ``AWS::AppSync::GraphQLApi`` resource creates a new AWS AppSync GraphQL API. This is the top-level construct for your application. For more information, see `Quick Start <https://docs.aws.amazon.com/appsync/latest/devguide/quickstart.html>`_ in the *AWS AppSync Developer Guide* .

    :cloudformationResource: AWS::AppSync::GraphQLApi
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_graph_qLApi = appsync.CfnGraphQLApi(self, "MyCfnGraphQLApi",
            authentication_type="authenticationType",
            name="name",
        
            # the properties below are optional
            additional_authentication_providers=[appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty(
                authentication_type="authenticationType",
        
                # the properties below are optional
                lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                    authorizer_result_ttl_in_seconds=123,
                    authorizer_uri="authorizerUri",
                    identity_validation_expression="identityValidationExpression"
                ),
                open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                    auth_ttl=123,
                    client_id="clientId",
                    iat_ttl=123,
                    issuer="issuer"
                ),
                user_pool_config=appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty(
                    app_id_client_regex="appIdClientRegex",
                    aws_region="awsRegion",
                    user_pool_id="userPoolId"
                )
            )],
            lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                authorizer_result_ttl_in_seconds=123,
                authorizer_uri="authorizerUri",
                identity_validation_expression="identityValidationExpression"
            ),
            log_config=appsync.CfnGraphQLApi.LogConfigProperty(
                cloud_watch_logs_role_arn="cloudWatchLogsRoleArn",
                exclude_verbose_content=False,
                field_log_level="fieldLogLevel"
            ),
            open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                auth_ttl=123,
                client_id="clientId",
                iat_ttl=123,
                issuer="issuer"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_pool_config=appsync.CfnGraphQLApi.UserPoolConfigProperty(
                app_id_client_regex="appIdClientRegex",
                aws_region="awsRegion",
                default_action="defaultAction",
                user_pool_id="userPoolId"
            ),
            xray_enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnGraphQLApi.AdditionalAuthenticationProviderProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        lambda_authorizer_config: typing.Optional[typing.Union[typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        log_config: typing.Optional[typing.Union[typing.Union["CfnGraphQLApi.LogConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        open_id_connect_config: typing.Optional[typing.Union[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_pool_config: typing.Optional[typing.Union[typing.Union["CfnGraphQLApi.UserPoolConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::AppSync::GraphQLApi``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authentication_type: Security configuration for your GraphQL API. For allowed values (such as ``API_KEY`` , ``AWS_IAM`` , ``AMAZON_COGNITO_USER_POOLS`` , ``OPENID_CONNECT`` , or ``AWS_LAMBDA`` ), see `Security <https://docs.aws.amazon.com/appsync/latest/devguide/security.html>`_ in the *AWS AppSync Developer Guide* .
        :param name: The API name.
        :param additional_authentication_providers: A list of additional authentication providers for the ``GraphqlApi`` API.
        :param lambda_authorizer_config: A ``LambdaAuthorizerConfig`` holds configuration on how to authorize AWS AppSync API access when using the ``AWS_LAMBDA`` authorizer mode. Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.
        :param log_config: The Amazon CloudWatch Logs configuration.
        :param open_id_connect_config: The OpenID Connect configuration.
        :param tags: An arbitrary set of tags (key-value pairs) for this GraphQL API.
        :param user_pool_config: Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.
        :param xray_enabled: A flag indicating whether to use AWS X-Ray tracing for this ``GraphqlApi`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54e0e0488820e5a410f75b28895d4271db1e58bd6c71e17fd04fcf3fad8696a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphQLApiProps(
            authentication_type=authentication_type,
            name=name,
            additional_authentication_providers=additional_authentication_providers,
            lambda_authorizer_config=lambda_authorizer_config,
            log_config=log_config,
            open_id_connect_config=open_id_connect_config,
            tags=tags,
            user_pool_config=user_pool_config,
            xray_enabled=xray_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef4f44613a72787cd83e4ceef509edefaabdb020300442c1eeb53ff3e20f525)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea2cc823b2c4f8c7f428fa2f0fe71c624a069d90ef8d4385d598404adbc586eb)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiId")
    def attr_api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API identifier.

        :cloudformationAttribute: ApiId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the API key, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGraphQlUrl")
    def attr_graph_ql_url(self) -> builtins.str:
        '''The Endpoint URL of your GraphQL API.

        :cloudformationAttribute: GraphQLUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGraphQlUrl"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An arbitrary set of tags (key-value pairs) for this GraphQL API.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        '''Security configuration for your GraphQL API.

        For allowed values (such as ``API_KEY`` , ``AWS_IAM`` , ``AMAZON_COGNITO_USER_POOLS`` , ``OPENID_CONNECT`` , or ``AWS_LAMBDA`` ), see `Security <https://docs.aws.amazon.com/appsync/latest/devguide/security.html>`_ in the *AWS AppSync Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype
        '''
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddf538537f9f940e10be3bb6aba02fdfaf8dc4a1cd2d9271f52eb0cc89a879de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The API name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6a61daae035f26bd4c76cf79a3d576be1077bd308cfbd0ecde402238ce095e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticationProviders")
    def additional_authentication_providers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnGraphQLApi.AdditionalAuthenticationProviderProperty", _IResolvable_da3f097b]]]]:
        '''A list of additional authentication providers for the ``GraphqlApi`` API.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-additionalauthenticationproviders
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnGraphQLApi.AdditionalAuthenticationProviderProperty", _IResolvable_da3f097b]]]], jsii.get(self, "additionalAuthenticationProviders"))

    @additional_authentication_providers.setter
    def additional_authentication_providers(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnGraphQLApi.AdditionalAuthenticationProviderProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d98241da3432e0393c78db49e66414c7e91e9bfc9e19f06380f6b18215ab489)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalAuthenticationProviders", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> typing.Optional[typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", _IResolvable_da3f097b]]:
        '''A ``LambdaAuthorizerConfig`` holds configuration on how to authorize AWS AppSync API access when using the ``AWS_LAMBDA`` authorizer mode.

        Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "lambdaAuthorizerConfig"))

    @lambda_authorizer_config.setter
    def lambda_authorizer_config(
        self,
        value: typing.Optional[typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ceade9d24f423834d3485476af5c7e3bd2e0ea0899583af5ac44f01e70b244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaAuthorizerConfig", value)

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(
        self,
    ) -> typing.Optional[typing.Union["CfnGraphQLApi.LogConfigProperty", _IResolvable_da3f097b]]:
        '''The Amazon CloudWatch Logs configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnGraphQLApi.LogConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "logConfig"))

    @log_config.setter
    def log_config(
        self,
        value: typing.Optional[typing.Union["CfnGraphQLApi.LogConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c0d15f646c5975aec4d344a5e6150a6fec6655df6d4354b817aef3ce9053464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logConfig", value)

    @builtins.property
    @jsii.member(jsii_name="openIdConnectConfig")
    def open_id_connect_config(
        self,
    ) -> typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_da3f097b]]:
        '''The OpenID Connect configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "openIdConnectConfig"))

    @open_id_connect_config.setter
    def open_id_connect_config(
        self,
        value: typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf051032d1109f154a4b02f8368044e2e1266c9008da417ccef7aa84293cc125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openIdConnectConfig", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> typing.Optional[typing.Union["CfnGraphQLApi.UserPoolConfigProperty", _IResolvable_da3f097b]]:
        '''Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnGraphQLApi.UserPoolConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "userPoolConfig"))

    @user_pool_config.setter
    def user_pool_config(
        self,
        value: typing.Optional[typing.Union["CfnGraphQLApi.UserPoolConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1d04f36c4d7d5f26bce761153a8d93212a34634f3833d3080b56cdd7a05e70b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolConfig", value)

    @builtins.property
    @jsii.member(jsii_name="xrayEnabled")
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag indicating whether to use AWS X-Ray tracing for this ``GraphqlApi`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "xrayEnabled"))

    @xray_enabled.setter
    def xray_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__863eb629614a817210cd5e0eb8ae7d3264658e2121ad2529a6090b38cd038199)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xrayEnabled", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_type": "authenticationType",
            "lambda_authorizer_config": "lambdaAuthorizerConfig",
            "open_id_connect_config": "openIdConnectConfig",
            "user_pool_config": "userPoolConfig",
        },
    )
    class AdditionalAuthenticationProviderProperty:
        def __init__(
            self,
            *,
            authentication_type: builtins.str,
            lambda_authorizer_config: typing.Optional[typing.Union[typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            open_id_connect_config: typing.Optional[typing.Union[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            user_pool_config: typing.Optional[typing.Union[typing.Union["CfnGraphQLApi.CognitoUserPoolConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes an additional authentication provider.

            :param authentication_type: The authentication type for API key, AWS Identity and Access Management , OIDC, Amazon Cognito user pools , or AWS Lambda . Valid Values: ``API_KEY`` | ``AWS_IAM`` | ``OPENID_CONNECT`` | ``AMAZON_COGNITO_USER_POOLS`` | ``AWS_LAMBDA``
            :param lambda_authorizer_config: Configuration for AWS Lambda function authorization.
            :param open_id_connect_config: The OIDC configuration.
            :param user_pool_config: The Amazon Cognito user pool configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                additional_authentication_provider_property = appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty(
                    authentication_type="authenticationType",
                
                    # the properties below are optional
                    lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                        authorizer_result_ttl_in_seconds=123,
                        authorizer_uri="authorizerUri",
                        identity_validation_expression="identityValidationExpression"
                    ),
                    open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                        auth_ttl=123,
                        client_id="clientId",
                        iat_ttl=123,
                        issuer="issuer"
                    ),
                    user_pool_config=appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty(
                        app_id_client_regex="appIdClientRegex",
                        aws_region="awsRegion",
                        user_pool_id="userPoolId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f8233eaa1ce5aeb807b7fe9374215f842f67afc12ed29dcbdf6773df7cd328a4)
                check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
                check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
                check_type(argname="argument open_id_connect_config", value=open_id_connect_config, expected_type=type_hints["open_id_connect_config"])
                check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authentication_type": authentication_type,
            }
            if lambda_authorizer_config is not None:
                self._values["lambda_authorizer_config"] = lambda_authorizer_config
            if open_id_connect_config is not None:
                self._values["open_id_connect_config"] = open_id_connect_config
            if user_pool_config is not None:
                self._values["user_pool_config"] = user_pool_config

        @builtins.property
        def authentication_type(self) -> builtins.str:
            '''The authentication type for API key, AWS Identity and Access Management , OIDC, Amazon Cognito user pools , or AWS Lambda .

            Valid Values: ``API_KEY`` | ``AWS_IAM`` | ``OPENID_CONNECT`` | ``AMAZON_COGNITO_USER_POOLS`` | ``AWS_LAMBDA``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype
            '''
            result = self._values.get("authentication_type")
            assert result is not None, "Required property 'authentication_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def lambda_authorizer_config(
            self,
        ) -> typing.Optional[typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", _IResolvable_da3f097b]]:
            '''Configuration for AWS Lambda function authorization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-lambdaauthorizerconfig
            '''
            result = self._values.get("lambda_authorizer_config")
            return typing.cast(typing.Optional[typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def open_id_connect_config(
            self,
        ) -> typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_da3f097b]]:
            '''The OIDC configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-openidconnectconfig
            '''
            result = self._values.get("open_id_connect_config")
            return typing.cast(typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def user_pool_config(
            self,
        ) -> typing.Optional[typing.Union["CfnGraphQLApi.CognitoUserPoolConfigProperty", _IResolvable_da3f097b]]:
            '''The Amazon Cognito user pool configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-userpoolconfig
            '''
            result = self._values.get("user_pool_config")
            return typing.cast(typing.Optional[typing.Union["CfnGraphQLApi.CognitoUserPoolConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdditionalAuthenticationProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_id_client_regex": "appIdClientRegex",
            "aws_region": "awsRegion",
            "user_pool_id": "userPoolId",
        },
    )
    class CognitoUserPoolConfigProperty:
        def __init__(
            self,
            *,
            app_id_client_regex: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
            user_pool_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an Amazon Cognito user pool configuration.

            :param app_id_client_regex: A regular expression for validating the incoming Amazon Cognito user pool app client ID.
            :param aws_region: The AWS Region in which the user pool was created.
            :param user_pool_id: The user pool ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                cognito_user_pool_config_property = appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty(
                    app_id_client_regex="appIdClientRegex",
                    aws_region="awsRegion",
                    user_pool_id="userPoolId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05b5c78d0d6cf8f2e5de126a1b379f17cb44634afea4439cb4b2b3c893dee502)
                check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_id_client_regex is not None:
                self._values["app_id_client_regex"] = app_id_client_regex
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def app_id_client_regex(self) -> typing.Optional[builtins.str]:
            '''A regular expression for validating the incoming Amazon Cognito user pool app client ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-appidclientregex
            '''
            result = self._values.get("app_id_client_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region in which the user pool was created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_pool_id(self) -> typing.Optional[builtins.str]:
            '''The user pool ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-userpoolid
            '''
            result = self._values.get("user_pool_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoUserPoolConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
            "authorizer_uri": "authorizerUri",
            "identity_validation_expression": "identityValidationExpression",
        },
    )
    class LambdaAuthorizerConfigProperty:
        def __init__(
            self,
            *,
            authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
            authorizer_uri: typing.Optional[builtins.str] = None,
            identity_validation_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for AWS Lambda function authorization.

            :param authorizer_result_ttl_in_seconds: The number of seconds a response should be cached for. The default is 5 minutes (300 seconds). The Lambda function can override this by returning a ``ttlOverride`` key in its response. A value of 0 disables caching of responses.
            :param authorizer_uri: The ARN of the Lambda function to be called for authorization. This may be a standard Lambda ARN, a version ARN ( ``.../v3`` ) or alias ARN. *Note* : This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To do so with the AWS CLI , run the following: ``aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction``
            :param identity_validation_expression: A regular expression for validation of tokens before the Lambda function is called.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                lambda_authorizer_config_property = appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                    authorizer_result_ttl_in_seconds=123,
                    authorizer_uri="authorizerUri",
                    identity_validation_expression="identityValidationExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f9291a235c0bd7ecea6f37d1aa830ec180ae9518e0555f8a98722d8088b1895)
                check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
                check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
                check_type(argname="argument identity_validation_expression", value=identity_validation_expression, expected_type=type_hints["identity_validation_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorizer_result_ttl_in_seconds is not None:
                self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
            if authorizer_uri is not None:
                self._values["authorizer_uri"] = authorizer_uri
            if identity_validation_expression is not None:
                self._values["identity_validation_expression"] = identity_validation_expression

        @builtins.property
        def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds a response should be cached for.

            The default is 5 minutes (300 seconds). The Lambda function can override this by returning a ``ttlOverride`` key in its response. A value of 0 disables caching of responses.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-authorizerresultttlinseconds
            '''
            result = self._values.get("authorizer_result_ttl_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def authorizer_uri(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Lambda function to be called for authorization.

            This may be a standard Lambda ARN, a version ARN ( ``.../v3`` ) or alias ARN.

            *Note* : This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To do so with the AWS CLI , run the following:

            ``aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-authorizeruri
            '''
            result = self._values.get("authorizer_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def identity_validation_expression(self) -> typing.Optional[builtins.str]:
            '''A regular expression for validation of tokens before the Lambda function is called.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-identityvalidationexpression
            '''
            result = self._values.get("identity_validation_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaAuthorizerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.LogConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_role_arn": "cloudWatchLogsRoleArn",
            "exclude_verbose_content": "excludeVerboseContent",
            "field_log_level": "fieldLogLevel",
        },
    )
    class LogConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
            exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            field_log_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LogConfig`` property type specifies the logging configuration when writing GraphQL operations and tracing to Amazon CloudWatch for an AWS AppSync GraphQL API.

            ``LogConfig`` is a property of the `AWS::AppSync::GraphQLApi <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html>`_ property type.

            :param cloud_watch_logs_role_arn: The service role that AWS AppSync will assume to publish to Amazon CloudWatch Logs in your account.
            :param exclude_verbose_content: Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.
            :param field_log_level: The field logging level. Values can be NONE, ERROR, or ALL. - *NONE* : No field-level logs are captured. - *ERROR* : Logs the following information only for the fields that are in error: - The error section in the server response. - Field-level errors. - The generated request/response functions that got resolved for error fields. - *ALL* : The following information is logged for all fields in the query: - Field-level tracing information. - The generated request/response functions that got resolved for each field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                log_config_property = appsync.CfnGraphQLApi.LogConfigProperty(
                    cloud_watch_logs_role_arn="cloudWatchLogsRoleArn",
                    exclude_verbose_content=False,
                    field_log_level="fieldLogLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9ff7e1cb756f4b27770bf07bfb18b0936eea6dc27410d5c20b3b259d960d7a3)
                check_type(argname="argument cloud_watch_logs_role_arn", value=cloud_watch_logs_role_arn, expected_type=type_hints["cloud_watch_logs_role_arn"])
                check_type(argname="argument exclude_verbose_content", value=exclude_verbose_content, expected_type=type_hints["exclude_verbose_content"])
                check_type(argname="argument field_log_level", value=field_log_level, expected_type=type_hints["field_log_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs_role_arn is not None:
                self._values["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
            if exclude_verbose_content is not None:
                self._values["exclude_verbose_content"] = exclude_verbose_content
            if field_log_level is not None:
                self._values["field_log_level"] = field_log_level

        @builtins.property
        def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
            '''The service role that AWS AppSync will assume to publish to Amazon CloudWatch Logs in your account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-cloudwatchlogsrolearn
            '''
            result = self._values.get("cloud_watch_logs_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclude_verbose_content(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-excludeverbosecontent
            '''
            result = self._values.get("exclude_verbose_content")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def field_log_level(self) -> typing.Optional[builtins.str]:
            '''The field logging level. Values can be NONE, ERROR, or ALL.

            - *NONE* : No field-level logs are captured.
            - *ERROR* : Logs the following information only for the fields that are in error:
            - The error section in the server response.
            - Field-level errors.
            - The generated request/response functions that got resolved for error fields.
            - *ALL* : The following information is logged for all fields in the query:
            - Field-level tracing information.
            - The generated request/response functions that got resolved for each field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-fieldloglevel
            '''
            result = self._values.get("field_log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.OpenIDConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_ttl": "authTtl",
            "client_id": "clientId",
            "iat_ttl": "iatTtl",
            "issuer": "issuer",
        },
    )
    class OpenIDConnectConfigProperty:
        def __init__(
            self,
            *,
            auth_ttl: typing.Optional[jsii.Number] = None,
            client_id: typing.Optional[builtins.str] = None,
            iat_ttl: typing.Optional[jsii.Number] = None,
            issuer: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``OpenIDConnectConfig`` property type specifies the optional authorization configuration for using an OpenID Connect compliant service with your GraphQL endpoint for an AWS AppSync GraphQL API.

            ``OpenIDConnectConfig`` is a property of the `AWS::AppSync::GraphQLApi <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html>`_ property type.

            :param auth_ttl: The number of milliseconds that a token is valid after being authenticated.
            :param client_id: The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.
            :param iat_ttl: The number of milliseconds that a token is valid after it's issued to a user.
            :param issuer: The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                open_iDConnect_config_property = appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                    auth_ttl=123,
                    client_id="clientId",
                    iat_ttl=123,
                    issuer="issuer"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07e62ce520030272762ccf6169ce5673be0610bd412fd2d9b9a3a7c7963d4853)
                check_type(argname="argument auth_ttl", value=auth_ttl, expected_type=type_hints["auth_ttl"])
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument iat_ttl", value=iat_ttl, expected_type=type_hints["iat_ttl"])
                check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auth_ttl is not None:
                self._values["auth_ttl"] = auth_ttl
            if client_id is not None:
                self._values["client_id"] = client_id
            if iat_ttl is not None:
                self._values["iat_ttl"] = iat_ttl
            if issuer is not None:
                self._values["issuer"] = issuer

        @builtins.property
        def auth_ttl(self) -> typing.Optional[jsii.Number]:
            '''The number of milliseconds that a token is valid after being authenticated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-authttl
            '''
            result = self._values.get("auth_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def client_id(self) -> typing.Optional[builtins.str]:
            '''The client identifier of the Relying party at the OpenID identity provider.

            This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-clientid
            '''
            result = self._values.get("client_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iat_ttl(self) -> typing.Optional[jsii.Number]:
            '''The number of milliseconds that a token is valid after it's issued to a user.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-iatttl
            '''
            result = self._values.get("iat_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def issuer(self) -> typing.Optional[builtins.str]:
            '''The issuer for the OIDC configuration.

            The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-issuer
            '''
            result = self._values.get("issuer")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenIDConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.UserPoolConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_id_client_regex": "appIdClientRegex",
            "aws_region": "awsRegion",
            "default_action": "defaultAction",
            "user_pool_id": "userPoolId",
        },
    )
    class UserPoolConfigProperty:
        def __init__(
            self,
            *,
            app_id_client_regex: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
            default_action: typing.Optional[builtins.str] = None,
            user_pool_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``UserPoolConfig`` property type specifies the optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint for an AWS AppSync GraphQL API.

            :param app_id_client_regex: A regular expression for validating the incoming Amazon Cognito user pool app client ID.
            :param aws_region: The AWS Region in which the user pool was created.
            :param default_action: The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration. When specifying Amazon Cognito user pools as the default authentication, you must set the value for ``DefaultAction`` to ``ALLOW`` if specifying ``AdditionalAuthenticationProviders`` .
            :param user_pool_id: The user pool ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                user_pool_config_property = appsync.CfnGraphQLApi.UserPoolConfigProperty(
                    app_id_client_regex="appIdClientRegex",
                    aws_region="awsRegion",
                    default_action="defaultAction",
                    user_pool_id="userPoolId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f0d0849f2d6ffc2b4b6a4eabed8e631f4ae22772572c4eae3d63c7ec6f2a4a4)
                check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
                check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_id_client_regex is not None:
                self._values["app_id_client_regex"] = app_id_client_regex
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if default_action is not None:
                self._values["default_action"] = default_action
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def app_id_client_regex(self) -> typing.Optional[builtins.str]:
            '''A regular expression for validating the incoming Amazon Cognito user pool app client ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-appidclientregex
            '''
            result = self._values.get("app_id_client_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region in which the user pool was created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_action(self) -> typing.Optional[builtins.str]:
            '''The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.

            When specifying Amazon Cognito user pools as the default authentication, you must set the value for ``DefaultAction`` to ``ALLOW`` if specifying ``AdditionalAuthenticationProviders`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-defaultaction
            '''
            result = self._values.get("default_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_pool_id(self) -> typing.Optional[builtins.str]:
            '''The user pool ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-userpoolid
            '''
            result = self._values.get("user_pool_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPoolConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "name": "name",
        "additional_authentication_providers": "additionalAuthenticationProviders",
        "lambda_authorizer_config": "lambdaAuthorizerConfig",
        "log_config": "logConfig",
        "open_id_connect_config": "openIdConnectConfig",
        "tags": "tags",
        "user_pool_config": "userPoolConfig",
        "xray_enabled": "xrayEnabled",
    },
)
class CfnGraphQLApiProps:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        lambda_authorizer_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        log_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.LogConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        open_id_connect_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_pool_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.UserPoolConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraphQLApi``.

        :param authentication_type: Security configuration for your GraphQL API. For allowed values (such as ``API_KEY`` , ``AWS_IAM`` , ``AMAZON_COGNITO_USER_POOLS`` , ``OPENID_CONNECT`` , or ``AWS_LAMBDA`` ), see `Security <https://docs.aws.amazon.com/appsync/latest/devguide/security.html>`_ in the *AWS AppSync Developer Guide* .
        :param name: The API name.
        :param additional_authentication_providers: A list of additional authentication providers for the ``GraphqlApi`` API.
        :param lambda_authorizer_config: A ``LambdaAuthorizerConfig`` holds configuration on how to authorize AWS AppSync API access when using the ``AWS_LAMBDA`` authorizer mode. Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.
        :param log_config: The Amazon CloudWatch Logs configuration.
        :param open_id_connect_config: The OpenID Connect configuration.
        :param tags: An arbitrary set of tags (key-value pairs) for this GraphQL API.
        :param user_pool_config: Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.
        :param xray_enabled: A flag indicating whether to use AWS X-Ray tracing for this ``GraphqlApi`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_graph_qLApi_props = appsync.CfnGraphQLApiProps(
                authentication_type="authenticationType",
                name="name",
            
                # the properties below are optional
                additional_authentication_providers=[appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty(
                    authentication_type="authenticationType",
            
                    # the properties below are optional
                    lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                        authorizer_result_ttl_in_seconds=123,
                        authorizer_uri="authorizerUri",
                        identity_validation_expression="identityValidationExpression"
                    ),
                    open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                        auth_ttl=123,
                        client_id="clientId",
                        iat_ttl=123,
                        issuer="issuer"
                    ),
                    user_pool_config=appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty(
                        app_id_client_regex="appIdClientRegex",
                        aws_region="awsRegion",
                        user_pool_id="userPoolId"
                    )
                )],
                lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                    authorizer_result_ttl_in_seconds=123,
                    authorizer_uri="authorizerUri",
                    identity_validation_expression="identityValidationExpression"
                ),
                log_config=appsync.CfnGraphQLApi.LogConfigProperty(
                    cloud_watch_logs_role_arn="cloudWatchLogsRoleArn",
                    exclude_verbose_content=False,
                    field_log_level="fieldLogLevel"
                ),
                open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                    auth_ttl=123,
                    client_id="clientId",
                    iat_ttl=123,
                    issuer="issuer"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_pool_config=appsync.CfnGraphQLApi.UserPoolConfigProperty(
                    app_id_client_regex="appIdClientRegex",
                    aws_region="awsRegion",
                    default_action="defaultAction",
                    user_pool_id="userPoolId"
                ),
                xray_enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c30fb6e2b0bf2994b166c6091173ca1bbdf2a226ff26da5bfc0c35067fc8cc07)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_authentication_providers", value=additional_authentication_providers, expected_type=type_hints["additional_authentication_providers"])
            check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument open_id_connect_config", value=open_id_connect_config, expected_type=type_hints["open_id_connect_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
            check_type(argname="argument xray_enabled", value=xray_enabled, expected_type=type_hints["xray_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
            "name": name,
        }
        if additional_authentication_providers is not None:
            self._values["additional_authentication_providers"] = additional_authentication_providers
        if lambda_authorizer_config is not None:
            self._values["lambda_authorizer_config"] = lambda_authorizer_config
        if log_config is not None:
            self._values["log_config"] = log_config
        if open_id_connect_config is not None:
            self._values["open_id_connect_config"] = open_id_connect_config
        if tags is not None:
            self._values["tags"] = tags
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''Security configuration for your GraphQL API.

        For allowed values (such as ``API_KEY`` , ``AWS_IAM`` , ``AMAZON_COGNITO_USER_POOLS`` , ``OPENID_CONNECT`` , or ``AWS_LAMBDA`` ), see `Security <https://docs.aws.amazon.com/appsync/latest/devguide/security.html>`_ in the *AWS AppSync Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype
        '''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The API name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_authentication_providers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, _IResolvable_da3f097b]]]]:
        '''A list of additional authentication providers for the ``GraphqlApi`` API.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-additionalauthenticationproviders
        '''
        result = self._values.get("additional_authentication_providers")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def lambda_authorizer_config(
        self,
    ) -> typing.Optional[typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, _IResolvable_da3f097b]]:
        '''A ``LambdaAuthorizerConfig`` holds configuration on how to authorize AWS AppSync API access when using the ``AWS_LAMBDA`` authorizer mode.

        Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig
        '''
        result = self._values.get("lambda_authorizer_config")
        return typing.cast(typing.Optional[typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def log_config(
        self,
    ) -> typing.Optional[typing.Union[CfnGraphQLApi.LogConfigProperty, _IResolvable_da3f097b]]:
        '''The Amazon CloudWatch Logs configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional[typing.Union[CfnGraphQLApi.LogConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def open_id_connect_config(
        self,
    ) -> typing.Optional[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, _IResolvable_da3f097b]]:
        '''The OpenID Connect configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig
        '''
        result = self._values.get("open_id_connect_config")
        return typing.cast(typing.Optional[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key-value pairs) for this GraphQL API.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_pool_config(
        self,
    ) -> typing.Optional[typing.Union[CfnGraphQLApi.UserPoolConfigProperty, _IResolvable_da3f097b]]:
        '''Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig
        '''
        result = self._values.get("user_pool_config")
        return typing.cast(typing.Optional[typing.Union[CfnGraphQLApi.UserPoolConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag indicating whether to use AWS X-Ray tracing for this ``GraphqlApi`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled
        '''
        result = self._values.get("xray_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphQLApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGraphQLSchema(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLSchema",
):
    '''A CloudFormation ``AWS::AppSync::GraphQLSchema``.

    The ``AWS::AppSync::GraphQLSchema`` resource is used for your AWS AppSync GraphQL schema that controls the data model for your API. Schema files are text written in Schema Definition Language (SDL) format. For more information about schema authoring, see `Designing a GraphQL API <https://docs.aws.amazon.com/appsync/latest/devguide/designing-a-graphql-api.html>`_ in the *AWS AppSync Developer Guide* .
    .. epigraph::

       When you submit an update, AWS CloudFormation updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the CloudFormation template. Changing the Amazon S3 file content without changing a property value will not result in an update operation.

       See `Update Behaviors of Stack Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html>`_ in the *AWS CloudFormation User Guide* .

    :cloudformationResource: AWS::AppSync::GraphQLSchema
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_graph_qLSchema = appsync.CfnGraphQLSchema(self, "MyCfnGraphQLSchema",
            api_id="apiId",
        
            # the properties below are optional
            definition="definition",
            definition_s3_location="definitionS3Location"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        definition: typing.Optional[builtins.str] = None,
        definition_s3_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::AppSync::GraphQLSchema``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: The AWS AppSync GraphQL API identifier to which you want to apply this schema.
        :param definition: The text representation of a GraphQL schema in SDL format. For more information about using the ``Ref`` function, see `Ref <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref>`_ .
        :param definition_s3_location: The location of a GraphQL schema file in an Amazon S3 bucket. Use this if you want to provision with the schema living in Amazon S3 rather than embedding it in your CloudFormation template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86eeb90bbb1ca5a453f08cfb90f5fb16cf4842431fc90d63f3ee21972f1be243)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphQLSchemaProps(
            api_id=api_id,
            definition=definition,
            definition_s3_location=definition_s3_location,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6052290b218f085df44320d030dc5da2a656bc2dfb652a6e8997c198d7360074)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5e7b1316522ac1b9a93d87179eb23379f7762341da46fd001056a8704a20b2c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API identifier to which you want to apply this schema.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-apiid
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__555a23d4ba449beaaf98ed745a155165b6830286b0aeae2a45d326885e8eddef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Optional[builtins.str]:
        '''The text representation of a GraphQL schema in SDL format.

        For more information about using the ``Ref`` function, see `Ref <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "definition"))

    @definition.setter
    def definition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29a3a5e0c95af4007408f43ded6d8b16b50975200325f9066820c3302d03398)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="definitionS3Location")
    def definition_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a GraphQL schema file in an Amazon S3 bucket.

        Use this if you want to provision with the schema living in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "definitionS3Location"))

    @definition_s3_location.setter
    def definition_s3_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4848140e56b16e4736cedb1aa2fb1ca3fd82aeca7e977c876274b365740b08de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionS3Location", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLSchemaProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "definition": "definition",
        "definition_s3_location": "definitionS3Location",
    },
)
class CfnGraphQLSchemaProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        definition: typing.Optional[builtins.str] = None,
        definition_s3_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraphQLSchema``.

        :param api_id: The AWS AppSync GraphQL API identifier to which you want to apply this schema.
        :param definition: The text representation of a GraphQL schema in SDL format. For more information about using the ``Ref`` function, see `Ref <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref>`_ .
        :param definition_s3_location: The location of a GraphQL schema file in an Amazon S3 bucket. Use this if you want to provision with the schema living in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_graph_qLSchema_props = appsync.CfnGraphQLSchemaProps(
                api_id="apiId",
            
                # the properties below are optional
                definition="definition",
                definition_s3_location="definitionS3Location"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20c7b2f1eadba8a608fdb8a0a590a3907eb9c891f22a7385f17ef74294ca1d0c)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument definition_s3_location", value=definition_s3_location, expected_type=type_hints["definition_s3_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
        }
        if definition is not None:
            self._values["definition"] = definition
        if definition_s3_location is not None:
            self._values["definition_s3_location"] = definition_s3_location

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API identifier to which you want to apply this schema.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def definition(self) -> typing.Optional[builtins.str]:
        '''The text representation of a GraphQL schema in SDL format.

        For more information about using the ``Ref`` function, see `Ref <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition
        '''
        result = self._values.get("definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def definition_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a GraphQL schema file in an Amazon S3 bucket.

        Use this if you want to provision with the schema living in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location
        '''
        result = self._values.get("definition_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphQLSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResolver(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnResolver",
):
    '''A CloudFormation ``AWS::AppSync::Resolver``.

    The ``AWS::AppSync::Resolver`` resource defines the logical GraphQL resolver that you attach to fields in a schema. Request and response templates for resolvers are written in Apache Velocity Template Language (VTL) format. For more information about resolvers, see `Resolver Mapping Template Reference <https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference.html>`_ .
    .. epigraph::

       When you submit an update, AWS CloudFormation updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the CloudFormation template. Changing the Amazon S3 file content without changing a property value will not result in an update operation.

       See `Update Behaviors of Stack Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html>`_ in the *AWS CloudFormation User Guide* .

    :cloudformationResource: AWS::AppSync::Resolver
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_resolver = appsync.CfnResolver(self, "MyCfnResolver",
            api_id="apiId",
            field_name="fieldName",
            type_name="typeName",
        
            # the properties below are optional
            caching_config=appsync.CfnResolver.CachingConfigProperty(
                ttl=123,
        
                # the properties below are optional
                caching_keys=["cachingKeys"]
            ),
            code="code",
            code_s3_location="codeS3Location",
            data_source_name="dataSourceName",
            kind="kind",
            max_batch_size=123,
            pipeline_config=appsync.CfnResolver.PipelineConfigProperty(
                functions=["functions"]
            ),
            request_mapping_template="requestMappingTemplate",
            request_mapping_template_s3_location="requestMappingTemplateS3Location",
            response_mapping_template="responseMappingTemplate",
            response_mapping_template_s3_location="responseMappingTemplateS3Location",
            runtime=appsync.CfnResolver.AppSyncRuntimeProperty(
                name="name",
                runtime_version="runtimeVersion"
            ),
            sync_config=appsync.CfnResolver.SyncConfigProperty(
                conflict_detection="conflictDetection",
        
                # the properties below are optional
                conflict_handler="conflictHandler",
                lambda_conflict_handler_config=appsync.CfnResolver.LambdaConflictHandlerConfigProperty(
                    lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[typing.Union["CfnResolver.CachingConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        code: typing.Optional[builtins.str] = None,
        code_s3_location: typing.Optional[builtins.str] = None,
        data_source_name: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Union[typing.Union["CfnResolver.PipelineConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union[typing.Union["CfnResolver.AppSyncRuntimeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        sync_config: typing.Optional[typing.Union[typing.Union["CfnResolver.SyncConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::AppSync::Resolver``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: The AWS AppSync GraphQL API to which you want to attach this resolver.
        :param field_name: The GraphQL field on a type that invokes the resolver.
        :param type_name: The GraphQL type that invokes this resolver.
        :param caching_config: The caching configuration for the resolver.
        :param code: ``AWS::AppSync::Resolver.Code``.
        :param code_s3_location: ``AWS::AppSync::Resolver.CodeS3Location``.
        :param data_source_name: The resolver data source name.
        :param kind: The resolver type. - *UNIT* : A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source. - *PIPELINE* : A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of ``Function`` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.
        :param max_batch_size: The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.
        :param pipeline_config: Functions linked with the pipeline resolver.
        :param request_mapping_template: The request mapping template. Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.
        :param request_mapping_template_s3_location: The location of a request mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param response_mapping_template: The response mapping template.
        :param response_mapping_template_s3_location: The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param runtime: ``AWS::AppSync::Resolver.Runtime``.
        :param sync_config: The ``SyncConfig`` for a resolver attached to a versioned data source.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45a19b37f9f570b32d81c1e70bfcb51be048fdffa3df94ad801e69b812f746f8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverProps(
            api_id=api_id,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            code=code,
            code_s3_location=code_s3_location,
            data_source_name=data_source_name,
            kind=kind,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            request_mapping_template_s3_location=request_mapping_template_s3_location,
            response_mapping_template=response_mapping_template,
            response_mapping_template_s3_location=response_mapping_template_s3_location,
            runtime=runtime,
            sync_config=sync_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95aca731304382cdf3dcd502764afa9c3fa4887077a0e30a6874db561995ccfa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__313f8d86637162de96ee41aad99883afe32469196f904fb4309e0e9e33fc98ba)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrFieldName")
    def attr_field_name(self) -> builtins.str:
        '''The GraphQL field on a type that invokes the resolver.

        :cloudformationAttribute: FieldName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFieldName"))

    @builtins.property
    @jsii.member(jsii_name="attrResolverArn")
    def attr_resolver_arn(self) -> builtins.str:
        '''ARN of the resolver, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/types/typename/resolvers/resolvername`` .

        :cloudformationAttribute: ResolverArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTypeName")
    def attr_type_name(self) -> builtins.str:
        '''The GraphQL type that invokes this resolver.

        :cloudformationAttribute: TypeName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API to which you want to attach this resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-apiid
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__472e69750f14de2abe38ed65522399a06e502ba89a0b921571c0b2746c638e5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="fieldName")
    def field_name(self) -> builtins.str:
        '''The GraphQL field on a type that invokes the resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-fieldname
        '''
        return typing.cast(builtins.str, jsii.get(self, "fieldName"))

    @field_name.setter
    def field_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2233218403900cf6b8a69c999e792511fca483ed05d2fa4306e0d7b2535010)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldName", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        '''The GraphQL type that invokes this resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-typename
        '''
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c08751b4795b139490b95abf3b3d0f17260bfea4a916f1afbaf08d435cfa21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="cachingConfig")
    def caching_config(
        self,
    ) -> typing.Optional[typing.Union["CfnResolver.CachingConfigProperty", _IResolvable_da3f097b]]:
        '''The caching configuration for the resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-cachingconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResolver.CachingConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "cachingConfig"))

    @caching_config.setter
    def caching_config(
        self,
        value: typing.Optional[typing.Union["CfnResolver.CachingConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6b9e8b849504be748695ce685546b844451460e25485772ca066bc2b65f61b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingConfig", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppSync::Resolver.Code``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-code
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "code"))

    @code.setter
    def code(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0dd83b21d0fde771732f3fdf63588b717c979c6ab095248970576c0a297e97d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="codeS3Location")
    def code_s3_location(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppSync::Resolver.CodeS3Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-codes3location
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeS3Location"))

    @code_s3_location.setter
    def code_s3_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd67bb7c14d4f8040b88b7d1c29031ed6038b21c10f80e4f0fcfd6c31af45cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> typing.Optional[builtins.str]:
        '''The resolver data source name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-datasourcename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceName"))

    @data_source_name.setter
    def data_source_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d90421590c8dc3a0c283260b096db2cd054cf3d6852e741d1bfaf1bf52bbe597)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> typing.Optional[builtins.str]:
        '''The resolver type.

        - *UNIT* : A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.
        - *PIPELINE* : A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of ``Function`` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-kind
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf560aa0e5a28a8ed71b1579e183bb6fb81cf53b398565d4fe06e8b7cfb4b31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchSize")
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-maxbatchsize
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchSize"))

    @max_batch_size.setter
    def max_batch_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66d0a40a93385979fce12d901f6a195637584cfcb71b3a04c20d8333f0a582bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchSize", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineConfig")
    def pipeline_config(
        self,
    ) -> typing.Optional[typing.Union["CfnResolver.PipelineConfigProperty", _IResolvable_da3f097b]]:
        '''Functions linked with the pipeline resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-pipelineconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResolver.PipelineConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "pipelineConfig"))

    @pipeline_config.setter
    def pipeline_config(
        self,
        value: typing.Optional[typing.Union["CfnResolver.PipelineConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c6c98074ee2ebbe5b451fe5513433aa3557366ed040722d6e61328ab781da16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineConfig", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The request mapping template.

        Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplate"))

    @request_mapping_template.setter
    def request_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd82effb0edb94da2492c911c5aecbe1fa5f2d88b6066513bb7f2a5713fdca7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a request mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplates3location
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplateS3Location"))

    @request_mapping_template_s3_location.setter
    def request_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd52da508686e9da63db3673bad91680eaa1eb468984c1b4f57757668dcaed40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The response mapping template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplate"))

    @response_mapping_template.setter
    def response_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f24f835e9a5b9af73089ccb61dfcf176cc230bb0feddf60b73360bab083e3f46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a response mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplates3location
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplateS3Location"))

    @response_mapping_template_s3_location.setter
    def response_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a067b0164755508220ca8ad5f24cbd5ac6d6c57fb44d8404b14392f12d372f0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(
        self,
    ) -> typing.Optional[typing.Union["CfnResolver.AppSyncRuntimeProperty", _IResolvable_da3f097b]]:
        '''``AWS::AppSync::Resolver.Runtime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-runtime
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResolver.AppSyncRuntimeProperty", _IResolvable_da3f097b]], jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(
        self,
        value: typing.Optional[typing.Union["CfnResolver.AppSyncRuntimeProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a14449468f6ed96319993479a0ae9b3feacd27ec17e068d4d17ce598a964715)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union["CfnResolver.SyncConfigProperty", _IResolvable_da3f097b]]:
        '''The ``SyncConfig`` for a resolver attached to a versioned data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-syncconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResolver.SyncConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "syncConfig"))

    @sync_config.setter
    def sync_config(
        self,
        value: typing.Optional[typing.Union["CfnResolver.SyncConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a111110922e122a02d7d649fe2daaa4c4d7cf1709e2078b92fe101fd93d8e4f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.AppSyncRuntimeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "runtime_version": "runtimeVersion"},
    )
    class AppSyncRuntimeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            runtime_version: builtins.str,
        ) -> None:
            '''
            :param name: ``CfnResolver.AppSyncRuntimeProperty.Name``.
            :param runtime_version: ``CfnResolver.AppSyncRuntimeProperty.RuntimeVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                app_sync_runtime_property = appsync.CfnResolver.AppSyncRuntimeProperty(
                    name="name",
                    runtime_version="runtimeVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d69cd55f1989ce956af7a1058706bfd4aaeba608d00146e50a90c1d3521cee0)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "runtime_version": runtime_version,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnResolver.AppSyncRuntimeProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html#cfn-appsync-resolver-appsyncruntime-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def runtime_version(self) -> builtins.str:
            '''``CfnResolver.AppSyncRuntimeProperty.RuntimeVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html#cfn-appsync-resolver-appsyncruntime-runtimeversion
            '''
            result = self._values.get("runtime_version")
            assert result is not None, "Required property 'runtime_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppSyncRuntimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.CachingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"ttl": "ttl", "caching_keys": "cachingKeys"},
    )
    class CachingConfigProperty:
        def __init__(
            self,
            *,
            ttl: jsii.Number,
            caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The caching configuration for a resolver that has caching activated.

            :param ttl: The TTL in seconds for a resolver that has caching activated. Valid values are 1–3,600 seconds.
            :param caching_keys: The caching keys for a resolver that has caching activated. Valid values are entries from the ``$context.arguments`` , ``$context.source`` , and ``$context.identity`` maps.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                caching_config_property = appsync.CfnResolver.CachingConfigProperty(
                    ttl=123,
                
                    # the properties below are optional
                    caching_keys=["cachingKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5089c8cac20eb98ddb2d855ec469e09dc0f7b1141ddaf4de8fd19eaaadac7891)
                check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
                check_type(argname="argument caching_keys", value=caching_keys, expected_type=type_hints["caching_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ttl": ttl,
            }
            if caching_keys is not None:
                self._values["caching_keys"] = caching_keys

        @builtins.property
        def ttl(self) -> jsii.Number:
            '''The TTL in seconds for a resolver that has caching activated.

            Valid values are 1–3,600 seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-ttl
            '''
            result = self._values.get("ttl")
            assert result is not None, "Required property 'ttl' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def caching_keys(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The caching keys for a resolver that has caching activated.

            Valid values are entries from the ``$context.arguments`` , ``$context.source`` , and ``$context.identity`` maps.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-cachingkeys
            '''
            result = self._values.get("caching_keys")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CachingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.LambdaConflictHandlerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
    )
    class LambdaConflictHandlerConfigProperty:
        def __init__(
            self,
            *,
            lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LambdaConflictHandlerConfig`` when configuring LAMBDA as the Conflict Handler.

            :param lambda_conflict_handler_arn: The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                lambda_conflict_handler_config_property = appsync.CfnResolver.LambdaConflictHandlerConfigProperty(
                    lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8760098edd4885448deb6a9ceb1ba3eb5367683995fadd12b5e5f3bf1e2fdd7e)
                check_type(argname="argument lambda_conflict_handler_arn", value=lambda_conflict_handler_arn, expected_type=type_hints["lambda_conflict_handler_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_conflict_handler_arn is not None:
                self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

        @builtins.property
        def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html#cfn-appsync-resolver-lambdaconflicthandlerconfig-lambdaconflicthandlerarn
            '''
            result = self._values.get("lambda_conflict_handler_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConflictHandlerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.PipelineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"functions": "functions"},
    )
    class PipelineConfigProperty:
        def __init__(
            self,
            *,
            functions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Use the ``PipelineConfig`` property type to specify ``PipelineConfig`` for an AWS AppSync resolver.

            ``PipelineConfig`` is a property of the `AWS::AppSync::Resolver <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html>`_ resource.

            :param functions: A list of ``Function`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                pipeline_config_property = appsync.CfnResolver.PipelineConfigProperty(
                    functions=["functions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2907a70554c3df66e94c41c4e36342a2860e214a5b7da358efbe204221066961)
                check_type(argname="argument functions", value=functions, expected_type=type_hints["functions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if functions is not None:
                self._values["functions"] = functions

        @builtins.property
        def functions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of ``Function`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html#cfn-appsync-resolver-pipelineconfig-functions
            '''
            result = self._values.get("functions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipelineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.SyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conflict_detection": "conflictDetection",
            "conflict_handler": "conflictHandler",
            "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
        },
    )
    class SyncConfigProperty:
        def __init__(
            self,
            *,
            conflict_detection: builtins.str,
            conflict_handler: typing.Optional[builtins.str] = None,
            lambda_conflict_handler_config: typing.Optional[typing.Union[typing.Union["CfnResolver.LambdaConflictHandlerConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes a Sync configuration for a resolver.

            Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

            :param conflict_detection: The Conflict Detection strategy to use. - *VERSION* : Detect conflicts based on object versions for this resolver. - *NONE* : Do not detect conflicts when invoking this resolver.
            :param conflict_handler: The Conflict Resolution strategy to perform in the event of a conflict. - *OPTIMISTIC_CONCURRENCY* : Resolve conflicts by rejecting mutations when versions don't match the latest version at the server. - *AUTOMERGE* : Resolve conflicts with the Automerge conflict resolution strategy. - *LAMBDA* : Resolve conflicts with an AWS Lambda function supplied in the ``LambdaConflictHandlerConfig`` .
            :param lambda_conflict_handler_config: The ``LambdaConflictHandlerConfig`` when configuring ``LAMBDA`` as the Conflict Handler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                sync_config_property = appsync.CfnResolver.SyncConfigProperty(
                    conflict_detection="conflictDetection",
                
                    # the properties below are optional
                    conflict_handler="conflictHandler",
                    lambda_conflict_handler_config=appsync.CfnResolver.LambdaConflictHandlerConfigProperty(
                        lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd8efb0c43d72e5061a7c9c3de6483787260ccff8a3dff5a5152ca959d6af6a3)
                check_type(argname="argument conflict_detection", value=conflict_detection, expected_type=type_hints["conflict_detection"])
                check_type(argname="argument conflict_handler", value=conflict_handler, expected_type=type_hints["conflict_handler"])
                check_type(argname="argument lambda_conflict_handler_config", value=lambda_conflict_handler_config, expected_type=type_hints["lambda_conflict_handler_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "conflict_detection": conflict_detection,
            }
            if conflict_handler is not None:
                self._values["conflict_handler"] = conflict_handler
            if lambda_conflict_handler_config is not None:
                self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

        @builtins.property
        def conflict_detection(self) -> builtins.str:
            '''The Conflict Detection strategy to use.

            - *VERSION* : Detect conflicts based on object versions for this resolver.
            - *NONE* : Do not detect conflicts when invoking this resolver.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflictdetection
            '''
            result = self._values.get("conflict_detection")
            assert result is not None, "Required property 'conflict_detection' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def conflict_handler(self) -> typing.Optional[builtins.str]:
            '''The Conflict Resolution strategy to perform in the event of a conflict.

            - *OPTIMISTIC_CONCURRENCY* : Resolve conflicts by rejecting mutations when versions don't match the latest version at the server.
            - *AUTOMERGE* : Resolve conflicts with the Automerge conflict resolution strategy.
            - *LAMBDA* : Resolve conflicts with an AWS Lambda function supplied in the ``LambdaConflictHandlerConfig`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflicthandler
            '''
            result = self._values.get("conflict_handler")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lambda_conflict_handler_config(
            self,
        ) -> typing.Optional[typing.Union["CfnResolver.LambdaConflictHandlerConfigProperty", _IResolvable_da3f097b]]:
            '''The ``LambdaConflictHandlerConfig`` when configuring ``LAMBDA`` as the Conflict Handler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-lambdaconflicthandlerconfig
            '''
            result = self._values.get("lambda_conflict_handler_config")
            return typing.cast(typing.Optional[typing.Union["CfnResolver.LambdaConflictHandlerConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "code": "code",
        "code_s3_location": "codeS3Location",
        "data_source_name": "dataSourceName",
        "kind": "kind",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "request_mapping_template_s3_location": "requestMappingTemplateS3Location",
        "response_mapping_template": "responseMappingTemplate",
        "response_mapping_template_s3_location": "responseMappingTemplateS3Location",
        "runtime": "runtime",
        "sync_config": "syncConfig",
    },
)
class CfnResolverProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[typing.Union[CfnResolver.CachingConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        code: typing.Optional[builtins.str] = None,
        code_s3_location: typing.Optional[builtins.str] = None,
        data_source_name: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Union[typing.Union[CfnResolver.PipelineConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union[typing.Union[CfnResolver.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        sync_config: typing.Optional[typing.Union[typing.Union[CfnResolver.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResolver``.

        :param api_id: The AWS AppSync GraphQL API to which you want to attach this resolver.
        :param field_name: The GraphQL field on a type that invokes the resolver.
        :param type_name: The GraphQL type that invokes this resolver.
        :param caching_config: The caching configuration for the resolver.
        :param code: ``AWS::AppSync::Resolver.Code``.
        :param code_s3_location: ``AWS::AppSync::Resolver.CodeS3Location``.
        :param data_source_name: The resolver data source name.
        :param kind: The resolver type. - *UNIT* : A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source. - *PIPELINE* : A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of ``Function`` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.
        :param max_batch_size: The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.
        :param pipeline_config: Functions linked with the pipeline resolver.
        :param request_mapping_template: The request mapping template. Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.
        :param request_mapping_template_s3_location: The location of a request mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param response_mapping_template: The response mapping template.
        :param response_mapping_template_s3_location: The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param runtime: ``AWS::AppSync::Resolver.Runtime``.
        :param sync_config: The ``SyncConfig`` for a resolver attached to a versioned data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_resolver_props = appsync.CfnResolverProps(
                api_id="apiId",
                field_name="fieldName",
                type_name="typeName",
            
                # the properties below are optional
                caching_config=appsync.CfnResolver.CachingConfigProperty(
                    ttl=123,
            
                    # the properties below are optional
                    caching_keys=["cachingKeys"]
                ),
                code="code",
                code_s3_location="codeS3Location",
                data_source_name="dataSourceName",
                kind="kind",
                max_batch_size=123,
                pipeline_config=appsync.CfnResolver.PipelineConfigProperty(
                    functions=["functions"]
                ),
                request_mapping_template="requestMappingTemplate",
                request_mapping_template_s3_location="requestMappingTemplateS3Location",
                response_mapping_template="responseMappingTemplate",
                response_mapping_template_s3_location="responseMappingTemplateS3Location",
                runtime=appsync.CfnResolver.AppSyncRuntimeProperty(
                    name="name",
                    runtime_version="runtimeVersion"
                ),
                sync_config=appsync.CfnResolver.SyncConfigProperty(
                    conflict_detection="conflictDetection",
            
                    # the properties below are optional
                    conflict_handler="conflictHandler",
                    lambda_conflict_handler_config=appsync.CfnResolver.LambdaConflictHandlerConfigProperty(
                        lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b1ba8346de8783ad38f1a2377fd50bdd7577d903f4b68402c7b5ab604f16e5)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument code_s3_location", value=code_s3_location, expected_type=type_hints["code_s3_location"])
            check_type(argname="argument data_source_name", value=data_source_name, expected_type=type_hints["data_source_name"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument request_mapping_template_s3_location", value=request_mapping_template_s3_location, expected_type=type_hints["request_mapping_template_s3_location"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument response_mapping_template_s3_location", value=response_mapping_template_s3_location, expected_type=type_hints["response_mapping_template_s3_location"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument sync_config", value=sync_config, expected_type=type_hints["sync_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "field_name": field_name,
            "type_name": type_name,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if code is not None:
            self._values["code"] = code
        if code_s3_location is not None:
            self._values["code_s3_location"] = code_s3_location
        if data_source_name is not None:
            self._values["data_source_name"] = data_source_name
        if kind is not None:
            self._values["kind"] = kind
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if request_mapping_template_s3_location is not None:
            self._values["request_mapping_template_s3_location"] = request_mapping_template_s3_location
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if response_mapping_template_s3_location is not None:
            self._values["response_mapping_template_s3_location"] = response_mapping_template_s3_location
        if runtime is not None:
            self._values["runtime"] = runtime
        if sync_config is not None:
            self._values["sync_config"] = sync_config

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API to which you want to attach this resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_name(self) -> builtins.str:
        '''The GraphQL field on a type that invokes the resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-fieldname
        '''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''The GraphQL type that invokes this resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-typename
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(
        self,
    ) -> typing.Optional[typing.Union[CfnResolver.CachingConfigProperty, _IResolvable_da3f097b]]:
        '''The caching configuration for the resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-cachingconfig
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional[typing.Union[CfnResolver.CachingConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppSync::Resolver.Code``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-code
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_s3_location(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppSync::Resolver.CodeS3Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-codes3location
        '''
        result = self._values.get("code_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_name(self) -> typing.Optional[builtins.str]:
        '''The resolver data source name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-datasourcename
        '''
        result = self._values.get("data_source_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The resolver type.

        - *UNIT* : A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.
        - *PIPELINE* : A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of ``Function`` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-maxbatchsize
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(
        self,
    ) -> typing.Optional[typing.Union[CfnResolver.PipelineConfigProperty, _IResolvable_da3f097b]]:
        '''Functions linked with the pipeline resolver.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-pipelineconfig
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional[typing.Union[CfnResolver.PipelineConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The request mapping template.

        Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplate
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a request mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplates3location
        '''
        result = self._values.get("request_mapping_template_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The response mapping template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplate
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a response mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplates3location
        '''
        result = self._values.get("response_mapping_template_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(
        self,
    ) -> typing.Optional[typing.Union[CfnResolver.AppSyncRuntimeProperty, _IResolvable_da3f097b]]:
        '''``AWS::AppSync::Resolver.Runtime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-runtime
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[typing.Union[CfnResolver.AppSyncRuntimeProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union[CfnResolver.SyncConfigProperty, _IResolvable_da3f097b]]:
        '''The ``SyncConfig`` for a resolver attached to a versioned data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-syncconfig
        '''
        result = self._values.get("sync_config")
        return typing.cast(typing.Optional[typing.Union[CfnResolver.SyncConfigProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApiCache",
    "CfnApiCacheProps",
    "CfnApiKey",
    "CfnApiKeyProps",
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnDomainName",
    "CfnDomainNameApiAssociation",
    "CfnDomainNameApiAssociationProps",
    "CfnDomainNameProps",
    "CfnFunctionConfiguration",
    "CfnFunctionConfigurationProps",
    "CfnGraphQLApi",
    "CfnGraphQLApiProps",
    "CfnGraphQLSchema",
    "CfnGraphQLSchemaProps",
    "CfnResolver",
    "CfnResolverProps",
]

publication.publish()

def _typecheckingstub__e9d92b7b2abdac7341eb92f7ac10d2d67dd2700af68eaf42c72c47ffdaacc344(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_caching_behavior: builtins.str,
    api_id: builtins.str,
    ttl: jsii.Number,
    type: builtins.str,
    at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142193172b7ee1304f3b8fd949531b4cfa950ea62d0dc10f9ed5a184a603132d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce863b5f21a86ce886458054cd4de0550269c18eb7c4f3fb37884dc2869845e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee6b3576fbf654864dae4f55fe292d210bf01534f16f80af0ac225f8fa338c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2fdac623dbaddb2a0226d75e6f3ca84c058f3f46b9c9a1289820c1cf0827e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1893b7ba08236941b8e5bb4704e7fe53f8819086085796443b5d68f513e66eaa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45dc491e21920c6cd0ddecd9aada80283ac759d9eaca52c45a6ce35197166e9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a4abe242f634763c1f128b7e17017d1176924c9b032d5536f4caa3b3fc3bd6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb39499095e917401c885f7c77781744d09df071b1ed62c6f2c32cbbc6fbdb33(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f054fa3186eb5f122c20e523bed485713c72511ee3ee94be25733ecad9a348c(
    *,
    api_caching_behavior: builtins.str,
    api_id: builtins.str,
    ttl: jsii.Number,
    type: builtins.str,
    at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6065dd18c9d420fd4fcd70aced8416006f044f82aecff54150165e832539a8e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    api_key_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    expires: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8f02bc91fc0b32c990b8d08a5d7a0ef78a88363920fa69d4196dcc7f2ecfb3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a844b496712966f29aae49f2f831e6a85c7acf03c2ce61c94162ccf13c5efd6d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1cce5f76a6037620e1cc2e57750c81cc5161ff526ce78123f0cd9f25c8e856(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5d6818eefb673237292bb9320e2134ad0c799f70d17a7cba2de3f4298ccf5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08afa042939638da41f04c7165f811f5081bd3c8943f787591f098aa4a3b8699(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b034facb88dea82241969fd1a22a5bbaccf03068403021106e073c92112ab45(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1688db2b7835c85b4e2cd69655b5d25321ff2aa2ea9e1b2a0612caff34184549(
    *,
    api_id: builtins.str,
    api_key_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    expires: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2dc8968068d09d9cb599cea5efad1a18016c4eca4fcc6c15e6169a0891e2678(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dynamo_db_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    elasticsearch_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    http_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    lambda_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    open_search_service_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    relational_database_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844d45e22564aca7d878e00ff3e6a39f30d70312a9d2fcf8bb2f587b070069f7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb33982b2405feec8337a5b841ef30f58e28ed8058a2e3d003d09ee8aac516a9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7863787830eb114a9c03188cb3a3bfd0b865645dac5dd0d3cf0b374c0a1af6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba82e0d60919163b242fed29c81421c4160f75a79249e58ce74b20f6b7d0f03d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aae6a5f086f2d2c36e8dff3cce5906d962da71d7148d7feec996abb025fb8f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29cebb36b12bc9cd3423d5991aeea26c635c2541d63fc9c3309a2177c24f1118(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffaca3e4a18d434a01277621d6792259ab70047809af34a6cb0bab3eb7886a2(
    value: typing.Optional[typing.Union[CfnDataSource.DynamoDBConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5323c0bb4d330a2f6b24616dd2b47847aa913d75611ddeae3cc451eda7ebb774(
    value: typing.Optional[typing.Union[CfnDataSource.ElasticsearchConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b1129f048e5b946eceb4eb9c372f68c9a28e32ebe6091b611c3b1b82e3e83d(
    value: typing.Optional[typing.Union[CfnDataSource.HttpConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ff8b510d0035620c1325857ec673c802695c9f3c8dd8fa109d1b44e652a641(
    value: typing.Optional[typing.Union[CfnDataSource.LambdaConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__876dd6f7515f1b03442f4aa7a0d78d1d6e5eef401db8d851e96b713bd30f989e(
    value: typing.Optional[typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72a1c504ec56f95938bf0b2a05d96acc7eb4b1190dc7285e9c33b6b194318386(
    value: typing.Optional[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8d23554bf1b07da4d8bb262596b409805d205b461615d34726f3323315abb2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b40b2b6b828a39a91cb37d699b9dccbe36d457b235d0c89f8d63a8c926a5443(
    *,
    authorization_type: builtins.str,
    aws_iam_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.AwsIamConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d3d6847bbd8b570bb51728b12402301a578fc159522a9bb797a8042b7c43dd(
    *,
    signing_region: typing.Optional[builtins.str] = None,
    signing_service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d8409bee2e379adfba84b9eedc28876ceca73a2b15ec9ad3045f33dc08a849c(
    *,
    base_table_ttl: builtins.str,
    delta_sync_table_name: builtins.str,
    delta_sync_table_ttl: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66016c117898c1cc0dc84bb648ce56335f475ea29f1590882ca3229c1e8ffe3f(
    *,
    aws_region: builtins.str,
    table_name: builtins.str,
    delta_sync_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.DeltaSyncConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    use_caller_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    versioned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7385ec04703540fe726bf7efc36f7ea05ba851b02e63ee657ec6cba21c5e805(
    *,
    aws_region: builtins.str,
    endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4a6ece9757475b2fd78d8a95bd18c7fd68758c889cf5d07cea125e31a32258(
    *,
    endpoint: builtins.str,
    authorization_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.AuthorizationConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ae7467c676f94be4511c7fb68e47ed5c3c90dde218c9a12592924c98f7837e(
    *,
    lambda_function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fecf5845831a0e0a203174a1662e533c942ecf67ea1e85e246e7a029865de49(
    *,
    aws_region: builtins.str,
    endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348849422fd4d08e7490da175f7a5ffa84cad62dcd8d49557a3436740b3dffd5(
    *,
    aws_region: builtins.str,
    aws_secret_store_arn: builtins.str,
    db_cluster_identifier: builtins.str,
    database_name: typing.Optional[builtins.str] = None,
    schema: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4357a1467126648487c710ab6683bf4d3954927d7c54c51b699c6f185a943236(
    *,
    relational_database_source_type: builtins.str,
    rds_http_endpoint_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.RdsHttpEndpointConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a27321db4878d92375c672ad2fd1de24e61150d04b9a9b7f544b60bf81d6d7(
    *,
    api_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dynamo_db_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    elasticsearch_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    http_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    lambda_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    open_search_service_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    relational_database_config: typing.Optional[typing.Union[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678693553586e835af6ffdc6ac5860f81ffd96791de73368d44d41d3a220fa5b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_arn: builtins.str,
    domain_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1bb36f58b6037c649f6de5b27bf9555b52f554bb5fe4108f80d1e6143cb6f24(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a3cf8beadfc199c9c9d148139af66f311d5dbd310ca59a7062e7f26c40c037(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21881e6a0cbde3bc434364c90ea094d149b2b6df42d7fc1beaa6dc2b7dfe9eca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d87464e3fb9b21e5511a8f5b32d36667e3c9d7faaf4d9cd05b6f5a75145649f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc72a5388fe698c3e3240ed821a6e614471584c2ffb80f06028269bf9d78d46e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053707dba2452392a89bf081ac7d866beeff7c348bacbfe351a815a6372a43d5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__942757d7ea72d07c8e5e78524b0a4e08dae920c7a26e14bfd77a565345201d36(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03652b1dc4a3294dad3ea732f92fa774dc0eda1cb1fe6263bac9fe9718f6e63b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1373752dfc88f0800245faefb7696b22aadcc994b58e7c2c57cd7f058ad814b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dd7f18cf3cb236d2ffa804f6505477d416e7b844f92f9ba86f74aea18663216(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a899ca55570211a5da411a83f28448dd1e54a82a4e83cb8d8ca2b1f292ebf5(
    *,
    api_id: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b0d09d8c1a97bdb5c0b0b95b798fbeb11f45abb25769bdb71d1903471361a5c(
    *,
    certificate_arn: builtins.str,
    domain_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a4866dafc094db4e3a18f26e71e3f210828f39f8958d47fe2d4c085adc6ff8f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    data_source_name: builtins.str,
    name: builtins.str,
    code: typing.Optional[builtins.str] = None,
    code_s3_location: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    function_version: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    sync_config: typing.Optional[typing.Union[typing.Union[CfnFunctionConfiguration.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b5daa219cb13e40ed1b20203fde593fe20c2c92bd36d7a071b49bcec839439b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f15942d1b688b5a1072d376a057d8302c1e87743f5a5200ad9fc3b45987f7a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddada6f46239ab33eec4921b4ac0cf9484ba0c89258d9ca8117a0ecf69c7631a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9493c684f0dde1a9223d5146974c138d33dbf89e0c56ed8d6d23f69b357bcde1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bcf772bf0a6d98d280769ee4b3e0c374a4881be9dfcc56425285f343d8c9a87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f176cd8f4e930d504d5f35fb87b141d2a2d197149a0763d630b94186516de330(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e20f51155c39c20c83124659b8133fc87948adf8035794534cadf37a3e7265e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e87fe0dd6ec9c662347f3659e76d0bd6308df654c93fd61f384e0c29e5eb24b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b218cd4f3808007654247768d1242189a48a8632f1621b5b37ab5e4ccc0f4a9c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9abf526bb6e39ee9360616d137b1625f90523f036a39b05e1cf79037baad4f63(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96a54d609ccde1c57b832776c4db93d393395273ac718e900a8503eaeb43283e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1031c7b0aa54c899315716446946b7d1e3385d7b3fb6f6d1d31ea4f653ad3cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45788eaccf27f4038c701605c623bce576d7990af5337245691eb20581091c26(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b40fcc0e01043cbd9cdf55c416d462b00a65d35ca5fdef3bfa9d0b412afbb19(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143abf7cef16b0a5749a28fb00575ff2cb3a1f027e142a59f5e914c1776d09fc(
    value: typing.Optional[typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d1624e61da41b1be885253dc0b667a61deba82d80481d4d6a6b5430b507b05(
    value: typing.Optional[typing.Union[CfnFunctionConfiguration.SyncConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b82405295f439f31600277f9055bf514ac45e79afd73f5b14450b84beac6e5c(
    *,
    name: builtins.str,
    runtime_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e67576fdd79515010563035ffc15df29a57e00be079931631598d07f7178f0c3(
    *,
    lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__441bd762beaec70fd67cf86d84e674beae78bf0e9f78d94f1b683b403e7b47f1(
    *,
    conflict_detection: builtins.str,
    conflict_handler: typing.Optional[builtins.str] = None,
    lambda_conflict_handler_config: typing.Optional[typing.Union[typing.Union[CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68fb3836c61478b4bf652995d052fa027e6b2f6b9606529969b49a74037c3061(
    *,
    api_id: builtins.str,
    data_source_name: builtins.str,
    name: builtins.str,
    code: typing.Optional[builtins.str] = None,
    code_s3_location: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    function_version: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    sync_config: typing.Optional[typing.Union[typing.Union[CfnFunctionConfiguration.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54e0e0488820e5a410f75b28895d4271db1e58bd6c71e17fd04fcf3fad8696a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authentication_type: builtins.str,
    name: builtins.str,
    additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    lambda_authorizer_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    log_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.LogConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    open_id_connect_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_pool_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.UserPoolConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef4f44613a72787cd83e4ceef509edefaabdb020300442c1eeb53ff3e20f525(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea2cc823b2c4f8c7f428fa2f0fe71c624a069d90ef8d4385d598404adbc586eb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf538537f9f940e10be3bb6aba02fdfaf8dc4a1cd2d9271f52eb0cc89a879de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6a61daae035f26bd4c76cf79a3d576be1077bd308cfbd0ecde402238ce095e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d98241da3432e0393c78db49e66414c7e91e9bfc9e19f06380f6b18215ab489(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ceade9d24f423834d3485476af5c7e3bd2e0ea0899583af5ac44f01e70b244(
    value: typing.Optional[typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c0d15f646c5975aec4d344a5e6150a6fec6655df6d4354b817aef3ce9053464(
    value: typing.Optional[typing.Union[CfnGraphQLApi.LogConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf051032d1109f154a4b02f8368044e2e1266c9008da417ccef7aa84293cc125(
    value: typing.Optional[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d04f36c4d7d5f26bce761153a8d93212a34634f3833d3080b56cdd7a05e70b(
    value: typing.Optional[typing.Union[CfnGraphQLApi.UserPoolConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__863eb629614a817210cd5e0eb8ae7d3264658e2121ad2529a6090b38cd038199(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8233eaa1ce5aeb807b7fe9374215f842f67afc12ed29dcbdf6773df7cd328a4(
    *,
    authentication_type: builtins.str,
    lambda_authorizer_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    open_id_connect_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    user_pool_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.CognitoUserPoolConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b5c78d0d6cf8f2e5de126a1b379f17cb44634afea4439cb4b2b3c893dee502(
    *,
    app_id_client_regex: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    user_pool_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f9291a235c0bd7ecea6f37d1aa830ec180ae9518e0555f8a98722d8088b1895(
    *,
    authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
    authorizer_uri: typing.Optional[builtins.str] = None,
    identity_validation_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9ff7e1cb756f4b27770bf07bfb18b0936eea6dc27410d5c20b3b259d960d7a3(
    *,
    cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
    exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    field_log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e62ce520030272762ccf6169ce5673be0610bd412fd2d9b9a3a7c7963d4853(
    *,
    auth_ttl: typing.Optional[jsii.Number] = None,
    client_id: typing.Optional[builtins.str] = None,
    iat_ttl: typing.Optional[jsii.Number] = None,
    issuer: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f0d0849f2d6ffc2b4b6a4eabed8e631f4ae22772572c4eae3d63c7ec6f2a4a4(
    *,
    app_id_client_regex: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    default_action: typing.Optional[builtins.str] = None,
    user_pool_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c30fb6e2b0bf2994b166c6091173ca1bbdf2a226ff26da5bfc0c35067fc8cc07(
    *,
    authentication_type: builtins.str,
    name: builtins.str,
    additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    lambda_authorizer_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    log_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.LogConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    open_id_connect_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_pool_config: typing.Optional[typing.Union[typing.Union[CfnGraphQLApi.UserPoolConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86eeb90bbb1ca5a453f08cfb90f5fb16cf4842431fc90d63f3ee21972f1be243(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    definition: typing.Optional[builtins.str] = None,
    definition_s3_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6052290b218f085df44320d030dc5da2a656bc2dfb652a6e8997c198d7360074(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e7b1316522ac1b9a93d87179eb23379f7762341da46fd001056a8704a20b2c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__555a23d4ba449beaaf98ed745a155165b6830286b0aeae2a45d326885e8eddef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29a3a5e0c95af4007408f43ded6d8b16b50975200325f9066820c3302d03398(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4848140e56b16e4736cedb1aa2fb1ca3fd82aeca7e977c876274b365740b08de(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20c7b2f1eadba8a608fdb8a0a590a3907eb9c891f22a7385f17ef74294ca1d0c(
    *,
    api_id: builtins.str,
    definition: typing.Optional[builtins.str] = None,
    definition_s3_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a19b37f9f570b32d81c1e70bfcb51be048fdffa3df94ad801e69b812f746f8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[typing.Union[CfnResolver.CachingConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    code: typing.Optional[builtins.str] = None,
    code_s3_location: typing.Optional[builtins.str] = None,
    data_source_name: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Union[typing.Union[CfnResolver.PipelineConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[typing.Union[CfnResolver.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    sync_config: typing.Optional[typing.Union[typing.Union[CfnResolver.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95aca731304382cdf3dcd502764afa9c3fa4887077a0e30a6874db561995ccfa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313f8d86637162de96ee41aad99883afe32469196f904fb4309e0e9e33fc98ba(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472e69750f14de2abe38ed65522399a06e502ba89a0b921571c0b2746c638e5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2233218403900cf6b8a69c999e792511fca483ed05d2fa4306e0d7b2535010(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c08751b4795b139490b95abf3b3d0f17260bfea4a916f1afbaf08d435cfa21d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6b9e8b849504be748695ce685546b844451460e25485772ca066bc2b65f61b1(
    value: typing.Optional[typing.Union[CfnResolver.CachingConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0dd83b21d0fde771732f3fdf63588b717c979c6ab095248970576c0a297e97d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd67bb7c14d4f8040b88b7d1c29031ed6038b21c10f80e4f0fcfd6c31af45cbd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d90421590c8dc3a0c283260b096db2cd054cf3d6852e741d1bfaf1bf52bbe597(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf560aa0e5a28a8ed71b1579e183bb6fb81cf53b398565d4fe06e8b7cfb4b31(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66d0a40a93385979fce12d901f6a195637584cfcb71b3a04c20d8333f0a582bf(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6c98074ee2ebbe5b451fe5513433aa3557366ed040722d6e61328ab781da16(
    value: typing.Optional[typing.Union[CfnResolver.PipelineConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd82effb0edb94da2492c911c5aecbe1fa5f2d88b6066513bb7f2a5713fdca7d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd52da508686e9da63db3673bad91680eaa1eb468984c1b4f57757668dcaed40(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f24f835e9a5b9af73089ccb61dfcf176cc230bb0feddf60b73360bab083e3f46(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a067b0164755508220ca8ad5f24cbd5ac6d6c57fb44d8404b14392f12d372f0c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a14449468f6ed96319993479a0ae9b3feacd27ec17e068d4d17ce598a964715(
    value: typing.Optional[typing.Union[CfnResolver.AppSyncRuntimeProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a111110922e122a02d7d649fe2daaa4c4d7cf1709e2078b92fe101fd93d8e4f5(
    value: typing.Optional[typing.Union[CfnResolver.SyncConfigProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d69cd55f1989ce956af7a1058706bfd4aaeba608d00146e50a90c1d3521cee0(
    *,
    name: builtins.str,
    runtime_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5089c8cac20eb98ddb2d855ec469e09dc0f7b1141ddaf4de8fd19eaaadac7891(
    *,
    ttl: jsii.Number,
    caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8760098edd4885448deb6a9ceb1ba3eb5367683995fadd12b5e5f3bf1e2fdd7e(
    *,
    lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2907a70554c3df66e94c41c4e36342a2860e214a5b7da358efbe204221066961(
    *,
    functions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd8efb0c43d72e5061a7c9c3de6483787260ccff8a3dff5a5152ca959d6af6a3(
    *,
    conflict_detection: builtins.str,
    conflict_handler: typing.Optional[builtins.str] = None,
    lambda_conflict_handler_config: typing.Optional[typing.Union[typing.Union[CfnResolver.LambdaConflictHandlerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b1ba8346de8783ad38f1a2377fd50bdd7577d903f4b68402c7b5ab604f16e5(
    *,
    api_id: builtins.str,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[typing.Union[CfnResolver.CachingConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    code: typing.Optional[builtins.str] = None,
    code_s3_location: typing.Optional[builtins.str] = None,
    data_source_name: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Union[typing.Union[CfnResolver.PipelineConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[typing.Union[CfnResolver.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    sync_config: typing.Optional[typing.Union[typing.Union[CfnResolver.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass
