'''
# AWS::KafkaConnect Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_kafkaconnect as kafkaconnect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for KafkaConnect construct libraries](https://constructs.dev/search?q=kafkaconnect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::KafkaConnect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KafkaConnect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::KafkaConnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KafkaConnect.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnConnector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector",
):
    '''A CloudFormation ``AWS::KafkaConnect::Connector``.

    Creates a connector using the specified properties.

    :cloudformationResource: AWS::KafkaConnect::Connector
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kafkaconnect as kafkaconnect
        
        cfn_connector = kafkaconnect.CfnConnector(self, "MyCfnConnector",
            capacity=kafkaconnect.CfnConnector.CapacityProperty(
                auto_scaling=kafkaconnect.CfnConnector.AutoScalingProperty(
                    max_worker_count=123,
                    mcu_count=123,
                    min_worker_count=123,
                    scale_in_policy=kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                        cpu_utilization_percentage=123
                    ),
                    scale_out_policy=kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                        cpu_utilization_percentage=123
                    )
                ),
                provisioned_capacity=kafkaconnect.CfnConnector.ProvisionedCapacityProperty(
                    worker_count=123,
        
                    # the properties below are optional
                    mcu_count=123
                )
            ),
            connector_configuration={
                "connector_configuration_key": "connectorConfiguration"
            },
            connector_name="connectorName",
            kafka_cluster=kafkaconnect.CfnConnector.KafkaClusterProperty(
                apache_kafka_cluster=kafkaconnect.CfnConnector.ApacheKafkaClusterProperty(
                    bootstrap_servers="bootstrapServers",
                    vpc=kafkaconnect.CfnConnector.VpcProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            ),
            kafka_cluster_client_authentication=kafkaconnect.CfnConnector.KafkaClusterClientAuthenticationProperty(
                authentication_type="authenticationType"
            ),
            kafka_cluster_encryption_in_transit=kafkaconnect.CfnConnector.KafkaClusterEncryptionInTransitProperty(
                encryption_type="encryptionType"
            ),
            kafka_connect_version="kafkaConnectVersion",
            plugins=[kafkaconnect.CfnConnector.PluginProperty(
                custom_plugin=kafkaconnect.CfnConnector.CustomPluginProperty(
                    custom_plugin_arn="customPluginArn",
                    revision=123
                )
            )],
            service_execution_role_arn="serviceExecutionRoleArn",
        
            # the properties below are optional
            connector_description="connectorDescription",
            log_delivery=kafkaconnect.CfnConnector.LogDeliveryProperty(
                worker_log_delivery=kafkaconnect.CfnConnector.WorkerLogDeliveryProperty(
                    cloud_watch_logs=kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                        enabled=False,
        
                        # the properties below are optional
                        log_group="logGroup"
                    ),
                    firehose=kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                        enabled=False,
        
                        # the properties below are optional
                        delivery_stream="deliveryStream"
                    ),
                    s3=kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                        enabled=False,
        
                        # the properties below are optional
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            ),
            worker_configuration=kafkaconnect.CfnConnector.WorkerConfigurationProperty(
                revision=123,
                worker_configuration_arn="workerConfigurationArn"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        capacity: typing.Union[typing.Union["CfnConnector.CapacityProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        connector_configuration: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
        connector_name: builtins.str,
        kafka_cluster: typing.Union[typing.Union["CfnConnector.KafkaClusterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        kafka_cluster_client_authentication: typing.Union[typing.Union["CfnConnector.KafkaClusterClientAuthenticationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        kafka_cluster_encryption_in_transit: typing.Union[typing.Union["CfnConnector.KafkaClusterEncryptionInTransitProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        kafka_connect_version: builtins.str,
        plugins: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnConnector.PluginProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        service_execution_role_arn: builtins.str,
        connector_description: typing.Optional[builtins.str] = None,
        log_delivery: typing.Optional[typing.Union[typing.Union["CfnConnector.LogDeliveryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        worker_configuration: typing.Optional[typing.Union[typing.Union["CfnConnector.WorkerConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::KafkaConnect::Connector``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param capacity: The connector's compute capacity settings.
        :param connector_configuration: The configuration of the connector.
        :param connector_name: The name of the connector.
        :param kafka_cluster: The details of the Apache Kafka cluster to which the connector is connected.
        :param kafka_cluster_client_authentication: The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used.
        :param kafka_cluster_encryption_in_transit: Details of encryption in transit to the Apache Kafka cluster.
        :param kafka_connect_version: The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.
        :param plugins: Specifies which plugin to use for the connector. You must specify a single-element list. Amazon MSK Connect does not currently support specifying multiple plugins.
        :param service_execution_role_arn: The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.
        :param connector_description: The description of the connector.
        :param log_delivery: The settings for delivering connector logs to Amazon CloudWatch Logs.
        :param worker_configuration: The worker configurations that are in use with the connector.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnector.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorProps(
            capacity=capacity,
            connector_configuration=connector_configuration,
            connector_name=connector_name,
            kafka_cluster=kafka_cluster,
            kafka_cluster_client_authentication=kafka_cluster_client_authentication,
            kafka_cluster_encryption_in_transit=kafka_cluster_encryption_in_transit,
            kafka_connect_version=kafka_connect_version,
            plugins=plugins,
            service_execution_role_arn=service_execution_role_arn,
            connector_description=connector_description,
            log_delivery=log_delivery,
            worker_configuration=worker_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnector.inspect)
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
            type_hints = typing.get_type_hints(CfnConnector._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrConnectorArn")
    def attr_connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the newly created connector.

        :cloudformationAttribute: ConnectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="capacity")
    def capacity(
        self,
    ) -> typing.Union["CfnConnector.CapacityProperty", _IResolvable_da3f097b]:
        '''The connector's compute capacity settings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-capacity
        '''
        return typing.cast(typing.Union["CfnConnector.CapacityProperty", _IResolvable_da3f097b], jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(
        self,
        value: typing.Union["CfnConnector.CapacityProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectorConfiguration")
    def connector_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
        '''The configuration of the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorconfiguration
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "connectorConfiguration"))

    @connector_configuration.setter
    def connector_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "connector_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectorName")
    def connector_name(self) -> builtins.str:
        '''The name of the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorname
        '''
        return typing.cast(builtins.str, jsii.get(self, "connectorName"))

    @connector_name.setter
    def connector_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "connector_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kafkaCluster")
    def kafka_cluster(
        self,
    ) -> typing.Union["CfnConnector.KafkaClusterProperty", _IResolvable_da3f097b]:
        '''The details of the Apache Kafka cluster to which the connector is connected.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkacluster
        '''
        return typing.cast(typing.Union["CfnConnector.KafkaClusterProperty", _IResolvable_da3f097b], jsii.get(self, "kafkaCluster"))

    @kafka_cluster.setter
    def kafka_cluster(
        self,
        value: typing.Union["CfnConnector.KafkaClusterProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "kafka_cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaCluster", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kafkaClusterClientAuthentication")
    def kafka_cluster_client_authentication(
        self,
    ) -> typing.Union["CfnConnector.KafkaClusterClientAuthenticationProperty", _IResolvable_da3f097b]:
        '''The type of client authentication used to connect to the Apache Kafka cluster.

        The value is NONE when no client authentication is used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication
        '''
        return typing.cast(typing.Union["CfnConnector.KafkaClusterClientAuthenticationProperty", _IResolvable_da3f097b], jsii.get(self, "kafkaClusterClientAuthentication"))

    @kafka_cluster_client_authentication.setter
    def kafka_cluster_client_authentication(
        self,
        value: typing.Union["CfnConnector.KafkaClusterClientAuthenticationProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "kafka_cluster_client_authentication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaClusterClientAuthentication", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kafkaClusterEncryptionInTransit")
    def kafka_cluster_encryption_in_transit(
        self,
    ) -> typing.Union["CfnConnector.KafkaClusterEncryptionInTransitProperty", _IResolvable_da3f097b]:
        '''Details of encryption in transit to the Apache Kafka cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit
        '''
        return typing.cast(typing.Union["CfnConnector.KafkaClusterEncryptionInTransitProperty", _IResolvable_da3f097b], jsii.get(self, "kafkaClusterEncryptionInTransit"))

    @kafka_cluster_encryption_in_transit.setter
    def kafka_cluster_encryption_in_transit(
        self,
        value: typing.Union["CfnConnector.KafkaClusterEncryptionInTransitProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "kafka_cluster_encryption_in_transit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaClusterEncryptionInTransit", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kafkaConnectVersion")
    def kafka_connect_version(self) -> builtins.str:
        '''The version of Kafka Connect.

        It has to be compatible with both the Apache Kafka cluster's version and the plugins.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaconnectversion
        '''
        return typing.cast(builtins.str, jsii.get(self, "kafkaConnectVersion"))

    @kafka_connect_version.setter
    def kafka_connect_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "kafka_connect_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaConnectVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="plugins")
    def plugins(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnConnector.PluginProperty", _IResolvable_da3f097b]]]:
        '''Specifies which plugin to use for the connector.

        You must specify a single-element list. Amazon MSK Connect does not currently support specifying multiple plugins.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-plugins
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnConnector.PluginProperty", _IResolvable_da3f097b]]], jsii.get(self, "plugins"))

    @plugins.setter
    def plugins(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnConnector.PluginProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "plugins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plugins", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-serviceexecutionrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceExecutionRoleArn"))

    @service_execution_role_arn.setter
    def service_execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "service_execution_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceExecutionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectorDescription")
    def connector_description(self) -> typing.Optional[builtins.str]:
        '''The description of the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectordescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorDescription"))

    @connector_description.setter
    def connector_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "connector_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logDelivery")
    def log_delivery(
        self,
    ) -> typing.Optional[typing.Union["CfnConnector.LogDeliveryProperty", _IResolvable_da3f097b]]:
        '''The settings for delivering connector logs to Amazon CloudWatch Logs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-logdelivery
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConnector.LogDeliveryProperty", _IResolvable_da3f097b]], jsii.get(self, "logDelivery"))

    @log_delivery.setter
    def log_delivery(
        self,
        value: typing.Optional[typing.Union["CfnConnector.LogDeliveryProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "log_delivery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDelivery", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workerConfiguration")
    def worker_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnConnector.WorkerConfigurationProperty", _IResolvable_da3f097b]]:
        '''The worker configurations that are in use with the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-workerconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConnector.WorkerConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "workerConfiguration"))

    @worker_configuration.setter
    def worker_configuration(
        self,
        value: typing.Optional[typing.Union["CfnConnector.WorkerConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnector, "worker_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.ApacheKafkaClusterProperty",
        jsii_struct_bases=[],
        name_mapping={"bootstrap_servers": "bootstrapServers", "vpc": "vpc"},
    )
    class ApacheKafkaClusterProperty:
        def __init__(
            self,
            *,
            bootstrap_servers: builtins.str,
            vpc: typing.Union[typing.Union["CfnConnector.VpcProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''The details of the Apache Kafka cluster to which the connector is connected.

            :param bootstrap_servers: The bootstrap servers of the cluster.
            :param vpc: Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                apache_kafka_cluster_property = kafkaconnect.CfnConnector.ApacheKafkaClusterProperty(
                    bootstrap_servers="bootstrapServers",
                    vpc=kafkaconnect.CfnConnector.VpcProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.ApacheKafkaClusterProperty.__init__)
                check_type(argname="argument bootstrap_servers", value=bootstrap_servers, expected_type=type_hints["bootstrap_servers"])
                check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            self._values: typing.Dict[str, typing.Any] = {
                "bootstrap_servers": bootstrap_servers,
                "vpc": vpc,
            }

        @builtins.property
        def bootstrap_servers(self) -> builtins.str:
            '''The bootstrap servers of the cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-bootstrapservers
            '''
            result = self._values.get("bootstrap_servers")
            assert result is not None, "Required property 'bootstrap_servers' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc(
            self,
        ) -> typing.Union["CfnConnector.VpcProperty", _IResolvable_da3f097b]:
            '''Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-vpc
            '''
            result = self._values.get("vpc")
            assert result is not None, "Required property 'vpc' is missing"
            return typing.cast(typing.Union["CfnConnector.VpcProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApacheKafkaClusterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.AutoScalingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_worker_count": "maxWorkerCount",
            "mcu_count": "mcuCount",
            "min_worker_count": "minWorkerCount",
            "scale_in_policy": "scaleInPolicy",
            "scale_out_policy": "scaleOutPolicy",
        },
    )
    class AutoScalingProperty:
        def __init__(
            self,
            *,
            max_worker_count: jsii.Number,
            mcu_count: jsii.Number,
            min_worker_count: jsii.Number,
            scale_in_policy: typing.Union[typing.Union["CfnConnector.ScaleInPolicyProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            scale_out_policy: typing.Union[typing.Union["CfnConnector.ScaleOutPolicyProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''Specifies how the connector scales.

            :param max_worker_count: The maximum number of workers allocated to the connector.
            :param mcu_count: The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.
            :param min_worker_count: The minimum number of workers allocated to the connector.
            :param scale_in_policy: The sacle-in policy for the connector.
            :param scale_out_policy: The sacle-out policy for the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                auto_scaling_property = kafkaconnect.CfnConnector.AutoScalingProperty(
                    max_worker_count=123,
                    mcu_count=123,
                    min_worker_count=123,
                    scale_in_policy=kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                        cpu_utilization_percentage=123
                    ),
                    scale_out_policy=kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                        cpu_utilization_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.AutoScalingProperty.__init__)
                check_type(argname="argument max_worker_count", value=max_worker_count, expected_type=type_hints["max_worker_count"])
                check_type(argname="argument mcu_count", value=mcu_count, expected_type=type_hints["mcu_count"])
                check_type(argname="argument min_worker_count", value=min_worker_count, expected_type=type_hints["min_worker_count"])
                check_type(argname="argument scale_in_policy", value=scale_in_policy, expected_type=type_hints["scale_in_policy"])
                check_type(argname="argument scale_out_policy", value=scale_out_policy, expected_type=type_hints["scale_out_policy"])
            self._values: typing.Dict[str, typing.Any] = {
                "max_worker_count": max_worker_count,
                "mcu_count": mcu_count,
                "min_worker_count": min_worker_count,
                "scale_in_policy": scale_in_policy,
                "scale_out_policy": scale_out_policy,
            }

        @builtins.property
        def max_worker_count(self) -> jsii.Number:
            '''The maximum number of workers allocated to the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-maxworkercount
            '''
            result = self._values.get("max_worker_count")
            assert result is not None, "Required property 'max_worker_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def mcu_count(self) -> jsii.Number:
            '''The number of microcontroller units (MCUs) allocated to each connector worker.

            The valid values are 1,2,4,8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-mcucount
            '''
            result = self._values.get("mcu_count")
            assert result is not None, "Required property 'mcu_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_worker_count(self) -> jsii.Number:
            '''The minimum number of workers allocated to the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-minworkercount
            '''
            result = self._values.get("min_worker_count")
            assert result is not None, "Required property 'min_worker_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def scale_in_policy(
            self,
        ) -> typing.Union["CfnConnector.ScaleInPolicyProperty", _IResolvable_da3f097b]:
            '''The sacle-in policy for the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleinpolicy
            '''
            result = self._values.get("scale_in_policy")
            assert result is not None, "Required property 'scale_in_policy' is missing"
            return typing.cast(typing.Union["CfnConnector.ScaleInPolicyProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def scale_out_policy(
            self,
        ) -> typing.Union["CfnConnector.ScaleOutPolicyProperty", _IResolvable_da3f097b]:
            '''The sacle-out policy for the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleoutpolicy
            '''
            result = self._values.get("scale_out_policy")
            assert result is not None, "Required property 'scale_out_policy' is missing"
            return typing.cast(typing.Union["CfnConnector.ScaleOutPolicyProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.CapacityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_scaling": "autoScaling",
            "provisioned_capacity": "provisionedCapacity",
        },
    )
    class CapacityProperty:
        def __init__(
            self,
            *,
            auto_scaling: typing.Optional[typing.Union[typing.Union["CfnConnector.AutoScalingProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            provisioned_capacity: typing.Optional[typing.Union[typing.Union["CfnConnector.ProvisionedCapacityProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Information about the capacity of the connector, whether it is auto scaled or provisioned.

            :param auto_scaling: Information about the auto scaling parameters for the connector.
            :param provisioned_capacity: Details about a fixed capacity allocated to a connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                capacity_property = kafkaconnect.CfnConnector.CapacityProperty(
                    auto_scaling=kafkaconnect.CfnConnector.AutoScalingProperty(
                        max_worker_count=123,
                        mcu_count=123,
                        min_worker_count=123,
                        scale_in_policy=kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                            cpu_utilization_percentage=123
                        ),
                        scale_out_policy=kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                            cpu_utilization_percentage=123
                        )
                    ),
                    provisioned_capacity=kafkaconnect.CfnConnector.ProvisionedCapacityProperty(
                        worker_count=123,
                
                        # the properties below are optional
                        mcu_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.CapacityProperty.__init__)
                check_type(argname="argument auto_scaling", value=auto_scaling, expected_type=type_hints["auto_scaling"])
                check_type(argname="argument provisioned_capacity", value=provisioned_capacity, expected_type=type_hints["provisioned_capacity"])
            self._values: typing.Dict[str, typing.Any] = {}
            if auto_scaling is not None:
                self._values["auto_scaling"] = auto_scaling
            if provisioned_capacity is not None:
                self._values["provisioned_capacity"] = provisioned_capacity

        @builtins.property
        def auto_scaling(
            self,
        ) -> typing.Optional[typing.Union["CfnConnector.AutoScalingProperty", _IResolvable_da3f097b]]:
            '''Information about the auto scaling parameters for the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-autoscaling
            '''
            result = self._values.get("auto_scaling")
            return typing.cast(typing.Optional[typing.Union["CfnConnector.AutoScalingProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def provisioned_capacity(
            self,
        ) -> typing.Optional[typing.Union["CfnConnector.ProvisionedCapacityProperty", _IResolvable_da3f097b]]:
            '''Details about a fixed capacity allocated to a connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-provisionedcapacity
            '''
            result = self._values.get("provisioned_capacity")
            return typing.cast(typing.Optional[typing.Union["CfnConnector.ProvisionedCapacityProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "log_group": "logGroup"},
    )
    class CloudWatchLogsLogDeliveryProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            log_group: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for delivering connector logs to Amazon CloudWatch Logs.

            :param enabled: Whether log delivery to Amazon CloudWatch Logs is enabled.
            :param log_group: The name of the CloudWatch log group that is the destination for log delivery.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                cloud_watch_logs_log_delivery_property = kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                    enabled=False,
                
                    # the properties below are optional
                    log_group="logGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.CloudWatchLogsLogDeliveryProperty.__init__)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }
            if log_group is not None:
                self._values["log_group"] = log_group

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Whether log delivery to Amazon CloudWatch Logs is enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def log_group(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch log group that is the destination for log delivery.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-loggroup
            '''
            result = self._values.get("log_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsLogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.CustomPluginProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_plugin_arn": "customPluginArn", "revision": "revision"},
    )
    class CustomPluginProperty:
        def __init__(
            self,
            *,
            custom_plugin_arn: builtins.str,
            revision: jsii.Number,
        ) -> None:
            '''A plugin is an AWS resource that contains the code that defines a connector's logic.

            :param custom_plugin_arn: The Amazon Resource Name (ARN) of the custom plugin.
            :param revision: The revision of the custom plugin.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                custom_plugin_property = kafkaconnect.CfnConnector.CustomPluginProperty(
                    custom_plugin_arn="customPluginArn",
                    revision=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.CustomPluginProperty.__init__)
                check_type(argname="argument custom_plugin_arn", value=custom_plugin_arn, expected_type=type_hints["custom_plugin_arn"])
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            self._values: typing.Dict[str, typing.Any] = {
                "custom_plugin_arn": custom_plugin_arn,
                "revision": revision,
            }

        @builtins.property
        def custom_plugin_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the custom plugin.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-custompluginarn
            '''
            result = self._values.get("custom_plugin_arn")
            assert result is not None, "Required property 'custom_plugin_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def revision(self) -> jsii.Number:
            '''The revision of the custom plugin.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomPluginProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "delivery_stream": "deliveryStream"},
    )
    class FirehoseLogDeliveryProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            delivery_stream: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for delivering logs to Amazon Kinesis Data Firehose.

            :param enabled: Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.
            :param delivery_stream: The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                firehose_log_delivery_property = kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                    enabled=False,
                
                    # the properties below are optional
                    delivery_stream="deliveryStream"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.FirehoseLogDeliveryProperty.__init__)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }
            if delivery_stream is not None:
                self._values["delivery_stream"] = delivery_stream

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def delivery_stream(self) -> typing.Optional[builtins.str]:
            '''The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-deliverystream
            '''
            result = self._values.get("delivery_stream")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseLogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.KafkaClusterClientAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"authentication_type": "authenticationType"},
    )
    class KafkaClusterClientAuthenticationProperty:
        def __init__(self, *, authentication_type: builtins.str) -> None:
            '''The client authentication information used in order to authenticate with the Apache Kafka cluster.

            :param authentication_type: The type of client authentication used to connect to the Apache Kafka cluster. Value NONE means that no client authentication is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                kafka_cluster_client_authentication_property = kafkaconnect.CfnConnector.KafkaClusterClientAuthenticationProperty(
                    authentication_type="authenticationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.KafkaClusterClientAuthenticationProperty.__init__)
                check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            self._values: typing.Dict[str, typing.Any] = {
                "authentication_type": authentication_type,
            }

        @builtins.property
        def authentication_type(self) -> builtins.str:
            '''The type of client authentication used to connect to the Apache Kafka cluster.

            Value NONE means that no client authentication is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication-authenticationtype
            '''
            result = self._values.get("authentication_type")
            assert result is not None, "Required property 'authentication_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaClusterClientAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.KafkaClusterEncryptionInTransitProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_type": "encryptionType"},
    )
    class KafkaClusterEncryptionInTransitProperty:
        def __init__(self, *, encryption_type: builtins.str) -> None:
            '''Details of encryption in transit to the Apache Kafka cluster.

            :param encryption_type: The type of encryption in transit to the Apache Kafka cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                kafka_cluster_encryption_in_transit_property = kafkaconnect.CfnConnector.KafkaClusterEncryptionInTransitProperty(
                    encryption_type="encryptionType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.KafkaClusterEncryptionInTransitProperty.__init__)
                check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            self._values: typing.Dict[str, typing.Any] = {
                "encryption_type": encryption_type,
            }

        @builtins.property
        def encryption_type(self) -> builtins.str:
            '''The type of encryption in transit to the Apache Kafka cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit-encryptiontype
            '''
            result = self._values.get("encryption_type")
            assert result is not None, "Required property 'encryption_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaClusterEncryptionInTransitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.KafkaClusterProperty",
        jsii_struct_bases=[],
        name_mapping={"apache_kafka_cluster": "apacheKafkaCluster"},
    )
    class KafkaClusterProperty:
        def __init__(
            self,
            *,
            apache_kafka_cluster: typing.Union[typing.Union["CfnConnector.ApacheKafkaClusterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''The details of the Apache Kafka cluster to which the connector is connected.

            :param apache_kafka_cluster: The Apache Kafka cluster to which the connector is connected.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                kafka_cluster_property = kafkaconnect.CfnConnector.KafkaClusterProperty(
                    apache_kafka_cluster=kafkaconnect.CfnConnector.ApacheKafkaClusterProperty(
                        bootstrap_servers="bootstrapServers",
                        vpc=kafkaconnect.CfnConnector.VpcProperty(
                            security_groups=["securityGroups"],
                            subnets=["subnets"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.KafkaClusterProperty.__init__)
                check_type(argname="argument apache_kafka_cluster", value=apache_kafka_cluster, expected_type=type_hints["apache_kafka_cluster"])
            self._values: typing.Dict[str, typing.Any] = {
                "apache_kafka_cluster": apache_kafka_cluster,
            }

        @builtins.property
        def apache_kafka_cluster(
            self,
        ) -> typing.Union["CfnConnector.ApacheKafkaClusterProperty", _IResolvable_da3f097b]:
            '''The Apache Kafka cluster to which the connector is connected.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html#cfn-kafkaconnect-connector-kafkacluster-apachekafkacluster
            '''
            result = self._values.get("apache_kafka_cluster")
            assert result is not None, "Required property 'apache_kafka_cluster' is missing"
            return typing.cast(typing.Union["CfnConnector.ApacheKafkaClusterProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaClusterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.LogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"worker_log_delivery": "workerLogDelivery"},
    )
    class LogDeliveryProperty:
        def __init__(
            self,
            *,
            worker_log_delivery: typing.Union[typing.Union["CfnConnector.WorkerLogDeliveryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''Details about log delivery.

            :param worker_log_delivery: The workers can send worker logs to different destination types. This configuration specifies the details of these destinations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                log_delivery_property = kafkaconnect.CfnConnector.LogDeliveryProperty(
                    worker_log_delivery=kafkaconnect.CfnConnector.WorkerLogDeliveryProperty(
                        cloud_watch_logs=kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                            enabled=False,
                
                            # the properties below are optional
                            log_group="logGroup"
                        ),
                        firehose=kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                            enabled=False,
                
                            # the properties below are optional
                            delivery_stream="deliveryStream"
                        ),
                        s3=kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                            enabled=False,
                
                            # the properties below are optional
                            bucket="bucket",
                            prefix="prefix"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.LogDeliveryProperty.__init__)
                check_type(argname="argument worker_log_delivery", value=worker_log_delivery, expected_type=type_hints["worker_log_delivery"])
            self._values: typing.Dict[str, typing.Any] = {
                "worker_log_delivery": worker_log_delivery,
            }

        @builtins.property
        def worker_log_delivery(
            self,
        ) -> typing.Union["CfnConnector.WorkerLogDeliveryProperty", _IResolvable_da3f097b]:
            '''The workers can send worker logs to different destination types.

            This configuration specifies the details of these destinations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html#cfn-kafkaconnect-connector-logdelivery-workerlogdelivery
            '''
            result = self._values.get("worker_log_delivery")
            assert result is not None, "Required property 'worker_log_delivery' is missing"
            return typing.cast(typing.Union["CfnConnector.WorkerLogDeliveryProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.PluginProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_plugin": "customPlugin"},
    )
    class PluginProperty:
        def __init__(
            self,
            *,
            custom_plugin: typing.Union[typing.Union["CfnConnector.CustomPluginProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''A plugin is an AWS resource that contains the code that defines your connector logic.

            :param custom_plugin: Details about a custom plugin.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                plugin_property = kafkaconnect.CfnConnector.PluginProperty(
                    custom_plugin=kafkaconnect.CfnConnector.CustomPluginProperty(
                        custom_plugin_arn="customPluginArn",
                        revision=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.PluginProperty.__init__)
                check_type(argname="argument custom_plugin", value=custom_plugin, expected_type=type_hints["custom_plugin"])
            self._values: typing.Dict[str, typing.Any] = {
                "custom_plugin": custom_plugin,
            }

        @builtins.property
        def custom_plugin(
            self,
        ) -> typing.Union["CfnConnector.CustomPluginProperty", _IResolvable_da3f097b]:
            '''Details about a custom plugin.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html#cfn-kafkaconnect-connector-plugin-customplugin
            '''
            result = self._values.get("custom_plugin")
            assert result is not None, "Required property 'custom_plugin' is missing"
            return typing.cast(typing.Union["CfnConnector.CustomPluginProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PluginProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.ProvisionedCapacityProperty",
        jsii_struct_bases=[],
        name_mapping={"worker_count": "workerCount", "mcu_count": "mcuCount"},
    )
    class ProvisionedCapacityProperty:
        def __init__(
            self,
            *,
            worker_count: jsii.Number,
            mcu_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Details about a connector's provisioned capacity.

            :param worker_count: The number of workers that are allocated to the connector.
            :param mcu_count: The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                provisioned_capacity_property = kafkaconnect.CfnConnector.ProvisionedCapacityProperty(
                    worker_count=123,
                
                    # the properties below are optional
                    mcu_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.ProvisionedCapacityProperty.__init__)
                check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
                check_type(argname="argument mcu_count", value=mcu_count, expected_type=type_hints["mcu_count"])
            self._values: typing.Dict[str, typing.Any] = {
                "worker_count": worker_count,
            }
            if mcu_count is not None:
                self._values["mcu_count"] = mcu_count

        @builtins.property
        def worker_count(self) -> jsii.Number:
            '''The number of workers that are allocated to the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-workercount
            '''
            result = self._values.get("worker_count")
            assert result is not None, "Required property 'worker_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def mcu_count(self) -> typing.Optional[jsii.Number]:
            '''The number of microcontroller units (MCUs) allocated to each connector worker.

            The valid values are 1,2,4,8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-mcucount
            '''
            result = self._values.get("mcu_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedCapacityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.S3LogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "bucket": "bucket", "prefix": "prefix"},
    )
    class S3LogDeliveryProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            bucket: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details about delivering logs to Amazon S3.

            :param enabled: Specifies whether connector logs get sent to the specified Amazon S3 destination.
            :param bucket: The name of the S3 bucket that is the destination for log delivery.
            :param prefix: The S3 prefix that is the destination for log delivery.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                s3_log_delivery_property = kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                    enabled=False,
                
                    # the properties below are optional
                    bucket="bucket",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.S3LogDeliveryProperty.__init__)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }
            if bucket is not None:
                self._values["bucket"] = bucket
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether connector logs get sent to the specified Amazon S3 destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def bucket(self) -> typing.Optional[builtins.str]:
            '''The name of the S3 bucket that is the destination for log delivery.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-bucket
            '''
            result = self._values.get("bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 prefix that is the destination for log delivery.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.ScaleInPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu_utilization_percentage": "cpuUtilizationPercentage"},
    )
    class ScaleInPolicyProperty:
        def __init__(self, *, cpu_utilization_percentage: jsii.Number) -> None:
            '''The scale-in policy for the connector.

            :param cpu_utilization_percentage: Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                scale_in_policy_property = kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                    cpu_utilization_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.ScaleInPolicyProperty.__init__)
                check_type(argname="argument cpu_utilization_percentage", value=cpu_utilization_percentage, expected_type=type_hints["cpu_utilization_percentage"])
            self._values: typing.Dict[str, typing.Any] = {
                "cpu_utilization_percentage": cpu_utilization_percentage,
            }

        @builtins.property
        def cpu_utilization_percentage(self) -> jsii.Number:
            '''Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html#cfn-kafkaconnect-connector-scaleinpolicy-cpuutilizationpercentage
            '''
            result = self._values.get("cpu_utilization_percentage")
            assert result is not None, "Required property 'cpu_utilization_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScaleInPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.ScaleOutPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu_utilization_percentage": "cpuUtilizationPercentage"},
    )
    class ScaleOutPolicyProperty:
        def __init__(self, *, cpu_utilization_percentage: jsii.Number) -> None:
            '''The scale-out policy for the connector.

            :param cpu_utilization_percentage: The CPU utilization percentage threshold at which you want connector scale out to be triggered.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                scale_out_policy_property = kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                    cpu_utilization_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.ScaleOutPolicyProperty.__init__)
                check_type(argname="argument cpu_utilization_percentage", value=cpu_utilization_percentage, expected_type=type_hints["cpu_utilization_percentage"])
            self._values: typing.Dict[str, typing.Any] = {
                "cpu_utilization_percentage": cpu_utilization_percentage,
            }

        @builtins.property
        def cpu_utilization_percentage(self) -> jsii.Number:
            '''The CPU utilization percentage threshold at which you want connector scale out to be triggered.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html#cfn-kafkaconnect-connector-scaleoutpolicy-cpuutilizationpercentage
            '''
            result = self._values.get("cpu_utilization_percentage")
            assert result is not None, "Required property 'cpu_utilization_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScaleOutPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.VpcProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
    )
    class VpcProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Information about the VPC in which the connector resides.

            :param security_groups: The security groups for the connector.
            :param subnets: The subnets for the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                vpc_property = kafkaconnect.CfnConnector.VpcProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.VpcProperty.__init__)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[str, typing.Any] = {
                "security_groups": security_groups,
                "subnets": subnets,
            }

        @builtins.property
        def security_groups(self) -> typing.List[builtins.str]:
            '''The security groups for the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-securitygroups
            '''
            result = self._values.get("security_groups")
            assert result is not None, "Required property 'security_groups' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''The subnets for the connector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.WorkerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "revision": "revision",
            "worker_configuration_arn": "workerConfigurationArn",
        },
    )
    class WorkerConfigurationProperty:
        def __init__(
            self,
            *,
            revision: jsii.Number,
            worker_configuration_arn: builtins.str,
        ) -> None:
            '''The configuration of the workers, which are the processes that run the connector logic.

            :param revision: The revision of the worker configuration.
            :param worker_configuration_arn: The Amazon Resource Name (ARN) of the worker configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                worker_configuration_property = kafkaconnect.CfnConnector.WorkerConfigurationProperty(
                    revision=123,
                    worker_configuration_arn="workerConfigurationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.WorkerConfigurationProperty.__init__)
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
                check_type(argname="argument worker_configuration_arn", value=worker_configuration_arn, expected_type=type_hints["worker_configuration_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "revision": revision,
                "worker_configuration_arn": worker_configuration_arn,
            }

        @builtins.property
        def revision(self) -> jsii.Number:
            '''The revision of the worker configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def worker_configuration_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the worker configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-workerconfigurationarn
            '''
            result = self._values.get("worker_configuration_arn")
            assert result is not None, "Required property 'worker_configuration_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnector.WorkerLogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs": "cloudWatchLogs",
            "firehose": "firehose",
            "s3": "s3",
        },
    )
    class WorkerLogDeliveryProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Optional[typing.Union[typing.Union["CfnConnector.CloudWatchLogsLogDeliveryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            firehose: typing.Optional[typing.Union[typing.Union["CfnConnector.FirehoseLogDeliveryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            s3: typing.Optional[typing.Union[typing.Union["CfnConnector.S3LogDeliveryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Workers can send worker logs to different destination types.

            This configuration specifies the details of these destinations.

            :param cloud_watch_logs: Details about delivering logs to Amazon CloudWatch Logs.
            :param firehose: Details about delivering logs to Amazon Kinesis Data Firehose.
            :param s3: Details about delivering logs to Amazon S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kafkaconnect as kafkaconnect
                
                worker_log_delivery_property = kafkaconnect.CfnConnector.WorkerLogDeliveryProperty(
                    cloud_watch_logs=kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                        enabled=False,
                
                        # the properties below are optional
                        log_group="logGroup"
                    ),
                    firehose=kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                        enabled=False,
                
                        # the properties below are optional
                        delivery_stream="deliveryStream"
                    ),
                    s3=kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                        enabled=False,
                
                        # the properties below are optional
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnector.WorkerLogDeliveryProperty.__init__)
                check_type(argname="argument cloud_watch_logs", value=cloud_watch_logs, expected_type=type_hints["cloud_watch_logs"])
                check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_watch_logs is not None:
                self._values["cloud_watch_logs"] = cloud_watch_logs
            if firehose is not None:
                self._values["firehose"] = firehose
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnConnector.CloudWatchLogsLogDeliveryProperty", _IResolvable_da3f097b]]:
            '''Details about delivering logs to Amazon CloudWatch Logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            return typing.cast(typing.Optional[typing.Union["CfnConnector.CloudWatchLogsLogDeliveryProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union["CfnConnector.FirehoseLogDeliveryProperty", _IResolvable_da3f097b]]:
            '''Details about delivering logs to Amazon Kinesis Data Firehose.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union["CfnConnector.FirehoseLogDeliveryProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union["CfnConnector.S3LogDeliveryProperty", _IResolvable_da3f097b]]:
            '''Details about delivering logs to Amazon S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union["CfnConnector.S3LogDeliveryProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkerLogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kafkaconnect.CfnConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "connector_configuration": "connectorConfiguration",
        "connector_name": "connectorName",
        "kafka_cluster": "kafkaCluster",
        "kafka_cluster_client_authentication": "kafkaClusterClientAuthentication",
        "kafka_cluster_encryption_in_transit": "kafkaClusterEncryptionInTransit",
        "kafka_connect_version": "kafkaConnectVersion",
        "plugins": "plugins",
        "service_execution_role_arn": "serviceExecutionRoleArn",
        "connector_description": "connectorDescription",
        "log_delivery": "logDelivery",
        "worker_configuration": "workerConfiguration",
    },
)
class CfnConnectorProps:
    def __init__(
        self,
        *,
        capacity: typing.Union[typing.Union[CfnConnector.CapacityProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        connector_configuration: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
        connector_name: builtins.str,
        kafka_cluster: typing.Union[typing.Union[CfnConnector.KafkaClusterProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        kafka_cluster_client_authentication: typing.Union[typing.Union[CfnConnector.KafkaClusterClientAuthenticationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        kafka_cluster_encryption_in_transit: typing.Union[typing.Union[CfnConnector.KafkaClusterEncryptionInTransitProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        kafka_connect_version: builtins.str,
        plugins: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnConnector.PluginProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        service_execution_role_arn: builtins.str,
        connector_description: typing.Optional[builtins.str] = None,
        log_delivery: typing.Optional[typing.Union[typing.Union[CfnConnector.LogDeliveryProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        worker_configuration: typing.Optional[typing.Union[typing.Union[CfnConnector.WorkerConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnector``.

        :param capacity: The connector's compute capacity settings.
        :param connector_configuration: The configuration of the connector.
        :param connector_name: The name of the connector.
        :param kafka_cluster: The details of the Apache Kafka cluster to which the connector is connected.
        :param kafka_cluster_client_authentication: The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used.
        :param kafka_cluster_encryption_in_transit: Details of encryption in transit to the Apache Kafka cluster.
        :param kafka_connect_version: The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.
        :param plugins: Specifies which plugin to use for the connector. You must specify a single-element list. Amazon MSK Connect does not currently support specifying multiple plugins.
        :param service_execution_role_arn: The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.
        :param connector_description: The description of the connector.
        :param log_delivery: The settings for delivering connector logs to Amazon CloudWatch Logs.
        :param worker_configuration: The worker configurations that are in use with the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kafkaconnect as kafkaconnect
            
            cfn_connector_props = kafkaconnect.CfnConnectorProps(
                capacity=kafkaconnect.CfnConnector.CapacityProperty(
                    auto_scaling=kafkaconnect.CfnConnector.AutoScalingProperty(
                        max_worker_count=123,
                        mcu_count=123,
                        min_worker_count=123,
                        scale_in_policy=kafkaconnect.CfnConnector.ScaleInPolicyProperty(
                            cpu_utilization_percentage=123
                        ),
                        scale_out_policy=kafkaconnect.CfnConnector.ScaleOutPolicyProperty(
                            cpu_utilization_percentage=123
                        )
                    ),
                    provisioned_capacity=kafkaconnect.CfnConnector.ProvisionedCapacityProperty(
                        worker_count=123,
            
                        # the properties below are optional
                        mcu_count=123
                    )
                ),
                connector_configuration={
                    "connector_configuration_key": "connectorConfiguration"
                },
                connector_name="connectorName",
                kafka_cluster=kafkaconnect.CfnConnector.KafkaClusterProperty(
                    apache_kafka_cluster=kafkaconnect.CfnConnector.ApacheKafkaClusterProperty(
                        bootstrap_servers="bootstrapServers",
                        vpc=kafkaconnect.CfnConnector.VpcProperty(
                            security_groups=["securityGroups"],
                            subnets=["subnets"]
                        )
                    )
                ),
                kafka_cluster_client_authentication=kafkaconnect.CfnConnector.KafkaClusterClientAuthenticationProperty(
                    authentication_type="authenticationType"
                ),
                kafka_cluster_encryption_in_transit=kafkaconnect.CfnConnector.KafkaClusterEncryptionInTransitProperty(
                    encryption_type="encryptionType"
                ),
                kafka_connect_version="kafkaConnectVersion",
                plugins=[kafkaconnect.CfnConnector.PluginProperty(
                    custom_plugin=kafkaconnect.CfnConnector.CustomPluginProperty(
                        custom_plugin_arn="customPluginArn",
                        revision=123
                    )
                )],
                service_execution_role_arn="serviceExecutionRoleArn",
            
                # the properties below are optional
                connector_description="connectorDescription",
                log_delivery=kafkaconnect.CfnConnector.LogDeliveryProperty(
                    worker_log_delivery=kafkaconnect.CfnConnector.WorkerLogDeliveryProperty(
                        cloud_watch_logs=kafkaconnect.CfnConnector.CloudWatchLogsLogDeliveryProperty(
                            enabled=False,
            
                            # the properties below are optional
                            log_group="logGroup"
                        ),
                        firehose=kafkaconnect.CfnConnector.FirehoseLogDeliveryProperty(
                            enabled=False,
            
                            # the properties below are optional
                            delivery_stream="deliveryStream"
                        ),
                        s3=kafkaconnect.CfnConnector.S3LogDeliveryProperty(
                            enabled=False,
            
                            # the properties below are optional
                            bucket="bucket",
                            prefix="prefix"
                        )
                    )
                ),
                worker_configuration=kafkaconnect.CfnConnector.WorkerConfigurationProperty(
                    revision=123,
                    worker_configuration_arn="workerConfigurationArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnectorProps.__init__)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument connector_configuration", value=connector_configuration, expected_type=type_hints["connector_configuration"])
            check_type(argname="argument connector_name", value=connector_name, expected_type=type_hints["connector_name"])
            check_type(argname="argument kafka_cluster", value=kafka_cluster, expected_type=type_hints["kafka_cluster"])
            check_type(argname="argument kafka_cluster_client_authentication", value=kafka_cluster_client_authentication, expected_type=type_hints["kafka_cluster_client_authentication"])
            check_type(argname="argument kafka_cluster_encryption_in_transit", value=kafka_cluster_encryption_in_transit, expected_type=type_hints["kafka_cluster_encryption_in_transit"])
            check_type(argname="argument kafka_connect_version", value=kafka_connect_version, expected_type=type_hints["kafka_connect_version"])
            check_type(argname="argument plugins", value=plugins, expected_type=type_hints["plugins"])
            check_type(argname="argument service_execution_role_arn", value=service_execution_role_arn, expected_type=type_hints["service_execution_role_arn"])
            check_type(argname="argument connector_description", value=connector_description, expected_type=type_hints["connector_description"])
            check_type(argname="argument log_delivery", value=log_delivery, expected_type=type_hints["log_delivery"])
            check_type(argname="argument worker_configuration", value=worker_configuration, expected_type=type_hints["worker_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "connector_configuration": connector_configuration,
            "connector_name": connector_name,
            "kafka_cluster": kafka_cluster,
            "kafka_cluster_client_authentication": kafka_cluster_client_authentication,
            "kafka_cluster_encryption_in_transit": kafka_cluster_encryption_in_transit,
            "kafka_connect_version": kafka_connect_version,
            "plugins": plugins,
            "service_execution_role_arn": service_execution_role_arn,
        }
        if connector_description is not None:
            self._values["connector_description"] = connector_description
        if log_delivery is not None:
            self._values["log_delivery"] = log_delivery
        if worker_configuration is not None:
            self._values["worker_configuration"] = worker_configuration

    @builtins.property
    def capacity(
        self,
    ) -> typing.Union[CfnConnector.CapacityProperty, _IResolvable_da3f097b]:
        '''The connector's compute capacity settings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-capacity
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(typing.Union[CfnConnector.CapacityProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def connector_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
        '''The configuration of the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorconfiguration
        '''
        result = self._values.get("connector_configuration")
        assert result is not None, "Required property 'connector_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def connector_name(self) -> builtins.str:
        '''The name of the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorname
        '''
        result = self._values.get("connector_name")
        assert result is not None, "Required property 'connector_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kafka_cluster(
        self,
    ) -> typing.Union[CfnConnector.KafkaClusterProperty, _IResolvable_da3f097b]:
        '''The details of the Apache Kafka cluster to which the connector is connected.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkacluster
        '''
        result = self._values.get("kafka_cluster")
        assert result is not None, "Required property 'kafka_cluster' is missing"
        return typing.cast(typing.Union[CfnConnector.KafkaClusterProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def kafka_cluster_client_authentication(
        self,
    ) -> typing.Union[CfnConnector.KafkaClusterClientAuthenticationProperty, _IResolvable_da3f097b]:
        '''The type of client authentication used to connect to the Apache Kafka cluster.

        The value is NONE when no client authentication is used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication
        '''
        result = self._values.get("kafka_cluster_client_authentication")
        assert result is not None, "Required property 'kafka_cluster_client_authentication' is missing"
        return typing.cast(typing.Union[CfnConnector.KafkaClusterClientAuthenticationProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def kafka_cluster_encryption_in_transit(
        self,
    ) -> typing.Union[CfnConnector.KafkaClusterEncryptionInTransitProperty, _IResolvable_da3f097b]:
        '''Details of encryption in transit to the Apache Kafka cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit
        '''
        result = self._values.get("kafka_cluster_encryption_in_transit")
        assert result is not None, "Required property 'kafka_cluster_encryption_in_transit' is missing"
        return typing.cast(typing.Union[CfnConnector.KafkaClusterEncryptionInTransitProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def kafka_connect_version(self) -> builtins.str:
        '''The version of Kafka Connect.

        It has to be compatible with both the Apache Kafka cluster's version and the plugins.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaconnectversion
        '''
        result = self._values.get("kafka_connect_version")
        assert result is not None, "Required property 'kafka_connect_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugins(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnConnector.PluginProperty, _IResolvable_da3f097b]]]:
        '''Specifies which plugin to use for the connector.

        You must specify a single-element list. Amazon MSK Connect does not currently support specifying multiple plugins.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-plugins
        '''
        result = self._values.get("plugins")
        assert result is not None, "Required property 'plugins' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnConnector.PluginProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def service_execution_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-serviceexecutionrolearn
        '''
        result = self._values.get("service_execution_role_arn")
        assert result is not None, "Required property 'service_execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_description(self) -> typing.Optional[builtins.str]:
        '''The description of the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectordescription
        '''
        result = self._values.get("connector_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery(
        self,
    ) -> typing.Optional[typing.Union[CfnConnector.LogDeliveryProperty, _IResolvable_da3f097b]]:
        '''The settings for delivering connector logs to Amazon CloudWatch Logs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-logdelivery
        '''
        result = self._values.get("log_delivery")
        return typing.cast(typing.Optional[typing.Union[CfnConnector.LogDeliveryProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def worker_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnConnector.WorkerConfigurationProperty, _IResolvable_da3f097b]]:
        '''The worker configurations that are in use with the connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-workerconfiguration
        '''
        result = self._values.get("worker_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnConnector.WorkerConfigurationProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnector",
    "CfnConnectorProps",
]

publication.publish()
