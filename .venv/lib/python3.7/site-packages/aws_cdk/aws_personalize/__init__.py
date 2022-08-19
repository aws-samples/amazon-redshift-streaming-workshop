'''
# AWS::Personalize Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_personalize as personalize
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Personalize construct libraries](https://constructs.dev/search?q=personalize)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Personalize resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Personalize.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Personalize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Personalize.html).

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
class CfnDataset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_personalize.CfnDataset",
):
    '''A CloudFormation ``AWS::Personalize::Dataset``.

    Creates an empty dataset and adds it to the specified dataset group. Use `CreateDatasetImportJob <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html>`_ to import your training data to a dataset.

    There are three types of datasets:

    - Interactions
    - Items
    - Users

    Each dataset type has an associated schema with required field types. Only the ``Interactions`` dataset is required in order to train a model (also referred to as creating a solution).

    A dataset can be in one of the following states:

    - CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    - DELETE PENDING > DELETE IN_PROGRESS

    To get the status of the dataset, call `DescribeDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html>`_ .

    **Related APIs** - `CreateDatasetGroup <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html>`_

    - `ListDatasets <https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasets.html>`_
    - `DescribeDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html>`_
    - `DeleteDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDataset.html>`_

    :cloudformationResource: AWS::Personalize::Dataset
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_personalize as personalize
        
        # data_source: Any
        
        cfn_dataset = personalize.CfnDataset(self, "MyCfnDataset",
            dataset_group_arn="datasetGroupArn",
            dataset_type="datasetType",
            name="name",
            schema_arn="schemaArn",
        
            # the properties below are optional
            dataset_import_job=personalize.CfnDataset.DatasetImportJobProperty(
                dataset_arn="datasetArn",
                dataset_import_job_arn="datasetImportJobArn",
                data_source=data_source,
                job_name="jobName",
                role_arn="roleArn"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dataset_group_arn: builtins.str,
        dataset_type: builtins.str,
        name: builtins.str,
        schema_arn: builtins.str,
        dataset_import_job: typing.Optional[typing.Union[typing.Union["CfnDataset.DatasetImportJobProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::Personalize::Dataset``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group.
        :param dataset_type: One of the following values:. - Interactions - Items - Users
        :param name: The name of the dataset.
        :param schema_arn: The ARN of the associated schema.
        :param dataset_import_job: Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataset.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetProps(
            dataset_group_arn=dataset_group_arn,
            dataset_type=dataset_type,
            name=name,
            schema_arn=schema_arn,
            dataset_import_job=dataset_import_job,
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
    @jsii.member(jsii_name="attrDatasetArn")
    def attr_dataset_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset.

        :cloudformationAttribute: DatasetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatasetArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetGroupArn")
    def dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasetgrouparn
        '''
        return typing.cast(builtins.str, jsii.get(self, "datasetGroupArn"))

    @dataset_group_arn.setter
    def dataset_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "dataset_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetGroupArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetType")
    def dataset_type(self) -> builtins.str:
        '''One of the following values:.

        - Interactions
        - Items
        - Users

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "datasetType"))

    @dataset_type.setter
    def dataset_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "dataset_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schemaArn")
    def schema_arn(self) -> builtins.str:
        '''The ARN of the associated schema.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-schemaarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "schemaArn"))

    @schema_arn.setter
    def schema_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "schema_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetImportJob")
    def dataset_import_job(
        self,
    ) -> typing.Optional[typing.Union["CfnDataset.DatasetImportJobProperty", _IResolvable_da3f097b]]:
        '''Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasetimportjob
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataset.DatasetImportJobProperty", _IResolvable_da3f097b]], jsii.get(self, "datasetImportJob"))

    @dataset_import_job.setter
    def dataset_import_job(
        self,
        value: typing.Optional[typing.Union["CfnDataset.DatasetImportJobProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataset, "dataset_import_job").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetImportJob", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnDataset.DatasetImportJobProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dataset_arn": "datasetArn",
            "dataset_import_job_arn": "datasetImportJobArn",
            "data_source": "dataSource",
            "job_name": "jobName",
            "role_arn": "roleArn",
        },
    )
    class DatasetImportJobProperty:
        def __init__(
            self,
            *,
            dataset_arn: typing.Optional[builtins.str] = None,
            dataset_import_job_arn: typing.Optional[builtins.str] = None,
            data_source: typing.Any = None,
            job_name: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.

            For more information, see `CreateDatasetImportJob <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html>`_ .

            A dataset import job can be in one of the following states:

            - CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

            :param dataset_arn: The Amazon Resource Name (ARN) of the dataset that receives the imported data.
            :param dataset_import_job_arn: The ARN of the dataset import job.
            :param data_source: The Amazon S3 bucket that contains the training data to import.
            :param job_name: The name of the import job.
            :param role_arn: The ARN of the IAM role that has permissions to read from the Amazon S3 data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                # data_source: Any
                
                dataset_import_job_property = personalize.CfnDataset.DatasetImportJobProperty(
                    dataset_arn="datasetArn",
                    dataset_import_job_arn="datasetImportJobArn",
                    data_source=data_source,
                    job_name="jobName",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDataset.DatasetImportJobProperty.__init__)
                check_type(argname="argument dataset_arn", value=dataset_arn, expected_type=type_hints["dataset_arn"])
                check_type(argname="argument dataset_import_job_arn", value=dataset_import_job_arn, expected_type=type_hints["dataset_import_job_arn"])
                check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
                check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if dataset_arn is not None:
                self._values["dataset_arn"] = dataset_arn
            if dataset_import_job_arn is not None:
                self._values["dataset_import_job_arn"] = dataset_import_job_arn
            if data_source is not None:
                self._values["data_source"] = data_source
            if job_name is not None:
                self._values["job_name"] = job_name
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def dataset_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the dataset that receives the imported data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasetarn
            '''
            result = self._values.get("dataset_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dataset_import_job_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the dataset import job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasetimportjobarn
            '''
            result = self._values.get("dataset_import_job_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_source(self) -> typing.Any:
            '''The Amazon S3 bucket that contains the training data to import.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasource
            '''
            result = self._values.get("data_source")
            return typing.cast(typing.Any, result)

        @builtins.property
        def job_name(self) -> typing.Optional[builtins.str]:
            '''The name of the import job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-jobname
            '''
            result = self._values.get("job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM role that has permissions to read from the Amazon S3 data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetImportJobProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnDatasetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_personalize.CfnDatasetGroup",
):
    '''A CloudFormation ``AWS::Personalize::DatasetGroup``.

    A dataset group is a collection of related datasets (Interactions, User, and Item). You create a dataset group by calling `CreateDatasetGroup <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html>`_ . You then create a dataset and add it to a dataset group by calling `CreateDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html>`_ . The dataset group is used to create and train a solution by calling `CreateSolution <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html>`_ . A dataset group can contain only one of each type of dataset.

    You can specify an AWS Key Management Service (KMS) key to encrypt the datasets in the group.

    :cloudformationResource: AWS::Personalize::DatasetGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_personalize as personalize
        
        cfn_dataset_group = personalize.CfnDatasetGroup(self, "MyCfnDatasetGroup",
            name="name",
        
            # the properties below are optional
            domain="domain",
            kms_key_arn="kmsKeyArn",
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Personalize::DatasetGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the dataset group.
        :param domain: The domain of a Domain dataset group.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the datasets.
        :param role_arn: The ARN of the IAM role that has permissions to create the dataset group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDatasetGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetGroupProps(
            name=name, domain=domain, kms_key_arn=kms_key_arn, role_arn=role_arn
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDatasetGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain of a Domain dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-domain
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDatasetGroup, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the datasets.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-kmskeyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDatasetGroup, "kms_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that has permissions to create the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDatasetGroup, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_personalize.CfnDatasetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "domain": "domain",
        "kms_key_arn": "kmsKeyArn",
        "role_arn": "roleArn",
    },
)
class CfnDatasetGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDatasetGroup``.

        :param name: The name of the dataset group.
        :param domain: The domain of a Domain dataset group.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the datasets.
        :param role_arn: The ARN of the IAM role that has permissions to create the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_personalize as personalize
            
            cfn_dataset_group_props = personalize.CfnDatasetGroupProps(
                name="name",
            
                # the properties below are optional
                domain="domain",
                kms_key_arn="kmsKeyArn",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDatasetGroupProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if domain is not None:
            self._values["domain"] = domain
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain of a Domain dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the datasets.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that has permissions to create the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_personalize.CfnDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_group_arn": "datasetGroupArn",
        "dataset_type": "datasetType",
        "name": "name",
        "schema_arn": "schemaArn",
        "dataset_import_job": "datasetImportJob",
    },
)
class CfnDatasetProps:
    def __init__(
        self,
        *,
        dataset_group_arn: builtins.str,
        dataset_type: builtins.str,
        name: builtins.str,
        schema_arn: builtins.str,
        dataset_import_job: typing.Optional[typing.Union[typing.Union[CfnDataset.DatasetImportJobProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataset``.

        :param dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group.
        :param dataset_type: One of the following values:. - Interactions - Items - Users
        :param name: The name of the dataset.
        :param schema_arn: The ARN of the associated schema.
        :param dataset_import_job: Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_personalize as personalize
            
            # data_source: Any
            
            cfn_dataset_props = personalize.CfnDatasetProps(
                dataset_group_arn="datasetGroupArn",
                dataset_type="datasetType",
                name="name",
                schema_arn="schemaArn",
            
                # the properties below are optional
                dataset_import_job=personalize.CfnDataset.DatasetImportJobProperty(
                    dataset_arn="datasetArn",
                    dataset_import_job_arn="datasetImportJobArn",
                    data_source=data_source,
                    job_name="jobName",
                    role_arn="roleArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDatasetProps.__init__)
            check_type(argname="argument dataset_group_arn", value=dataset_group_arn, expected_type=type_hints["dataset_group_arn"])
            check_type(argname="argument dataset_type", value=dataset_type, expected_type=type_hints["dataset_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
            check_type(argname="argument dataset_import_job", value=dataset_import_job, expected_type=type_hints["dataset_import_job"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_group_arn": dataset_group_arn,
            "dataset_type": dataset_type,
            "name": name,
            "schema_arn": schema_arn,
        }
        if dataset_import_job is not None:
            self._values["dataset_import_job"] = dataset_import_job

    @builtins.property
    def dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasetgrouparn
        '''
        result = self._values.get("dataset_group_arn")
        assert result is not None, "Required property 'dataset_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_type(self) -> builtins.str:
        '''One of the following values:.

        - Interactions
        - Items
        - Users

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasettype
        '''
        result = self._values.get("dataset_type")
        assert result is not None, "Required property 'dataset_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_arn(self) -> builtins.str:
        '''The ARN of the associated schema.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-schemaarn
        '''
        result = self._values.get("schema_arn")
        assert result is not None, "Required property 'schema_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_import_job(
        self,
    ) -> typing.Optional[typing.Union[CfnDataset.DatasetImportJobProperty, _IResolvable_da3f097b]]:
        '''Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasetimportjob
        '''
        result = self._values.get("dataset_import_job")
        return typing.cast(typing.Optional[typing.Union[CfnDataset.DatasetImportJobProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSchema(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_personalize.CfnSchema",
):
    '''A CloudFormation ``AWS::Personalize::Schema``.

    Creates an Amazon Personalize schema from the specified schema string. The schema you create must be in Avro JSON format.

    Amazon Personalize recognizes three schema variants. Each schema is associated with a dataset type and has a set of required field and keywords. If you are creating a schema for a dataset in a Domain dataset group, you provide the domain of the Domain dataset group. You specify a schema when you call `CreateDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html>`_ .

    For more information on schemas, see `Datasets and schemas <https://docs.aws.amazon.com/personalize/latest/dg/how-it-works-dataset-schema.html>`_ .

    **Related APIs** - `ListSchemas <https://docs.aws.amazon.com/personalize/latest/dg/API_ListSchemas.html>`_

    - `DescribeSchema <https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSchema.html>`_
    - `DeleteSchema <https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSchema.html>`_

    :cloudformationResource: AWS::Personalize::Schema
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_personalize as personalize
        
        cfn_schema = personalize.CfnSchema(self, "MyCfnSchema",
            name="name",
            schema="schema",
        
            # the properties below are optional
            domain="domain"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        schema: builtins.str,
        domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Personalize::Schema``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the schema.
        :param schema: The schema.
        :param domain: The domain of a schema that you created for a dataset in a Domain dataset group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSchema.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchemaProps(name=name, schema=schema, domain=domain)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSchema.inspect)
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
            type_hints = typing.get_type_hints(CfnSchema._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSchemaArn")
    def attr_schema_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the schema.

        :cloudformationAttribute: SchemaArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the schema.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSchema, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        '''The schema.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-schema
        '''
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSchema, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain of a schema that you created for a dataset in a Domain dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-domain
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSchema, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_personalize.CfnSchemaProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "schema": "schema", "domain": "domain"},
)
class CfnSchemaProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        schema: builtins.str,
        domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchema``.

        :param name: The name of the schema.
        :param schema: The schema.
        :param domain: The domain of a schema that you created for a dataset in a Domain dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_personalize as personalize
            
            cfn_schema_props = personalize.CfnSchemaProps(
                name="name",
                schema="schema",
            
                # the properties below are optional
                domain="domain"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSchemaProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "schema": schema,
        }
        if domain is not None:
            self._values["domain"] = domain

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the schema.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> builtins.str:
        '''The schema.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-schema
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain of a schema that you created for a dataset in a Domain dataset group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSolution(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_personalize.CfnSolution",
):
    '''A CloudFormation ``AWS::Personalize::Solution``.

    An object that provides information about a solution. A solution is a trained model that can be deployed as a campaign.

    :cloudformationResource: AWS::Personalize::Solution
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_personalize as personalize
        
        # auto_ml_config: Any
        # hpo_config: Any
        
        cfn_solution = personalize.CfnSolution(self, "MyCfnSolution",
            dataset_group_arn="datasetGroupArn",
            name="name",
        
            # the properties below are optional
            event_type="eventType",
            perform_auto_ml=False,
            perform_hpo=False,
            recipe_arn="recipeArn",
            solution_config=personalize.CfnSolution.SolutionConfigProperty(
                algorithm_hyper_parameters={
                    "algorithm_hyper_parameters_key": "algorithmHyperParameters"
                },
                auto_ml_config=auto_ml_config,
                event_value_threshold="eventValueThreshold",
                feature_transformation_parameters={
                    "feature_transformation_parameters_key": "featureTransformationParameters"
                },
                hpo_config=hpo_config
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dataset_group_arn: builtins.str,
        name: builtins.str,
        event_type: typing.Optional[builtins.str] = None,
        perform_auto_ml: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        perform_hpo: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recipe_arn: typing.Optional[builtins.str] = None,
        solution_config: typing.Optional[typing.Union[typing.Union["CfnSolution.SolutionConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::Personalize::Solution``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group that provides the training data.
        :param name: The name of the solution.
        :param event_type: The event type (for example, 'click' or 'like') that is used for training the model. If no ``eventType`` is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.
        :param perform_auto_ml: When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration ( ``recipeArn`` must not be specified). When false (the default), Amazon Personalize uses ``recipeArn`` for training.
        :param perform_hpo: Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is ``false`` .
        :param recipe_arn: The ARN of the recipe used to create the solution.
        :param solution_config: Describes the configuration properties for the solution.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSolution.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSolutionProps(
            dataset_group_arn=dataset_group_arn,
            name=name,
            event_type=event_type,
            perform_auto_ml=perform_auto_ml,
            perform_hpo=perform_hpo,
            recipe_arn=recipe_arn,
            solution_config=solution_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSolution.inspect)
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
            type_hints = typing.get_type_hints(CfnSolution._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSolutionArn")
    def attr_solution_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the solution.

        :cloudformationAttribute: SolutionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSolutionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetGroupArn")
    def dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group that provides the training data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-datasetgrouparn
        '''
        return typing.cast(builtins.str, jsii.get(self, "datasetGroupArn"))

    @dataset_group_arn.setter
    def dataset_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSolution, "dataset_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetGroupArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the solution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSolution, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> typing.Optional[builtins.str]:
        '''The event type (for example, 'click' or 'like') that is used for training the model.

        If no ``eventType`` is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-eventtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSolution, "event_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="performAutoMl")
    def perform_auto_ml(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration ( ``recipeArn`` must not be specified).

        When false (the default), Amazon Personalize uses ``recipeArn`` for training.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-performautoml
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "performAutoMl"))

    @perform_auto_ml.setter
    def perform_auto_ml(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSolution, "perform_auto_ml").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performAutoMl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="performHpo")
    def perform_hpo(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to perform hyperparameter optimization (HPO) on the chosen recipe.

        The default is ``false`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-performhpo
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "performHpo"))

    @perform_hpo.setter
    def perform_hpo(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSolution, "perform_hpo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performHpo", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recipeArn")
    def recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the recipe used to create the solution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-recipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recipeArn"))

    @recipe_arn.setter
    def recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSolution, "recipe_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recipeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="solutionConfig")
    def solution_config(
        self,
    ) -> typing.Optional[typing.Union["CfnSolution.SolutionConfigProperty", _IResolvable_da3f097b]]:
        '''Describes the configuration properties for the solution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-solutionconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnSolution.SolutionConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "solutionConfig"))

    @solution_config.setter
    def solution_config(
        self,
        value: typing.Optional[typing.Union["CfnSolution.SolutionConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSolution, "solution_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "solutionConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.SolutionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm_hyper_parameters": "algorithmHyperParameters",
            "auto_ml_config": "autoMlConfig",
            "event_value_threshold": "eventValueThreshold",
            "feature_transformation_parameters": "featureTransformationParameters",
            "hpo_config": "hpoConfig",
        },
    )
    class SolutionConfigProperty:
        def __init__(
            self,
            *,
            algorithm_hyper_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            auto_ml_config: typing.Any = None,
            event_value_threshold: typing.Optional[builtins.str] = None,
            feature_transformation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            hpo_config: typing.Any = None,
        ) -> None:
            '''Describes the configuration properties for the solution.

            :param algorithm_hyper_parameters: Lists the hyperparameter names and ranges.
            :param auto_ml_config: The `AutoMLConfig <https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLConfig.html>`_ object containing a list of recipes to search when AutoML is performed.
            :param event_value_threshold: Only events with a value greater than or equal to this threshold are used for training a model.
            :param feature_transformation_parameters: Lists the feature transformation parameters.
            :param hpo_config: Describes the properties for hyperparameter optimization (HPO).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                # auto_ml_config: Any
                # hpo_config: Any
                
                solution_config_property = personalize.CfnSolution.SolutionConfigProperty(
                    algorithm_hyper_parameters={
                        "algorithm_hyper_parameters_key": "algorithmHyperParameters"
                    },
                    auto_ml_config=auto_ml_config,
                    event_value_threshold="eventValueThreshold",
                    feature_transformation_parameters={
                        "feature_transformation_parameters_key": "featureTransformationParameters"
                    },
                    hpo_config=hpo_config
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSolution.SolutionConfigProperty.__init__)
                check_type(argname="argument algorithm_hyper_parameters", value=algorithm_hyper_parameters, expected_type=type_hints["algorithm_hyper_parameters"])
                check_type(argname="argument auto_ml_config", value=auto_ml_config, expected_type=type_hints["auto_ml_config"])
                check_type(argname="argument event_value_threshold", value=event_value_threshold, expected_type=type_hints["event_value_threshold"])
                check_type(argname="argument feature_transformation_parameters", value=feature_transformation_parameters, expected_type=type_hints["feature_transformation_parameters"])
                check_type(argname="argument hpo_config", value=hpo_config, expected_type=type_hints["hpo_config"])
            self._values: typing.Dict[str, typing.Any] = {}
            if algorithm_hyper_parameters is not None:
                self._values["algorithm_hyper_parameters"] = algorithm_hyper_parameters
            if auto_ml_config is not None:
                self._values["auto_ml_config"] = auto_ml_config
            if event_value_threshold is not None:
                self._values["event_value_threshold"] = event_value_threshold
            if feature_transformation_parameters is not None:
                self._values["feature_transformation_parameters"] = feature_transformation_parameters
            if hpo_config is not None:
                self._values["hpo_config"] = hpo_config

        @builtins.property
        def algorithm_hyper_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Lists the hyperparameter names and ranges.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-algorithmhyperparameters
            '''
            result = self._values.get("algorithm_hyper_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def auto_ml_config(self) -> typing.Any:
            '''The `AutoMLConfig <https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLConfig.html>`_ object containing a list of recipes to search when AutoML is performed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-automlconfig
            '''
            result = self._values.get("auto_ml_config")
            return typing.cast(typing.Any, result)

        @builtins.property
        def event_value_threshold(self) -> typing.Optional[builtins.str]:
            '''Only events with a value greater than or equal to this threshold are used for training a model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-eventvaluethreshold
            '''
            result = self._values.get("event_value_threshold")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def feature_transformation_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Lists the feature transformation parameters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-featuretransformationparameters
            '''
            result = self._values.get("feature_transformation_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def hpo_config(self) -> typing.Any:
            '''Describes the properties for hyperparameter optimization (HPO).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-hpoconfig
            '''
            result = self._values.get("hpo_config")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SolutionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_personalize.CfnSolutionProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_group_arn": "datasetGroupArn",
        "name": "name",
        "event_type": "eventType",
        "perform_auto_ml": "performAutoMl",
        "perform_hpo": "performHpo",
        "recipe_arn": "recipeArn",
        "solution_config": "solutionConfig",
    },
)
class CfnSolutionProps:
    def __init__(
        self,
        *,
        dataset_group_arn: builtins.str,
        name: builtins.str,
        event_type: typing.Optional[builtins.str] = None,
        perform_auto_ml: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        perform_hpo: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recipe_arn: typing.Optional[builtins.str] = None,
        solution_config: typing.Optional[typing.Union[typing.Union[CfnSolution.SolutionConfigProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSolution``.

        :param dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group that provides the training data.
        :param name: The name of the solution.
        :param event_type: The event type (for example, 'click' or 'like') that is used for training the model. If no ``eventType`` is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.
        :param perform_auto_ml: When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration ( ``recipeArn`` must not be specified). When false (the default), Amazon Personalize uses ``recipeArn`` for training.
        :param perform_hpo: Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is ``false`` .
        :param recipe_arn: The ARN of the recipe used to create the solution.
        :param solution_config: Describes the configuration properties for the solution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_personalize as personalize
            
            # auto_ml_config: Any
            # hpo_config: Any
            
            cfn_solution_props = personalize.CfnSolutionProps(
                dataset_group_arn="datasetGroupArn",
                name="name",
            
                # the properties below are optional
                event_type="eventType",
                perform_auto_ml=False,
                perform_hpo=False,
                recipe_arn="recipeArn",
                solution_config=personalize.CfnSolution.SolutionConfigProperty(
                    algorithm_hyper_parameters={
                        "algorithm_hyper_parameters_key": "algorithmHyperParameters"
                    },
                    auto_ml_config=auto_ml_config,
                    event_value_threshold="eventValueThreshold",
                    feature_transformation_parameters={
                        "feature_transformation_parameters_key": "featureTransformationParameters"
                    },
                    hpo_config=hpo_config
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSolutionProps.__init__)
            check_type(argname="argument dataset_group_arn", value=dataset_group_arn, expected_type=type_hints["dataset_group_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument perform_auto_ml", value=perform_auto_ml, expected_type=type_hints["perform_auto_ml"])
            check_type(argname="argument perform_hpo", value=perform_hpo, expected_type=type_hints["perform_hpo"])
            check_type(argname="argument recipe_arn", value=recipe_arn, expected_type=type_hints["recipe_arn"])
            check_type(argname="argument solution_config", value=solution_config, expected_type=type_hints["solution_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_group_arn": dataset_group_arn,
            "name": name,
        }
        if event_type is not None:
            self._values["event_type"] = event_type
        if perform_auto_ml is not None:
            self._values["perform_auto_ml"] = perform_auto_ml
        if perform_hpo is not None:
            self._values["perform_hpo"] = perform_hpo
        if recipe_arn is not None:
            self._values["recipe_arn"] = recipe_arn
        if solution_config is not None:
            self._values["solution_config"] = solution_config

    @builtins.property
    def dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group that provides the training data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-datasetgrouparn
        '''
        result = self._values.get("dataset_group_arn")
        assert result is not None, "Required property 'dataset_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the solution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_type(self) -> typing.Optional[builtins.str]:
        '''The event type (for example, 'click' or 'like') that is used for training the model.

        If no ``eventType`` is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-eventtype
        '''
        result = self._values.get("event_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def perform_auto_ml(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration ( ``recipeArn`` must not be specified).

        When false (the default), Amazon Personalize uses ``recipeArn`` for training.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-performautoml
        '''
        result = self._values.get("perform_auto_ml")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def perform_hpo(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to perform hyperparameter optimization (HPO) on the chosen recipe.

        The default is ``false`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-performhpo
        '''
        result = self._values.get("perform_hpo")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the recipe used to create the solution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-recipearn
        '''
        result = self._values.get("recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def solution_config(
        self,
    ) -> typing.Optional[typing.Union[CfnSolution.SolutionConfigProperty, _IResolvable_da3f097b]]:
        '''Describes the configuration properties for the solution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-solutionconfig
        '''
        result = self._values.get("solution_config")
        return typing.cast(typing.Optional[typing.Union[CfnSolution.SolutionConfigProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSolutionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataset",
    "CfnDatasetGroup",
    "CfnDatasetGroupProps",
    "CfnDatasetProps",
    "CfnSchema",
    "CfnSchemaProps",
    "CfnSolution",
    "CfnSolutionProps",
]

publication.publish()
