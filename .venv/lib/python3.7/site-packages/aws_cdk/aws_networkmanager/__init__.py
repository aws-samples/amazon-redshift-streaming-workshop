'''
# AWS::NetworkManager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_networkmanager as networkmanager
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NetworkManager construct libraries](https://constructs.dev/search?q=networkmanager)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NetworkManager resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkManager.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NetworkManager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkManager.html).

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
class CfnConnectAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectAttachment",
):
    '''A CloudFormation ``AWS::NetworkManager::ConnectAttachment``.

    Creates a core network Connect attachment from a specified core network attachment.

    A core network Connect attachment is a GRE-based tunnel attachment that you can use to establish a connection between a core network and an appliance. A core network Connect attachment uses an existing VPC attachment as the underlying transport mechanism.

    :cloudformationResource: AWS::NetworkManager::ConnectAttachment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_connect_attachment = networkmanager.CfnConnectAttachment(self, "MyCfnConnectAttachment",
            core_network_id="coreNetworkId",
            edge_location="edgeLocation",
            options=networkmanager.CfnConnectAttachment.ConnectAttachmentOptionsProperty(
                protocol="protocol"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            transport_attachment_id="transportAttachmentId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        core_network_id: typing.Optional[builtins.str] = None,
        edge_location: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[typing.Union["CfnConnectAttachment.ConnectAttachmentOptionsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        transport_attachment_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::ConnectAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param core_network_id: The core network ID.
        :param edge_location: The Region where the edge is located.
        :param options: Options for creating a Connect attachment.
        :param tags: The tags associated with the Connect attachment.
        :param transport_attachment_id: The ID of the attachment between the two connections.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnectAttachment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectAttachmentProps(
            core_network_id=core_network_id,
            edge_location=edge_location,
            options=options,
            tags=tags,
            transport_attachment_id=transport_attachment_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnectAttachment.inspect)
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
            type_hints = typing.get_type_hints(CfnConnectAttachment._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentId")
    def attr_attachment_id(self) -> builtins.str:
        '''The ID of the Connect attachment.

        :cloudformationAttribute: AttachmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentPolicyRuleNumber")
    def attr_attachment_policy_rule_number(self) -> jsii.Number:
        '''The rule number associated with the attachment.

        :cloudformationAttribute: AttachmentPolicyRuleNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAttachmentPolicyRuleNumber"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentType")
    def attr_attachment_type(self) -> builtins.str:
        '''The type of attachment.

        This will be ``CONNECT`` .

        :cloudformationAttribute: AttachmentType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the Connect attachment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The ID of the Connect attachment owner.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The resource ARN for the Connect attachment.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSegmentName")
    def attr_segment_name(self) -> builtins.str:
        '''The name of the Connect attachment's segment.

        :cloudformationAttribute: SegmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the Connect attachment.

        This can be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the Connect attachment was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags associated with the Connect attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="coreNetworkId")
    def core_network_id(self) -> typing.Optional[builtins.str]:
        '''The core network ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-corenetworkid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreNetworkId"))

    @core_network_id.setter
    def core_network_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectAttachment, "core_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="edgeLocation")
    def edge_location(self) -> typing.Optional[builtins.str]:
        '''The Region where the edge is located.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-edgelocation
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeLocation"))

    @edge_location.setter
    def edge_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectAttachment, "edge_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeLocation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="options")
    def options(
        self,
    ) -> typing.Optional[typing.Union["CfnConnectAttachment.ConnectAttachmentOptionsProperty", _IResolvable_da3f097b]]:
        '''Options for creating a Connect attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-options
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConnectAttachment.ConnectAttachmentOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "options"))

    @options.setter
    def options(
        self,
        value: typing.Optional[typing.Union["CfnConnectAttachment.ConnectAttachmentOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectAttachment, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transportAttachmentId")
    def transport_attachment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the attachment between the two connections.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-transportattachmentid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transportAttachmentId"))

    @transport_attachment_id.setter
    def transport_attachment_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectAttachment, "transport_attachment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transportAttachmentId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectAttachment.ConnectAttachmentOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"protocol": "protocol"},
    )
    class ConnectAttachmentOptionsProperty:
        def __init__(self, *, protocol: typing.Optional[builtins.str] = None) -> None:
            '''Describes a core network Connect attachment options.

            :param protocol: The protocol used for the attachment connection.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                connect_attachment_options_property = networkmanager.CfnConnectAttachment.ConnectAttachmentOptionsProperty(
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnectAttachment.ConnectAttachmentOptionsProperty.__init__)
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[str, typing.Any] = {}
            if protocol is not None:
                self._values["protocol"] = protocol

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The protocol used for the attachment connection.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html#cfn-networkmanager-connectattachment-connectattachmentoptions-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectAttachmentOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_id": "coreNetworkId",
        "edge_location": "edgeLocation",
        "options": "options",
        "tags": "tags",
        "transport_attachment_id": "transportAttachmentId",
    },
)
class CfnConnectAttachmentProps:
    def __init__(
        self,
        *,
        core_network_id: typing.Optional[builtins.str] = None,
        edge_location: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[typing.Union[CfnConnectAttachment.ConnectAttachmentOptionsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        transport_attachment_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnectAttachment``.

        :param core_network_id: The core network ID.
        :param edge_location: The Region where the edge is located.
        :param options: Options for creating a Connect attachment.
        :param tags: The tags associated with the Connect attachment.
        :param transport_attachment_id: The ID of the attachment between the two connections.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_connect_attachment_props = networkmanager.CfnConnectAttachmentProps(
                core_network_id="coreNetworkId",
                edge_location="edgeLocation",
                options=networkmanager.CfnConnectAttachment.ConnectAttachmentOptionsProperty(
                    protocol="protocol"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                transport_attachment_id="transportAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnectAttachmentProps.__init__)
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
            check_type(argname="argument edge_location", value=edge_location, expected_type=type_hints["edge_location"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transport_attachment_id", value=transport_attachment_id, expected_type=type_hints["transport_attachment_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if core_network_id is not None:
            self._values["core_network_id"] = core_network_id
        if edge_location is not None:
            self._values["edge_location"] = edge_location
        if options is not None:
            self._values["options"] = options
        if tags is not None:
            self._values["tags"] = tags
        if transport_attachment_id is not None:
            self._values["transport_attachment_id"] = transport_attachment_id

    @builtins.property
    def core_network_id(self) -> typing.Optional[builtins.str]:
        '''The core network ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-corenetworkid
        '''
        result = self._values.get("core_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edge_location(self) -> typing.Optional[builtins.str]:
        '''The Region where the edge is located.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-edgelocation
        '''
        result = self._values.get("edge_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional[typing.Union[CfnConnectAttachment.ConnectAttachmentOptionsProperty, _IResolvable_da3f097b]]:
        '''Options for creating a Connect attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-options
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Union[CfnConnectAttachment.ConnectAttachmentOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the Connect attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def transport_attachment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the attachment between the two connections.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-transportattachmentid
        '''
        result = self._values.get("transport_attachment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConnectPeer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectPeer",
):
    '''A CloudFormation ``AWS::NetworkManager::ConnectPeer``.

    Creates a core network Connect peer for a specified core network connect attachment between a core network and an appliance. The peer address and transit gateway address must be the same IP address family (IPv4 or IPv6).

    :cloudformationResource: AWS::NetworkManager::ConnectPeer
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_connect_peer = networkmanager.CfnConnectPeer(self, "MyCfnConnectPeer",
            bgp_options=networkmanager.CfnConnectPeer.BgpOptionsProperty(
                peer_asn=123
            ),
            connect_attachment_id="connectAttachmentId",
            core_network_address="coreNetworkAddress",
            inside_cidr_blocks=["insideCidrBlocks"],
            peer_address="peerAddress",
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
        bgp_options: typing.Optional[typing.Union[typing.Union["CfnConnectPeer.BgpOptionsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        connect_attachment_id: typing.Optional[builtins.str] = None,
        core_network_address: typing.Optional[builtins.str] = None,
        inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        peer_address: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::ConnectPeer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bgp_options: The BGP peer options.
        :param connect_attachment_id: The ID of Connect peer.
        :param core_network_address: The IP address of a core network.
        :param inside_cidr_blocks: The inside IP addresses used for a Connect peer configuration.
        :param peer_address: The IP address of the Connect peer.
        :param tags: The tags associated with the Connect peer.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnectPeer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectPeerProps(
            bgp_options=bgp_options,
            connect_attachment_id=connect_attachment_id,
            core_network_address=core_network_address,
            inside_cidr_blocks=inside_cidr_blocks,
            peer_address=peer_address,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnectPeer.inspect)
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
            type_hints = typing.get_type_hints(CfnConnectPeer._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrConnectPeerId")
    def attr_connect_peer_id(self) -> builtins.str:
        '''The ID of the Connect peer.

        :cloudformationAttribute: ConnectPeerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectPeerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCoreNetworkId")
    def attr_core_network_id(self) -> builtins.str:
        '''The core network ID.

        :cloudformationAttribute: CoreNetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the Connect peer was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEdgeLocation")
    def attr_edge_location(self) -> builtins.str:
        '''The Region where the edge is located.

        :cloudformationAttribute: EdgeLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEdgeLocation"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the Connect peer.

        This will be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags associated with the Connect peer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bgpOptions")
    def bgp_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConnectPeer.BgpOptionsProperty", _IResolvable_da3f097b]]:
        '''The BGP peer options.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-bgpoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConnectPeer.BgpOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "bgpOptions"))

    @bgp_options.setter
    def bgp_options(
        self,
        value: typing.Optional[typing.Union["CfnConnectPeer.BgpOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectPeer, "bgp_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectAttachmentId")
    def connect_attachment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of Connect peer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-connectattachmentid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectAttachmentId"))

    @connect_attachment_id.setter
    def connect_attachment_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectPeer, "connect_attachment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectAttachmentId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="coreNetworkAddress")
    def core_network_address(self) -> typing.Optional[builtins.str]:
        '''The IP address of a core network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-corenetworkaddress
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreNetworkAddress"))

    @core_network_address.setter
    def core_network_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectPeer, "core_network_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkAddress", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The inside IP addresses used for a Connect peer configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-insidecidrblocks
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "insideCidrBlocks"))

    @inside_cidr_blocks.setter
    def inside_cidr_blocks(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectPeer, "inside_cidr_blocks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insideCidrBlocks", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="peerAddress")
    def peer_address(self) -> typing.Optional[builtins.str]:
        '''The IP address of the Connect peer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-peeraddress
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerAddress"))

    @peer_address.setter
    def peer_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConnectPeer, "peer_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerAddress", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectPeer.BgpOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"peer_asn": "peerAsn"},
    )
    class BgpOptionsProperty:
        def __init__(self, *, peer_asn: typing.Optional[jsii.Number] = None) -> None:
            '''Describes the BGP options.

            :param peer_asn: The Peer ASN of the BGP.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                bgp_options_property = networkmanager.CfnConnectPeer.BgpOptionsProperty(
                    peer_asn=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConnectPeer.BgpOptionsProperty.__init__)
                check_type(argname="argument peer_asn", value=peer_asn, expected_type=type_hints["peer_asn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if peer_asn is not None:
                self._values["peer_asn"] = peer_asn

        @builtins.property
        def peer_asn(self) -> typing.Optional[jsii.Number]:
            '''The Peer ASN of the BGP.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html#cfn-networkmanager-connectpeer-bgpoptions-peerasn
            '''
            result = self._values.get("peer_asn")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BgpOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectPeerProps",
    jsii_struct_bases=[],
    name_mapping={
        "bgp_options": "bgpOptions",
        "connect_attachment_id": "connectAttachmentId",
        "core_network_address": "coreNetworkAddress",
        "inside_cidr_blocks": "insideCidrBlocks",
        "peer_address": "peerAddress",
        "tags": "tags",
    },
)
class CfnConnectPeerProps:
    def __init__(
        self,
        *,
        bgp_options: typing.Optional[typing.Union[typing.Union[CfnConnectPeer.BgpOptionsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        connect_attachment_id: typing.Optional[builtins.str] = None,
        core_network_address: typing.Optional[builtins.str] = None,
        inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        peer_address: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnectPeer``.

        :param bgp_options: The BGP peer options.
        :param connect_attachment_id: The ID of Connect peer.
        :param core_network_address: The IP address of a core network.
        :param inside_cidr_blocks: The inside IP addresses used for a Connect peer configuration.
        :param peer_address: The IP address of the Connect peer.
        :param tags: The tags associated with the Connect peer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_connect_peer_props = networkmanager.CfnConnectPeerProps(
                bgp_options=networkmanager.CfnConnectPeer.BgpOptionsProperty(
                    peer_asn=123
                ),
                connect_attachment_id="connectAttachmentId",
                core_network_address="coreNetworkAddress",
                inside_cidr_blocks=["insideCidrBlocks"],
                peer_address="peerAddress",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConnectPeerProps.__init__)
            check_type(argname="argument bgp_options", value=bgp_options, expected_type=type_hints["bgp_options"])
            check_type(argname="argument connect_attachment_id", value=connect_attachment_id, expected_type=type_hints["connect_attachment_id"])
            check_type(argname="argument core_network_address", value=core_network_address, expected_type=type_hints["core_network_address"])
            check_type(argname="argument inside_cidr_blocks", value=inside_cidr_blocks, expected_type=type_hints["inside_cidr_blocks"])
            check_type(argname="argument peer_address", value=peer_address, expected_type=type_hints["peer_address"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bgp_options is not None:
            self._values["bgp_options"] = bgp_options
        if connect_attachment_id is not None:
            self._values["connect_attachment_id"] = connect_attachment_id
        if core_network_address is not None:
            self._values["core_network_address"] = core_network_address
        if inside_cidr_blocks is not None:
            self._values["inside_cidr_blocks"] = inside_cidr_blocks
        if peer_address is not None:
            self._values["peer_address"] = peer_address
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bgp_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConnectPeer.BgpOptionsProperty, _IResolvable_da3f097b]]:
        '''The BGP peer options.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-bgpoptions
        '''
        result = self._values.get("bgp_options")
        return typing.cast(typing.Optional[typing.Union[CfnConnectPeer.BgpOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def connect_attachment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of Connect peer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-connectattachmentid
        '''
        result = self._values.get("connect_attachment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_network_address(self) -> typing.Optional[builtins.str]:
        '''The IP address of a core network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-corenetworkaddress
        '''
        result = self._values.get("core_network_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inside_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The inside IP addresses used for a Connect peer configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-insidecidrblocks
        '''
        result = self._values.get("inside_cidr_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def peer_address(self) -> typing.Optional[builtins.str]:
        '''The IP address of the Connect peer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-peeraddress
        '''
        result = self._values.get("peer_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the Connect peer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectPeerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCoreNetwork(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnCoreNetwork",
):
    '''A CloudFormation ``AWS::NetworkManager::CoreNetwork``.

    Describes a core network within a global network.

    :cloudformationResource: AWS::NetworkManager::CoreNetwork
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        # policy_document: Any
        
        cfn_core_network = networkmanager.CfnCoreNetwork(self, "MyCfnCoreNetwork",
            global_network_id="globalNetworkId",
        
            # the properties below are optional
            description="description",
            policy_document=policy_document,
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
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        policy_document: typing.Any = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::CoreNetwork``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param global_network_id: The ID of the global network that your core network is a part of.
        :param description: The description of a core network.
        :param policy_document: Describes a core network policy. If you update the policy document, CloudFormation will apply the core network change set generated from the updated policy document, and then set it as the LIVE policy.
        :param tags: The tags associated with a core network.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCoreNetwork.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCoreNetworkProps(
            global_network_id=global_network_id,
            description=description,
            policy_document=policy_document,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCoreNetwork.inspect)
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
            type_hints = typing.get_type_hints(CfnCoreNetwork._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCoreNetworkId")
    def attr_core_network_id(self) -> builtins.str:
        '''The core network ID.

        :cloudformationAttribute: CoreNetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the core network was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEdges")
    def attr_edges(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Edges
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEdges"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOwnerAccount")
    def attr_owner_account(self) -> builtins.str:
        '''
        :cloudformationAttribute: OwnerAccount
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSegments")
    def attr_segments(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Segments
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrSegments"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The current state of the core network.

        These states are: ``CREATING`` | ``UPDATING`` | ``AVAILABLE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags associated with a core network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network that your core network is a part of.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCoreNetwork, "global_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''Describes a core network policy.

        If you update the policy document, CloudFormation will apply the core network change set generated from the updated policy document, and then set it as the LIVE policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-policydocument
        '''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCoreNetwork, "policy_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a core network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCoreNetwork, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnCoreNetwork.CoreNetworkEdgeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "asn": "asn",
            "edge_location": "edgeLocation",
            "inside_cidr_blocks": "insideCidrBlocks",
        },
    )
    class CoreNetworkEdgeProperty:
        def __init__(
            self,
            *,
            asn: typing.Optional[jsii.Number] = None,
            edge_location: typing.Optional[builtins.str] = None,
            inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes a core network edge.

            :param asn: The ASN of a core network edge.
            :param edge_location: The Region where a core network edge is located.
            :param inside_cidr_blocks: The inside IP addresses used for core network edges.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                core_network_edge_property = networkmanager.CfnCoreNetwork.CoreNetworkEdgeProperty(
                    asn=123,
                    edge_location="edgeLocation",
                    inside_cidr_blocks=["insideCidrBlocks"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCoreNetwork.CoreNetworkEdgeProperty.__init__)
                check_type(argname="argument asn", value=asn, expected_type=type_hints["asn"])
                check_type(argname="argument edge_location", value=edge_location, expected_type=type_hints["edge_location"])
                check_type(argname="argument inside_cidr_blocks", value=inside_cidr_blocks, expected_type=type_hints["inside_cidr_blocks"])
            self._values: typing.Dict[str, typing.Any] = {}
            if asn is not None:
                self._values["asn"] = asn
            if edge_location is not None:
                self._values["edge_location"] = edge_location
            if inside_cidr_blocks is not None:
                self._values["inside_cidr_blocks"] = inside_cidr_blocks

        @builtins.property
        def asn(self) -> typing.Optional[jsii.Number]:
            '''The ASN of a core network edge.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-asn
            '''
            result = self._values.get("asn")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def edge_location(self) -> typing.Optional[builtins.str]:
            '''The Region where a core network edge is located.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-edgelocation
            '''
            result = self._values.get("edge_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inside_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The inside IP addresses used for core network edges.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-insidecidrblocks
            '''
            result = self._values.get("inside_cidr_blocks")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoreNetworkEdgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnCoreNetwork.CoreNetworkSegmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "edge_locations": "edgeLocations",
            "name": "name",
            "shared_segments": "sharedSegments",
        },
    )
    class CoreNetworkSegmentProperty:
        def __init__(
            self,
            *,
            edge_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
            name: typing.Optional[builtins.str] = None,
            shared_segments: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes a core network segment, which are dedicated routes.

            Only attachments within this segment can communicate with each other.

            :param edge_locations: The Regions where the edges are located.
            :param name: The name of a core network segment.
            :param shared_segments: The shared segments of a core network.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                core_network_segment_property = networkmanager.CfnCoreNetwork.CoreNetworkSegmentProperty(
                    edge_locations=["edgeLocations"],
                    name="name",
                    shared_segments=["sharedSegments"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCoreNetwork.CoreNetworkSegmentProperty.__init__)
                check_type(argname="argument edge_locations", value=edge_locations, expected_type=type_hints["edge_locations"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument shared_segments", value=shared_segments, expected_type=type_hints["shared_segments"])
            self._values: typing.Dict[str, typing.Any] = {}
            if edge_locations is not None:
                self._values["edge_locations"] = edge_locations
            if name is not None:
                self._values["name"] = name
            if shared_segments is not None:
                self._values["shared_segments"] = shared_segments

        @builtins.property
        def edge_locations(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Regions where the edges are located.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-edgelocations
            '''
            result = self._values.get("edge_locations")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of a core network segment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shared_segments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The shared segments of a core network.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-sharedsegments
            '''
            result = self._values.get("shared_segments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoreNetworkSegmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnCoreNetworkProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "description": "description",
        "policy_document": "policyDocument",
        "tags": "tags",
    },
)
class CfnCoreNetworkProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        policy_document: typing.Any = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCoreNetwork``.

        :param global_network_id: The ID of the global network that your core network is a part of.
        :param description: The description of a core network.
        :param policy_document: Describes a core network policy. If you update the policy document, CloudFormation will apply the core network change set generated from the updated policy document, and then set it as the LIVE policy.
        :param tags: The tags associated with a core network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            # policy_document: Any
            
            cfn_core_network_props = networkmanager.CfnCoreNetworkProps(
                global_network_id="globalNetworkId",
            
                # the properties below are optional
                description="description",
                policy_document=policy_document,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCoreNetworkProps.__init__)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "global_network_id": global_network_id,
        }
        if description is not None:
            self._values["description"] = description
        if policy_document is not None:
            self._values["policy_document"] = policy_document
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network that your core network is a part of.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a core network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''Describes a core network policy.

        If you update the policy document, CloudFormation will apply the core network change set generated from the updated policy document, and then set it as the LIVE policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-policydocument
        '''
        result = self._values.get("policy_document")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with a core network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCustomerGatewayAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnCustomerGatewayAssociation",
):
    '''A CloudFormation ``AWS::NetworkManager::CustomerGatewayAssociation``.

    Specifies an association between a customer gateway, a device, and optionally, a link. If you specify a link, it must be associated with the specified device. The customer gateway must be connected to a VPN attachment on a transit gateway that's registered in your global network.

    You cannot associate a customer gateway with more than one device and link.

    :cloudformationResource: AWS::NetworkManager::CustomerGatewayAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_customer_gateway_association = networkmanager.CfnCustomerGatewayAssociation(self, "MyCfnCustomerGatewayAssociation",
            customer_gateway_arn="customerGatewayArn",
            device_id="deviceId",
            global_network_id="globalNetworkId",
        
            # the properties below are optional
            link_id="linkId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        customer_gateway_arn: builtins.str,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::CustomerGatewayAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param customer_gateway_arn: The Amazon Resource Name (ARN) of the customer gateway.
        :param device_id: The ID of the device.
        :param global_network_id: The ID of the global network.
        :param link_id: The ID of the link.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCustomerGatewayAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomerGatewayAssociationProps(
            customer_gateway_arn=customer_gateway_arn,
            device_id=device_id,
            global_network_id=global_network_id,
            link_id=link_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCustomerGatewayAssociation.inspect)
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
            type_hints = typing.get_type_hints(CfnCustomerGatewayAssociation._render_properties)
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
    @jsii.member(jsii_name="customerGatewayArn")
    def customer_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the customer gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-customergatewayarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "customerGatewayArn"))

    @customer_gateway_arn.setter
    def customer_gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomerGatewayAssociation, "customer_gateway_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerGatewayArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deviceId")
    def device_id(self) -> builtins.str:
        '''The ID of the device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-deviceid
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceId"))

    @device_id.setter
    def device_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomerGatewayAssociation, "device_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomerGatewayAssociation, "global_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="linkId")
    def link_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-linkid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkId"))

    @link_id.setter
    def link_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomerGatewayAssociation, "link_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnCustomerGatewayAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "customer_gateway_arn": "customerGatewayArn",
        "device_id": "deviceId",
        "global_network_id": "globalNetworkId",
        "link_id": "linkId",
    },
)
class CfnCustomerGatewayAssociationProps:
    def __init__(
        self,
        *,
        customer_gateway_arn: builtins.str,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomerGatewayAssociation``.

        :param customer_gateway_arn: The Amazon Resource Name (ARN) of the customer gateway.
        :param device_id: The ID of the device.
        :param global_network_id: The ID of the global network.
        :param link_id: The ID of the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_customer_gateway_association_props = networkmanager.CfnCustomerGatewayAssociationProps(
                customer_gateway_arn="customerGatewayArn",
                device_id="deviceId",
                global_network_id="globalNetworkId",
            
                # the properties below are optional
                link_id="linkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCustomerGatewayAssociationProps.__init__)
            check_type(argname="argument customer_gateway_arn", value=customer_gateway_arn, expected_type=type_hints["customer_gateway_arn"])
            check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument link_id", value=link_id, expected_type=type_hints["link_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "customer_gateway_arn": customer_gateway_arn,
            "device_id": device_id,
            "global_network_id": global_network_id,
        }
        if link_id is not None:
            self._values["link_id"] = link_id

    @builtins.property
    def customer_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the customer gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-customergatewayarn
        '''
        result = self._values.get("customer_gateway_arn")
        assert result is not None, "Required property 'customer_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device_id(self) -> builtins.str:
        '''The ID of the device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-deviceid
        '''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-linkid
        '''
        result = self._values.get("link_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomerGatewayAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDevice(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnDevice",
):
    '''A CloudFormation ``AWS::NetworkManager::Device``.

    Specifies a device.

    :cloudformationResource: AWS::NetworkManager::Device
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_device = networkmanager.CfnDevice(self, "MyCfnDevice",
            global_network_id="globalNetworkId",
        
            # the properties below are optional
            description="description",
            location=networkmanager.CfnDevice.LocationProperty(
                address="address",
                latitude="latitude",
                longitude="longitude"
            ),
            model="model",
            serial_number="serialNumber",
            site_id="siteId",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type",
            vendor="vendor"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[typing.Union["CfnDevice.LocationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        model: typing.Optional[builtins.str] = None,
        serial_number: typing.Optional[builtins.str] = None,
        site_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        type: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::Device``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param global_network_id: The ID of the global network.
        :param description: A description of the device. Constraints: Maximum length of 256 characters.
        :param location: The site location.
        :param model: The model of the device. Constraints: Maximum length of 128 characters.
        :param serial_number: The serial number of the device. Constraints: Maximum length of 128 characters.
        :param site_id: The site ID.
        :param tags: The tags for the device.
        :param type: The device type.
        :param vendor: The vendor of the device. Constraints: Maximum length of 128 characters.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDevice.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeviceProps(
            global_network_id=global_network_id,
            description=description,
            location=location,
            model=model,
            serial_number=serial_number,
            site_id=site_id,
            tags=tags,
            type=type,
            vendor=vendor,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDevice.inspect)
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
            type_hints = typing.get_type_hints(CfnDevice._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDeviceArn")
    def attr_device_arn(self) -> builtins.str:
        '''The ARN of the device.

        For example, ``arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123`` .

        :cloudformationAttribute: DeviceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeviceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDeviceId")
    def attr_device_id(self) -> builtins.str:
        '''The ID of the device.

        For example, ``device-07f6fd08867abc123`` .

        :cloudformationAttribute: DeviceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeviceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags for the device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDevice, "global_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the device.

        Constraints: Maximum length of 256 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDevice, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union["CfnDevice.LocationProperty", _IResolvable_da3f097b]]:
        '''The site location.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-location
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDevice.LocationProperty", _IResolvable_da3f097b]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union["CfnDevice.LocationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDevice, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="model")
    def model(self) -> typing.Optional[builtins.str]:
        '''The model of the device.

        Constraints: Maximum length of 128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-model
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "model"))

    @model.setter
    def model(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDevice, "model").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "model", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> typing.Optional[builtins.str]:
        '''The serial number of the device.

        Constraints: Maximum length of 128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-serialnumber
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serialNumber"))

    @serial_number.setter
    def serial_number(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDevice, "serial_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serialNumber", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="siteId")
    def site_id(self) -> typing.Optional[builtins.str]:
        '''The site ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-siteid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "siteId"))

    @site_id.setter
    def site_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDevice, "site_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The device type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDevice, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> typing.Optional[builtins.str]:
        '''The vendor of the device.

        Constraints: Maximum length of 128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-vendor
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDevice, "vendor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendor", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnDevice.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "latitude": "latitude",
            "longitude": "longitude",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            latitude: typing.Optional[builtins.str] = None,
            longitude: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a location.

            :param address: The physical address.
            :param latitude: The latitude.
            :param longitude: The longitude.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                location_property = networkmanager.CfnDevice.LocationProperty(
                    address="address",
                    latitude="latitude",
                    longitude="longitude"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDevice.LocationProperty.__init__)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
                check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            self._values: typing.Dict[str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if latitude is not None:
                self._values["latitude"] = latitude
            if longitude is not None:
                self._values["longitude"] = longitude

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The physical address.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def latitude(self) -> typing.Optional[builtins.str]:
            '''The latitude.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-latitude
            '''
            result = self._values.get("latitude")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def longitude(self) -> typing.Optional[builtins.str]:
            '''The longitude.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-longitude
            '''
            result = self._values.get("longitude")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "description": "description",
        "location": "location",
        "model": "model",
        "serial_number": "serialNumber",
        "site_id": "siteId",
        "tags": "tags",
        "type": "type",
        "vendor": "vendor",
    },
)
class CfnDeviceProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[typing.Union[CfnDevice.LocationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        model: typing.Optional[builtins.str] = None,
        serial_number: typing.Optional[builtins.str] = None,
        site_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        type: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDevice``.

        :param global_network_id: The ID of the global network.
        :param description: A description of the device. Constraints: Maximum length of 256 characters.
        :param location: The site location.
        :param model: The model of the device. Constraints: Maximum length of 128 characters.
        :param serial_number: The serial number of the device. Constraints: Maximum length of 128 characters.
        :param site_id: The site ID.
        :param tags: The tags for the device.
        :param type: The device type.
        :param vendor: The vendor of the device. Constraints: Maximum length of 128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_device_props = networkmanager.CfnDeviceProps(
                global_network_id="globalNetworkId",
            
                # the properties below are optional
                description="description",
                location=networkmanager.CfnDevice.LocationProperty(
                    address="address",
                    latitude="latitude",
                    longitude="longitude"
                ),
                model="model",
                serial_number="serialNumber",
                site_id="siteId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type",
                vendor="vendor"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDeviceProps.__init__)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument model", value=model, expected_type=type_hints["model"])
            check_type(argname="argument serial_number", value=serial_number, expected_type=type_hints["serial_number"])
            check_type(argname="argument site_id", value=site_id, expected_type=type_hints["site_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument vendor", value=vendor, expected_type=type_hints["vendor"])
        self._values: typing.Dict[str, typing.Any] = {
            "global_network_id": global_network_id,
        }
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if model is not None:
            self._values["model"] = model
        if serial_number is not None:
            self._values["serial_number"] = serial_number
        if site_id is not None:
            self._values["site_id"] = site_id
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the device.

        Constraints: Maximum length of 256 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[CfnDevice.LocationProperty, _IResolvable_da3f097b]]:
        '''The site location.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[CfnDevice.LocationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def model(self) -> typing.Optional[builtins.str]:
        '''The model of the device.

        Constraints: Maximum length of 128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-model
        '''
        result = self._values.get("model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serial_number(self) -> typing.Optional[builtins.str]:
        '''The serial number of the device.

        Constraints: Maximum length of 128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-serialnumber
        '''
        result = self._values.get("serial_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def site_id(self) -> typing.Optional[builtins.str]:
        '''The site ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-siteid
        '''
        result = self._values.get("site_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The device type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        '''The vendor of the device.

        Constraints: Maximum length of 128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-vendor
        '''
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGlobalNetwork(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnGlobalNetwork",
):
    '''A CloudFormation ``AWS::NetworkManager::GlobalNetwork``.

    Creates a new, empty global network.

    :cloudformationResource: AWS::NetworkManager::GlobalNetwork
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_global_network = networkmanager.CfnGlobalNetwork(self, "MyCfnGlobalNetwork",
            description="description",
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
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::GlobalNetwork``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: A description of the global network. Constraints: Maximum length of 256 characters.
        :param tags: The tags for the global network.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnGlobalNetwork.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGlobalNetworkProps(description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnGlobalNetwork.inspect)
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
            type_hints = typing.get_type_hints(CfnGlobalNetwork._render_properties)
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
        '''The ARN of the global network.

        For example, ``arn:aws:networkmanager::123456789012:global-network/global-network-01231231231231231`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the global network.

        For example, ``global-network-01231231231231231`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags for the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the global network.

        Constraints: Maximum length of 256 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnGlobalNetwork, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnGlobalNetworkProps",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "tags": "tags"},
)
class CfnGlobalNetworkProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGlobalNetwork``.

        :param description: A description of the global network. Constraints: Maximum length of 256 characters.
        :param tags: The tags for the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_global_network_props = networkmanager.CfnGlobalNetworkProps(
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnGlobalNetworkProps.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the global network.

        Constraints: Maximum length of 256 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGlobalNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLink(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnLink",
):
    '''A CloudFormation ``AWS::NetworkManager::Link``.

    Specifies a link for a site.

    :cloudformationResource: AWS::NetworkManager::Link
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_link = networkmanager.CfnLink(self, "MyCfnLink",
            bandwidth=networkmanager.CfnLink.BandwidthProperty(
                download_speed=123,
                upload_speed=123
            ),
            global_network_id="globalNetworkId",
            site_id="siteId",
        
            # the properties below are optional
            description="description",
            provider="provider",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        bandwidth: typing.Union[typing.Union["CfnLink.BandwidthProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        global_network_id: builtins.str,
        site_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::Link``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bandwidth: The bandwidth for the link.
        :param global_network_id: The ID of the global network.
        :param site_id: The ID of the site.
        :param description: A description of the link. Constraints: Maximum length of 256 characters.
        :param provider: The provider of the link. Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^
        :param tags: The tags for the link.
        :param type: The type of the link. Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLink.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLinkProps(
            bandwidth=bandwidth,
            global_network_id=global_network_id,
            site_id=site_id,
            description=description,
            provider=provider,
            tags=tags,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLink.inspect)
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
            type_hints = typing.get_type_hints(CfnLink._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLinkArn")
    def attr_link_arn(self) -> builtins.str:
        '''The ARN of the link.

        For example, ``arn:aws:networkmanager::123456789012:link/global-network-01231231231231231/link-11112222aaaabbbb1`` .

        :cloudformationAttribute: LinkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLinkId")
    def attr_link_id(self) -> builtins.str:
        '''The ID of the link.

        For example, ``link-11112222aaaabbbb1`` .

        :cloudformationAttribute: LinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags for the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bandwidth")
    def bandwidth(
        self,
    ) -> typing.Union["CfnLink.BandwidthProperty", _IResolvable_da3f097b]:
        '''The bandwidth for the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-bandwidth
        '''
        return typing.cast(typing.Union["CfnLink.BandwidthProperty", _IResolvable_da3f097b], jsii.get(self, "bandwidth"))

    @bandwidth.setter
    def bandwidth(
        self,
        value: typing.Union["CfnLink.BandwidthProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLink, "bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bandwidth", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLink, "global_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="siteId")
    def site_id(self) -> builtins.str:
        '''The ID of the site.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-siteid
        '''
        return typing.cast(builtins.str, jsii.get(self, "siteId"))

    @site_id.setter
    def site_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLink, "site_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the link.

        Constraints: Maximum length of 256 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLink, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional[builtins.str]:
        '''The provider of the link.

        Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-provider
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLink, "provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provider", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the link.

        Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLink, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnLink.BandwidthProperty",
        jsii_struct_bases=[],
        name_mapping={
            "download_speed": "downloadSpeed",
            "upload_speed": "uploadSpeed",
        },
    )
    class BandwidthProperty:
        def __init__(
            self,
            *,
            download_speed: typing.Optional[jsii.Number] = None,
            upload_speed: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes bandwidth information.

            :param download_speed: Download speed in Mbps.
            :param upload_speed: Upload speed in Mbps.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                bandwidth_property = networkmanager.CfnLink.BandwidthProperty(
                    download_speed=123,
                    upload_speed=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnLink.BandwidthProperty.__init__)
                check_type(argname="argument download_speed", value=download_speed, expected_type=type_hints["download_speed"])
                check_type(argname="argument upload_speed", value=upload_speed, expected_type=type_hints["upload_speed"])
            self._values: typing.Dict[str, typing.Any] = {}
            if download_speed is not None:
                self._values["download_speed"] = download_speed
            if upload_speed is not None:
                self._values["upload_speed"] = upload_speed

        @builtins.property
        def download_speed(self) -> typing.Optional[jsii.Number]:
            '''Download speed in Mbps.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-downloadspeed
            '''
            result = self._values.get("download_speed")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def upload_speed(self) -> typing.Optional[jsii.Number]:
            '''Upload speed in Mbps.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-uploadspeed
            '''
            result = self._values.get("upload_speed")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BandwidthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnLinkAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnLinkAssociation",
):
    '''A CloudFormation ``AWS::NetworkManager::LinkAssociation``.

    Specifies the association between a device and a link. A device can be associated to multiple links and a link can be associated to multiple devices. The device and link must be in the same global network and the same site.

    :cloudformationResource: AWS::NetworkManager::LinkAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_link_association = networkmanager.CfnLinkAssociation(self, "MyCfnLinkAssociation",
            device_id="deviceId",
            global_network_id="globalNetworkId",
            link_id="linkId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::LinkAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param device_id: The device ID for the link association.
        :param global_network_id: The ID of the global network.
        :param link_id: The ID of the link.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLinkAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLinkAssociationProps(
            device_id=device_id, global_network_id=global_network_id, link_id=link_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLinkAssociation.inspect)
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
            type_hints = typing.get_type_hints(CfnLinkAssociation._render_properties)
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
    @jsii.member(jsii_name="deviceId")
    def device_id(self) -> builtins.str:
        '''The device ID for the link association.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-deviceid
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceId"))

    @device_id.setter
    def device_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLinkAssociation, "device_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLinkAssociation, "global_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="linkId")
    def link_id(self) -> builtins.str:
        '''The ID of the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-linkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "linkId"))

    @link_id.setter
    def link_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLinkAssociation, "link_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnLinkAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "device_id": "deviceId",
        "global_network_id": "globalNetworkId",
        "link_id": "linkId",
    },
)
class CfnLinkAssociationProps:
    def __init__(
        self,
        *,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnLinkAssociation``.

        :param device_id: The device ID for the link association.
        :param global_network_id: The ID of the global network.
        :param link_id: The ID of the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_link_association_props = networkmanager.CfnLinkAssociationProps(
                device_id="deviceId",
                global_network_id="globalNetworkId",
                link_id="linkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLinkAssociationProps.__init__)
            check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument link_id", value=link_id, expected_type=type_hints["link_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "device_id": device_id,
            "global_network_id": global_network_id,
            "link_id": link_id,
        }

    @builtins.property
    def device_id(self) -> builtins.str:
        '''The device ID for the link association.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-deviceid
        '''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_id(self) -> builtins.str:
        '''The ID of the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-linkid
        '''
        result = self._values.get("link_id")
        assert result is not None, "Required property 'link_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinkAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnLinkProps",
    jsii_struct_bases=[],
    name_mapping={
        "bandwidth": "bandwidth",
        "global_network_id": "globalNetworkId",
        "site_id": "siteId",
        "description": "description",
        "provider": "provider",
        "tags": "tags",
        "type": "type",
    },
)
class CfnLinkProps:
    def __init__(
        self,
        *,
        bandwidth: typing.Union[typing.Union[CfnLink.BandwidthProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        global_network_id: builtins.str,
        site_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLink``.

        :param bandwidth: The bandwidth for the link.
        :param global_network_id: The ID of the global network.
        :param site_id: The ID of the site.
        :param description: A description of the link. Constraints: Maximum length of 256 characters.
        :param provider: The provider of the link. Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^
        :param tags: The tags for the link.
        :param type: The type of the link. Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_link_props = networkmanager.CfnLinkProps(
                bandwidth=networkmanager.CfnLink.BandwidthProperty(
                    download_speed=123,
                    upload_speed=123
                ),
                global_network_id="globalNetworkId",
                site_id="siteId",
            
                # the properties below are optional
                description="description",
                provider="provider",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLinkProps.__init__)
            check_type(argname="argument bandwidth", value=bandwidth, expected_type=type_hints["bandwidth"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument site_id", value=site_id, expected_type=type_hints["site_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "bandwidth": bandwidth,
            "global_network_id": global_network_id,
            "site_id": site_id,
        }
        if description is not None:
            self._values["description"] = description
        if provider is not None:
            self._values["provider"] = provider
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def bandwidth(
        self,
    ) -> typing.Union[CfnLink.BandwidthProperty, _IResolvable_da3f097b]:
        '''The bandwidth for the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-bandwidth
        '''
        result = self._values.get("bandwidth")
        assert result is not None, "Required property 'bandwidth' is missing"
        return typing.cast(typing.Union[CfnLink.BandwidthProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_id(self) -> builtins.str:
        '''The ID of the site.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-siteid
        '''
        result = self._values.get("site_id")
        assert result is not None, "Required property 'site_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the link.

        Constraints: Maximum length of 256 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider(self) -> typing.Optional[builtins.str]:
        '''The provider of the link.

        Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-provider
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the link.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the link.

        Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSite(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnSite",
):
    '''A CloudFormation ``AWS::NetworkManager::Site``.

    Specifies a site in a global network.

    :cloudformationResource: AWS::NetworkManager::Site
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_site = networkmanager.CfnSite(self, "MyCfnSite",
            global_network_id="globalNetworkId",
        
            # the properties below are optional
            description="description",
            location=networkmanager.CfnSite.LocationProperty(
                address="address",
                latitude="latitude",
                longitude="longitude"
            ),
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
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[typing.Union["CfnSite.LocationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::Site``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param global_network_id: The ID of the global network.
        :param description: A description of your site. Constraints: Maximum length of 256 characters.
        :param location: The site location. This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated. - ``Address`` : The physical address of the site. - ``Latitude`` : The latitude of the site. - ``Longitude`` : The longitude of the site.
        :param tags: The tags for the site.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSite.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSiteProps(
            global_network_id=global_network_id,
            description=description,
            location=location,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSite.inspect)
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
            type_hints = typing.get_type_hints(CfnSite._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSiteArn")
    def attr_site_arn(self) -> builtins.str:
        '''The ARN of the site.

        For example, ``arn:aws:networkmanager::123456789012:site/global-network-01231231231231231/site-444555aaabbb11223`` .

        :cloudformationAttribute: SiteArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSiteId")
    def attr_site_id(self) -> builtins.str:
        '''The ID of the site.

        For example, ``site-444555aaabbb11223`` .

        :cloudformationAttribute: SiteId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags for the site.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSite, "global_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of your site.

        Constraints: Maximum length of 256 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSite, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union["CfnSite.LocationProperty", _IResolvable_da3f097b]]:
        '''The site location.

        This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated.

        - ``Address`` : The physical address of the site.
        - ``Latitude`` : The latitude of the site.
        - ``Longitude`` : The longitude of the site.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-location
        '''
        return typing.cast(typing.Optional[typing.Union["CfnSite.LocationProperty", _IResolvable_da3f097b]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union["CfnSite.LocationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSite, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnSite.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "latitude": "latitude",
            "longitude": "longitude",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            latitude: typing.Optional[builtins.str] = None,
            longitude: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a location.

            :param address: The physical address.
            :param latitude: The latitude.
            :param longitude: The longitude.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                location_property = networkmanager.CfnSite.LocationProperty(
                    address="address",
                    latitude="latitude",
                    longitude="longitude"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSite.LocationProperty.__init__)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
                check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            self._values: typing.Dict[str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if latitude is not None:
                self._values["latitude"] = latitude
            if longitude is not None:
                self._values["longitude"] = longitude

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The physical address.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def latitude(self) -> typing.Optional[builtins.str]:
            '''The latitude.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-latitude
            '''
            result = self._values.get("latitude")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def longitude(self) -> typing.Optional[builtins.str]:
            '''The longitude.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-longitude
            '''
            result = self._values.get("longitude")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnSiteProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "description": "description",
        "location": "location",
        "tags": "tags",
    },
)
class CfnSiteProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[typing.Union[CfnSite.LocationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSite``.

        :param global_network_id: The ID of the global network.
        :param description: A description of your site. Constraints: Maximum length of 256 characters.
        :param location: The site location. This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated. - ``Address`` : The physical address of the site. - ``Latitude`` : The latitude of the site. - ``Longitude`` : The longitude of the site.
        :param tags: The tags for the site.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_site_props = networkmanager.CfnSiteProps(
                global_network_id="globalNetworkId",
            
                # the properties below are optional
                description="description",
                location=networkmanager.CfnSite.LocationProperty(
                    address="address",
                    latitude="latitude",
                    longitude="longitude"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSiteProps.__init__)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "global_network_id": global_network_id,
        }
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of your site.

        Constraints: Maximum length of 256 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[CfnSite.LocationProperty, _IResolvable_da3f097b]]:
        '''The site location.

        This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated.

        - ``Address`` : The physical address of the site.
        - ``Latitude`` : The latitude of the site.
        - ``Longitude`` : The longitude of the site.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[CfnSite.LocationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the site.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSiteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSiteToSiteVpnAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnSiteToSiteVpnAttachment",
):
    '''A CloudFormation ``AWS::NetworkManager::SiteToSiteVpnAttachment``.

    Creates an Amazon Web Services site-to-site VPN attachment on an edge location of a core network.

    :cloudformationResource: AWS::NetworkManager::SiteToSiteVpnAttachment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_site_to_site_vpn_attachment = networkmanager.CfnSiteToSiteVpnAttachment(self, "MyCfnSiteToSiteVpnAttachment",
            core_network_id="coreNetworkId",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpn_connection_arn="vpnConnectionArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        core_network_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        vpn_connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::SiteToSiteVpnAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param core_network_id: The core network ID.
        :param tags: The tags associated with the site-to-site VPN attachment.
        :param vpn_connection_arn: The ARN of the site-to-site VPN attachment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSiteToSiteVpnAttachment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSiteToSiteVpnAttachmentProps(
            core_network_id=core_network_id,
            tags=tags,
            vpn_connection_arn=vpn_connection_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSiteToSiteVpnAttachment.inspect)
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
            type_hints = typing.get_type_hints(CfnSiteToSiteVpnAttachment._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentId")
    def attr_attachment_id(self) -> builtins.str:
        '''The ID of the site-to-site VPN attachment.

        :cloudformationAttribute: AttachmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentPolicyRuleNumber")
    def attr_attachment_policy_rule_number(self) -> jsii.Number:
        '''The policy rule number associated with the attachment.

        :cloudformationAttribute: AttachmentPolicyRuleNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAttachmentPolicyRuleNumber"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentType")
    def attr_attachment_type(self) -> builtins.str:
        '''The type of attachment.

        This will be ``SITE_TO_SITE_VPN`` .

        :cloudformationAttribute: AttachmentType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the site-to-site VPN attachment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEdgeLocation")
    def attr_edge_location(self) -> builtins.str:
        '''The Region where the core network edge is located.

        :cloudformationAttribute: EdgeLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEdgeLocation"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The ID of the site-to-site VPN attachment owner.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The resource ARN for the site-to-site VPN attachment.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSegmentName")
    def attr_segment_name(self) -> builtins.str:
        '''The name of the site-to-site VPN attachment's segment.

        :cloudformationAttribute: SegmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the site-to-site VPN attachment.

        This can be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the site-to-site VPN attachment was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags associated with the site-to-site VPN attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="coreNetworkId")
    def core_network_id(self) -> typing.Optional[builtins.str]:
        '''The core network ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-corenetworkid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreNetworkId"))

    @core_network_id.setter
    def core_network_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSiteToSiteVpnAttachment, "core_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpnConnectionArn")
    def vpn_connection_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the site-to-site VPN attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-vpnconnectionarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnConnectionArn"))

    @vpn_connection_arn.setter
    def vpn_connection_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSiteToSiteVpnAttachment, "vpn_connection_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnConnectionArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnSiteToSiteVpnAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_id": "coreNetworkId",
        "tags": "tags",
        "vpn_connection_arn": "vpnConnectionArn",
    },
)
class CfnSiteToSiteVpnAttachmentProps:
    def __init__(
        self,
        *,
        core_network_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        vpn_connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSiteToSiteVpnAttachment``.

        :param core_network_id: The core network ID.
        :param tags: The tags associated with the site-to-site VPN attachment.
        :param vpn_connection_arn: The ARN of the site-to-site VPN attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_site_to_site_vpn_attachment_props = networkmanager.CfnSiteToSiteVpnAttachmentProps(
                core_network_id="coreNetworkId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpn_connection_arn="vpnConnectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSiteToSiteVpnAttachmentProps.__init__)
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpn_connection_arn", value=vpn_connection_arn, expected_type=type_hints["vpn_connection_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if core_network_id is not None:
            self._values["core_network_id"] = core_network_id
        if tags is not None:
            self._values["tags"] = tags
        if vpn_connection_arn is not None:
            self._values["vpn_connection_arn"] = vpn_connection_arn

    @builtins.property
    def core_network_id(self) -> typing.Optional[builtins.str]:
        '''The core network ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-corenetworkid
        '''
        result = self._values.get("core_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the site-to-site VPN attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpn_connection_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the site-to-site VPN attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-vpnconnectionarn
        '''
        result = self._values.get("vpn_connection_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSiteToSiteVpnAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTransitGatewayRegistration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayRegistration",
):
    '''A CloudFormation ``AWS::NetworkManager::TransitGatewayRegistration``.

    Registers a transit gateway in your global network. The transit gateway can be in any AWS Region , but it must be owned by the same AWS account that owns the global network. You cannot register a transit gateway in more than one global network.

    :cloudformationResource: AWS::NetworkManager::TransitGatewayRegistration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_transit_gateway_registration = networkmanager.CfnTransitGatewayRegistration(self, "MyCfnTransitGatewayRegistration",
            global_network_id="globalNetworkId",
            transit_gateway_arn="transitGatewayArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        global_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::TransitGatewayRegistration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param global_network_id: The ID of the global network.
        :param transit_gateway_arn: The Amazon Resource Name (ARN) of the transit gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTransitGatewayRegistration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTransitGatewayRegistrationProps(
            global_network_id=global_network_id,
            transit_gateway_arn=transit_gateway_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTransitGatewayRegistration.inspect)
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
            type_hints = typing.get_type_hints(CfnTransitGatewayRegistration._render_properties)
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
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTransitGatewayRegistration, "global_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transitGatewayArn")
    def transit_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the transit gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-transitgatewayarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayArn"))

    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTransitGatewayRegistration, "transit_gateway_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayRegistrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "transit_gateway_arn": "transitGatewayArn",
    },
)
class CfnTransitGatewayRegistrationProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnTransitGatewayRegistration``.

        :param global_network_id: The ID of the global network.
        :param transit_gateway_arn: The Amazon Resource Name (ARN) of the transit gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_transit_gateway_registration_props = networkmanager.CfnTransitGatewayRegistrationProps(
                global_network_id="globalNetworkId",
                transit_gateway_arn="transitGatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTransitGatewayRegistrationProps.__init__)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument transit_gateway_arn", value=transit_gateway_arn, expected_type=type_hints["transit_gateway_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "global_network_id": global_network_id,
            "transit_gateway_arn": transit_gateway_arn,
        }

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the transit gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-transitgatewayarn
        '''
        result = self._values.get("transit_gateway_arn")
        assert result is not None, "Required property 'transit_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransitGatewayRegistrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnVpcAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnVpcAttachment",
):
    '''A CloudFormation ``AWS::NetworkManager::VpcAttachment``.

    Creates a VPC attachment on an edge location of a core network.

    :cloudformationResource: AWS::NetworkManager::VpcAttachment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_vpc_attachment = networkmanager.CfnVpcAttachment(self, "MyCfnVpcAttachment",
            core_network_id="coreNetworkId",
            options=networkmanager.CfnVpcAttachment.VpcOptionsProperty(
                ipv6_support=False
            ),
            subnet_arns=["subnetArns"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_arn="vpcArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        core_network_id: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[typing.Union["CfnVpcAttachment.VpcOptionsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        vpc_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::VpcAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param core_network_id: The core network ID.
        :param options: Options for creating the VPC attachment.
        :param subnet_arns: The subnet ARNs.
        :param tags: The tags associated with the VPC attachment.
        :param vpc_arn: The ARN of the VPC attachment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVpcAttachment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcAttachmentProps(
            core_network_id=core_network_id,
            options=options,
            subnet_arns=subnet_arns,
            tags=tags,
            vpc_arn=vpc_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVpcAttachment.inspect)
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
            type_hints = typing.get_type_hints(CfnVpcAttachment._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentId")
    def attr_attachment_id(self) -> builtins.str:
        '''The ID of the VPC attachment.

        :cloudformationAttribute: AttachmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentPolicyRuleNumber")
    def attr_attachment_policy_rule_number(self) -> jsii.Number:
        '''The policy rule number associated with the attachment.

        :cloudformationAttribute: AttachmentPolicyRuleNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAttachmentPolicyRuleNumber"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentType")
    def attr_attachment_type(self) -> builtins.str:
        '''The type of attachment.

        This will be ``VPC`` .

        :cloudformationAttribute: AttachmentType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the VPC attachment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEdgeLocation")
    def attr_edge_location(self) -> builtins.str:
        '''The Region where the core network edge is located.

        :cloudformationAttribute: EdgeLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEdgeLocation"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The ID of the VPC attachment owner.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The resource ARN for the VPC attachment.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSegmentName")
    def attr_segment_name(self) -> builtins.str:
        '''The name of the attachment's segment.

        :cloudformationAttribute: SegmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the attachment.

        This can be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the VPC attachment was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags associated with the VPC attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="coreNetworkId")
    def core_network_id(self) -> typing.Optional[builtins.str]:
        '''The core network ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-corenetworkid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreNetworkId"))

    @core_network_id.setter
    def core_network_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVpcAttachment, "core_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="options")
    def options(
        self,
    ) -> typing.Optional[typing.Union["CfnVpcAttachment.VpcOptionsProperty", _IResolvable_da3f097b]]:
        '''Options for creating the VPC attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-options
        '''
        return typing.cast(typing.Optional[typing.Union["CfnVpcAttachment.VpcOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "options"))

    @options.setter
    def options(
        self,
        value: typing.Optional[typing.Union["CfnVpcAttachment.VpcOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVpcAttachment, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetArns")
    def subnet_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The subnet ARNs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-subnetarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetArns"))

    @subnet_arns.setter
    def subnet_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVpcAttachment, "subnet_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcArn")
    def vpc_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the VPC attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-vpcarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcArn"))

    @vpc_arn.setter
    def vpc_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVpcAttachment, "vpc_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnVpcAttachment.VpcOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"ipv6_support": "ipv6Support"},
    )
    class VpcOptionsProperty:
        def __init__(
            self,
            *,
            ipv6_support: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the VPC options.

            :param ipv6_support: Indicates whether IPv6 is supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                vpc_options_property = networkmanager.CfnVpcAttachment.VpcOptionsProperty(
                    ipv6_support=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnVpcAttachment.VpcOptionsProperty.__init__)
                check_type(argname="argument ipv6_support", value=ipv6_support, expected_type=type_hints["ipv6_support"])
            self._values: typing.Dict[str, typing.Any] = {}
            if ipv6_support is not None:
                self._values["ipv6_support"] = ipv6_support

        @builtins.property
        def ipv6_support(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether IPv6 is supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html#cfn-networkmanager-vpcattachment-vpcoptions-ipv6support
            '''
            result = self._values.get("ipv6_support")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnVpcAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_id": "coreNetworkId",
        "options": "options",
        "subnet_arns": "subnetArns",
        "tags": "tags",
        "vpc_arn": "vpcArn",
    },
)
class CfnVpcAttachmentProps:
    def __init__(
        self,
        *,
        core_network_id: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[typing.Union[CfnVpcAttachment.VpcOptionsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        vpc_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVpcAttachment``.

        :param core_network_id: The core network ID.
        :param options: Options for creating the VPC attachment.
        :param subnet_arns: The subnet ARNs.
        :param tags: The tags associated with the VPC attachment.
        :param vpc_arn: The ARN of the VPC attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_vpc_attachment_props = networkmanager.CfnVpcAttachmentProps(
                core_network_id="coreNetworkId",
                options=networkmanager.CfnVpcAttachment.VpcOptionsProperty(
                    ipv6_support=False
                ),
                subnet_arns=["subnetArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_arn="vpcArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVpcAttachmentProps.__init__)
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument subnet_arns", value=subnet_arns, expected_type=type_hints["subnet_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_arn", value=vpc_arn, expected_type=type_hints["vpc_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if core_network_id is not None:
            self._values["core_network_id"] = core_network_id
        if options is not None:
            self._values["options"] = options
        if subnet_arns is not None:
            self._values["subnet_arns"] = subnet_arns
        if tags is not None:
            self._values["tags"] = tags
        if vpc_arn is not None:
            self._values["vpc_arn"] = vpc_arn

    @builtins.property
    def core_network_id(self) -> typing.Optional[builtins.str]:
        '''The core network ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-corenetworkid
        '''
        result = self._values.get("core_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional[typing.Union[CfnVpcAttachment.VpcOptionsProperty, _IResolvable_da3f097b]]:
        '''Options for creating the VPC attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-options
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Union[CfnVpcAttachment.VpcOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def subnet_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The subnet ARNs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-subnetarns
        '''
        result = self._values.get("subnet_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the VPC attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the VPC attachment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-vpcarn
        '''
        result = self._values.get("vpc_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnectAttachment",
    "CfnConnectAttachmentProps",
    "CfnConnectPeer",
    "CfnConnectPeerProps",
    "CfnCoreNetwork",
    "CfnCoreNetworkProps",
    "CfnCustomerGatewayAssociation",
    "CfnCustomerGatewayAssociationProps",
    "CfnDevice",
    "CfnDeviceProps",
    "CfnGlobalNetwork",
    "CfnGlobalNetworkProps",
    "CfnLink",
    "CfnLinkAssociation",
    "CfnLinkAssociationProps",
    "CfnLinkProps",
    "CfnSite",
    "CfnSiteProps",
    "CfnSiteToSiteVpnAttachment",
    "CfnSiteToSiteVpnAttachmentProps",
    "CfnTransitGatewayRegistration",
    "CfnTransitGatewayRegistrationProps",
    "CfnVpcAttachment",
    "CfnVpcAttachmentProps",
]

publication.publish()
