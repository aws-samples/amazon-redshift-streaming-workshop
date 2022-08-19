'''
# AWS IoT Things Graph Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotthingsgraph as iotthingsgraph
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTThingsGraph construct libraries](https://constructs.dev/search?q=iotthingsgraph)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTThingsGraph resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTThingsGraph.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTThingsGraph](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTThingsGraph.html).

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
class CfnFlowTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotthingsgraph.CfnFlowTemplate",
):
    '''A CloudFormation ``AWS::IoTThingsGraph::FlowTemplate``.

    Represents a workflow template. Workflows can be created only in the user's namespace. (The public namespace contains only entities.) The workflow can contain only entities in the specified namespace. The workflow is validated against the entities in the latest version of the user's namespace unless another namespace version is specified in the request.

    :cloudformationResource: AWS::IoTThingsGraph::FlowTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotthingsgraph as iotthingsgraph
        
        cfn_flow_template = iotthingsgraph.CfnFlowTemplate(self, "MyCfnFlowTemplate",
            definition=iotthingsgraph.CfnFlowTemplate.DefinitionDocumentProperty(
                language="language",
                text="text"
            ),
        
            # the properties below are optional
            compatible_namespace_version=123
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        definition: typing.Union[typing.Union["CfnFlowTemplate.DefinitionDocumentProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        compatible_namespace_version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::IoTThingsGraph::FlowTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param definition: A workflow's definition document.
        :param compatible_namespace_version: The version of the user's namespace against which the workflow was validated. Use this value in your system instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFlowTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowTemplateProps(
            definition=definition,
            compatible_namespace_version=compatible_namespace_version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFlowTemplate.inspect)
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
            type_hints = typing.get_type_hints(CfnFlowTemplate._render_properties)
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
    @jsii.member(jsii_name="definition")
    def definition(
        self,
    ) -> typing.Union["CfnFlowTemplate.DefinitionDocumentProperty", _IResolvable_da3f097b]:
        '''A workflow's definition document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-definition
        '''
        return typing.cast(typing.Union["CfnFlowTemplate.DefinitionDocumentProperty", _IResolvable_da3f097b], jsii.get(self, "definition"))

    @definition.setter
    def definition(
        self,
        value: typing.Union["CfnFlowTemplate.DefinitionDocumentProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFlowTemplate, "definition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="compatibleNamespaceVersion")
    def compatible_namespace_version(self) -> typing.Optional[jsii.Number]:
        '''The version of the user's namespace against which the workflow was validated.

        Use this value in your system instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-compatiblenamespaceversion
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "compatibleNamespaceVersion"))

    @compatible_namespace_version.setter
    def compatible_namespace_version(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFlowTemplate, "compatible_namespace_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compatibleNamespaceVersion", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotthingsgraph.CfnFlowTemplate.DefinitionDocumentProperty",
        jsii_struct_bases=[],
        name_mapping={"language": "language", "text": "text"},
    )
    class DefinitionDocumentProperty:
        def __init__(self, *, language: builtins.str, text: builtins.str) -> None:
            '''A document that defines an entity.

            :param language: The language used to define the entity. ``GRAPHQL`` is the only valid value.
            :param text: The GraphQL text that defines the entity.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotthingsgraph as iotthingsgraph
                
                definition_document_property = iotthingsgraph.CfnFlowTemplate.DefinitionDocumentProperty(
                    language="language",
                    text="text"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFlowTemplate.DefinitionDocumentProperty.__init__)
                check_type(argname="argument language", value=language, expected_type=type_hints["language"])
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            self._values: typing.Dict[str, typing.Any] = {
                "language": language,
                "text": text,
            }

        @builtins.property
        def language(self) -> builtins.str:
            '''The language used to define the entity.

            ``GRAPHQL`` is the only valid value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html#cfn-iotthingsgraph-flowtemplate-definitiondocument-language
            '''
            result = self._values.get("language")
            assert result is not None, "Required property 'language' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def text(self) -> builtins.str:
            '''The GraphQL text that defines the entity.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html#cfn-iotthingsgraph-flowtemplate-definitiondocument-text
            '''
            result = self._values.get("text")
            assert result is not None, "Required property 'text' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefinitionDocumentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotthingsgraph.CfnFlowTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "definition": "definition",
        "compatible_namespace_version": "compatibleNamespaceVersion",
    },
)
class CfnFlowTemplateProps:
    def __init__(
        self,
        *,
        definition: typing.Union[typing.Union[CfnFlowTemplate.DefinitionDocumentProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        compatible_namespace_version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlowTemplate``.

        :param definition: A workflow's definition document.
        :param compatible_namespace_version: The version of the user's namespace against which the workflow was validated. Use this value in your system instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotthingsgraph as iotthingsgraph
            
            cfn_flow_template_props = iotthingsgraph.CfnFlowTemplateProps(
                definition=iotthingsgraph.CfnFlowTemplate.DefinitionDocumentProperty(
                    language="language",
                    text="text"
                ),
            
                # the properties below are optional
                compatible_namespace_version=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFlowTemplateProps.__init__)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument compatible_namespace_version", value=compatible_namespace_version, expected_type=type_hints["compatible_namespace_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "definition": definition,
        }
        if compatible_namespace_version is not None:
            self._values["compatible_namespace_version"] = compatible_namespace_version

    @builtins.property
    def definition(
        self,
    ) -> typing.Union[CfnFlowTemplate.DefinitionDocumentProperty, _IResolvable_da3f097b]:
        '''A workflow's definition document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-definition
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast(typing.Union[CfnFlowTemplate.DefinitionDocumentProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def compatible_namespace_version(self) -> typing.Optional[jsii.Number]:
        '''The version of the user's namespace against which the workflow was validated.

        Use this value in your system instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-compatiblenamespaceversion
        '''
        result = self._values.get("compatible_namespace_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFlowTemplate",
    "CfnFlowTemplateProps",
]

publication.publish()
