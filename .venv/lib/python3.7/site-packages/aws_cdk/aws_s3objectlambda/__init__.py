'''
# AWS::S3ObjectLambda Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3objectlambda as s3objectlambda
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3ObjectLambda construct libraries](https://constructs.dev/search?q=s3objectlambda)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3ObjectLambda resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3ObjectLambda.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-s3objectlambda-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3ObjectLambda](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3ObjectLambda.html).

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
class CfnAccessPoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint",
):
    '''A CloudFormation ``AWS::S3ObjectLambda::AccessPoint``.

    The ``AWS::S3ObjectLambda::AccessPoint`` resource specifies an Object Lambda Access Point used to access a bucket.

    :cloudformationResource: AWS::S3ObjectLambda::AccessPoint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3objectlambda as s3objectlambda
        
        # content_transformation: Any
        
        cfn_access_point = s3objectlambda.CfnAccessPoint(self, "MyCfnAccessPoint",
            object_lambda_configuration=s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty(
                supporting_access_point="supportingAccessPoint",
                transformation_configurations=[s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
                    actions=["actions"],
                    content_transformation=content_transformation
                )],
        
                # the properties below are optional
                allowed_features=["allowedFeatures"],
                cloud_watch_metrics_enabled=False
            ),
        
            # the properties below are optional
            name="name"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        object_lambda_configuration: typing.Union[typing.Union["CfnAccessPoint.ObjectLambdaConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::S3ObjectLambda::AccessPoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param object_lambda_configuration: A configuration used when creating an Object Lambda Access Point.
        :param name: The name of this access point.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccessPoint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPointProps(
            object_lambda_configuration=object_lambda_configuration, name=name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccessPoint.inspect)
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
            type_hints = typing.get_type_hints(CfnAccessPoint._render_properties)
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
        '''Specifies the ARN for the Object Lambda Access Point.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The date and time when the specified Object Lambda Access Point was created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="objectLambdaConfiguration")
    def object_lambda_configuration(
        self,
    ) -> typing.Union["CfnAccessPoint.ObjectLambdaConfigurationProperty", _IResolvable_da3f097b]:
        '''A configuration used when creating an Object Lambda Access Point.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration
        '''
        return typing.cast(typing.Union["CfnAccessPoint.ObjectLambdaConfigurationProperty", _IResolvable_da3f097b], jsii.get(self, "objectLambdaConfiguration"))

    @object_lambda_configuration.setter
    def object_lambda_configuration(
        self,
        value: typing.Union["CfnAccessPoint.ObjectLambdaConfigurationProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAccessPoint, "object_lambda_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectLambdaConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this access point.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAccessPoint, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "supporting_access_point": "supportingAccessPoint",
            "transformation_configurations": "transformationConfigurations",
            "allowed_features": "allowedFeatures",
            "cloud_watch_metrics_enabled": "cloudWatchMetricsEnabled",
        },
    )
    class ObjectLambdaConfigurationProperty:
        def __init__(
            self,
            *,
            supporting_access_point: builtins.str,
            transformation_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnAccessPoint.TransformationConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            allowed_features: typing.Optional[typing.Sequence[builtins.str]] = None,
            cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A configuration used when creating an Object Lambda Access Point.

            :param supporting_access_point: Standard access point associated with the Object Lambda Access Point.
            :param transformation_configurations: A container for transformation configurations for an Object Lambda Access Point.
            :param allowed_features: A container for allowed features. Valid inputs are ``GetObject-Range`` and ``GetObject-PartNumber`` .
            :param cloud_watch_metrics_enabled: A container for whether the CloudWatch metrics configuration is enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                # content_transformation: Any
                
                object_lambda_configuration_property = s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty(
                    supporting_access_point="supportingAccessPoint",
                    transformation_configurations=[s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
                        actions=["actions"],
                        content_transformation=content_transformation
                    )],
                
                    # the properties below are optional
                    allowed_features=["allowedFeatures"],
                    cloud_watch_metrics_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnAccessPoint.ObjectLambdaConfigurationProperty.__init__)
                check_type(argname="argument supporting_access_point", value=supporting_access_point, expected_type=type_hints["supporting_access_point"])
                check_type(argname="argument transformation_configurations", value=transformation_configurations, expected_type=type_hints["transformation_configurations"])
                check_type(argname="argument allowed_features", value=allowed_features, expected_type=type_hints["allowed_features"])
                check_type(argname="argument cloud_watch_metrics_enabled", value=cloud_watch_metrics_enabled, expected_type=type_hints["cloud_watch_metrics_enabled"])
            self._values: typing.Dict[str, typing.Any] = {
                "supporting_access_point": supporting_access_point,
                "transformation_configurations": transformation_configurations,
            }
            if allowed_features is not None:
                self._values["allowed_features"] = allowed_features
            if cloud_watch_metrics_enabled is not None:
                self._values["cloud_watch_metrics_enabled"] = cloud_watch_metrics_enabled

        @builtins.property
        def supporting_access_point(self) -> builtins.str:
            '''Standard access point associated with the Object Lambda Access Point.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-supportingaccesspoint
            '''
            result = self._values.get("supporting_access_point")
            assert result is not None, "Required property 'supporting_access_point' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def transformation_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnAccessPoint.TransformationConfigurationProperty", _IResolvable_da3f097b]]]:
            '''A container for transformation configurations for an Object Lambda Access Point.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-transformationconfigurations
            '''
            result = self._values.get("transformation_configurations")
            assert result is not None, "Required property 'transformation_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnAccessPoint.TransformationConfigurationProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def allowed_features(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A container for allowed features.

            Valid inputs are ``GetObject-Range`` and ``GetObject-PartNumber`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-allowedfeatures
            '''
            result = self._values.get("allowed_features")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def cloud_watch_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A container for whether the CloudWatch metrics configuration is enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-cloudwatchmetricsenabled
            '''
            result = self._values.get("cloud_watch_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectLambdaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "content_transformation": "contentTransformation",
        },
    )
    class TransformationConfigurationProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            content_transformation: typing.Any,
        ) -> None:
            '''A configuration used when creating an Object Lambda Access Point transformation.

            :param actions: A container for the action of an Object Lambda Access Point configuration. Valid input is ``GetObject`` .
            :param content_transformation: A container for the content transformation of an Object Lambda Access Point configuration. Can include the FunctionArn and FunctionPayload. For more information, see `AwsLambdaTransformation <https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AwsLambdaTransformation.html>`_ in the *Amazon S3 API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                # content_transformation: Any
                
                transformation_configuration_property = s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
                    actions=["actions"],
                    content_transformation=content_transformation
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnAccessPoint.TransformationConfigurationProperty.__init__)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument content_transformation", value=content_transformation, expected_type=type_hints["content_transformation"])
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "content_transformation": content_transformation,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''A container for the action of an Object Lambda Access Point configuration.

            Valid input is ``GetObject`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def content_transformation(self) -> typing.Any:
            '''A container for the content transformation of an Object Lambda Access Point configuration.

            Can include the FunctionArn and FunctionPayload. For more information, see `AwsLambdaTransformation <https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AwsLambdaTransformation.html>`_ in the *Amazon S3 API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-contenttransformation
            '''
            result = self._values.get("content_transformation")
            assert result is not None, "Required property 'content_transformation' is missing"
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnAccessPointPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPointPolicy",
):
    '''A CloudFormation ``AWS::S3ObjectLambda::AccessPointPolicy``.

    The ``AWS::S3ObjectLambda::AccessPointPolicy`` resource specifies the Object Lambda Access Point resource policy document.

    :cloudformationResource: AWS::S3ObjectLambda::AccessPointPolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3objectlambda as s3objectlambda
        
        # policy_document: Any
        
        cfn_access_point_policy = s3objectlambda.CfnAccessPointPolicy(self, "MyCfnAccessPointPolicy",
            object_lambda_access_point="objectLambdaAccessPoint",
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        object_lambda_access_point: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''Create a new ``AWS::S3ObjectLambda::AccessPointPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param object_lambda_access_point: An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.
        :param policy_document: Object Lambda Access Point resource policy document.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccessPointPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPointPolicyProps(
            object_lambda_access_point=object_lambda_access_point,
            policy_document=policy_document,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccessPointPolicy.inspect)
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
            type_hints = typing.get_type_hints(CfnAccessPointPolicy._render_properties)
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
    @jsii.member(jsii_name="objectLambdaAccessPoint")
    def object_lambda_access_point(self) -> builtins.str:
        '''An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-objectlambdaaccesspoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "objectLambdaAccessPoint"))

    @object_lambda_access_point.setter
    def object_lambda_access_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAccessPointPolicy, "object_lambda_access_point").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectLambdaAccessPoint", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''Object Lambda Access Point resource policy document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-policydocument
        '''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAccessPointPolicy, "policy_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPointPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "object_lambda_access_point": "objectLambdaAccessPoint",
        "policy_document": "policyDocument",
    },
)
class CfnAccessPointPolicyProps:
    def __init__(
        self,
        *,
        object_lambda_access_point: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''Properties for defining a ``CfnAccessPointPolicy``.

        :param object_lambda_access_point: An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.
        :param policy_document: Object Lambda Access Point resource policy document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3objectlambda as s3objectlambda
            
            # policy_document: Any
            
            cfn_access_point_policy_props = s3objectlambda.CfnAccessPointPolicyProps(
                object_lambda_access_point="objectLambdaAccessPoint",
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccessPointPolicyProps.__init__)
            check_type(argname="argument object_lambda_access_point", value=object_lambda_access_point, expected_type=type_hints["object_lambda_access_point"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_lambda_access_point": object_lambda_access_point,
            "policy_document": policy_document,
        }

    @builtins.property
    def object_lambda_access_point(self) -> builtins.str:
        '''An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-objectlambdaaccesspoint
        '''
        result = self._values.get("object_lambda_access_point")
        assert result is not None, "Required property 'object_lambda_access_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''Object Lambda Access Point resource policy document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPointPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPointProps",
    jsii_struct_bases=[],
    name_mapping={
        "object_lambda_configuration": "objectLambdaConfiguration",
        "name": "name",
    },
)
class CfnAccessPointProps:
    def __init__(
        self,
        *,
        object_lambda_configuration: typing.Union[typing.Union[CfnAccessPoint.ObjectLambdaConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessPoint``.

        :param object_lambda_configuration: A configuration used when creating an Object Lambda Access Point.
        :param name: The name of this access point.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3objectlambda as s3objectlambda
            
            # content_transformation: Any
            
            cfn_access_point_props = s3objectlambda.CfnAccessPointProps(
                object_lambda_configuration=s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty(
                    supporting_access_point="supportingAccessPoint",
                    transformation_configurations=[s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
                        actions=["actions"],
                        content_transformation=content_transformation
                    )],
            
                    # the properties below are optional
                    allowed_features=["allowedFeatures"],
                    cloud_watch_metrics_enabled=False
                ),
            
                # the properties below are optional
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccessPointProps.__init__)
            check_type(argname="argument object_lambda_configuration", value=object_lambda_configuration, expected_type=type_hints["object_lambda_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_lambda_configuration": object_lambda_configuration,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def object_lambda_configuration(
        self,
    ) -> typing.Union[CfnAccessPoint.ObjectLambdaConfigurationProperty, _IResolvable_da3f097b]:
        '''A configuration used when creating an Object Lambda Access Point.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration
        '''
        result = self._values.get("object_lambda_configuration")
        assert result is not None, "Required property 'object_lambda_configuration' is missing"
        return typing.cast(typing.Union[CfnAccessPoint.ObjectLambdaConfigurationProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this access point.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessPoint",
    "CfnAccessPointPolicy",
    "CfnAccessPointPolicyProps",
    "CfnAccessPointProps",
]

publication.publish()
