'''
# AWS::MediaTailor Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mediatailor as mediatailor
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MediaTailor construct libraries](https://constructs.dev/search?q=mediatailor)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MediaTailor resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaTailor.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MediaTailor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaTailor.html).

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
class CfnPlaybackConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration",
):
    '''A CloudFormation ``AWS::MediaTailor::PlaybackConfiguration``.

    Adds a new playback configuration to AWS Elemental MediaTailor.

    :cloudformationResource: AWS::MediaTailor::PlaybackConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        # configuration_aliases: Any
        
        cfn_playback_configuration = mediatailor.CfnPlaybackConfiguration(self, "MyCfnPlaybackConfiguration",
            ad_decision_server_url="adDecisionServerUrl",
            name="name",
            video_content_source_url="videoContentSourceUrl",
        
            # the properties below are optional
            avail_suppression=mediatailor.CfnPlaybackConfiguration.AvailSuppressionProperty(
                mode="mode",
                value="value"
            ),
            bumper=mediatailor.CfnPlaybackConfiguration.BumperProperty(
                end_url="endUrl",
                start_url="startUrl"
            ),
            cdn_configuration=mediatailor.CfnPlaybackConfiguration.CdnConfigurationProperty(
                ad_segment_url_prefix="adSegmentUrlPrefix",
                content_segment_url_prefix="contentSegmentUrlPrefix"
            ),
            configuration_aliases={
                "configuration_aliases_key": configuration_aliases
            },
            dash_configuration=mediatailor.CfnPlaybackConfiguration.DashConfigurationProperty(
                manifest_endpoint_prefix="manifestEndpointPrefix",
                mpd_location="mpdLocation",
                origin_manifest_type="originManifestType"
            ),
            live_pre_roll_configuration=mediatailor.CfnPlaybackConfiguration.LivePreRollConfigurationProperty(
                ad_decision_server_url="adDecisionServerUrl",
                max_duration_seconds=123
            ),
            manifest_processing_rules=mediatailor.CfnPlaybackConfiguration.ManifestProcessingRulesProperty(
                ad_marker_passthrough=mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty(
                    enabled=False
                )
            ),
            personalization_threshold_seconds=123,
            slate_ad_url="slateAdUrl",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            transcode_profile_name="transcodeProfileName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ad_decision_server_url: builtins.str,
        name: builtins.str,
        video_content_source_url: builtins.str,
        avail_suppression: typing.Optional[typing.Union[typing.Union["CfnPlaybackConfiguration.AvailSuppressionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        bumper: typing.Optional[typing.Union[typing.Union["CfnPlaybackConfiguration.BumperProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        cdn_configuration: typing.Optional[typing.Union[typing.Union["CfnPlaybackConfiguration.CdnConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        configuration_aliases: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]] = None,
        dash_configuration: typing.Optional[typing.Union[typing.Union["CfnPlaybackConfiguration.DashConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        live_pre_roll_configuration: typing.Optional[typing.Union[typing.Union["CfnPlaybackConfiguration.LivePreRollConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        manifest_processing_rules: typing.Optional[typing.Union[typing.Union["CfnPlaybackConfiguration.ManifestProcessingRulesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        personalization_threshold_seconds: typing.Optional[jsii.Number] = None,
        slate_ad_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        transcode_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::PlaybackConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param ad_decision_server_url: The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
        :param name: The identifier for the playback configuration.
        :param video_content_source_url: The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
        :param avail_suppression: The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .
        :param bumper: The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .
        :param cdn_configuration: The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
        :param configuration_aliases: The player parameters and aliases used as dynamic variables during session initialization. For more information, see `Domain Variables <https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domain.html>`_ .
        :param dash_configuration: The configuration for DASH content.
        :param live_pre_roll_configuration: The configuration for pre-roll ad insertion.
        :param manifest_processing_rules: The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
        :param personalization_threshold_seconds: Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see `Ad Behavior in MediaTailor <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .
        :param slate_ad_url: The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
        :param tags: The tags to assign to the playback configuration.
        :param transcode_profile_name: The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPlaybackConfiguration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlaybackConfigurationProps(
            ad_decision_server_url=ad_decision_server_url,
            name=name,
            video_content_source_url=video_content_source_url,
            avail_suppression=avail_suppression,
            bumper=bumper,
            cdn_configuration=cdn_configuration,
            configuration_aliases=configuration_aliases,
            dash_configuration=dash_configuration,
            live_pre_roll_configuration=live_pre_roll_configuration,
            manifest_processing_rules=manifest_processing_rules,
            personalization_threshold_seconds=personalization_threshold_seconds,
            slate_ad_url=slate_ad_url,
            tags=tags,
            transcode_profile_name=transcode_profile_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPlaybackConfiguration.inspect)
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
            type_hints = typing.get_type_hints(CfnPlaybackConfiguration._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDashConfigurationManifestEndpointPrefix")
    def attr_dash_configuration_manifest_endpoint_prefix(self) -> builtins.str:
        '''
        :cloudformationAttribute: DashConfiguration.ManifestEndpointPrefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDashConfigurationManifestEndpointPrefix"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHlsConfigurationManifestEndpointPrefix")
    def attr_hls_configuration_manifest_endpoint_prefix(self) -> builtins.str:
        '''
        :cloudformationAttribute: HlsConfiguration.ManifestEndpointPrefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHlsConfigurationManifestEndpointPrefix"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPlaybackConfigurationArn")
    def attr_playback_configuration_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: PlaybackConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlaybackConfigurationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPlaybackEndpointPrefix")
    def attr_playback_endpoint_prefix(self) -> builtins.str:
        '''
        :cloudformationAttribute: PlaybackEndpointPrefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlaybackEndpointPrefix"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSessionInitializationEndpointPrefix")
    def attr_session_initialization_endpoint_prefix(self) -> builtins.str:
        '''
        :cloudformationAttribute: SessionInitializationEndpointPrefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSessionInitializationEndpointPrefix"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags to assign to the playback configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="adDecisionServerUrl")
    def ad_decision_server_url(self) -> builtins.str:
        '''The URL for the ad decision server (ADS).

        This includes the specification of static parameters and placeholders for dynamic parameters. MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-addecisionserverurl
        '''
        return typing.cast(builtins.str, jsii.get(self, "adDecisionServerUrl"))

    @ad_decision_server_url.setter
    def ad_decision_server_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "ad_decision_server_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adDecisionServerUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The identifier for the playback configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="videoContentSourceUrl")
    def video_content_source_url(self) -> builtins.str:
        '''The URL prefix for the parent manifest for the stream, minus the asset ID.

        The maximum length is 512 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-videocontentsourceurl
        '''
        return typing.cast(builtins.str, jsii.get(self, "videoContentSourceUrl"))

    @video_content_source_url.setter
    def video_content_source_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "video_content_source_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "videoContentSourceUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availSuppression")
    def avail_suppression(
        self,
    ) -> typing.Optional[typing.Union["CfnPlaybackConfiguration.AvailSuppressionProperty", _IResolvable_da3f097b]]:
        '''The configuration for avail suppression, also known as ad suppression.

        For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-availsuppression
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPlaybackConfiguration.AvailSuppressionProperty", _IResolvable_da3f097b]], jsii.get(self, "availSuppression"))

    @avail_suppression.setter
    def avail_suppression(
        self,
        value: typing.Optional[typing.Union["CfnPlaybackConfiguration.AvailSuppressionProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "avail_suppression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availSuppression", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bumper")
    def bumper(
        self,
    ) -> typing.Optional[typing.Union["CfnPlaybackConfiguration.BumperProperty", _IResolvable_da3f097b]]:
        '''The configuration for bumpers.

        Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-bumper
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPlaybackConfiguration.BumperProperty", _IResolvable_da3f097b]], jsii.get(self, "bumper"))

    @bumper.setter
    def bumper(
        self,
        value: typing.Optional[typing.Union["CfnPlaybackConfiguration.BumperProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "bumper").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bumper", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cdnConfiguration")
    def cdn_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnPlaybackConfiguration.CdnConfigurationProperty", _IResolvable_da3f097b]]:
        '''The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPlaybackConfiguration.CdnConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "cdnConfiguration"))

    @cdn_configuration.setter
    def cdn_configuration(
        self,
        value: typing.Optional[typing.Union["CfnPlaybackConfiguration.CdnConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "cdn_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationAliases")
    def configuration_aliases(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]]:
        '''The player parameters and aliases used as dynamic variables during session initialization.

        For more information, see `Domain Variables <https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domain.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-configurationaliases
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]], jsii.get(self, "configurationAliases"))

    @configuration_aliases.setter
    def configuration_aliases(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "configuration_aliases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationAliases", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashConfiguration")
    def dash_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnPlaybackConfiguration.DashConfigurationProperty", _IResolvable_da3f097b]]:
        '''The configuration for DASH content.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPlaybackConfiguration.DashConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "dashConfiguration"))

    @dash_configuration.setter
    def dash_configuration(
        self,
        value: typing.Optional[typing.Union["CfnPlaybackConfiguration.DashConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "dash_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="livePreRollConfiguration")
    def live_pre_roll_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnPlaybackConfiguration.LivePreRollConfigurationProperty", _IResolvable_da3f097b]]:
        '''The configuration for pre-roll ad insertion.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPlaybackConfiguration.LivePreRollConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "livePreRollConfiguration"))

    @live_pre_roll_configuration.setter
    def live_pre_roll_configuration(
        self,
        value: typing.Optional[typing.Union["CfnPlaybackConfiguration.LivePreRollConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "live_pre_roll_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "livePreRollConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="manifestProcessingRules")
    def manifest_processing_rules(
        self,
    ) -> typing.Optional[typing.Union["CfnPlaybackConfiguration.ManifestProcessingRulesProperty", _IResolvable_da3f097b]]:
        '''The configuration for manifest processing rules.

        Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-manifestprocessingrules
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPlaybackConfiguration.ManifestProcessingRulesProperty", _IResolvable_da3f097b]], jsii.get(self, "manifestProcessingRules"))

    @manifest_processing_rules.setter
    def manifest_processing_rules(
        self,
        value: typing.Optional[typing.Union["CfnPlaybackConfiguration.ManifestProcessingRulesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "manifest_processing_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifestProcessingRules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="personalizationThresholdSeconds")
    def personalization_threshold_seconds(self) -> typing.Optional[jsii.Number]:
        '''Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break.

        If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see `Ad Behavior in MediaTailor <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-personalizationthresholdseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "personalizationThresholdSeconds"))

    @personalization_threshold_seconds.setter
    def personalization_threshold_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "personalization_threshold_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "personalizationThresholdSeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="slateAdUrl")
    def slate_ad_url(self) -> typing.Optional[builtins.str]:
        '''The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads.

        MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-slateadurl
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slateAdUrl"))

    @slate_ad_url.setter
    def slate_ad_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "slate_ad_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slateAdUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transcodeProfileName")
    def transcode_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name that is used to associate this playback configuration with a custom transcode profile.

        This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-transcodeprofilename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transcodeProfileName"))

    @transcode_profile_name.setter
    def transcode_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPlaybackConfiguration, "transcode_profile_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transcodeProfileName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class AdMarkerPassthroughProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''For HLS, when set to ``true`` , MediaTailor passes through ``EXT-X-CUE-IN`` , ``EXT-X-CUE-OUT`` , and ``EXT-X-SPLICEPOINT-SCTE35`` ad markers from the origin manifest to the MediaTailor personalized manifest.

            No logic is applied to these ad markers. For example, if ``EXT-X-CUE-OUT`` has a value of ``60`` , but no ads are filled for that ad break, MediaTailor will not set the value to ``0`` .

            :param enabled: Enables ad marker passthrough for your configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                ad_marker_passthrough_property = mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPlaybackConfiguration.AdMarkerPassthroughProperty.__init__)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables ad marker passthrough for your configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html#cfn-mediatailor-playbackconfiguration-admarkerpassthrough-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdMarkerPassthroughProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AvailSuppressionProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode", "value": "value"},
    )
    class AvailSuppressionProperty:
        def __init__(
            self,
            *,
            mode: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for avail suppression, also known as ad suppression.

            For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .

            :param mode: Sets the ad suppression mode. By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to BEHIND_LIVE_EDGE, ad suppression is active and MediaTailor won't fill ad breaks on or behind the ad suppression Value time in the manifest lookback window.
            :param value: A live edge offset time in HH:MM:SS. MediaTailor won't fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor won't fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor won't fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but won't fill ad breaks on or behind 45 minutes behind the live edge.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                avail_suppression_property = mediatailor.CfnPlaybackConfiguration.AvailSuppressionProperty(
                    mode="mode",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPlaybackConfiguration.AvailSuppressionProperty.__init__)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {}
            if mode is not None:
                self._values["mode"] = mode
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''Sets the ad suppression mode.

            By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to BEHIND_LIVE_EDGE, ad suppression is active and MediaTailor won't fill ad breaks on or behind the ad suppression Value time in the manifest lookback window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html#cfn-mediatailor-playbackconfiguration-availsuppression-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''A live edge offset time in HH:MM:SS.

            MediaTailor won't fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor won't fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor won't fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but won't fill ad breaks on or behind 45 minutes behind the live edge.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html#cfn-mediatailor-playbackconfiguration-availsuppression-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailSuppressionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.BumperProperty",
        jsii_struct_bases=[],
        name_mapping={"end_url": "endUrl", "start_url": "startUrl"},
    )
    class BumperProperty:
        def __init__(
            self,
            *,
            end_url: typing.Optional[builtins.str] = None,
            start_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for bumpers.

            Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .

            :param end_url: The URL for the end bumper asset.
            :param start_url: The URL for the start bumper asset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                bumper_property = mediatailor.CfnPlaybackConfiguration.BumperProperty(
                    end_url="endUrl",
                    start_url="startUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPlaybackConfiguration.BumperProperty.__init__)
                check_type(argname="argument end_url", value=end_url, expected_type=type_hints["end_url"])
                check_type(argname="argument start_url", value=start_url, expected_type=type_hints["start_url"])
            self._values: typing.Dict[str, typing.Any] = {}
            if end_url is not None:
                self._values["end_url"] = end_url
            if start_url is not None:
                self._values["start_url"] = start_url

        @builtins.property
        def end_url(self) -> typing.Optional[builtins.str]:
            '''The URL for the end bumper asset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html#cfn-mediatailor-playbackconfiguration-bumper-endurl
            '''
            result = self._values.get("end_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_url(self) -> typing.Optional[builtins.str]:
            '''The URL for the start bumper asset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html#cfn-mediatailor-playbackconfiguration-bumper-starturl
            '''
            result = self._values.get("start_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BumperProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.CdnConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_segment_url_prefix": "adSegmentUrlPrefix",
            "content_segment_url_prefix": "contentSegmentUrlPrefix",
        },
    )
    class CdnConfigurationProperty:
        def __init__(
            self,
            *,
            ad_segment_url_prefix: typing.Optional[builtins.str] = None,
            content_segment_url_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

            :param ad_segment_url_prefix: A non-default content delivery network (CDN) to serve ad segments. By default, MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the origin ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in this AdSegmentUrlPrefix. When MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
            :param content_segment_url_prefix: A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this ContentSegmentUrlPrefix. When MediaTailor serves a manifest, it reports your CDN as the source for content segments.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                cdn_configuration_property = mediatailor.CfnPlaybackConfiguration.CdnConfigurationProperty(
                    ad_segment_url_prefix="adSegmentUrlPrefix",
                    content_segment_url_prefix="contentSegmentUrlPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPlaybackConfiguration.CdnConfigurationProperty.__init__)
                check_type(argname="argument ad_segment_url_prefix", value=ad_segment_url_prefix, expected_type=type_hints["ad_segment_url_prefix"])
                check_type(argname="argument content_segment_url_prefix", value=content_segment_url_prefix, expected_type=type_hints["content_segment_url_prefix"])
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_segment_url_prefix is not None:
                self._values["ad_segment_url_prefix"] = ad_segment_url_prefix
            if content_segment_url_prefix is not None:
                self._values["content_segment_url_prefix"] = content_segment_url_prefix

        @builtins.property
        def ad_segment_url_prefix(self) -> typing.Optional[builtins.str]:
            '''A non-default content delivery network (CDN) to serve ad segments.

            By default, MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the origin ads.mediatailor..amazonaws.com. Then specify the rule's name in this AdSegmentUrlPrefix. When MediaTailor serves a manifest, it reports your CDN as the source for ad segments.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration-adsegmenturlprefix
            '''
            result = self._values.get("ad_segment_url_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def content_segment_url_prefix(self) -> typing.Optional[builtins.str]:
            '''A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server.

            First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this ContentSegmentUrlPrefix. When MediaTailor serves a manifest, it reports your CDN as the source for content segments.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration-contentsegmenturlprefix
            '''
            result = self._values.get("content_segment_url_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CdnConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.DashConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_endpoint_prefix": "manifestEndpointPrefix",
            "mpd_location": "mpdLocation",
            "origin_manifest_type": "originManifestType",
        },
    )
    class DashConfigurationProperty:
        def __init__(
            self,
            *,
            manifest_endpoint_prefix: typing.Optional[builtins.str] = None,
            mpd_location: typing.Optional[builtins.str] = None,
            origin_manifest_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for DASH content.

            :param manifest_endpoint_prefix: The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations.
            :param mpd_location: The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.
            :param origin_manifest_type: The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                dash_configuration_property = mediatailor.CfnPlaybackConfiguration.DashConfigurationProperty(
                    manifest_endpoint_prefix="manifestEndpointPrefix",
                    mpd_location="mpdLocation",
                    origin_manifest_type="originManifestType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPlaybackConfiguration.DashConfigurationProperty.__init__)
                check_type(argname="argument manifest_endpoint_prefix", value=manifest_endpoint_prefix, expected_type=type_hints["manifest_endpoint_prefix"])
                check_type(argname="argument mpd_location", value=mpd_location, expected_type=type_hints["mpd_location"])
                check_type(argname="argument origin_manifest_type", value=origin_manifest_type, expected_type=type_hints["origin_manifest_type"])
            self._values: typing.Dict[str, typing.Any] = {}
            if manifest_endpoint_prefix is not None:
                self._values["manifest_endpoint_prefix"] = manifest_endpoint_prefix
            if mpd_location is not None:
                self._values["mpd_location"] = mpd_location
            if origin_manifest_type is not None:
                self._values["origin_manifest_type"] = origin_manifest_type

        @builtins.property
        def manifest_endpoint_prefix(self) -> typing.Optional[builtins.str]:
            '''The URL generated by MediaTailor to initiate a playback session.

            The session uses server-side reporting. This setting is ignored in PUT operations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-manifestendpointprefix
            '''
            result = self._values.get("manifest_endpoint_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mpd_location(self) -> typing.Optional[builtins.str]:
            '''The setting that controls whether MediaTailor includes the Location tag in DASH manifests.

            MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-mpdlocation
            '''
            result = self._values.get("mpd_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def origin_manifest_type(self) -> typing.Optional[builtins.str]:
            '''The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests.

            If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-originmanifesttype
            '''
            result = self._values.get("origin_manifest_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.HlsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"manifest_endpoint_prefix": "manifestEndpointPrefix"},
    )
    class HlsConfigurationProperty:
        def __init__(
            self,
            *,
            manifest_endpoint_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for HLS content.

            :param manifest_endpoint_prefix: The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                hls_configuration_property = mediatailor.CfnPlaybackConfiguration.HlsConfigurationProperty(
                    manifest_endpoint_prefix="manifestEndpointPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPlaybackConfiguration.HlsConfigurationProperty.__init__)
                check_type(argname="argument manifest_endpoint_prefix", value=manifest_endpoint_prefix, expected_type=type_hints["manifest_endpoint_prefix"])
            self._values: typing.Dict[str, typing.Any] = {}
            if manifest_endpoint_prefix is not None:
                self._values["manifest_endpoint_prefix"] = manifest_endpoint_prefix

        @builtins.property
        def manifest_endpoint_prefix(self) -> typing.Optional[builtins.str]:
            '''The URL that is used to initiate a playback session for devices that support Apple HLS.

            The session uses server-side reporting.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html#cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix
            '''
            result = self._values.get("manifest_endpoint_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.LivePreRollConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_decision_server_url": "adDecisionServerUrl",
            "max_duration_seconds": "maxDurationSeconds",
        },
    )
    class LivePreRollConfigurationProperty:
        def __init__(
            self,
            *,
            ad_decision_server_url: typing.Optional[builtins.str] = None,
            max_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The configuration for pre-roll ad insertion.

            :param ad_decision_server_url: The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
            :param max_duration_seconds: The maximum allowed duration for the pre-roll ad avail. MediaTailor won't play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                live_pre_roll_configuration_property = mediatailor.CfnPlaybackConfiguration.LivePreRollConfigurationProperty(
                    ad_decision_server_url="adDecisionServerUrl",
                    max_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPlaybackConfiguration.LivePreRollConfigurationProperty.__init__)
                check_type(argname="argument ad_decision_server_url", value=ad_decision_server_url, expected_type=type_hints["ad_decision_server_url"])
                check_type(argname="argument max_duration_seconds", value=max_duration_seconds, expected_type=type_hints["max_duration_seconds"])
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_decision_server_url is not None:
                self._values["ad_decision_server_url"] = ad_decision_server_url
            if max_duration_seconds is not None:
                self._values["max_duration_seconds"] = max_duration_seconds

        @builtins.property
        def ad_decision_server_url(self) -> typing.Optional[builtins.str]:
            '''The URL for the ad decision server (ADS) for pre-roll ads.

            This includes the specification of static parameters and placeholders for dynamic parameters. MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverurl
            '''
            result = self._values.get("ad_decision_server_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum allowed duration for the pre-roll ad avail.

            MediaTailor won't play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-maxdurationseconds
            '''
            result = self._values.get("max_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LivePreRollConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.ManifestProcessingRulesProperty",
        jsii_struct_bases=[],
        name_mapping={"ad_marker_passthrough": "adMarkerPassthrough"},
    )
    class ManifestProcessingRulesProperty:
        def __init__(
            self,
            *,
            ad_marker_passthrough: typing.Optional[typing.Union[typing.Union["CfnPlaybackConfiguration.AdMarkerPassthroughProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The configuration for manifest processing rules.

            Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

            :param ad_marker_passthrough: For HLS, when set to ``true`` , MediaTailor passes through ``EXT-X-CUE-IN`` , ``EXT-X-CUE-OUT`` , and ``EXT-X-SPLICEPOINT-SCTE35`` ad markers from the origin manifest to the MediaTailor personalized manifest. No logic is applied to these ad markers. For example, if ``EXT-X-CUE-OUT`` has a value of ``60`` , but no ads are filled for that ad break, MediaTailor will not set the value to ``0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                manifest_processing_rules_property = mediatailor.CfnPlaybackConfiguration.ManifestProcessingRulesProperty(
                    ad_marker_passthrough=mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnPlaybackConfiguration.ManifestProcessingRulesProperty.__init__)
                check_type(argname="argument ad_marker_passthrough", value=ad_marker_passthrough, expected_type=type_hints["ad_marker_passthrough"])
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_marker_passthrough is not None:
                self._values["ad_marker_passthrough"] = ad_marker_passthrough

        @builtins.property
        def ad_marker_passthrough(
            self,
        ) -> typing.Optional[typing.Union["CfnPlaybackConfiguration.AdMarkerPassthroughProperty", _IResolvable_da3f097b]]:
            '''For HLS, when set to ``true`` , MediaTailor passes through ``EXT-X-CUE-IN`` , ``EXT-X-CUE-OUT`` , and ``EXT-X-SPLICEPOINT-SCTE35`` ad markers from the origin manifest to the MediaTailor personalized manifest.

            No logic is applied to these ad markers. For example, if ``EXT-X-CUE-OUT`` has a value of ``60`` , but no ads are filled for that ad break, MediaTailor will not set the value to ``0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html#cfn-mediatailor-playbackconfiguration-manifestprocessingrules-admarkerpassthrough
            '''
            result = self._values.get("ad_marker_passthrough")
            return typing.cast(typing.Optional[typing.Union["CfnPlaybackConfiguration.AdMarkerPassthroughProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManifestProcessingRulesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "ad_decision_server_url": "adDecisionServerUrl",
        "name": "name",
        "video_content_source_url": "videoContentSourceUrl",
        "avail_suppression": "availSuppression",
        "bumper": "bumper",
        "cdn_configuration": "cdnConfiguration",
        "configuration_aliases": "configurationAliases",
        "dash_configuration": "dashConfiguration",
        "live_pre_roll_configuration": "livePreRollConfiguration",
        "manifest_processing_rules": "manifestProcessingRules",
        "personalization_threshold_seconds": "personalizationThresholdSeconds",
        "slate_ad_url": "slateAdUrl",
        "tags": "tags",
        "transcode_profile_name": "transcodeProfileName",
    },
)
class CfnPlaybackConfigurationProps:
    def __init__(
        self,
        *,
        ad_decision_server_url: builtins.str,
        name: builtins.str,
        video_content_source_url: builtins.str,
        avail_suppression: typing.Optional[typing.Union[typing.Union[CfnPlaybackConfiguration.AvailSuppressionProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        bumper: typing.Optional[typing.Union[typing.Union[CfnPlaybackConfiguration.BumperProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        cdn_configuration: typing.Optional[typing.Union[typing.Union[CfnPlaybackConfiguration.CdnConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        configuration_aliases: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]] = None,
        dash_configuration: typing.Optional[typing.Union[typing.Union[CfnPlaybackConfiguration.DashConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        live_pre_roll_configuration: typing.Optional[typing.Union[typing.Union[CfnPlaybackConfiguration.LivePreRollConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        manifest_processing_rules: typing.Optional[typing.Union[typing.Union[CfnPlaybackConfiguration.ManifestProcessingRulesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        personalization_threshold_seconds: typing.Optional[jsii.Number] = None,
        slate_ad_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        transcode_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlaybackConfiguration``.

        :param ad_decision_server_url: The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
        :param name: The identifier for the playback configuration.
        :param video_content_source_url: The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
        :param avail_suppression: The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .
        :param bumper: The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .
        :param cdn_configuration: The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
        :param configuration_aliases: The player parameters and aliases used as dynamic variables during session initialization. For more information, see `Domain Variables <https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domain.html>`_ .
        :param dash_configuration: The configuration for DASH content.
        :param live_pre_roll_configuration: The configuration for pre-roll ad insertion.
        :param manifest_processing_rules: The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
        :param personalization_threshold_seconds: Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see `Ad Behavior in MediaTailor <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .
        :param slate_ad_url: The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
        :param tags: The tags to assign to the playback configuration.
        :param transcode_profile_name: The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            # configuration_aliases: Any
            
            cfn_playback_configuration_props = mediatailor.CfnPlaybackConfigurationProps(
                ad_decision_server_url="adDecisionServerUrl",
                name="name",
                video_content_source_url="videoContentSourceUrl",
            
                # the properties below are optional
                avail_suppression=mediatailor.CfnPlaybackConfiguration.AvailSuppressionProperty(
                    mode="mode",
                    value="value"
                ),
                bumper=mediatailor.CfnPlaybackConfiguration.BumperProperty(
                    end_url="endUrl",
                    start_url="startUrl"
                ),
                cdn_configuration=mediatailor.CfnPlaybackConfiguration.CdnConfigurationProperty(
                    ad_segment_url_prefix="adSegmentUrlPrefix",
                    content_segment_url_prefix="contentSegmentUrlPrefix"
                ),
                configuration_aliases={
                    "configuration_aliases_key": configuration_aliases
                },
                dash_configuration=mediatailor.CfnPlaybackConfiguration.DashConfigurationProperty(
                    manifest_endpoint_prefix="manifestEndpointPrefix",
                    mpd_location="mpdLocation",
                    origin_manifest_type="originManifestType"
                ),
                live_pre_roll_configuration=mediatailor.CfnPlaybackConfiguration.LivePreRollConfigurationProperty(
                    ad_decision_server_url="adDecisionServerUrl",
                    max_duration_seconds=123
                ),
                manifest_processing_rules=mediatailor.CfnPlaybackConfiguration.ManifestProcessingRulesProperty(
                    ad_marker_passthrough=mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty(
                        enabled=False
                    )
                ),
                personalization_threshold_seconds=123,
                slate_ad_url="slateAdUrl",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                transcode_profile_name="transcodeProfileName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPlaybackConfigurationProps.__init__)
            check_type(argname="argument ad_decision_server_url", value=ad_decision_server_url, expected_type=type_hints["ad_decision_server_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument video_content_source_url", value=video_content_source_url, expected_type=type_hints["video_content_source_url"])
            check_type(argname="argument avail_suppression", value=avail_suppression, expected_type=type_hints["avail_suppression"])
            check_type(argname="argument bumper", value=bumper, expected_type=type_hints["bumper"])
            check_type(argname="argument cdn_configuration", value=cdn_configuration, expected_type=type_hints["cdn_configuration"])
            check_type(argname="argument configuration_aliases", value=configuration_aliases, expected_type=type_hints["configuration_aliases"])
            check_type(argname="argument dash_configuration", value=dash_configuration, expected_type=type_hints["dash_configuration"])
            check_type(argname="argument live_pre_roll_configuration", value=live_pre_roll_configuration, expected_type=type_hints["live_pre_roll_configuration"])
            check_type(argname="argument manifest_processing_rules", value=manifest_processing_rules, expected_type=type_hints["manifest_processing_rules"])
            check_type(argname="argument personalization_threshold_seconds", value=personalization_threshold_seconds, expected_type=type_hints["personalization_threshold_seconds"])
            check_type(argname="argument slate_ad_url", value=slate_ad_url, expected_type=type_hints["slate_ad_url"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transcode_profile_name", value=transcode_profile_name, expected_type=type_hints["transcode_profile_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "ad_decision_server_url": ad_decision_server_url,
            "name": name,
            "video_content_source_url": video_content_source_url,
        }
        if avail_suppression is not None:
            self._values["avail_suppression"] = avail_suppression
        if bumper is not None:
            self._values["bumper"] = bumper
        if cdn_configuration is not None:
            self._values["cdn_configuration"] = cdn_configuration
        if configuration_aliases is not None:
            self._values["configuration_aliases"] = configuration_aliases
        if dash_configuration is not None:
            self._values["dash_configuration"] = dash_configuration
        if live_pre_roll_configuration is not None:
            self._values["live_pre_roll_configuration"] = live_pre_roll_configuration
        if manifest_processing_rules is not None:
            self._values["manifest_processing_rules"] = manifest_processing_rules
        if personalization_threshold_seconds is not None:
            self._values["personalization_threshold_seconds"] = personalization_threshold_seconds
        if slate_ad_url is not None:
            self._values["slate_ad_url"] = slate_ad_url
        if tags is not None:
            self._values["tags"] = tags
        if transcode_profile_name is not None:
            self._values["transcode_profile_name"] = transcode_profile_name

    @builtins.property
    def ad_decision_server_url(self) -> builtins.str:
        '''The URL for the ad decision server (ADS).

        This includes the specification of static parameters and placeholders for dynamic parameters. MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-addecisionserverurl
        '''
        result = self._values.get("ad_decision_server_url")
        assert result is not None, "Required property 'ad_decision_server_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The identifier for the playback configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def video_content_source_url(self) -> builtins.str:
        '''The URL prefix for the parent manifest for the stream, minus the asset ID.

        The maximum length is 512 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-videocontentsourceurl
        '''
        result = self._values.get("video_content_source_url")
        assert result is not None, "Required property 'video_content_source_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def avail_suppression(
        self,
    ) -> typing.Optional[typing.Union[CfnPlaybackConfiguration.AvailSuppressionProperty, _IResolvable_da3f097b]]:
        '''The configuration for avail suppression, also known as ad suppression.

        For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-availsuppression
        '''
        result = self._values.get("avail_suppression")
        return typing.cast(typing.Optional[typing.Union[CfnPlaybackConfiguration.AvailSuppressionProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def bumper(
        self,
    ) -> typing.Optional[typing.Union[CfnPlaybackConfiguration.BumperProperty, _IResolvable_da3f097b]]:
        '''The configuration for bumpers.

        Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-bumper
        '''
        result = self._values.get("bumper")
        return typing.cast(typing.Optional[typing.Union[CfnPlaybackConfiguration.BumperProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def cdn_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnPlaybackConfiguration.CdnConfigurationProperty, _IResolvable_da3f097b]]:
        '''The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration
        '''
        result = self._values.get("cdn_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnPlaybackConfiguration.CdnConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def configuration_aliases(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]]:
        '''The player parameters and aliases used as dynamic variables during session initialization.

        For more information, see `Domain Variables <https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domain.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-configurationaliases
        '''
        result = self._values.get("configuration_aliases")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]], result)

    @builtins.property
    def dash_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnPlaybackConfiguration.DashConfigurationProperty, _IResolvable_da3f097b]]:
        '''The configuration for DASH content.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration
        '''
        result = self._values.get("dash_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnPlaybackConfiguration.DashConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def live_pre_roll_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnPlaybackConfiguration.LivePreRollConfigurationProperty, _IResolvable_da3f097b]]:
        '''The configuration for pre-roll ad insertion.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration
        '''
        result = self._values.get("live_pre_roll_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnPlaybackConfiguration.LivePreRollConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def manifest_processing_rules(
        self,
    ) -> typing.Optional[typing.Union[CfnPlaybackConfiguration.ManifestProcessingRulesProperty, _IResolvable_da3f097b]]:
        '''The configuration for manifest processing rules.

        Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-manifestprocessingrules
        '''
        result = self._values.get("manifest_processing_rules")
        return typing.cast(typing.Optional[typing.Union[CfnPlaybackConfiguration.ManifestProcessingRulesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def personalization_threshold_seconds(self) -> typing.Optional[jsii.Number]:
        '''Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break.

        If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see `Ad Behavior in MediaTailor <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-personalizationthresholdseconds
        '''
        result = self._values.get("personalization_threshold_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def slate_ad_url(self) -> typing.Optional[builtins.str]:
        '''The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads.

        MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-slateadurl
        '''
        result = self._values.get("slate_ad_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the playback configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def transcode_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name that is used to associate this playback configuration with a custom transcode profile.

        This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-transcodeprofilename
        '''
        result = self._values.get("transcode_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlaybackConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPlaybackConfiguration",
    "CfnPlaybackConfigurationProps",
]

publication.publish()
