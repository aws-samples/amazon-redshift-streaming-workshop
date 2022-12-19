'''
# AWS::Grafana Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_grafana as grafana
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Grafana construct libraries](https://constructs.dev/search?q=grafana)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Grafana resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Grafana.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Grafana](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Grafana.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnWorkspace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_grafana.CfnWorkspace",
):
    '''A CloudFormation ``AWS::Grafana::Workspace``.

    :cloudformationResource: AWS::Grafana::Workspace
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_grafana as grafana
        
        cfn_workspace = grafana.CfnWorkspace(self, "MyCfnWorkspace",
            account_access_type="accountAccessType",
            authentication_providers=["authenticationProviders"],
            client_token="clientToken",
            data_sources=["dataSources"],
            description="description",
            name="name",
            notification_destinations=["notificationDestinations"],
            organizational_units=["organizationalUnits"],
            organization_role_name="organizationRoleName",
            permission_type="permissionType",
            role_arn="roleArn",
            saml_configuration=grafana.CfnWorkspace.SamlConfigurationProperty(
                idp_metadata=grafana.CfnWorkspace.IdpMetadataProperty(
                    url="url",
                    xml="xml"
                ),
        
                # the properties below are optional
                allowed_organizations=["allowedOrganizations"],
                assertion_attributes=grafana.CfnWorkspace.AssertionAttributesProperty(
                    email="email",
                    groups="groups",
                    login="login",
                    name="name",
                    org="org",
                    role="role"
                ),
                login_validity_duration=123,
                role_values=grafana.CfnWorkspace.RoleValuesProperty(
                    admin=["admin"],
                    editor=["editor"]
                )
            ),
            stack_set_name="stackSetName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account_access_type: typing.Optional[builtins.str] = None,
        authentication_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_token: typing.Optional[builtins.str] = None,
        data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notification_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
        organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_role_name: typing.Optional[builtins.str] = None,
        permission_type: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        saml_configuration: typing.Optional[typing.Union[typing.Union["CfnWorkspace.SamlConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        stack_set_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Grafana::Workspace``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_access_type: ``AWS::Grafana::Workspace.AccountAccessType``.
        :param authentication_providers: ``AWS::Grafana::Workspace.AuthenticationProviders``.
        :param client_token: ``AWS::Grafana::Workspace.ClientToken``.
        :param data_sources: ``AWS::Grafana::Workspace.DataSources``.
        :param description: ``AWS::Grafana::Workspace.Description``.
        :param name: ``AWS::Grafana::Workspace.Name``.
        :param notification_destinations: ``AWS::Grafana::Workspace.NotificationDestinations``.
        :param organizational_units: ``AWS::Grafana::Workspace.OrganizationalUnits``.
        :param organization_role_name: ``AWS::Grafana::Workspace.OrganizationRoleName``.
        :param permission_type: ``AWS::Grafana::Workspace.PermissionType``.
        :param role_arn: ``AWS::Grafana::Workspace.RoleArn``.
        :param saml_configuration: ``AWS::Grafana::Workspace.SamlConfiguration``.
        :param stack_set_name: ``AWS::Grafana::Workspace.StackSetName``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__972564e8260607f3980c99a1e9aecab41a9a45a486b896a29b3870ef3024c82d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkspaceProps(
            account_access_type=account_access_type,
            authentication_providers=authentication_providers,
            client_token=client_token,
            data_sources=data_sources,
            description=description,
            name=name,
            notification_destinations=notification_destinations,
            organizational_units=organizational_units,
            organization_role_name=organization_role_name,
            permission_type=permission_type,
            role_arn=role_arn,
            saml_configuration=saml_configuration,
            stack_set_name=stack_set_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d1ddbb2c282ef63cbb246c4096b7de3713eca2c5e898a4fb0399bceaaea80a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e08c8dd7b33829bf4264a10897017350edb485216cf0320b30df6a4971d42cb2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTimestamp")
    def attr_creation_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''
        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrGrafanaVersion")
    def attr_grafana_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: GrafanaVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGrafanaVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrModificationTimestamp")
    def attr_modification_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModificationTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModificationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrSamlConfigurationStatus")
    def attr_saml_configuration_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: SamlConfigurationStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSamlConfigurationStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrSsoClientId")
    def attr_sso_client_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SsoClientId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSsoClientId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accountAccessType")
    def account_access_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.AccountAccessType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-accountaccesstype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountAccessType"))

    @account_access_type.setter
    def account_access_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4788a164346232bc27f2ed87a4f889be94efaa385debfe7555b9c38ef7b43c82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountAccessType", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationProviders")
    def authentication_providers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Grafana::Workspace.AuthenticationProviders``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-authenticationproviders
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authenticationProviders"))

    @authentication_providers.setter
    def authentication_providers(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d659e2c8f9a80dbb1ff10a5d496ecce9ddb784e34300fef292b95604867dd120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationProviders", value)

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.ClientToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-clienttoken
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67e7c7d4ab889d7976d4a0296a9cbd591db1c64ed24ef025e255a240848da349)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value)

    @builtins.property
    @jsii.member(jsii_name="dataSources")
    def data_sources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Grafana::Workspace.DataSources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-datasources
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataSources"))

    @data_sources.setter
    def data_sources(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3dfcb10305df8d464fbbcb5e8fd3d5b6da64568993c8b2c51b8dcd3395b6ac9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSources", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8893d9a8b4f97f5af788c15dca1db97953d288f193df1c206ed4015e08c9c2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3054f2932686c0aea4252a167d3c57cd2cac6f217af055688e0e4ad5956bce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationDestinations")
    def notification_destinations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Grafana::Workspace.NotificationDestinations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-notificationdestinations
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationDestinations"))

    @notification_destinations.setter
    def notification_destinations(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b512e7c00943f52045050d8d881411bf80d8753e7e5db4cfa04be2d23c840a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationDestinations", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnits")
    def organizational_units(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Grafana::Workspace.OrganizationalUnits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-organizationalunits
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "organizationalUnits"))

    @organizational_units.setter
    def organizational_units(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab5eb86d4408bb6fa769c29f35ddd196f30186a96e904ce407fa53d08a69a42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnits", value)

    @builtins.property
    @jsii.member(jsii_name="organizationRoleName")
    def organization_role_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.OrganizationRoleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-organizationrolename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationRoleName"))

    @organization_role_name.setter
    def organization_role_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a0bc3f30f5cd3553fef63aadcf02d8cd56cd0a20cd147f34b2b500608b2dba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="permissionType")
    def permission_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.PermissionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-permissiontype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionType"))

    @permission_type.setter
    def permission_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2912f1e45e2bf3ca7cdbd6783ea28e244af545c2648fd8b9c918da6bdfb2a69e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionType", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edafda7b927ef527400465d2e8fb7713cb6a76ed45cd51372ae245440c1f42ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="samlConfiguration")
    def saml_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnWorkspace.SamlConfigurationProperty", _IResolvable_da3f097b]]:
        '''``AWS::Grafana::Workspace.SamlConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-samlconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnWorkspace.SamlConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "samlConfiguration"))

    @saml_configuration.setter
    def saml_configuration(
        self,
        value: typing.Optional[typing.Union["CfnWorkspace.SamlConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__512287bf24818cb838cc5045af81a100afbe0fdcf464601403fff719622ccc4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samlConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="stackSetName")
    def stack_set_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.StackSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-stacksetname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stackSetName"))

    @stack_set_name.setter
    def stack_set_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61ab7cafff5a486f361d533b95f12ec0ab7499ff5e38660d0dcabb7a049a78e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackSetName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_grafana.CfnWorkspace.AssertionAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "email": "email",
            "groups": "groups",
            "login": "login",
            "name": "name",
            "org": "org",
            "role": "role",
        },
    )
    class AssertionAttributesProperty:
        def __init__(
            self,
            *,
            email: typing.Optional[builtins.str] = None,
            groups: typing.Optional[builtins.str] = None,
            login: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            org: typing.Optional[builtins.str] = None,
            role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param email: ``CfnWorkspace.AssertionAttributesProperty.Email``.
            :param groups: ``CfnWorkspace.AssertionAttributesProperty.Groups``.
            :param login: ``CfnWorkspace.AssertionAttributesProperty.Login``.
            :param name: ``CfnWorkspace.AssertionAttributesProperty.Name``.
            :param org: ``CfnWorkspace.AssertionAttributesProperty.Org``.
            :param role: ``CfnWorkspace.AssertionAttributesProperty.Role``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_grafana as grafana
                
                assertion_attributes_property = grafana.CfnWorkspace.AssertionAttributesProperty(
                    email="email",
                    groups="groups",
                    login="login",
                    name="name",
                    org="org",
                    role="role"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__426a4b6fbcb381e0187dcb5da594244c44b4957c28015e552b55102d8f9d90bb)
                check_type(argname="argument email", value=email, expected_type=type_hints["email"])
                check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
                check_type(argname="argument login", value=login, expected_type=type_hints["login"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument org", value=org, expected_type=type_hints["org"])
                check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email is not None:
                self._values["email"] = email
            if groups is not None:
                self._values["groups"] = groups
            if login is not None:
                self._values["login"] = login
            if name is not None:
                self._values["name"] = name
            if org is not None:
                self._values["org"] = org
            if role is not None:
                self._values["role"] = role

        @builtins.property
        def email(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.AssertionAttributesProperty.Email``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-email
            '''
            result = self._values.get("email")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def groups(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.AssertionAttributesProperty.Groups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-groups
            '''
            result = self._values.get("groups")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def login(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.AssertionAttributesProperty.Login``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-login
            '''
            result = self._values.get("login")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.AssertionAttributesProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def org(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.AssertionAttributesProperty.Org``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-org
            '''
            result = self._values.get("org")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.AssertionAttributesProperty.Role``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-role
            '''
            result = self._values.get("role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssertionAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_grafana.CfnWorkspace.IdpMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url", "xml": "xml"},
    )
    class IdpMetadataProperty:
        def __init__(
            self,
            *,
            url: typing.Optional[builtins.str] = None,
            xml: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param url: ``CfnWorkspace.IdpMetadataProperty.Url``.
            :param xml: ``CfnWorkspace.IdpMetadataProperty.Xml``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-idpmetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_grafana as grafana
                
                idp_metadata_property = grafana.CfnWorkspace.IdpMetadataProperty(
                    url="url",
                    xml="xml"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__795bb61a773252bae3dfe518ca3d5b70274419b485b5d57f1ce43409a8952902)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument xml", value=xml, expected_type=type_hints["xml"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if url is not None:
                self._values["url"] = url
            if xml is not None:
                self._values["xml"] = xml

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.IdpMetadataProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-idpmetadata.html#cfn-grafana-workspace-idpmetadata-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def xml(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.IdpMetadataProperty.Xml``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-idpmetadata.html#cfn-grafana-workspace-idpmetadata-xml
            '''
            result = self._values.get("xml")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdpMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_grafana.CfnWorkspace.RoleValuesProperty",
        jsii_struct_bases=[],
        name_mapping={"admin": "admin", "editor": "editor"},
    )
    class RoleValuesProperty:
        def __init__(
            self,
            *,
            admin: typing.Optional[typing.Sequence[builtins.str]] = None,
            editor: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param admin: ``CfnWorkspace.RoleValuesProperty.Admin``.
            :param editor: ``CfnWorkspace.RoleValuesProperty.Editor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-rolevalues.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_grafana as grafana
                
                role_values_property = grafana.CfnWorkspace.RoleValuesProperty(
                    admin=["admin"],
                    editor=["editor"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9a8bcd06f64d00222d2b41bf08f31c81d292e457d23272ddb87234eda7f15a0)
                check_type(argname="argument admin", value=admin, expected_type=type_hints["admin"])
                check_type(argname="argument editor", value=editor, expected_type=type_hints["editor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if admin is not None:
                self._values["admin"] = admin
            if editor is not None:
                self._values["editor"] = editor

        @builtins.property
        def admin(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnWorkspace.RoleValuesProperty.Admin``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-rolevalues.html#cfn-grafana-workspace-rolevalues-admin
            '''
            result = self._values.get("admin")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def editor(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnWorkspace.RoleValuesProperty.Editor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-rolevalues.html#cfn-grafana-workspace-rolevalues-editor
            '''
            result = self._values.get("editor")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoleValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_grafana.CfnWorkspace.SamlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "idp_metadata": "idpMetadata",
            "allowed_organizations": "allowedOrganizations",
            "assertion_attributes": "assertionAttributes",
            "login_validity_duration": "loginValidityDuration",
            "role_values": "roleValues",
        },
    )
    class SamlConfigurationProperty:
        def __init__(
            self,
            *,
            idp_metadata: typing.Union[typing.Union["CfnWorkspace.IdpMetadataProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
            allowed_organizations: typing.Optional[typing.Sequence[builtins.str]] = None,
            assertion_attributes: typing.Optional[typing.Union[typing.Union["CfnWorkspace.AssertionAttributesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            login_validity_duration: typing.Optional[jsii.Number] = None,
            role_values: typing.Optional[typing.Union[typing.Union["CfnWorkspace.RoleValuesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param idp_metadata: ``CfnWorkspace.SamlConfigurationProperty.IdpMetadata``.
            :param allowed_organizations: ``CfnWorkspace.SamlConfigurationProperty.AllowedOrganizations``.
            :param assertion_attributes: ``CfnWorkspace.SamlConfigurationProperty.AssertionAttributes``.
            :param login_validity_duration: ``CfnWorkspace.SamlConfigurationProperty.LoginValidityDuration``.
            :param role_values: ``CfnWorkspace.SamlConfigurationProperty.RoleValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_grafana as grafana
                
                saml_configuration_property = grafana.CfnWorkspace.SamlConfigurationProperty(
                    idp_metadata=grafana.CfnWorkspace.IdpMetadataProperty(
                        url="url",
                        xml="xml"
                    ),
                
                    # the properties below are optional
                    allowed_organizations=["allowedOrganizations"],
                    assertion_attributes=grafana.CfnWorkspace.AssertionAttributesProperty(
                        email="email",
                        groups="groups",
                        login="login",
                        name="name",
                        org="org",
                        role="role"
                    ),
                    login_validity_duration=123,
                    role_values=grafana.CfnWorkspace.RoleValuesProperty(
                        admin=["admin"],
                        editor=["editor"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__14277625e97dae304b4384016dde2bbc729157d1053eb0a76e4c512ebf08325d)
                check_type(argname="argument idp_metadata", value=idp_metadata, expected_type=type_hints["idp_metadata"])
                check_type(argname="argument allowed_organizations", value=allowed_organizations, expected_type=type_hints["allowed_organizations"])
                check_type(argname="argument assertion_attributes", value=assertion_attributes, expected_type=type_hints["assertion_attributes"])
                check_type(argname="argument login_validity_duration", value=login_validity_duration, expected_type=type_hints["login_validity_duration"])
                check_type(argname="argument role_values", value=role_values, expected_type=type_hints["role_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "idp_metadata": idp_metadata,
            }
            if allowed_organizations is not None:
                self._values["allowed_organizations"] = allowed_organizations
            if assertion_attributes is not None:
                self._values["assertion_attributes"] = assertion_attributes
            if login_validity_duration is not None:
                self._values["login_validity_duration"] = login_validity_duration
            if role_values is not None:
                self._values["role_values"] = role_values

        @builtins.property
        def idp_metadata(
            self,
        ) -> typing.Union["CfnWorkspace.IdpMetadataProperty", _IResolvable_da3f097b]:
            '''``CfnWorkspace.SamlConfigurationProperty.IdpMetadata``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-idpmetadata
            '''
            result = self._values.get("idp_metadata")
            assert result is not None, "Required property 'idp_metadata' is missing"
            return typing.cast(typing.Union["CfnWorkspace.IdpMetadataProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def allowed_organizations(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnWorkspace.SamlConfigurationProperty.AllowedOrganizations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-allowedorganizations
            '''
            result = self._values.get("allowed_organizations")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def assertion_attributes(
            self,
        ) -> typing.Optional[typing.Union["CfnWorkspace.AssertionAttributesProperty", _IResolvable_da3f097b]]:
            '''``CfnWorkspace.SamlConfigurationProperty.AssertionAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-assertionattributes
            '''
            result = self._values.get("assertion_attributes")
            return typing.cast(typing.Optional[typing.Union["CfnWorkspace.AssertionAttributesProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def login_validity_duration(self) -> typing.Optional[jsii.Number]:
            '''``CfnWorkspace.SamlConfigurationProperty.LoginValidityDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-loginvalidityduration
            '''
            result = self._values.get("login_validity_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def role_values(
            self,
        ) -> typing.Optional[typing.Union["CfnWorkspace.RoleValuesProperty", _IResolvable_da3f097b]]:
            '''``CfnWorkspace.SamlConfigurationProperty.RoleValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-rolevalues
            '''
            result = self._values.get("role_values")
            return typing.cast(typing.Optional[typing.Union["CfnWorkspace.RoleValuesProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_grafana.CfnWorkspaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_access_type": "accountAccessType",
        "authentication_providers": "authenticationProviders",
        "client_token": "clientToken",
        "data_sources": "dataSources",
        "description": "description",
        "name": "name",
        "notification_destinations": "notificationDestinations",
        "organizational_units": "organizationalUnits",
        "organization_role_name": "organizationRoleName",
        "permission_type": "permissionType",
        "role_arn": "roleArn",
        "saml_configuration": "samlConfiguration",
        "stack_set_name": "stackSetName",
    },
)
class CfnWorkspaceProps:
    def __init__(
        self,
        *,
        account_access_type: typing.Optional[builtins.str] = None,
        authentication_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_token: typing.Optional[builtins.str] = None,
        data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notification_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
        organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_role_name: typing.Optional[builtins.str] = None,
        permission_type: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        saml_configuration: typing.Optional[typing.Union[typing.Union[CfnWorkspace.SamlConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        stack_set_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkspace``.

        :param account_access_type: ``AWS::Grafana::Workspace.AccountAccessType``.
        :param authentication_providers: ``AWS::Grafana::Workspace.AuthenticationProviders``.
        :param client_token: ``AWS::Grafana::Workspace.ClientToken``.
        :param data_sources: ``AWS::Grafana::Workspace.DataSources``.
        :param description: ``AWS::Grafana::Workspace.Description``.
        :param name: ``AWS::Grafana::Workspace.Name``.
        :param notification_destinations: ``AWS::Grafana::Workspace.NotificationDestinations``.
        :param organizational_units: ``AWS::Grafana::Workspace.OrganizationalUnits``.
        :param organization_role_name: ``AWS::Grafana::Workspace.OrganizationRoleName``.
        :param permission_type: ``AWS::Grafana::Workspace.PermissionType``.
        :param role_arn: ``AWS::Grafana::Workspace.RoleArn``.
        :param saml_configuration: ``AWS::Grafana::Workspace.SamlConfiguration``.
        :param stack_set_name: ``AWS::Grafana::Workspace.StackSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_grafana as grafana
            
            cfn_workspace_props = grafana.CfnWorkspaceProps(
                account_access_type="accountAccessType",
                authentication_providers=["authenticationProviders"],
                client_token="clientToken",
                data_sources=["dataSources"],
                description="description",
                name="name",
                notification_destinations=["notificationDestinations"],
                organizational_units=["organizationalUnits"],
                organization_role_name="organizationRoleName",
                permission_type="permissionType",
                role_arn="roleArn",
                saml_configuration=grafana.CfnWorkspace.SamlConfigurationProperty(
                    idp_metadata=grafana.CfnWorkspace.IdpMetadataProperty(
                        url="url",
                        xml="xml"
                    ),
            
                    # the properties below are optional
                    allowed_organizations=["allowedOrganizations"],
                    assertion_attributes=grafana.CfnWorkspace.AssertionAttributesProperty(
                        email="email",
                        groups="groups",
                        login="login",
                        name="name",
                        org="org",
                        role="role"
                    ),
                    login_validity_duration=123,
                    role_values=grafana.CfnWorkspace.RoleValuesProperty(
                        admin=["admin"],
                        editor=["editor"]
                    )
                ),
                stack_set_name="stackSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b0ac807ec7944eb7226ae6fc02b338bc05594b2b8737ec34bf5dbdefd42280)
            check_type(argname="argument account_access_type", value=account_access_type, expected_type=type_hints["account_access_type"])
            check_type(argname="argument authentication_providers", value=authentication_providers, expected_type=type_hints["authentication_providers"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument data_sources", value=data_sources, expected_type=type_hints["data_sources"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notification_destinations", value=notification_destinations, expected_type=type_hints["notification_destinations"])
            check_type(argname="argument organizational_units", value=organizational_units, expected_type=type_hints["organizational_units"])
            check_type(argname="argument organization_role_name", value=organization_role_name, expected_type=type_hints["organization_role_name"])
            check_type(argname="argument permission_type", value=permission_type, expected_type=type_hints["permission_type"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument saml_configuration", value=saml_configuration, expected_type=type_hints["saml_configuration"])
            check_type(argname="argument stack_set_name", value=stack_set_name, expected_type=type_hints["stack_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_access_type is not None:
            self._values["account_access_type"] = account_access_type
        if authentication_providers is not None:
            self._values["authentication_providers"] = authentication_providers
        if client_token is not None:
            self._values["client_token"] = client_token
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if notification_destinations is not None:
            self._values["notification_destinations"] = notification_destinations
        if organizational_units is not None:
            self._values["organizational_units"] = organizational_units
        if organization_role_name is not None:
            self._values["organization_role_name"] = organization_role_name
        if permission_type is not None:
            self._values["permission_type"] = permission_type
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if saml_configuration is not None:
            self._values["saml_configuration"] = saml_configuration
        if stack_set_name is not None:
            self._values["stack_set_name"] = stack_set_name

    @builtins.property
    def account_access_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.AccountAccessType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-accountaccesstype
        '''
        result = self._values.get("account_access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication_providers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Grafana::Workspace.AuthenticationProviders``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-authenticationproviders
        '''
        result = self._values.get("authentication_providers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.ClientToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_sources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Grafana::Workspace.DataSources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-datasources
        '''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_destinations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Grafana::Workspace.NotificationDestinations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-notificationdestinations
        '''
        result = self._values.get("notification_destinations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organizational_units(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Grafana::Workspace.OrganizationalUnits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-organizationalunits
        '''
        result = self._values.get("organizational_units")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organization_role_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.OrganizationRoleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-organizationrolename
        '''
        result = self._values.get("organization_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permission_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.PermissionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-permissiontype
        '''
        result = self._values.get("permission_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnWorkspace.SamlConfigurationProperty, _IResolvable_da3f097b]]:
        '''``AWS::Grafana::Workspace.SamlConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-samlconfiguration
        '''
        result = self._values.get("saml_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnWorkspace.SamlConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def stack_set_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Grafana::Workspace.StackSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-stacksetname
        '''
        result = self._values.get("stack_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnWorkspace",
    "CfnWorkspaceProps",
]

publication.publish()

def _typecheckingstub__972564e8260607f3980c99a1e9aecab41a9a45a486b896a29b3870ef3024c82d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_access_type: typing.Optional[builtins.str] = None,
    authentication_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
    client_token: typing.Optional[builtins.str] = None,
    data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notification_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
    organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_role_name: typing.Optional[builtins.str] = None,
    permission_type: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    saml_configuration: typing.Optional[typing.Union[typing.Union[CfnWorkspace.SamlConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    stack_set_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d1ddbb2c282ef63cbb246c4096b7de3713eca2c5e898a4fb0399bceaaea80a2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e08c8dd7b33829bf4264a10897017350edb485216cf0320b30df6a4971d42cb2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4788a164346232bc27f2ed87a4f889be94efaa385debfe7555b9c38ef7b43c82(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d659e2c8f9a80dbb1ff10a5d496ecce9ddb784e34300fef292b95604867dd120(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e7c7d4ab889d7976d4a0296a9cbd591db1c64ed24ef025e255a240848da349(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3dfcb10305df8d464fbbcb5e8fd3d5b6da64568993c8b2c51b8dcd3395b6ac9(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8893d9a8b4f97f5af788c15dca1db97953d288f193df1c206ed4015e08c9c2d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3054f2932686c0aea4252a167d3c57cd2cac6f217af055688e0e4ad5956bce3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b512e7c00943f52045050d8d881411bf80d8753e7e5db4cfa04be2d23c840a5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab5eb86d4408bb6fa769c29f35ddd196f30186a96e904ce407fa53d08a69a42(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0bc3f30f5cd3553fef63aadcf02d8cd56cd0a20cd147f34b2b500608b2dba8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2912f1e45e2bf3ca7cdbd6783ea28e244af545c2648fd8b9c918da6bdfb2a69e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edafda7b927ef527400465d2e8fb7713cb6a76ed45cd51372ae245440c1f42ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__512287bf24818cb838cc5045af81a100afbe0fdcf464601403fff719622ccc4d(
    value: typing.Optional[typing.Union[CfnWorkspace.SamlConfigurationProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61ab7cafff5a486f361d533b95f12ec0ab7499ff5e38660d0dcabb7a049a78e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__426a4b6fbcb381e0187dcb5da594244c44b4957c28015e552b55102d8f9d90bb(
    *,
    email: typing.Optional[builtins.str] = None,
    groups: typing.Optional[builtins.str] = None,
    login: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    org: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795bb61a773252bae3dfe518ca3d5b70274419b485b5d57f1ce43409a8952902(
    *,
    url: typing.Optional[builtins.str] = None,
    xml: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a8bcd06f64d00222d2b41bf08f31c81d292e457d23272ddb87234eda7f15a0(
    *,
    admin: typing.Optional[typing.Sequence[builtins.str]] = None,
    editor: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14277625e97dae304b4384016dde2bbc729157d1053eb0a76e4c512ebf08325d(
    *,
    idp_metadata: typing.Union[typing.Union[CfnWorkspace.IdpMetadataProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    allowed_organizations: typing.Optional[typing.Sequence[builtins.str]] = None,
    assertion_attributes: typing.Optional[typing.Union[typing.Union[CfnWorkspace.AssertionAttributesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    login_validity_duration: typing.Optional[jsii.Number] = None,
    role_values: typing.Optional[typing.Union[typing.Union[CfnWorkspace.RoleValuesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58b0ac807ec7944eb7226ae6fc02b338bc05594b2b8737ec34bf5dbdefd42280(
    *,
    account_access_type: typing.Optional[builtins.str] = None,
    authentication_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
    client_token: typing.Optional[builtins.str] = None,
    data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notification_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
    organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_role_name: typing.Optional[builtins.str] = None,
    permission_type: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    saml_configuration: typing.Optional[typing.Union[typing.Union[CfnWorkspace.SamlConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    stack_set_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
