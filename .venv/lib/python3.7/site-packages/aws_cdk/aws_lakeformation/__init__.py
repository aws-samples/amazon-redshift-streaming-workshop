'''
# AWS::LakeFormation Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_lakeformation as lakeformation
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LakeFormation construct libraries](https://constructs.dev/search?q=lakeformation)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LakeFormation resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LakeFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.html).

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
class CfnDataCellsFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataCellsFilter",
):
    '''A CloudFormation ``AWS::LakeFormation::DataCellsFilter``.

    :cloudformationResource: AWS::LakeFormation::DataCellsFilter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        # all_rows_wildcard: Any
        
        cfn_data_cells_filter = lakeformation.CfnDataCellsFilter(self, "MyCfnDataCellsFilter",
            database_name="databaseName",
            name="name",
            table_catalog_id="tableCatalogId",
            table_name="tableName",
        
            # the properties below are optional
            column_names=["columnNames"],
            column_wildcard=lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                excluded_column_names=["excludedColumnNames"]
            ),
            row_filter=lakeformation.CfnDataCellsFilter.RowFilterProperty(
                all_rows_wildcard=all_rows_wildcard,
                filter_expression="filterExpression"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        database_name: builtins.str,
        name: builtins.str,
        table_catalog_id: builtins.str,
        table_name: builtins.str,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        column_wildcard: typing.Optional[typing.Union[typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        row_filter: typing.Optional[typing.Union[typing.Union["CfnDataCellsFilter.RowFilterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::DataCellsFilter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param database_name: ``AWS::LakeFormation::DataCellsFilter.DatabaseName``.
        :param name: ``AWS::LakeFormation::DataCellsFilter.Name``.
        :param table_catalog_id: ``AWS::LakeFormation::DataCellsFilter.TableCatalogId``.
        :param table_name: ``AWS::LakeFormation::DataCellsFilter.TableName``.
        :param column_names: ``AWS::LakeFormation::DataCellsFilter.ColumnNames``.
        :param column_wildcard: ``AWS::LakeFormation::DataCellsFilter.ColumnWildcard``.
        :param row_filter: ``AWS::LakeFormation::DataCellsFilter.RowFilter``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataCellsFilter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataCellsFilterProps(
            database_name=database_name,
            name=name,
            table_catalog_id=table_catalog_id,
            table_name=table_name,
            column_names=column_names,
            column_wildcard=column_wildcard,
            row_filter=row_filter,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataCellsFilter.inspect)
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
            type_hints = typing.get_type_hints(CfnDataCellsFilter._render_properties)
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
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        '''``AWS::LakeFormation::DataCellsFilter.DatabaseName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-databasename
        '''
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataCellsFilter, "database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::LakeFormation::DataCellsFilter.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataCellsFilter, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableCatalogId")
    def table_catalog_id(self) -> builtins.str:
        '''``AWS::LakeFormation::DataCellsFilter.TableCatalogId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablecatalogid
        '''
        return typing.cast(builtins.str, jsii.get(self, "tableCatalogId"))

    @table_catalog_id.setter
    def table_catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataCellsFilter, "table_catalog_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableCatalogId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        '''``AWS::LakeFormation::DataCellsFilter.TableName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablename
        '''
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataCellsFilter, "table_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="columnNames")
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::DataCellsFilter.ColumnNames``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnnames
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "columnNames"))

    @column_names.setter
    def column_names(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataCellsFilter, "column_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnNames", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="columnWildcard")
    def column_wildcard(
        self,
    ) -> typing.Optional[typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", _IResolvable_da3f097b]]:
        '''``AWS::LakeFormation::DataCellsFilter.ColumnWildcard``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnwildcard
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", _IResolvable_da3f097b]], jsii.get(self, "columnWildcard"))

    @column_wildcard.setter
    def column_wildcard(
        self,
        value: typing.Optional[typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataCellsFilter, "column_wildcard").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnWildcard", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rowFilter")
    def row_filter(
        self,
    ) -> typing.Optional[typing.Union["CfnDataCellsFilter.RowFilterProperty", _IResolvable_da3f097b]]:
        '''``AWS::LakeFormation::DataCellsFilter.RowFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-rowfilter
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataCellsFilter.RowFilterProperty", _IResolvable_da3f097b]], jsii.get(self, "rowFilter"))

    @row_filter.setter
    def row_filter(
        self,
        value: typing.Optional[typing.Union["CfnDataCellsFilter.RowFilterProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataCellsFilter, "row_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowFilter", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataCellsFilter.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param excluded_column_names: ``CfnDataCellsFilter.ColumnWildcardProperty.ExcludedColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDataCellsFilter.ColumnWildcardProperty.__init__)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataCellsFilter.ColumnWildcardProperty.ExcludedColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html#cfn-lakeformation-datacellsfilter-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataCellsFilter.RowFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_rows_wildcard": "allRowsWildcard",
            "filter_expression": "filterExpression",
        },
    )
    class RowFilterProperty:
        def __init__(
            self,
            *,
            all_rows_wildcard: typing.Any = None,
            filter_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param all_rows_wildcard: ``CfnDataCellsFilter.RowFilterProperty.AllRowsWildcard``.
            :param filter_expression: ``CfnDataCellsFilter.RowFilterProperty.FilterExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # all_rows_wildcard: Any
                
                row_filter_property = lakeformation.CfnDataCellsFilter.RowFilterProperty(
                    all_rows_wildcard=all_rows_wildcard,
                    filter_expression="filterExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDataCellsFilter.RowFilterProperty.__init__)
                check_type(argname="argument all_rows_wildcard", value=all_rows_wildcard, expected_type=type_hints["all_rows_wildcard"])
                check_type(argname="argument filter_expression", value=filter_expression, expected_type=type_hints["filter_expression"])
            self._values: typing.Dict[str, typing.Any] = {}
            if all_rows_wildcard is not None:
                self._values["all_rows_wildcard"] = all_rows_wildcard
            if filter_expression is not None:
                self._values["filter_expression"] = filter_expression

        @builtins.property
        def all_rows_wildcard(self) -> typing.Any:
            '''``CfnDataCellsFilter.RowFilterProperty.AllRowsWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html#cfn-lakeformation-datacellsfilter-rowfilter-allrowswildcard
            '''
            result = self._values.get("all_rows_wildcard")
            return typing.cast(typing.Any, result)

        @builtins.property
        def filter_expression(self) -> typing.Optional[builtins.str]:
            '''``CfnDataCellsFilter.RowFilterProperty.FilterExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html#cfn-lakeformation-datacellsfilter-rowfilter-filterexpression
            '''
            result = self._values.get("filter_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RowFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataCellsFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "name": "name",
        "table_catalog_id": "tableCatalogId",
        "table_name": "tableName",
        "column_names": "columnNames",
        "column_wildcard": "columnWildcard",
        "row_filter": "rowFilter",
    },
)
class CfnDataCellsFilterProps:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        name: builtins.str,
        table_catalog_id: builtins.str,
        table_name: builtins.str,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        column_wildcard: typing.Optional[typing.Union[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        row_filter: typing.Optional[typing.Union[typing.Union[CfnDataCellsFilter.RowFilterProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataCellsFilter``.

        :param database_name: ``AWS::LakeFormation::DataCellsFilter.DatabaseName``.
        :param name: ``AWS::LakeFormation::DataCellsFilter.Name``.
        :param table_catalog_id: ``AWS::LakeFormation::DataCellsFilter.TableCatalogId``.
        :param table_name: ``AWS::LakeFormation::DataCellsFilter.TableName``.
        :param column_names: ``AWS::LakeFormation::DataCellsFilter.ColumnNames``.
        :param column_wildcard: ``AWS::LakeFormation::DataCellsFilter.ColumnWildcard``.
        :param row_filter: ``AWS::LakeFormation::DataCellsFilter.RowFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            # all_rows_wildcard: Any
            
            cfn_data_cells_filter_props = lakeformation.CfnDataCellsFilterProps(
                database_name="databaseName",
                name="name",
                table_catalog_id="tableCatalogId",
                table_name="tableName",
            
                # the properties below are optional
                column_names=["columnNames"],
                column_wildcard=lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                ),
                row_filter=lakeformation.CfnDataCellsFilter.RowFilterProperty(
                    all_rows_wildcard=all_rows_wildcard,
                    filter_expression="filterExpression"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataCellsFilterProps.__init__)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument table_catalog_id", value=table_catalog_id, expected_type=type_hints["table_catalog_id"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
            check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
            check_type(argname="argument row_filter", value=row_filter, expected_type=type_hints["row_filter"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "name": name,
            "table_catalog_id": table_catalog_id,
            "table_name": table_name,
        }
        if column_names is not None:
            self._values["column_names"] = column_names
        if column_wildcard is not None:
            self._values["column_wildcard"] = column_wildcard
        if row_filter is not None:
            self._values["row_filter"] = row_filter

    @builtins.property
    def database_name(self) -> builtins.str:
        '''``AWS::LakeFormation::DataCellsFilter.DatabaseName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-databasename
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::LakeFormation::DataCellsFilter.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_catalog_id(self) -> builtins.str:
        '''``AWS::LakeFormation::DataCellsFilter.TableCatalogId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablecatalogid
        '''
        result = self._values.get("table_catalog_id")
        assert result is not None, "Required property 'table_catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''``AWS::LakeFormation::DataCellsFilter.TableName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablename
        '''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::DataCellsFilter.ColumnNames``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnnames
        '''
        result = self._values.get("column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def column_wildcard(
        self,
    ) -> typing.Optional[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, _IResolvable_da3f097b]]:
        '''``AWS::LakeFormation::DataCellsFilter.ColumnWildcard``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnwildcard
        '''
        result = self._values.get("column_wildcard")
        return typing.cast(typing.Optional[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def row_filter(
        self,
    ) -> typing.Optional[typing.Union[CfnDataCellsFilter.RowFilterProperty, _IResolvable_da3f097b]]:
        '''``AWS::LakeFormation::DataCellsFilter.RowFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-rowfilter
        '''
        result = self._values.get("row_filter")
        return typing.cast(typing.Optional[typing.Union[CfnDataCellsFilter.RowFilterProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataCellsFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDataLakeSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings",
):
    '''A CloudFormation ``AWS::LakeFormation::DataLakeSettings``.

    The ``AWS::LakeFormation::DataLakeSettings`` resource is an AWS Lake Formation resource type that manages the data lake settings for your account. Note that the CloudFormation template only supports updating the ``Admins`` list. It does not support updating the `CreateDatabaseDefaultPermissions <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-settings.html#aws-lake-formation-api-aws-lake-formation-api-settings-DataLakeSettings>`_ or `CreateTableDefaultPermissions <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-settings.html#aws-lake-formation-api-aws-lake-formation-api-settings-DataLakeSettings>`_ . Those permissions can only be edited in the DataLakeSettings resource via the API.

    :cloudformationResource: AWS::LakeFormation::DataLakeSettings
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        cfn_data_lake_settings = lakeformation.CfnDataLakeSettings(self, "MyCfnDataLakeSettings",
            admins=[lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            )],
            trusted_resource_owners=["trustedResourceOwners"]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        admins: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::DataLakeSettings``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param admins: A list of AWS Lake Formation principals.
        :param trusted_resource_owners: ``AWS::LakeFormation::DataLakeSettings.TrustedResourceOwners``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataLakeSettings.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataLakeSettingsProps(
            admins=admins, trusted_resource_owners=trusted_resource_owners
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataLakeSettings.inspect)
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
            type_hints = typing.get_type_hints(CfnDataLakeSettings._render_properties)
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
    @jsii.member(jsii_name="admins")
    def admins(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", _IResolvable_da3f097b]]]]:
        '''A list of AWS Lake Formation principals.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", _IResolvable_da3f097b]]]], jsii.get(self, "admins"))

    @admins.setter
    def admins(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataLakeSettings, "admins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "admins", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trustedResourceOwners")
    def trusted_resource_owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::DataLakeSettings.TrustedResourceOwners``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedResourceOwners"))

    @trusted_resource_owners.setter
    def trusted_resource_owners(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDataLakeSettings, "trusted_resource_owners").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedResourceOwners", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Lake Formation principal.

            :param data_lake_principal_identifier: An identifier for the Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDataLakeSettings.DataLakePrincipalProperty.__init__)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''An identifier for the Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "admins": "admins",
        "trusted_resource_owners": "trustedResourceOwners",
    },
)
class CfnDataLakeSettingsProps:
    def __init__(
        self,
        *,
        admins: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataLakeSettings``.

        :param admins: A list of AWS Lake Formation principals.
        :param trusted_resource_owners: ``AWS::LakeFormation::DataLakeSettings.TrustedResourceOwners``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            cfn_data_lake_settings_props = lakeformation.CfnDataLakeSettingsProps(
                admins=[lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )],
                trusted_resource_owners=["trustedResourceOwners"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDataLakeSettingsProps.__init__)
            check_type(argname="argument admins", value=admins, expected_type=type_hints["admins"])
            check_type(argname="argument trusted_resource_owners", value=trusted_resource_owners, expected_type=type_hints["trusted_resource_owners"])
        self._values: typing.Dict[str, typing.Any] = {}
        if admins is not None:
            self._values["admins"] = admins
        if trusted_resource_owners is not None:
            self._values["trusted_resource_owners"] = trusted_resource_owners

    @builtins.property
    def admins(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, _IResolvable_da3f097b]]]]:
        '''A list of AWS Lake Formation principals.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        '''
        result = self._values.get("admins")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def trusted_resource_owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::DataLakeSettings.TrustedResourceOwners``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        '''
        result = self._values.get("trusted_resource_owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataLakeSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPermissions(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions",
):
    '''A CloudFormation ``AWS::LakeFormation::Permissions``.

    The ``AWS::LakeFormation::Permissions`` resource represents the permissions that a principal has on an AWS Glue Data Catalog resource (such as AWS Glue database or AWS Glue tables). When you upload a permissions stack, the permissions are granted to the principal and when you remove the stack, the permissions are revoked from the principal. If you remove a stack, and the principal does not have the permissions referenced in the stack then AWS Lake Formation will throw an error because you can’t call revoke on non-existing permissions. To successfully remove the stack, you’ll need to regrant those permissions and then remove the stack.

    :cloudformationResource: AWS::LakeFormation::Permissions
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        cfn_permissions = lakeformation.CfnPermissions(self, "MyCfnPermissions",
            data_lake_principal=lakeformation.CfnPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            ),
            resource=lakeformation.CfnPermissions.ResourceProperty(
                database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    s3_resource="s3Resource"
                ),
                table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                    table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                ),
                table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    ),
                    database_name="databaseName",
                    name="name"
                )
            ),
        
            # the properties below are optional
            permissions=["permissions"],
            permissions_with_grant_option=["permissionsWithGrantOption"]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        data_lake_principal: typing.Union[typing.Union["CfnPermissions.DataLakePrincipalProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        resource: typing.Union[typing.Union["CfnPermissions.ResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::Permissions``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_lake_principal: The AWS Lake Formation principal.
        :param resource: A structure for the resource.
        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPermissions.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionsProps(
            data_lake_principal=data_lake_principal,
            resource=resource,
            permissions=permissions,
            permissions_with_grant_option=permissions_with_grant_option,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPermissions.inspect)
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
            type_hints = typing.get_type_hints(CfnPermissions._render_properties)
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
    @jsii.member(jsii_name="dataLakePrincipal")
    def data_lake_principal(
        self,
    ) -> typing.Union["CfnPermissions.DataLakePrincipalProperty", _IResolvable_da3f097b]:
        '''The AWS Lake Formation principal.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        '''
        return typing.cast(typing.Union["CfnPermissions.DataLakePrincipalProperty", _IResolvable_da3f097b], jsii.get(self, "dataLakePrincipal"))

    @data_lake_principal.setter
    def data_lake_principal(
        self,
        value: typing.Union["CfnPermissions.DataLakePrincipalProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissions, "data_lake_principal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLakePrincipal", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union["CfnPermissions.ResourceProperty", _IResolvable_da3f097b]:
        '''A structure for the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        '''
        return typing.cast(typing.Union["CfnPermissions.ResourceProperty", _IResolvable_da3f097b], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union["CfnPermissions.ResourceProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissions, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The permissions granted or revoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissions, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsWithGrantOption"))

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPermissions, "permissions_with_grant_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsWithGrantOption", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A wildcard object, consisting of an optional list of excluded column names or indexes.

            :param excluded_column_names: Excludes column names. Any column with this name will be excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnPermissions.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissions.ColumnWildcardProperty.__init__)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Excludes column names.

            Any column with this name will be excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Lake Formation principal.

            :param data_lake_principal_identifier: An identifier for the Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissions.DataLakePrincipalProperty.__init__)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''An identifier for the Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.DataLocationResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "s3_resource": "s3Resource"},
    )
    class DataLocationResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            s3_resource: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for a data location object where permissions are granted or revoked.

            :param catalog_id: ``CfnPermissions.DataLocationResourceProperty.CatalogId``.
            :param s3_resource: Currently not supported by AWS CloudFormation .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_location_resource_property = lakeformation.CfnPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    s3_resource="s3Resource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissions.DataLocationResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument s3_resource", value=s3_resource, expected_type=type_hints["s3_resource"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if s3_resource is not None:
                self._values["s3_resource"] = s3_resource

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.DataLocationResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_resource(self) -> typing.Optional[builtins.str]:
            '''Currently not supported by AWS CloudFormation .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource
            '''
            result = self._values.get("s3_resource")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLocationResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for the database object.

            :param catalog_id: ``CfnPermissions.DatabaseResourceProperty.CatalogId``.
            :param name: The name of the database resource. Unique to the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissions.DatabaseResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.DatabaseResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the database resource.

            Unique to the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_resource": "databaseResource",
            "data_location_resource": "dataLocationResource",
            "table_resource": "tableResource",
            "table_with_columns_resource": "tableWithColumnsResource",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            database_resource: typing.Optional[typing.Union[typing.Union["CfnPermissions.DatabaseResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            data_location_resource: typing.Optional[typing.Union[typing.Union["CfnPermissions.DataLocationResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            table_resource: typing.Optional[typing.Union[typing.Union["CfnPermissions.TableResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            table_with_columns_resource: typing.Optional[typing.Union[typing.Union["CfnPermissions.TableWithColumnsResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A structure for the resource.

            :param database_resource: A structure for the database object.
            :param data_location_resource: A structure for a data location object where permissions are granted or revoked.
            :param table_resource: A structure for the table object. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param table_with_columns_resource: Currently not supported by AWS CloudFormation .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                resource_property = lakeformation.CfnPermissions.ResourceProperty(
                    database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        s3_resource="s3Resource"
                    ),
                    table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                        table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                    ),
                    table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        ),
                        database_name="databaseName",
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissions.ResourceProperty.__init__)
                check_type(argname="argument database_resource", value=database_resource, expected_type=type_hints["database_resource"])
                check_type(argname="argument data_location_resource", value=data_location_resource, expected_type=type_hints["data_location_resource"])
                check_type(argname="argument table_resource", value=table_resource, expected_type=type_hints["table_resource"])
                check_type(argname="argument table_with_columns_resource", value=table_with_columns_resource, expected_type=type_hints["table_with_columns_resource"])
            self._values: typing.Dict[str, typing.Any] = {}
            if database_resource is not None:
                self._values["database_resource"] = database_resource
            if data_location_resource is not None:
                self._values["data_location_resource"] = data_location_resource
            if table_resource is not None:
                self._values["table_resource"] = table_resource
            if table_with_columns_resource is not None:
                self._values["table_with_columns_resource"] = table_with_columns_resource

        @builtins.property
        def database_resource(
            self,
        ) -> typing.Optional[typing.Union["CfnPermissions.DatabaseResourceProperty", _IResolvable_da3f097b]]:
            '''A structure for the database object.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource
            '''
            result = self._values.get("database_resource")
            return typing.cast(typing.Optional[typing.Union["CfnPermissions.DatabaseResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def data_location_resource(
            self,
        ) -> typing.Optional[typing.Union["CfnPermissions.DataLocationResourceProperty", _IResolvable_da3f097b]]:
            '''A structure for a data location object where permissions are granted or revoked.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource
            '''
            result = self._values.get("data_location_resource")
            return typing.cast(typing.Optional[typing.Union["CfnPermissions.DataLocationResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def table_resource(
            self,
        ) -> typing.Optional[typing.Union["CfnPermissions.TableResourceProperty", _IResolvable_da3f097b]]:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource
            '''
            result = self._values.get("table_resource")
            return typing.cast(typing.Optional[typing.Union["CfnPermissions.TableResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def table_with_columns_resource(
            self,
        ) -> typing.Optional[typing.Union["CfnPermissions.TableWithColumnsResourceProperty", _IResolvable_da3f097b]]:
            '''Currently not supported by AWS CloudFormation .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource
            '''
            result = self._values.get("table_with_columns_resource")
            return typing.cast(typing.Optional[typing.Union["CfnPermissions.TableWithColumnsResourceProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Optional[typing.Union[typing.Union["CfnPermissions.TableWildcardProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :param catalog_id: ``CfnPermissions.TableResourceProperty.CatalogId``.
            :param database_name: The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table.
            :param table_wildcard: An empty object representing all tables under a database. If this field is specified instead of the ``Name`` field, all tables under ``DatabaseName`` will have permission changes applied.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_resource_property = lakeformation.CfnPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                    table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissions.TableResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.TableResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the database for the table.

            Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(
            self,
        ) -> typing.Optional[typing.Union["CfnPermissions.TableWildcardProperty", _IResolvable_da3f097b]]:
            '''An empty object representing all tables under a database.

            If this field is specified instead of the ``Name`` field, all tables under ``DatabaseName`` will have permission changes applied.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Optional[typing.Union["CfnPermissions.TableWildcardProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.TableWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class TableWildcardProperty:
        def __init__(self) -> None:
            '''A wildcard object representing every table under a database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_wildcard_property = lakeformation.CfnPermissions.TableWildcardProperty()
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "column_names": "columnNames",
            "column_wildcard": "columnWildcard",
            "database_name": "databaseName",
            "name": "name",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            column_wildcard: typing.Optional[typing.Union[typing.Union["CfnPermissions.ColumnWildcardProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for a table with columns object. This object is only used when granting a SELECT permission.

            This object must take a value for at least one of ``ColumnsNames`` , ``ColumnsIndexes`` , or ``ColumnsWildcard`` .

            :param catalog_id: ``CfnPermissions.TableWithColumnsResourceProperty.CatalogId``.
            :param column_names: The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param column_wildcard: A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param database_name: The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    ),
                    database_name="databaseName",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPermissions.TableWithColumnsResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if column_names is not None:
                self._values["column_names"] = column_names
            if column_wildcard is not None:
                self._values["column_wildcard"] = column_wildcard
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.TableWithColumnsResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of column names for the table.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def column_wildcard(
            self,
        ) -> typing.Optional[typing.Union["CfnPermissions.ColumnWildcardProperty", _IResolvable_da3f097b]]:
            '''A wildcard specified by a ``ColumnWildcard`` object.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard
            '''
            result = self._values.get("column_wildcard")
            return typing.cast(typing.Optional[typing.Union["CfnPermissions.ColumnWildcardProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the database for the table with columns resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissionsProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_lake_principal": "dataLakePrincipal",
        "resource": "resource",
        "permissions": "permissions",
        "permissions_with_grant_option": "permissionsWithGrantOption",
    },
)
class CfnPermissionsProps:
    def __init__(
        self,
        *,
        data_lake_principal: typing.Union[typing.Union[CfnPermissions.DataLakePrincipalProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        resource: typing.Union[typing.Union[CfnPermissions.ResourceProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermissions``.

        :param data_lake_principal: The AWS Lake Formation principal.
        :param resource: A structure for the resource.
        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            cfn_permissions_props = lakeformation.CfnPermissionsProps(
                data_lake_principal=lakeformation.CfnPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                ),
                resource=lakeformation.CfnPermissions.ResourceProperty(
                    database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        s3_resource="s3Resource"
                    ),
                    table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                        table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                    ),
                    table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        ),
                        database_name="databaseName",
                        name="name"
                    )
                ),
            
                # the properties below are optional
                permissions=["permissions"],
                permissions_with_grant_option=["permissionsWithGrantOption"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPermissionsProps.__init__)
            check_type(argname="argument data_lake_principal", value=data_lake_principal, expected_type=type_hints["data_lake_principal"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument permissions_with_grant_option", value=permissions_with_grant_option, expected_type=type_hints["permissions_with_grant_option"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_lake_principal": data_lake_principal,
            "resource": resource,
        }
        if permissions is not None:
            self._values["permissions"] = permissions
        if permissions_with_grant_option is not None:
            self._values["permissions_with_grant_option"] = permissions_with_grant_option

    @builtins.property
    def data_lake_principal(
        self,
    ) -> typing.Union[CfnPermissions.DataLakePrincipalProperty, _IResolvable_da3f097b]:
        '''The AWS Lake Formation principal.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        '''
        result = self._values.get("data_lake_principal")
        assert result is not None, "Required property 'data_lake_principal' is missing"
        return typing.cast(typing.Union[CfnPermissions.DataLakePrincipalProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[CfnPermissions.ResourceProperty, _IResolvable_da3f097b]:
        '''A structure for the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[CfnPermissions.ResourceProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The permissions granted or revoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        '''
        result = self._values.get("permissions_with_grant_option")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPrincipalPermissions(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions",
):
    '''A CloudFormation ``AWS::LakeFormation::PrincipalPermissions``.

    :cloudformationResource: AWS::LakeFormation::PrincipalPermissions
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        # catalog: Any
        # table_wildcard: Any
        
        cfn_principal_permissions = lakeformation.CfnPrincipalPermissions(self, "MyCfnPrincipalPermissions",
            permissions=["permissions"],
            permissions_with_grant_option=["permissionsWithGrantOption"],
            principal=lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            ),
            resource=lakeformation.CfnPrincipalPermissions.ResourceProperty(
                catalog=catalog,
                database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                    database_name="databaseName",
                    name="name",
                    table_catalog_id="tableCatalogId",
                    table_name="tableName"
                ),
                data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    resource_arn="resourceArn"
                ),
                lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                ),
                lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                    catalog_id="catalogId",
                    expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    )],
                    resource_type="resourceType"
                ),
                table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
        
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                ),
                table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
        
                    # the properties below are optional
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    )
                )
            ),
        
            # the properties below are optional
            catalog="catalog"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        permissions: typing.Sequence[builtins.str],
        permissions_with_grant_option: typing.Sequence[builtins.str],
        principal: typing.Union[typing.Union["CfnPrincipalPermissions.DataLakePrincipalProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        resource: typing.Union[typing.Union["CfnPrincipalPermissions.ResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        catalog: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::PrincipalPermissions``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param permissions: ``AWS::LakeFormation::PrincipalPermissions.Permissions``.
        :param permissions_with_grant_option: ``AWS::LakeFormation::PrincipalPermissions.PermissionsWithGrantOption``.
        :param principal: ``AWS::LakeFormation::PrincipalPermissions.Principal``.
        :param resource: ``AWS::LakeFormation::PrincipalPermissions.Resource``.
        :param catalog: ``AWS::LakeFormation::PrincipalPermissions.Catalog``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPrincipalPermissions.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrincipalPermissionsProps(
            permissions=permissions,
            permissions_with_grant_option=permissions_with_grant_option,
            principal=principal,
            resource=resource,
            catalog=catalog,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPrincipalPermissions.inspect)
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
            type_hints = typing.get_type_hints(CfnPrincipalPermissions._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPrincipalIdentifier")
    def attr_principal_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: PrincipalIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrincipalIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceIdentifier")
    def attr_resource_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.List[builtins.str]:
        '''``AWS::LakeFormation::PrincipalPermissions.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissions
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPrincipalPermissions, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> typing.List[builtins.str]:
        '''``AWS::LakeFormation::PrincipalPermissions.PermissionsWithGrantOption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissionswithgrantoption
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissionsWithGrantOption"))

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPrincipalPermissions, "permissions_with_grant_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsWithGrantOption", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="principal")
    def principal(
        self,
    ) -> typing.Union["CfnPrincipalPermissions.DataLakePrincipalProperty", _IResolvable_da3f097b]:
        '''``AWS::LakeFormation::PrincipalPermissions.Principal``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-principal
        '''
        return typing.cast(typing.Union["CfnPrincipalPermissions.DataLakePrincipalProperty", _IResolvable_da3f097b], jsii.get(self, "principal"))

    @principal.setter
    def principal(
        self,
        value: typing.Union["CfnPrincipalPermissions.DataLakePrincipalProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPrincipalPermissions, "principal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union["CfnPrincipalPermissions.ResourceProperty", _IResolvable_da3f097b]:
        '''``AWS::LakeFormation::PrincipalPermissions.Resource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-resource
        '''
        return typing.cast(typing.Union["CfnPrincipalPermissions.ResourceProperty", _IResolvable_da3f097b], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union["CfnPrincipalPermissions.ResourceProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPrincipalPermissions, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> typing.Optional[builtins.str]:
        '''``AWS::LakeFormation::PrincipalPermissions.Catalog``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-catalog
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPrincipalPermissions, "catalog").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param excluded_column_names: ``CfnPrincipalPermissions.ColumnWildcardProperty.ExcludedColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.ColumnWildcardProperty.__init__)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPrincipalPermissions.ColumnWildcardProperty.ExcludedColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html#cfn-lakeformation-principalpermissions-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "name": "name",
            "table_catalog_id": "tableCatalogId",
            "table_name": "tableName",
        },
    )
    class DataCellsFilterResourceProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            name: builtins.str,
            table_catalog_id: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''
            :param database_name: ``CfnPrincipalPermissions.DataCellsFilterResourceProperty.DatabaseName``.
            :param name: ``CfnPrincipalPermissions.DataCellsFilterResourceProperty.Name``.
            :param table_catalog_id: ``CfnPrincipalPermissions.DataCellsFilterResourceProperty.TableCatalogId``.
            :param table_name: ``CfnPrincipalPermissions.DataCellsFilterResourceProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_cells_filter_resource_property = lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                    database_name="databaseName",
                    name="name",
                    table_catalog_id="tableCatalogId",
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.DataCellsFilterResourceProperty.__init__)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_catalog_id", value=table_catalog_id, expected_type=type_hints["table_catalog_id"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[str, typing.Any] = {
                "database_name": database_name,
                "name": name,
                "table_catalog_id": table_catalog_id,
                "table_name": table_name,
            }

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnPrincipalPermissions.DataCellsFilterResourceProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnPrincipalPermissions.DataCellsFilterResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_catalog_id(self) -> builtins.str:
            '''``CfnPrincipalPermissions.DataCellsFilterResourceProperty.TableCatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablecatalogid
            '''
            result = self._values.get("table_catalog_id")
            assert result is not None, "Required property 'table_catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''``CfnPrincipalPermissions.DataCellsFilterResourceProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCellsFilterResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_lake_principal_identifier: ``CfnPrincipalPermissions.DataLakePrincipalProperty.DataLakePrincipalIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.DataLakePrincipalProperty.__init__)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnPrincipalPermissions.DataLakePrincipalProperty.DataLakePrincipalIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html#cfn-lakeformation-principalpermissions-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "resource_arn": "resourceArn"},
    )
    class DataLocationResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            resource_arn: builtins.str,
        ) -> None:
            '''
            :param catalog_id: ``CfnPrincipalPermissions.DataLocationResourceProperty.CatalogId``.
            :param resource_arn: ``CfnPrincipalPermissions.DataLocationResourceProperty.ResourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_location_resource_property = lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.DataLocationResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "resource_arn": resource_arn,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnPrincipalPermissions.DataLocationResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html#cfn-lakeformation-principalpermissions-datalocationresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''``CfnPrincipalPermissions.DataLocationResourceProperty.ResourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html#cfn-lakeformation-principalpermissions-datalocationresource-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLocationResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(self, *, catalog_id: builtins.str, name: builtins.str) -> None:
            '''
            :param catalog_id: ``CfnPrincipalPermissions.DatabaseResourceProperty.CatalogId``.
            :param name: ``CfnPrincipalPermissions.DatabaseResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.DatabaseResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnPrincipalPermissions.DatabaseResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html#cfn-lakeformation-principalpermissions-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnPrincipalPermissions.DatabaseResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html#cfn-lakeformation-principalpermissions-databaseresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "tag_key": "tagKey",
            "tag_values": "tagValues",
        },
    )
    class LFTagKeyResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            tag_key: builtins.str,
            tag_values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param catalog_id: ``CfnPrincipalPermissions.LFTagKeyResourceProperty.CatalogId``.
            :param tag_key: ``CfnPrincipalPermissions.LFTagKeyResourceProperty.TagKey``.
            :param tag_values: ``CfnPrincipalPermissions.LFTagKeyResourceProperty.TagValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                l_fTag_key_resource_property = lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.LFTagKeyResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "tag_key": tag_key,
                "tag_values": tag_values,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnPrincipalPermissions.LFTagKeyResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_key(self) -> builtins.str:
            '''``CfnPrincipalPermissions.LFTagKeyResourceProperty.TagKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-tagkey
            '''
            result = self._values.get("tag_key")
            assert result is not None, "Required property 'tag_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_values(self) -> typing.List[builtins.str]:
            '''``CfnPrincipalPermissions.LFTagKeyResourceProperty.TagValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-tagvalues
            '''
            result = self._values.get("tag_values")
            assert result is not None, "Required property 'tag_values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagKeyResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "expression": "expression",
            "resource_type": "resourceType",
        },
    )
    class LFTagPolicyResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            expression: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnPrincipalPermissions.LFTagProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            resource_type: builtins.str,
        ) -> None:
            '''
            :param catalog_id: ``CfnPrincipalPermissions.LFTagPolicyResourceProperty.CatalogId``.
            :param expression: ``CfnPrincipalPermissions.LFTagPolicyResourceProperty.Expression``.
            :param resource_type: ``CfnPrincipalPermissions.LFTagPolicyResourceProperty.ResourceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                l_fTag_policy_resource_property = lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                    catalog_id="catalogId",
                    expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    )],
                    resource_type="resourceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.LFTagPolicyResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "expression": expression,
                "resource_type": resource_type,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnPrincipalPermissions.LFTagPolicyResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def expression(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPrincipalPermissions.LFTagProperty", _IResolvable_da3f097b]]]:
            '''``CfnPrincipalPermissions.LFTagPolicyResourceProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPrincipalPermissions.LFTagProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''``CfnPrincipalPermissions.LFTagPolicyResourceProperty.ResourceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagPolicyResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.LFTagProperty",
        jsii_struct_bases=[],
        name_mapping={"tag_key": "tagKey", "tag_values": "tagValues"},
    )
    class LFTagProperty:
        def __init__(
            self,
            *,
            tag_key: typing.Optional[builtins.str] = None,
            tag_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param tag_key: ``CfnPrincipalPermissions.LFTagProperty.TagKey``.
            :param tag_values: ``CfnPrincipalPermissions.LFTagProperty.TagValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                l_fTag_property = lakeformation.CfnPrincipalPermissions.LFTagProperty(
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.LFTagProperty.__init__)
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[str, typing.Any] = {}
            if tag_key is not None:
                self._values["tag_key"] = tag_key
            if tag_values is not None:
                self._values["tag_values"] = tag_values

        @builtins.property
        def tag_key(self) -> typing.Optional[builtins.str]:
            '''``CfnPrincipalPermissions.LFTagProperty.TagKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html#cfn-lakeformation-principalpermissions-lftag-tagkey
            '''
            result = self._values.get("tag_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPrincipalPermissions.LFTagProperty.TagValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html#cfn-lakeformation-principalpermissions-lftag-tagvalues
            '''
            result = self._values.get("tag_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog": "catalog",
            "database": "database",
            "data_cells_filter": "dataCellsFilter",
            "data_location": "dataLocation",
            "lf_tag": "lfTag",
            "lf_tag_policy": "lfTagPolicy",
            "table": "table",
            "table_with_columns": "tableWithColumns",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            catalog: typing.Any = None,
            database: typing.Optional[typing.Union[typing.Union["CfnPrincipalPermissions.DatabaseResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            data_cells_filter: typing.Optional[typing.Union[typing.Union["CfnPrincipalPermissions.DataCellsFilterResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            data_location: typing.Optional[typing.Union[typing.Union["CfnPrincipalPermissions.DataLocationResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            lf_tag: typing.Optional[typing.Union[typing.Union["CfnPrincipalPermissions.LFTagKeyResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            lf_tag_policy: typing.Optional[typing.Union[typing.Union["CfnPrincipalPermissions.LFTagPolicyResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            table: typing.Optional[typing.Union[typing.Union["CfnPrincipalPermissions.TableResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            table_with_columns: typing.Optional[typing.Union[typing.Union["CfnPrincipalPermissions.TableWithColumnsResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param catalog: ``CfnPrincipalPermissions.ResourceProperty.Catalog``.
            :param database: ``CfnPrincipalPermissions.ResourceProperty.Database``.
            :param data_cells_filter: ``CfnPrincipalPermissions.ResourceProperty.DataCellsFilter``.
            :param data_location: ``CfnPrincipalPermissions.ResourceProperty.DataLocation``.
            :param lf_tag: ``CfnPrincipalPermissions.ResourceProperty.LFTag``.
            :param lf_tag_policy: ``CfnPrincipalPermissions.ResourceProperty.LFTagPolicy``.
            :param table: ``CfnPrincipalPermissions.ResourceProperty.Table``.
            :param table_with_columns: ``CfnPrincipalPermissions.ResourceProperty.TableWithColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # catalog: Any
                # table_wildcard: Any
                
                resource_property = lakeformation.CfnPrincipalPermissions.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                        database_name="databaseName",
                        name="name",
                        table_catalog_id="tableCatalogId",
                        table_name="tableName"
                    ),
                    data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        resource_arn="resourceArn"
                    ),
                    lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                        catalog_id="catalogId",
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    ),
                    lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                        catalog_id="catalogId",
                        expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                            tag_key="tagKey",
                            tag_values=["tagValues"]
                        )],
                        resource_type="resourceType"
                    ),
                    table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                
                        # the properties below are optional
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.ResourceProperty.__init__)
                check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument data_cells_filter", value=data_cells_filter, expected_type=type_hints["data_cells_filter"])
                check_type(argname="argument data_location", value=data_location, expected_type=type_hints["data_location"])
                check_type(argname="argument lf_tag", value=lf_tag, expected_type=type_hints["lf_tag"])
                check_type(argname="argument lf_tag_policy", value=lf_tag_policy, expected_type=type_hints["lf_tag_policy"])
                check_type(argname="argument table", value=table, expected_type=type_hints["table"])
                check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog is not None:
                self._values["catalog"] = catalog
            if database is not None:
                self._values["database"] = database
            if data_cells_filter is not None:
                self._values["data_cells_filter"] = data_cells_filter
            if data_location is not None:
                self._values["data_location"] = data_location
            if lf_tag is not None:
                self._values["lf_tag"] = lf_tag
            if lf_tag_policy is not None:
                self._values["lf_tag_policy"] = lf_tag_policy
            if table is not None:
                self._values["table"] = table
            if table_with_columns is not None:
                self._values["table_with_columns"] = table_with_columns

        @builtins.property
        def catalog(self) -> typing.Any:
            '''``CfnPrincipalPermissions.ResourceProperty.Catalog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-catalog
            '''
            result = self._values.get("catalog")
            return typing.cast(typing.Any, result)

        @builtins.property
        def database(
            self,
        ) -> typing.Optional[typing.Union["CfnPrincipalPermissions.DatabaseResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnPrincipalPermissions.ResourceProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-database
            '''
            result = self._values.get("database")
            return typing.cast(typing.Optional[typing.Union["CfnPrincipalPermissions.DatabaseResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def data_cells_filter(
            self,
        ) -> typing.Optional[typing.Union["CfnPrincipalPermissions.DataCellsFilterResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnPrincipalPermissions.ResourceProperty.DataCellsFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-datacellsfilter
            '''
            result = self._values.get("data_cells_filter")
            return typing.cast(typing.Optional[typing.Union["CfnPrincipalPermissions.DataCellsFilterResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def data_location(
            self,
        ) -> typing.Optional[typing.Union["CfnPrincipalPermissions.DataLocationResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnPrincipalPermissions.ResourceProperty.DataLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-datalocation
            '''
            result = self._values.get("data_location")
            return typing.cast(typing.Optional[typing.Union["CfnPrincipalPermissions.DataLocationResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def lf_tag(
            self,
        ) -> typing.Optional[typing.Union["CfnPrincipalPermissions.LFTagKeyResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnPrincipalPermissions.ResourceProperty.LFTag``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-lftag
            '''
            result = self._values.get("lf_tag")
            return typing.cast(typing.Optional[typing.Union["CfnPrincipalPermissions.LFTagKeyResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def lf_tag_policy(
            self,
        ) -> typing.Optional[typing.Union["CfnPrincipalPermissions.LFTagPolicyResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnPrincipalPermissions.ResourceProperty.LFTagPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-lftagpolicy
            '''
            result = self._values.get("lf_tag_policy")
            return typing.cast(typing.Optional[typing.Union["CfnPrincipalPermissions.LFTagPolicyResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def table(
            self,
        ) -> typing.Optional[typing.Union["CfnPrincipalPermissions.TableResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnPrincipalPermissions.ResourceProperty.Table``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-table
            '''
            result = self._values.get("table")
            return typing.cast(typing.Optional[typing.Union["CfnPrincipalPermissions.TableResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def table_with_columns(
            self,
        ) -> typing.Optional[typing.Union["CfnPrincipalPermissions.TableWithColumnsResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnPrincipalPermissions.ResourceProperty.TableWithColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-tablewithcolumns
            '''
            result = self._values.get("table_with_columns")
            return typing.cast(typing.Optional[typing.Union["CfnPrincipalPermissions.TableWithColumnsResourceProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Any = None,
        ) -> None:
            '''
            :param catalog_id: ``CfnPrincipalPermissions.TableResourceProperty.CatalogId``.
            :param database_name: ``CfnPrincipalPermissions.TableResourceProperty.DatabaseName``.
            :param name: ``CfnPrincipalPermissions.TableResourceProperty.Name``.
            :param table_wildcard: ``CfnPrincipalPermissions.TableResourceProperty.TableWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # table_wildcard: Any
                
                table_resource_property = lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.TableResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
            }
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnPrincipalPermissions.TableResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnPrincipalPermissions.TableResourceProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPrincipalPermissions.TableResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(self) -> typing.Any:
            '''``CfnPrincipalPermissions.TableResourceProperty.TableWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "column_names": "columnNames",
            "column_wildcard": "columnWildcard",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: builtins.str,
            column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            column_wildcard: typing.Optional[typing.Union[typing.Union["CfnPrincipalPermissions.ColumnWildcardProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param catalog_id: ``CfnPrincipalPermissions.TableWithColumnsResourceProperty.CatalogId``.
            :param database_name: ``CfnPrincipalPermissions.TableWithColumnsResourceProperty.DatabaseName``.
            :param name: ``CfnPrincipalPermissions.TableWithColumnsResourceProperty.Name``.
            :param column_names: ``CfnPrincipalPermissions.TableWithColumnsResourceProperty.ColumnNames``.
            :param column_wildcard: ``CfnPrincipalPermissions.TableWithColumnsResourceProperty.ColumnWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                
                    # the properties below are optional
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPrincipalPermissions.TableWithColumnsResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
                "name": name,
            }
            if column_names is not None:
                self._values["column_names"] = column_names
            if column_wildcard is not None:
                self._values["column_wildcard"] = column_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnPrincipalPermissions.TableWithColumnsResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnPrincipalPermissions.TableWithColumnsResourceProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnPrincipalPermissions.TableWithColumnsResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPrincipalPermissions.TableWithColumnsResourceProperty.ColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def column_wildcard(
            self,
        ) -> typing.Optional[typing.Union["CfnPrincipalPermissions.ColumnWildcardProperty", _IResolvable_da3f097b]]:
            '''``CfnPrincipalPermissions.TableWithColumnsResourceProperty.ColumnWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnwildcard
            '''
            result = self._values.get("column_wildcard")
            return typing.cast(typing.Optional[typing.Union["CfnPrincipalPermissions.ColumnWildcardProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissionsProps",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "permissions_with_grant_option": "permissionsWithGrantOption",
        "principal": "principal",
        "resource": "resource",
        "catalog": "catalog",
    },
)
class CfnPrincipalPermissionsProps:
    def __init__(
        self,
        *,
        permissions: typing.Sequence[builtins.str],
        permissions_with_grant_option: typing.Sequence[builtins.str],
        principal: typing.Union[typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        resource: typing.Union[typing.Union[CfnPrincipalPermissions.ResourceProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        catalog: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrincipalPermissions``.

        :param permissions: ``AWS::LakeFormation::PrincipalPermissions.Permissions``.
        :param permissions_with_grant_option: ``AWS::LakeFormation::PrincipalPermissions.PermissionsWithGrantOption``.
        :param principal: ``AWS::LakeFormation::PrincipalPermissions.Principal``.
        :param resource: ``AWS::LakeFormation::PrincipalPermissions.Resource``.
        :param catalog: ``AWS::LakeFormation::PrincipalPermissions.Catalog``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            # catalog: Any
            # table_wildcard: Any
            
            cfn_principal_permissions_props = lakeformation.CfnPrincipalPermissionsProps(
                permissions=["permissions"],
                permissions_with_grant_option=["permissionsWithGrantOption"],
                principal=lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                ),
                resource=lakeformation.CfnPrincipalPermissions.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                        database_name="databaseName",
                        name="name",
                        table_catalog_id="tableCatalogId",
                        table_name="tableName"
                    ),
                    data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        resource_arn="resourceArn"
                    ),
                    lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                        catalog_id="catalogId",
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    ),
                    lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                        catalog_id="catalogId",
                        expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                            tag_key="tagKey",
                            tag_values=["tagValues"]
                        )],
                        resource_type="resourceType"
                    ),
                    table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
            
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
            
                        # the properties below are optional
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        )
                    )
                ),
            
                # the properties below are optional
                catalog="catalog"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPrincipalPermissionsProps.__init__)
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument permissions_with_grant_option", value=permissions_with_grant_option, expected_type=type_hints["permissions_with_grant_option"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
        self._values: typing.Dict[str, typing.Any] = {
            "permissions": permissions,
            "permissions_with_grant_option": permissions_with_grant_option,
            "principal": principal,
            "resource": resource,
        }
        if catalog is not None:
            self._values["catalog"] = catalog

    @builtins.property
    def permissions(self) -> typing.List[builtins.str]:
        '''``AWS::LakeFormation::PrincipalPermissions.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissions
        '''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def permissions_with_grant_option(self) -> typing.List[builtins.str]:
        '''``AWS::LakeFormation::PrincipalPermissions.PermissionsWithGrantOption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissionswithgrantoption
        '''
        result = self._values.get("permissions_with_grant_option")
        assert result is not None, "Required property 'permissions_with_grant_option' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def principal(
        self,
    ) -> typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, _IResolvable_da3f097b]:
        '''``AWS::LakeFormation::PrincipalPermissions.Principal``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[CfnPrincipalPermissions.ResourceProperty, _IResolvable_da3f097b]:
        '''``AWS::LakeFormation::PrincipalPermissions.Resource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[CfnPrincipalPermissions.ResourceProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def catalog(self) -> typing.Optional[builtins.str]:
        '''``AWS::LakeFormation::PrincipalPermissions.Catalog``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-catalog
        '''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrincipalPermissionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnResource",
):
    '''A CloudFormation ``AWS::LakeFormation::Resource``.

    The ``AWS::LakeFormation::Resource`` represents the data (Amazon S3 buckets and folders) that is being registered with AWS Lake Formation . When a ``Resource`` type CloudFormation template is uploaded, an AWS Lake Formation ```RegisterResource`` <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-RegisterResource>`_ API call is made to register the resource. When a ``Resource`` type CloudFormation template is removed, the AWS Lake Formation ```DeregisterResource`` <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-DeregisterResource>`_ API is called.

    :cloudformationResource: AWS::LakeFormation::Resource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        cfn_resource = lakeformation.CfnResource(self, "MyCfnResource",
            resource_arn="resourceArn",
            use_service_linked_role=False,
        
            # the properties below are optional
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        resource_arn: builtins.str,
        use_service_linked_role: typing.Union[builtins.bool, _IResolvable_da3f097b],
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::Resource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param use_service_linked_role: Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog.
        :param role_arn: The IAM role that registered a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResource.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceProps(
            resource_arn=resource_arn,
            use_service_linked_role=use_service_linked_role,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResource.inspect)
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
            type_hints = typing.get_type_hints(CfnResource._render_properties)
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
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResource, "resource_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="useServiceLinkedRole")
    def use_service_linked_role(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "useServiceLinkedRole"))

    @use_service_linked_role.setter
    def use_service_linked_role(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResource, "use_service_linked_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useServiceLinkedRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM role that registered a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResource, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_arn": "resourceArn",
        "use_service_linked_role": "useServiceLinkedRole",
        "role_arn": "roleArn",
    },
)
class CfnResourceProps:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        use_service_linked_role: typing.Union[builtins.bool, _IResolvable_da3f097b],
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResource``.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param use_service_linked_role: Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog.
        :param role_arn: The IAM role that registered a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            cfn_resource_props = lakeformation.CfnResourceProps(
                resource_arn="resourceArn",
                use_service_linked_role=False,
            
                # the properties below are optional
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResourceProps.__init__)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument use_service_linked_role", value=use_service_linked_role, expected_type=type_hints["use_service_linked_role"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "use_service_linked_role": use_service_linked_role,
        }
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_service_linked_role(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        '''
        result = self._values.get("use_service_linked_role")
        assert result is not None, "Required property 'use_service_linked_role' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM role that registered a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTag(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnTag",
):
    '''A CloudFormation ``AWS::LakeFormation::Tag``.

    :cloudformationResource: AWS::LakeFormation::Tag
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        cfn_tag = lakeformation.CfnTag(self, "MyCfnTag",
            tag_key="tagKey",
            tag_values=["tagValues"],
        
            # the properties below are optional
            catalog_id="catalogId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        tag_key: builtins.str,
        tag_values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::Tag``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param tag_key: ``AWS::LakeFormation::Tag.TagKey``.
        :param tag_values: ``AWS::LakeFormation::Tag.TagValues``.
        :param catalog_id: ``AWS::LakeFormation::Tag.CatalogId``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTag.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTagProps(
            tag_key=tag_key, tag_values=tag_values, catalog_id=catalog_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTag.inspect)
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
            type_hints = typing.get_type_hints(CfnTag._render_properties)
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
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        '''``AWS::LakeFormation::Tag.TagKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagkey
        '''
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTag, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagValues")
    def tag_values(self) -> typing.List[builtins.str]:
        '''``AWS::LakeFormation::Tag.TagValues``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagvalues
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tagValues"))

    @tag_values.setter
    def tag_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTag, "tag_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValues", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::LakeFormation::Tag.CatalogId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-catalogid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTag, "catalog_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)


@jsii.implements(_IInspectable_c2943556)
class CfnTagAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation",
):
    '''A CloudFormation ``AWS::LakeFormation::TagAssociation``.

    :cloudformationResource: AWS::LakeFormation::TagAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        # catalog: Any
        # table_wildcard: Any
        
        cfn_tag_association = lakeformation.CfnTagAssociation(self, "MyCfnTagAssociation",
            lf_tags=[lakeformation.CfnTagAssociation.LFTagPairProperty(
                catalog_id="catalogId",
                tag_key="tagKey",
                tag_values=["tagValues"]
            )],
            resource=lakeformation.CfnTagAssociation.ResourceProperty(
                catalog=catalog,
                database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                table=lakeformation.CfnTagAssociation.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
        
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                ),
                table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    database_name="databaseName",
                    name="name"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        lf_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTagAssociation.LFTagPairProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        resource: typing.Union[typing.Union["CfnTagAssociation.ResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
    ) -> None:
        '''Create a new ``AWS::LakeFormation::TagAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lf_tags: ``AWS::LakeFormation::TagAssociation.LFTags``.
        :param resource: ``AWS::LakeFormation::TagAssociation.Resource``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTagAssociationProps(lf_tags=lf_tags, resource=resource)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagAssociation.inspect)
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
            type_hints = typing.get_type_hints(CfnTagAssociation._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceIdentifier")
    def attr_resource_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTagsIdentifier")
    def attr_tags_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: TagsIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTagsIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lfTags")
    def lf_tags(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTagAssociation.LFTagPairProperty", _IResolvable_da3f097b]]]:
        '''``AWS::LakeFormation::TagAssociation.LFTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-lftags
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTagAssociation.LFTagPairProperty", _IResolvable_da3f097b]]], jsii.get(self, "lfTags"))

    @lf_tags.setter
    def lf_tags(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTagAssociation.LFTagPairProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTagAssociation, "lf_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lfTags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union["CfnTagAssociation.ResourceProperty", _IResolvable_da3f097b]:
        '''``AWS::LakeFormation::TagAssociation.Resource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-resource
        '''
        return typing.cast(typing.Union["CfnTagAssociation.ResourceProperty", _IResolvable_da3f097b], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union["CfnTagAssociation.ResourceProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTagAssociation, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(self, *, catalog_id: builtins.str, name: builtins.str) -> None:
            '''
            :param catalog_id: ``CfnTagAssociation.DatabaseResourceProperty.CatalogId``.
            :param name: ``CfnTagAssociation.DatabaseResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTagAssociation.DatabaseResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnTagAssociation.DatabaseResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html#cfn-lakeformation-tagassociation-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnTagAssociation.DatabaseResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html#cfn-lakeformation-tagassociation-databaseresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.LFTagPairProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "tag_key": "tagKey",
            "tag_values": "tagValues",
        },
    )
    class LFTagPairProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            tag_key: builtins.str,
            tag_values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param catalog_id: ``CfnTagAssociation.LFTagPairProperty.CatalogId``.
            :param tag_key: ``CfnTagAssociation.LFTagPairProperty.TagKey``.
            :param tag_values: ``CfnTagAssociation.LFTagPairProperty.TagValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                l_fTag_pair_property = lakeformation.CfnTagAssociation.LFTagPairProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTagAssociation.LFTagPairProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "tag_key": tag_key,
                "tag_values": tag_values,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnTagAssociation.LFTagPairProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_key(self) -> builtins.str:
            '''``CfnTagAssociation.LFTagPairProperty.TagKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-tagkey
            '''
            result = self._values.get("tag_key")
            assert result is not None, "Required property 'tag_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_values(self) -> typing.List[builtins.str]:
            '''``CfnTagAssociation.LFTagPairProperty.TagValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-tagvalues
            '''
            result = self._values.get("tag_values")
            assert result is not None, "Required property 'tag_values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagPairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog": "catalog",
            "database": "database",
            "table": "table",
            "table_with_columns": "tableWithColumns",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            catalog: typing.Any = None,
            database: typing.Optional[typing.Union[typing.Union["CfnTagAssociation.DatabaseResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            table: typing.Optional[typing.Union[typing.Union["CfnTagAssociation.TableResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            table_with_columns: typing.Optional[typing.Union[typing.Union["CfnTagAssociation.TableWithColumnsResourceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param catalog: ``CfnTagAssociation.ResourceProperty.Catalog``.
            :param database: ``CfnTagAssociation.ResourceProperty.Database``.
            :param table: ``CfnTagAssociation.ResourceProperty.Table``.
            :param table_with_columns: ``CfnTagAssociation.ResourceProperty.TableWithColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # catalog: Any
                # table_wildcard: Any
                
                resource_property = lakeformation.CfnTagAssociation.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    table=lakeformation.CfnTagAssociation.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        database_name="databaseName",
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTagAssociation.ResourceProperty.__init__)
                check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument table", value=table, expected_type=type_hints["table"])
                check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog is not None:
                self._values["catalog"] = catalog
            if database is not None:
                self._values["database"] = database
            if table is not None:
                self._values["table"] = table
            if table_with_columns is not None:
                self._values["table_with_columns"] = table_with_columns

        @builtins.property
        def catalog(self) -> typing.Any:
            '''``CfnTagAssociation.ResourceProperty.Catalog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-catalog
            '''
            result = self._values.get("catalog")
            return typing.cast(typing.Any, result)

        @builtins.property
        def database(
            self,
        ) -> typing.Optional[typing.Union["CfnTagAssociation.DatabaseResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnTagAssociation.ResourceProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-database
            '''
            result = self._values.get("database")
            return typing.cast(typing.Optional[typing.Union["CfnTagAssociation.DatabaseResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def table(
            self,
        ) -> typing.Optional[typing.Union["CfnTagAssociation.TableResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnTagAssociation.ResourceProperty.Table``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-table
            '''
            result = self._values.get("table")
            return typing.cast(typing.Optional[typing.Union["CfnTagAssociation.TableResourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def table_with_columns(
            self,
        ) -> typing.Optional[typing.Union["CfnTagAssociation.TableWithColumnsResourceProperty", _IResolvable_da3f097b]]:
            '''``CfnTagAssociation.ResourceProperty.TableWithColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-tablewithcolumns
            '''
            result = self._values.get("table_with_columns")
            return typing.cast(typing.Optional[typing.Union["CfnTagAssociation.TableWithColumnsResourceProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Any = None,
        ) -> None:
            '''
            :param catalog_id: ``CfnTagAssociation.TableResourceProperty.CatalogId``.
            :param database_name: ``CfnTagAssociation.TableResourceProperty.DatabaseName``.
            :param name: ``CfnTagAssociation.TableResourceProperty.Name``.
            :param table_wildcard: ``CfnTagAssociation.TableResourceProperty.TableWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # table_wildcard: Any
                
                table_resource_property = lakeformation.CfnTagAssociation.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTagAssociation.TableResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
            }
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnTagAssociation.TableResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnTagAssociation.TableResourceProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnTagAssociation.TableResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(self) -> typing.Any:
            '''``CfnTagAssociation.TableResourceProperty.TableWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "column_names": "columnNames",
            "database_name": "databaseName",
            "name": "name",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            column_names: typing.Sequence[builtins.str],
            database_name: builtins.str,
            name: builtins.str,
        ) -> None:
            '''
            :param catalog_id: ``CfnTagAssociation.TableWithColumnsResourceProperty.CatalogId``.
            :param column_names: ``CfnTagAssociation.TableWithColumnsResourceProperty.ColumnNames``.
            :param database_name: ``CfnTagAssociation.TableWithColumnsResourceProperty.DatabaseName``.
            :param name: ``CfnTagAssociation.TableWithColumnsResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    database_name="databaseName",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTagAssociation.TableWithColumnsResourceProperty.__init__)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "column_names": column_names,
                "database_name": database_name,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnTagAssociation.TableWithColumnsResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_names(self) -> typing.List[builtins.str]:
            '''``CfnTagAssociation.TableWithColumnsResourceProperty.ColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            assert result is not None, "Required property 'column_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnTagAssociation.TableWithColumnsResourceProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnTagAssociation.TableWithColumnsResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"lf_tags": "lfTags", "resource": "resource"},
)
class CfnTagAssociationProps:
    def __init__(
        self,
        *,
        lf_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTagAssociation.LFTagPairProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        resource: typing.Union[typing.Union[CfnTagAssociation.ResourceProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
    ) -> None:
        '''Properties for defining a ``CfnTagAssociation``.

        :param lf_tags: ``AWS::LakeFormation::TagAssociation.LFTags``.
        :param resource: ``AWS::LakeFormation::TagAssociation.Resource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            # catalog: Any
            # table_wildcard: Any
            
            cfn_tag_association_props = lakeformation.CfnTagAssociationProps(
                lf_tags=[lakeformation.CfnTagAssociation.LFTagPairProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )],
                resource=lakeformation.CfnTagAssociation.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    table=lakeformation.CfnTagAssociation.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
            
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        database_name="databaseName",
                        name="name"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagAssociationProps.__init__)
            check_type(argname="argument lf_tags", value=lf_tags, expected_type=type_hints["lf_tags"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[str, typing.Any] = {
            "lf_tags": lf_tags,
            "resource": resource,
        }

    @builtins.property
    def lf_tags(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTagAssociation.LFTagPairProperty, _IResolvable_da3f097b]]]:
        '''``AWS::LakeFormation::TagAssociation.LFTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-lftags
        '''
        result = self._values.get("lf_tags")
        assert result is not None, "Required property 'lf_tags' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTagAssociation.LFTagPairProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[CfnTagAssociation.ResourceProperty, _IResolvable_da3f097b]:
        '''``AWS::LakeFormation::TagAssociation.Resource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[CfnTagAssociation.ResourceProperty, _IResolvable_da3f097b], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagProps",
    jsii_struct_bases=[],
    name_mapping={
        "tag_key": "tagKey",
        "tag_values": "tagValues",
        "catalog_id": "catalogId",
    },
)
class CfnTagProps:
    def __init__(
        self,
        *,
        tag_key: builtins.str,
        tag_values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTag``.

        :param tag_key: ``AWS::LakeFormation::Tag.TagKey``.
        :param tag_values: ``AWS::LakeFormation::Tag.TagValues``.
        :param catalog_id: ``AWS::LakeFormation::Tag.CatalogId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            cfn_tag_props = lakeformation.CfnTagProps(
                tag_key="tagKey",
                tag_values=["tagValues"],
            
                # the properties below are optional
                catalog_id="catalogId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagProps.__init__)
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "tag_key": tag_key,
            "tag_values": tag_values,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def tag_key(self) -> builtins.str:
        '''``AWS::LakeFormation::Tag.TagKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagkey
        '''
        result = self._values.get("tag_key")
        assert result is not None, "Required property 'tag_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_values(self) -> typing.List[builtins.str]:
        '''``AWS::LakeFormation::Tag.TagValues``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagvalues
        '''
        result = self._values.get("tag_values")
        assert result is not None, "Required property 'tag_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::LakeFormation::Tag.CatalogId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-catalogid
        '''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataCellsFilter",
    "CfnDataCellsFilterProps",
    "CfnDataLakeSettings",
    "CfnDataLakeSettingsProps",
    "CfnPermissions",
    "CfnPermissionsProps",
    "CfnPrincipalPermissions",
    "CfnPrincipalPermissionsProps",
    "CfnResource",
    "CfnResourceProps",
    "CfnTag",
    "CfnTagAssociation",
    "CfnTagAssociationProps",
    "CfnTagProps",
]

publication.publish()
