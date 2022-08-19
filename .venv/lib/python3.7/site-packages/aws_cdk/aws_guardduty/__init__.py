'''
# Amazon GuardDuty Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_guardduty as guardduty
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for GuardDuty construct libraries](https://constructs.dev/search?q=guardduty)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::GuardDuty resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GuardDuty.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GuardDuty](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GuardDuty.html).

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
class CfnDetector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector",
):
    '''A CloudFormation ``AWS::GuardDuty::Detector``.

    The ``AWS::GuardDuty::Detector`` resource specifies a new  detector. A detector is an object that represents the  service. A detector is required for  to become operational.

    :cloudformationResource: AWS::GuardDuty::Detector
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_detector = guardduty.CfnDetector(self, "MyCfnDetector",
            enable=False,
        
            # the properties below are optional
            data_sources=guardduty.CfnDetector.CFNDataSourceConfigurationsProperty(
                kubernetes=guardduty.CfnDetector.CFNKubernetesConfigurationProperty(
                    audit_logs=guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                        enable=False
                    )
                ),
                malware_protection=guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty(
                    scan_ec2_instance_with_findings=guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                        ebs_volumes=False
                    )
                ),
                s3_logs=guardduty.CfnDetector.CFNS3LogsConfigurationProperty(
                    enable=False
                )
            ),
            finding_publishing_frequency="findingPublishingFrequency",
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
        enable: typing.Union[builtins.bool, _IResolvable_da3f097b],
        data_sources: typing.Optional[typing.Union[typing.Union["CfnDetector.CFNDataSourceConfigurationsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::Detector``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param enable: Specifies whether the detector is to be enabled on creation.
        :param data_sources: Describes which data sources will be enabled for the detector.
        :param finding_publishing_frequency: Specifies how frequently updated findings are exported.
        :param tags: ``AWS::GuardDuty::Detector.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDetector.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDetectorProps(
            enable=enable,
            data_sources=data_sources,
            finding_publishing_frequency=finding_publishing_frequency,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDetector.inspect)
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
            type_hints = typing.get_type_hints(CfnDetector._render_properties)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::GuardDuty::Detector.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Specifies whether the detector is to be enabled on creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, _IResolvable_da3f097b]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDetector, "enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSources")
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union["CfnDetector.CFNDataSourceConfigurationsProperty", _IResolvable_da3f097b]]:
        '''Describes which data sources will be enabled for the detector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-datasources
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDetector.CFNDataSourceConfigurationsProperty", _IResolvable_da3f097b]], jsii.get(self, "dataSources"))

    @data_sources.setter
    def data_sources(
        self,
        value: typing.Optional[typing.Union["CfnDetector.CFNDataSourceConfigurationsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDetector, "data_sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''Specifies how frequently updated findings are exported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "findingPublishingFrequency"))

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDetector, "finding_publishing_frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingPublishingFrequency", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNDataSourceConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kubernetes": "kubernetes",
            "malware_protection": "malwareProtection",
            "s3_logs": "s3Logs",
        },
    )
    class CFNDataSourceConfigurationsProperty:
        def __init__(
            self,
            *,
            kubernetes: typing.Optional[typing.Union[typing.Union["CfnDetector.CFNKubernetesConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            malware_protection: typing.Optional[typing.Union[typing.Union["CfnDetector.CFNMalwareProtectionConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            s3_logs: typing.Optional[typing.Union[typing.Union["CfnDetector.CFNS3LogsConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes whether S3 data event logs or Kubernetes audit logs will be enabled as a data source when the detector is created.

            :param kubernetes: Describes which Kuberentes data sources are enabled for a detector.
            :param malware_protection: ``CfnDetector.CFNDataSourceConfigurationsProperty.MalwareProtection``.
            :param s3_logs: Describes whether S3 data event logs are enabled as a data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNData_source_configurations_property = guardduty.CfnDetector.CFNDataSourceConfigurationsProperty(
                    kubernetes=guardduty.CfnDetector.CFNKubernetesConfigurationProperty(
                        audit_logs=guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                            enable=False
                        )
                    ),
                    malware_protection=guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty(
                        scan_ec2_instance_with_findings=guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                            ebs_volumes=False
                        )
                    ),
                    s3_logs=guardduty.CfnDetector.CFNS3LogsConfigurationProperty(
                        enable=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDetector.CFNDataSourceConfigurationsProperty.__init__)
                check_type(argname="argument kubernetes", value=kubernetes, expected_type=type_hints["kubernetes"])
                check_type(argname="argument malware_protection", value=malware_protection, expected_type=type_hints["malware_protection"])
                check_type(argname="argument s3_logs", value=s3_logs, expected_type=type_hints["s3_logs"])
            self._values: typing.Dict[str, typing.Any] = {}
            if kubernetes is not None:
                self._values["kubernetes"] = kubernetes
            if malware_protection is not None:
                self._values["malware_protection"] = malware_protection
            if s3_logs is not None:
                self._values["s3_logs"] = s3_logs

        @builtins.property
        def kubernetes(
            self,
        ) -> typing.Optional[typing.Union["CfnDetector.CFNKubernetesConfigurationProperty", _IResolvable_da3f097b]]:
            '''Describes which Kuberentes data sources are enabled for a detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-kubernetes
            '''
            result = self._values.get("kubernetes")
            return typing.cast(typing.Optional[typing.Union["CfnDetector.CFNKubernetesConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def malware_protection(
            self,
        ) -> typing.Optional[typing.Union["CfnDetector.CFNMalwareProtectionConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDetector.CFNDataSourceConfigurationsProperty.MalwareProtection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-malwareprotection
            '''
            result = self._values.get("malware_protection")
            return typing.cast(typing.Optional[typing.Union["CfnDetector.CFNMalwareProtectionConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnDetector.CFNS3LogsConfigurationProperty", _IResolvable_da3f097b]]:
            '''Describes whether S3 data event logs are enabled as a data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-s3logs
            '''
            result = self._values.get("s3_logs")
            return typing.cast(typing.Optional[typing.Union["CfnDetector.CFNS3LogsConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNDataSourceConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enable": "enable"},
    )
    class CFNKubernetesAuditLogsConfigurationProperty:
        def __init__(
            self,
            *,
            enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes which optional data sources are enabled for a detector.

            :param enable: Describes whether Kubernetes audit logs are enabled as a data source for the detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNKubernetes_audit_logs_configuration_property = guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                    enable=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDetector.CFNKubernetesAuditLogsConfigurationProperty.__init__)
                check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            self._values: typing.Dict[str, typing.Any] = {}
            if enable is not None:
                self._values["enable"] = enable

        @builtins.property
        def enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Describes whether Kubernetes audit logs are enabled as a data source for the detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html#cfn-guardduty-detector-cfnkubernetesauditlogsconfiguration-enable
            '''
            result = self._values.get("enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNKubernetesAuditLogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNKubernetesConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"audit_logs": "auditLogs"},
    )
    class CFNKubernetesConfigurationProperty:
        def __init__(
            self,
            *,
            audit_logs: typing.Optional[typing.Union[typing.Union["CfnDetector.CFNKubernetesAuditLogsConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes which Kubernetes protection data sources are enabled for the detector.

            :param audit_logs: Describes whether Kubernetes audit logs are enabled as a data source for the detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNKubernetes_configuration_property = guardduty.CfnDetector.CFNKubernetesConfigurationProperty(
                    audit_logs=guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                        enable=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDetector.CFNKubernetesConfigurationProperty.__init__)
                check_type(argname="argument audit_logs", value=audit_logs, expected_type=type_hints["audit_logs"])
            self._values: typing.Dict[str, typing.Any] = {}
            if audit_logs is not None:
                self._values["audit_logs"] = audit_logs

        @builtins.property
        def audit_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnDetector.CFNKubernetesAuditLogsConfigurationProperty", _IResolvable_da3f097b]]:
            '''Describes whether Kubernetes audit logs are enabled as a data source for the detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesconfiguration.html#cfn-guardduty-detector-cfnkubernetesconfiguration-auditlogs
            '''
            result = self._values.get("audit_logs")
            return typing.cast(typing.Optional[typing.Union["CfnDetector.CFNKubernetesAuditLogsConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNKubernetesConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scan_ec2_instance_with_findings": "scanEc2InstanceWithFindings",
        },
    )
    class CFNMalwareProtectionConfigurationProperty:
        def __init__(
            self,
            *,
            scan_ec2_instance_with_findings: typing.Optional[typing.Union[typing.Union["CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param scan_ec2_instance_with_findings: ``CfnDetector.CFNMalwareProtectionConfigurationProperty.ScanEc2InstanceWithFindings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnmalwareprotectionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNMalware_protection_configuration_property = guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty(
                    scan_ec2_instance_with_findings=guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                        ebs_volumes=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDetector.CFNMalwareProtectionConfigurationProperty.__init__)
                check_type(argname="argument scan_ec2_instance_with_findings", value=scan_ec2_instance_with_findings, expected_type=type_hints["scan_ec2_instance_with_findings"])
            self._values: typing.Dict[str, typing.Any] = {}
            if scan_ec2_instance_with_findings is not None:
                self._values["scan_ec2_instance_with_findings"] = scan_ec2_instance_with_findings

        @builtins.property
        def scan_ec2_instance_with_findings(
            self,
        ) -> typing.Optional[typing.Union["CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDetector.CFNMalwareProtectionConfigurationProperty.ScanEc2InstanceWithFindings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnmalwareprotectionconfiguration.html#cfn-guardduty-detector-cfnmalwareprotectionconfiguration-scanec2instancewithfindings
            '''
            result = self._values.get("scan_ec2_instance_with_findings")
            return typing.cast(typing.Optional[typing.Union["CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNMalwareProtectionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNS3LogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enable": "enable"},
    )
    class CFNS3LogsConfigurationProperty:
        def __init__(
            self,
            *,
            enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes whether S3 data event logs will be enabled as a data source when the detector is created.

            :param enable: The status of S3 data event logs as a data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNS3_logs_configuration_property = guardduty.CfnDetector.CFNS3LogsConfigurationProperty(
                    enable=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDetector.CFNS3LogsConfigurationProperty.__init__)
                check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            self._values: typing.Dict[str, typing.Any] = {}
            if enable is not None:
                self._values["enable"] = enable

        @builtins.property
        def enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The status of S3 data event logs as a data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html#cfn-guardduty-detector-cfns3logsconfiguration-enable
            '''
            result = self._values.get("enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNS3LogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"ebs_volumes": "ebsVolumes"},
    )
    class CFNScanEc2InstanceWithFindingsConfigurationProperty:
        def __init__(
            self,
            *,
            ebs_volumes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param ebs_volumes: ``CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty.EbsVolumes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnscanec2instancewithfindingsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNScan_ec2_instance_with_findings_configuration_property = guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                    ebs_volumes=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty.__init__)
                check_type(argname="argument ebs_volumes", value=ebs_volumes, expected_type=type_hints["ebs_volumes"])
            self._values: typing.Dict[str, typing.Any] = {}
            if ebs_volumes is not None:
                self._values["ebs_volumes"] = ebs_volumes

        @builtins.property
        def ebs_volumes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty.EbsVolumes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnscanec2instancewithfindingsconfiguration.html#cfn-guardduty-detector-cfnscanec2instancewithfindingsconfiguration-ebsvolumes
            '''
            result = self._values.get("ebs_volumes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNScanEc2InstanceWithFindingsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "enable": "enable",
        "data_sources": "dataSources",
        "finding_publishing_frequency": "findingPublishingFrequency",
        "tags": "tags",
    },
)
class CfnDetectorProps:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, _IResolvable_da3f097b],
        data_sources: typing.Optional[typing.Union[typing.Union[CfnDetector.CFNDataSourceConfigurationsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDetector``.

        :param enable: Specifies whether the detector is to be enabled on creation.
        :param data_sources: Describes which data sources will be enabled for the detector.
        :param finding_publishing_frequency: Specifies how frequently updated findings are exported.
        :param tags: ``AWS::GuardDuty::Detector.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_detector_props = guardduty.CfnDetectorProps(
                enable=False,
            
                # the properties below are optional
                data_sources=guardduty.CfnDetector.CFNDataSourceConfigurationsProperty(
                    kubernetes=guardduty.CfnDetector.CFNKubernetesConfigurationProperty(
                        audit_logs=guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                            enable=False
                        )
                    ),
                    malware_protection=guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty(
                        scan_ec2_instance_with_findings=guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                            ebs_volumes=False
                        )
                    ),
                    s3_logs=guardduty.CfnDetector.CFNS3LogsConfigurationProperty(
                        enable=False
                    )
                ),
                finding_publishing_frequency="findingPublishingFrequency",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDetectorProps.__init__)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument data_sources", value=data_sources, expected_type=type_hints["data_sources"])
            check_type(argname="argument finding_publishing_frequency", value=finding_publishing_frequency, expected_type=type_hints["finding_publishing_frequency"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable": enable,
        }
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if finding_publishing_frequency is not None:
            self._values["finding_publishing_frequency"] = finding_publishing_frequency
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Specifies whether the detector is to be enabled on creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
        '''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[CfnDetector.CFNDataSourceConfigurationsProperty, _IResolvable_da3f097b]]:
        '''Describes which data sources will be enabled for the detector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-datasources
        '''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.Union[CfnDetector.CFNDataSourceConfigurationsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''Specifies how frequently updated findings are exported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
        '''
        result = self._values.get("finding_publishing_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::GuardDuty::Detector.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnFilter",
):
    '''A CloudFormation ``AWS::GuardDuty::Filter``.

    The ``AWS::GuardDuty::Filter`` resource specifies a new filter defined by the provided ``findingCriteria`` .

    :cloudformationResource: AWS::GuardDuty::Filter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        # criterion: Any
        
        cfn_filter = guardduty.CfnFilter(self, "MyCfnFilter",
            action="action",
            description="description",
            detector_id="detectorId",
            finding_criteria=guardduty.CfnFilter.FindingCriteriaProperty(
                criterion=criterion,
                item_type=guardduty.CfnFilter.ConditionProperty(
                    eq=["eq"],
                    equal_to=["equalTo"],
                    greater_than=123,
                    greater_than_or_equal=123,
                    gt=123,
                    gte=123,
                    less_than=123,
                    less_than_or_equal=123,
                    lt=123,
                    lte=123,
                    neq=["neq"],
                    not_equals=["notEquals"]
                )
            ),
            name="name",
            rank=123,
        
            # the properties below are optional
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
        action: builtins.str,
        description: builtins.str,
        detector_id: builtins.str,
        finding_criteria: typing.Union[typing.Union["CfnFilter.FindingCriteriaProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        rank: jsii.Number,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::Filter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: Specifies the action that is to be applied to the findings that match the filter.
        :param description: The description of the filter.
        :param detector_id: The ID of the detector belonging to the GuardDuty account that you want to create a filter for.
        :param finding_criteria: Represents the criteria to be used in the filter for querying findings.
        :param name: The name of the filter. Minimum length of 3. Maximum length of 64. Valid characters include alphanumeric characters, dot (.), underscore (_), and dash (-). Spaces are not allowed.
        :param rank: ``AWS::GuardDuty::Filter.Rank``.
        :param tags: ``AWS::GuardDuty::Filter.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFilter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFilterProps(
            action=action,
            description=description,
            detector_id=detector_id,
            finding_criteria=finding_criteria,
            name=name,
            rank=rank,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFilter.inspect)
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
            type_hints = typing.get_type_hints(CfnFilter._render_properties)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::GuardDuty::Filter.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        '''Specifies the action that is to be applied to the findings that match the filter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
        '''
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFilter, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the filter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFilter, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The ID of the detector belonging to the GuardDuty account that you want to create a filter for.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFilter, "detector_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(
        self,
    ) -> typing.Union["CfnFilter.FindingCriteriaProperty", _IResolvable_da3f097b]:
        '''Represents the criteria to be used in the filter for querying findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
        '''
        return typing.cast(typing.Union["CfnFilter.FindingCriteriaProperty", _IResolvable_da3f097b], jsii.get(self, "findingCriteria"))

    @finding_criteria.setter
    def finding_criteria(
        self,
        value: typing.Union["CfnFilter.FindingCriteriaProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFilter, "finding_criteria").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingCriteria", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the filter.

        Minimum length of 3. Maximum length of 64. Valid characters include alphanumeric characters, dot (.), underscore (_), and dash (-). Spaces are not allowed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFilter, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rank")
    def rank(self) -> jsii.Number:
        '''``AWS::GuardDuty::Filter.Rank``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
        '''
        return typing.cast(jsii.Number, jsii.get(self, "rank"))

    @rank.setter
    def rank(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFilter, "rank").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rank", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnFilter.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "eq": "eq",
            "equal_to": "equalTo",
            "greater_than": "greaterThan",
            "greater_than_or_equal": "greaterThanOrEqual",
            "gt": "gt",
            "gte": "gte",
            "less_than": "lessThan",
            "less_than_or_equal": "lessThanOrEqual",
            "lt": "lt",
            "lte": "lte",
            "neq": "neq",
            "not_equals": "notEquals",
        },
    )
    class ConditionProperty:
        def __init__(
            self,
            *,
            eq: typing.Optional[typing.Sequence[builtins.str]] = None,
            equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
            greater_than: typing.Optional[jsii.Number] = None,
            greater_than_or_equal: typing.Optional[jsii.Number] = None,
            gt: typing.Optional[jsii.Number] = None,
            gte: typing.Optional[jsii.Number] = None,
            less_than: typing.Optional[jsii.Number] = None,
            less_than_or_equal: typing.Optional[jsii.Number] = None,
            lt: typing.Optional[jsii.Number] = None,
            lte: typing.Optional[jsii.Number] = None,
            neq: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the condition to apply to a single field when filtering through  findings.

            :param eq: Represents the equal condition to apply to a single field when querying for findings.
            :param equal_to: Represents an *equal* ** condition to be applied to a single field when querying for findings.
            :param greater_than: Represents a *greater than* condition to be applied to a single field when querying for findings.
            :param greater_than_or_equal: Represents a *greater than or equal* condition to be applied to a single field when querying for findings.
            :param gt: Represents a *greater than* condition to be applied to a single field when querying for findings.
            :param gte: Represents the greater than or equal condition to apply to a single field when querying for findings.
            :param less_than: Represents a *less than* condition to be applied to a single field when querying for findings.
            :param less_than_or_equal: Represents a *less than or equal* condition to be applied to a single field when querying for findings.
            :param lt: Represents the less than condition to apply to a single field when querying for findings.
            :param lte: Represents the less than or equal condition to apply to a single field when querying for findings.
            :param neq: Represents the not equal condition to apply to a single field when querying for findings.
            :param not_equals: Represents a *not equal* ** condition to be applied to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                condition_property = guardduty.CfnFilter.ConditionProperty(
                    eq=["eq"],
                    equal_to=["equalTo"],
                    greater_than=123,
                    greater_than_or_equal=123,
                    gt=123,
                    gte=123,
                    less_than=123,
                    less_than_or_equal=123,
                    lt=123,
                    lte=123,
                    neq=["neq"],
                    not_equals=["notEquals"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFilter.ConditionProperty.__init__)
                check_type(argname="argument eq", value=eq, expected_type=type_hints["eq"])
                check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
                check_type(argname="argument greater_than", value=greater_than, expected_type=type_hints["greater_than"])
                check_type(argname="argument greater_than_or_equal", value=greater_than_or_equal, expected_type=type_hints["greater_than_or_equal"])
                check_type(argname="argument gt", value=gt, expected_type=type_hints["gt"])
                check_type(argname="argument gte", value=gte, expected_type=type_hints["gte"])
                check_type(argname="argument less_than", value=less_than, expected_type=type_hints["less_than"])
                check_type(argname="argument less_than_or_equal", value=less_than_or_equal, expected_type=type_hints["less_than_or_equal"])
                check_type(argname="argument lt", value=lt, expected_type=type_hints["lt"])
                check_type(argname="argument lte", value=lte, expected_type=type_hints["lte"])
                check_type(argname="argument neq", value=neq, expected_type=type_hints["neq"])
                check_type(argname="argument not_equals", value=not_equals, expected_type=type_hints["not_equals"])
            self._values: typing.Dict[str, typing.Any] = {}
            if eq is not None:
                self._values["eq"] = eq
            if equal_to is not None:
                self._values["equal_to"] = equal_to
            if greater_than is not None:
                self._values["greater_than"] = greater_than
            if greater_than_or_equal is not None:
                self._values["greater_than_or_equal"] = greater_than_or_equal
            if gt is not None:
                self._values["gt"] = gt
            if gte is not None:
                self._values["gte"] = gte
            if less_than is not None:
                self._values["less_than"] = less_than
            if less_than_or_equal is not None:
                self._values["less_than_or_equal"] = less_than_or_equal
            if lt is not None:
                self._values["lt"] = lt
            if lte is not None:
                self._values["lte"] = lte
            if neq is not None:
                self._values["neq"] = neq
            if not_equals is not None:
                self._values["not_equals"] = not_equals

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents the equal condition to apply to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def equal_to(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents an *equal* ** condition to be applied to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-equals
            '''
            result = self._values.get("equal_to")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def greater_than(self) -> typing.Optional[jsii.Number]:
            '''Represents a *greater than* condition to be applied to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-greaterthan
            '''
            result = self._values.get("greater_than")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def greater_than_or_equal(self) -> typing.Optional[jsii.Number]:
            '''Represents a *greater than or equal* condition to be applied to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-greaterthanorequal
            '''
            result = self._values.get("greater_than_or_equal")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gt(self) -> typing.Optional[jsii.Number]:
            '''Represents a *greater than* condition to be applied to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gt
            '''
            result = self._values.get("gt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gte(self) -> typing.Optional[jsii.Number]:
            '''Represents the greater than or equal condition to apply to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gte
            '''
            result = self._values.get("gte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def less_than(self) -> typing.Optional[jsii.Number]:
            '''Represents a *less than* condition to be applied to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lessthan
            '''
            result = self._values.get("less_than")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def less_than_or_equal(self) -> typing.Optional[jsii.Number]:
            '''Represents a *less than or equal* condition to be applied to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lessthanorequal
            '''
            result = self._values.get("less_than_or_equal")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lt(self) -> typing.Optional[jsii.Number]:
            '''Represents the less than condition to apply to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lt
            '''
            result = self._values.get("lt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lte(self) -> typing.Optional[jsii.Number]:
            '''Represents the less than or equal condition to apply to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lte
            '''
            result = self._values.get("lte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents the not equal condition to apply to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-neq
            '''
            result = self._values.get("neq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_equals(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents a *not equal* ** condition to be applied to a single field when querying for findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-notequals
            '''
            result = self._values.get("not_equals")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnFilter.FindingCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"criterion": "criterion", "item_type": "itemType"},
    )
    class FindingCriteriaProperty:
        def __init__(
            self,
            *,
            criterion: typing.Any = None,
            item_type: typing.Optional[typing.Union[typing.Union["CfnFilter.ConditionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents a map of finding properties that match specified conditions and values when querying findings.

            :param criterion: Represents a map of finding properties that match specified conditions and values when querying findings. For a mapping of JSON criterion to their console equivalent see `Finding criteria <https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html#filter_criteria>`_ . The following are the available criterion: - accountId - region - confidence - id - resource.accessKeyDetails.accessKeyId - resource.accessKeyDetails.principalId - resource.accessKeyDetails.userName - resource.accessKeyDetails.userType - resource.instanceDetails.iamInstanceProfile.id - resource.instanceDetails.imageId - resource.instanceDetails.instanceId - resource.instanceDetails.outpostArn - resource.instanceDetails.networkInterfaces.ipv6Addresses - resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress - resource.instanceDetails.networkInterfaces.publicDnsName - resource.instanceDetails.networkInterfaces.publicIp - resource.instanceDetails.networkInterfaces.securityGroups.groupId - resource.instanceDetails.networkInterfaces.securityGroups.groupName - resource.instanceDetails.networkInterfaces.subnetId - resource.instanceDetails.networkInterfaces.vpcId - resource.instanceDetails.tags.key - resource.instanceDetails.tags.value - resource.resourceType - service.action.actionType - service.action.awsApiCallAction.api - service.action.awsApiCallAction.callerType - service.action.awsApiCallAction.errorCode - service.action.awsApiCallAction.remoteIpDetails.city.cityName - service.action.awsApiCallAction.remoteIpDetails.country.countryName - service.action.awsApiCallAction.remoteIpDetails.ipAddressV4 - service.action.awsApiCallAction.remoteIpDetails.organization.asn - service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg - service.action.awsApiCallAction.serviceName - service.action.dnsRequestAction.domain - service.action.networkConnectionAction.blocked - service.action.networkConnectionAction.connectionDirection - service.action.networkConnectionAction.localPortDetails.port - service.action.networkConnectionAction.protocol - service.action.networkConnectionAction.localIpDetails.ipAddressV4 - service.action.networkConnectionAction.remoteIpDetails.city.cityName - service.action.networkConnectionAction.remoteIpDetails.country.countryName - service.action.networkConnectionAction.remoteIpDetails.ipAddressV4 - service.action.networkConnectionAction.remoteIpDetails.organization.asn - service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg - service.action.networkConnectionAction.remotePortDetails.port - service.additionalInfo.threatListName - service.archived When this attribute is set to TRUE, only archived findings are listed. When it's set to FALSE, only unarchived findings are listed. When this attribute is not set, all existing findings are listed. - service.resourceRole - severity - type - updatedAt Type: ISO 8601 string format: YYYY-MM-DDTHH:MM:SS.SSSZ or YYYY-MM-DDTHH:MM:SSZ depending on whether the value contains milliseconds.
            :param item_type: Specifies the condition to be applied to a single field when filtering through findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                # criterion: Any
                
                finding_criteria_property = guardduty.CfnFilter.FindingCriteriaProperty(
                    criterion=criterion,
                    item_type=guardduty.CfnFilter.ConditionProperty(
                        eq=["eq"],
                        equal_to=["equalTo"],
                        greater_than=123,
                        greater_than_or_equal=123,
                        gt=123,
                        gte=123,
                        less_than=123,
                        less_than_or_equal=123,
                        lt=123,
                        lte=123,
                        neq=["neq"],
                        not_equals=["notEquals"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFilter.FindingCriteriaProperty.__init__)
                check_type(argname="argument criterion", value=criterion, expected_type=type_hints["criterion"])
                check_type(argname="argument item_type", value=item_type, expected_type=type_hints["item_type"])
            self._values: typing.Dict[str, typing.Any] = {}
            if criterion is not None:
                self._values["criterion"] = criterion
            if item_type is not None:
                self._values["item_type"] = item_type

        @builtins.property
        def criterion(self) -> typing.Any:
            '''Represents a map of finding properties that match specified conditions and values when querying findings.

            For a mapping of JSON criterion to their console equivalent see `Finding criteria <https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html#filter_criteria>`_ . The following are the available criterion:

            - accountId
            - region
            - confidence
            - id
            - resource.accessKeyDetails.accessKeyId
            - resource.accessKeyDetails.principalId
            - resource.accessKeyDetails.userName
            - resource.accessKeyDetails.userType
            - resource.instanceDetails.iamInstanceProfile.id
            - resource.instanceDetails.imageId
            - resource.instanceDetails.instanceId
            - resource.instanceDetails.outpostArn
            - resource.instanceDetails.networkInterfaces.ipv6Addresses
            - resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress
            - resource.instanceDetails.networkInterfaces.publicDnsName
            - resource.instanceDetails.networkInterfaces.publicIp
            - resource.instanceDetails.networkInterfaces.securityGroups.groupId
            - resource.instanceDetails.networkInterfaces.securityGroups.groupName
            - resource.instanceDetails.networkInterfaces.subnetId
            - resource.instanceDetails.networkInterfaces.vpcId
            - resource.instanceDetails.tags.key
            - resource.instanceDetails.tags.value
            - resource.resourceType
            - service.action.actionType
            - service.action.awsApiCallAction.api
            - service.action.awsApiCallAction.callerType
            - service.action.awsApiCallAction.errorCode
            - service.action.awsApiCallAction.remoteIpDetails.city.cityName
            - service.action.awsApiCallAction.remoteIpDetails.country.countryName
            - service.action.awsApiCallAction.remoteIpDetails.ipAddressV4
            - service.action.awsApiCallAction.remoteIpDetails.organization.asn
            - service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg
            - service.action.awsApiCallAction.serviceName
            - service.action.dnsRequestAction.domain
            - service.action.networkConnectionAction.blocked
            - service.action.networkConnectionAction.connectionDirection
            - service.action.networkConnectionAction.localPortDetails.port
            - service.action.networkConnectionAction.protocol
            - service.action.networkConnectionAction.localIpDetails.ipAddressV4
            - service.action.networkConnectionAction.remoteIpDetails.city.cityName
            - service.action.networkConnectionAction.remoteIpDetails.country.countryName
            - service.action.networkConnectionAction.remoteIpDetails.ipAddressV4
            - service.action.networkConnectionAction.remoteIpDetails.organization.asn
            - service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg
            - service.action.networkConnectionAction.remotePortDetails.port
            - service.additionalInfo.threatListName
            - service.archived

            When this attribute is set to TRUE, only archived findings are listed. When it's set to FALSE, only unarchived findings are listed. When this attribute is not set, all existing findings are listed.

            - service.resourceRole
            - severity
            - type
            - updatedAt

            Type: ISO 8601 string format: YYYY-MM-DDTHH:MM:SS.SSSZ or YYYY-MM-DDTHH:MM:SSZ depending on whether the value contains milliseconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-criterion
            '''
            result = self._values.get("criterion")
            return typing.cast(typing.Any, result)

        @builtins.property
        def item_type(
            self,
        ) -> typing.Optional[typing.Union["CfnFilter.ConditionProperty", _IResolvable_da3f097b]]:
            '''Specifies the condition to be applied to a single field when filtering through findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-itemtype
            '''
            result = self._values.get("item_type")
            return typing.cast(typing.Optional[typing.Union["CfnFilter.ConditionProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "description": "description",
        "detector_id": "detectorId",
        "finding_criteria": "findingCriteria",
        "name": "name",
        "rank": "rank",
        "tags": "tags",
    },
)
class CfnFilterProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        description: builtins.str,
        detector_id: builtins.str,
        finding_criteria: typing.Union[typing.Union[CfnFilter.FindingCriteriaProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        rank: jsii.Number,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFilter``.

        :param action: Specifies the action that is to be applied to the findings that match the filter.
        :param description: The description of the filter.
        :param detector_id: The ID of the detector belonging to the GuardDuty account that you want to create a filter for.
        :param finding_criteria: Represents the criteria to be used in the filter for querying findings.
        :param name: The name of the filter. Minimum length of 3. Maximum length of 64. Valid characters include alphanumeric characters, dot (.), underscore (_), and dash (-). Spaces are not allowed.
        :param rank: ``AWS::GuardDuty::Filter.Rank``.
        :param tags: ``AWS::GuardDuty::Filter.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            # criterion: Any
            
            cfn_filter_props = guardduty.CfnFilterProps(
                action="action",
                description="description",
                detector_id="detectorId",
                finding_criteria=guardduty.CfnFilter.FindingCriteriaProperty(
                    criterion=criterion,
                    item_type=guardduty.CfnFilter.ConditionProperty(
                        eq=["eq"],
                        equal_to=["equalTo"],
                        greater_than=123,
                        greater_than_or_equal=123,
                        gt=123,
                        gte=123,
                        less_than=123,
                        less_than_or_equal=123,
                        lt=123,
                        lte=123,
                        neq=["neq"],
                        not_equals=["notEquals"]
                    )
                ),
                name="name",
                rank=123,
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFilterProps.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument finding_criteria", value=finding_criteria, expected_type=type_hints["finding_criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rank", value=rank, expected_type=type_hints["rank"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "description": description,
            "detector_id": detector_id,
            "finding_criteria": finding_criteria,
            "name": name,
            "rank": rank,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action(self) -> builtins.str:
        '''Specifies the action that is to be applied to the findings that match the filter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the filter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The ID of the detector belonging to the GuardDuty account that you want to create a filter for.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def finding_criteria(
        self,
    ) -> typing.Union[CfnFilter.FindingCriteriaProperty, _IResolvable_da3f097b]:
        '''Represents the criteria to be used in the filter for querying findings.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
        '''
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return typing.cast(typing.Union[CfnFilter.FindingCriteriaProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the filter.

        Minimum length of 3. Maximum length of 64. Valid characters include alphanumeric characters, dot (.), underscore (_), and dash (-). Spaces are not allowed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rank(self) -> jsii.Number:
        '''``AWS::GuardDuty::Filter.Rank``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
        '''
        result = self._values.get("rank")
        assert result is not None, "Required property 'rank' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::GuardDuty::Filter.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIPSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnIPSet",
):
    '''A CloudFormation ``AWS::GuardDuty::IPSet``.

    The ``AWS::GuardDuty::IPSet`` resource specifies a new ``IPSet`` . An ``IPSet`` is a list of trusted IP addresses from which secure communication is allowed with AWS infrastructure and applications.

    :cloudformationResource: AWS::GuardDuty::IPSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_iPSet = guardduty.CfnIPSet(self, "MyCfnIPSet",
            activate=False,
            detector_id="detectorId",
            format="format",
            location="location",
        
            # the properties below are optional
            name="name",
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
        activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::IPSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param activate: Indicates whether or not uses the ``IPSet`` .
        :param detector_id: The unique ID of the detector of the GuardDuty account that you want to create an IPSet for.
        :param format: The format of the file that contains the IPSet.
        :param location: The URI of the file that contains the IPSet.
        :param name: The user-friendly name to identify the IPSet. Allowed characters are alphanumerics, spaces, hyphens (-), and underscores (_).
        :param tags: ``AWS::GuardDuty::IPSet.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnIPSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIPSetProps(
            activate=activate,
            detector_id=detector_id,
            format=format,
            location=location,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnIPSet.inspect)
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
            type_hints = typing.get_type_hints(CfnIPSet._render_properties)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::GuardDuty::IPSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Indicates whether or not  uses the ``IPSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "activate"))

    @activate.setter
    def activate(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnIPSet, "activate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty account that you want to create an IPSet for.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnIPSet, "detector_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''The format of the file that contains the IPSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        '''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnIPSet, "format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        '''The URI of the file that contains the IPSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        '''
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnIPSet, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name to identify the IPSet.

        Allowed characters are alphanumerics, spaces, hyphens (-), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnIPSet, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnIPSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "activate": "activate",
        "detector_id": "detectorId",
        "format": "format",
        "location": "location",
        "name": "name",
        "tags": "tags",
    },
)
class CfnIPSetProps:
    def __init__(
        self,
        *,
        activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIPSet``.

        :param activate: Indicates whether or not uses the ``IPSet`` .
        :param detector_id: The unique ID of the detector of the GuardDuty account that you want to create an IPSet for.
        :param format: The format of the file that contains the IPSet.
        :param location: The URI of the file that contains the IPSet.
        :param name: The user-friendly name to identify the IPSet. Allowed characters are alphanumerics, spaces, hyphens (-), and underscores (_).
        :param tags: ``AWS::GuardDuty::IPSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_iPSet_props = guardduty.CfnIPSetProps(
                activate=False,
                detector_id="detectorId",
                format="format",
                location="location",
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnIPSetProps.__init__)
            check_type(argname="argument activate", value=activate, expected_type=type_hints["activate"])
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "activate": activate,
            "detector_id": detector_id,
            "format": format,
            "location": location,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def activate(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Indicates whether or not  uses the ``IPSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        '''
        result = self._values.get("activate")
        assert result is not None, "Required property 'activate' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty account that you want to create an IPSet for.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''The format of the file that contains the IPSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The URI of the file that contains the IPSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name to identify the IPSet.

        Allowed characters are alphanumerics, spaces, hyphens (-), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::GuardDuty::IPSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIPSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnMaster",
):
    '''A CloudFormation ``AWS::GuardDuty::Master``.

    You can use the ``AWS::GuardDuty::Master`` resource in a  member account to accept an invitation from a  administrator account. The invitation to the member account must be sent prior to using the ``AWS::GuardDuty::Master`` resource to accept the administrator account's invitation. You can invite a member account by using the ``InviteMembers`` operation of the  API, or by creating an ``AWS::GuardDuty::Member`` resource.

    :cloudformationResource: AWS::GuardDuty::Master
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_master = guardduty.CfnMaster(self, "MyCfnMaster",
            detector_id="detectorId",
            master_id="masterId",
        
            # the properties below are optional
            invitation_id="invitationId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        detector_id: builtins.str,
        master_id: builtins.str,
        invitation_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::Master``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detector_id: The unique ID of the detector of the GuardDuty member account.
        :param master_id: The AWS account ID of the account designated as the administrator account.
        :param invitation_id: The ID of the invitation that is sent to the account designated as a member account. You can find the invitation ID by using the ListInvitation action of the API.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMaster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMasterProps(
            detector_id=detector_id, master_id=master_id, invitation_id=invitation_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMaster.inspect)
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
            type_hints = typing.get_type_hints(CfnMaster._render_properties)
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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty member account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMaster, "detector_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterId")
    def master_id(self) -> builtins.str:
        '''The AWS account ID of the account designated as the  administrator account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
        '''
        return typing.cast(builtins.str, jsii.get(self, "masterId"))

    @master_id.setter
    def master_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMaster, "master_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="invitationId")
    def invitation_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the invitation that is sent to the account designated as a member account.

        You can find the invitation ID by using the ListInvitation action of the  API.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invitationId"))

    @invitation_id.setter
    def invitation_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMaster, "invitation_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invitationId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnMasterProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "master_id": "masterId",
        "invitation_id": "invitationId",
    },
)
class CfnMasterProps:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        master_id: builtins.str,
        invitation_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMaster``.

        :param detector_id: The unique ID of the detector of the GuardDuty member account.
        :param master_id: The AWS account ID of the account designated as the administrator account.
        :param invitation_id: The ID of the invitation that is sent to the account designated as a member account. You can find the invitation ID by using the ListInvitation action of the API.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_master_props = guardduty.CfnMasterProps(
                detector_id="detectorId",
                master_id="masterId",
            
                # the properties below are optional
                invitation_id="invitationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMasterProps.__init__)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument master_id", value=master_id, expected_type=type_hints["master_id"])
            check_type(argname="argument invitation_id", value=invitation_id, expected_type=type_hints["invitation_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "detector_id": detector_id,
            "master_id": master_id,
        }
        if invitation_id is not None:
            self._values["invitation_id"] = invitation_id

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty member account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_id(self) -> builtins.str:
        '''The AWS account ID of the account designated as the  administrator account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
        '''
        result = self._values.get("master_id")
        assert result is not None, "Required property 'master_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invitation_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the invitation that is sent to the account designated as a member account.

        You can find the invitation ID by using the ListInvitation action of the  API.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
        '''
        result = self._values.get("invitation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMasterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMember(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnMember",
):
    '''A CloudFormation ``AWS::GuardDuty::Member``.

    You can use the ``AWS::GuardDuty::Member`` resource to add an AWS account as a  member account to the current  administrator account. If the value of the ``Status`` property is not provided or is set to ``Created`` , a member account is created but not invited. If the value of the ``Status`` property is set to ``Invited`` , a member account is created and invited. An ``AWS::GuardDuty::Member`` resource must be created with the ``Status`` property set to ``Invited`` before the ``AWS::GuardDuty::Master`` resource can be created in a  member account.

    :cloudformationResource: AWS::GuardDuty::Member
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_member = guardduty.CfnMember(self, "MyCfnMember",
            detector_id="detectorId",
            email="email",
            member_id="memberId",
        
            # the properties below are optional
            disable_email_notification=False,
            message="message",
            status="status"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        detector_id: builtins.str,
        email: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        message: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::Member``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detector_id: The ID of the detector associated with the service to add the member to.
        :param email: The email address associated with the member account.
        :param member_id: The AWS account ID of the account to designate as a member.
        :param disable_email_notification: Specifies whether or not to disable email notification for the member account that you invite.
        :param message: The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.
        :param status: You can use the ``Status`` property to update the status of the relationship between the member account and its administrator account. Valid values are ``Created`` and ``Invited`` when using an ``AWS::GuardDuty::Member`` resource. If the value for this property is not provided or set to ``Created`` , a member account is created but not invited. If the value of this property is set to ``Invited`` , a member account is created and invited.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMember.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMemberProps(
            detector_id=detector_id,
            email=email,
            member_id=member_id,
            disable_email_notification=disable_email_notification,
            message=message,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMember.inspect)
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
            type_hints = typing.get_type_hints(CfnMember._render_properties)
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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The ID of the detector associated with the  service to add the member to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMember, "detector_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        '''The email address associated with the member account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
        '''
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMember, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> builtins.str:
        '''The AWS account ID of the account to designate as a member.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
        '''
        return typing.cast(builtins.str, jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMember, "member_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="disableEmailNotification")
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether or not to disable email notification for the member account that you invite.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "disableEmailNotification"))

    @disable_email_notification.setter
    def disable_email_notification(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMember, "disable_email_notification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEmailNotification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Optional[builtins.str]:
        '''The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "message"))

    @message.setter
    def message(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMember, "message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''You can use the ``Status`` property to update the status of the relationship between the member account and its administrator account.

        Valid values are ``Created`` and ``Invited`` when using an ``AWS::GuardDuty::Member`` resource. If the value for this property is not provided or set to ``Created`` , a member account is created but not invited. If the value of this property is set to ``Invited`` , a member account is created and invited.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMember, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnMemberProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "email": "email",
        "member_id": "memberId",
        "disable_email_notification": "disableEmailNotification",
        "message": "message",
        "status": "status",
    },
)
class CfnMemberProps:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        email: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        message: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMember``.

        :param detector_id: The ID of the detector associated with the service to add the member to.
        :param email: The email address associated with the member account.
        :param member_id: The AWS account ID of the account to designate as a member.
        :param disable_email_notification: Specifies whether or not to disable email notification for the member account that you invite.
        :param message: The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.
        :param status: You can use the ``Status`` property to update the status of the relationship between the member account and its administrator account. Valid values are ``Created`` and ``Invited`` when using an ``AWS::GuardDuty::Member`` resource. If the value for this property is not provided or set to ``Created`` , a member account is created but not invited. If the value of this property is set to ``Invited`` , a member account is created and invited.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_member_props = guardduty.CfnMemberProps(
                detector_id="detectorId",
                email="email",
                member_id="memberId",
            
                # the properties below are optional
                disable_email_notification=False,
                message="message",
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMemberProps.__init__)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
            check_type(argname="argument disable_email_notification", value=disable_email_notification, expected_type=type_hints["disable_email_notification"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {
            "detector_id": detector_id,
            "email": email,
            "member_id": member_id,
        }
        if disable_email_notification is not None:
            self._values["disable_email_notification"] = disable_email_notification
        if message is not None:
            self._values["message"] = message
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The ID of the detector associated with the  service to add the member to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The email address associated with the member account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(self) -> builtins.str:
        '''The AWS account ID of the account to designate as a member.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether or not to disable email notification for the member account that you invite.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
        '''
        result = self._values.get("disable_email_notification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''You can use the ``Status`` property to update the status of the relationship between the member account and its administrator account.

        Valid values are ``Created`` and ``Invited`` when using an ``AWS::GuardDuty::Member`` resource. If the value for this property is not provided or set to ``Created`` , a member account is created but not invited. If the value of this property is set to ``Invited`` , a member account is created and invited.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnThreatIntelSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnThreatIntelSet",
):
    '''A CloudFormation ``AWS::GuardDuty::ThreatIntelSet``.

    The ``AWS::GuardDuty::ThreatIntelSet`` resource specifies a new ``ThreatIntelSet`` . A ``ThreatIntelSet`` consists of known malicious IP addresses.  generates findings based on the ``ThreatIntelSet`` when it is activated.

    :cloudformationResource: AWS::GuardDuty::ThreatIntelSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_threat_intel_set = guardduty.CfnThreatIntelSet(self, "MyCfnThreatIntelSet",
            activate=False,
            detector_id="detectorId",
            format="format",
            location="location",
        
            # the properties below are optional
            name="name",
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
        activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::ThreatIntelSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param activate: A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        :param detector_id: The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.
        :param format: The format of the file that contains the ThreatIntelSet.
        :param location: The URI of the file that contains the ThreatIntelSet.
        :param name: A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        :param tags: ``AWS::GuardDuty::ThreatIntelSet.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThreatIntelSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnThreatIntelSetProps(
            activate=activate,
            detector_id=detector_id,
            format=format,
            location=location,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThreatIntelSet.inspect)
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
            type_hints = typing.get_type_hints(CfnThreatIntelSet._render_properties)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::GuardDuty::ThreatIntelSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "activate"))

    @activate.setter
    def activate(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThreatIntelSet, "activate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThreatIntelSet, "detector_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''The format of the file that contains the ThreatIntelSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
        '''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThreatIntelSet, "format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        '''The URI of the file that contains the ThreatIntelSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
        '''
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThreatIntelSet, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThreatIntelSet, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnThreatIntelSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "activate": "activate",
        "detector_id": "detectorId",
        "format": "format",
        "location": "location",
        "name": "name",
        "tags": "tags",
    },
)
class CfnThreatIntelSetProps:
    def __init__(
        self,
        *,
        activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnThreatIntelSet``.

        :param activate: A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        :param detector_id: The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.
        :param format: The format of the file that contains the ThreatIntelSet.
        :param location: The URI of the file that contains the ThreatIntelSet.
        :param name: A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        :param tags: ``AWS::GuardDuty::ThreatIntelSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_threat_intel_set_props = guardduty.CfnThreatIntelSetProps(
                activate=False,
                detector_id="detectorId",
                format="format",
                location="location",
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThreatIntelSetProps.__init__)
            check_type(argname="argument activate", value=activate, expected_type=type_hints["activate"])
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "activate": activate,
            "detector_id": detector_id,
            "format": format,
            "location": location,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def activate(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
        '''
        result = self._values.get("activate")
        assert result is not None, "Required property 'activate' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''The format of the file that contains the ThreatIntelSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The URI of the file that contains the ThreatIntelSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::GuardDuty::ThreatIntelSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThreatIntelSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDetector",
    "CfnDetectorProps",
    "CfnFilter",
    "CfnFilterProps",
    "CfnIPSet",
    "CfnIPSetProps",
    "CfnMaster",
    "CfnMasterProps",
    "CfnMember",
    "CfnMemberProps",
    "CfnThreatIntelSet",
    "CfnThreatIntelSetProps",
]

publication.publish()
