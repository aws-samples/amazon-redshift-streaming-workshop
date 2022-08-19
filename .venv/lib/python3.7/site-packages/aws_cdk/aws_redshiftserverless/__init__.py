'''
# AWS::RedshiftServerless Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_redshiftserverless as redshiftserverless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RedshiftServerless construct libraries](https://constructs.dev/search?q=redshiftserverless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RedshiftServerless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RedshiftServerless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RedshiftServerless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RedshiftServerless.html).

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
class CfnNamespace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespace",
):
    '''A CloudFormation ``AWS::RedshiftServerless::Namespace``.

    :cloudformationResource: AWS::RedshiftServerless::Namespace
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshiftserverless as redshiftserverless
        
        cfn_namespace = redshiftserverless.CfnNamespace(self, "MyCfnNamespace",
            namespace_name="namespaceName",
        
            # the properties below are optional
            admin_username="adminUsername",
            admin_user_password="adminUserPassword",
            db_name="dbName",
            default_iam_role_arn="defaultIamRoleArn",
            final_snapshot_name="finalSnapshotName",
            final_snapshot_retention_period=123,
            iam_roles=["iamRoles"],
            kms_key_id="kmsKeyId",
            log_exports=["logExports"],
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
        namespace_name: builtins.str,
        admin_username: typing.Optional[builtins.str] = None,
        admin_user_password: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        default_iam_role_arn: typing.Optional[builtins.str] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::RedshiftServerless::Namespace``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param namespace_name: ``AWS::RedshiftServerless::Namespace.NamespaceName``.
        :param admin_username: ``AWS::RedshiftServerless::Namespace.AdminUsername``.
        :param admin_user_password: ``AWS::RedshiftServerless::Namespace.AdminUserPassword``.
        :param db_name: ``AWS::RedshiftServerless::Namespace.DbName``.
        :param default_iam_role_arn: ``AWS::RedshiftServerless::Namespace.DefaultIamRoleArn``.
        :param final_snapshot_name: ``AWS::RedshiftServerless::Namespace.FinalSnapshotName``.
        :param final_snapshot_retention_period: ``AWS::RedshiftServerless::Namespace.FinalSnapshotRetentionPeriod``.
        :param iam_roles: ``AWS::RedshiftServerless::Namespace.IamRoles``.
        :param kms_key_id: ``AWS::RedshiftServerless::Namespace.KmsKeyId``.
        :param log_exports: ``AWS::RedshiftServerless::Namespace.LogExports``.
        :param tags: ``AWS::RedshiftServerless::Namespace.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnNamespace.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNamespaceProps(
            namespace_name=namespace_name,
            admin_username=admin_username,
            admin_user_password=admin_user_password,
            db_name=db_name,
            default_iam_role_arn=default_iam_role_arn,
            final_snapshot_name=final_snapshot_name,
            final_snapshot_retention_period=final_snapshot_retention_period,
            iam_roles=iam_roles,
            kms_key_id=kms_key_id,
            log_exports=log_exports,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnNamespace.inspect)
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
            type_hints = typing.get_type_hints(CfnNamespace._render_properties)
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
        '''``AWS::RedshiftServerless::Namespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        '''``AWS::RedshiftServerless::Namespace.NamespaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-namespacename
        '''
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "namespace_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.AdminUsername``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminusername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "admin_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="adminUserPassword")
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.AdminUserPassword``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminuserpassword
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUserPassword"))

    @admin_user_password.setter
    def admin_user_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "admin_user_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUserPassword", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.DbName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-dbname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "db_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.DefaultIamRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-defaultiamrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultIamRoleArn"))

    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "default_iam_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultIamRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="finalSnapshotName")
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.FinalSnapshotName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "finalSnapshotName"))

    @final_snapshot_name.setter
    def final_snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "final_snapshot_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="finalSnapshotRetentionPeriod")
    def final_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''``AWS::RedshiftServerless::Namespace.FinalSnapshotRetentionPeriod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotretentionperiod
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "finalSnapshotRetentionPeriod"))

    @final_snapshot_retention_period.setter
    def final_snapshot_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "final_snapshot_retention_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotRetentionPeriod", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="iamRoles")
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RedshiftServerless::Namespace.IamRoles``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-iamroles
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "iamRoles"))

    @iam_roles.setter
    def iam_roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "iam_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoles", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logExports")
    def log_exports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RedshiftServerless::Namespace.LogExports``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-logexports
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logExports"))

    @log_exports.setter
    def log_exports(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnNamespace, "log_exports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logExports", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_name": "namespaceName",
        "admin_username": "adminUsername",
        "admin_user_password": "adminUserPassword",
        "db_name": "dbName",
        "default_iam_role_arn": "defaultIamRoleArn",
        "final_snapshot_name": "finalSnapshotName",
        "final_snapshot_retention_period": "finalSnapshotRetentionPeriod",
        "iam_roles": "iamRoles",
        "kms_key_id": "kmsKeyId",
        "log_exports": "logExports",
        "tags": "tags",
    },
)
class CfnNamespaceProps:
    def __init__(
        self,
        *,
        namespace_name: builtins.str,
        admin_username: typing.Optional[builtins.str] = None,
        admin_user_password: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        default_iam_role_arn: typing.Optional[builtins.str] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnNamespace``.

        :param namespace_name: ``AWS::RedshiftServerless::Namespace.NamespaceName``.
        :param admin_username: ``AWS::RedshiftServerless::Namespace.AdminUsername``.
        :param admin_user_password: ``AWS::RedshiftServerless::Namespace.AdminUserPassword``.
        :param db_name: ``AWS::RedshiftServerless::Namespace.DbName``.
        :param default_iam_role_arn: ``AWS::RedshiftServerless::Namespace.DefaultIamRoleArn``.
        :param final_snapshot_name: ``AWS::RedshiftServerless::Namespace.FinalSnapshotName``.
        :param final_snapshot_retention_period: ``AWS::RedshiftServerless::Namespace.FinalSnapshotRetentionPeriod``.
        :param iam_roles: ``AWS::RedshiftServerless::Namespace.IamRoles``.
        :param kms_key_id: ``AWS::RedshiftServerless::Namespace.KmsKeyId``.
        :param log_exports: ``AWS::RedshiftServerless::Namespace.LogExports``.
        :param tags: ``AWS::RedshiftServerless::Namespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshiftserverless as redshiftserverless
            
            cfn_namespace_props = redshiftserverless.CfnNamespaceProps(
                namespace_name="namespaceName",
            
                # the properties below are optional
                admin_username="adminUsername",
                admin_user_password="adminUserPassword",
                db_name="dbName",
                default_iam_role_arn="defaultIamRoleArn",
                final_snapshot_name="finalSnapshotName",
                final_snapshot_retention_period=123,
                iam_roles=["iamRoles"],
                kms_key_id="kmsKeyId",
                log_exports=["logExports"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnNamespaceProps.__init__)
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument admin_user_password", value=admin_user_password, expected_type=type_hints["admin_user_password"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument default_iam_role_arn", value=default_iam_role_arn, expected_type=type_hints["default_iam_role_arn"])
            check_type(argname="argument final_snapshot_name", value=final_snapshot_name, expected_type=type_hints["final_snapshot_name"])
            check_type(argname="argument final_snapshot_retention_period", value=final_snapshot_retention_period, expected_type=type_hints["final_snapshot_retention_period"])
            check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_exports", value=log_exports, expected_type=type_hints["log_exports"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "namespace_name": namespace_name,
        }
        if admin_username is not None:
            self._values["admin_username"] = admin_username
        if admin_user_password is not None:
            self._values["admin_user_password"] = admin_user_password
        if db_name is not None:
            self._values["db_name"] = db_name
        if default_iam_role_arn is not None:
            self._values["default_iam_role_arn"] = default_iam_role_arn
        if final_snapshot_name is not None:
            self._values["final_snapshot_name"] = final_snapshot_name
        if final_snapshot_retention_period is not None:
            self._values["final_snapshot_retention_period"] = final_snapshot_retention_period
        if iam_roles is not None:
            self._values["iam_roles"] = iam_roles
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_exports is not None:
            self._values["log_exports"] = log_exports
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''``AWS::RedshiftServerless::Namespace.NamespaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-namespacename
        '''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_username(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.AdminUsername``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminusername
        '''
        result = self._values.get("admin_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.AdminUserPassword``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminuserpassword
        '''
        result = self._values.get("admin_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.DbName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-dbname
        '''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.DefaultIamRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-defaultiamrolearn
        '''
        result = self._values.get("default_iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.FinalSnapshotName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotname
        '''
        result = self._values.get("final_snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''``AWS::RedshiftServerless::Namespace.FinalSnapshotRetentionPeriod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotretentionperiod
        '''
        result = self._values.get("final_snapshot_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RedshiftServerless::Namespace.IamRoles``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-iamroles
        '''
        result = self._values.get("iam_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Namespace.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_exports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RedshiftServerless::Namespace.LogExports``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-logexports
        '''
        result = self._values.get("log_exports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::RedshiftServerless::Namespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnWorkgroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup",
):
    '''A CloudFormation ``AWS::RedshiftServerless::Workgroup``.

    :cloudformationResource: AWS::RedshiftServerless::Workgroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshiftserverless as redshiftserverless
        
        cfn_workgroup = redshiftserverless.CfnWorkgroup(self, "MyCfnWorkgroup",
            workgroup_name="workgroupName",
        
            # the properties below are optional
            base_capacity=123,
            config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                parameter_key="parameterKey",
                parameter_value="parameterValue"
            )],
            enhanced_vpc_routing=False,
            namespace_name="namespaceName",
            publicly_accessible=False,
            security_group_ids=["securityGroupIds"],
            subnet_ids=["subnetIds"],
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
        workgroup_name: builtins.str,
        base_capacity: typing.Optional[jsii.Number] = None,
        config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnWorkgroup.ConfigParameterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        namespace_name: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::RedshiftServerless::Workgroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param workgroup_name: ``AWS::RedshiftServerless::Workgroup.WorkgroupName``.
        :param base_capacity: ``AWS::RedshiftServerless::Workgroup.BaseCapacity``.
        :param config_parameters: ``AWS::RedshiftServerless::Workgroup.ConfigParameters``.
        :param enhanced_vpc_routing: ``AWS::RedshiftServerless::Workgroup.EnhancedVpcRouting``.
        :param namespace_name: ``AWS::RedshiftServerless::Workgroup.NamespaceName``.
        :param publicly_accessible: ``AWS::RedshiftServerless::Workgroup.PubliclyAccessible``.
        :param security_group_ids: ``AWS::RedshiftServerless::Workgroup.SecurityGroupIds``.
        :param subnet_ids: ``AWS::RedshiftServerless::Workgroup.SubnetIds``.
        :param tags: ``AWS::RedshiftServerless::Workgroup.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnWorkgroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkgroupProps(
            workgroup_name=workgroup_name,
            base_capacity=base_capacity,
            config_parameters=config_parameters,
            enhanced_vpc_routing=enhanced_vpc_routing,
            namespace_name=namespace_name,
            publicly_accessible=publicly_accessible,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnWorkgroup.inspect)
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
            type_hints = typing.get_type_hints(CfnWorkgroup._render_properties)
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
        '''``AWS::RedshiftServerless::Workgroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workgroupName")
    def workgroup_name(self) -> builtins.str:
        '''``AWS::RedshiftServerless::Workgroup.WorkgroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-workgroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "workgroupName"))

    @workgroup_name.setter
    def workgroup_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnWorkgroup, "workgroup_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workgroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="baseCapacity")
    def base_capacity(self) -> typing.Optional[jsii.Number]:
        '''``AWS::RedshiftServerless::Workgroup.BaseCapacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-basecapacity
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseCapacity"))

    @base_capacity.setter
    def base_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnWorkgroup, "base_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseCapacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configParameters")
    def config_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnWorkgroup.ConfigParameterProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::RedshiftServerless::Workgroup.ConfigParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-configparameters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnWorkgroup.ConfigParameterProperty", _IResolvable_da3f097b]]]], jsii.get(self, "configParameters"))

    @config_parameters.setter
    def config_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnWorkgroup.ConfigParameterProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnWorkgroup, "config_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enhancedVpcRouting")
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::RedshiftServerless::Workgroup.EnhancedVpcRouting``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-enhancedvpcrouting
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enhancedVpcRouting"))

    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnWorkgroup, "enhanced_vpc_routing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedVpcRouting", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Workgroup.NamespaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-namespacename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnWorkgroup, "namespace_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::RedshiftServerless::Workgroup.PubliclyAccessible``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-publiclyaccessible
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnWorkgroup, "publicly_accessible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RedshiftServerless::Workgroup.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-securitygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnWorkgroup, "security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RedshiftServerless::Workgroup.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-subnetids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnWorkgroup, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.ConfigParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_key": "parameterKey",
            "parameter_value": "parameterValue",
        },
    )
    class ConfigParameterProperty:
        def __init__(
            self,
            *,
            parameter_key: typing.Optional[builtins.str] = None,
            parameter_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param parameter_key: ``CfnWorkgroup.ConfigParameterProperty.ParameterKey``.
            :param parameter_value: ``CfnWorkgroup.ConfigParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                config_parameter_property = redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnWorkgroup.ConfigParameterProperty.__init__)
                check_type(argname="argument parameter_key", value=parameter_key, expected_type=type_hints["parameter_key"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[str, typing.Any] = {}
            if parameter_key is not None:
                self._values["parameter_key"] = parameter_key
            if parameter_value is not None:
                self._values["parameter_value"] = parameter_value

        @builtins.property
        def parameter_key(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkgroup.ConfigParameterProperty.ParameterKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html#cfn-redshiftserverless-workgroup-configparameter-parameterkey
            '''
            result = self._values.get("parameter_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameter_value(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkgroup.ConfigParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html#cfn-redshiftserverless-workgroup-configparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "workgroup_name": "workgroupName",
        "base_capacity": "baseCapacity",
        "config_parameters": "configParameters",
        "enhanced_vpc_routing": "enhancedVpcRouting",
        "namespace_name": "namespaceName",
        "publicly_accessible": "publiclyAccessible",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnWorkgroupProps:
    def __init__(
        self,
        *,
        workgroup_name: builtins.str,
        base_capacity: typing.Optional[jsii.Number] = None,
        config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        namespace_name: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkgroup``.

        :param workgroup_name: ``AWS::RedshiftServerless::Workgroup.WorkgroupName``.
        :param base_capacity: ``AWS::RedshiftServerless::Workgroup.BaseCapacity``.
        :param config_parameters: ``AWS::RedshiftServerless::Workgroup.ConfigParameters``.
        :param enhanced_vpc_routing: ``AWS::RedshiftServerless::Workgroup.EnhancedVpcRouting``.
        :param namespace_name: ``AWS::RedshiftServerless::Workgroup.NamespaceName``.
        :param publicly_accessible: ``AWS::RedshiftServerless::Workgroup.PubliclyAccessible``.
        :param security_group_ids: ``AWS::RedshiftServerless::Workgroup.SecurityGroupIds``.
        :param subnet_ids: ``AWS::RedshiftServerless::Workgroup.SubnetIds``.
        :param tags: ``AWS::RedshiftServerless::Workgroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshiftserverless as redshiftserverless
            
            cfn_workgroup_props = redshiftserverless.CfnWorkgroupProps(
                workgroup_name="workgroupName",
            
                # the properties below are optional
                base_capacity=123,
                config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )],
                enhanced_vpc_routing=False,
                namespace_name="namespaceName",
                publicly_accessible=False,
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnWorkgroupProps.__init__)
            check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            check_type(argname="argument base_capacity", value=base_capacity, expected_type=type_hints["base_capacity"])
            check_type(argname="argument config_parameters", value=config_parameters, expected_type=type_hints["config_parameters"])
            check_type(argname="argument enhanced_vpc_routing", value=enhanced_vpc_routing, expected_type=type_hints["enhanced_vpc_routing"])
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "workgroup_name": workgroup_name,
        }
        if base_capacity is not None:
            self._values["base_capacity"] = base_capacity
        if config_parameters is not None:
            self._values["config_parameters"] = config_parameters
        if enhanced_vpc_routing is not None:
            self._values["enhanced_vpc_routing"] = enhanced_vpc_routing
        if namespace_name is not None:
            self._values["namespace_name"] = namespace_name
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def workgroup_name(self) -> builtins.str:
        '''``AWS::RedshiftServerless::Workgroup.WorkgroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-workgroupname
        '''
        result = self._values.get("workgroup_name")
        assert result is not None, "Required property 'workgroup_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_capacity(self) -> typing.Optional[jsii.Number]:
        '''``AWS::RedshiftServerless::Workgroup.BaseCapacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-basecapacity
        '''
        result = self._values.get("base_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def config_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnWorkgroup.ConfigParameterProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::RedshiftServerless::Workgroup.ConfigParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-configparameters
        '''
        result = self._values.get("config_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnWorkgroup.ConfigParameterProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::RedshiftServerless::Workgroup.EnhancedVpcRouting``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-enhancedvpcrouting
        '''
        result = self._values.get("enhanced_vpc_routing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def namespace_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::RedshiftServerless::Workgroup.NamespaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-namespacename
        '''
        result = self._values.get("namespace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::RedshiftServerless::Workgroup.PubliclyAccessible``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RedshiftServerless::Workgroup.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RedshiftServerless::Workgroup.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::RedshiftServerless::Workgroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkgroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNamespace",
    "CfnNamespaceProps",
    "CfnWorkgroup",
    "CfnWorkgroupProps",
]

publication.publish()
