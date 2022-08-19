'''
# AWS::Forecast Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_forecast as forecast
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Forecast construct libraries](https://constructs.dev/search?q=forecast)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Forecast resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Forecast.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Forecast](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Forecast.html).

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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDataset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_forecast.CfnDataset",
):
    '''A CloudFormation ``AWS::Forecast::Dataset``.

    Creates an Amazon Forecast dataset. The information about the dataset that you provide helps Forecast understand how to consume the data for model training. This includes the following:

    - *``DataFrequency``* - How frequently your historical time-series data is collected.
    - *``Domain``* and *``DatasetType``* - Each dataset has an associated dataset domain and a type within the domain. Amazon Forecast provides a list of predefined domains and types within each domain. For each unique dataset domain and type within the domain, Amazon Forecast requires your data to include a minimum set of predefined fields.
    - *``Schema``* - A schema specifies the fields in the dataset, including the field name and data type.

    After creating a dataset, you import your training data into it and add the dataset to a dataset group. You use the dataset group to create a predictor. For more information, see `Importing datasets <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html>`_ .

    To get a list of all your datasets, use the `ListDatasets <https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasets.html>`_ operation.

    For example Forecast datasets, see the `Amazon Forecast Sample GitHub repository <https://docs.aws.amazon.com/https://github.com/aws-samples/amazon-forecast-samples>`_ .
    .. epigraph::

       The ``Status`` of a dataset must be ``ACTIVE`` before you can import training data. Use the `DescribeDataset <https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html>`_ operation to get the status.

    :cloudformationResource: AWS::Forecast::Dataset
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_forecast as forecast
        
        # encryption_config: Any
        # schema: Any
        # tags: Any
        
        cfn_dataset = forecast.CfnDataset(self, "MyCfnDataset",
            dataset_name="datasetName",
            dataset_type="datasetType",
            domain="domain",
            schema=schema,
        
            # the properties below are optional
            data_frequency="dataFrequency",
            encryption_config=encryption_config,
            tags=[tags]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dataset_name: builtins.str,
        dataset_type: builtins.str,
        domain: builtins.str,
        schema: typing.Any,
        data_frequency: typing.Optional[builtins.str] = None,
        encryption_config: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''Create a new ``AWS::Forecast::Dataset``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dataset_name: The name of the dataset.
        :param dataset_type: The dataset type.
        :param domain: The domain associated with the dataset.
        :param schema: The schema for the dataset. The schema attributes and their order must match the fields in your data. The dataset ``Domain`` and ``DatasetType`` that you choose determine the minimum required fields in your training data. For information about the required fields for a specific dataset domain and type, see `Dataset Domains and Dataset Types <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-domains-ds-types.html>`_ .
        :param data_frequency: The frequency of data collection. This parameter is required for RELATED_TIME_SERIES datasets. Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, "D" indicates every day and "15min" indicates every 15 minutes.
        :param encryption_config: A Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataset.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetProps(
            dataset_name=dataset_name,
            dataset_type=dataset_type,
            domain=domain,
            schema=schema,
            data_frequency=data_frequency,
            encryption_config=encryption_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataset.inspect)
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
            type_hints = typing.get_type_hints(CfnDataset._render_properties)
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
        '''The Amazon Resource Name (ARN) of the dataset.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> builtins.str:
        '''The name of the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datasetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "dataset_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetType")
    def dataset_type(self) -> builtins.str:
        '''The dataset type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datasettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "datasetType"))

    @dataset_type.setter
    def dataset_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "dataset_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        '''The domain associated with the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-domain
        '''
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(self) -> typing.Any:
        '''A Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-encryptionconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "encryptionConfig"))

    @encryption_config.setter
    def encryption_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "encryption_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schema")
    def schema(self) -> typing.Any:
        '''The schema for the dataset.

        The schema attributes and their order must match the fields in your data. The dataset ``Domain`` and ``DatasetType`` that you choose determine the minimum required fields in your training data. For information about the required fields for a specific dataset domain and type, see `Dataset Domains and Dataset Types <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-domains-ds-types.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-schema
        '''
        return typing.cast(typing.Any, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataFrequency")
    def data_frequency(self) -> typing.Optional[builtins.str]:
        '''The frequency of data collection. This parameter is required for RELATED_TIME_SERIES datasets.

        Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, "D" indicates every day and "15min" indicates every 15 minutes.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datafrequency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFrequency"))

    @data_frequency.setter
    def data_frequency(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "data_frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFrequency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[typing.Any]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-tags
        '''
        return typing.cast(typing.Optional[typing.List[typing.Any]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[typing.Any]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.implements(_IInspectable_c2943556)
class CfnDatasetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_forecast.CfnDatasetGroup",
):
    '''A CloudFormation ``AWS::Forecast::DatasetGroup``.

    Creates a dataset group, which holds a collection of related datasets. You can add datasets to the dataset group when you create the dataset group, or later by using the `UpdateDatasetGroup <https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html>`_ operation.

    After creating a dataset group and adding datasets, you use the dataset group when you create a predictor. For more information, see `Dataset groups <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html>`_ .

    To get a list of all your datasets groups, use the `ListDatasetGroups <https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetGroups.html>`_ operation.
    .. epigraph::

       The ``Status`` of a dataset group must be ``ACTIVE`` before you can use the dataset group to create a predictor. To get the status, use the `DescribeDatasetGroup <https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html>`_ operation.

    :cloudformationResource: AWS::Forecast::DatasetGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_forecast as forecast
        
        cfn_dataset_group = forecast.CfnDatasetGroup(self, "MyCfnDatasetGroup",
            dataset_group_name="datasetGroupName",
            domain="domain",
        
            # the properties below are optional
            dataset_arns=["datasetArns"],
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
        dataset_group_name: builtins.str,
        domain: builtins.str,
        dataset_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Forecast::DatasetGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dataset_group_name: The name of the dataset group.
        :param domain: The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the ``Domain`` parameter of the `CreateDataset <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html>`_ operation must match. The ``Domain`` and ``DatasetType`` that you choose determine the fields that must be present in training data that you import to a dataset. For example, if you choose the ``RETAIL`` domain and ``TARGET_TIME_SERIES`` as the ``DatasetType`` , Amazon Forecast requires that ``item_id`` , ``timestamp`` , and ``demand`` fields are present in your data. For more information, see `Dataset groups <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html>`_ .
        :param dataset_arns: An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDatasetGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetGroupProps(
            dataset_group_name=dataset_group_name,
            domain=domain,
            dataset_arns=dataset_arns,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDatasetGroup.inspect)
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
            type_hints = typing.get_type_hints(CfnDatasetGroup._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDatasetGroupArn")
    def attr_dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group.

        :cloudformationAttribute: DatasetGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatasetGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetGroupName")
    def dataset_group_name(self) -> builtins.str:
        '''The name of the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-datasetgroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "datasetGroupName"))

    @dataset_group_name.setter
    def dataset_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDatasetGroup, "dataset_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        '''The domain associated with the dataset group.

        When you add a dataset to a dataset group, this value and the value specified for the ``Domain`` parameter of the `CreateDataset <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html>`_ operation must match.

        The ``Domain`` and ``DatasetType`` that you choose determine the fields that must be present in training data that you import to a dataset. For example, if you choose the ``RETAIL`` domain and ``TARGET_TIME_SERIES`` as the ``DatasetType`` , Amazon Forecast requires that ``item_id`` , ``timestamp`` , and ``demand`` fields are present in your data. For more information, see `Dataset groups <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-domain
        '''
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDatasetGroup, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetArns")
    def dataset_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-datasetarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "datasetArns"))

    @dataset_arns.setter
    def dataset_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDatasetGroup, "dataset_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetArns", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_forecast.CfnDatasetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_group_name": "datasetGroupName",
        "domain": "domain",
        "dataset_arns": "datasetArns",
        "tags": "tags",
    },
)
class CfnDatasetGroupProps:
    def __init__(
        self,
        *,
        dataset_group_name: builtins.str,
        domain: builtins.str,
        dataset_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDatasetGroup``.

        :param dataset_group_name: The name of the dataset group.
        :param domain: The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the ``Domain`` parameter of the `CreateDataset <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html>`_ operation must match. The ``Domain`` and ``DatasetType`` that you choose determine the fields that must be present in training data that you import to a dataset. For example, if you choose the ``RETAIL`` domain and ``TARGET_TIME_SERIES`` as the ``DatasetType`` , Amazon Forecast requires that ``item_id`` , ``timestamp`` , and ``demand`` fields are present in your data. For more information, see `Dataset groups <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html>`_ .
        :param dataset_arns: An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_forecast as forecast
            
            cfn_dataset_group_props = forecast.CfnDatasetGroupProps(
                dataset_group_name="datasetGroupName",
                domain="domain",
            
                # the properties below are optional
                dataset_arns=["datasetArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDatasetGroupProps.__init__)
            check_type(argname="argument dataset_group_name", value=dataset_group_name, expected_type=type_hints["dataset_group_name"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument dataset_arns", value=dataset_arns, expected_type=type_hints["dataset_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_group_name": dataset_group_name,
            "domain": domain,
        }
        if dataset_arns is not None:
            self._values["dataset_arns"] = dataset_arns
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dataset_group_name(self) -> builtins.str:
        '''The name of the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-datasetgroupname
        '''
        result = self._values.get("dataset_group_name")
        assert result is not None, "Required property 'dataset_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> builtins.str:
        '''The domain associated with the dataset group.

        When you add a dataset to a dataset group, this value and the value specified for the ``Domain`` parameter of the `CreateDataset <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html>`_ operation must match.

        The ``Domain`` and ``DatasetType`` that you choose determine the fields that must be present in training data that you import to a dataset. For example, if you choose the ``RETAIL`` domain and ``TARGET_TIME_SERIES`` as the ``DatasetType`` , Amazon Forecast requires that ``item_id`` , ``timestamp`` , and ``demand`` fields are present in your data. For more information, see `Dataset groups <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-domain
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-datasetarns
        '''
        result = self._values.get("dataset_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_forecast.CfnDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_name": "datasetName",
        "dataset_type": "datasetType",
        "domain": "domain",
        "schema": "schema",
        "data_frequency": "dataFrequency",
        "encryption_config": "encryptionConfig",
        "tags": "tags",
    },
)
class CfnDatasetProps:
    def __init__(
        self,
        *,
        dataset_name: builtins.str,
        dataset_type: builtins.str,
        domain: builtins.str,
        schema: typing.Any,
        data_frequency: typing.Optional[builtins.str] = None,
        encryption_config: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataset``.

        :param dataset_name: The name of the dataset.
        :param dataset_type: The dataset type.
        :param domain: The domain associated with the dataset.
        :param schema: The schema for the dataset. The schema attributes and their order must match the fields in your data. The dataset ``Domain`` and ``DatasetType`` that you choose determine the minimum required fields in your training data. For information about the required fields for a specific dataset domain and type, see `Dataset Domains and Dataset Types <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-domains-ds-types.html>`_ .
        :param data_frequency: The frequency of data collection. This parameter is required for RELATED_TIME_SERIES datasets. Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, "D" indicates every day and "15min" indicates every 15 minutes.
        :param encryption_config: A Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_forecast as forecast
            
            # encryption_config: Any
            # schema: Any
            # tags: Any
            
            cfn_dataset_props = forecast.CfnDatasetProps(
                dataset_name="datasetName",
                dataset_type="datasetType",
                domain="domain",
                schema=schema,
            
                # the properties below are optional
                data_frequency="dataFrequency",
                encryption_config=encryption_config,
                tags=[tags]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDatasetProps.__init__)
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            check_type(argname="argument dataset_type", value=dataset_type, expected_type=type_hints["dataset_type"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument data_frequency", value=data_frequency, expected_type=type_hints["data_frequency"])
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_name": dataset_name,
            "dataset_type": dataset_type,
            "domain": domain,
            "schema": schema,
        }
        if data_frequency is not None:
            self._values["data_frequency"] = data_frequency
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dataset_name(self) -> builtins.str:
        '''The name of the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datasetname
        '''
        result = self._values.get("dataset_name")
        assert result is not None, "Required property 'dataset_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_type(self) -> builtins.str:
        '''The dataset type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datasettype
        '''
        result = self._values.get("dataset_type")
        assert result is not None, "Required property 'dataset_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> builtins.str:
        '''The domain associated with the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-domain
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> typing.Any:
        '''The schema for the dataset.

        The schema attributes and their order must match the fields in your data. The dataset ``Domain`` and ``DatasetType`` that you choose determine the minimum required fields in your training data. For information about the required fields for a specific dataset domain and type, see `Dataset Domains and Dataset Types <https://docs.aws.amazon.com/forecast/latest/dg/howitworks-domains-ds-types.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-schema
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def data_frequency(self) -> typing.Optional[builtins.str]:
        '''The frequency of data collection. This parameter is required for RELATED_TIME_SERIES datasets.

        Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, "D" indicates every day and "15min" indicates every 15 minutes.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datafrequency
        '''
        result = self._values.get("data_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_config(self) -> typing.Any:
        '''A Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-encryptionconfig
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[typing.Any]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataset",
    "CfnDatasetGroup",
    "CfnDatasetGroupProps",
    "CfnDatasetProps",
]

publication.publish()
