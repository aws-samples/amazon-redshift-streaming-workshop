'''
# AWS::RefactorSpaces Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_refactorspaces as refactorspaces
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RefactorSpaces construct libraries](https://constructs.dev/search?q=refactorspaces)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RefactorSpaces resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RefactorSpaces.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RefactorSpaces](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RefactorSpaces.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnApplication",
):
    '''A CloudFormation ``AWS::RefactorSpaces::Application``.

    Creates an AWS Migration Hub Refactor Spaces application. The account that owns the environment also owns the applications created inside the environment, regardless of the account that creates the application. Refactor Spaces provisions an Amazon API Gateway , API Gateway VPC link, and Network Load Balancer for the application proxy inside your account.

    :cloudformationResource: AWS::RefactorSpaces::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_refactorspaces as refactorspaces
        
        cfn_application = refactorspaces.CfnApplication(self, "MyCfnApplication",
            api_gateway_proxy=refactorspaces.CfnApplication.ApiGatewayProxyInputProperty(
                endpoint_type="endpointType",
                stage_name="stageName"
            ),
            environment_identifier="environmentIdentifier",
            name="name",
            proxy_type="proxyType",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_id="vpcId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        api_gateway_proxy: typing.Optional[typing.Union[typing.Union["CfnApplication.ApiGatewayProxyInputProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        environment_identifier: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        proxy_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::RefactorSpaces::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_gateway_proxy: The endpoint URL of the Amazon API Gateway proxy.
        :param environment_identifier: The unique identifier of the environment.
        :param name: The name of the application.
        :param proxy_type: The proxy type of the proxy created within the application.
        :param tags: The tags assigned to the application.
        :param vpc_id: The ID of the virtual private cloud (VPC).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApplication.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            api_gateway_proxy=api_gateway_proxy,
            environment_identifier=environment_identifier,
            name=name,
            proxy_type=proxy_type,
            tags=tags,
            vpc_id=vpc_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApplication.inspect)
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
            type_hints = typing.get_type_hints(CfnApplication._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrApiGatewayId")
    def attr_api_gateway_id(self) -> builtins.str:
        '''The resource ID of the API Gateway for the proxy.

        :cloudformationAttribute: ApiGatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiGatewayId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrApplicationIdentifier")
    def attr_application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.

        :cloudformationAttribute: ApplicationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the application.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNlbArn")
    def attr_nlb_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Network Load Balancer .

        :cloudformationAttribute: NlbArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNlbArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNlbName")
    def attr_nlb_name(self) -> builtins.str:
        '''The name of the Network Load Balancer configured by the API Gateway proxy.

        :cloudformationAttribute: NlbName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNlbName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProxyUrl")
    def attr_proxy_url(self) -> builtins.str:
        '''The endpoint URL of the Amazon API Gateway proxy.

        :cloudformationAttribute: ProxyUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProxyUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStageName")
    def attr_stage_name(self) -> builtins.str:
        '''The name of the API Gateway stage.

        The name defaults to ``prod`` .

        :cloudformationAttribute: StageName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStageName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVpcLinkId")
    def attr_vpc_link_id(self) -> builtins.str:
        '''The ``VpcLink`` ID of the API Gateway proxy.

        :cloudformationAttribute: VpcLinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcLinkId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags assigned to the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiGatewayProxy")
    def api_gateway_proxy(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.ApiGatewayProxyInputProperty", _IResolvable_da3f097b]]:
        '''The endpoint URL of the Amazon API Gateway proxy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-apigatewayproxy
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.ApiGatewayProxyInputProperty", _IResolvable_da3f097b]], jsii.get(self, "apiGatewayProxy"))

    @api_gateway_proxy.setter
    def api_gateway_proxy(
        self,
        value: typing.Optional[typing.Union["CfnApplication.ApiGatewayProxyInputProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "api_gateway_proxy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGatewayProxy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-environmentidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "environment_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="proxyType")
    def proxy_type(self) -> typing.Optional[builtins.str]:
        '''The proxy type of the proxy created within the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-proxytype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyType"))

    @proxy_type.setter
    def proxy_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "proxy_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-vpcid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "vpc_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnApplication.ApiGatewayProxyInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_type": "endpointType", "stage_name": "stageName"},
    )
    class ApiGatewayProxyInputProperty:
        def __init__(
            self,
            *,
            endpoint_type: typing.Optional[builtins.str] = None,
            stage_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A wrapper object holding the Amazon API Gateway endpoint input.

            :param endpoint_type: The type of endpoint to use for the API Gateway proxy. If no value is specified in the request, the value is set to ``REGIONAL`` by default. If the value is set to ``PRIVATE`` in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud ( Amazon VPC ) endpoints for Amazon API Gateway that have been granted access.
            :param stage_name: The name of the API Gateway stage. The name defaults to ``prod`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                api_gateway_proxy_input_property = refactorspaces.CfnApplication.ApiGatewayProxyInputProperty(
                    endpoint_type="endpointType",
                    stage_name="stageName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.ApiGatewayProxyInputProperty.__init__)
                check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
                check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if endpoint_type is not None:
                self._values["endpoint_type"] = endpoint_type
            if stage_name is not None:
                self._values["stage_name"] = stage_name

        @builtins.property
        def endpoint_type(self) -> typing.Optional[builtins.str]:
            '''The type of endpoint to use for the API Gateway proxy.

            If no value is specified in the request, the value is set to ``REGIONAL`` by default.

            If the value is set to ``PRIVATE`` in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud ( Amazon VPC ) endpoints for Amazon API Gateway that have been granted access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html#cfn-refactorspaces-application-apigatewayproxyinput-endpointtype
            '''
            result = self._values.get("endpoint_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stage_name(self) -> typing.Optional[builtins.str]:
            '''The name of the API Gateway stage.

            The name defaults to ``prod`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html#cfn-refactorspaces-application-apigatewayproxyinput-stagename
            '''
            result = self._values.get("stage_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiGatewayProxyInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_gateway_proxy": "apiGatewayProxy",
        "environment_identifier": "environmentIdentifier",
        "name": "name",
        "proxy_type": "proxyType",
        "tags": "tags",
        "vpc_id": "vpcId",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        api_gateway_proxy: typing.Optional[typing.Union[typing.Union[CfnApplication.ApiGatewayProxyInputProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        environment_identifier: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        proxy_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param api_gateway_proxy: The endpoint URL of the Amazon API Gateway proxy.
        :param environment_identifier: The unique identifier of the environment.
        :param name: The name of the application.
        :param proxy_type: The proxy type of the proxy created within the application.
        :param tags: The tags assigned to the application.
        :param vpc_id: The ID of the virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_refactorspaces as refactorspaces
            
            cfn_application_props = refactorspaces.CfnApplicationProps(
                api_gateway_proxy=refactorspaces.CfnApplication.ApiGatewayProxyInputProperty(
                    endpoint_type="endpointType",
                    stage_name="stageName"
                ),
                environment_identifier="environmentIdentifier",
                name="name",
                proxy_type="proxyType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApplicationProps.__init__)
            check_type(argname="argument api_gateway_proxy", value=api_gateway_proxy, expected_type=type_hints["api_gateway_proxy"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument proxy_type", value=proxy_type, expected_type=type_hints["proxy_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if api_gateway_proxy is not None:
            self._values["api_gateway_proxy"] = api_gateway_proxy
        if environment_identifier is not None:
            self._values["environment_identifier"] = environment_identifier
        if name is not None:
            self._values["name"] = name
        if proxy_type is not None:
            self._values["proxy_type"] = proxy_type
        if tags is not None:
            self._values["tags"] = tags
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def api_gateway_proxy(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.ApiGatewayProxyInputProperty, _IResolvable_da3f097b]]:
        '''The endpoint URL of the Amazon API Gateway proxy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-apigatewayproxy
        '''
        result = self._values.get("api_gateway_proxy")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.ApiGatewayProxyInputProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def environment_identifier(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_type(self) -> typing.Optional[builtins.str]:
        '''The proxy type of the proxy created within the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-proxytype
        '''
        result = self._values.get("proxy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-vpcid
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnEnvironment",
):
    '''A CloudFormation ``AWS::RefactorSpaces::Environment``.

    Creates an AWS Migration Hub Refactor Spaces environment. The caller owns the environment resource, and all Refactor Spaces applications, services, and routes created within the environment. They are referred to as the *environment owner* . The environment owner has cross-account visibility and control of Refactor Spaces resources that are added to the environment by other accounts that the environment is shared with. When creating an environment, Refactor Spaces provisions a transit gateway in your account.

    :cloudformationResource: AWS::RefactorSpaces::Environment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_refactorspaces as refactorspaces
        
        cfn_environment = refactorspaces.CfnEnvironment(self, "MyCfnEnvironment",
            description="description",
            name="name",
            network_fabric_type="networkFabricType",
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
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        network_fabric_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::RefactorSpaces::Environment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: A description of the environment.
        :param name: The name of the environment.
        :param network_fabric_type: The network fabric type of the environment.
        :param tags: The tags assigned to the environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEnvironment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            description=description,
            name=name,
            network_fabric_type=network_fabric_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEnvironment.inspect)
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
            type_hints = typing.get_type_hints(CfnEnvironment._render_properties)
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
        '''The Amazon Resource Name (ARN) of the environment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEnvironmentIdentifier")
    def attr_environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :cloudformationAttribute: EnvironmentIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTransitGatewayId")
    def attr_transit_gateway_id(self) -> builtins.str:
        '''The ID of the AWS Transit Gateway set up by the environment.

        :cloudformationAttribute: TransitGatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTransitGatewayId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags assigned to the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEnvironment, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEnvironment, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkFabricType")
    def network_fabric_type(self) -> typing.Optional[builtins.str]:
        '''The network fabric type of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-networkfabrictype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkFabricType"))

    @network_fabric_type.setter
    def network_fabric_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEnvironment, "network_fabric_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkFabricType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "network_fabric_type": "networkFabricType",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        network_fabric_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param description: A description of the environment.
        :param name: The name of the environment.
        :param network_fabric_type: The network fabric type of the environment.
        :param tags: The tags assigned to the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_refactorspaces as refactorspaces
            
            cfn_environment_props = refactorspaces.CfnEnvironmentProps(
                description="description",
                name="name",
                network_fabric_type="networkFabricType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEnvironmentProps.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_fabric_type", value=network_fabric_type, expected_type=type_hints["network_fabric_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if network_fabric_type is not None:
            self._values["network_fabric_type"] = network_fabric_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_fabric_type(self) -> typing.Optional[builtins.str]:
        '''The network fabric type of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-networkfabrictype
        '''
        result = self._values.get("network_fabric_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRoute(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnRoute",
):
    '''A CloudFormation ``AWS::RefactorSpaces::Route``.

    Creates an AWS Migration Hub Refactor Spaces route. The account owner of the service resource is always the environment owner, regardless of the account creating the route. Routes target a service in the application. If an application does not have any routes, then the first route must be created as a ``DEFAULT`` ``RouteType`` .
    .. epigraph::

       In the ``AWS::RefactorSpaces::Route`` resource, you can only update the ``SourcePath`` and ``Methods`` properties, which reside under the ``UriPathRoute`` property. All other properties associated with the ``AWS::RefactorSpaces::Route`` cannot be updated, even though the property description might indicate otherwise.

    When you create a route, Refactor Spaces configures the Amazon API Gateway to send traffic to the target service.

    - If the service has a URL endpoint, and the endpoint resolves to a private IP address, Refactor Spaces routes traffic using the API Gateway VPC link.
    - If the service has a URL endpoint, and the endpoint resolves to a public IP address, Refactor Spaces routes traffic over the public internet.
    - If the service has a AWS Lambda function endpoint, then Refactor Spaces uses API Gateway ’s Lambda integration.

    A health check is performed on the service when the route is created. If the health check fails, the route transitions to ``FAILED`` , and no traffic is sent to the service. For Lambda functions, the Lambda function state is checked. If the function is not active, the function configuration is updated so Lambda resources are provisioned. If the Lambda state is ``Failed`` , then the route creation fails. For more information, see the `GetFunctionConfiguration's State response parameter <https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#SSS-GetFunctionConfiguration-response-State>`_ in the *AWS Lambda Developer Guide* . For public URLs, a connection is opened to the public endpoint. If the URL is not reachable, the health check fails. For private URLs, a target groups is created and the target group health check is run. The ``HealthCheckProtocol`` , ``HealthCheckPort`` , and ``HealthCheckPath`` are the same protocol, port, and path specified in the URL or Health URL if used. All other settings use the default values, as described in `Health checks for your target groups <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html>`_ . The health check is considered successful if at least one target within the target group transitions to healthy state.

    :cloudformationResource: AWS::RefactorSpaces::Route
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_refactorspaces as refactorspaces
        
        cfn_route = refactorspaces.CfnRoute(self, "MyCfnRoute",
            application_identifier="applicationIdentifier",
            environment_identifier="environmentIdentifier",
            service_identifier="serviceIdentifier",
        
            # the properties below are optional
            default_route=refactorspaces.CfnRoute.DefaultRouteInputProperty(
                activation_state="activationState"
            ),
            route_type="routeType",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            uri_path_route=refactorspaces.CfnRoute.UriPathRouteInputProperty(
                activation_state="activationState",
        
                # the properties below are optional
                include_child_paths=False,
                methods=["methods"],
                source_path="sourcePath"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
        service_identifier: builtins.str,
        default_route: typing.Optional[typing.Union[typing.Union["CfnRoute.DefaultRouteInputProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        route_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        uri_path_route: typing.Optional[typing.Union[typing.Union["CfnRoute.UriPathRouteInputProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::RefactorSpaces::Route``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_identifier: The unique identifier of the application.
        :param environment_identifier: The unique identifier of the environment.
        :param service_identifier: The unique identifier of the service.
        :param default_route: ``AWS::RefactorSpaces::Route.DefaultRoute``.
        :param route_type: The route type of the route.
        :param tags: The tags assigned to the route.
        :param uri_path_route: The configuration for the URI path route type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnRoute.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRouteProps(
            application_identifier=application_identifier,
            environment_identifier=environment_identifier,
            service_identifier=service_identifier,
            default_route=default_route,
            route_type=route_type,
            tags=tags,
            uri_path_route=uri_path_route,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnRoute.inspect)
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
            type_hints = typing.get_type_hints(CfnRoute._render_properties)
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
        '''The Amazon Resource Name (ARN) of the route.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPathResourceToId")
    def attr_path_resource_to_id(self) -> builtins.str:
        '''A mapping of Amazon API Gateway path resources to resource IDs.

        :cloudformationAttribute: PathResourceToId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPathResourceToId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRouteIdentifier")
    def attr_route_identifier(self) -> builtins.str:
        '''The unique identifier of the route.

        :cloudformationAttribute: RouteIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRouteIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags assigned to the route.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationIdentifier")
    def application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-applicationidentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationIdentifier"))

    @application_identifier.setter
    def application_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoute, "application_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-environmentidentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoute, "environment_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceIdentifier")
    def service_identifier(self) -> builtins.str:
        '''The unique identifier of the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-serviceidentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceIdentifier"))

    @service_identifier.setter
    def service_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoute, "service_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultRoute")
    def default_route(
        self,
    ) -> typing.Optional[typing.Union["CfnRoute.DefaultRouteInputProperty", _IResolvable_da3f097b]]:
        '''``AWS::RefactorSpaces::Route.DefaultRoute``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-defaultroute
        '''
        return typing.cast(typing.Optional[typing.Union["CfnRoute.DefaultRouteInputProperty", _IResolvable_da3f097b]], jsii.get(self, "defaultRoute"))

    @default_route.setter
    def default_route(
        self,
        value: typing.Optional[typing.Union["CfnRoute.DefaultRouteInputProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoute, "default_route").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRoute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routeType")
    def route_type(self) -> typing.Optional[builtins.str]:
        '''The route type of the route.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-routetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeType"))

    @route_type.setter
    def route_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoute, "route_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="uriPathRoute")
    def uri_path_route(
        self,
    ) -> typing.Optional[typing.Union["CfnRoute.UriPathRouteInputProperty", _IResolvable_da3f097b]]:
        '''The configuration for the URI path route type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-uripathroute
        '''
        return typing.cast(typing.Optional[typing.Union["CfnRoute.UriPathRouteInputProperty", _IResolvable_da3f097b]], jsii.get(self, "uriPathRoute"))

    @uri_path_route.setter
    def uri_path_route(
        self,
        value: typing.Optional[typing.Union["CfnRoute.UriPathRouteInputProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoute, "uri_path_route").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uriPathRoute", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnRoute.DefaultRouteInputProperty",
        jsii_struct_bases=[],
        name_mapping={"activation_state": "activationState"},
    )
    class DefaultRouteInputProperty:
        def __init__(self, *, activation_state: builtins.str) -> None:
            '''
            :param activation_state: ``CfnRoute.DefaultRouteInputProperty.ActivationState``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-defaultrouteinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                default_route_input_property = refactorspaces.CfnRoute.DefaultRouteInputProperty(
                    activation_state="activationState"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnRoute.DefaultRouteInputProperty.__init__)
                check_type(argname="argument activation_state", value=activation_state, expected_type=type_hints["activation_state"])
            self._values: typing.Dict[str, typing.Any] = {
                "activation_state": activation_state,
            }

        @builtins.property
        def activation_state(self) -> builtins.str:
            '''``CfnRoute.DefaultRouteInputProperty.ActivationState``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-defaultrouteinput.html#cfn-refactorspaces-route-defaultrouteinput-activationstate
            '''
            result = self._values.get("activation_state")
            assert result is not None, "Required property 'activation_state' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultRouteInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnRoute.UriPathRouteInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "activation_state": "activationState",
            "include_child_paths": "includeChildPaths",
            "methods": "methods",
            "source_path": "sourcePath",
        },
    )
    class UriPathRouteInputProperty:
        def __init__(
            self,
            *,
            activation_state: builtins.str,
            include_child_paths: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            methods: typing.Optional[typing.Sequence[builtins.str]] = None,
            source_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for the URI path route type.

            :param activation_state: Indicates whether traffic is forwarded to this route’s service after the route is created.
            :param include_child_paths: Indicates whether to match all subpaths of the given source path. If this value is ``false`` , requests must match the source path exactly before they are forwarded to this route's service.
            :param methods: A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.
            :param source_path: The path to use to match traffic. Paths must start with ``/`` and are relative to the base of the application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                uri_path_route_input_property = refactorspaces.CfnRoute.UriPathRouteInputProperty(
                    activation_state="activationState",
                
                    # the properties below are optional
                    include_child_paths=False,
                    methods=["methods"],
                    source_path="sourcePath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnRoute.UriPathRouteInputProperty.__init__)
                check_type(argname="argument activation_state", value=activation_state, expected_type=type_hints["activation_state"])
                check_type(argname="argument include_child_paths", value=include_child_paths, expected_type=type_hints["include_child_paths"])
                check_type(argname="argument methods", value=methods, expected_type=type_hints["methods"])
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
            self._values: typing.Dict[str, typing.Any] = {
                "activation_state": activation_state,
            }
            if include_child_paths is not None:
                self._values["include_child_paths"] = include_child_paths
            if methods is not None:
                self._values["methods"] = methods
            if source_path is not None:
                self._values["source_path"] = source_path

        @builtins.property
        def activation_state(self) -> builtins.str:
            '''Indicates whether traffic is forwarded to this route’s service after the route is created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-activationstate
            '''
            result = self._values.get("activation_state")
            assert result is not None, "Required property 'activation_state' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def include_child_paths(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to match all subpaths of the given source path.

            If this value is ``false`` , requests must match the source path exactly before they are forwarded to this route's service.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-includechildpaths
            '''
            result = self._values.get("include_child_paths")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def methods(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of HTTP methods to match.

            An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-methods
            '''
            result = self._values.get("methods")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def source_path(self) -> typing.Optional[builtins.str]:
            '''The path to use to match traffic.

            Paths must start with ``/`` and are relative to the base of the application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-sourcepath
            '''
            result = self._values.get("source_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UriPathRouteInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnRouteProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_identifier": "applicationIdentifier",
        "environment_identifier": "environmentIdentifier",
        "service_identifier": "serviceIdentifier",
        "default_route": "defaultRoute",
        "route_type": "routeType",
        "tags": "tags",
        "uri_path_route": "uriPathRoute",
    },
)
class CfnRouteProps:
    def __init__(
        self,
        *,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
        service_identifier: builtins.str,
        default_route: typing.Optional[typing.Union[typing.Union[CfnRoute.DefaultRouteInputProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        route_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        uri_path_route: typing.Optional[typing.Union[typing.Union[CfnRoute.UriPathRouteInputProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRoute``.

        :param application_identifier: The unique identifier of the application.
        :param environment_identifier: The unique identifier of the environment.
        :param service_identifier: The unique identifier of the service.
        :param default_route: ``AWS::RefactorSpaces::Route.DefaultRoute``.
        :param route_type: The route type of the route.
        :param tags: The tags assigned to the route.
        :param uri_path_route: The configuration for the URI path route type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_refactorspaces as refactorspaces
            
            cfn_route_props = refactorspaces.CfnRouteProps(
                application_identifier="applicationIdentifier",
                environment_identifier="environmentIdentifier",
                service_identifier="serviceIdentifier",
            
                # the properties below are optional
                default_route=refactorspaces.CfnRoute.DefaultRouteInputProperty(
                    activation_state="activationState"
                ),
                route_type="routeType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                uri_path_route=refactorspaces.CfnRoute.UriPathRouteInputProperty(
                    activation_state="activationState",
            
                    # the properties below are optional
                    include_child_paths=False,
                    methods=["methods"],
                    source_path="sourcePath"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnRouteProps.__init__)
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument service_identifier", value=service_identifier, expected_type=type_hints["service_identifier"])
            check_type(argname="argument default_route", value=default_route, expected_type=type_hints["default_route"])
            check_type(argname="argument route_type", value=route_type, expected_type=type_hints["route_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument uri_path_route", value=uri_path_route, expected_type=type_hints["uri_path_route"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
            "service_identifier": service_identifier,
        }
        if default_route is not None:
            self._values["default_route"] = default_route
        if route_type is not None:
            self._values["route_type"] = route_type
        if tags is not None:
            self._values["tags"] = tags
        if uri_path_route is not None:
            self._values["uri_path_route"] = uri_path_route

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-applicationidentifier
        '''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_identifier(self) -> builtins.str:
        '''The unique identifier of the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-serviceidentifier
        '''
        result = self._values.get("service_identifier")
        assert result is not None, "Required property 'service_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_route(
        self,
    ) -> typing.Optional[typing.Union[CfnRoute.DefaultRouteInputProperty, _IResolvable_da3f097b]]:
        '''``AWS::RefactorSpaces::Route.DefaultRoute``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-defaultroute
        '''
        result = self._values.get("default_route")
        return typing.cast(typing.Optional[typing.Union[CfnRoute.DefaultRouteInputProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def route_type(self) -> typing.Optional[builtins.str]:
        '''The route type of the route.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-routetype
        '''
        result = self._values.get("route_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the route.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def uri_path_route(
        self,
    ) -> typing.Optional[typing.Union[CfnRoute.UriPathRouteInputProperty, _IResolvable_da3f097b]]:
        '''The configuration for the URI path route type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-uripathroute
        '''
        result = self._values.get("uri_path_route")
        return typing.cast(typing.Optional[typing.Union[CfnRoute.UriPathRouteInputProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnService(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnService",
):
    '''A CloudFormation ``AWS::RefactorSpaces::Service``.

    Creates an AWS Migration Hub Refactor Spaces service. The account owner of the service is always the environment owner, regardless of which account in the environment creates the service. Services have either a URL endpoint in a virtual private cloud (VPC), or a Lambda function endpoint.
    .. epigraph::

       If an AWS resource is launched in a service VPC, and you want it to be accessible to all of an environment’s services with VPCs and routes, apply the ``RefactorSpacesSecurityGroup`` to the resource. Alternatively, to add more cross-account constraints, apply your own security group.

    :cloudformationResource: AWS::RefactorSpaces::Service
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_refactorspaces as refactorspaces
        
        cfn_service = refactorspaces.CfnService(self, "MyCfnService",
            application_identifier="applicationIdentifier",
            environment_identifier="environmentIdentifier",
        
            # the properties below are optional
            description="description",
            endpoint_type="endpointType",
            lambda_endpoint=refactorspaces.CfnService.LambdaEndpointInputProperty(
                arn="arn"
            ),
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            url_endpoint=refactorspaces.CfnService.UrlEndpointInputProperty(
                url="url",
        
                # the properties below are optional
                health_url="healthUrl"
            ),
            vpc_id="vpcId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        endpoint_type: typing.Optional[builtins.str] = None,
        lambda_endpoint: typing.Optional[typing.Union[typing.Union["CfnService.LambdaEndpointInputProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        url_endpoint: typing.Optional[typing.Union[typing.Union["CfnService.UrlEndpointInputProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::RefactorSpaces::Service``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_identifier: The unique identifier of the application.
        :param environment_identifier: The unique identifier of the environment.
        :param description: A description of the service.
        :param endpoint_type: The endpoint type of the service.
        :param lambda_endpoint: A summary of the configuration for the AWS Lambda endpoint type.
        :param name: The name of the service.
        :param tags: The tags assigned to the service.
        :param url_endpoint: The summary of the configuration for the URL endpoint type.
        :param vpc_id: The ID of the virtual private cloud (VPC).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProps(
            application_identifier=application_identifier,
            environment_identifier=environment_identifier,
            description=description,
            endpoint_type=endpoint_type,
            lambda_endpoint=lambda_endpoint,
            name=name,
            tags=tags,
            url_endpoint=url_endpoint,
            vpc_id=vpc_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnService.inspect)
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
            type_hints = typing.get_type_hints(CfnService._render_properties)
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
        '''The Amazon Resource Name (ARN) of the service.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceIdentifier")
    def attr_service_identifier(self) -> builtins.str:
        '''The unique identifier of the service.

        :cloudformationAttribute: ServiceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags assigned to the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationIdentifier")
    def application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-applicationidentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationIdentifier"))

    @application_identifier.setter
    def application_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "application_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-environmentidentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "environment_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> typing.Optional[builtins.str]:
        '''The endpoint type of the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-endpointtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "endpoint_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lambdaEndpoint")
    def lambda_endpoint(
        self,
    ) -> typing.Optional[typing.Union["CfnService.LambdaEndpointInputProperty", _IResolvable_da3f097b]]:
        '''A summary of the configuration for the AWS Lambda endpoint type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-lambdaendpoint
        '''
        return typing.cast(typing.Optional[typing.Union["CfnService.LambdaEndpointInputProperty", _IResolvable_da3f097b]], jsii.get(self, "lambdaEndpoint"))

    @lambda_endpoint.setter
    def lambda_endpoint(
        self,
        value: typing.Optional[typing.Union["CfnService.LambdaEndpointInputProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "lambda_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaEndpoint", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="urlEndpoint")
    def url_endpoint(
        self,
    ) -> typing.Optional[typing.Union["CfnService.UrlEndpointInputProperty", _IResolvable_da3f097b]]:
        '''The summary of the configuration for the URL endpoint type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-urlendpoint
        '''
        return typing.cast(typing.Optional[typing.Union["CfnService.UrlEndpointInputProperty", _IResolvable_da3f097b]], jsii.get(self, "urlEndpoint"))

    @url_endpoint.setter
    def url_endpoint(
        self,
        value: typing.Optional[typing.Union["CfnService.UrlEndpointInputProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "url_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlEndpoint", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-vpcid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "vpc_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnService.LambdaEndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class LambdaEndpointInputProperty:
        def __init__(self, *, arn: builtins.str) -> None:
            '''The input for the AWS Lambda endpoint type.

            :param arn: The Amazon Resource Name (ARN) of the Lambda endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-lambdaendpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                lambda_endpoint_input_property = refactorspaces.CfnService.LambdaEndpointInputProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.LambdaEndpointInputProperty.__init__)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Lambda endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-lambdaendpointinput.html#cfn-refactorspaces-service-lambdaendpointinput-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaEndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnService.UrlEndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url", "health_url": "healthUrl"},
    )
    class UrlEndpointInputProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            health_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for the URL endpoint type.

            :param url: The URL to route traffic to. The URL must be an `rfc3986-formatted URL <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc3986>`_ . If the host is a domain name, the name must be resolvable over the public internet. If the scheme is ``https`` , the top level domain of the host must be listed in the `IANA root zone database <https://docs.aws.amazon.com/https://www.iana.org/domains/root/db>`_ .
            :param health_url: The health check URL of the URL endpoint type. If the URL is a public endpoint, the ``HealthUrl`` must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                url_endpoint_input_property = refactorspaces.CfnService.UrlEndpointInputProperty(
                    url="url",
                
                    # the properties below are optional
                    health_url="healthUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.UrlEndpointInputProperty.__init__)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument health_url", value=health_url, expected_type=type_hints["health_url"])
            self._values: typing.Dict[str, typing.Any] = {
                "url": url,
            }
            if health_url is not None:
                self._values["health_url"] = health_url

        @builtins.property
        def url(self) -> builtins.str:
            '''The URL to route traffic to.

            The URL must be an `rfc3986-formatted URL <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc3986>`_ . If the host is a domain name, the name must be resolvable over the public internet. If the scheme is ``https`` , the top level domain of the host must be listed in the `IANA root zone database <https://docs.aws.amazon.com/https://www.iana.org/domains/root/db>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html#cfn-refactorspaces-service-urlendpointinput-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def health_url(self) -> typing.Optional[builtins.str]:
            '''The health check URL of the URL endpoint type.

            If the URL is a public endpoint, the ``HealthUrl`` must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html#cfn-refactorspaces-service-urlendpointinput-healthurl
            '''
            result = self._values.get("health_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UrlEndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_identifier": "applicationIdentifier",
        "environment_identifier": "environmentIdentifier",
        "description": "description",
        "endpoint_type": "endpointType",
        "lambda_endpoint": "lambdaEndpoint",
        "name": "name",
        "tags": "tags",
        "url_endpoint": "urlEndpoint",
        "vpc_id": "vpcId",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        endpoint_type: typing.Optional[builtins.str] = None,
        lambda_endpoint: typing.Optional[typing.Union[typing.Union[CfnService.LambdaEndpointInputProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        url_endpoint: typing.Optional[typing.Union[typing.Union[CfnService.UrlEndpointInputProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnService``.

        :param application_identifier: The unique identifier of the application.
        :param environment_identifier: The unique identifier of the environment.
        :param description: A description of the service.
        :param endpoint_type: The endpoint type of the service.
        :param lambda_endpoint: A summary of the configuration for the AWS Lambda endpoint type.
        :param name: The name of the service.
        :param tags: The tags assigned to the service.
        :param url_endpoint: The summary of the configuration for the URL endpoint type.
        :param vpc_id: The ID of the virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_refactorspaces as refactorspaces
            
            cfn_service_props = refactorspaces.CfnServiceProps(
                application_identifier="applicationIdentifier",
                environment_identifier="environmentIdentifier",
            
                # the properties below are optional
                description="description",
                endpoint_type="endpointType",
                lambda_endpoint=refactorspaces.CfnService.LambdaEndpointInputProperty(
                    arn="arn"
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                url_endpoint=refactorspaces.CfnService.UrlEndpointInputProperty(
                    url="url",
            
                    # the properties below are optional
                    health_url="healthUrl"
                ),
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnServiceProps.__init__)
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument lambda_endpoint", value=lambda_endpoint, expected_type=type_hints["lambda_endpoint"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument url_endpoint", value=url_endpoint, expected_type=type_hints["url_endpoint"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
        }
        if description is not None:
            self._values["description"] = description
        if endpoint_type is not None:
            self._values["endpoint_type"] = endpoint_type
        if lambda_endpoint is not None:
            self._values["lambda_endpoint"] = lambda_endpoint
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if url_endpoint is not None:
            self._values["url_endpoint"] = url_endpoint
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-applicationidentifier
        '''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_type(self) -> typing.Optional[builtins.str]:
        '''The endpoint type of the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-endpointtype
        '''
        result = self._values.get("endpoint_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_endpoint(
        self,
    ) -> typing.Optional[typing.Union[CfnService.LambdaEndpointInputProperty, _IResolvable_da3f097b]]:
        '''A summary of the configuration for the AWS Lambda endpoint type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-lambdaendpoint
        '''
        result = self._values.get("lambda_endpoint")
        return typing.cast(typing.Optional[typing.Union[CfnService.LambdaEndpointInputProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def url_endpoint(
        self,
    ) -> typing.Optional[typing.Union[CfnService.UrlEndpointInputProperty, _IResolvable_da3f097b]]:
        '''The summary of the configuration for the URL endpoint type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-urlendpoint
        '''
        result = self._values.get("url_endpoint")
        return typing.cast(typing.Optional[typing.Union[CfnService.UrlEndpointInputProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-vpcid
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnEnvironment",
    "CfnEnvironmentProps",
    "CfnRoute",
    "CfnRouteProps",
    "CfnService",
    "CfnServiceProps",
]

publication.publish()
