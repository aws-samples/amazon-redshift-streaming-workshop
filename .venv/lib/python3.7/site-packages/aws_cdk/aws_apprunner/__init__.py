'''
# AWS::AppRunner Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_apprunner as apprunner
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppRunner construct libraries](https://constructs.dev/search?q=apprunner)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppRunner resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppRunner.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-apprunner-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppRunner](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppRunner.html).

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
class CfnObservabilityConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apprunner.CfnObservabilityConfiguration",
):
    '''A CloudFormation ``AWS::AppRunner::ObservabilityConfiguration``.

    Specify an AWS App Runner observability configuration by using the ``AWS::AppRunner::ObservabilityConfiguration`` resource in an AWS CloudFormation template.

    The ``AWS::AppRunner::ObservabilityConfiguration`` resource is an AWS App Runner resource type that specifies an App Runner observability configuration.

    App Runner requires this resource when you specify App Runner services and you want to enable non-default observability features. You can share an observability configuration across multiple services.

    Create multiple revisions of a configuration by specifying this resource multiple times using the same ``ObservabilityConfigurationName`` . App Runner creates multiple resources with incremental ``ObservabilityConfigurationRevision`` values. When you specify a service and configure an observability configuration resource, the service uses the latest active revision of the observability configuration by default. You can optionally configure the service to use a specific revision.

    The observability configuration resource is designed to configure multiple features (currently one feature, tracing). This resource takes optional parameters that describe the configuration of these features (currently one parameter, ``TraceConfiguration`` ). If you don't specify a feature parameter, App Runner doesn't enable the feature.

    :cloudformationResource: AWS::AppRunner::ObservabilityConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apprunner as apprunner
        
        cfn_observability_configuration = apprunner.CfnObservabilityConfiguration(self, "MyCfnObservabilityConfiguration",
            observability_configuration_name="observabilityConfigurationName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trace_configuration=apprunner.CfnObservabilityConfiguration.TraceConfigurationProperty(
                vendor="vendor"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        observability_configuration_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        trace_configuration: typing.Optional[typing.Union[typing.Union["CfnObservabilityConfiguration.TraceConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::AppRunner::ObservabilityConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param observability_configuration_name: A name for the observability configuration. When you use it for the first time in an AWS Region , App Runner creates revision number ``1`` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration. .. epigraph:: The name ``DefaultConfiguration`` is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it. When you want to use your own observability configuration for your App Runner service, *create a configuration with a different name* , and then provide it when you create or update your service. If you don't specify a name, AWS CloudFormation generates a name for your observability configuration.
        :param tags: A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
        :param trace_configuration: The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnObservabilityConfiguration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnObservabilityConfigurationProps(
            observability_configuration_name=observability_configuration_name,
            tags=tags,
            trace_configuration=trace_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnObservabilityConfiguration.inspect)
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
            type_hints = typing.get_type_hints(CfnObservabilityConfiguration._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLatest")
    def attr_latest(self) -> _IResolvable_da3f097b:
        '''It's set to ``true`` for the configuration with the highest ``Revision`` among all configurations that share the same ``ObservabilityConfigurationName`` .

        It's set to ``false`` otherwise.

        :cloudformationAttribute: Latest
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLatest"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrObservabilityConfigurationArn")
    def attr_observability_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of this observability configuration.

        :cloudformationAttribute: ObservabilityConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrObservabilityConfigurationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrObservabilityConfigurationRevision")
    def attr_observability_configuration_revision(self) -> jsii.Number:
        '''The revision of this observability configuration.

        It's unique among all the active configurations ( ``"Status": "ACTIVE"`` ) that share the same ``ObservabilityConfigurationName`` .

        :cloudformationAttribute: ObservabilityConfigurationRevision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrObservabilityConfigurationRevision"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''A list of metadata items that you can associate with your observability configuration resource.

        A tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfigurationName")
    def observability_configuration_name(self) -> typing.Optional[builtins.str]:
        '''A name for the observability configuration.

        When you use it for the first time in an AWS Region , App Runner creates revision number ``1`` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
        .. epigraph::

           The name ``DefaultConfiguration`` is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it.

           When you want to use your own observability configuration for your App Runner service, *create a configuration with a different name* , and then provide it when you create or update your service.

        If you don't specify a name, AWS CloudFormation generates a name for your observability configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-observabilityconfigurationname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "observabilityConfigurationName"))

    @observability_configuration_name.setter
    def observability_configuration_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnObservabilityConfiguration, "observability_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "observabilityConfigurationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="traceConfiguration")
    def trace_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnObservabilityConfiguration.TraceConfigurationProperty", _IResolvable_da3f097b]]:
        '''The configuration of the tracing feature within this observability configuration.

        If you don't specify it, App Runner doesn't enable tracing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnObservabilityConfiguration.TraceConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "traceConfiguration"))

    @trace_configuration.setter
    def trace_configuration(
        self,
        value: typing.Optional[typing.Union["CfnObservabilityConfiguration.TraceConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnObservabilityConfiguration, "trace_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "traceConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnObservabilityConfiguration.TraceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vendor": "vendor"},
    )
    class TraceConfigurationProperty:
        def __init__(self, *, vendor: builtins.str) -> None:
            '''Describes the configuration of the tracing feature within an AWS App Runner observability configuration.

            :param vendor: The implementation provider chosen for tracing App Runner services.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                trace_configuration_property = apprunner.CfnObservabilityConfiguration.TraceConfigurationProperty(
                    vendor="vendor"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnObservabilityConfiguration.TraceConfigurationProperty.__init__)
                check_type(argname="argument vendor", value=vendor, expected_type=type_hints["vendor"])
            self._values: typing.Dict[str, typing.Any] = {
                "vendor": vendor,
            }

        @builtins.property
        def vendor(self) -> builtins.str:
            '''The implementation provider chosen for tracing App Runner services.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration-vendor
            '''
            result = self._values.get("vendor")
            assert result is not None, "Required property 'vendor' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TraceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apprunner.CfnObservabilityConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "observability_configuration_name": "observabilityConfigurationName",
        "tags": "tags",
        "trace_configuration": "traceConfiguration",
    },
)
class CfnObservabilityConfigurationProps:
    def __init__(
        self,
        *,
        observability_configuration_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        trace_configuration: typing.Optional[typing.Union[typing.Union[CfnObservabilityConfiguration.TraceConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnObservabilityConfiguration``.

        :param observability_configuration_name: A name for the observability configuration. When you use it for the first time in an AWS Region , App Runner creates revision number ``1`` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration. .. epigraph:: The name ``DefaultConfiguration`` is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it. When you want to use your own observability configuration for your App Runner service, *create a configuration with a different name* , and then provide it when you create or update your service. If you don't specify a name, AWS CloudFormation generates a name for your observability configuration.
        :param tags: A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
        :param trace_configuration: The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apprunner as apprunner
            
            cfn_observability_configuration_props = apprunner.CfnObservabilityConfigurationProps(
                observability_configuration_name="observabilityConfigurationName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trace_configuration=apprunner.CfnObservabilityConfiguration.TraceConfigurationProperty(
                    vendor="vendor"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnObservabilityConfigurationProps.__init__)
            check_type(argname="argument observability_configuration_name", value=observability_configuration_name, expected_type=type_hints["observability_configuration_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trace_configuration", value=trace_configuration, expected_type=type_hints["trace_configuration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if observability_configuration_name is not None:
            self._values["observability_configuration_name"] = observability_configuration_name
        if tags is not None:
            self._values["tags"] = tags
        if trace_configuration is not None:
            self._values["trace_configuration"] = trace_configuration

    @builtins.property
    def observability_configuration_name(self) -> typing.Optional[builtins.str]:
        '''A name for the observability configuration.

        When you use it for the first time in an AWS Region , App Runner creates revision number ``1`` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
        .. epigraph::

           The name ``DefaultConfiguration`` is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it.

           When you want to use your own observability configuration for your App Runner service, *create a configuration with a different name* , and then provide it when you create or update your service.

        If you don't specify a name, AWS CloudFormation generates a name for your observability configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-observabilityconfigurationname
        '''
        result = self._values.get("observability_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of metadata items that you can associate with your observability configuration resource.

        A tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def trace_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnObservabilityConfiguration.TraceConfigurationProperty, _IResolvable_da3f097b]]:
        '''The configuration of the tracing feature within this observability configuration.

        If you don't specify it, App Runner doesn't enable tracing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration
        '''
        result = self._values.get("trace_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnObservabilityConfiguration.TraceConfigurationProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnObservabilityConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnService(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apprunner.CfnService",
):
    '''A CloudFormation ``AWS::AppRunner::Service``.

    Specify an AWS App Runner service by using the ``AWS::AppRunner::Service`` resource in an AWS CloudFormation template.

    The ``AWS::AppRunner::Service`` resource is an AWS App Runner resource type that specifies an App Runner service.

    :cloudformationResource: AWS::AppRunner::Service
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apprunner as apprunner
        
        cfn_service = apprunner.CfnService(self, "MyCfnService",
            source_configuration=apprunner.CfnService.SourceConfigurationProperty(
                authentication_configuration=apprunner.CfnService.AuthenticationConfigurationProperty(
                    access_role_arn="accessRoleArn",
                    connection_arn="connectionArn"
                ),
                auto_deployments_enabled=False,
                code_repository=apprunner.CfnService.CodeRepositoryProperty(
                    repository_url="repositoryUrl",
                    source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                        type="type",
                        value="value"
                    ),
        
                    # the properties below are optional
                    code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                        configuration_source="configurationSource",
        
                        # the properties below are optional
                        code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                            runtime="runtime",
        
                            # the properties below are optional
                            build_command="buildCommand",
                            port="port",
                            runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            start_command="startCommand"
                        )
                    )
                ),
                image_repository=apprunner.CfnService.ImageRepositoryProperty(
                    image_identifier="imageIdentifier",
                    image_repository_type="imageRepositoryType",
        
                    # the properties below are optional
                    image_configuration=apprunner.CfnService.ImageConfigurationProperty(
                        port="port",
                        runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        start_command="startCommand"
                    )
                )
            ),
        
            # the properties below are optional
            auto_scaling_configuration_arn="autoScalingConfigurationArn",
            encryption_configuration=apprunner.CfnService.EncryptionConfigurationProperty(
                kms_key="kmsKey"
            ),
            health_check_configuration=apprunner.CfnService.HealthCheckConfigurationProperty(
                healthy_threshold=123,
                interval=123,
                path="path",
                protocol="protocol",
                timeout=123,
                unhealthy_threshold=123
            ),
            instance_configuration=apprunner.CfnService.InstanceConfigurationProperty(
                cpu="cpu",
                instance_role_arn="instanceRoleArn",
                memory="memory"
            ),
            network_configuration=apprunner.CfnService.NetworkConfigurationProperty(
                egress_configuration=apprunner.CfnService.EgressConfigurationProperty(
                    egress_type="egressType",
        
                    # the properties below are optional
                    vpc_connector_arn="vpcConnectorArn"
                )
            ),
            observability_configuration=apprunner.CfnService.ServiceObservabilityConfigurationProperty(
                observability_enabled=False,
        
                # the properties below are optional
                observability_configuration_arn="observabilityConfigurationArn"
            ),
            service_name="serviceName",
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
        source_configuration: typing.Union[typing.Union["CfnService.SourceConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[typing.Union["CfnService.EncryptionConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        health_check_configuration: typing.Optional[typing.Union[typing.Union["CfnService.HealthCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        instance_configuration: typing.Optional[typing.Union[typing.Union["CfnService.InstanceConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        network_configuration: typing.Optional[typing.Union[typing.Union["CfnService.NetworkConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        observability_configuration: typing.Optional[typing.Union[typing.Union["CfnService.ServiceObservabilityConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        service_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::AppRunner::Service``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param source_configuration: The source to deploy to the App Runner service. It can be a code or an image repository.
        :param auto_scaling_configuration_arn: The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration. Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3`` Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability``
        :param encryption_configuration: An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed key .
        :param health_check_configuration: The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.
        :param instance_configuration: The runtime configuration of instances (scaling units) of your service.
        :param network_configuration: Configuration settings related to network traffic of the web application that the App Runner service runs.
        :param observability_configuration: The observability configuration of your service.
        :param service_name: A name for the App Runner service. It must be unique across all the running App Runner services in your AWS account in the AWS Region . If you don't specify a name, AWS CloudFormation generates a name for your service.
        :param tags: An optional list of metadata items that you can associate with the App Runner service resource. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProps(
            source_configuration=source_configuration,
            auto_scaling_configuration_arn=auto_scaling_configuration_arn,
            encryption_configuration=encryption_configuration,
            health_check_configuration=health_check_configuration,
            instance_configuration=instance_configuration,
            network_configuration=network_configuration,
            observability_configuration=observability_configuration,
            service_name=service_name,
            tags=tags,
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
    @jsii.member(jsii_name="attrServiceArn")
    def attr_service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of this service.

        :cloudformationAttribute: ServiceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceId")
    def attr_service_id(self) -> builtins.str:
        '''An ID that App Runner generated for this service.

        It's unique within the AWS Region .

        :cloudformationAttribute: ServiceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceUrl")
    def attr_service_url(self) -> builtins.str:
        '''A subdomain URL that App Runner generated for this service.

        You can use this URL to access your service web application.

        :cloudformationAttribute: ServiceUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current state of the App Runner service. These particular values mean the following.

        - ``CREATE_FAILED`` – The service failed to create. To troubleshoot this failure, read the failure events and logs, change any parameters that need to be fixed, and retry the call to create the service.

        The failed service isn't usable, and still counts towards your service quota. When you're done analyzing the failure, delete the service.

        - ``DELETE_FAILED`` – The service failed to delete and can't be successfully recovered. Retry the service deletion call to ensure that all related resources are removed.

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
        '''An optional list of metadata items that you can associate with the App Runner service resource.

        A tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Union["CfnService.SourceConfigurationProperty", _IResolvable_da3f097b]:
        '''The source to deploy to the App Runner service.

        It can be a code or an image repository.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        '''
        return typing.cast(typing.Union["CfnService.SourceConfigurationProperty", _IResolvable_da3f097b], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Union["CfnService.SourceConfigurationProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "source_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service.

        If not provided, App Runner associates the latest revision of a default auto scaling configuration.

        Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3``

        Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingConfigurationArn"))

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "auto_scaling_configuration_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnService.EncryptionConfigurationProperty", _IResolvable_da3f097b]]:
        '''An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs.

        By default, App Runner uses an AWS managed key .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnService.EncryptionConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union["CfnService.EncryptionConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "encryption_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckConfiguration")
    def health_check_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnService.HealthCheckConfigurationProperty", _IResolvable_da3f097b]]:
        '''The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnService.HealthCheckConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "healthCheckConfiguration"))

    @health_check_configuration.setter
    def health_check_configuration(
        self,
        value: typing.Optional[typing.Union["CfnService.HealthCheckConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "health_check_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnService.InstanceConfigurationProperty", _IResolvable_da3f097b]]:
        '''The runtime configuration of instances (scaling units) of your service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnService.InstanceConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "instanceConfiguration"))

    @instance_configuration.setter
    def instance_configuration(
        self,
        value: typing.Optional[typing.Union["CfnService.InstanceConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "instance_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnService.NetworkConfigurationProperty", _IResolvable_da3f097b]]:
        '''Configuration settings related to network traffic of the web application that the App Runner service runs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-networkconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnService.NetworkConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Optional[typing.Union["CfnService.NetworkConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "network_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="observabilityConfiguration")
    def observability_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnService.ServiceObservabilityConfigurationProperty", _IResolvable_da3f097b]]:
        '''The observability configuration of your service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-observabilityconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnService.ServiceObservabilityConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "observabilityConfiguration"))

    @observability_configuration.setter
    def observability_configuration(
        self,
        value: typing.Optional[typing.Union["CfnService.ServiceObservabilityConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "observability_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "observabilityConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> typing.Optional[builtins.str]:
        '''A name for the App Runner service.

        It must be unique across all the running App Runner services in your AWS account in the AWS Region .

        If you don't specify a name, AWS CloudFormation generates a name for your service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnService, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_role_arn": "accessRoleArn",
            "connection_arn": "connectionArn",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            access_role_arn: typing.Optional[builtins.str] = None,
            connection_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes resources needed to authenticate access to some source repositories.

            The specific resource depends on the repository provider.

            :param access_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository. It's required for ECR image repositories (but not for ECR Public repositories).
            :param connection_arn: The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository. It's required for GitHub code repositories.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                authentication_configuration_property = apprunner.CfnService.AuthenticationConfigurationProperty(
                    access_role_arn="accessRoleArn",
                    connection_arn="connectionArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.AuthenticationConfigurationProperty.__init__)
                check_type(argname="argument access_role_arn", value=access_role_arn, expected_type=type_hints["access_role_arn"])
                check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if access_role_arn is not None:
                self._values["access_role_arn"] = access_role_arn
            if connection_arn is not None:
                self._values["connection_arn"] = connection_arn

        @builtins.property
        def access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository.

            It's required for ECR image repositories (but not for ECR Public repositories).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-accessrolearn
            '''
            result = self._values.get("access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository.

            It's required for GitHub code repositories.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-connectionarn
            '''
            result = self._values.get("connection_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.CodeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_source": "configurationSource",
            "code_configuration_values": "codeConfigurationValues",
        },
    )
    class CodeConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_source: builtins.str,
            code_configuration_values: typing.Optional[typing.Union[typing.Union["CfnService.CodeConfigurationValuesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the configuration that AWS App Runner uses to build and run an App Runner service from a source code repository.

            :param configuration_source: The source of the App Runner configuration. Values are interpreted as follows:. - ``REPOSITORY`` – App Runner reads configuration values from the ``apprunner.yaml`` file in the source code repository and ignores ``CodeConfigurationValues`` . - ``API`` – App Runner uses configuration values provided in ``CodeConfigurationValues`` and ignores the ``apprunner.yaml`` file in the source code repository.
            :param code_configuration_values: The basic configuration for building and running the App Runner service. Use it to quickly launch an App Runner service without providing a ``apprunner.yaml`` file in the source code repository (or ignoring the file if it exists).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                code_configuration_property = apprunner.CfnService.CodeConfigurationProperty(
                    configuration_source="configurationSource",
                
                    # the properties below are optional
                    code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                        runtime="runtime",
                
                        # the properties below are optional
                        build_command="buildCommand",
                        port="port",
                        runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        start_command="startCommand"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.CodeConfigurationProperty.__init__)
                check_type(argname="argument configuration_source", value=configuration_source, expected_type=type_hints["configuration_source"])
                check_type(argname="argument code_configuration_values", value=code_configuration_values, expected_type=type_hints["code_configuration_values"])
            self._values: typing.Dict[str, typing.Any] = {
                "configuration_source": configuration_source,
            }
            if code_configuration_values is not None:
                self._values["code_configuration_values"] = code_configuration_values

        @builtins.property
        def configuration_source(self) -> builtins.str:
            '''The source of the App Runner configuration. Values are interpreted as follows:.

            - ``REPOSITORY`` – App Runner reads configuration values from the ``apprunner.yaml`` file in the source code repository and ignores ``CodeConfigurationValues`` .
            - ``API`` – App Runner uses configuration values provided in ``CodeConfigurationValues`` and ignores the ``apprunner.yaml`` file in the source code repository.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-configurationsource
            '''
            result = self._values.get("configuration_source")
            assert result is not None, "Required property 'configuration_source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def code_configuration_values(
            self,
        ) -> typing.Optional[typing.Union["CfnService.CodeConfigurationValuesProperty", _IResolvable_da3f097b]]:
            '''The basic configuration for building and running the App Runner service.

            Use it to quickly launch an App Runner service without providing a ``apprunner.yaml`` file in the source code repository (or ignoring the file if it exists).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-codeconfigurationvalues
            '''
            result = self._values.get("code_configuration_values")
            return typing.cast(typing.Optional[typing.Union["CfnService.CodeConfigurationValuesProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.CodeConfigurationValuesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "runtime": "runtime",
            "build_command": "buildCommand",
            "port": "port",
            "runtime_environment_variables": "runtimeEnvironmentVariables",
            "start_command": "startCommand",
        },
    )
    class CodeConfigurationValuesProperty:
        def __init__(
            self,
            *,
            runtime: builtins.str,
            build_command: typing.Optional[builtins.str] = None,
            port: typing.Optional[builtins.str] = None,
            runtime_environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnService.KeyValuePairProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            start_command: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the basic configuration needed for building and running an AWS App Runner service.

            This type doesn't support the full set of possible configuration options. Fur full configuration capabilities, use a ``apprunner.yaml`` file in the source code repository.

            :param runtime: A runtime environment type for building and running an App Runner service. It represents a programming language runtime.
            :param build_command: The command App Runner runs to build your application.
            :param port: The port that your application listens to in the container. Default: ``8080``
            :param runtime_environment_variables: The environment variables that are available to your running App Runner service. An array of key-value pairs. Keys with a prefix of ``AWSAPPRUNNER`` are reserved for system use and aren't valid.
            :param start_command: The command App Runner runs to start your application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                code_configuration_values_property = apprunner.CfnService.CodeConfigurationValuesProperty(
                    runtime="runtime",
                
                    # the properties below are optional
                    build_command="buildCommand",
                    port="port",
                    runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                        name="name",
                        value="value"
                    )],
                    start_command="startCommand"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.CodeConfigurationValuesProperty.__init__)
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument runtime_environment_variables", value=runtime_environment_variables, expected_type=type_hints["runtime_environment_variables"])
                check_type(argname="argument start_command", value=start_command, expected_type=type_hints["start_command"])
            self._values: typing.Dict[str, typing.Any] = {
                "runtime": runtime,
            }
            if build_command is not None:
                self._values["build_command"] = build_command
            if port is not None:
                self._values["port"] = port
            if runtime_environment_variables is not None:
                self._values["runtime_environment_variables"] = runtime_environment_variables
            if start_command is not None:
                self._values["start_command"] = start_command

        @builtins.property
        def runtime(self) -> builtins.str:
            '''A runtime environment type for building and running an App Runner service.

            It represents a programming language runtime.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def build_command(self) -> typing.Optional[builtins.str]:
            '''The command App Runner runs to build your application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-buildcommand
            '''
            result = self._values.get("build_command")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The port that your application listens to in the container.

            Default: ``8080``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_environment_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnService.KeyValuePairProperty", _IResolvable_da3f097b]]]]:
            '''The environment variables that are available to your running App Runner service.

            An array of key-value pairs. Keys with a prefix of ``AWSAPPRUNNER`` are reserved for system use and aren't valid.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentvariables
            '''
            result = self._values.get("runtime_environment_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnService.KeyValuePairProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def start_command(self) -> typing.Optional[builtins.str]:
            '''The command App Runner runs to start your application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-startcommand
            '''
            result = self._values.get("start_command")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.CodeRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "repository_url": "repositoryUrl",
            "source_code_version": "sourceCodeVersion",
            "code_configuration": "codeConfiguration",
        },
    )
    class CodeRepositoryProperty:
        def __init__(
            self,
            *,
            repository_url: builtins.str,
            source_code_version: typing.Union[typing.Union["CfnService.SourceCodeVersionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            code_configuration: typing.Optional[typing.Union[typing.Union["CfnService.CodeConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes a source code repository.

            :param repository_url: The location of the repository that contains the source code.
            :param source_code_version: The version that should be used within the source code repository.
            :param code_configuration: Configuration for building and running the service from a source code repository. .. epigraph:: ``CodeConfiguration`` is required only for ``CreateService`` request.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                code_repository_property = apprunner.CfnService.CodeRepositoryProperty(
                    repository_url="repositoryUrl",
                    source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                        type="type",
                        value="value"
                    ),
                
                    # the properties below are optional
                    code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                        configuration_source="configurationSource",
                
                        # the properties below are optional
                        code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                            runtime="runtime",
                
                            # the properties below are optional
                            build_command="buildCommand",
                            port="port",
                            runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            start_command="startCommand"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.CodeRepositoryProperty.__init__)
                check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
                check_type(argname="argument source_code_version", value=source_code_version, expected_type=type_hints["source_code_version"])
                check_type(argname="argument code_configuration", value=code_configuration, expected_type=type_hints["code_configuration"])
            self._values: typing.Dict[str, typing.Any] = {
                "repository_url": repository_url,
                "source_code_version": source_code_version,
            }
            if code_configuration is not None:
                self._values["code_configuration"] = code_configuration

        @builtins.property
        def repository_url(self) -> builtins.str:
            '''The location of the repository that contains the source code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-repositoryurl
            '''
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_code_version(
            self,
        ) -> typing.Union["CfnService.SourceCodeVersionProperty", _IResolvable_da3f097b]:
            '''The version that should be used within the source code repository.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-sourcecodeversion
            '''
            result = self._values.get("source_code_version")
            assert result is not None, "Required property 'source_code_version' is missing"
            return typing.cast(typing.Union["CfnService.SourceCodeVersionProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def code_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnService.CodeConfigurationProperty", _IResolvable_da3f097b]]:
            '''Configuration for building and running the service from a source code repository.

            .. epigraph::

               ``CodeConfiguration`` is required only for ``CreateService`` request.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-codeconfiguration
            '''
            result = self._values.get("code_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnService.CodeConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.EgressConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "egress_type": "egressType",
            "vpc_connector_arn": "vpcConnectorArn",
        },
    )
    class EgressConfigurationProperty:
        def __init__(
            self,
            *,
            egress_type: builtins.str,
            vpc_connector_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes configuration settings related to outbound network traffic of an AWS App Runner service.

            :param egress_type: The type of egress configuration. Set to ``DEFAULT`` for access to resources hosted on public networks. Set to ``VPC`` to associate your service to a custom VPC specified by ``VpcConnectorArn`` .
            :param vpc_connector_arn: The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to associate with your App Runner service. Only valid when ``EgressType = VPC`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                egress_configuration_property = apprunner.CfnService.EgressConfigurationProperty(
                    egress_type="egressType",
                
                    # the properties below are optional
                    vpc_connector_arn="vpcConnectorArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.EgressConfigurationProperty.__init__)
                check_type(argname="argument egress_type", value=egress_type, expected_type=type_hints["egress_type"])
                check_type(argname="argument vpc_connector_arn", value=vpc_connector_arn, expected_type=type_hints["vpc_connector_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "egress_type": egress_type,
            }
            if vpc_connector_arn is not None:
                self._values["vpc_connector_arn"] = vpc_connector_arn

        @builtins.property
        def egress_type(self) -> builtins.str:
            '''The type of egress configuration.

            Set to ``DEFAULT`` for access to resources hosted on public networks.

            Set to ``VPC`` to associate your service to a custom VPC specified by ``VpcConnectorArn`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-egresstype
            '''
            result = self._values.get("egress_type")
            assert result is not None, "Required property 'egress_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_connector_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to associate with your App Runner service.

            Only valid when ``EgressType = VPC`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-vpcconnectorarn
            '''
            result = self._values.get("vpc_connector_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EgressConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(self, *, kms_key: builtins.str) -> None:
            '''Describes a custom encryption key that AWS App Runner uses to encrypt copies of the source repository and service logs.

            :param kms_key: The ARN of the KMS key that's used for encryption.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                encryption_configuration_property = apprunner.CfnService.EncryptionConfigurationProperty(
                    kms_key="kmsKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.EncryptionConfigurationProperty.__init__)
                check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            self._values: typing.Dict[str, typing.Any] = {
                "kms_key": kms_key,
            }

        @builtins.property
        def kms_key(self) -> builtins.str:
            '''The ARN of the KMS key that's used for encryption.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html#cfn-apprunner-service-encryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
            assert result is not None, "Required property 'kms_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.HealthCheckConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "healthy_threshold": "healthyThreshold",
            "interval": "interval",
            "path": "path",
            "protocol": "protocol",
            "timeout": "timeout",
            "unhealthy_threshold": "unhealthyThreshold",
        },
    )
    class HealthCheckConfigurationProperty:
        def __init__(
            self,
            *,
            healthy_threshold: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            path: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
            timeout: typing.Optional[jsii.Number] = None,
            unhealthy_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the settings for the health check that AWS App Runner performs to monitor the health of a service.

            :param healthy_threshold: The number of consecutive checks that must succeed before App Runner decides that the service is healthy. Default: ``1``
            :param interval: The time interval, in seconds, between health checks. Default: ``5``
            :param path: The URL that health check requests are sent to. ``Path`` is only applicable when you set ``Protocol`` to ``HTTP`` . Default: ``"/"``
            :param protocol: The IP protocol that App Runner uses to perform health checks for your service. If you set ``Protocol`` to ``HTTP`` , App Runner sends health check requests to the HTTP path specified by ``Path`` . Default: ``TCP``
            :param timeout: The time, in seconds, to wait for a health check response before deciding it failed. Default: ``2``
            :param unhealthy_threshold: The number of consecutive checks that must fail before App Runner decides that the service is unhealthy. Default: ``5``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                health_check_configuration_property = apprunner.CfnService.HealthCheckConfigurationProperty(
                    healthy_threshold=123,
                    interval=123,
                    path="path",
                    protocol="protocol",
                    timeout=123,
                    unhealthy_threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.HealthCheckConfigurationProperty.__init__)
                check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
                check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
            self._values: typing.Dict[str, typing.Any] = {}
            if healthy_threshold is not None:
                self._values["healthy_threshold"] = healthy_threshold
            if interval is not None:
                self._values["interval"] = interval
            if path is not None:
                self._values["path"] = path
            if protocol is not None:
                self._values["protocol"] = protocol
            if timeout is not None:
                self._values["timeout"] = timeout
            if unhealthy_threshold is not None:
                self._values["unhealthy_threshold"] = unhealthy_threshold

        @builtins.property
        def healthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive checks that must succeed before App Runner decides that the service is healthy.

            Default: ``1``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-healthythreshold
            '''
            result = self._values.get("healthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''The time interval, in seconds, between health checks.

            Default: ``5``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The URL that health check requests are sent to.

            ``Path`` is only applicable when you set ``Protocol`` to ``HTTP`` .

            Default: ``"/"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The IP protocol that App Runner uses to perform health checks for your service.

            If you set ``Protocol`` to ``HTTP`` , App Runner sends health check requests to the HTTP path specified by ``Path`` .

            Default: ``TCP``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''The time, in seconds, to wait for a health check response before deciding it failed.

            Default: ``2``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive checks that must fail before App Runner decides that the service is unhealthy.

            Default: ``5``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-unhealthythreshold
            '''
            result = self._values.get("unhealthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.ImageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port": "port",
            "runtime_environment_variables": "runtimeEnvironmentVariables",
            "start_command": "startCommand",
        },
    )
    class ImageConfigurationProperty:
        def __init__(
            self,
            *,
            port: typing.Optional[builtins.str] = None,
            runtime_environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnService.KeyValuePairProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            start_command: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration that AWS App Runner uses to run an App Runner service using an image pulled from a source image repository.

            :param port: The port that your application listens to in the container. Default: ``8080``
            :param runtime_environment_variables: Environment variables that are available to your running App Runner service. An array of key-value pairs. Keys with a prefix of ``AWSAPPRUNNER`` are reserved for system use and aren't valid.
            :param start_command: An optional command that App Runner runs to start the application in the source image. If specified, this command overrides the Docker image’s default start command.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                image_configuration_property = apprunner.CfnService.ImageConfigurationProperty(
                    port="port",
                    runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                        name="name",
                        value="value"
                    )],
                    start_command="startCommand"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.ImageConfigurationProperty.__init__)
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument runtime_environment_variables", value=runtime_environment_variables, expected_type=type_hints["runtime_environment_variables"])
                check_type(argname="argument start_command", value=start_command, expected_type=type_hints["start_command"])
            self._values: typing.Dict[str, typing.Any] = {}
            if port is not None:
                self._values["port"] = port
            if runtime_environment_variables is not None:
                self._values["runtime_environment_variables"] = runtime_environment_variables
            if start_command is not None:
                self._values["start_command"] = start_command

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The port that your application listens to in the container.

            Default: ``8080``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_environment_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnService.KeyValuePairProperty", _IResolvable_da3f097b]]]]:
            '''Environment variables that are available to your running App Runner service.

            An array of key-value pairs. Keys with a prefix of ``AWSAPPRUNNER`` are reserved for system use and aren't valid.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables
            '''
            result = self._values.get("runtime_environment_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnService.KeyValuePairProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def start_command(self) -> typing.Optional[builtins.str]:
            '''An optional command that App Runner runs to start the application in the source image.

            If specified, this command overrides the Docker image’s default start command.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-startcommand
            '''
            result = self._values.get("start_command")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.ImageRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_identifier": "imageIdentifier",
            "image_repository_type": "imageRepositoryType",
            "image_configuration": "imageConfiguration",
        },
    )
    class ImageRepositoryProperty:
        def __init__(
            self,
            *,
            image_identifier: builtins.str,
            image_repository_type: builtins.str,
            image_configuration: typing.Optional[typing.Union[typing.Union["CfnService.ImageConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes a source image repository.

            :param image_identifier: The identifier of an image. For an image in Amazon Elastic Container Registry (Amazon ECR), this is an image name. For the image name format, see `Pulling an image <https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html>`_ in the *Amazon ECR User Guide* .
            :param image_repository_type: The type of the image repository. This reflects the repository provider and whether the repository is private or public.
            :param image_configuration: Configuration for running the identified image.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                image_repository_property = apprunner.CfnService.ImageRepositoryProperty(
                    image_identifier="imageIdentifier",
                    image_repository_type="imageRepositoryType",
                
                    # the properties below are optional
                    image_configuration=apprunner.CfnService.ImageConfigurationProperty(
                        port="port",
                        runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        start_command="startCommand"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.ImageRepositoryProperty.__init__)
                check_type(argname="argument image_identifier", value=image_identifier, expected_type=type_hints["image_identifier"])
                check_type(argname="argument image_repository_type", value=image_repository_type, expected_type=type_hints["image_repository_type"])
                check_type(argname="argument image_configuration", value=image_configuration, expected_type=type_hints["image_configuration"])
            self._values: typing.Dict[str, typing.Any] = {
                "image_identifier": image_identifier,
                "image_repository_type": image_repository_type,
            }
            if image_configuration is not None:
                self._values["image_configuration"] = image_configuration

        @builtins.property
        def image_identifier(self) -> builtins.str:
            '''The identifier of an image.

            For an image in Amazon Elastic Container Registry (Amazon ECR), this is an image name. For the image name format, see `Pulling an image <https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html>`_ in the *Amazon ECR User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageidentifier
            '''
            result = self._values.get("image_identifier")
            assert result is not None, "Required property 'image_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_repository_type(self) -> builtins.str:
            '''The type of the image repository.

            This reflects the repository provider and whether the repository is private or public.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imagerepositorytype
            '''
            result = self._values.get("image_repository_type")
            assert result is not None, "Required property 'image_repository_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnService.ImageConfigurationProperty", _IResolvable_da3f097b]]:
            '''Configuration for running the identified image.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageconfiguration
            '''
            result = self._values.get("image_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnService.ImageConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.InstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu": "cpu",
            "instance_role_arn": "instanceRoleArn",
            "memory": "memory",
        },
    )
    class InstanceConfigurationProperty:
        def __init__(
            self,
            *,
            cpu: typing.Optional[builtins.str] = None,
            instance_role_arn: typing.Optional[builtins.str] = None,
            memory: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the runtime configuration of an AWS App Runner service instance (scaling unit).

            :param cpu: The number of CPU units reserved for each instance of your App Runner service. Default: ``1 vCPU``
            :param instance_role_arn: The Amazon Resource Name (ARN) of an IAM role that provides permissions to your App Runner service. These are permissions that your code needs when it calls any AWS APIs.
            :param memory: The amount of memory, in MB or GB, reserved for each instance of your App Runner service. Default: ``2 GB``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                instance_configuration_property = apprunner.CfnService.InstanceConfigurationProperty(
                    cpu="cpu",
                    instance_role_arn="instanceRoleArn",
                    memory="memory"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.InstanceConfigurationProperty.__init__)
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument instance_role_arn", value=instance_role_arn, expected_type=type_hints["instance_role_arn"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            self._values: typing.Dict[str, typing.Any] = {}
            if cpu is not None:
                self._values["cpu"] = cpu
            if instance_role_arn is not None:
                self._values["instance_role_arn"] = instance_role_arn
            if memory is not None:
                self._values["memory"] = memory

        @builtins.property
        def cpu(self) -> typing.Optional[builtins.str]:
            '''The number of CPU units reserved for each instance of your App Runner service.

            Default: ``1 vCPU``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-cpu
            '''
            result = self._values.get("cpu")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of an IAM role that provides permissions to your App Runner service.

            These are permissions that your code needs when it calls any AWS APIs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-instancerolearn
            '''
            result = self._values.get("instance_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def memory(self) -> typing.Optional[builtins.str]:
            '''The amount of memory, in MB or GB, reserved for each instance of your App Runner service.

            Default: ``2 GB``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.KeyValuePairProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class KeyValuePairProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a key-value pair, which is a string-to-string mapping.

            :param name: The key name string to map to a value.
            :param value: The value string to which the key name is mapped.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                key_value_pair_property = apprunner.CfnService.KeyValuePairProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.KeyValuePairProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The key name string to map to a value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value string to which the key name is mapped.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValuePairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"egress_configuration": "egressConfiguration"},
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            egress_configuration: typing.Union[typing.Union["CfnService.EgressConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''Describes configuration settings related to network traffic of an AWS App Runner service.

            Consists of embedded objects for each configurable network feature.

            :param egress_configuration: Network configuration settings for outbound message traffic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                network_configuration_property = apprunner.CfnService.NetworkConfigurationProperty(
                    egress_configuration=apprunner.CfnService.EgressConfigurationProperty(
                        egress_type="egressType",
                
                        # the properties below are optional
                        vpc_connector_arn="vpcConnectorArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.NetworkConfigurationProperty.__init__)
                check_type(argname="argument egress_configuration", value=egress_configuration, expected_type=type_hints["egress_configuration"])
            self._values: typing.Dict[str, typing.Any] = {
                "egress_configuration": egress_configuration,
            }

        @builtins.property
        def egress_configuration(
            self,
        ) -> typing.Union["CfnService.EgressConfigurationProperty", _IResolvable_da3f097b]:
            '''Network configuration settings for outbound message traffic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-egressconfiguration
            '''
            result = self._values.get("egress_configuration")
            assert result is not None, "Required property 'egress_configuration' is missing"
            return typing.cast(typing.Union["CfnService.EgressConfigurationProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.ServiceObservabilityConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "observability_enabled": "observabilityEnabled",
            "observability_configuration_arn": "observabilityConfigurationArn",
        },
    )
    class ServiceObservabilityConfigurationProperty:
        def __init__(
            self,
            *,
            observability_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            observability_configuration_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the observability configuration of an AWS App Runner service.

            These are additional observability features, like tracing, that you choose to enable. They're configured in a separate resource that you associate with your service.

            :param observability_enabled: When ``true`` , an observability configuration resource is associated with the service, and an ``ObservabilityConfigurationArn`` is specified.
            :param observability_configuration_arn: The Amazon Resource Name (ARN) of the observability configuration that is associated with the service. Specified only when ``ObservabilityEnabled`` is ``true`` . Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/3`` Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                service_observability_configuration_property = apprunner.CfnService.ServiceObservabilityConfigurationProperty(
                    observability_enabled=False,
                
                    # the properties below are optional
                    observability_configuration_arn="observabilityConfigurationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.ServiceObservabilityConfigurationProperty.__init__)
                check_type(argname="argument observability_enabled", value=observability_enabled, expected_type=type_hints["observability_enabled"])
                check_type(argname="argument observability_configuration_arn", value=observability_configuration_arn, expected_type=type_hints["observability_configuration_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "observability_enabled": observability_enabled,
            }
            if observability_configuration_arn is not None:
                self._values["observability_configuration_arn"] = observability_configuration_arn

        @builtins.property
        def observability_enabled(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''When ``true`` , an observability configuration resource is associated with the service, and an ``ObservabilityConfigurationArn`` is specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityenabled
            '''
            result = self._values.get("observability_enabled")
            assert result is not None, "Required property 'observability_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def observability_configuration_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the observability configuration that is associated with the service.

            Specified only when ``ObservabilityEnabled`` is ``true`` .

            Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/3``

            Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityconfigurationarn
            '''
            result = self._values.get("observability_configuration_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceObservabilityConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.SourceCodeVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class SourceCodeVersionProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''Identifies a version of code that AWS App Runner refers to within a source code repository.

            :param type: The type of version identifier. For a git-based repository, branches represent versions.
            :param value: A source code version. For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                source_code_version_property = apprunner.CfnService.SourceCodeVersionProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.SourceCodeVersionProperty.__init__)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of version identifier.

            For a git-based repository, branches represent versions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''A source code version.

            For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceCodeVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "auto_deployments_enabled": "autoDeploymentsEnabled",
            "code_repository": "codeRepository",
            "image_repository": "imageRepository",
        },
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Optional[typing.Union[typing.Union["CfnService.AuthenticationConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            auto_deployments_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            code_repository: typing.Optional[typing.Union[typing.Union["CfnService.CodeRepositoryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            image_repository: typing.Optional[typing.Union[typing.Union["CfnService.ImageRepositoryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the source deployed to an AWS App Runner service.

            It can be a code or an image repository.

            :param authentication_configuration: Describes the resources that are needed to authenticate access to some source repositories.
            :param auto_deployments_enabled: If ``true`` , continuous integration from the source repository is enabled for the App Runner service. Each repository change (including any source code commit or new image version) starts a deployment. Default: App Runner sets to ``false`` for a source image that uses an ECR Public repository or an ECR repository that's in an AWS account other than the one that the service is in. App Runner sets to ``true`` in all other cases (which currently include a source code repository or a source image using a same-account ECR repository).
            :param code_repository: The description of a source code repository. You must provide either this member or ``ImageRepository`` (but not both).
            :param image_repository: The description of a source image repository. You must provide either this member or ``CodeRepository`` (but not both).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                source_configuration_property = apprunner.CfnService.SourceConfigurationProperty(
                    authentication_configuration=apprunner.CfnService.AuthenticationConfigurationProperty(
                        access_role_arn="accessRoleArn",
                        connection_arn="connectionArn"
                    ),
                    auto_deployments_enabled=False,
                    code_repository=apprunner.CfnService.CodeRepositoryProperty(
                        repository_url="repositoryUrl",
                        source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                            type="type",
                            value="value"
                        ),
                
                        # the properties below are optional
                        code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                            configuration_source="configurationSource",
                
                            # the properties below are optional
                            code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                                runtime="runtime",
                
                                # the properties below are optional
                                build_command="buildCommand",
                                port="port",
                                runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                    name="name",
                                    value="value"
                                )],
                                start_command="startCommand"
                            )
                        )
                    ),
                    image_repository=apprunner.CfnService.ImageRepositoryProperty(
                        image_identifier="imageIdentifier",
                        image_repository_type="imageRepositoryType",
                
                        # the properties below are optional
                        image_configuration=apprunner.CfnService.ImageConfigurationProperty(
                            port="port",
                            runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            start_command="startCommand"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnService.SourceConfigurationProperty.__init__)
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument auto_deployments_enabled", value=auto_deployments_enabled, expected_type=type_hints["auto_deployments_enabled"])
                check_type(argname="argument code_repository", value=code_repository, expected_type=type_hints["code_repository"])
                check_type(argname="argument image_repository", value=image_repository, expected_type=type_hints["image_repository"])
            self._values: typing.Dict[str, typing.Any] = {}
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if auto_deployments_enabled is not None:
                self._values["auto_deployments_enabled"] = auto_deployments_enabled
            if code_repository is not None:
                self._values["code_repository"] = code_repository
            if image_repository is not None:
                self._values["image_repository"] = image_repository

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnService.AuthenticationConfigurationProperty", _IResolvable_da3f097b]]:
            '''Describes the resources that are needed to authenticate access to some source repositories.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnService.AuthenticationConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def auto_deployments_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , continuous integration from the source repository is enabled for the App Runner service.

            Each repository change (including any source code commit or new image version) starts a deployment.

            Default: App Runner sets to ``false`` for a source image that uses an ECR Public repository or an ECR repository that's in an AWS account other than the one that the service is in. App Runner sets to ``true`` in all other cases (which currently include a source code repository or a source image using a same-account ECR repository).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-autodeploymentsenabled
            '''
            result = self._values.get("auto_deployments_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def code_repository(
            self,
        ) -> typing.Optional[typing.Union["CfnService.CodeRepositoryProperty", _IResolvable_da3f097b]]:
            '''The description of a source code repository.

            You must provide either this member or ``ImageRepository`` (but not both).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-coderepository
            '''
            result = self._values.get("code_repository")
            return typing.cast(typing.Optional[typing.Union["CfnService.CodeRepositoryProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def image_repository(
            self,
        ) -> typing.Optional[typing.Union["CfnService.ImageRepositoryProperty", _IResolvable_da3f097b]]:
            '''The description of a source image repository.

            You must provide either this member or ``CodeRepository`` (but not both).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-imagerepository
            '''
            result = self._values.get("image_repository")
            return typing.cast(typing.Optional[typing.Union["CfnService.ImageRepositoryProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apprunner.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "source_configuration": "sourceConfiguration",
        "auto_scaling_configuration_arn": "autoScalingConfigurationArn",
        "encryption_configuration": "encryptionConfiguration",
        "health_check_configuration": "healthCheckConfiguration",
        "instance_configuration": "instanceConfiguration",
        "network_configuration": "networkConfiguration",
        "observability_configuration": "observabilityConfiguration",
        "service_name": "serviceName",
        "tags": "tags",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        source_configuration: typing.Union[typing.Union[CfnService.SourceConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[typing.Union[CfnService.EncryptionConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        health_check_configuration: typing.Optional[typing.Union[typing.Union[CfnService.HealthCheckConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        instance_configuration: typing.Optional[typing.Union[typing.Union[CfnService.InstanceConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        network_configuration: typing.Optional[typing.Union[typing.Union[CfnService.NetworkConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        observability_configuration: typing.Optional[typing.Union[typing.Union[CfnService.ServiceObservabilityConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        service_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnService``.

        :param source_configuration: The source to deploy to the App Runner service. It can be a code or an image repository.
        :param auto_scaling_configuration_arn: The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration. Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3`` Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability``
        :param encryption_configuration: An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed key .
        :param health_check_configuration: The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.
        :param instance_configuration: The runtime configuration of instances (scaling units) of your service.
        :param network_configuration: Configuration settings related to network traffic of the web application that the App Runner service runs.
        :param observability_configuration: The observability configuration of your service.
        :param service_name: A name for the App Runner service. It must be unique across all the running App Runner services in your AWS account in the AWS Region . If you don't specify a name, AWS CloudFormation generates a name for your service.
        :param tags: An optional list of metadata items that you can associate with the App Runner service resource. A tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apprunner as apprunner
            
            cfn_service_props = apprunner.CfnServiceProps(
                source_configuration=apprunner.CfnService.SourceConfigurationProperty(
                    authentication_configuration=apprunner.CfnService.AuthenticationConfigurationProperty(
                        access_role_arn="accessRoleArn",
                        connection_arn="connectionArn"
                    ),
                    auto_deployments_enabled=False,
                    code_repository=apprunner.CfnService.CodeRepositoryProperty(
                        repository_url="repositoryUrl",
                        source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                            type="type",
                            value="value"
                        ),
            
                        # the properties below are optional
                        code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                            configuration_source="configurationSource",
            
                            # the properties below are optional
                            code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                                runtime="runtime",
            
                                # the properties below are optional
                                build_command="buildCommand",
                                port="port",
                                runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                    name="name",
                                    value="value"
                                )],
                                start_command="startCommand"
                            )
                        )
                    ),
                    image_repository=apprunner.CfnService.ImageRepositoryProperty(
                        image_identifier="imageIdentifier",
                        image_repository_type="imageRepositoryType",
            
                        # the properties below are optional
                        image_configuration=apprunner.CfnService.ImageConfigurationProperty(
                            port="port",
                            runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            start_command="startCommand"
                        )
                    )
                ),
            
                # the properties below are optional
                auto_scaling_configuration_arn="autoScalingConfigurationArn",
                encryption_configuration=apprunner.CfnService.EncryptionConfigurationProperty(
                    kms_key="kmsKey"
                ),
                health_check_configuration=apprunner.CfnService.HealthCheckConfigurationProperty(
                    healthy_threshold=123,
                    interval=123,
                    path="path",
                    protocol="protocol",
                    timeout=123,
                    unhealthy_threshold=123
                ),
                instance_configuration=apprunner.CfnService.InstanceConfigurationProperty(
                    cpu="cpu",
                    instance_role_arn="instanceRoleArn",
                    memory="memory"
                ),
                network_configuration=apprunner.CfnService.NetworkConfigurationProperty(
                    egress_configuration=apprunner.CfnService.EgressConfigurationProperty(
                        egress_type="egressType",
            
                        # the properties below are optional
                        vpc_connector_arn="vpcConnectorArn"
                    )
                ),
                observability_configuration=apprunner.CfnService.ServiceObservabilityConfigurationProperty(
                    observability_enabled=False,
            
                    # the properties below are optional
                    observability_configuration_arn="observabilityConfigurationArn"
                ),
                service_name="serviceName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnServiceProps.__init__)
            check_type(argname="argument source_configuration", value=source_configuration, expected_type=type_hints["source_configuration"])
            check_type(argname="argument auto_scaling_configuration_arn", value=auto_scaling_configuration_arn, expected_type=type_hints["auto_scaling_configuration_arn"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument health_check_configuration", value=health_check_configuration, expected_type=type_hints["health_check_configuration"])
            check_type(argname="argument instance_configuration", value=instance_configuration, expected_type=type_hints["instance_configuration"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument observability_configuration", value=observability_configuration, expected_type=type_hints["observability_configuration"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_configuration": source_configuration,
        }
        if auto_scaling_configuration_arn is not None:
            self._values["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if health_check_configuration is not None:
            self._values["health_check_configuration"] = health_check_configuration
        if instance_configuration is not None:
            self._values["instance_configuration"] = instance_configuration
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if observability_configuration is not None:
            self._values["observability_configuration"] = observability_configuration
        if service_name is not None:
            self._values["service_name"] = service_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Union[CfnService.SourceConfigurationProperty, _IResolvable_da3f097b]:
        '''The source to deploy to the App Runner service.

        It can be a code or an image repository.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        assert result is not None, "Required property 'source_configuration' is missing"
        return typing.cast(typing.Union[CfnService.SourceConfigurationProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service.

        If not provided, App Runner associates the latest revision of a default auto scaling configuration.

        Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3``

        Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        '''
        result = self._values.get("auto_scaling_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnService.EncryptionConfigurationProperty, _IResolvable_da3f097b]]:
        '''An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs.

        By default, App Runner uses an AWS managed key .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnService.EncryptionConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def health_check_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnService.HealthCheckConfigurationProperty, _IResolvable_da3f097b]]:
        '''The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        '''
        result = self._values.get("health_check_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnService.HealthCheckConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnService.InstanceConfigurationProperty, _IResolvable_da3f097b]]:
        '''The runtime configuration of instances (scaling units) of your service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        '''
        result = self._values.get("instance_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnService.InstanceConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnService.NetworkConfigurationProperty, _IResolvable_da3f097b]]:
        '''Configuration settings related to network traffic of the web application that the App Runner service runs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnService.NetworkConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def observability_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnService.ServiceObservabilityConfigurationProperty, _IResolvable_da3f097b]]:
        '''The observability configuration of your service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-observabilityconfiguration
        '''
        result = self._values.get("observability_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnService.ServiceObservabilityConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''A name for the App Runner service.

        It must be unique across all the running App Runner services in your AWS account in the AWS Region .

        If you don't specify a name, AWS CloudFormation generates a name for your service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the App Runner service resource.

        A tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnVpcConnector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apprunner.CfnVpcConnector",
):
    '''A CloudFormation ``AWS::AppRunner::VpcConnector``.

    Specify an AWS App Runner VPC connector by using the ``AWS::AppRunner::VpcConnector`` resource in an AWS CloudFormation template.

    The ``AWS::AppRunner::VpcConnector`` resource is an AWS App Runner resource type that specifies an App Runner VPC connector.

    App Runner requires this resource when you want to associate your App Runner service to a custom Amazon Virtual Private Cloud ( Amazon VPC ).

    :cloudformationResource: AWS::AppRunner::VpcConnector
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apprunner as apprunner
        
        cfn_vpc_connector = apprunner.CfnVpcConnector(self, "MyCfnVpcConnector",
            subnets=["subnets"],
        
            # the properties below are optional
            security_groups=["securityGroups"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_connector_name="vpcConnectorName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        subnets: typing.Sequence[builtins.str],
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        vpc_connector_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::AppRunner::VpcConnector``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param subnets: A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify. .. epigraph:: App Runner currently only provides support for IPv4.
        :param security_groups: A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
        :param tags: A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
        :param vpc_connector_name: A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVpcConnector.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcConnectorProps(
            subnets=subnets,
            security_groups=security_groups,
            tags=tags,
            vpc_connector_name=vpc_connector_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVpcConnector.inspect)
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
            type_hints = typing.get_type_hints(CfnVpcConnector._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVpcConnectorArn")
    def attr_vpc_connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of this VPC connector.

        :cloudformationAttribute: VpcConnectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcConnectorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVpcConnectorRevision")
    def attr_vpc_connector_revision(self) -> jsii.Number:
        '''The revision of this VPC connector.

        It's unique among all the active connectors ( ``"Status": "ACTIVE"`` ) that share the same ``Name`` .
        .. epigraph::

           At this time, App Runner supports only one revision per name.

        :cloudformationAttribute: VpcConnectorRevision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVpcConnectorRevision"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''A list of metadata items that you can associate with your VPC connector resource.

        A tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        '''A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC.

        Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
        .. epigraph::

           App Runner currently only provides support for IPv4.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-subnets
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVpcConnector, "subnets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets.

        If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-securitygroups
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVpcConnector, "security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConnectorName")
    def vpc_connector_name(self) -> typing.Optional[builtins.str]:
        '''A name for the VPC connector.

        If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-vpcconnectorname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcConnectorName"))

    @vpc_connector_name.setter
    def vpc_connector_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVpcConnector, "vpc_connector_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConnectorName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apprunner.CfnVpcConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "security_groups": "securityGroups",
        "tags": "tags",
        "vpc_connector_name": "vpcConnectorName",
    },
)
class CfnVpcConnectorProps:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        vpc_connector_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVpcConnector``.

        :param subnets: A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify. .. epigraph:: App Runner currently only provides support for IPv4.
        :param security_groups: A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
        :param tags: A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
        :param vpc_connector_name: A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apprunner as apprunner
            
            cfn_vpc_connector_props = apprunner.CfnVpcConnectorProps(
                subnets=["subnets"],
            
                # the properties below are optional
                security_groups=["securityGroups"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_connector_name="vpcConnectorName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVpcConnectorProps.__init__)
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_connector_name", value=vpc_connector_name, expected_type=type_hints["vpc_connector_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnets": subnets,
        }
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if tags is not None:
            self._values["tags"] = tags
        if vpc_connector_name is not None:
            self._values["vpc_connector_name"] = vpc_connector_name

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC.

        Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
        .. epigraph::

           App Runner currently only provides support for IPv4.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-subnets
        '''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets.

        If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-securitygroups
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of metadata items that you can associate with your VPC connector resource.

        A tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_connector_name(self) -> typing.Optional[builtins.str]:
        '''A name for the VPC connector.

        If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-vpcconnectorname
        '''
        result = self._values.get("vpc_connector_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnObservabilityConfiguration",
    "CfnObservabilityConfigurationProps",
    "CfnService",
    "CfnServiceProps",
    "CfnVpcConnector",
    "CfnVpcConnectorProps",
]

publication.publish()
