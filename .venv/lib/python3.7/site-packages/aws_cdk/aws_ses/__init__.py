'''
# Amazon Simple Email Service Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Email receiving

Create a receipt rule set with rules and actions (actions can be found in the
`@aws-cdk/aws-ses-actions` package):

```python
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_ses_actions as actions


bucket = s3.Bucket(self, "Bucket")
topic = sns.Topic(self, "Topic")

ses.ReceiptRuleSet(self, "RuleSet",
    rules=[ses.ReceiptRuleOptions(
        recipients=["hello@aws.com"],
        actions=[
            actions.AddHeader(
                name="X-Special-Header",
                value="aws"
            ),
            actions.S3(
                bucket=bucket,
                object_key_prefix="emails/",
                topic=topic
            )
        ]
    ), ses.ReceiptRuleOptions(
        recipients=["aws.com"],
        actions=[
            actions.Sns(
                topic=topic
            )
        ]
    )
    ]
)
```

Alternatively, rules can be added to a rule set:

```python
rule_set = ses.ReceiptRuleSet(self, "RuleSet")

aws_rule = rule_set.add_rule("Aws",
    recipients=["aws.com"]
)
```

And actions to rules:

```python
import aws_cdk.aws_ses_actions as actions

# aws_rule: ses.ReceiptRule
# topic: sns.Topic

aws_rule.add_action(actions.Sns(
    topic=topic
))
```

When using `addRule`, the new rule is added after the last added rule unless `after` is specified.

### Drop spams

A rule to drop spam can be added by setting `dropSpam` to `true`:

```python
ses.ReceiptRuleSet(self, "RuleSet",
    drop_spam=True
)
```

This will add a rule at the top of the rule set with a Lambda action that stops processing messages that have at least one spam indicator. See [Lambda Function Examples](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda-example-functions.html).

### Receipt filter

Create a receipt filter:

```python
ses.ReceiptFilter(self, "Filter",
    ip="1.2.3.4/16"
)
```

An allow list filter is also available:

```python
ses.AllowListReceiptFilter(self, "AllowList",
    ips=["10.0.0.0/16", "1.2.3.4/16"
    ]
)
```

This will first create a block all filter and then create allow filters for the listed ip addresses.

## Email sending

### Dedicated IP pools

When you create a new Amazon SES account, your emails are sent from IP addresses that are shared with other
Amazon SES users. For [an additional monthly charge](https://aws.amazon.com/ses/pricing/), you can lease
dedicated IP addresses that are reserved for your exclusive use.

Use the `DedicatedIpPool` construct to create a pool of dedicated IP addresses:

```python
ses.DedicatedIpPool(self, "Pool")
```

The pool can then be used in a configuration set.

### Configuration sets

Configuration sets are groups of rules that you can apply to your verified identities. A verified identity is
a domain, subdomain, or email address you use to send email through Amazon SES. When you apply a configuration
set to an email, all of the rules in that configuration set are applied to the email.

Use the `ConfigurationSet` construct to create a configuration set:

```python
# my_pool: ses.IDedicatedIpPool


ses.ConfigurationSet(self, "ConfigurationSet",
    custom_tracking_redirect_domain="track.cdk.dev",
    suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
    tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
    dedicated_ip_pool=my_pool
)
```

### Email identity

In Amazon SES, a verified identity is a domain or email address that you use to send or receive email. Before you
can send an email using Amazon SES, you must create and verify each identity that you're going to use as a `From`,
`Source`, `Sender`, or `Return-Path` address. Verifying an identity with Amazon SES confirms that you own it and
helps prevent unauthorized use.

To verify an identity for a hosted zone, you create an `EmailIdentity`:

```python
# Example automatically generated from non-compiling source. May contain errors.
# my_hosted_zone: route53.IPublicHostedZone


identity = ses.EmailIdentity(stack, "Identity",
    identity=ses.Identity.public_hosted_zone(my_hosted_zone),
    mail_from_domain="mail.cdk.dev"
)
```

By default, [Easy DKIM](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html) with
a 2048-bit DKIM key is used.

You can instead configure DKIM authentication by using your own public-private key pair. This process is known
as [Bring Your Own DKIM (BYODKIM)](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-bring-your-own.html):

```python
# Example automatically generated from non-compiling source. May contain errors.
# my_hosted_zone: route53.IPublicHostedZone


ses.EmailIdentity(stack, "Identity",
    identity=ses.Identity.public_hosted_zone(my_hosted_zone),
    dkim_identity=DkimIdentity.byo_dkim(
        private_key=SecretValue.secrets_manager("dkim-private-key"),
        public_key="...base64-encoded-public-key...",
        selector="selector"
    )
)
```

When using `publicHostedZone()` for the identity, all necessary Amazon Route 53 records are created automatically:

* CNAME records for Easy DKIM
* TXT record for BYOD DKIM
* MX and TXT records for the custom MAIL FROM

When working with `domain()`, records must be created manually:

```python
# Example automatically generated from non-compiling source. May contain errors.
identity = ses.EmailIdentity(stack, "Identity",
    identity=ses.Identity.domain("cdk.dev")
)

for record in identity.dkim_records:
    pass
```
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
    IResource as _IResource_c80c4260,
    Resource as _Resource_45bc6135,
    SecretValue as _SecretValue_3dd0ddae,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_route53 import IPublicHostedZone as _IPublicHostedZone_9b6e7da4


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.AddHeaderActionConfig",
    jsii_struct_bases=[],
    name_mapping={"header_name": "headerName", "header_value": "headerValue"},
)
class AddHeaderActionConfig:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
    ) -> None:
        '''AddHeaderAction configuration.

        :param header_name: The name of the header that you want to add to the incoming message.
        :param header_value: The content that you want to include in the header.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            add_header_action_config = ses.AddHeaderActionConfig(
                header_name="headerName",
                header_value="headerValue"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AddHeaderActionConfig.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header that you want to add to the incoming message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The content that you want to include in the header.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddHeaderActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AllowListReceiptFilter(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.AllowListReceiptFilter",
):
    '''An allow list receipt filter.

    :exampleMetadata: infused

    Example::

        ses.AllowListReceiptFilter(self, "AllowList",
            ips=["10.0.0.0/16", "1.2.3.4/16"
            ]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ips: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ips: A list of ip addresses or ranges to allow list.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AllowListReceiptFilter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AllowListReceiptFilterProps(ips=ips)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.AllowListReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={"ips": "ips"},
)
class AllowListReceiptFilterProps:
    def __init__(self, *, ips: typing.Sequence[builtins.str]) -> None:
        '''Construction properties for am AllowListReceiptFilter.

        :param ips: A list of ip addresses or ranges to allow list.

        :exampleMetadata: infused

        Example::

            ses.AllowListReceiptFilter(self, "AllowList",
                ips=["10.0.0.0/16", "1.2.3.4/16"
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AllowListReceiptFilterProps.__init__)
            check_type(argname="argument ips", value=ips, expected_type=type_hints["ips"])
        self._values: typing.Dict[str, typing.Any] = {
            "ips": ips,
        }

    @builtins.property
    def ips(self) -> typing.List[builtins.str]:
        '''A list of ip addresses or ranges to allow list.'''
        result = self._values.get("ips")
        assert result is not None, "Required property 'ips' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AllowListReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.BounceActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "message": "message",
        "sender": "sender",
        "smtp_reply_code": "smtpReplyCode",
        "status_code": "statusCode",
        "topic_arn": "topicArn",
    },
)
class BounceActionConfig:
    def __init__(
        self,
        *,
        message: builtins.str,
        sender: builtins.str,
        smtp_reply_code: builtins.str,
        status_code: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''BoundAction configuration.

        :param message: Human-readable text to include in the bounce message.
        :param sender: The email address of the sender of the bounced email. This is the address that the bounce message is sent from.
        :param smtp_reply_code: The SMTP reply code, as defined by RFC 5321.
        :param status_code: The SMTP enhanced status code, as defined by RFC 3463. Default: - No status code.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            bounce_action_config = ses.BounceActionConfig(
                message="message",
                sender="sender",
                smtp_reply_code="smtpReplyCode",
            
                # the properties below are optional
                status_code="statusCode",
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BounceActionConfig.__init__)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument sender", value=sender, expected_type=type_hints["sender"])
            check_type(argname="argument smtp_reply_code", value=smtp_reply_code, expected_type=type_hints["smtp_reply_code"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
            "sender": sender,
            "smtp_reply_code": smtp_reply_code,
        }
        if status_code is not None:
            self._values["status_code"] = status_code
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def message(self) -> builtins.str:
        '''Human-readable text to include in the bounce message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sender(self) -> builtins.str:
        '''The email address of the sender of the bounced email.

        This is the address that the bounce message is sent from.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender
        '''
        result = self._values.get("sender")
        assert result is not None, "Required property 'sender' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def smtp_reply_code(self) -> builtins.str:
        '''The SMTP reply code, as defined by RFC 5321.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode
        '''
        result = self._values.get("smtp_reply_code")
        assert result is not None, "Required property 'smtp_reply_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code(self) -> typing.Optional[builtins.str]:
        '''The SMTP enhanced status code, as defined by RFC 3463.

        :default: - No status code.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BounceActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ByoDkimOptions",
    jsii_struct_bases=[],
    name_mapping={
        "private_key": "privateKey",
        "selector": "selector",
        "public_key": "publicKey",
    },
)
class ByoDkimOptions:
    def __init__(
        self,
        *,
        private_key: _SecretValue_3dd0ddae,
        selector: builtins.str,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for BYO DKIM.

        :param private_key: The private key that's used to generate a DKIM signature.
        :param selector: A string that's used to identify a public key in the DNS configuration for a domain.
        :param public_key: The public key. If specified, a TXT record with the public key is created. Default: - the validation TXT record with the public key is not created

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_ses as ses
            
            # secret_value: cdk.SecretValue
            
            byo_dkim_options = ses.ByoDkimOptions(
                private_key=secret_value,
                selector="selector",
            
                # the properties below are optional
                public_key="publicKey"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ByoDkimOptions.__init__)
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "private_key": private_key,
            "selector": selector,
        }
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def private_key(self) -> _SecretValue_3dd0ddae:
        '''The private key that's used to generate a DKIM signature.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(_SecretValue_3dd0ddae, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''A string that's used to identify a public key in the DNS configuration for a domain.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''The public key.

        If specified, a TXT record with the public key is created.

        :default: - the validation TXT record with the public key is not created
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ByoDkimOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet",
):
    '''A CloudFormation ``AWS::SES::ConfigurationSet``.

    The name of the configuration set.

    Configuration sets let you create groups of rules that you can apply to the emails you send using Amazon SES. For more information about using configuration sets, see `Using Amazon SES Configuration Sets <https://docs.aws.amazon.com/ses/latest/dg/using-configuration-sets.html>`_ in the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/>`_ .

    :cloudformationResource: AWS::SES::ConfigurationSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_configuration_set = ses.CfnConfigurationSet(self, "MyCfnConfigurationSet",
            delivery_options=ses.CfnConfigurationSet.DeliveryOptionsProperty(
                sending_pool_name="sendingPoolName",
                tls_policy="tlsPolicy"
            ),
            name="name",
            reputation_options=ses.CfnConfigurationSet.ReputationOptionsProperty(
                reputation_metrics_enabled=False
            ),
            sending_options=ses.CfnConfigurationSet.SendingOptionsProperty(
                sending_enabled=False
            ),
            suppression_options=ses.CfnConfigurationSet.SuppressionOptionsProperty(
                suppressed_reasons=["suppressedReasons"]
            ),
            tracking_options=ses.CfnConfigurationSet.TrackingOptionsProperty(
                custom_redirect_domain="customRedirectDomain"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        delivery_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        reputation_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.ReputationOptionsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        sending_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.SendingOptionsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        suppression_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.SuppressionOptionsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tracking_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.TrackingOptionsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::SES::ConfigurationSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param delivery_options: ``AWS::SES::ConfigurationSet.DeliveryOptions``.
        :param name: The name of the configuration set. The name must meet the following requirements:. - Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). - Contain 64 characters or fewer.
        :param reputation_options: ``AWS::SES::ConfigurationSet.ReputationOptions``.
        :param sending_options: ``AWS::SES::ConfigurationSet.SendingOptions``.
        :param suppression_options: ``AWS::SES::ConfigurationSet.SuppressionOptions``.
        :param tracking_options: ``AWS::SES::ConfigurationSet.TrackingOptions``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConfigurationSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetProps(
            delivery_options=delivery_options,
            name=name,
            reputation_options=reputation_options,
            sending_options=sending_options,
            suppression_options=suppression_options,
            tracking_options=tracking_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConfigurationSet.inspect)
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
            type_hints = typing.get_type_hints(CfnConfigurationSet._render_properties)
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
    @jsii.member(jsii_name="deliveryOptions")
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.DeliveryOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-deliveryoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "deliveryOptions"))

    @delivery_options.setter
    def delivery_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConfigurationSet, "delivery_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration set. The name must meet the following requirements:.

        - Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
        - Contain 64 characters or fewer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConfigurationSet, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="reputationOptions")
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.ReputationOptionsProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.ReputationOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-reputationoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.ReputationOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "reputationOptions"))

    @reputation_options.setter
    def reputation_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.ReputationOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConfigurationSet, "reputation_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reputationOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sendingOptions")
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.SendingOptionsProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.SendingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-sendingoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.SendingOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "sendingOptions"))

    @sending_options.setter
    def sending_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.SendingOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConfigurationSet, "sending_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendingOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="suppressionOptions")
    def suppression_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.SuppressionOptionsProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.SuppressionOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-suppressionoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.SuppressionOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "suppressionOptions"))

    @suppression_options.setter
    def suppression_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.SuppressionOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConfigurationSet, "suppression_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppressionOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trackingOptions")
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.TrackingOptionsProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.TrackingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-trackingoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.TrackingOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "trackingOptions"))

    @tracking_options.setter
    def tracking_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.TrackingOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConfigurationSet, "tracking_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackingOptions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.DeliveryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sending_pool_name": "sendingPoolName",
            "tls_policy": "tlsPolicy",
        },
    )
    class DeliveryOptionsProperty:
        def __init__(
            self,
            *,
            sending_pool_name: typing.Optional[builtins.str] = None,
            tls_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param sending_pool_name: ``CfnConfigurationSet.DeliveryOptionsProperty.SendingPoolName``.
            :param tls_policy: ``CfnConfigurationSet.DeliveryOptionsProperty.TlsPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                delivery_options_property = ses.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName",
                    tls_policy="tlsPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSet.DeliveryOptionsProperty.__init__)
                check_type(argname="argument sending_pool_name", value=sending_pool_name, expected_type=type_hints["sending_pool_name"])
                check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
            self._values: typing.Dict[str, typing.Any] = {}
            if sending_pool_name is not None:
                self._values["sending_pool_name"] = sending_pool_name
            if tls_policy is not None:
                self._values["tls_policy"] = tls_policy

        @builtins.property
        def sending_pool_name(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSet.DeliveryOptionsProperty.SendingPoolName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-sendingpoolname
            '''
            result = self._values.get("sending_pool_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tls_policy(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSet.DeliveryOptionsProperty.TlsPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-tlspolicy
            '''
            result = self._values.get("tls_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeliveryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.ReputationOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"reputation_metrics_enabled": "reputationMetricsEnabled"},
    )
    class ReputationOptionsProperty:
        def __init__(
            self,
            *,
            reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param reputation_metrics_enabled: ``CfnConfigurationSet.ReputationOptionsProperty.ReputationMetricsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                reputation_options_property = ses.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSet.ReputationOptionsProperty.__init__)
                check_type(argname="argument reputation_metrics_enabled", value=reputation_metrics_enabled, expected_type=type_hints["reputation_metrics_enabled"])
            self._values: typing.Dict[str, typing.Any] = {}
            if reputation_metrics_enabled is not None:
                self._values["reputation_metrics_enabled"] = reputation_metrics_enabled

        @builtins.property
        def reputation_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnConfigurationSet.ReputationOptionsProperty.ReputationMetricsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html#cfn-ses-configurationset-reputationoptions-reputationmetricsenabled
            '''
            result = self._values.get("reputation_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReputationOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.SendingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_enabled": "sendingEnabled"},
    )
    class SendingOptionsProperty:
        def __init__(
            self,
            *,
            sending_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param sending_enabled: ``CfnConfigurationSet.SendingOptionsProperty.SendingEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                sending_options_property = ses.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSet.SendingOptionsProperty.__init__)
                check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
            self._values: typing.Dict[str, typing.Any] = {}
            if sending_enabled is not None:
                self._values["sending_enabled"] = sending_enabled

        @builtins.property
        def sending_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnConfigurationSet.SendingOptionsProperty.SendingEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html#cfn-ses-configurationset-sendingoptions-sendingenabled
            '''
            result = self._values.get("sending_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SendingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.SuppressionOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"suppressed_reasons": "suppressedReasons"},
    )
    class SuppressionOptionsProperty:
        def __init__(
            self,
            *,
            suppressed_reasons: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param suppressed_reasons: ``CfnConfigurationSet.SuppressionOptionsProperty.SuppressedReasons``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                suppression_options_property = ses.CfnConfigurationSet.SuppressionOptionsProperty(
                    suppressed_reasons=["suppressedReasons"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSet.SuppressionOptionsProperty.__init__)
                check_type(argname="argument suppressed_reasons", value=suppressed_reasons, expected_type=type_hints["suppressed_reasons"])
            self._values: typing.Dict[str, typing.Any] = {}
            if suppressed_reasons is not None:
                self._values["suppressed_reasons"] = suppressed_reasons

        @builtins.property
        def suppressed_reasons(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnConfigurationSet.SuppressionOptionsProperty.SuppressedReasons``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html#cfn-ses-configurationset-suppressionoptions-suppressedreasons
            '''
            result = self._values.get("suppressed_reasons")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SuppressionOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.TrackingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_redirect_domain": "customRedirectDomain"},
    )
    class TrackingOptionsProperty:
        def __init__(
            self,
            *,
            custom_redirect_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param custom_redirect_domain: ``CfnConfigurationSet.TrackingOptionsProperty.CustomRedirectDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                tracking_options_property = ses.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSet.TrackingOptionsProperty.__init__)
                check_type(argname="argument custom_redirect_domain", value=custom_redirect_domain, expected_type=type_hints["custom_redirect_domain"])
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_redirect_domain is not None:
                self._values["custom_redirect_domain"] = custom_redirect_domain

        @builtins.property
        def custom_redirect_domain(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSet.TrackingOptionsProperty.CustomRedirectDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html#cfn-ses-configurationset-trackingoptions-customredirectdomain
            '''
            result = self._values.get("custom_redirect_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrackingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationSetEventDestination(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination",
):
    '''A CloudFormation ``AWS::SES::ConfigurationSetEventDestination``.

    Specifies a configuration set event destination. An event destination is an AWS service that Amazon SES publishes email sending events to. When you specify an event destination, you provide one, and only one, destination. You can send event data to Amazon CloudWatch or Amazon Kinesis Data Firehose.
    .. epigraph::

       You can't specify Amazon SNS event destinations in CloudFormation templates.

    :cloudformationResource: AWS::SES::ConfigurationSetEventDestination
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_configuration_set_event_destination = ses.CfnConfigurationSetEventDestination(self, "MyCfnConfigurationSetEventDestination",
            configuration_set_name="configurationSetName",
            event_destination=ses.CfnConfigurationSetEventDestination.EventDestinationProperty(
                matching_event_types=["matchingEventTypes"],
        
                # the properties below are optional
                cloud_watch_destination=ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                ),
                enabled=False,
                kinesis_firehose_destination=ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                ),
                name="name",
                sns_destination=ses.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        configuration_set_name: builtins.str,
        event_destination: typing.Union[typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
    ) -> None:
        '''Create a new ``AWS::SES::ConfigurationSetEventDestination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param configuration_set_name: The name of the configuration set that contains the event destination.
        :param event_destination: The event destination object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConfigurationSetEventDestination.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetEventDestinationProps(
            configuration_set_name=configuration_set_name,
            event_destination=event_destination,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConfigurationSetEventDestination.inspect)
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
            type_hints = typing.get_type_hints(CfnConfigurationSetEventDestination._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set that contains the event destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-configurationsetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

    @configuration_set_name.setter
    def configuration_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConfigurationSetEventDestination, "configuration_set_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventDestination")
    def event_destination(
        self,
    ) -> typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", _IResolvable_da3f097b]:
        '''The event destination object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-eventdestination
        '''
        return typing.cast(typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", _IResolvable_da3f097b], jsii.get(self, "eventDestination"))

    @event_destination.setter
    def event_destination(
        self,
        value: typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnConfigurationSetEventDestination, "event_destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestination", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_configurations": "dimensionConfigurations"},
    )
    class CloudWatchDestinationProperty:
        def __init__(
            self,
            *,
            dimension_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Contains information associated with an Amazon CloudWatch event destination to which email sending events are published.

            Event destinations, such as Amazon CloudWatch, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param dimension_configurations: A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                cloud_watch_destination_property = ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSetEventDestination.CloudWatchDestinationProperty.__init__)
                check_type(argname="argument dimension_configurations", value=dimension_configurations, expected_type=type_hints["dimension_configurations"])
            self._values: typing.Dict[str, typing.Any] = {}
            if dimension_configurations is not None:
                self._values["dimension_configurations"] = dimension_configurations

        @builtins.property
        def dimension_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", _IResolvable_da3f097b]]]]:
            '''A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html#cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations
            '''
            result = self._values.get("dimension_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_dimension_value": "defaultDimensionValue",
            "dimension_name": "dimensionName",
            "dimension_value_source": "dimensionValueSource",
        },
    )
    class DimensionConfigurationProperty:
        def __init__(
            self,
            *,
            default_dimension_value: builtins.str,
            dimension_name: builtins.str,
            dimension_value_source: builtins.str,
        ) -> None:
            '''Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.

            For information about publishing email sending events to Amazon CloudWatch, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param default_dimension_value: The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must meet the following requirements: - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), at signs (@), or periods (.). - Contain 256 characters or fewer.
            :param dimension_name: The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must meet the following requirements: - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or colons (:). - Contain 256 characters or fewer.
            :param dimension_value_source: The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` / ``SendRawEmail`` API, specify ``messageTag`` . To use your own email headers, specify ``emailHeader`` . To put a custom tag on any link included in your email, specify ``linkTag`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                dimension_configuration_property = ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                    default_dimension_value="defaultDimensionValue",
                    dimension_name="dimensionName",
                    dimension_value_source="dimensionValueSource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSetEventDestination.DimensionConfigurationProperty.__init__)
                check_type(argname="argument default_dimension_value", value=default_dimension_value, expected_type=type_hints["default_dimension_value"])
                check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
                check_type(argname="argument dimension_value_source", value=dimension_value_source, expected_type=type_hints["dimension_value_source"])
            self._values: typing.Dict[str, typing.Any] = {
                "default_dimension_value": default_dimension_value,
                "dimension_name": dimension_name,
                "dimension_value_source": dimension_value_source,
            }

        @builtins.property
        def default_dimension_value(self) -> builtins.str:
            '''The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email.

            The default value must meet the following requirements:

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), at signs (@), or periods (.).
            - Contain 256 characters or fewer.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue
            '''
            result = self._values.get("default_dimension_value")
            assert result is not None, "Required property 'default_dimension_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_name(self) -> builtins.str:
            '''The name of an Amazon CloudWatch dimension associated with an email sending metric.

            The name must meet the following requirements:

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or colons (:).
            - Contain 256 characters or fewer.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname
            '''
            result = self._values.get("dimension_name")
            assert result is not None, "Required property 'dimension_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_value_source(self) -> builtins.str:
            '''The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch.

            To use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` / ``SendRawEmail`` API, specify ``messageTag`` . To use your own email headers, specify ``emailHeader`` . To put a custom tag on any link included in your email, specify ``linkTag`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource
            '''
            result = self._values.get("dimension_value_source")
            assert result is not None, "Required property 'dimension_value_source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.EventDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "matching_event_types": "matchingEventTypes",
            "cloud_watch_destination": "cloudWatchDestination",
            "enabled": "enabled",
            "kinesis_firehose_destination": "kinesisFirehoseDestination",
            "name": "name",
            "sns_destination": "snsDestination",
        },
    )
    class EventDestinationProperty:
        def __init__(
            self,
            *,
            matching_event_types: typing.Sequence[builtins.str],
            cloud_watch_destination: typing.Optional[typing.Union[typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            kinesis_firehose_destination: typing.Optional[typing.Union[typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            name: typing.Optional[builtins.str] = None,
            sns_destination: typing.Optional[typing.Union[typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains information about an event destination.

            .. epigraph::

               When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose or Amazon Simple Notification Service (Amazon SNS).

            Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param matching_event_types: The type of email sending events to publish to the event destination. - ``send`` - The call was successful and Amazon SES is attempting to deliver the email. - ``reject`` - Amazon SES determined that the email contained a virus and rejected it. - ``bounce`` - The recipient's mail server permanently rejected the email. This corresponds to a hard bounce. - ``complaint`` - The recipient marked the email as spam. - ``delivery`` - Amazon SES successfully delivered the email to the recipient's mail server. - ``open`` - The recipient received the email and opened it in their email client. - ``click`` - The recipient clicked one or more links in the email. - ``renderingFailure`` - Amazon SES did not send the email because of a template rendering issue.
            :param cloud_watch_destination: An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.
            :param enabled: Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to ``true`` to enable publishing to this destination; set to ``false`` to prevent publishing to this destination. The default value is ``false`` .
            :param kinesis_firehose_destination: An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.
            :param name: The name of the event destination. The name must meet the following requirements:. - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). - Contain 64 characters or fewer.
            :param sns_destination: ``CfnConfigurationSetEventDestination.EventDestinationProperty.SnsDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                event_destination_property = ses.CfnConfigurationSetEventDestination.EventDestinationProperty(
                    matching_event_types=["matchingEventTypes"],
                
                    # the properties below are optional
                    cloud_watch_destination=ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                        dimension_configurations=[ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                            default_dimension_value="defaultDimensionValue",
                            dimension_name="dimensionName",
                            dimension_value_source="dimensionValueSource"
                        )]
                    ),
                    enabled=False,
                    kinesis_firehose_destination=ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    name="name",
                    sns_destination=ses.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSetEventDestination.EventDestinationProperty.__init__)
                check_type(argname="argument matching_event_types", value=matching_event_types, expected_type=type_hints["matching_event_types"])
                check_type(argname="argument cloud_watch_destination", value=cloud_watch_destination, expected_type=type_hints["cloud_watch_destination"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument kinesis_firehose_destination", value=kinesis_firehose_destination, expected_type=type_hints["kinesis_firehose_destination"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sns_destination", value=sns_destination, expected_type=type_hints["sns_destination"])
            self._values: typing.Dict[str, typing.Any] = {
                "matching_event_types": matching_event_types,
            }
            if cloud_watch_destination is not None:
                self._values["cloud_watch_destination"] = cloud_watch_destination
            if enabled is not None:
                self._values["enabled"] = enabled
            if kinesis_firehose_destination is not None:
                self._values["kinesis_firehose_destination"] = kinesis_firehose_destination
            if name is not None:
                self._values["name"] = name
            if sns_destination is not None:
                self._values["sns_destination"] = sns_destination

        @builtins.property
        def matching_event_types(self) -> typing.List[builtins.str]:
            '''The type of email sending events to publish to the event destination.

            - ``send`` - The call was successful and Amazon SES is attempting to deliver the email.
            - ``reject`` - Amazon SES determined that the email contained a virus and rejected it.
            - ``bounce`` - The recipient's mail server permanently rejected the email. This corresponds to a hard bounce.
            - ``complaint`` - The recipient marked the email as spam.
            - ``delivery`` - Amazon SES successfully delivered the email to the recipient's mail server.
            - ``open`` - The recipient received the email and opened it in their email client.
            - ``click`` - The recipient clicked one or more links in the email.
            - ``renderingFailure`` - Amazon SES did not send the email because of a template rendering issue.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes
            '''
            result = self._values.get("matching_event_types")
            assert result is not None, "Required property 'matching_event_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def cloud_watch_destination(
            self,
        ) -> typing.Optional[typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", _IResolvable_da3f097b]]:
            '''An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination
            '''
            result = self._values.get("cloud_watch_destination")
            return typing.cast(typing.Optional[typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set.

            Set to ``true`` to enable publishing to this destination; set to ``false`` to prevent publishing to this destination. The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def kinesis_firehose_destination(
            self,
        ) -> typing.Optional[typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", _IResolvable_da3f097b]]:
            '''An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination
            '''
            result = self._values.get("kinesis_firehose_destination")
            return typing.cast(typing.Optional[typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the event destination. The name must meet the following requirements:.

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            - Contain 64 characters or fewer.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sns_destination(
            self,
        ) -> typing.Optional[typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", _IResolvable_da3f097b]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.SnsDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-snsdestination
            '''
            result = self._values.get("sns_destination")
            return typing.cast(typing.Optional[typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_arn": "deliveryStreamArn",
            "iam_role_arn": "iamRoleArn",
        },
    )
    class KinesisFirehoseDestinationProperty:
        def __init__(
            self,
            *,
            delivery_stream_arn: builtins.str,
            iam_role_arn: builtins.str,
        ) -> None:
            '''Contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

            Event destinations, such as Amazon Kinesis Firehose, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param delivery_stream_arn: The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.
            :param iam_role_arn: The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                kinesis_firehose_destination_property = ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.__init__)
                check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "delivery_stream_arn": delivery_stream_arn,
                "iam_role_arn": iam_role_arn,
            }

        @builtins.property
        def delivery_stream_arn(self) -> builtins.str:
            '''The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn
            '''
            result = self._values.get("delivery_stream_arn")
            assert result is not None, "Required property 'delivery_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.SnsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsDestinationProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''
            :param topic_arn: ``CfnConfigurationSetEventDestination.SnsDestinationProperty.TopicARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                sns_destination_property = ses.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnConfigurationSetEventDestination.SnsDestinationProperty.__init__)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.SnsDestinationProperty.TopicARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html#cfn-ses-configurationseteventdestination-snsdestination-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "event_destination": "eventDestination",
    },
)
class CfnConfigurationSetEventDestinationProps:
    def __init__(
        self,
        *,
        configuration_set_name: builtins.str,
        event_destination: typing.Union[typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSetEventDestination``.

        :param configuration_set_name: The name of the configuration set that contains the event destination.
        :param event_destination: The event destination object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_configuration_set_event_destination_props = ses.CfnConfigurationSetEventDestinationProps(
                configuration_set_name="configurationSetName",
                event_destination=ses.CfnConfigurationSetEventDestination.EventDestinationProperty(
                    matching_event_types=["matchingEventTypes"],
            
                    # the properties below are optional
                    cloud_watch_destination=ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                        dimension_configurations=[ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                            default_dimension_value="defaultDimensionValue",
                            dimension_name="dimensionName",
                            dimension_value_source="dimensionValueSource"
                        )]
                    ),
                    enabled=False,
                    kinesis_firehose_destination=ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    name="name",
                    sns_destination=ses.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConfigurationSetEventDestinationProps.__init__)
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "configuration_set_name": configuration_set_name,
            "event_destination": event_destination,
        }

    @builtins.property
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set that contains the event destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-configurationsetname
        '''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination(
        self,
    ) -> typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, _IResolvable_da3f097b]:
        '''The event destination object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-eventdestination
        '''
        result = self._values.get("event_destination")
        assert result is not None, "Required property 'event_destination' is missing"
        return typing.cast(typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, _IResolvable_da3f097b], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetEventDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_options": "deliveryOptions",
        "name": "name",
        "reputation_options": "reputationOptions",
        "sending_options": "sendingOptions",
        "suppression_options": "suppressionOptions",
        "tracking_options": "trackingOptions",
    },
)
class CfnConfigurationSetProps:
    def __init__(
        self,
        *,
        delivery_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        reputation_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        sending_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        suppression_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.SuppressionOptionsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tracking_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSet``.

        :param delivery_options: ``AWS::SES::ConfigurationSet.DeliveryOptions``.
        :param name: The name of the configuration set. The name must meet the following requirements:. - Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). - Contain 64 characters or fewer.
        :param reputation_options: ``AWS::SES::ConfigurationSet.ReputationOptions``.
        :param sending_options: ``AWS::SES::ConfigurationSet.SendingOptions``.
        :param suppression_options: ``AWS::SES::ConfigurationSet.SuppressionOptions``.
        :param tracking_options: ``AWS::SES::ConfigurationSet.TrackingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_configuration_set_props = ses.CfnConfigurationSetProps(
                delivery_options=ses.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName",
                    tls_policy="tlsPolicy"
                ),
                name="name",
                reputation_options=ses.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                ),
                sending_options=ses.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                ),
                suppression_options=ses.CfnConfigurationSet.SuppressionOptionsProperty(
                    suppressed_reasons=["suppressedReasons"]
                ),
                tracking_options=ses.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnConfigurationSetProps.__init__)
            check_type(argname="argument delivery_options", value=delivery_options, expected_type=type_hints["delivery_options"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument reputation_options", value=reputation_options, expected_type=type_hints["reputation_options"])
            check_type(argname="argument sending_options", value=sending_options, expected_type=type_hints["sending_options"])
            check_type(argname="argument suppression_options", value=suppression_options, expected_type=type_hints["suppression_options"])
            check_type(argname="argument tracking_options", value=tracking_options, expected_type=type_hints["tracking_options"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delivery_options is not None:
            self._values["delivery_options"] = delivery_options
        if name is not None:
            self._values["name"] = name
        if reputation_options is not None:
            self._values["reputation_options"] = reputation_options
        if sending_options is not None:
            self._values["sending_options"] = sending_options
        if suppression_options is not None:
            self._values["suppression_options"] = suppression_options
        if tracking_options is not None:
            self._values["tracking_options"] = tracking_options

    @builtins.property
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.DeliveryOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-deliveryoptions
        '''
        result = self._values.get("delivery_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration set. The name must meet the following requirements:.

        - Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
        - Contain 64 characters or fewer.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.ReputationOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-reputationoptions
        '''
        result = self._values.get("reputation_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.SendingOptionsProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.SendingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-sendingoptions
        '''
        result = self._values.get("sending_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.SendingOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def suppression_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.SuppressionOptionsProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.SuppressionOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-suppressionoptions
        '''
        result = self._values.get("suppression_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.SuppressionOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::ConfigurationSet.TrackingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-trackingoptions
        '''
        result = self._values.get("tracking_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnContactList(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnContactList",
):
    '''A CloudFormation ``AWS::SES::ContactList``.

    A list that contains contacts that have subscribed to a particular topic or topics.

    :cloudformationResource: AWS::SES::ContactList
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_contact_list = ses.CfnContactList(self, "MyCfnContactList",
            contact_list_name="contactListName",
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            topics=[ses.CfnContactList.TopicProperty(
                default_subscription_status="defaultSubscriptionStatus",
                display_name="displayName",
                topic_name="topicName",
        
                # the properties below are optional
                description="description"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        contact_list_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        topics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnContactList.TopicProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SES::ContactList``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param contact_list_name: The name of the contact list.
        :param description: A description of what the contact list is about.
        :param tags: The tags associated with a contact list.
        :param topics: An interest group, theme, or label within a list. A contact list can have multiple topics.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactList.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContactListProps(
            contact_list_name=contact_list_name,
            description=description,
            tags=tags,
            topics=topics,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactList.inspect)
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
            type_hints = typing.get_type_hints(CfnContactList._render_properties)
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
        '''The tags associated with a contact list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactListName")
    def contact_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the contact list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactListName"))

    @contact_list_name.setter
    def contact_list_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactList, "contact_list_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactListName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of what the contact list is about.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactList, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="topics")
    def topics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnContactList.TopicProperty", _IResolvable_da3f097b]]]]:
        '''An interest group, theme, or label within a list.

        A contact list can have multiple topics.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnContactList.TopicProperty", _IResolvable_da3f097b]]]], jsii.get(self, "topics"))

    @topics.setter
    def topics(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnContactList.TopicProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnContactList, "topics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topics", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnContactList.TopicProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_subscription_status": "defaultSubscriptionStatus",
            "display_name": "displayName",
            "topic_name": "topicName",
            "description": "description",
        },
    )
    class TopicProperty:
        def __init__(
            self,
            *,
            default_subscription_status: builtins.str,
            display_name: builtins.str,
            topic_name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An interest group, theme, or label within a list.

            Lists can have multiple topics.

            :param default_subscription_status: The default subscription status to be applied to a contact if the contact has not noted their preference for subscribing to a topic.
            :param display_name: The name of the topic the contact will see.
            :param topic_name: The name of the topic.
            :param description: A description of what the topic is about, which the contact will see.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                topic_property = ses.CfnContactList.TopicProperty(
                    default_subscription_status="defaultSubscriptionStatus",
                    display_name="displayName",
                    topic_name="topicName",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnContactList.TopicProperty.__init__)
                check_type(argname="argument default_subscription_status", value=default_subscription_status, expected_type=type_hints["default_subscription_status"])
                check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
                check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[str, typing.Any] = {
                "default_subscription_status": default_subscription_status,
                "display_name": display_name,
                "topic_name": topic_name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def default_subscription_status(self) -> builtins.str:
            '''The default subscription status to be applied to a contact if the contact has not noted their preference for subscribing to a topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-defaultsubscriptionstatus
            '''
            result = self._values.get("default_subscription_status")
            assert result is not None, "Required property 'default_subscription_status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def display_name(self) -> builtins.str:
            '''The name of the topic the contact will see.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-displayname
            '''
            result = self._values.get("display_name")
            assert result is not None, "Required property 'display_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_name(self) -> builtins.str:
            '''The name of the topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-topicname
            '''
            result = self._values.get("topic_name")
            assert result is not None, "Required property 'topic_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of what the topic is about, which the contact will see.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TopicProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnContactListProps",
    jsii_struct_bases=[],
    name_mapping={
        "contact_list_name": "contactListName",
        "description": "description",
        "tags": "tags",
        "topics": "topics",
    },
)
class CfnContactListProps:
    def __init__(
        self,
        *,
        contact_list_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        topics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnContactList.TopicProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContactList``.

        :param contact_list_name: The name of the contact list.
        :param description: A description of what the contact list is about.
        :param tags: The tags associated with a contact list.
        :param topics: An interest group, theme, or label within a list. A contact list can have multiple topics.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_contact_list_props = ses.CfnContactListProps(
                contact_list_name="contactListName",
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                topics=[ses.CfnContactList.TopicProperty(
                    default_subscription_status="defaultSubscriptionStatus",
                    display_name="displayName",
                    topic_name="topicName",
            
                    # the properties below are optional
                    description="description"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnContactListProps.__init__)
            check_type(argname="argument contact_list_name", value=contact_list_name, expected_type=type_hints["contact_list_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
        self._values: typing.Dict[str, typing.Any] = {}
        if contact_list_name is not None:
            self._values["contact_list_name"] = contact_list_name
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if topics is not None:
            self._values["topics"] = topics

    @builtins.property
    def contact_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the contact list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        '''
        result = self._values.get("contact_list_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of what the contact list is about.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with a contact list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def topics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnContactList.TopicProperty, _IResolvable_da3f097b]]]]:
        '''An interest group, theme, or label within a list.

        A contact list can have multiple topics.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnContactList.TopicProperty, _IResolvable_da3f097b]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDedicatedIpPool(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnDedicatedIpPool",
):
    '''A CloudFormation ``AWS::SES::DedicatedIpPool``.

    :cloudformationResource: AWS::SES::DedicatedIpPool
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_dedicated_ip_pool = ses.CfnDedicatedIpPool(self, "MyCfnDedicatedIpPool",
            pool_name="poolName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        pool_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SES::DedicatedIpPool``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param pool_name: ``AWS::SES::DedicatedIpPool.PoolName``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDedicatedIpPool.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDedicatedIpPoolProps(pool_name=pool_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDedicatedIpPool.inspect)
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
            type_hints = typing.get_type_hints(CfnDedicatedIpPool._render_properties)
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
    @jsii.member(jsii_name="poolName")
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::DedicatedIpPool.PoolName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-poolname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolName"))

    @pool_name.setter
    def pool_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDedicatedIpPool, "pool_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnDedicatedIpPoolProps",
    jsii_struct_bases=[],
    name_mapping={"pool_name": "poolName"},
)
class CfnDedicatedIpPoolProps:
    def __init__(self, *, pool_name: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``CfnDedicatedIpPool``.

        :param pool_name: ``AWS::SES::DedicatedIpPool.PoolName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_dedicated_ip_pool_props = ses.CfnDedicatedIpPoolProps(
                pool_name="poolName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDedicatedIpPoolProps.__init__)
            check_type(argname="argument pool_name", value=pool_name, expected_type=type_hints["pool_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if pool_name is not None:
            self._values["pool_name"] = pool_name

    @builtins.property
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::DedicatedIpPool.PoolName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-poolname
        '''
        result = self._values.get("pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDedicatedIpPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEmailIdentity(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity",
):
    '''A CloudFormation ``AWS::SES::EmailIdentity``.

    :cloudformationResource: AWS::SES::EmailIdentity
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_email_identity = ses.CfnEmailIdentity(self, "MyCfnEmailIdentity",
            email_identity="emailIdentity",
        
            # the properties below are optional
            configuration_set_attributes=ses.CfnEmailIdentity.ConfigurationSetAttributesProperty(
                configuration_set_name="configurationSetName"
            ),
            dkim_attributes=ses.CfnEmailIdentity.DkimAttributesProperty(
                signing_enabled=False
            ),
            dkim_signing_attributes=ses.CfnEmailIdentity.DkimSigningAttributesProperty(
                domain_signing_private_key="domainSigningPrivateKey",
                domain_signing_selector="domainSigningSelector",
                next_signing_key_length="nextSigningKeyLength"
            ),
            feedback_attributes=ses.CfnEmailIdentity.FeedbackAttributesProperty(
                email_forwarding_enabled=False
            ),
            mail_from_attributes=ses.CfnEmailIdentity.MailFromAttributesProperty(
                behavior_on_mx_failure="behaviorOnMxFailure",
                mail_from_domain="mailFromDomain"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        email_identity: builtins.str,
        configuration_set_attributes: typing.Optional[typing.Union[typing.Union["CfnEmailIdentity.ConfigurationSetAttributesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        dkim_attributes: typing.Optional[typing.Union[typing.Union["CfnEmailIdentity.DkimAttributesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        dkim_signing_attributes: typing.Optional[typing.Union[typing.Union["CfnEmailIdentity.DkimSigningAttributesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        feedback_attributes: typing.Optional[typing.Union[typing.Union["CfnEmailIdentity.FeedbackAttributesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        mail_from_attributes: typing.Optional[typing.Union[typing.Union["CfnEmailIdentity.MailFromAttributesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::SES::EmailIdentity``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param email_identity: ``AWS::SES::EmailIdentity.EmailIdentity``.
        :param configuration_set_attributes: ``AWS::SES::EmailIdentity.ConfigurationSetAttributes``.
        :param dkim_attributes: ``AWS::SES::EmailIdentity.DkimAttributes``.
        :param dkim_signing_attributes: ``AWS::SES::EmailIdentity.DkimSigningAttributes``.
        :param feedback_attributes: ``AWS::SES::EmailIdentity.FeedbackAttributes``.
        :param mail_from_attributes: ``AWS::SES::EmailIdentity.MailFromAttributes``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEmailIdentity.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEmailIdentityProps(
            email_identity=email_identity,
            configuration_set_attributes=configuration_set_attributes,
            dkim_attributes=dkim_attributes,
            dkim_signing_attributes=dkim_signing_attributes,
            feedback_attributes=feedback_attributes,
            mail_from_attributes=mail_from_attributes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEmailIdentity.inspect)
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
            type_hints = typing.get_type_hints(CfnEmailIdentity._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDkimDnsTokenName1")
    def attr_dkim_dns_token_name1(self) -> builtins.str:
        '''
        :cloudformationAttribute: DkimDNSTokenName1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenName1"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDkimDnsTokenName2")
    def attr_dkim_dns_token_name2(self) -> builtins.str:
        '''
        :cloudformationAttribute: DkimDNSTokenName2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenName2"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDkimDnsTokenName3")
    def attr_dkim_dns_token_name3(self) -> builtins.str:
        '''
        :cloudformationAttribute: DkimDNSTokenName3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenName3"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDkimDnsTokenValue1")
    def attr_dkim_dns_token_value1(self) -> builtins.str:
        '''
        :cloudformationAttribute: DkimDNSTokenValue1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenValue1"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDkimDnsTokenValue2")
    def attr_dkim_dns_token_value2(self) -> builtins.str:
        '''
        :cloudformationAttribute: DkimDNSTokenValue2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenValue2"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDkimDnsTokenValue3")
    def attr_dkim_dns_token_value3(self) -> builtins.str:
        '''
        :cloudformationAttribute: DkimDNSTokenValue3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenValue3"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="emailIdentity")
    def email_identity(self) -> builtins.str:
        '''``AWS::SES::EmailIdentity.EmailIdentity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-emailidentity
        '''
        return typing.cast(builtins.str, jsii.get(self, "emailIdentity"))

    @email_identity.setter
    def email_identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEmailIdentity, "email_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailIdentity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationSetAttributes")
    def configuration_set_attributes(
        self,
    ) -> typing.Optional[typing.Union["CfnEmailIdentity.ConfigurationSetAttributesProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.ConfigurationSetAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-configurationsetattributes
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEmailIdentity.ConfigurationSetAttributesProperty", _IResolvable_da3f097b]], jsii.get(self, "configurationSetAttributes"))

    @configuration_set_attributes.setter
    def configuration_set_attributes(
        self,
        value: typing.Optional[typing.Union["CfnEmailIdentity.ConfigurationSetAttributesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEmailIdentity, "configuration_set_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSetAttributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimAttributes")
    def dkim_attributes(
        self,
    ) -> typing.Optional[typing.Union["CfnEmailIdentity.DkimAttributesProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.DkimAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimattributes
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEmailIdentity.DkimAttributesProperty", _IResolvable_da3f097b]], jsii.get(self, "dkimAttributes"))

    @dkim_attributes.setter
    def dkim_attributes(
        self,
        value: typing.Optional[typing.Union["CfnEmailIdentity.DkimAttributesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEmailIdentity, "dkim_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dkimAttributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimSigningAttributes")
    def dkim_signing_attributes(
        self,
    ) -> typing.Optional[typing.Union["CfnEmailIdentity.DkimSigningAttributesProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.DkimSigningAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimsigningattributes
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEmailIdentity.DkimSigningAttributesProperty", _IResolvable_da3f097b]], jsii.get(self, "dkimSigningAttributes"))

    @dkim_signing_attributes.setter
    def dkim_signing_attributes(
        self,
        value: typing.Optional[typing.Union["CfnEmailIdentity.DkimSigningAttributesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEmailIdentity, "dkim_signing_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dkimSigningAttributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="feedbackAttributes")
    def feedback_attributes(
        self,
    ) -> typing.Optional[typing.Union["CfnEmailIdentity.FeedbackAttributesProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.FeedbackAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-feedbackattributes
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEmailIdentity.FeedbackAttributesProperty", _IResolvable_da3f097b]], jsii.get(self, "feedbackAttributes"))

    @feedback_attributes.setter
    def feedback_attributes(
        self,
        value: typing.Optional[typing.Union["CfnEmailIdentity.FeedbackAttributesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEmailIdentity, "feedback_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "feedbackAttributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mailFromAttributes")
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union["CfnEmailIdentity.MailFromAttributesProperty", _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.MailFromAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-mailfromattributes
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEmailIdentity.MailFromAttributesProperty", _IResolvable_da3f097b]], jsii.get(self, "mailFromAttributes"))

    @mail_from_attributes.setter
    def mail_from_attributes(
        self,
        value: typing.Optional[typing.Union["CfnEmailIdentity.MailFromAttributesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEmailIdentity, "mail_from_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mailFromAttributes", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.ConfigurationSetAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"configuration_set_name": "configurationSetName"},
    )
    class ConfigurationSetAttributesProperty:
        def __init__(
            self,
            *,
            configuration_set_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param configuration_set_name: ``CfnEmailIdentity.ConfigurationSetAttributesProperty.ConfigurationSetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                configuration_set_attributes_property = ses.CfnEmailIdentity.ConfigurationSetAttributesProperty(
                    configuration_set_name="configurationSetName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnEmailIdentity.ConfigurationSetAttributesProperty.__init__)
                check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if configuration_set_name is not None:
                self._values["configuration_set_name"] = configuration_set_name

        @builtins.property
        def configuration_set_name(self) -> typing.Optional[builtins.str]:
            '''``CfnEmailIdentity.ConfigurationSetAttributesProperty.ConfigurationSetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html#cfn-ses-emailidentity-configurationsetattributes-configurationsetname
            '''
            result = self._values.get("configuration_set_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationSetAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.DkimAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"signing_enabled": "signingEnabled"},
    )
    class DkimAttributesProperty:
        def __init__(
            self,
            *,
            signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param signing_enabled: ``CfnEmailIdentity.DkimAttributesProperty.SigningEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                dkim_attributes_property = ses.CfnEmailIdentity.DkimAttributesProperty(
                    signing_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnEmailIdentity.DkimAttributesProperty.__init__)
                check_type(argname="argument signing_enabled", value=signing_enabled, expected_type=type_hints["signing_enabled"])
            self._values: typing.Dict[str, typing.Any] = {}
            if signing_enabled is not None:
                self._values["signing_enabled"] = signing_enabled

        @builtins.property
        def signing_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnEmailIdentity.DkimAttributesProperty.SigningEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html#cfn-ses-emailidentity-dkimattributes-signingenabled
            '''
            result = self._values.get("signing_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DkimAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.DkimSigningAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "domain_signing_private_key": "domainSigningPrivateKey",
            "domain_signing_selector": "domainSigningSelector",
            "next_signing_key_length": "nextSigningKeyLength",
        },
    )
    class DkimSigningAttributesProperty:
        def __init__(
            self,
            *,
            domain_signing_private_key: typing.Optional[builtins.str] = None,
            domain_signing_selector: typing.Optional[builtins.str] = None,
            next_signing_key_length: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param domain_signing_private_key: ``CfnEmailIdentity.DkimSigningAttributesProperty.DomainSigningPrivateKey``.
            :param domain_signing_selector: ``CfnEmailIdentity.DkimSigningAttributesProperty.DomainSigningSelector``.
            :param next_signing_key_length: ``CfnEmailIdentity.DkimSigningAttributesProperty.NextSigningKeyLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                dkim_signing_attributes_property = ses.CfnEmailIdentity.DkimSigningAttributesProperty(
                    domain_signing_private_key="domainSigningPrivateKey",
                    domain_signing_selector="domainSigningSelector",
                    next_signing_key_length="nextSigningKeyLength"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnEmailIdentity.DkimSigningAttributesProperty.__init__)
                check_type(argname="argument domain_signing_private_key", value=domain_signing_private_key, expected_type=type_hints["domain_signing_private_key"])
                check_type(argname="argument domain_signing_selector", value=domain_signing_selector, expected_type=type_hints["domain_signing_selector"])
                check_type(argname="argument next_signing_key_length", value=next_signing_key_length, expected_type=type_hints["next_signing_key_length"])
            self._values: typing.Dict[str, typing.Any] = {}
            if domain_signing_private_key is not None:
                self._values["domain_signing_private_key"] = domain_signing_private_key
            if domain_signing_selector is not None:
                self._values["domain_signing_selector"] = domain_signing_selector
            if next_signing_key_length is not None:
                self._values["next_signing_key_length"] = next_signing_key_length

        @builtins.property
        def domain_signing_private_key(self) -> typing.Optional[builtins.str]:
            '''``CfnEmailIdentity.DkimSigningAttributesProperty.DomainSigningPrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningprivatekey
            '''
            result = self._values.get("domain_signing_private_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def domain_signing_selector(self) -> typing.Optional[builtins.str]:
            '''``CfnEmailIdentity.DkimSigningAttributesProperty.DomainSigningSelector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningselector
            '''
            result = self._values.get("domain_signing_selector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next_signing_key_length(self) -> typing.Optional[builtins.str]:
            '''``CfnEmailIdentity.DkimSigningAttributesProperty.NextSigningKeyLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-nextsigningkeylength
            '''
            result = self._values.get("next_signing_key_length")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DkimSigningAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.FeedbackAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"email_forwarding_enabled": "emailForwardingEnabled"},
    )
    class FeedbackAttributesProperty:
        def __init__(
            self,
            *,
            email_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param email_forwarding_enabled: ``CfnEmailIdentity.FeedbackAttributesProperty.EmailForwardingEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                feedback_attributes_property = ses.CfnEmailIdentity.FeedbackAttributesProperty(
                    email_forwarding_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnEmailIdentity.FeedbackAttributesProperty.__init__)
                check_type(argname="argument email_forwarding_enabled", value=email_forwarding_enabled, expected_type=type_hints["email_forwarding_enabled"])
            self._values: typing.Dict[str, typing.Any] = {}
            if email_forwarding_enabled is not None:
                self._values["email_forwarding_enabled"] = email_forwarding_enabled

        @builtins.property
        def email_forwarding_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnEmailIdentity.FeedbackAttributesProperty.EmailForwardingEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html#cfn-ses-emailidentity-feedbackattributes-emailforwardingenabled
            '''
            result = self._values.get("email_forwarding_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FeedbackAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.MailFromAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "behavior_on_mx_failure": "behaviorOnMxFailure",
            "mail_from_domain": "mailFromDomain",
        },
    )
    class MailFromAttributesProperty:
        def __init__(
            self,
            *,
            behavior_on_mx_failure: typing.Optional[builtins.str] = None,
            mail_from_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param behavior_on_mx_failure: ``CfnEmailIdentity.MailFromAttributesProperty.BehaviorOnMxFailure``.
            :param mail_from_domain: ``CfnEmailIdentity.MailFromAttributesProperty.MailFromDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                mail_from_attributes_property = ses.CfnEmailIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnEmailIdentity.MailFromAttributesProperty.__init__)
                check_type(argname="argument behavior_on_mx_failure", value=behavior_on_mx_failure, expected_type=type_hints["behavior_on_mx_failure"])
                check_type(argname="argument mail_from_domain", value=mail_from_domain, expected_type=type_hints["mail_from_domain"])
            self._values: typing.Dict[str, typing.Any] = {}
            if behavior_on_mx_failure is not None:
                self._values["behavior_on_mx_failure"] = behavior_on_mx_failure
            if mail_from_domain is not None:
                self._values["mail_from_domain"] = mail_from_domain

        @builtins.property
        def behavior_on_mx_failure(self) -> typing.Optional[builtins.str]:
            '''``CfnEmailIdentity.MailFromAttributesProperty.BehaviorOnMxFailure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-behavioronmxfailure
            '''
            result = self._values.get("behavior_on_mx_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mail_from_domain(self) -> typing.Optional[builtins.str]:
            '''``CfnEmailIdentity.MailFromAttributesProperty.MailFromDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-mailfromdomain
            '''
            result = self._values.get("mail_from_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MailFromAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "email_identity": "emailIdentity",
        "configuration_set_attributes": "configurationSetAttributes",
        "dkim_attributes": "dkimAttributes",
        "dkim_signing_attributes": "dkimSigningAttributes",
        "feedback_attributes": "feedbackAttributes",
        "mail_from_attributes": "mailFromAttributes",
    },
)
class CfnEmailIdentityProps:
    def __init__(
        self,
        *,
        email_identity: builtins.str,
        configuration_set_attributes: typing.Optional[typing.Union[typing.Union[CfnEmailIdentity.ConfigurationSetAttributesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        dkim_attributes: typing.Optional[typing.Union[typing.Union[CfnEmailIdentity.DkimAttributesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        dkim_signing_attributes: typing.Optional[typing.Union[typing.Union[CfnEmailIdentity.DkimSigningAttributesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        feedback_attributes: typing.Optional[typing.Union[typing.Union[CfnEmailIdentity.FeedbackAttributesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        mail_from_attributes: typing.Optional[typing.Union[typing.Union[CfnEmailIdentity.MailFromAttributesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEmailIdentity``.

        :param email_identity: ``AWS::SES::EmailIdentity.EmailIdentity``.
        :param configuration_set_attributes: ``AWS::SES::EmailIdentity.ConfigurationSetAttributes``.
        :param dkim_attributes: ``AWS::SES::EmailIdentity.DkimAttributes``.
        :param dkim_signing_attributes: ``AWS::SES::EmailIdentity.DkimSigningAttributes``.
        :param feedback_attributes: ``AWS::SES::EmailIdentity.FeedbackAttributes``.
        :param mail_from_attributes: ``AWS::SES::EmailIdentity.MailFromAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_email_identity_props = ses.CfnEmailIdentityProps(
                email_identity="emailIdentity",
            
                # the properties below are optional
                configuration_set_attributes=ses.CfnEmailIdentity.ConfigurationSetAttributesProperty(
                    configuration_set_name="configurationSetName"
                ),
                dkim_attributes=ses.CfnEmailIdentity.DkimAttributesProperty(
                    signing_enabled=False
                ),
                dkim_signing_attributes=ses.CfnEmailIdentity.DkimSigningAttributesProperty(
                    domain_signing_private_key="domainSigningPrivateKey",
                    domain_signing_selector="domainSigningSelector",
                    next_signing_key_length="nextSigningKeyLength"
                ),
                feedback_attributes=ses.CfnEmailIdentity.FeedbackAttributesProperty(
                    email_forwarding_enabled=False
                ),
                mail_from_attributes=ses.CfnEmailIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEmailIdentityProps.__init__)
            check_type(argname="argument email_identity", value=email_identity, expected_type=type_hints["email_identity"])
            check_type(argname="argument configuration_set_attributes", value=configuration_set_attributes, expected_type=type_hints["configuration_set_attributes"])
            check_type(argname="argument dkim_attributes", value=dkim_attributes, expected_type=type_hints["dkim_attributes"])
            check_type(argname="argument dkim_signing_attributes", value=dkim_signing_attributes, expected_type=type_hints["dkim_signing_attributes"])
            check_type(argname="argument feedback_attributes", value=feedback_attributes, expected_type=type_hints["feedback_attributes"])
            check_type(argname="argument mail_from_attributes", value=mail_from_attributes, expected_type=type_hints["mail_from_attributes"])
        self._values: typing.Dict[str, typing.Any] = {
            "email_identity": email_identity,
        }
        if configuration_set_attributes is not None:
            self._values["configuration_set_attributes"] = configuration_set_attributes
        if dkim_attributes is not None:
            self._values["dkim_attributes"] = dkim_attributes
        if dkim_signing_attributes is not None:
            self._values["dkim_signing_attributes"] = dkim_signing_attributes
        if feedback_attributes is not None:
            self._values["feedback_attributes"] = feedback_attributes
        if mail_from_attributes is not None:
            self._values["mail_from_attributes"] = mail_from_attributes

    @builtins.property
    def email_identity(self) -> builtins.str:
        '''``AWS::SES::EmailIdentity.EmailIdentity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-emailidentity
        '''
        result = self._values.get("email_identity")
        assert result is not None, "Required property 'email_identity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_set_attributes(
        self,
    ) -> typing.Optional[typing.Union[CfnEmailIdentity.ConfigurationSetAttributesProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.ConfigurationSetAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-configurationsetattributes
        '''
        result = self._values.get("configuration_set_attributes")
        return typing.cast(typing.Optional[typing.Union[CfnEmailIdentity.ConfigurationSetAttributesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def dkim_attributes(
        self,
    ) -> typing.Optional[typing.Union[CfnEmailIdentity.DkimAttributesProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.DkimAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimattributes
        '''
        result = self._values.get("dkim_attributes")
        return typing.cast(typing.Optional[typing.Union[CfnEmailIdentity.DkimAttributesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def dkim_signing_attributes(
        self,
    ) -> typing.Optional[typing.Union[CfnEmailIdentity.DkimSigningAttributesProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.DkimSigningAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimsigningattributes
        '''
        result = self._values.get("dkim_signing_attributes")
        return typing.cast(typing.Optional[typing.Union[CfnEmailIdentity.DkimSigningAttributesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def feedback_attributes(
        self,
    ) -> typing.Optional[typing.Union[CfnEmailIdentity.FeedbackAttributesProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.FeedbackAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-feedbackattributes
        '''
        result = self._values.get("feedback_attributes")
        return typing.cast(typing.Optional[typing.Union[CfnEmailIdentity.FeedbackAttributesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[CfnEmailIdentity.MailFromAttributesProperty, _IResolvable_da3f097b]]:
        '''``AWS::SES::EmailIdentity.MailFromAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-mailfromattributes
        '''
        result = self._values.get("mail_from_attributes")
        return typing.cast(typing.Optional[typing.Union[CfnEmailIdentity.MailFromAttributesProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEmailIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnReceiptFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptFilter",
):
    '''A CloudFormation ``AWS::SES::ReceiptFilter``.

    Specify a new IP address filter. You use IP address filters when you receive email with Amazon SES.

    :cloudformationResource: AWS::SES::ReceiptFilter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_receipt_filter = ses.CfnReceiptFilter(self, "MyCfnReceiptFilter",
            filter=ses.CfnReceiptFilter.FilterProperty(
                ip_filter=ses.CfnReceiptFilter.IpFilterProperty(
                    cidr="cidr",
                    policy="policy"
                ),
        
                # the properties below are optional
                name="name"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        filter: typing.Union[typing.Union["CfnReceiptFilter.FilterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
    ) -> None:
        '''Create a new ``AWS::SES::ReceiptFilter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param filter: A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptFilter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReceiptFilterProps(filter=filter)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptFilter.inspect)
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
            type_hints = typing.get_type_hints(CfnReceiptFilter._render_properties)
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
    @jsii.member(jsii_name="filter")
    def filter(
        self,
    ) -> typing.Union["CfnReceiptFilter.FilterProperty", _IResolvable_da3f097b]:
        '''A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html#cfn-ses-receiptfilter-filter
        '''
        return typing.cast(typing.Union["CfnReceiptFilter.FilterProperty", _IResolvable_da3f097b], jsii.get(self, "filter"))

    @filter.setter
    def filter(
        self,
        value: typing.Union["CfnReceiptFilter.FilterProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnReceiptFilter, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptFilter.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"ip_filter": "ipFilter", "name": "name"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            ip_filter: typing.Union[typing.Union["CfnReceiptFilter.IpFilterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies an IP address filter.

            :param ip_filter: A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.
            :param name: The name of the IP address filter. The name must meet the following requirements:. - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). - Start and end with a letter or number. - Contain 64 characters or fewer.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                filter_property = ses.CfnReceiptFilter.FilterProperty(
                    ip_filter=ses.CfnReceiptFilter.IpFilterProperty(
                        cidr="cidr",
                        policy="policy"
                    ),
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptFilter.FilterProperty.__init__)
                check_type(argname="argument ip_filter", value=ip_filter, expected_type=type_hints["ip_filter"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "ip_filter": ip_filter,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def ip_filter(
            self,
        ) -> typing.Union["CfnReceiptFilter.IpFilterProperty", _IResolvable_da3f097b]:
            '''A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-ipfilter
            '''
            result = self._values.get("ip_filter")
            assert result is not None, "Required property 'ip_filter' is missing"
            return typing.cast(typing.Union["CfnReceiptFilter.IpFilterProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the IP address filter. The name must meet the following requirements:.

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            - Start and end with a letter or number.
            - Contain 64 characters or fewer.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptFilter.IpFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr": "cidr", "policy": "policy"},
    )
    class IpFilterProperty:
        def __init__(self, *, cidr: builtins.str, policy: builtins.str) -> None:
            '''A receipt IP address filter enables you to specify whether to accept or reject mail originating from an IP address or range of IP addresses.

            For information about setting up IP address filters, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html>`_ .

            :param cidr: A single IP address or a range of IP addresses to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see `RFC 2317 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc2317>`_ .
            :param policy: Indicates whether to block or allow incoming mail from the specified IP addresses.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                ip_filter_property = ses.CfnReceiptFilter.IpFilterProperty(
                    cidr="cidr",
                    policy="policy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptFilter.IpFilterProperty.__init__)
                check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
                check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            self._values: typing.Dict[str, typing.Any] = {
                "cidr": cidr,
                "policy": policy,
            }

        @builtins.property
        def cidr(self) -> builtins.str:
            '''A single IP address or a range of IP addresses to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation.

            An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see `RFC 2317 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc2317>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-cidr
            '''
            result = self._values.get("cidr")
            assert result is not None, "Required property 'cidr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def policy(self) -> builtins.str:
            '''Indicates whether to block or allow incoming mail from the specified IP addresses.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-policy
            '''
            result = self._values.get("policy")
            assert result is not None, "Required property 'policy' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={"filter": "filter"},
)
class CfnReceiptFilterProps:
    def __init__(
        self,
        *,
        filter: typing.Union[typing.Union[CfnReceiptFilter.FilterProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
    ) -> None:
        '''Properties for defining a ``CfnReceiptFilter``.

        :param filter: A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_receipt_filter_props = ses.CfnReceiptFilterProps(
                filter=ses.CfnReceiptFilter.FilterProperty(
                    ip_filter=ses.CfnReceiptFilter.IpFilterProperty(
                        cidr="cidr",
                        policy="policy"
                    ),
            
                    # the properties below are optional
                    name="name"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptFilterProps.__init__)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
        }

    @builtins.property
    def filter(
        self,
    ) -> typing.Union[CfnReceiptFilter.FilterProperty, _IResolvable_da3f097b]:
        '''A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html#cfn-ses-receiptfilter-filter
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Union[CfnReceiptFilter.FilterProperty, _IResolvable_da3f097b], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnReceiptRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule",
):
    '''A CloudFormation ``AWS::SES::ReceiptRule``.

    Specifies a receipt rule.

    :cloudformationResource: AWS::SES::ReceiptRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_receipt_rule = ses.CfnReceiptRule(self, "MyCfnReceiptRule",
            rule=ses.CfnReceiptRule.RuleProperty(
                actions=[ses.CfnReceiptRule.ActionProperty(
                    add_header_action=ses.CfnReceiptRule.AddHeaderActionProperty(
                        header_name="headerName",
                        header_value="headerValue"
                    ),
                    bounce_action=ses.CfnReceiptRule.BounceActionProperty(
                        message="message",
                        sender="sender",
                        smtp_reply_code="smtpReplyCode",
        
                        # the properties below are optional
                        status_code="statusCode",
                        topic_arn="topicArn"
                    ),
                    lambda_action=ses.CfnReceiptRule.LambdaActionProperty(
                        function_arn="functionArn",
        
                        # the properties below are optional
                        invocation_type="invocationType",
                        topic_arn="topicArn"
                    ),
                    s3_action=ses.CfnReceiptRule.S3ActionProperty(
                        bucket_name="bucketName",
        
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn",
                        object_key_prefix="objectKeyPrefix",
                        topic_arn="topicArn"
                    ),
                    sns_action=ses.CfnReceiptRule.SNSActionProperty(
                        encoding="encoding",
                        topic_arn="topicArn"
                    ),
                    stop_action=ses.CfnReceiptRule.StopActionProperty(
                        scope="scope",
        
                        # the properties below are optional
                        topic_arn="topicArn"
                    ),
                    workmail_action=ses.CfnReceiptRule.WorkmailActionProperty(
                        organization_arn="organizationArn",
        
                        # the properties below are optional
                        topic_arn="topicArn"
                    )
                )],
                enabled=False,
                name="name",
                recipients=["recipients"],
                scan_enabled=False,
                tls_policy="tlsPolicy"
            ),
            rule_set_name="ruleSetName",
        
            # the properties below are optional
            after="after"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        rule: typing.Union[typing.Union["CfnReceiptRule.RuleProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        rule_set_name: builtins.str,
        after: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SES::ReceiptRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param rule: A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.
        :param rule_set_name: The name of the rule set where the receipt rule is added.
        :param after: The name of an existing rule after which the new rule is placed. If this parameter is null, the new rule is inserted at the beginning of the rule list.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReceiptRuleProps(
            rule=rule, rule_set_name=rule_set_name, after=after
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptRule.inspect)
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
            type_hints = typing.get_type_hints(CfnReceiptRule._render_properties)
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
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union["CfnReceiptRule.RuleProperty", _IResolvable_da3f097b]:
        '''A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rule
        '''
        return typing.cast(typing.Union["CfnReceiptRule.RuleProperty", _IResolvable_da3f097b], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union["CfnReceiptRule.RuleProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnReceiptRule, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> builtins.str:
        '''The name of the rule set where the receipt rule is added.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rulesetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "ruleSetName"))

    @rule_set_name.setter
    def rule_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnReceiptRule, "rule_set_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="after")
    def after(self) -> typing.Optional[builtins.str]:
        '''The name of an existing rule after which the new rule is placed.

        If this parameter is null, the new rule is inserted at the beginning of the rule list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-after
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "after"))

    @after.setter
    def after(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnReceiptRule, "after").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "after", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_header_action": "addHeaderAction",
            "bounce_action": "bounceAction",
            "lambda_action": "lambdaAction",
            "s3_action": "s3Action",
            "sns_action": "snsAction",
            "stop_action": "stopAction",
            "workmail_action": "workmailAction",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            add_header_action: typing.Optional[typing.Union[typing.Union["CfnReceiptRule.AddHeaderActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            bounce_action: typing.Optional[typing.Union[typing.Union["CfnReceiptRule.BounceActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            lambda_action: typing.Optional[typing.Union[typing.Union["CfnReceiptRule.LambdaActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            s3_action: typing.Optional[typing.Union[typing.Union["CfnReceiptRule.S3ActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            sns_action: typing.Optional[typing.Union[typing.Union["CfnReceiptRule.SNSActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            stop_action: typing.Optional[typing.Union[typing.Union["CfnReceiptRule.StopActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            workmail_action: typing.Optional[typing.Union[typing.Union["CfnReceiptRule.WorkmailActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own.

            An instance of this data type can represent only one action.

            For information about setting up receipt rules, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html>`_ .

            :param add_header_action: Adds a header to the received email.
            :param bounce_action: Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
            :param lambda_action: Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
            :param s3_action: Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.
            :param sns_action: Publishes the email content within a notification to Amazon SNS.
            :param stop_action: Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
            :param workmail_action: Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                action_property = ses.CfnReceiptRule.ActionProperty(
                    add_header_action=ses.CfnReceiptRule.AddHeaderActionProperty(
                        header_name="headerName",
                        header_value="headerValue"
                    ),
                    bounce_action=ses.CfnReceiptRule.BounceActionProperty(
                        message="message",
                        sender="sender",
                        smtp_reply_code="smtpReplyCode",
                
                        # the properties below are optional
                        status_code="statusCode",
                        topic_arn="topicArn"
                    ),
                    lambda_action=ses.CfnReceiptRule.LambdaActionProperty(
                        function_arn="functionArn",
                
                        # the properties below are optional
                        invocation_type="invocationType",
                        topic_arn="topicArn"
                    ),
                    s3_action=ses.CfnReceiptRule.S3ActionProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn",
                        object_key_prefix="objectKeyPrefix",
                        topic_arn="topicArn"
                    ),
                    sns_action=ses.CfnReceiptRule.SNSActionProperty(
                        encoding="encoding",
                        topic_arn="topicArn"
                    ),
                    stop_action=ses.CfnReceiptRule.StopActionProperty(
                        scope="scope",
                
                        # the properties below are optional
                        topic_arn="topicArn"
                    ),
                    workmail_action=ses.CfnReceiptRule.WorkmailActionProperty(
                        organization_arn="organizationArn",
                
                        # the properties below are optional
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.ActionProperty.__init__)
                check_type(argname="argument add_header_action", value=add_header_action, expected_type=type_hints["add_header_action"])
                check_type(argname="argument bounce_action", value=bounce_action, expected_type=type_hints["bounce_action"])
                check_type(argname="argument lambda_action", value=lambda_action, expected_type=type_hints["lambda_action"])
                check_type(argname="argument s3_action", value=s3_action, expected_type=type_hints["s3_action"])
                check_type(argname="argument sns_action", value=sns_action, expected_type=type_hints["sns_action"])
                check_type(argname="argument stop_action", value=stop_action, expected_type=type_hints["stop_action"])
                check_type(argname="argument workmail_action", value=workmail_action, expected_type=type_hints["workmail_action"])
            self._values: typing.Dict[str, typing.Any] = {}
            if add_header_action is not None:
                self._values["add_header_action"] = add_header_action
            if bounce_action is not None:
                self._values["bounce_action"] = bounce_action
            if lambda_action is not None:
                self._values["lambda_action"] = lambda_action
            if s3_action is not None:
                self._values["s3_action"] = s3_action
            if sns_action is not None:
                self._values["sns_action"] = sns_action
            if stop_action is not None:
                self._values["stop_action"] = stop_action
            if workmail_action is not None:
                self._values["workmail_action"] = workmail_action

        @builtins.property
        def add_header_action(
            self,
        ) -> typing.Optional[typing.Union["CfnReceiptRule.AddHeaderActionProperty", _IResolvable_da3f097b]]:
            '''Adds a header to the received email.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-addheaderaction
            '''
            result = self._values.get("add_header_action")
            return typing.cast(typing.Optional[typing.Union["CfnReceiptRule.AddHeaderActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def bounce_action(
            self,
        ) -> typing.Optional[typing.Union["CfnReceiptRule.BounceActionProperty", _IResolvable_da3f097b]]:
            '''Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-bounceaction
            '''
            result = self._values.get("bounce_action")
            return typing.cast(typing.Optional[typing.Union["CfnReceiptRule.BounceActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def lambda_action(
            self,
        ) -> typing.Optional[typing.Union["CfnReceiptRule.LambdaActionProperty", _IResolvable_da3f097b]]:
            '''Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-lambdaaction
            '''
            result = self._values.get("lambda_action")
            return typing.cast(typing.Optional[typing.Union["CfnReceiptRule.LambdaActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_action(
            self,
        ) -> typing.Optional[typing.Union["CfnReceiptRule.S3ActionProperty", _IResolvable_da3f097b]]:
            '''Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-s3action
            '''
            result = self._values.get("s3_action")
            return typing.cast(typing.Optional[typing.Union["CfnReceiptRule.S3ActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sns_action(
            self,
        ) -> typing.Optional[typing.Union["CfnReceiptRule.SNSActionProperty", _IResolvable_da3f097b]]:
            '''Publishes the email content within a notification to Amazon SNS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-snsaction
            '''
            result = self._values.get("sns_action")
            return typing.cast(typing.Optional[typing.Union["CfnReceiptRule.SNSActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def stop_action(
            self,
        ) -> typing.Optional[typing.Union["CfnReceiptRule.StopActionProperty", _IResolvable_da3f097b]]:
            '''Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-stopaction
            '''
            result = self._values.get("stop_action")
            return typing.cast(typing.Optional[typing.Union["CfnReceiptRule.StopActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def workmail_action(
            self,
        ) -> typing.Optional[typing.Union["CfnReceiptRule.WorkmailActionProperty", _IResolvable_da3f097b]]:
            '''Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-workmailaction
            '''
            result = self._values.get("workmail_action")
            return typing.cast(typing.Optional[typing.Union["CfnReceiptRule.WorkmailActionProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.AddHeaderActionProperty",
        jsii_struct_bases=[],
        name_mapping={"header_name": "headerName", "header_value": "headerValue"},
    )
    class AddHeaderActionProperty:
        def __init__(
            self,
            *,
            header_name: builtins.str,
            header_value: builtins.str,
        ) -> None:
            '''When included in a receipt rule, this action adds a header to the received email.

            For information about adding a header using a receipt rule, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-add-header.html>`_ .

            :param header_name: The name of the header to add to the incoming message. The name must contain at least one character, and can contain up to 50 characters. It consists of alphanumeric (a–z, A–Z, 0–9) characters and dashes.
            :param header_value: The content to include in the header. This value can contain up to 2048 characters. It can't contain newline ( ``\\n`` ) or carriage return ( ``\\r`` ) characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                add_header_action_property = ses.CfnReceiptRule.AddHeaderActionProperty(
                    header_name="headerName",
                    header_value="headerValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.AddHeaderActionProperty.__init__)
                check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
                check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            self._values: typing.Dict[str, typing.Any] = {
                "header_name": header_name,
                "header_value": header_value,
            }

        @builtins.property
        def header_name(self) -> builtins.str:
            '''The name of the header to add to the incoming message.

            The name must contain at least one character, and can contain up to 50 characters. It consists of alphanumeric (a–z, A–Z, 0–9) characters and dashes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername
            '''
            result = self._values.get("header_name")
            assert result is not None, "Required property 'header_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def header_value(self) -> builtins.str:
            '''The content to include in the header.

            This value can contain up to 2048 characters. It can't contain newline ( ``\\n`` ) or carriage return ( ``\\r`` ) characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue
            '''
            result = self._values.get("header_value")
            assert result is not None, "Required property 'header_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddHeaderActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.BounceActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message": "message",
            "sender": "sender",
            "smtp_reply_code": "smtpReplyCode",
            "status_code": "statusCode",
            "topic_arn": "topicArn",
        },
    )
    class BounceActionProperty:
        def __init__(
            self,
            *,
            message: builtins.str,
            sender: builtins.str,
            smtp_reply_code: builtins.str,
            status_code: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            For information about sending a bounce message in response to a received email, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-bounce.html>`_ .

            :param message: Human-readable text to include in the bounce message.
            :param sender: The email address of the sender of the bounced email. This is the address from which the bounce message is sent.
            :param smtp_reply_code: The SMTP reply code, as defined by `RFC 5321 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5321>`_ .
            :param status_code: The SMTP enhanced status code, as defined by `RFC 3463 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3463>`_ .
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                bounce_action_property = ses.CfnReceiptRule.BounceActionProperty(
                    message="message",
                    sender="sender",
                    smtp_reply_code="smtpReplyCode",
                
                    # the properties below are optional
                    status_code="statusCode",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.BounceActionProperty.__init__)
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
                check_type(argname="argument sender", value=sender, expected_type=type_hints["sender"])
                check_type(argname="argument smtp_reply_code", value=smtp_reply_code, expected_type=type_hints["smtp_reply_code"])
                check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "message": message,
                "sender": sender,
                "smtp_reply_code": smtp_reply_code,
            }
            if status_code is not None:
                self._values["status_code"] = status_code
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def message(self) -> builtins.str:
            '''Human-readable text to include in the bounce message.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message
            '''
            result = self._values.get("message")
            assert result is not None, "Required property 'message' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sender(self) -> builtins.str:
            '''The email address of the sender of the bounced email.

            This is the address from which the bounce message is sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender
            '''
            result = self._values.get("sender")
            assert result is not None, "Required property 'sender' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def smtp_reply_code(self) -> builtins.str:
            '''The SMTP reply code, as defined by `RFC 5321 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5321>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode
            '''
            result = self._values.get("smtp_reply_code")
            assert result is not None, "Required property 'smtp_reply_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status_code(self) -> typing.Optional[builtins.str]:
            '''The SMTP enhanced status code, as defined by `RFC 3463 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3463>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode
            '''
            result = self._values.get("status_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BounceActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.LambdaActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_arn": "functionArn",
            "invocation_type": "invocationType",
            "topic_arn": "topicArn",
        },
    )
    class LambdaActionProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            invocation_type: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action calls an AWS Lambda function and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            To enable Amazon SES to call your AWS Lambda function or to publish to an Amazon SNS topic of another account, Amazon SES must have permission to access those resources. For information about giving permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ .

            For information about using AWS Lambda actions in receipt rules, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda.html>`_ .

            :param function_arn: The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`_ .
            :param invocation_type: The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse`` means that the execution of the function immediately results in a response, and a value of ``Event`` means that the function is invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`_ . .. epigraph:: There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                lambda_action_property = ses.CfnReceiptRule.LambdaActionProperty(
                    function_arn="functionArn",
                
                    # the properties below are optional
                    invocation_type="invocationType",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.LambdaActionProperty.__init__)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
                check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "function_arn": function_arn,
            }
            if invocation_type is not None:
                self._values["invocation_type"] = invocation_type
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Lambda function.

            An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invocation_type(self) -> typing.Optional[builtins.str]:
            '''The invocation type of the AWS Lambda function.

            An invocation type of ``RequestResponse`` means that the execution of the function immediately results in a response, and a value of ``Event`` means that the function is invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`_ .
            .. epigraph::

               There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype
            '''
            result = self._values.get("invocation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "enabled": "enabled",
            "name": "name",
            "recipients": "recipients",
            "scan_enabled": "scanEnabled",
            "tls_policy": "tlsPolicy",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnReceiptRule.ActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            name: typing.Optional[builtins.str] = None,
            recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
            scan_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            tls_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Receipt rules enable you to specify which actions Amazon SES should take when it receives mail on behalf of one or more email addresses or domains that you own.

            Each receipt rule defines a set of email addresses or domains that it applies to. If the email addresses or domains match at least one recipient address of the message, Amazon SES executes all of the receipt rule's actions on the message.

            For information about setting up receipt rules, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html>`_ .

            :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.
            :param enabled: If ``true`` , the receipt rule is active. The default value is ``false`` .
            :param name: The name of the receipt rule. The name must meet the following requirements:. - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or periods (.). - Start and end with a letter or number. - Contain 64 characters or fewer.
            :param recipients: The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule matches all recipients on all verified domains.
            :param scan_enabled: If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is ``false`` .
            :param tls_policy: Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon SES bounces emails that are not received over TLS. The default is ``Optional`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                rule_property = ses.CfnReceiptRule.RuleProperty(
                    actions=[ses.CfnReceiptRule.ActionProperty(
                        add_header_action=ses.CfnReceiptRule.AddHeaderActionProperty(
                            header_name="headerName",
                            header_value="headerValue"
                        ),
                        bounce_action=ses.CfnReceiptRule.BounceActionProperty(
                            message="message",
                            sender="sender",
                            smtp_reply_code="smtpReplyCode",
                
                            # the properties below are optional
                            status_code="statusCode",
                            topic_arn="topicArn"
                        ),
                        lambda_action=ses.CfnReceiptRule.LambdaActionProperty(
                            function_arn="functionArn",
                
                            # the properties below are optional
                            invocation_type="invocationType",
                            topic_arn="topicArn"
                        ),
                        s3_action=ses.CfnReceiptRule.S3ActionProperty(
                            bucket_name="bucketName",
                
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn",
                            object_key_prefix="objectKeyPrefix",
                            topic_arn="topicArn"
                        ),
                        sns_action=ses.CfnReceiptRule.SNSActionProperty(
                            encoding="encoding",
                            topic_arn="topicArn"
                        ),
                        stop_action=ses.CfnReceiptRule.StopActionProperty(
                            scope="scope",
                
                            # the properties below are optional
                            topic_arn="topicArn"
                        ),
                        workmail_action=ses.CfnReceiptRule.WorkmailActionProperty(
                            organization_arn="organizationArn",
                
                            # the properties below are optional
                            topic_arn="topicArn"
                        )
                    )],
                    enabled=False,
                    name="name",
                    recipients=["recipients"],
                    scan_enabled=False,
                    tls_policy="tlsPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.RuleProperty.__init__)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
                check_type(argname="argument scan_enabled", value=scan_enabled, expected_type=type_hints["scan_enabled"])
                check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
            self._values: typing.Dict[str, typing.Any] = {}
            if actions is not None:
                self._values["actions"] = actions
            if enabled is not None:
                self._values["enabled"] = enabled
            if name is not None:
                self._values["name"] = name
            if recipients is not None:
                self._values["recipients"] = recipients
            if scan_enabled is not None:
                self._values["scan_enabled"] = scan_enabled
            if tls_policy is not None:
                self._values["tls_policy"] = tls_policy

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnReceiptRule.ActionProperty", _IResolvable_da3f097b]]]]:
            '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnReceiptRule.ActionProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , the receipt rule is active.

            The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the receipt rule. The name must meet the following requirements:.

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or periods (.).
            - Start and end with a letter or number.
            - Contain 64 characters or fewer.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The recipient domains and email addresses that the receipt rule applies to.

            If this field is not specified, this rule matches all recipients on all verified domains.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-recipients
            '''
            result = self._values.get("recipients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def scan_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses.

            The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-scanenabled
            '''
            result = self._values.get("scan_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def tls_policy(self) -> typing.Optional[builtins.str]:
            '''Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

            If this parameter is set to ``Require`` , Amazon SES bounces emails that are not received over TLS. The default is ``Optional`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-tlspolicy
            '''
            result = self._values.get("tls_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.S3ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "kms_key_arn": "kmsKeyArn",
            "object_key_prefix": "objectKeyPrefix",
            "topic_arn": "topicArn",
        },
    )
    class S3ActionProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
            object_key_prefix: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            To enable Amazon SES to write emails to your Amazon S3 bucket, use an AWS KMS key to encrypt your emails, or publish to an Amazon SNS topic of another account, Amazon SES must have permission to access those resources. For information about granting permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ .
            .. epigraph::

               When you save your emails to an Amazon S3 bucket, the maximum email size (including headers) is 30 MB. Emails larger than that bounces.

            For information about specifying Amazon S3 actions in receipt rules, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-s3.html>`_ .

            :param bucket_name: The name of the Amazon S3 bucket for incoming email.
            :param kms_key_arn: The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key that you created in AWS KMS as follows: - To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) Region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key. - To use a custom master key that you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ . For more information about key policies, see the `AWS KMS Developer Guide <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`_ . If you do not specify a master key, Amazon SES does not encrypt your emails. .. epigraph:: Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS SDK for Java <https://docs.aws.amazon.com/sdk-for-java/>`_ and `AWS SDK for Ruby <https://docs.aws.amazon.com/sdk-for-ruby/>`_ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`_ .
            :param object_key_prefix: The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.
            :param topic_arn: The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                s3_action_property = ses.CfnReceiptRule.S3ActionProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn",
                    object_key_prefix="objectKeyPrefix",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.S3ActionProperty.__init__)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if object_key_prefix is not None:
                self._values["object_key_prefix"] = object_key_prefix
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the Amazon S3 bucket for incoming email.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket.

            You can use the default master key or a custom master key that you created in AWS KMS as follows:

            - To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) Region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key.
            - To use a custom master key that you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ .

            For more information about key policies, see the `AWS KMS Developer Guide <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`_ . If you do not specify a master key, Amazon SES does not encrypt your emails.
            .. epigraph::

               Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS SDK for Java <https://docs.aws.amazon.com/sdk-for-java/>`_ and `AWS SDK for Ruby <https://docs.aws.amazon.com/sdk-for-ruby/>`_ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The key prefix of the Amazon S3 bucket.

            The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix
            '''
            result = self._values.get("object_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.SNSActionProperty",
        jsii_struct_bases=[],
        name_mapping={"encoding": "encoding", "topic_arn": "topicArn"},
    )
    class SNSActionProperty:
        def __init__(
            self,
            *,
            encoding: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            This action includes a complete copy of the email content in the Amazon SNS notifications. Amazon SNS notifications for all other actions simply provide information about the email. They do not include the email content itself.

            If you own the Amazon SNS topic, you don't need to do anything to give Amazon SES permission to publish emails to it. However, if you don't own the Amazon SNS topic, you need to attach a policy to the topic to give Amazon SES permissions to access it. For information about giving permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ .
            .. epigraph::

               You can only publish emails that are 150 KB or less (including the header) to Amazon SNS. Larger emails bounce. If you anticipate emails larger than 150 KB, use the S3 action instead.

            For information about using a receipt rule to publish an Amazon SNS notification, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-sns.html>`_ .

            :param encoding: The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                s_nSAction_property = ses.CfnReceiptRule.SNSActionProperty(
                    encoding="encoding",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.SNSActionProperty.__init__)
                check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if encoding is not None:
                self._values["encoding"] = encoding
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def encoding(self) -> typing.Optional[builtins.str]:
            '''The encoding to use for the email within the Amazon SNS notification.

            UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding
            '''
            result = self._values.get("encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SNSActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.StopActionProperty",
        jsii_struct_bases=[],
        name_mapping={"scope": "scope", "topic_arn": "topicArn"},
    )
    class StopActionProperty:
        def __init__(
            self,
            *,
            scope: builtins.str,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action terminates the evaluation of the receipt rule set and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            For information about setting a stop action in a receipt rule, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-stop.html>`_ .

            :param scope: The scope of the StopAction. The only acceptable value is ``RuleSet`` .
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ Amazon SNS operation. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                stop_action_property = ses.CfnReceiptRule.StopActionProperty(
                    scope="scope",
                
                    # the properties below are optional
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.StopActionProperty.__init__)
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "scope": scope,
            }
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def scope(self) -> builtins.str:
            '''The scope of the StopAction.

            The only acceptable value is ``RuleSet`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope
            '''
            result = self._values.get("scope")
            assert result is not None, "Required property 'scope' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ Amazon SNS operation.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StopActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.WorkmailActionProperty",
        jsii_struct_bases=[],
        name_mapping={"organization_arn": "organizationArn", "topic_arn": "topicArn"},
    )
    class WorkmailActionProperty:
        def __init__(
            self,
            *,
            organization_arn: builtins.str,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action calls Amazon WorkMail and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            It usually isn't necessary to set this up manually, because Amazon WorkMail adds the rule automatically during its setup procedure.

            For information using a receipt rule to call Amazon WorkMail, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-workmail.html>`_ .

            :param organization_arn: The Amazon Resource Name (ARN) of the Amazon WorkMail organization. Amazon WorkMail ARNs use the following format:. ``arn:aws:workmail:<region>:<awsAccountId>:organization/<workmailOrganizationId>`` You can find the ID of your organization by using the `ListOrganizations <https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListOrganizations.html>`_ operation in Amazon WorkMail. Amazon WorkMail organization IDs begin with " ``m-`` ", followed by a string of alphanumeric characters. For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`_ .
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                workmail_action_property = ses.CfnReceiptRule.WorkmailActionProperty(
                    organization_arn="organizationArn",
                
                    # the properties below are optional
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnReceiptRule.WorkmailActionProperty.__init__)
                check_type(argname="argument organization_arn", value=organization_arn, expected_type=type_hints["organization_arn"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "organization_arn": organization_arn,
            }
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def organization_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon WorkMail organization. Amazon WorkMail ARNs use the following format:.

            ``arn:aws:workmail:<region>:<awsAccountId>:organization/<workmailOrganizationId>``

            You can find the ID of your organization by using the `ListOrganizations <https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListOrganizations.html>`_ operation in Amazon WorkMail. Amazon WorkMail organization IDs begin with " ``m-`` ", followed by a string of alphanumeric characters.

            For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn
            '''
            result = self._values.get("organization_arn")
            assert result is not None, "Required property 'organization_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkmailActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_set_name": "ruleSetName", "after": "after"},
)
class CfnReceiptRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union[typing.Union[CfnReceiptRule.RuleProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        rule_set_name: builtins.str,
        after: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnReceiptRule``.

        :param rule: A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.
        :param rule_set_name: The name of the rule set where the receipt rule is added.
        :param after: The name of an existing rule after which the new rule is placed. If this parameter is null, the new rule is inserted at the beginning of the rule list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_receipt_rule_props = ses.CfnReceiptRuleProps(
                rule=ses.CfnReceiptRule.RuleProperty(
                    actions=[ses.CfnReceiptRule.ActionProperty(
                        add_header_action=ses.CfnReceiptRule.AddHeaderActionProperty(
                            header_name="headerName",
                            header_value="headerValue"
                        ),
                        bounce_action=ses.CfnReceiptRule.BounceActionProperty(
                            message="message",
                            sender="sender",
                            smtp_reply_code="smtpReplyCode",
            
                            # the properties below are optional
                            status_code="statusCode",
                            topic_arn="topicArn"
                        ),
                        lambda_action=ses.CfnReceiptRule.LambdaActionProperty(
                            function_arn="functionArn",
            
                            # the properties below are optional
                            invocation_type="invocationType",
                            topic_arn="topicArn"
                        ),
                        s3_action=ses.CfnReceiptRule.S3ActionProperty(
                            bucket_name="bucketName",
            
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn",
                            object_key_prefix="objectKeyPrefix",
                            topic_arn="topicArn"
                        ),
                        sns_action=ses.CfnReceiptRule.SNSActionProperty(
                            encoding="encoding",
                            topic_arn="topicArn"
                        ),
                        stop_action=ses.CfnReceiptRule.StopActionProperty(
                            scope="scope",
            
                            # the properties below are optional
                            topic_arn="topicArn"
                        ),
                        workmail_action=ses.CfnReceiptRule.WorkmailActionProperty(
                            organization_arn="organizationArn",
            
                            # the properties below are optional
                            topic_arn="topicArn"
                        )
                    )],
                    enabled=False,
                    name="name",
                    recipients=["recipients"],
                    scan_enabled=False,
                    tls_policy="tlsPolicy"
                ),
                rule_set_name="ruleSetName",
            
                # the properties below are optional
                after="after"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptRuleProps.__init__)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_set_name", value=rule_set_name, expected_type=type_hints["rule_set_name"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
            "rule_set_name": rule_set_name,
        }
        if after is not None:
            self._values["after"] = after

    @builtins.property
    def rule(self) -> typing.Union[CfnReceiptRule.RuleProperty, _IResolvable_da3f097b]:
        '''A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[CfnReceiptRule.RuleProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def rule_set_name(self) -> builtins.str:
        '''The name of the rule set where the receipt rule is added.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rulesetname
        '''
        result = self._values.get("rule_set_name")
        assert result is not None, "Required property 'rule_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def after(self) -> typing.Optional[builtins.str]:
        '''The name of an existing rule after which the new rule is placed.

        If this parameter is null, the new rule is inserted at the beginning of the rule list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-after
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnReceiptRuleSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRuleSet",
):
    '''A CloudFormation ``AWS::SES::ReceiptRuleSet``.

    Creates an empty receipt rule set.

    For information about setting up receipt rule sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules>`_ .

    You can execute this operation no more than once per second.

    :cloudformationResource: AWS::SES::ReceiptRuleSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_receipt_rule_set = ses.CfnReceiptRuleSet(self, "MyCfnReceiptRuleSet",
            rule_set_name="ruleSetName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        rule_set_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SES::ReceiptRuleSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param rule_set_name: The name of the receipt rule set to reorder.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptRuleSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReceiptRuleSetProps(rule_set_name=rule_set_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptRuleSet.inspect)
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
            type_hints = typing.get_type_hints(CfnReceiptRuleSet._render_properties)
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
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the receipt rule set to reorder.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html#cfn-ses-receiptruleset-rulesetname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSetName"))

    @rule_set_name.setter
    def rule_set_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnReceiptRuleSet, "rule_set_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={"rule_set_name": "ruleSetName"},
)
class CfnReceiptRuleSetProps:
    def __init__(self, *, rule_set_name: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``CfnReceiptRuleSet``.

        :param rule_set_name: The name of the receipt rule set to reorder.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_receipt_rule_set_props = ses.CfnReceiptRuleSetProps(
                rule_set_name="ruleSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnReceiptRuleSetProps.__init__)
            check_type(argname="argument rule_set_name", value=rule_set_name, expected_type=type_hints["rule_set_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if rule_set_name is not None:
            self._values["rule_set_name"] = rule_set_name

    @builtins.property
    def rule_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the receipt rule set to reorder.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html#cfn-ses-receiptruleset-rulesetname
        '''
        result = self._values.get("rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnTemplate",
):
    '''A CloudFormation ``AWS::SES::Template``.

    Specifies an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation.

    :cloudformationResource: AWS::SES::Template
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_template = ses.CfnTemplate(self, "MyCfnTemplate",
            template=ses.CfnTemplate.TemplateProperty(
                subject_part="subjectPart",
        
                # the properties below are optional
                html_part="htmlPart",
                template_name="templateName",
                text_part="textPart"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        template: typing.Optional[typing.Union[typing.Union["CfnTemplate.TemplateProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::SES::Template``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param template: The content of the email, composed of a subject line and either an HTML part or a text-only part.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTemplateProps(template=template)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTemplate.inspect)
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
            type_hints = typing.get_type_hints(CfnTemplate._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="template")
    def template(
        self,
    ) -> typing.Optional[typing.Union["CfnTemplate.TemplateProperty", _IResolvable_da3f097b]]:
        '''The content of the email, composed of a subject line and either an HTML part or a text-only part.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#cfn-ses-template-template
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTemplate.TemplateProperty", _IResolvable_da3f097b]], jsii.get(self, "template"))

    @template.setter
    def template(
        self,
        value: typing.Optional[typing.Union["CfnTemplate.TemplateProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTemplate, "template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnTemplate.TemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "subject_part": "subjectPart",
            "html_part": "htmlPart",
            "template_name": "templateName",
            "text_part": "textPart",
        },
    )
    class TemplateProperty:
        def __init__(
            self,
            *,
            subject_part: builtins.str,
            html_part: typing.Optional[builtins.str] = None,
            template_name: typing.Optional[builtins.str] = None,
            text_part: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The content of the email, composed of a subject line and either an HTML part or a text-only part.

            :param subject_part: The subject line of the email.
            :param html_part: The HTML body of the email.
            :param template_name: The name of the template.
            :param text_part: The email body that is visible to recipients whose email clients do not display HTML content.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                template_property = ses.CfnTemplate.TemplateProperty(
                    subject_part="subjectPart",
                
                    # the properties below are optional
                    html_part="htmlPart",
                    template_name="templateName",
                    text_part="textPart"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTemplate.TemplateProperty.__init__)
                check_type(argname="argument subject_part", value=subject_part, expected_type=type_hints["subject_part"])
                check_type(argname="argument html_part", value=html_part, expected_type=type_hints["html_part"])
                check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
                check_type(argname="argument text_part", value=text_part, expected_type=type_hints["text_part"])
            self._values: typing.Dict[str, typing.Any] = {
                "subject_part": subject_part,
            }
            if html_part is not None:
                self._values["html_part"] = html_part
            if template_name is not None:
                self._values["template_name"] = template_name
            if text_part is not None:
                self._values["text_part"] = text_part

        @builtins.property
        def subject_part(self) -> builtins.str:
            '''The subject line of the email.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-subjectpart
            '''
            result = self._values.get("subject_part")
            assert result is not None, "Required property 'subject_part' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def html_part(self) -> typing.Optional[builtins.str]:
            '''The HTML body of the email.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-htmlpart
            '''
            result = self._values.get("html_part")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_name(self) -> typing.Optional[builtins.str]:
            '''The name of the template.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-templatename
            '''
            result = self._values.get("template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_part(self) -> typing.Optional[builtins.str]:
            '''The email body that is visible to recipients whose email clients do not display HTML content.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-textpart
            '''
            result = self._values.get("text_part")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnTemplateProps",
    jsii_struct_bases=[],
    name_mapping={"template": "template"},
)
class CfnTemplateProps:
    def __init__(
        self,
        *,
        template: typing.Optional[typing.Union[typing.Union[CfnTemplate.TemplateProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTemplate``.

        :param template: The content of the email, composed of a subject line and either an HTML part or a text-only part.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_template_props = ses.CfnTemplateProps(
                template=ses.CfnTemplate.TemplateProperty(
                    subject_part="subjectPart",
            
                    # the properties below are optional
                    html_part="htmlPart",
                    template_name="templateName",
                    text_part="textPart"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTemplateProps.__init__)
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def template(
        self,
    ) -> typing.Optional[typing.Union[CfnTemplate.TemplateProperty, _IResolvable_da3f097b]]:
        '''The content of the email, composed of a subject line and either an HTML part or a text-only part.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#cfn-ses-template-template
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[typing.Union[CfnTemplate.TemplateProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "custom_tracking_redirect_domain": "customTrackingRedirectDomain",
        "dedicated_ip_pool": "dedicatedIpPool",
        "reputation_metrics": "reputationMetrics",
        "sending_enabled": "sendingEnabled",
        "suppression_reasons": "suppressionReasons",
        "tls_policy": "tlsPolicy",
    },
)
class ConfigurationSetProps:
    def __init__(
        self,
        *,
        configuration_set_name: typing.Optional[builtins.str] = None,
        custom_tracking_redirect_domain: typing.Optional[builtins.str] = None,
        dedicated_ip_pool: typing.Optional["IDedicatedIpPool"] = None,
        reputation_metrics: typing.Optional[builtins.bool] = None,
        sending_enabled: typing.Optional[builtins.bool] = None,
        suppression_reasons: typing.Optional["SuppressionReasons"] = None,
        tls_policy: typing.Optional["ConfigurationSetTlsPolicy"] = None,
    ) -> None:
        '''Properties for a configuration set.

        :param configuration_set_name: A name for the configuration set. Default: - a CloudFormation generated name
        :param custom_tracking_redirect_domain: The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain. Default: - use the default awstrack.me domain
        :param dedicated_ip_pool: The dedicated IP pool to associate with the configuration set. Default: - do not use a dedicated IP pool
        :param reputation_metrics: Whether to publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch. Default: false
        :param sending_enabled: Whether email sending is enabled. Default: true
        :param suppression_reasons: The reasons for which recipient email addresses should be automatically added to your account's suppression list. Default: - use account level settings
        :param tls_policy: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). Default: ConfigurationSetTlsPolicy.OPTIONAL

        :exampleMetadata: infused

        Example::

            # my_pool: ses.IDedicatedIpPool
            
            
            ses.ConfigurationSet(self, "ConfigurationSet",
                custom_tracking_redirect_domain="track.cdk.dev",
                suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
                tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
                dedicated_ip_pool=my_pool
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigurationSetProps.__init__)
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            check_type(argname="argument custom_tracking_redirect_domain", value=custom_tracking_redirect_domain, expected_type=type_hints["custom_tracking_redirect_domain"])
            check_type(argname="argument dedicated_ip_pool", value=dedicated_ip_pool, expected_type=type_hints["dedicated_ip_pool"])
            check_type(argname="argument reputation_metrics", value=reputation_metrics, expected_type=type_hints["reputation_metrics"])
            check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
            check_type(argname="argument suppression_reasons", value=suppression_reasons, expected_type=type_hints["suppression_reasons"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if configuration_set_name is not None:
            self._values["configuration_set_name"] = configuration_set_name
        if custom_tracking_redirect_domain is not None:
            self._values["custom_tracking_redirect_domain"] = custom_tracking_redirect_domain
        if dedicated_ip_pool is not None:
            self._values["dedicated_ip_pool"] = dedicated_ip_pool
        if reputation_metrics is not None:
            self._values["reputation_metrics"] = reputation_metrics
        if sending_enabled is not None:
            self._values["sending_enabled"] = sending_enabled
        if suppression_reasons is not None:
            self._values["suppression_reasons"] = suppression_reasons
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def configuration_set_name(self) -> typing.Optional[builtins.str]:
        '''A name for the configuration set.

        :default: - a CloudFormation generated name
        '''
        result = self._values.get("configuration_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_tracking_redirect_domain(self) -> typing.Optional[builtins.str]:
        '''The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain.

        :default: - use the default awstrack.me domain
        '''
        result = self._values.get("custom_tracking_redirect_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dedicated_ip_pool(self) -> typing.Optional["IDedicatedIpPool"]:
        '''The dedicated IP pool to associate with the configuration set.

        :default: - do not use a dedicated IP pool
        '''
        result = self._values.get("dedicated_ip_pool")
        return typing.cast(typing.Optional["IDedicatedIpPool"], result)

    @builtins.property
    def reputation_metrics(self) -> typing.Optional[builtins.bool]:
        '''Whether to publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.

        :default: false
        '''
        result = self._values.get("reputation_metrics")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sending_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether email sending is enabled.

        :default: true
        '''
        result = self._values.get("sending_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def suppression_reasons(self) -> typing.Optional["SuppressionReasons"]:
        '''The reasons for which recipient email addresses should be automatically added to your account's suppression list.

        :default: - use account level settings
        '''
        result = self._values.get("suppression_reasons")
        return typing.cast(typing.Optional["SuppressionReasons"], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional["ConfigurationSetTlsPolicy"]:
        '''Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).

        :default: ConfigurationSetTlsPolicy.OPTIONAL
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional["ConfigurationSetTlsPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.ConfigurationSetTlsPolicy")
class ConfigurationSetTlsPolicy(enum.Enum):
    '''TLS policy for a configuration set.

    :exampleMetadata: infused

    Example::

        # my_pool: ses.IDedicatedIpPool
        
        
        ses.ConfigurationSet(self, "ConfigurationSet",
            custom_tracking_redirect_domain="track.cdk.dev",
            suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
            tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
            dedicated_ip_pool=my_pool
        )
    '''

    REQUIRE = "REQUIRE"
    '''Messages are only delivered if a TLS connection can be established.'''
    OPTIONAL = "OPTIONAL"
    '''Messages can be delivered in plain text if a TLS connection can't be established.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.DedicatedIpPoolProps",
    jsii_struct_bases=[],
    name_mapping={"dedicated_ip_pool_name": "dedicatedIpPoolName"},
)
class DedicatedIpPoolProps:
    def __init__(
        self,
        *,
        dedicated_ip_pool_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a dedicated IP pool.

        :param dedicated_ip_pool_name: A name for the dedicated IP pool. Default: - a CloudFormation generated name

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            dedicated_ip_pool_props = ses.DedicatedIpPoolProps(
                dedicated_ip_pool_name="dedicatedIpPoolName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DedicatedIpPoolProps.__init__)
            check_type(argname="argument dedicated_ip_pool_name", value=dedicated_ip_pool_name, expected_type=type_hints["dedicated_ip_pool_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dedicated_ip_pool_name is not None:
            self._values["dedicated_ip_pool_name"] = dedicated_ip_pool_name

    @builtins.property
    def dedicated_ip_pool_name(self) -> typing.Optional[builtins.str]:
        '''A name for the dedicated IP pool.

        :default: - a CloudFormation generated name
        '''
        result = self._values.get("dedicated_ip_pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DedicatedIpPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DkimIdentity(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_ses.DkimIdentity",
):
    '''The identity to use for DKIM.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # my_hosted_zone: route53.IPublicHostedZone
        
        
        ses.EmailIdentity(stack, "Identity",
            identity=ses.Identity.public_hosted_zone(my_hosted_zone),
            dkim_identity=DkimIdentity.byo_dkim(
                private_key=SecretValue.secrets_manager("dkim-private-key"),
                public_key="...base64-encoded-public-key...",
                selector="selector"
            )
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="byoDkim") # type: ignore[misc]
    @builtins.classmethod
    def byo_dkim(
        cls,
        *,
        private_key: _SecretValue_3dd0ddae,
        selector: builtins.str,
        public_key: typing.Optional[builtins.str] = None,
    ) -> "DkimIdentity":
        '''Bring Your Own DKIM.

        :param private_key: The private key that's used to generate a DKIM signature.
        :param selector: A string that's used to identify a public key in the DNS configuration for a domain.
        :param public_key: The public key. If specified, a TXT record with the public key is created. Default: - the validation TXT record with the public key is not created

        :see: https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-bring-your-own.html
        '''
        options = ByoDkimOptions(
            private_key=private_key, selector=selector, public_key=public_key
        )

        return typing.cast("DkimIdentity", jsii.sinvoke(cls, "byoDkim", [options]))

    @jsii.member(jsii_name="easyDkim") # type: ignore[misc]
    @builtins.classmethod
    def easy_dkim(
        cls,
        signing_key_length: typing.Optional["EasyDkimSigningKeyLength"] = None,
    ) -> "DkimIdentity":
        '''Easy DKIM.

        :param signing_key_length: The length of the signing key. This can be changed at most once per day.

        :see: https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DkimIdentity.easy_dkim)
            check_type(argname="argument signing_key_length", value=signing_key_length, expected_type=type_hints["signing_key_length"])
        return typing.cast("DkimIdentity", jsii.sinvoke(cls, "easyDkim", [signing_key_length]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(
        self,
        email_identity: "EmailIdentity",
        hosted_zone: typing.Optional[_IPublicHostedZone_9b6e7da4] = None,
    ) -> typing.Optional["DkimIdentityConfig"]:
        '''Binds this DKIM identity to the email identity.

        :param email_identity: -
        :param hosted_zone: -
        '''
        ...


class _DkimIdentityProxy(DkimIdentity):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        email_identity: "EmailIdentity",
        hosted_zone: typing.Optional[_IPublicHostedZone_9b6e7da4] = None,
    ) -> typing.Optional["DkimIdentityConfig"]:
        '''Binds this DKIM identity to the email identity.

        :param email_identity: -
        :param hosted_zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DkimIdentity.bind)
            check_type(argname="argument email_identity", value=email_identity, expected_type=type_hints["email_identity"])
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
        return typing.cast(typing.Optional["DkimIdentityConfig"], jsii.invoke(self, "bind", [email_identity, hosted_zone]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DkimIdentity).__jsii_proxy_class__ = lambda : _DkimIdentityProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.DkimIdentityConfig",
    jsii_struct_bases=[],
    name_mapping={
        "domain_signing_private_key": "domainSigningPrivateKey",
        "domain_signing_selector": "domainSigningSelector",
        "next_signing_key_length": "nextSigningKeyLength",
    },
)
class DkimIdentityConfig:
    def __init__(
        self,
        *,
        domain_signing_private_key: typing.Optional[builtins.str] = None,
        domain_signing_selector: typing.Optional[builtins.str] = None,
        next_signing_key_length: typing.Optional["EasyDkimSigningKeyLength"] = None,
    ) -> None:
        '''Configuration for DKIM identity.

        :param domain_signing_private_key: A private key that's used to generate a DKIM signature. Default: - use Easy DKIM
        :param domain_signing_selector: A string that's used to identify a public key in the DNS configuration for a domain. Default: - use Easy DKIM
        :param next_signing_key_length: The key length of the future DKIM key pair to be generated. This can be changed at most once per day. Default: EasyDkimSigningKeyLength.RSA_2048_BIT

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            dkim_identity_config = ses.DkimIdentityConfig(
                domain_signing_private_key="domainSigningPrivateKey",
                domain_signing_selector="domainSigningSelector",
                next_signing_key_length=ses.EasyDkimSigningKeyLength.RSA_1024_BIT
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DkimIdentityConfig.__init__)
            check_type(argname="argument domain_signing_private_key", value=domain_signing_private_key, expected_type=type_hints["domain_signing_private_key"])
            check_type(argname="argument domain_signing_selector", value=domain_signing_selector, expected_type=type_hints["domain_signing_selector"])
            check_type(argname="argument next_signing_key_length", value=next_signing_key_length, expected_type=type_hints["next_signing_key_length"])
        self._values: typing.Dict[str, typing.Any] = {}
        if domain_signing_private_key is not None:
            self._values["domain_signing_private_key"] = domain_signing_private_key
        if domain_signing_selector is not None:
            self._values["domain_signing_selector"] = domain_signing_selector
        if next_signing_key_length is not None:
            self._values["next_signing_key_length"] = next_signing_key_length

    @builtins.property
    def domain_signing_private_key(self) -> typing.Optional[builtins.str]:
        '''A private key that's used to generate a DKIM signature.

        :default: - use Easy DKIM
        '''
        result = self._values.get("domain_signing_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_signing_selector(self) -> typing.Optional[builtins.str]:
        '''A string that's used to identify a public key in the DNS configuration for a domain.

        :default: - use Easy DKIM
        '''
        result = self._values.get("domain_signing_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_signing_key_length(self) -> typing.Optional["EasyDkimSigningKeyLength"]:
        '''The key length of the future DKIM key pair to be generated.

        This can be changed
        at most once per day.

        :default: EasyDkimSigningKeyLength.RSA_2048_BIT
        '''
        result = self._values.get("next_signing_key_length")
        return typing.cast(typing.Optional["EasyDkimSigningKeyLength"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DkimIdentityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.DkimRecord",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class DkimRecord:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''A DKIM record.

        :param name: The name of the record.
        :param value: The value of the record.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            dkim_record = ses.DkimRecord(
                name="name",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DkimRecord.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the record.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the record.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DkimRecord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DropSpamReceiptRule(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.DropSpamReceiptRule",
):
    '''A rule added at the top of the rule set to drop spam/virus.

    :see: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda-example-functions.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        # receipt_rule: ses.ReceiptRule
        # receipt_rule_action: ses.IReceiptRuleAction
        # receipt_rule_set: ses.ReceiptRuleSet
        
        drop_spam_receipt_rule = ses.DropSpamReceiptRule(self, "MyDropSpamReceiptRule",
            rule_set=receipt_rule_set,
        
            # the properties below are optional
            actions=[receipt_rule_action],
            after=receipt_rule,
            enabled=False,
            receipt_rule_name="receiptRuleName",
            recipients=["recipients"],
            scan_enabled=False,
            tls_policy=ses.TlsPolicy.OPTIONAL
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        rule_set: "IReceiptRuleSet",
        actions: typing.Optional[typing.Sequence["IReceiptRuleAction"]] = None,
        after: typing.Optional["IReceiptRule"] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rule_set: The name of the rule set that the receipt rule will be added to.
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DropSpamReceiptRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DropSpamReceiptRuleProps(
            rule_set=rule_set,
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rule")
    def rule(self) -> "ReceiptRule":
        return typing.cast("ReceiptRule", jsii.get(self, "rule"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.EasyDkimSigningKeyLength")
class EasyDkimSigningKeyLength(enum.Enum):
    '''The signing key length for Easy DKIM.'''

    RSA_1024_BIT = "RSA_1024_BIT"
    '''RSA 1024-bit.'''
    RSA_2048_BIT = "RSA_2048_BIT"
    '''RSA 2048-bit.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.EmailIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "identity": "identity",
        "configuration_set": "configurationSet",
        "dkim_identity": "dkimIdentity",
        "dkim_signing": "dkimSigning",
        "feedback_forwarding": "feedbackForwarding",
        "mail_from_behavior_on_mx_failure": "mailFromBehaviorOnMxFailure",
        "mail_from_domain": "mailFromDomain",
    },
)
class EmailIdentityProps:
    def __init__(
        self,
        *,
        identity: "Identity",
        configuration_set: typing.Optional["IConfigurationSet"] = None,
        dkim_identity: typing.Optional[DkimIdentity] = None,
        dkim_signing: typing.Optional[builtins.bool] = None,
        feedback_forwarding: typing.Optional[builtins.bool] = None,
        mail_from_behavior_on_mx_failure: typing.Optional["MailFromBehaviorOnMxFailure"] = None,
        mail_from_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for an email identity.

        :param identity: The email address or domain to verify.
        :param configuration_set: The configuration set to associate with the email identity. Default: - do not use a specific configuration set
        :param dkim_identity: The type of DKIM identity to use. Default: - Easy DKIM with a key length of 2048-bit
        :param dkim_signing: Whether the messages that are sent from the identity are signed using DKIM. Default: true
        :param feedback_forwarding: Whether to receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the ``Return-Path`` header of the original email. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled). Default: true
        :param mail_from_behavior_on_mx_failure: The action to take if the required MX record for the MAIL FROM domain isn't found when you send an email. Default: MailFromBehaviorOnMxFailure.USE_DEFAULT_VALUE
        :param mail_from_domain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria: - It has to be a subdomain of the verified identity - It can't be used to receive email - It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails Default: - use amazonses.com

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # my_hosted_zone: route53.IPublicHostedZone
            
            
            identity = ses.EmailIdentity(stack, "Identity",
                identity=ses.Identity.public_hosted_zone(my_hosted_zone),
                mail_from_domain="mail.cdk.dev"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EmailIdentityProps.__init__)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument configuration_set", value=configuration_set, expected_type=type_hints["configuration_set"])
            check_type(argname="argument dkim_identity", value=dkim_identity, expected_type=type_hints["dkim_identity"])
            check_type(argname="argument dkim_signing", value=dkim_signing, expected_type=type_hints["dkim_signing"])
            check_type(argname="argument feedback_forwarding", value=feedback_forwarding, expected_type=type_hints["feedback_forwarding"])
            check_type(argname="argument mail_from_behavior_on_mx_failure", value=mail_from_behavior_on_mx_failure, expected_type=type_hints["mail_from_behavior_on_mx_failure"])
            check_type(argname="argument mail_from_domain", value=mail_from_domain, expected_type=type_hints["mail_from_domain"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity": identity,
        }
        if configuration_set is not None:
            self._values["configuration_set"] = configuration_set
        if dkim_identity is not None:
            self._values["dkim_identity"] = dkim_identity
        if dkim_signing is not None:
            self._values["dkim_signing"] = dkim_signing
        if feedback_forwarding is not None:
            self._values["feedback_forwarding"] = feedback_forwarding
        if mail_from_behavior_on_mx_failure is not None:
            self._values["mail_from_behavior_on_mx_failure"] = mail_from_behavior_on_mx_failure
        if mail_from_domain is not None:
            self._values["mail_from_domain"] = mail_from_domain

    @builtins.property
    def identity(self) -> "Identity":
        '''The email address or domain to verify.'''
        result = self._values.get("identity")
        assert result is not None, "Required property 'identity' is missing"
        return typing.cast("Identity", result)

    @builtins.property
    def configuration_set(self) -> typing.Optional["IConfigurationSet"]:
        '''The configuration set to associate with the email identity.

        :default: - do not use a specific configuration set
        '''
        result = self._values.get("configuration_set")
        return typing.cast(typing.Optional["IConfigurationSet"], result)

    @builtins.property
    def dkim_identity(self) -> typing.Optional[DkimIdentity]:
        '''The type of DKIM identity to use.

        :default: - Easy DKIM with a key length of 2048-bit
        '''
        result = self._values.get("dkim_identity")
        return typing.cast(typing.Optional[DkimIdentity], result)

    @builtins.property
    def dkim_signing(self) -> typing.Optional[builtins.bool]:
        '''Whether the messages that are sent from the identity are signed using DKIM.

        :default: true
        '''
        result = self._values.get("dkim_signing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def feedback_forwarding(self) -> typing.Optional[builtins.bool]:
        '''Whether to receive email notifications when bounce or complaint events occur.

        These notifications are sent to the address that you specified in the ``Return-Path``
        header of the original email.

        You're required to have a method of tracking bounces and complaints. If you haven't set
        up another mechanism for receiving bounce or complaint notifications (for example, by
        setting up an event destination), you receive an email notification when these events
        occur (even if this setting is disabled).

        :default: true
        '''
        result = self._values.get("feedback_forwarding")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mail_from_behavior_on_mx_failure(
        self,
    ) -> typing.Optional["MailFromBehaviorOnMxFailure"]:
        '''The action to take if the required MX record for the MAIL FROM domain isn't found when you send an email.

        :default: MailFromBehaviorOnMxFailure.USE_DEFAULT_VALUE
        '''
        result = self._values.get("mail_from_behavior_on_mx_failure")
        return typing.cast(typing.Optional["MailFromBehaviorOnMxFailure"], result)

    @builtins.property
    def mail_from_domain(self) -> typing.Optional[builtins.str]:
        '''The custom MAIL FROM domain that you want the verified identity to use.

        The MAIL FROM domain
        must meet the following criteria:

        - It has to be a subdomain of the verified identity
        - It can't be used to receive email
        - It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback
          forwarding emails

        :default: - use amazonses.com
        '''
        result = self._values.get("mail_from_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IConfigurationSet")
class IConfigurationSet(_IResource_c80c4260, typing_extensions.Protocol):
    '''A configuration set.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set.

        :attribute: true
        '''
        ...


class _IConfigurationSetProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''A configuration set.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IConfigurationSet"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationSet).__jsii_proxy_class__ = lambda : _IConfigurationSetProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IDedicatedIpPool")
class IDedicatedIpPool(_IResource_c80c4260, typing_extensions.Protocol):
    '''A dedicated IP pool.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedIpPoolName")
    def dedicated_ip_pool_name(self) -> builtins.str:
        '''The name of the dedicated IP pool.

        :attribute: true
        '''
        ...


class _IDedicatedIpPoolProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''A dedicated IP pool.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IDedicatedIpPool"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedIpPoolName")
    def dedicated_ip_pool_name(self) -> builtins.str:
        '''The name of the dedicated IP pool.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dedicatedIpPoolName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDedicatedIpPool).__jsii_proxy_class__ = lambda : _IDedicatedIpPoolProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IEmailIdentity")
class IEmailIdentity(_IResource_c80c4260, typing_extensions.Protocol):
    '''An email identity.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="emailIdentityName")
    def email_identity_name(self) -> builtins.str:
        '''The name of the email identity.

        :attribute: true
        '''
        ...


class _IEmailIdentityProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''An email identity.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IEmailIdentity"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="emailIdentityName")
    def email_identity_name(self) -> builtins.str:
        '''The name of the email identity.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "emailIdentityName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEmailIdentity).__jsii_proxy_class__ = lambda : _IEmailIdentityProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IReceiptRule")
class IReceiptRule(_IResource_c80c4260, typing_extensions.Protocol):
    '''A receipt rule.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.

        :attribute: true
        '''
        ...


class _IReceiptRuleProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''A receipt rule.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IReceiptRule"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRule).__jsii_proxy_class__ = lambda : _IReceiptRuleProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IReceiptRuleAction")
class IReceiptRuleAction(typing_extensions.Protocol):
    '''An abstract action for a receipt rule.'''

    @jsii.member(jsii_name="bind")
    def bind(self, receipt_rule: IReceiptRule) -> "ReceiptRuleActionConfig":
        '''Returns the receipt rule action specification.

        :param receipt_rule: -
        '''
        ...


class _IReceiptRuleActionProxy:
    '''An abstract action for a receipt rule.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IReceiptRuleAction"

    @jsii.member(jsii_name="bind")
    def bind(self, receipt_rule: IReceiptRule) -> "ReceiptRuleActionConfig":
        '''Returns the receipt rule action specification.

        :param receipt_rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IReceiptRuleAction.bind)
            check_type(argname="argument receipt_rule", value=receipt_rule, expected_type=type_hints["receipt_rule"])
        return typing.cast("ReceiptRuleActionConfig", jsii.invoke(self, "bind", [receipt_rule]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRuleAction).__jsii_proxy_class__ = lambda : _IReceiptRuleActionProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IReceiptRuleSet")
class IReceiptRuleSet(_IResource_c80c4260, typing_extensions.Protocol):
    '''A receipt rule set.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> "ReceiptRule":
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        ...


class _IReceiptRuleSetProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''A receipt rule set.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IReceiptRuleSet"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleSetName"))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> "ReceiptRule":
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IReceiptRuleSet.add_rule)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = ReceiptRuleOptions(
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        return typing.cast("ReceiptRule", jsii.invoke(self, "addRule", [id, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRuleSet).__jsii_proxy_class__ = lambda : _IReceiptRuleSetProxy


class Identity(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_ses.Identity",
):
    '''Identity.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # my_hosted_zone: route53.IPublicHostedZone
        
        
        identity = ses.EmailIdentity(stack, "Identity",
            identity=ses.Identity.public_hosted_zone(my_hosted_zone),
            mail_from_domain="mail.cdk.dev"
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="domain") # type: ignore[misc]
    @builtins.classmethod
    def domain(cls, domain: builtins.str) -> "Identity":
        '''Verify a domain name.

        DKIM records will have to be added manually to complete the verification
        process

        :param domain: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Identity.domain)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        return typing.cast("Identity", jsii.sinvoke(cls, "domain", [domain]))

    @jsii.member(jsii_name="email") # type: ignore[misc]
    @builtins.classmethod
    def email(cls, email: builtins.str) -> "Identity":
        '''Verify an email address.

        To complete the verification process look for an email from
        no-reply-aws@amazon.com, open it and click the link.

        :param email: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Identity.email)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
        return typing.cast("Identity", jsii.sinvoke(cls, "email", [email]))

    @jsii.member(jsii_name="publicHostedZone") # type: ignore[misc]
    @builtins.classmethod
    def public_hosted_zone(cls, hosted_zone: _IPublicHostedZone_9b6e7da4) -> "Identity":
        '''Verify a public hosted zone.

        DKIM and MAIL FROM records will be added automatically to the hosted
        zone

        :param hosted_zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Identity.public_hosted_zone)
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
        return typing.cast("Identity", jsii.sinvoke(cls, "publicHostedZone", [hosted_zone]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    @abc.abstractmethod
    def value(self) -> builtins.str:
        '''The value of the identity.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostedZone")
    @abc.abstractmethod
    def hosted_zone(self) -> typing.Optional[_IPublicHostedZone_9b6e7da4]:
        '''The hosted zone associated with this identity.

        :default: - no hosted zone is associated and no records are created
        '''
        ...


class _IdentityProxy(Identity):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''The value of the identity.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostedZone")
    def hosted_zone(self) -> typing.Optional[_IPublicHostedZone_9b6e7da4]:
        '''The hosted zone associated with this identity.

        :default: - no hosted zone is associated and no records are created
        '''
        return typing.cast(typing.Optional[_IPublicHostedZone_9b6e7da4], jsii.get(self, "hostedZone"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Identity).__jsii_proxy_class__ = lambda : _IdentityProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.LambdaActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "function_arn": "functionArn",
        "invocation_type": "invocationType",
        "topic_arn": "topicArn",
    },
)
class LambdaActionConfig:
    def __init__(
        self,
        *,
        function_arn: builtins.str,
        invocation_type: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''LambdaAction configuration.

        :param function_arn: The Amazon Resource Name (ARN) of the AWS Lambda function.
        :param invocation_type: The invocation type of the AWS Lambda function. Default: 'Event'
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            lambda_action_config = ses.LambdaActionConfig(
                function_arn="functionArn",
            
                # the properties below are optional
                invocation_type="invocationType",
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LambdaActionConfig.__init__)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
            check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "function_arn": function_arn,
        }
        if invocation_type is not None:
            self._values["invocation_type"] = invocation_type
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS Lambda function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn
        '''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invocation_type(self) -> typing.Optional[builtins.str]:
        '''The invocation type of the AWS Lambda function.

        :default: 'Event'

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype
        '''
        result = self._values.get("invocation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.MailFromBehaviorOnMxFailure")
class MailFromBehaviorOnMxFailure(enum.Enum):
    '''The action to take if the required MX record for the MAIL FROM domain isn't found.'''

    USE_DEFAULT_VALUE = "USE_DEFAULT_VALUE"
    '''The mail is sent using amazonses.com as the MAIL FROM domain.'''
    REJECT_MESSAGE = "REJECT_MESSAGE"
    '''The Amazon SES API v2 returns a ``MailFromDomainNotVerified`` error and doesn't attempt to deliver the email.'''


class ReceiptFilter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ReceiptFilter",
):
    '''A receipt filter.

    When instantiated without props, it creates a
    block all receipt filter.

    :exampleMetadata: infused

    Example::

        ses.ReceiptFilter(self, "Filter",
            ip="1.2.3.4/16"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ip: typing.Optional[builtins.str] = None,
        policy: typing.Optional["ReceiptFilterPolicy"] = None,
        receipt_filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ip: The ip address or range to filter. Default: 0.0.0.0/0
        :param policy: The policy for the filter. Default: Block
        :param receipt_filter_name: The name for the receipt filter. Default: a CloudFormation generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptFilter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ReceiptFilterProps(
            ip=ip, policy=policy, receipt_filter_name=receipt_filter_name
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.ReceiptFilterPolicy")
class ReceiptFilterPolicy(enum.Enum):
    '''The policy for the receipt filter.'''

    ALLOW = "ALLOW"
    '''Allow the ip address or range.'''
    BLOCK = "BLOCK"
    '''Block the ip address or range.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "ip": "ip",
        "policy": "policy",
        "receipt_filter_name": "receiptFilterName",
    },
)
class ReceiptFilterProps:
    def __init__(
        self,
        *,
        ip: typing.Optional[builtins.str] = None,
        policy: typing.Optional[ReceiptFilterPolicy] = None,
        receipt_filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for a ReceiptFilter.

        :param ip: The ip address or range to filter. Default: 0.0.0.0/0
        :param policy: The policy for the filter. Default: Block
        :param receipt_filter_name: The name for the receipt filter. Default: a CloudFormation generated name

        :exampleMetadata: infused

        Example::

            ses.ReceiptFilter(self, "Filter",
                ip="1.2.3.4/16"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptFilterProps.__init__)
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument receipt_filter_name", value=receipt_filter_name, expected_type=type_hints["receipt_filter_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ip is not None:
            self._values["ip"] = ip
        if policy is not None:
            self._values["policy"] = policy
        if receipt_filter_name is not None:
            self._values["receipt_filter_name"] = receipt_filter_name

    @builtins.property
    def ip(self) -> typing.Optional[builtins.str]:
        '''The ip address or range to filter.

        :default: 0.0.0.0/0
        '''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[ReceiptFilterPolicy]:
        '''The policy for the filter.

        :default: Block
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[ReceiptFilterPolicy], result)

    @builtins.property
    def receipt_filter_name(self) -> typing.Optional[builtins.str]:
        '''The name for the receipt filter.

        :default: a CloudFormation generated name
        '''
        result = self._values.get("receipt_filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IReceiptRule)
class ReceiptRule(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRule",
):
    '''A new receipt rule.

    :exampleMetadata: infused

    Example::

        rule_set = ses.ReceiptRuleSet(self, "RuleSet")
        
        aws_rule = rule_set.add_rule("Aws",
            recipients=["aws.com"]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        rule_set: IReceiptRuleSet,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rule_set: The name of the rule set that the receipt rule will be added to.
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ReceiptRuleProps(
            rule_set=rule_set,
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromReceiptRuleName") # type: ignore[misc]
    @builtins.classmethod
    def from_receipt_rule_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        receipt_rule_name: builtins.str,
    ) -> IReceiptRule:
        '''
        :param scope: -
        :param id: -
        :param receipt_rule_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRule.from_receipt_rule_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument receipt_rule_name", value=receipt_rule_name, expected_type=type_hints["receipt_rule_name"])
        return typing.cast(IReceiptRule, jsii.sinvoke(cls, "fromReceiptRuleName", [scope, id, receipt_rule_name]))

    @jsii.member(jsii_name="addAction")
    def add_action(self, action: IReceiptRuleAction) -> None:
        '''Adds an action to this receipt rule.

        :param action: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRule.add_action)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
        return typing.cast(None, jsii.invoke(self, "addAction", [action]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.'''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "add_header_action": "addHeaderAction",
        "bounce_action": "bounceAction",
        "lambda_action": "lambdaAction",
        "s3_action": "s3Action",
        "sns_action": "snsAction",
        "stop_action": "stopAction",
        "workmail_action": "workmailAction",
    },
)
class ReceiptRuleActionConfig:
    def __init__(
        self,
        *,
        add_header_action: typing.Optional[typing.Union[AddHeaderActionConfig, typing.Dict[str, typing.Any]]] = None,
        bounce_action: typing.Optional[typing.Union[BounceActionConfig, typing.Dict[str, typing.Any]]] = None,
        lambda_action: typing.Optional[typing.Union[LambdaActionConfig, typing.Dict[str, typing.Any]]] = None,
        s3_action: typing.Optional[typing.Union["S3ActionConfig", typing.Dict[str, typing.Any]]] = None,
        sns_action: typing.Optional[typing.Union["SNSActionConfig", typing.Dict[str, typing.Any]]] = None,
        stop_action: typing.Optional[typing.Union["StopActionConfig", typing.Dict[str, typing.Any]]] = None,
        workmail_action: typing.Optional[typing.Union["WorkmailActionConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''Properties for a receipt rule action.

        :param add_header_action: Adds a header to the received email.
        :param bounce_action: Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon SNS.
        :param lambda_action: Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
        :param s3_action: Saves the received message to an Amazon S3 bucket and, optionally, publishes a notification to Amazon SNS.
        :param sns_action: Publishes the email content within a notification to Amazon SNS.
        :param stop_action: Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
        :param workmail_action: Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            receipt_rule_action_config = ses.ReceiptRuleActionConfig(
                add_header_action=ses.AddHeaderActionConfig(
                    header_name="headerName",
                    header_value="headerValue"
                ),
                bounce_action=ses.BounceActionConfig(
                    message="message",
                    sender="sender",
                    smtp_reply_code="smtpReplyCode",
            
                    # the properties below are optional
                    status_code="statusCode",
                    topic_arn="topicArn"
                ),
                lambda_action=ses.LambdaActionConfig(
                    function_arn="functionArn",
            
                    # the properties below are optional
                    invocation_type="invocationType",
                    topic_arn="topicArn"
                ),
                s3_action=ses.S3ActionConfig(
                    bucket_name="bucketName",
            
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn",
                    object_key_prefix="objectKeyPrefix",
                    topic_arn="topicArn"
                ),
                sns_action=ses.SNSActionConfig(
                    encoding="encoding",
                    topic_arn="topicArn"
                ),
                stop_action=ses.StopActionConfig(
                    scope="scope",
            
                    # the properties below are optional
                    topic_arn="topicArn"
                ),
                workmail_action=ses.WorkmailActionConfig(
                    organization_arn="organizationArn",
            
                    # the properties below are optional
                    topic_arn="topicArn"
                )
            )
        '''
        if isinstance(add_header_action, dict):
            add_header_action = AddHeaderActionConfig(**add_header_action)
        if isinstance(bounce_action, dict):
            bounce_action = BounceActionConfig(**bounce_action)
        if isinstance(lambda_action, dict):
            lambda_action = LambdaActionConfig(**lambda_action)
        if isinstance(s3_action, dict):
            s3_action = S3ActionConfig(**s3_action)
        if isinstance(sns_action, dict):
            sns_action = SNSActionConfig(**sns_action)
        if isinstance(stop_action, dict):
            stop_action = StopActionConfig(**stop_action)
        if isinstance(workmail_action, dict):
            workmail_action = WorkmailActionConfig(**workmail_action)
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRuleActionConfig.__init__)
            check_type(argname="argument add_header_action", value=add_header_action, expected_type=type_hints["add_header_action"])
            check_type(argname="argument bounce_action", value=bounce_action, expected_type=type_hints["bounce_action"])
            check_type(argname="argument lambda_action", value=lambda_action, expected_type=type_hints["lambda_action"])
            check_type(argname="argument s3_action", value=s3_action, expected_type=type_hints["s3_action"])
            check_type(argname="argument sns_action", value=sns_action, expected_type=type_hints["sns_action"])
            check_type(argname="argument stop_action", value=stop_action, expected_type=type_hints["stop_action"])
            check_type(argname="argument workmail_action", value=workmail_action, expected_type=type_hints["workmail_action"])
        self._values: typing.Dict[str, typing.Any] = {}
        if add_header_action is not None:
            self._values["add_header_action"] = add_header_action
        if bounce_action is not None:
            self._values["bounce_action"] = bounce_action
        if lambda_action is not None:
            self._values["lambda_action"] = lambda_action
        if s3_action is not None:
            self._values["s3_action"] = s3_action
        if sns_action is not None:
            self._values["sns_action"] = sns_action
        if stop_action is not None:
            self._values["stop_action"] = stop_action
        if workmail_action is not None:
            self._values["workmail_action"] = workmail_action

    @builtins.property
    def add_header_action(self) -> typing.Optional[AddHeaderActionConfig]:
        '''Adds a header to the received email.'''
        result = self._values.get("add_header_action")
        return typing.cast(typing.Optional[AddHeaderActionConfig], result)

    @builtins.property
    def bounce_action(self) -> typing.Optional[BounceActionConfig]:
        '''Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("bounce_action")
        return typing.cast(typing.Optional[BounceActionConfig], result)

    @builtins.property
    def lambda_action(self) -> typing.Optional[LambdaActionConfig]:
        '''Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("lambda_action")
        return typing.cast(typing.Optional[LambdaActionConfig], result)

    @builtins.property
    def s3_action(self) -> typing.Optional["S3ActionConfig"]:
        '''Saves the received message to an Amazon S3 bucket and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("s3_action")
        return typing.cast(typing.Optional["S3ActionConfig"], result)

    @builtins.property
    def sns_action(self) -> typing.Optional["SNSActionConfig"]:
        '''Publishes the email content within a notification to Amazon SNS.'''
        result = self._values.get("sns_action")
        return typing.cast(typing.Optional["SNSActionConfig"], result)

    @builtins.property
    def stop_action(self) -> typing.Optional["StopActionConfig"]:
        '''Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.'''
        result = self._values.get("stop_action")
        return typing.cast(typing.Optional["StopActionConfig"], result)

    @builtins.property
    def workmail_action(self) -> typing.Optional["WorkmailActionConfig"]:
        '''Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("workmail_action")
        return typing.cast(typing.Optional["WorkmailActionConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleOptions",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
    },
)
class ReceiptRuleOptions:
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''Options to add a receipt rule to a receipt rule set.

        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.

        :exampleMetadata: infused

        Example::

            rule_set = ses.ReceiptRuleSet(self, "RuleSet")
            
            aws_rule = rule_set.add_rule("Aws",
                recipients=["aws.com"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRuleOptions.__init__)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument receipt_rule_name", value=receipt_rule_name, expected_type=type_hints["receipt_rule_name"])
            check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
            check_type(argname="argument scan_enabled", value=scan_enabled, expected_type=type_hints["scan_enabled"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional["TlsPolicy"]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional["TlsPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleProps",
    jsii_struct_bases=[ReceiptRuleOptions],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
        "rule_set": "ruleSet",
    },
)
class ReceiptRuleProps(ReceiptRuleOptions):
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
        rule_set: IReceiptRuleSet,
    ) -> None:
        '''Construction properties for a ReceiptRule.

        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        :param rule_set: The name of the rule set that the receipt rule will be added to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            # receipt_rule: ses.ReceiptRule
            # receipt_rule_action: ses.IReceiptRuleAction
            # receipt_rule_set: ses.ReceiptRuleSet
            
            receipt_rule_props = ses.ReceiptRuleProps(
                rule_set=receipt_rule_set,
            
                # the properties below are optional
                actions=[receipt_rule_action],
                after=receipt_rule,
                enabled=False,
                receipt_rule_name="receiptRuleName",
                recipients=["recipients"],
                scan_enabled=False,
                tls_policy=ses.TlsPolicy.OPTIONAL
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRuleProps.__init__)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument receipt_rule_name", value=receipt_rule_name, expected_type=type_hints["receipt_rule_name"])
            check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
            check_type(argname="argument scan_enabled", value=scan_enabled, expected_type=type_hints["scan_enabled"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
            check_type(argname="argument rule_set", value=rule_set, expected_type=type_hints["rule_set"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule_set": rule_set,
        }
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional["TlsPolicy"]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional["TlsPolicy"], result)

    @builtins.property
    def rule_set(self) -> IReceiptRuleSet:
        '''The name of the rule set that the receipt rule will be added to.'''
        result = self._values.get("rule_set")
        assert result is not None, "Required property 'rule_set' is missing"
        return typing.cast(IReceiptRuleSet, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IReceiptRuleSet)
class ReceiptRuleSet(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleSet",
):
    '''A new receipt rule set.

    :exampleMetadata: infused

    Example::

        rule_set = ses.ReceiptRuleSet(self, "RuleSet")
        
        aws_rule = rule_set.add_rule("Aws",
            recipients=["aws.com"]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        drop_spam: typing.Optional[builtins.bool] = None,
        receipt_rule_set_name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[ReceiptRuleOptions, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param drop_spam: Whether to add a first rule to stop processing messages that have at least one spam indicator. Default: false
        :param receipt_rule_set_name: The name for the receipt rule set. Default: - A CloudFormation generated name.
        :param rules: The list of rules to add to this rule set. Rules are added in the same order as they appear in the list. Default: - No rules are added to the rule set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRuleSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ReceiptRuleSetProps(
            drop_spam=drop_spam,
            receipt_rule_set_name=receipt_rule_set_name,
            rules=rules,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromReceiptRuleSetName") # type: ignore[misc]
    @builtins.classmethod
    def from_receipt_rule_set_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        receipt_rule_set_name: builtins.str,
    ) -> IReceiptRuleSet:
        '''Import an exported receipt rule set.

        :param scope: -
        :param id: -
        :param receipt_rule_set_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRuleSet.from_receipt_rule_set_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument receipt_rule_set_name", value=receipt_rule_set_name, expected_type=type_hints["receipt_rule_set_name"])
        return typing.cast(IReceiptRuleSet, jsii.sinvoke(cls, "fromReceiptRuleSetName", [scope, id, receipt_rule_set_name]))

    @jsii.member(jsii_name="addDropSpamRule")
    def _add_drop_spam_rule(self) -> None:
        '''Adds a drop spam rule.'''
        return typing.cast(None, jsii.invoke(self, "addDropSpamRule", []))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> ReceiptRule:
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRuleSet.add_rule)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = ReceiptRuleOptions(
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        return typing.cast(ReceiptRule, jsii.invoke(self, "addRule", [id, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.'''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleSetName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "drop_spam": "dropSpam",
        "receipt_rule_set_name": "receiptRuleSetName",
        "rules": "rules",
    },
)
class ReceiptRuleSetProps:
    def __init__(
        self,
        *,
        drop_spam: typing.Optional[builtins.bool] = None,
        receipt_rule_set_name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[ReceiptRuleOptions, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Construction properties for a ReceiptRuleSet.

        :param drop_spam: Whether to add a first rule to stop processing messages that have at least one spam indicator. Default: false
        :param receipt_rule_set_name: The name for the receipt rule set. Default: - A CloudFormation generated name.
        :param rules: The list of rules to add to this rule set. Rules are added in the same order as they appear in the list. Default: - No rules are added to the rule set.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            import aws_cdk.aws_ses_actions as actions
            
            
            bucket = s3.Bucket(self, "Bucket")
            topic = sns.Topic(self, "Topic")
            
            ses.ReceiptRuleSet(self, "RuleSet",
                rules=[ses.ReceiptRuleOptions(
                    recipients=["hello@aws.com"],
                    actions=[
                        actions.AddHeader(
                            name="X-Special-Header",
                            value="aws"
                        ),
                        actions.S3(
                            bucket=bucket,
                            object_key_prefix="emails/",
                            topic=topic
                        )
                    ]
                ), ses.ReceiptRuleOptions(
                    recipients=["aws.com"],
                    actions=[
                        actions.Sns(
                            topic=topic
                        )
                    ]
                )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReceiptRuleSetProps.__init__)
            check_type(argname="argument drop_spam", value=drop_spam, expected_type=type_hints["drop_spam"])
            check_type(argname="argument receipt_rule_set_name", value=receipt_rule_set_name, expected_type=type_hints["receipt_rule_set_name"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[str, typing.Any] = {}
        if drop_spam is not None:
            self._values["drop_spam"] = drop_spam
        if receipt_rule_set_name is not None:
            self._values["receipt_rule_set_name"] = receipt_rule_set_name
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def drop_spam(self) -> typing.Optional[builtins.bool]:
        '''Whether to add a first rule to stop processing messages that have at least one spam indicator.

        :default: false
        '''
        result = self._values.get("drop_spam")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_set_name(self) -> typing.Optional[builtins.str]:
        '''The name for the receipt rule set.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[ReceiptRuleOptions]]:
        '''The list of rules to add to this rule set.

        Rules are added in the same
        order as they appear in the list.

        :default: - No rules are added to the rule set.
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[ReceiptRuleOptions]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.S3ActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "kms_key_arn": "kmsKeyArn",
        "object_key_prefix": "objectKeyPrefix",
        "topic_arn": "topicArn",
    },
)
class S3ActionConfig:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''S3Action configuration.

        :param bucket_name: The name of the Amazon S3 bucket that you want to send incoming mail to.
        :param kms_key_arn: The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. Default: - Emails are not encrypted.
        :param object_key_prefix: The key prefix of the Amazon S3 bucket. Default: - No prefix.
        :param topic_arn: The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            s3_action_config = ses.S3ActionConfig(
                bucket_name="bucketName",
            
                # the properties below are optional
                kms_key_arn="kmsKeyArn",
                object_key_prefix="objectKeyPrefix",
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(S3ActionConfig.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if object_key_prefix is not None:
            self._values["object_key_prefix"] = object_key_prefix
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of the Amazon S3 bucket that you want to send incoming mail to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket.

        :default: - Emails are not encrypted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The key prefix of the Amazon S3 bucket.

        :default: - No prefix.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix
        '''
        result = self._values.get("object_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.SNSActionConfig",
    jsii_struct_bases=[],
    name_mapping={"encoding": "encoding", "topic_arn": "topicArn"},
)
class SNSActionConfig:
    def __init__(
        self,
        *,
        encoding: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''SNSAction configuration.

        :param encoding: The encoding to use for the email within the Amazon SNS notification. Default: 'UTF-8'
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            s_nSAction_config = ses.SNSActionConfig(
                encoding="encoding",
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SNSActionConfig.__init__)
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if encoding is not None:
            self._values["encoding"] = encoding
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''The encoding to use for the email within the Amazon SNS notification.

        :default: 'UTF-8'

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SNSActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.StopActionConfig",
    jsii_struct_bases=[],
    name_mapping={"scope": "scope", "topic_arn": "topicArn"},
)
class StopActionConfig:
    def __init__(
        self,
        *,
        scope: builtins.str,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''StopAction configuration.

        :param scope: The scope of the StopAction. The only acceptable value is RuleSet.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            stop_action_config = ses.StopActionConfig(
                scope="scope",
            
                # the properties below are optional
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StopActionConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "scope": scope,
        }
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def scope(self) -> builtins.str:
        '''The scope of the StopAction.

        The only acceptable value is RuleSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StopActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.SuppressionReasons")
class SuppressionReasons(enum.Enum):
    '''Reasons for which recipient email addresses should be automatically added to your account's suppression list.

    :exampleMetadata: infused

    Example::

        # my_pool: ses.IDedicatedIpPool
        
        
        ses.ConfigurationSet(self, "ConfigurationSet",
            custom_tracking_redirect_domain="track.cdk.dev",
            suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
            tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
            dedicated_ip_pool=my_pool
        )
    '''

    BOUNCES_AND_COMPLAINTS = "BOUNCES_AND_COMPLAINTS"
    '''Bounces and complaints.'''
    BOUNCES_ONLY = "BOUNCES_ONLY"
    '''Bounces only.'''
    COMPLAINTS_ONLY = "COMPLAINTS_ONLY"
    '''Complaints only.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.TlsPolicy")
class TlsPolicy(enum.Enum):
    '''The type of TLS policy for a receipt rule.'''

    OPTIONAL = "OPTIONAL"
    '''Do not check for TLS.'''
    REQUIRE = "REQUIRE"
    '''Bounce emails that are not received over TLS.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.WorkmailActionConfig",
    jsii_struct_bases=[],
    name_mapping={"organization_arn": "organizationArn", "topic_arn": "topicArn"},
)
class WorkmailActionConfig:
    def __init__(
        self,
        *,
        organization_arn: builtins.str,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''WorkmailAction configuration.

        :param organization_arn: The Amazon Resource Name (ARN) of the Amazon WorkMail organization.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            workmail_action_config = ses.WorkmailActionConfig(
                organization_arn="organizationArn",
            
                # the properties below are optional
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkmailActionConfig.__init__)
            check_type(argname="argument organization_arn", value=organization_arn, expected_type=type_hints["organization_arn"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "organization_arn": organization_arn,
        }
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def organization_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon WorkMail organization.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn
        '''
        result = self._values.get("organization_arn")
        assert result is not None, "Required property 'organization_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkmailActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IConfigurationSet)
class ConfigurationSet(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ConfigurationSet",
):
    '''A configuration set.

    :exampleMetadata: infused

    Example::

        # my_pool: ses.IDedicatedIpPool
        
        
        ses.ConfigurationSet(self, "ConfigurationSet",
            custom_tracking_redirect_domain="track.cdk.dev",
            suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
            tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
            dedicated_ip_pool=my_pool
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        configuration_set_name: typing.Optional[builtins.str] = None,
        custom_tracking_redirect_domain: typing.Optional[builtins.str] = None,
        dedicated_ip_pool: typing.Optional[IDedicatedIpPool] = None,
        reputation_metrics: typing.Optional[builtins.bool] = None,
        sending_enabled: typing.Optional[builtins.bool] = None,
        suppression_reasons: typing.Optional[SuppressionReasons] = None,
        tls_policy: typing.Optional[ConfigurationSetTlsPolicy] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param configuration_set_name: A name for the configuration set. Default: - a CloudFormation generated name
        :param custom_tracking_redirect_domain: The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain. Default: - use the default awstrack.me domain
        :param dedicated_ip_pool: The dedicated IP pool to associate with the configuration set. Default: - do not use a dedicated IP pool
        :param reputation_metrics: Whether to publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch. Default: false
        :param sending_enabled: Whether email sending is enabled. Default: true
        :param suppression_reasons: The reasons for which recipient email addresses should be automatically added to your account's suppression list. Default: - use account level settings
        :param tls_policy: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). Default: ConfigurationSetTlsPolicy.OPTIONAL
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigurationSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ConfigurationSetProps(
            configuration_set_name=configuration_set_name,
            custom_tracking_redirect_domain=custom_tracking_redirect_domain,
            dedicated_ip_pool=dedicated_ip_pool,
            reputation_metrics=reputation_metrics,
            sending_enabled=sending_enabled,
            suppression_reasons=suppression_reasons,
            tls_policy=tls_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigurationSetName") # type: ignore[misc]
    @builtins.classmethod
    def from_configuration_set_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        configuration_set_name: builtins.str,
    ) -> IConfigurationSet:
        '''Use an existing configuration set.

        :param scope: -
        :param id: -
        :param configuration_set_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfigurationSet.from_configuration_set_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
        return typing.cast(IConfigurationSet, jsii.sinvoke(cls, "fromConfigurationSetName", [scope, id, configuration_set_name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))


@jsii.implements(IDedicatedIpPool)
class DedicatedIpPool(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.DedicatedIpPool",
):
    '''A dedicated IP pool.

    :exampleMetadata: infused

    Example::

        ses.DedicatedIpPool(self, "Pool")
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dedicated_ip_pool_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dedicated_ip_pool_name: A name for the dedicated IP pool. Default: - a CloudFormation generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DedicatedIpPool.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DedicatedIpPoolProps(dedicated_ip_pool_name=dedicated_ip_pool_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDedicatedIpPoolName") # type: ignore[misc]
    @builtins.classmethod
    def from_dedicated_ip_pool_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        dedicated_ip_pool_name: builtins.str,
    ) -> IDedicatedIpPool:
        '''Use an existing dedicated IP pool.

        :param scope: -
        :param id: -
        :param dedicated_ip_pool_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DedicatedIpPool.from_dedicated_ip_pool_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument dedicated_ip_pool_name", value=dedicated_ip_pool_name, expected_type=type_hints["dedicated_ip_pool_name"])
        return typing.cast(IDedicatedIpPool, jsii.sinvoke(cls, "fromDedicatedIpPoolName", [scope, id, dedicated_ip_pool_name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedIpPoolName")
    def dedicated_ip_pool_name(self) -> builtins.str:
        '''The name of the dedicated IP pool.'''
        return typing.cast(builtins.str, jsii.get(self, "dedicatedIpPoolName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.DropSpamReceiptRuleProps",
    jsii_struct_bases=[ReceiptRuleProps],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
        "rule_set": "ruleSet",
    },
)
class DropSpamReceiptRuleProps(ReceiptRuleProps):
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional[TlsPolicy] = None,
        rule_set: IReceiptRuleSet,
    ) -> None:
        '''
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        :param rule_set: The name of the rule set that the receipt rule will be added to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            # receipt_rule: ses.ReceiptRule
            # receipt_rule_action: ses.IReceiptRuleAction
            # receipt_rule_set: ses.ReceiptRuleSet
            
            drop_spam_receipt_rule_props = ses.DropSpamReceiptRuleProps(
                rule_set=receipt_rule_set,
            
                # the properties below are optional
                actions=[receipt_rule_action],
                after=receipt_rule,
                enabled=False,
                receipt_rule_name="receiptRuleName",
                recipients=["recipients"],
                scan_enabled=False,
                tls_policy=ses.TlsPolicy.OPTIONAL
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DropSpamReceiptRuleProps.__init__)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument receipt_rule_name", value=receipt_rule_name, expected_type=type_hints["receipt_rule_name"])
            check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
            check_type(argname="argument scan_enabled", value=scan_enabled, expected_type=type_hints["scan_enabled"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
            check_type(argname="argument rule_set", value=rule_set, expected_type=type_hints["rule_set"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule_set": rule_set,
        }
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional[TlsPolicy]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional[TlsPolicy], result)

    @builtins.property
    def rule_set(self) -> IReceiptRuleSet:
        '''The name of the rule set that the receipt rule will be added to.'''
        result = self._values.get("rule_set")
        assert result is not None, "Required property 'rule_set' is missing"
        return typing.cast(IReceiptRuleSet, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DropSpamReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEmailIdentity)
class EmailIdentity(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.EmailIdentity",
):
    '''An email identity.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # my_hosted_zone: route53.IPublicHostedZone
        
        
        identity = ses.EmailIdentity(stack, "Identity",
            identity=ses.Identity.public_hosted_zone(my_hosted_zone),
            mail_from_domain="mail.cdk.dev"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        identity: Identity,
        configuration_set: typing.Optional[IConfigurationSet] = None,
        dkim_identity: typing.Optional[DkimIdentity] = None,
        dkim_signing: typing.Optional[builtins.bool] = None,
        feedback_forwarding: typing.Optional[builtins.bool] = None,
        mail_from_behavior_on_mx_failure: typing.Optional[MailFromBehaviorOnMxFailure] = None,
        mail_from_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param identity: The email address or domain to verify.
        :param configuration_set: The configuration set to associate with the email identity. Default: - do not use a specific configuration set
        :param dkim_identity: The type of DKIM identity to use. Default: - Easy DKIM with a key length of 2048-bit
        :param dkim_signing: Whether the messages that are sent from the identity are signed using DKIM. Default: true
        :param feedback_forwarding: Whether to receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the ``Return-Path`` header of the original email. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled). Default: true
        :param mail_from_behavior_on_mx_failure: The action to take if the required MX record for the MAIL FROM domain isn't found when you send an email. Default: MailFromBehaviorOnMxFailure.USE_DEFAULT_VALUE
        :param mail_from_domain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria: - It has to be a subdomain of the verified identity - It can't be used to receive email - It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails Default: - use amazonses.com
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EmailIdentity.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EmailIdentityProps(
            identity=identity,
            configuration_set=configuration_set,
            dkim_identity=dkim_identity,
            dkim_signing=dkim_signing,
            feedback_forwarding=feedback_forwarding,
            mail_from_behavior_on_mx_failure=mail_from_behavior_on_mx_failure,
            mail_from_domain=mail_from_domain,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEmailIdentityName") # type: ignore[misc]
    @builtins.classmethod
    def from_email_identity_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        email_identity_name: builtins.str,
    ) -> IEmailIdentity:
        '''Use an existing email identity.

        :param scope: -
        :param id: -
        :param email_identity_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EmailIdentity.from_email_identity_name)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument email_identity_name", value=email_identity_name, expected_type=type_hints["email_identity_name"])
        return typing.cast(IEmailIdentity, jsii.sinvoke(cls, "fromEmailIdentityName", [scope, id, email_identity_name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimDnsTokenName1")
    def dkim_dns_token_name1(self) -> builtins.str:
        '''The host name for the first token that you have to add to the DNS configurationfor your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenName1"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimDnsTokenName2")
    def dkim_dns_token_name2(self) -> builtins.str:
        '''The host name for the second token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenName2"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimDnsTokenName3")
    def dkim_dns_token_name3(self) -> builtins.str:
        '''The host name for the third token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenName3"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimDnsTokenValue1")
    def dkim_dns_token_value1(self) -> builtins.str:
        '''The record value for the first token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenValue1"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimDnsTokenValue2")
    def dkim_dns_token_value2(self) -> builtins.str:
        '''The record value for the second token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenValue2"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimDnsTokenValue3")
    def dkim_dns_token_value3(self) -> builtins.str:
        '''The record value for the third token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenValue3"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimRecords")
    def dkim_records(self) -> typing.List[DkimRecord]:
        '''DKIM records for this identity.'''
        return typing.cast(typing.List[DkimRecord], jsii.get(self, "dkimRecords"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="emailIdentityName")
    def email_identity_name(self) -> builtins.str:
        '''The name of the email identity.'''
        return typing.cast(builtins.str, jsii.get(self, "emailIdentityName"))


__all__ = [
    "AddHeaderActionConfig",
    "AllowListReceiptFilter",
    "AllowListReceiptFilterProps",
    "BounceActionConfig",
    "ByoDkimOptions",
    "CfnConfigurationSet",
    "CfnConfigurationSetEventDestination",
    "CfnConfigurationSetEventDestinationProps",
    "CfnConfigurationSetProps",
    "CfnContactList",
    "CfnContactListProps",
    "CfnDedicatedIpPool",
    "CfnDedicatedIpPoolProps",
    "CfnEmailIdentity",
    "CfnEmailIdentityProps",
    "CfnReceiptFilter",
    "CfnReceiptFilterProps",
    "CfnReceiptRule",
    "CfnReceiptRuleProps",
    "CfnReceiptRuleSet",
    "CfnReceiptRuleSetProps",
    "CfnTemplate",
    "CfnTemplateProps",
    "ConfigurationSet",
    "ConfigurationSetProps",
    "ConfigurationSetTlsPolicy",
    "DedicatedIpPool",
    "DedicatedIpPoolProps",
    "DkimIdentity",
    "DkimIdentityConfig",
    "DkimRecord",
    "DropSpamReceiptRule",
    "DropSpamReceiptRuleProps",
    "EasyDkimSigningKeyLength",
    "EmailIdentity",
    "EmailIdentityProps",
    "IConfigurationSet",
    "IDedicatedIpPool",
    "IEmailIdentity",
    "IReceiptRule",
    "IReceiptRuleAction",
    "IReceiptRuleSet",
    "Identity",
    "LambdaActionConfig",
    "MailFromBehaviorOnMxFailure",
    "ReceiptFilter",
    "ReceiptFilterPolicy",
    "ReceiptFilterProps",
    "ReceiptRule",
    "ReceiptRuleActionConfig",
    "ReceiptRuleOptions",
    "ReceiptRuleProps",
    "ReceiptRuleSet",
    "ReceiptRuleSetProps",
    "S3ActionConfig",
    "SNSActionConfig",
    "StopActionConfig",
    "SuppressionReasons",
    "TlsPolicy",
    "WorkmailActionConfig",
]

publication.publish()
