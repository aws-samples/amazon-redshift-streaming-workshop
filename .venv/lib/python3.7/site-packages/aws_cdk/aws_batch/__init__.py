'''
# AWS Batch Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_batch as batch
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Batch construct libraries](https://constructs.dev/search?q=batch)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Batch resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Batch.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-batch-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Batch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Batch.html).

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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnComputeEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment",
):
    '''A CloudFormation ``AWS::Batch::ComputeEnvironment``.

    The ``AWS::Batch::ComputeEnvironment`` resource defines your AWS Batch compute environment. You can define ``MANAGED`` or ``UNMANAGED`` compute environments. ``MANAGED`` compute environments can use Amazon EC2 or AWS Fargate resources. ``UNMANAGED`` compute environments can only use EC2 resources. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .

    In a managed compute environment, AWS Batch manages the capacity and instance types of the compute resources within the environment. This is based on the compute resource specification that you define or the `launch template <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>`_ that you specify when you create the compute environment. You can choose either to use EC2 On-Demand Instances and EC2 Spot Instances, or to use Fargate and Fargate Spot capacity in your managed compute environment. You can optionally set a maximum price so that Spot Instances only launch when the Spot Instance price is below a specified percentage of the On-Demand price.
    .. epigraph::

       Multi-node parallel jobs are not supported on Spot Instances.

    In an unmanaged compute environment, you can manage your own EC2 compute resources and have a lot of flexibility with how you configure your compute resources. For example, you can use custom AMI. However, you need to verify that your AMI meets the Amazon ECS container instance AMI specification. For more information, see `container instance AMIs <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container_instance_AMIs.html>`_ in the *Amazon Elastic Container Service Developer Guide* . After you have created your unmanaged compute environment, you can use the `DescribeComputeEnvironments <https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeComputeEnvironments.html>`_ operation to find the Amazon ECS cluster that is associated with it. Then, manually launch your container instances into that Amazon ECS cluster. For more information, see `Launching an Amazon ECS container instance <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
    .. epigraph::

       AWS Batch doesn't upgrade the AMIs in a compute environment after it's created except under specific conditions. For example, it doesn't automatically update the AMIs when a newer version of the Amazon ECS optimized AMI is available. Therefore, you're responsible for the management of the guest operating system (including updates and security patches) and any additional application software or utilities that you install on the compute resources. There are two ways to use a new AMI for your AWS Batch jobs. The original method is to complete these steps:

       - Create a new compute environment with the new AMI.
       - Add the compute environment to an existing job queue.
       - Remove the earlier compute environment from your job queue.
       - Delete the earlier compute environment.

       In April 2022, AWS Batch added enhanced support for updating compute environments. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . To use the enhanced updating of compute environments to update AMIs, follow these rules:

       - Either do not set the `ServiceRole <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-servicerole>`_ property or set it to the *AWSServiceRoleForBatch* service-linked role.
       - Set the `AllocationStrategy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ property to ``BEST_FIT_PROGRESSIVE`` or ``SPOT_CAPACITY_OPTIMIZED`` .
       - Set the `ReplaceComputeEnvironment <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-replacecomputeenvironment>`_ property to ``false`` .
       - Set the `UpdateToLatestImageVersion <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ property to ``true`` .
       - Either do not specify an image ID in `ImageId <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ or `ImageIdOverride <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imageidoverride>`_ properties, or in the launch template identified by the `Launch Template <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ property. In that case AWS Batch will select the latest Amazon ECS optimized AMI supported by AWS Batch at the time the infrastructure update is initiated. Alternatively you can specify the AMI ID in the ``ImageId`` or ``ImageIdOverride`` properties, or the launch template identified by the ``LaunchTemplate`` properties. Changing any of these properties will trigger an infrastructure update.

       If these rules are followed, any update that triggers an infrastructure update will cause the AMI ID to be re-selected. If the `Version <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-version>`_ property of the `LaunchTemplateSpecification <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html>`_ is set to ``$Latest`` or ``$Default`` , the latest or default version of the launch template will be evaluated up at the time of the infrastructure update, even if the ``LaunchTemplateSpecification`` was not updated.

    :cloudformationResource: AWS::Batch::ComputeEnvironment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_batch as batch
        
        cfn_compute_environment = batch.CfnComputeEnvironment(self, "MyCfnComputeEnvironment",
            type="type",
        
            # the properties below are optional
            compute_environment_name="computeEnvironmentName",
            compute_resources=batch.CfnComputeEnvironment.ComputeResourcesProperty(
                maxv_cpus=123,
                subnets=["subnets"],
                type="type",
        
                # the properties below are optional
                allocation_strategy="allocationStrategy",
                bid_percentage=123,
                desiredv_cpus=123,
                ec2_configuration=[batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty(
                    image_type="imageType",
        
                    # the properties below are optional
                    image_id_override="imageIdOverride"
                )],
                ec2_key_pair="ec2KeyPair",
                image_id="imageId",
                instance_role="instanceRole",
                instance_types=["instanceTypes"],
                launch_template=batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    version="version"
                ),
                minv_cpus=123,
                placement_group="placementGroup",
                security_group_ids=["securityGroupIds"],
                spot_iam_fleet_role="spotIamFleetRole",
                tags={
                    "tags_key": "tags"
                },
                update_to_latest_image_version=False
            ),
            replace_compute_environment=False,
            service_role="serviceRole",
            state="state",
            tags={
                "tags_key": "tags"
            },
            unmanagedv_cpus=123,
            update_policy=batch.CfnComputeEnvironment.UpdatePolicyProperty(
                job_execution_timeout_minutes=123,
                terminate_jobs_on_update=False
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        compute_environment_name: typing.Optional[builtins.str] = None,
        compute_resources: typing.Optional[typing.Union[typing.Union["CfnComputeEnvironment.ComputeResourcesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        replace_compute_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        service_role: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        unmanagedv_cpus: typing.Optional[jsii.Number] = None,
        update_policy: typing.Optional[typing.Union[typing.Union["CfnComputeEnvironment.UpdatePolicyProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::Batch::ComputeEnvironment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param type: The type of the compute environment: ``MANAGED`` or ``UNMANAGED`` . For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .
        :param compute_environment_name: The name for your compute environment. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param compute_resources: The ComputeResources property type specifies details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .
        :param replace_compute_environment: Specifies whether the compute environment should be replaced if an update is made that requires replacing the instances in the compute environment. The default value is ``true`` . To enable more properties to be updated, set this property to ``false`` . When changing the value of this property to ``false`` , no other properties should be changed at the same time. If other properties are changed at the same time, and the change needs to be rolled back but it can't, it's possible for the stack to go into the ``UPDATE_ROLLBACK_FAILED`` state. You can't update a stack that is in the ``UPDATE_ROLLBACK_FAILED`` state. However, if you can continue to roll it back, you can return the stack to its original settings and then try to update it again. For more information, see `Continue rolling back an update <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`_ in the *AWS CloudFormation User Guide* . The properties that can't be changed without replacing the compute environment are in the ```ComputeResources`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html>`_ property type: ```AllocationStrategy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ , ```BidPercentage`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage>`_ , ```Ec2Configuration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```ImageId`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ , ```InstanceRole`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole>`_ , ```InstanceTypes`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes>`_ , ```LaunchTemplate`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ , ```MaxvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus>`_ , ```MinvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus>`_ , ```PlacementGroup`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup>`_ , ```SecurityGroupIds`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids>`_ , ```Subnets`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets>`_ , `Tags <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags>`_ , ```Type`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type>`_ , and ```UpdateToLatestImageVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ .
        :param service_role: The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf. For more information, see `AWS Batch service IAM role <https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html>`_ in the *AWS Batch User Guide* . .. epigraph:: If your account already created the AWS Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the AWS Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the AWS Batch service-linked role in your account. If your specified role has a path other than ``/`` , then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` then you would specify ``/foo/bar`` as the role name. For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* . .. epigraph:: Depending on how you created your AWS Batch service role, its ARN might contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
        :param state: The state of the compute environment. If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues. If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand. If the state is ``DISABLED`` , then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state don't scale out. However, they scale in to ``minvCpus`` value after instances become idle.
        :param tags: The tags applied to the compute environment.
        :param unmanagedv_cpus: The maximum number of vCPUs for an unmanaged compute environment. This parameter is only used for fair share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair share job queue, no vCPU capacity is reserved. .. epigraph:: This parameter is only supported when the ``type`` parameter is set to ``UNMANAGED`` .
        :param update_policy: Specifies the infrastructure update policy for the compute environment. For more information about infrastructure updates, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnComputeEnvironment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComputeEnvironmentProps(
            type=type,
            compute_environment_name=compute_environment_name,
            compute_resources=compute_resources,
            replace_compute_environment=replace_compute_environment,
            service_role=service_role,
            state=state,
            tags=tags,
            unmanagedv_cpus=unmanagedv_cpus,
            update_policy=update_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnComputeEnvironment.inspect)
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
            type_hints = typing.get_type_hints(CfnComputeEnvironment._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrComputeEnvironmentArn")
    def attr_compute_environment_arn(self) -> builtins.str:
        '''Returns the compute environment ARN, such as ``batch: *us-east-1* : *111122223333* :compute-environment/ *ComputeEnvironmentName*`` .

        :cloudformationAttribute: ComputeEnvironmentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComputeEnvironmentArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags applied to the compute environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the compute environment: ``MANAGED`` or ``UNMANAGED`` .

        For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnComputeEnvironment, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="computeEnvironmentName")
    def compute_environment_name(self) -> typing.Optional[builtins.str]:
        '''The name for your compute environment.

        It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-computeenvironmentname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeEnvironmentName"))

    @compute_environment_name.setter
    def compute_environment_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnComputeEnvironment, "compute_environment_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeEnvironmentName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="computeResources")
    def compute_resources(
        self,
    ) -> typing.Optional[typing.Union["CfnComputeEnvironment.ComputeResourcesProperty", _IResolvable_da3f097b]]:
        '''The ComputeResources property type specifies details of the compute resources managed by the compute environment.

        This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-computeresources
        '''
        return typing.cast(typing.Optional[typing.Union["CfnComputeEnvironment.ComputeResourcesProperty", _IResolvable_da3f097b]], jsii.get(self, "computeResources"))

    @compute_resources.setter
    def compute_resources(
        self,
        value: typing.Optional[typing.Union["CfnComputeEnvironment.ComputeResourcesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnComputeEnvironment, "compute_resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replaceComputeEnvironment")
    def replace_compute_environment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the compute environment should be replaced if an update is made that requires replacing the instances in the compute environment.

        The default value is ``true`` . To enable more properties to be updated, set this property to ``false`` . When changing the value of this property to ``false`` , no other properties should be changed at the same time. If other properties are changed at the same time, and the change needs to be rolled back but it can't, it's possible for the stack to go into the ``UPDATE_ROLLBACK_FAILED`` state. You can't update a stack that is in the ``UPDATE_ROLLBACK_FAILED`` state. However, if you can continue to roll it back, you can return the stack to its original settings and then try to update it again. For more information, see `Continue rolling back an update <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`_ in the *AWS CloudFormation User Guide* .

        The properties that can't be changed without replacing the compute environment are in the ```ComputeResources`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html>`_ property type: ```AllocationStrategy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ , ```BidPercentage`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage>`_ , ```Ec2Configuration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```ImageId`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ , ```InstanceRole`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole>`_ , ```InstanceTypes`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes>`_ , ```LaunchTemplate`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ , ```MaxvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus>`_ , ```MinvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus>`_ , ```PlacementGroup`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup>`_ , ```SecurityGroupIds`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids>`_ , ```Subnets`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets>`_ , `Tags <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags>`_ , ```Type`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type>`_ , and ```UpdateToLatestImageVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-replacecomputeenvironment
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "replaceComputeEnvironment"))

    @replace_compute_environment.setter
    def replace_compute_environment(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnComputeEnvironment, "replace_compute_environment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replaceComputeEnvironment", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> typing.Optional[builtins.str]:
        '''The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

        For more information, see `AWS Batch service IAM role <https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html>`_ in the *AWS Batch User Guide* .
        .. epigraph::

           If your account already created the AWS Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the AWS Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the AWS Batch service-linked role in your account.

        If your specified role has a path other than ``/`` , then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` then you would specify ``/foo/bar`` as the role name. For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* .
        .. epigraph::

           Depending on how you created your AWS Batch service role, its ARN might contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-servicerole
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnComputeEnvironment, "service_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the compute environment.

        If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.

        If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.

        If the state is ``DISABLED`` , then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state don't scale out. However, they scale in to ``minvCpus`` value after instances become idle.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnComputeEnvironment, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unmanagedvCpus")
    def unmanagedv_cpus(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of vCPUs for an unmanaged compute environment.

        This parameter is only used for fair share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair share job queue, no vCPU capacity is reserved.
        .. epigraph::

           This parameter is only supported when the ``type`` parameter is set to ``UNMANAGED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-unmanagedvcpus
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unmanagedvCpus"))

    @unmanagedv_cpus.setter
    def unmanagedv_cpus(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnComputeEnvironment, "unmanagedv_cpus").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unmanagedvCpus", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updatePolicy")
    def update_policy(
        self,
    ) -> typing.Optional[typing.Union["CfnComputeEnvironment.UpdatePolicyProperty", _IResolvable_da3f097b]]:
        '''Specifies the infrastructure update policy for the compute environment.

        For more information about infrastructure updates, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-updatepolicy
        '''
        return typing.cast(typing.Optional[typing.Union["CfnComputeEnvironment.UpdatePolicyProperty", _IResolvable_da3f097b]], jsii.get(self, "updatePolicy"))

    @update_policy.setter
    def update_policy(
        self,
        value: typing.Optional[typing.Union["CfnComputeEnvironment.UpdatePolicyProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnComputeEnvironment, "update_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatePolicy", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.ComputeResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maxv_cpus": "maxvCpus",
            "subnets": "subnets",
            "type": "type",
            "allocation_strategy": "allocationStrategy",
            "bid_percentage": "bidPercentage",
            "desiredv_cpus": "desiredvCpus",
            "ec2_configuration": "ec2Configuration",
            "ec2_key_pair": "ec2KeyPair",
            "image_id": "imageId",
            "instance_role": "instanceRole",
            "instance_types": "instanceTypes",
            "launch_template": "launchTemplate",
            "minv_cpus": "minvCpus",
            "placement_group": "placementGroup",
            "security_group_ids": "securityGroupIds",
            "spot_iam_fleet_role": "spotIamFleetRole",
            "tags": "tags",
            "update_to_latest_image_version": "updateToLatestImageVersion",
        },
    )
    class ComputeResourcesProperty:
        def __init__(
            self,
            *,
            maxv_cpus: jsii.Number,
            subnets: typing.Sequence[builtins.str],
            type: builtins.str,
            allocation_strategy: typing.Optional[builtins.str] = None,
            bid_percentage: typing.Optional[jsii.Number] = None,
            desiredv_cpus: typing.Optional[jsii.Number] = None,
            ec2_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComputeEnvironment.Ec2ConfigurationObjectProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            ec2_key_pair: typing.Optional[builtins.str] = None,
            image_id: typing.Optional[builtins.str] = None,
            instance_role: typing.Optional[builtins.str] = None,
            instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            launch_template: typing.Optional[typing.Union[typing.Union["CfnComputeEnvironment.LaunchTemplateSpecificationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            minv_cpus: typing.Optional[jsii.Number] = None,
            placement_group: typing.Optional[builtins.str] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            spot_iam_fleet_role: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            update_to_latest_image_version: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Details about the compute resources managed by the compute environment.

            This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .

            :param maxv_cpus: The maximum number of Amazon EC2 vCPUs that an environment can reach. .. epigraph:: With both ``BEST_FIT_PROGRESSIVE`` and ``SPOT_CAPACITY_OPTIMIZED`` allocation strategies, AWS Batch might need to exceed ``maxvCpus`` to meet your capacity requirements. In this event, AWS Batch never exceeds ``maxvCpus`` by more than a single instance. That is, no more than a single instance from among those specified in your compute environment.
            :param subnets: The VPC subnets where the compute resources are launched. Fargate compute resources can contain up to 16 subnets. For Fargate compute resources, providing an empty list will be handled as if this parameter wasn't specified and no change is made. For EC2 compute resources, providing an empty list removes the VPC subnets from the compute resource. For more information, see `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon VPC User Guide* . When updating a compute environment, changing the VPC subnets requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            :param type: The type of compute environment: ``EC2`` , ``SPOT`` , ``FARGATE`` , or ``FARGATE_SPOT`` . For more information, see `Compute environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* . If you choose ``SPOT`` , you must also specify an Amazon EC2 Spot Fleet role with the ``spotIamFleetRole`` parameter. For more information, see `Amazon EC2 spot fleet role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`_ in the *AWS Batch User Guide* . When updating compute environment, changing the type of a compute environment requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . When updating the type of a compute environment, changing between ``EC2`` and ``SPOT`` or between ``FARGATE`` and ``FARGATE_SPOT`` will initiate an infrastructure update, but if you switch between ``EC2`` and ``FARGATE`` , AWS CloudFormation will create a new compute environment.
            :param allocation_strategy: The allocation strategy to use for the compute resource if not enough instances of the best fitting instance type can be allocated. This might be because of availability of the instance type in the Region or `Amazon EC2 service limits <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ . For more information, see `Allocation strategies <https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html>`_ in the *AWS Batch User Guide* . When updating a compute environment, changing the allocation strategy requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . ``BEST_FIT`` is not supported when updating a compute environment. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified. - **BEST_FIT (default)** - AWS Batch selects an instance type that best fits the needs of the jobs with a preference for the lowest-cost instance type. If additional instances of the selected instance type aren't available, AWS Batch waits for the additional instances to be available. If there aren't enough instances available, or if the user is reaching `Amazon EC2 service limits <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ then additional jobs aren't run until the currently running jobs have completed. This allocation strategy keeps costs lower but can limit scaling. If you are using Spot Fleets with ``BEST_FIT`` then the Spot Fleet IAM role must be specified. - **BEST_FIT_PROGRESSIVE** - AWS Batch will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types with a lower cost per unit vCPU. If additional instances of the previously selected instance types aren't available, AWS Batch will select new instance types. - **SPOT_CAPACITY_OPTIMIZED** - AWS Batch will select one or more instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types that are less likely to be interrupted. This allocation strategy is only available for Spot Instance compute resources. With both ``BEST_FIT_PROGRESSIVE`` and ``SPOT_CAPACITY_OPTIMIZED`` strategies, AWS Batch might need to go above ``maxvCpus`` to meet your capacity requirements. In this event, AWS Batch never exceeds ``maxvCpus`` by more than a single instance.
            :param bid_percentage: The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be less than 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. When updating a compute environment, changing the bid percentage requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.
            :param desiredv_cpus: The desired number of Amazon EC2 vCPUS in the compute environment. AWS Batch modifies this value between the minimum and maximum values based on job queue demand. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.
            :param ec2_configuration: Provides information used to select Amazon Machine Images (AMIs) for EC2 instances in the compute environment. If ``Ec2Configuration`` isn't specified, the default is ``ECS_AL2`` . When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . To remove the EC2 configuration and any custom AMI ID specified in ``imageIdOverride`` , set this value to an empty string. One or two values can be provided. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.
            :param ec2_key_pair: The Amazon EC2 key pair that's used for instances launched in the compute environment. You can use this key pair to log in to your instances with SSH. To remove the Amazon EC2 key pair, set this value to an empty string. When updating a compute environment, changing the EC2 key pair requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.
            :param image_id: The Amazon Machine Image (AMI) ID used for instances launched in the compute environment. This parameter is overridden by the ``imageIdOverride`` member of the ``Ec2Configuration`` structure. To remove the custom AMI ID and use the default AMI ID, set this value to an empty string. When updating a compute environment, changing the AMI ID requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified. > The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param instance_role: The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ``*ecsInstanceRole*`` or ``arn:aws:iam:: *<aws_account_id>* :instance-profile/ *ecsInstanceRole*`` . For more information, see `Amazon ECS instance role <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`_ in the *AWS Batch User Guide* . When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.
            :param instance_types: The instances types that can be launched. You can specify instance families to launch any instance type within those families (for example, ``c5`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose ``optimal`` to select instance types (from the C4, M4, and R4 instance families) that match the demand of your job queues. When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified. > When you create a compute environment, the instance types that you select for the compute environment must share the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment. > Currently, ``optimal`` uses instance types from the C4, M4, and R4 instance families. In Regions that don't have instance types from those instance families, instance types from the C5, M5. and R5 instance families are used.
            :param launch_template: The launch template to use for your compute resources. Any other compute resource parameters that you specify in a `CreateComputeEnvironment <https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html>`_ API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see `Launch Template Support <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`_ in the ** . .. epigraph:: This parameter isn't applicable to jobs running on Fargate resources, and shouldn't be specified.
            :param minv_cpus: The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the compute environment is ``DISABLED`` ). .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.
            :param placement_group: The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see `Placement groups <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`_ in the *Amazon EC2 User Guide for Linux Instances* . When updating a compute environment, changing the placement group requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.
            :param security_group_ids: The Amazon EC2 security groups associated with instances launched in the compute environment. This parameter is required for Fargate compute resources, where it can contain up to 5 security groups. For Fargate compute resources, providing an empty list is handled as if this parameter wasn't specified and no change is made. For EC2 compute resources, providing an empty list removes the security groups from the compute resource. When updating a compute environment, changing the EC2 security groups requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            :param spot_iam_fleet_role: The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment. This role is required if the allocation strategy set to ``BEST_FIT`` or if the allocation strategy isn't specified. For more information, see `Amazon EC2 spot fleet role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified. > To tag your Spot Instances on creation, the Spot Fleet IAM role specified here must use the newer *AmazonEC2SpotFleetTaggingRole* managed policy. The previously recommended *AmazonEC2SpotFleetRole* managed policy doesn't have the required permissions to tag Spot Instances. For more information, see `Spot instances not tagged on creation <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#spot-instance-no-tag>`_ in the *AWS Batch User Guide* .
            :param tags: Key-value pair tags to be applied to EC2 resources that are launched in the compute environment. For AWS Batch , these take the form of "String1": "String2", where String1 is the tag key and String2 is the tag value−for example, ``{ "Name": "Batch Instance - C4OnDemand" }`` . This is helpful for recognizing your AWS Batch instances in the Amazon EC2 console. These tags aren't seen when using the AWS Batch ``ListTagsForResource`` API operation. When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.
            :param update_to_latest_image_version: Specifies whether the AMI ID is updated to the latest one that's supported by AWS Batch when the compute environment has an infrastructure update. The default value is ``false`` . .. epigraph:: If an AMI ID is specified in the ``imageId`` or ``imageIdOverride`` parameters or by the launch template specified in the ``launchTemplate`` parameter, this parameter is ignored. For more information on updating AMI IDs during an infrastructure update, see `Updating the AMI ID <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html#updating-compute-environments-ami>`_ in the *AWS Batch User Guide* . When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                compute_resources_property = batch.CfnComputeEnvironment.ComputeResourcesProperty(
                    maxv_cpus=123,
                    subnets=["subnets"],
                    type="type",
                
                    # the properties below are optional
                    allocation_strategy="allocationStrategy",
                    bid_percentage=123,
                    desiredv_cpus=123,
                    ec2_configuration=[batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty(
                        image_type="imageType",
                
                        # the properties below are optional
                        image_id_override="imageIdOverride"
                    )],
                    ec2_key_pair="ec2KeyPair",
                    image_id="imageId",
                    instance_role="instanceRole",
                    instance_types=["instanceTypes"],
                    launch_template=batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty(
                        launch_template_id="launchTemplateId",
                        launch_template_name="launchTemplateName",
                        version="version"
                    ),
                    minv_cpus=123,
                    placement_group="placementGroup",
                    security_group_ids=["securityGroupIds"],
                    spot_iam_fleet_role="spotIamFleetRole",
                    tags={
                        "tags_key": "tags"
                    },
                    update_to_latest_image_version=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnComputeEnvironment.ComputeResourcesProperty.__init__)
                check_type(argname="argument maxv_cpus", value=maxv_cpus, expected_type=type_hints["maxv_cpus"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
                check_type(argname="argument bid_percentage", value=bid_percentage, expected_type=type_hints["bid_percentage"])
                check_type(argname="argument desiredv_cpus", value=desiredv_cpus, expected_type=type_hints["desiredv_cpus"])
                check_type(argname="argument ec2_configuration", value=ec2_configuration, expected_type=type_hints["ec2_configuration"])
                check_type(argname="argument ec2_key_pair", value=ec2_key_pair, expected_type=type_hints["ec2_key_pair"])
                check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
                check_type(argname="argument instance_role", value=instance_role, expected_type=type_hints["instance_role"])
                check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
                check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
                check_type(argname="argument minv_cpus", value=minv_cpus, expected_type=type_hints["minv_cpus"])
                check_type(argname="argument placement_group", value=placement_group, expected_type=type_hints["placement_group"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument spot_iam_fleet_role", value=spot_iam_fleet_role, expected_type=type_hints["spot_iam_fleet_role"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
                check_type(argname="argument update_to_latest_image_version", value=update_to_latest_image_version, expected_type=type_hints["update_to_latest_image_version"])
            self._values: typing.Dict[str, typing.Any] = {
                "maxv_cpus": maxv_cpus,
                "subnets": subnets,
                "type": type,
            }
            if allocation_strategy is not None:
                self._values["allocation_strategy"] = allocation_strategy
            if bid_percentage is not None:
                self._values["bid_percentage"] = bid_percentage
            if desiredv_cpus is not None:
                self._values["desiredv_cpus"] = desiredv_cpus
            if ec2_configuration is not None:
                self._values["ec2_configuration"] = ec2_configuration
            if ec2_key_pair is not None:
                self._values["ec2_key_pair"] = ec2_key_pair
            if image_id is not None:
                self._values["image_id"] = image_id
            if instance_role is not None:
                self._values["instance_role"] = instance_role
            if instance_types is not None:
                self._values["instance_types"] = instance_types
            if launch_template is not None:
                self._values["launch_template"] = launch_template
            if minv_cpus is not None:
                self._values["minv_cpus"] = minv_cpus
            if placement_group is not None:
                self._values["placement_group"] = placement_group
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if spot_iam_fleet_role is not None:
                self._values["spot_iam_fleet_role"] = spot_iam_fleet_role
            if tags is not None:
                self._values["tags"] = tags
            if update_to_latest_image_version is not None:
                self._values["update_to_latest_image_version"] = update_to_latest_image_version

        @builtins.property
        def maxv_cpus(self) -> jsii.Number:
            '''The maximum number of Amazon EC2 vCPUs that an environment can reach.

            .. epigraph::

               With both ``BEST_FIT_PROGRESSIVE`` and ``SPOT_CAPACITY_OPTIMIZED`` allocation strategies, AWS Batch might need to exceed ``maxvCpus`` to meet your capacity requirements. In this event, AWS Batch never exceeds ``maxvCpus`` by more than a single instance. That is, no more than a single instance from among those specified in your compute environment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus
            '''
            result = self._values.get("maxv_cpus")
            assert result is not None, "Required property 'maxv_cpus' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''The VPC subnets where the compute resources are launched.

            Fargate compute resources can contain up to 16 subnets. For Fargate compute resources, providing an empty list will be handled as if this parameter wasn't specified and no change is made. For EC2 compute resources, providing an empty list removes the VPC subnets from the compute resource. For more information, see `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon VPC User Guide* .

            When updating a compute environment, changing the VPC subnets requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of compute environment: ``EC2`` , ``SPOT`` , ``FARGATE`` , or ``FARGATE_SPOT`` .

            For more information, see `Compute environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .

            If you choose ``SPOT`` , you must also specify an Amazon EC2 Spot Fleet role with the ``spotIamFleetRole`` parameter. For more information, see `Amazon EC2 spot fleet role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`_ in the *AWS Batch User Guide* .

            When updating compute environment, changing the type of a compute environment requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            When updating the type of a compute environment, changing between ``EC2`` and ``SPOT`` or between ``FARGATE`` and ``FARGATE_SPOT`` will initiate an infrastructure update, but if you switch between ``EC2`` and ``FARGATE`` , AWS CloudFormation will create a new compute environment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allocation_strategy(self) -> typing.Optional[builtins.str]:
            '''The allocation strategy to use for the compute resource if not enough instances of the best fitting instance type can be allocated.

            This might be because of availability of the instance type in the Region or `Amazon EC2 service limits <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ . For more information, see `Allocation strategies <https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html>`_ in the *AWS Batch User Guide* .

            When updating a compute environment, changing the allocation strategy requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . ``BEST_FIT`` is not supported when updating a compute environment.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            - **BEST_FIT (default)** - AWS Batch selects an instance type that best fits the needs of the jobs with a preference for the lowest-cost instance type. If additional instances of the selected instance type aren't available, AWS Batch waits for the additional instances to be available. If there aren't enough instances available, or if the user is reaching `Amazon EC2 service limits <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ then additional jobs aren't run until the currently running jobs have completed. This allocation strategy keeps costs lower but can limit scaling. If you are using Spot Fleets with ``BEST_FIT`` then the Spot Fleet IAM role must be specified.
            - **BEST_FIT_PROGRESSIVE** - AWS Batch will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types with a lower cost per unit vCPU. If additional instances of the previously selected instance types aren't available, AWS Batch will select new instance types.
            - **SPOT_CAPACITY_OPTIMIZED** - AWS Batch will select one or more instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types that are less likely to be interrupted. This allocation strategy is only available for Spot Instance compute resources.

            With both ``BEST_FIT_PROGRESSIVE`` and ``SPOT_CAPACITY_OPTIMIZED`` strategies, AWS Batch might need to go above ``maxvCpus`` to meet your capacity requirements. In this event, AWS Batch never exceeds ``maxvCpus`` by more than a single instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bid_percentage(self) -> typing.Optional[jsii.Number]:
            '''The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched.

            For example, if your maximum percentage is 20%, then the Spot price must be less than 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage.

            When updating a compute environment, changing the bid percentage requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage
            '''
            result = self._values.get("bid_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def desiredv_cpus(self) -> typing.Optional[jsii.Number]:
            '''The desired number of Amazon EC2 vCPUS in the compute environment.

            AWS Batch modifies this value between the minimum and maximum values based on job queue demand.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-desiredvcpus
            '''
            result = self._values.get("desiredv_cpus")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ec2_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComputeEnvironment.Ec2ConfigurationObjectProperty", _IResolvable_da3f097b]]]]:
            '''Provides information used to select Amazon Machine Images (AMIs) for EC2 instances in the compute environment.

            If ``Ec2Configuration`` isn't specified, the default is ``ECS_AL2`` .

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . To remove the EC2 configuration and any custom AMI ID specified in ``imageIdOverride`` , set this value to an empty string.

            One or two values can be provided.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration
            '''
            result = self._values.get("ec2_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComputeEnvironment.Ec2ConfigurationObjectProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def ec2_key_pair(self) -> typing.Optional[builtins.str]:
            '''The Amazon EC2 key pair that's used for instances launched in the compute environment.

            You can use this key pair to log in to your instances with SSH. To remove the Amazon EC2 key pair, set this value to an empty string.

            When updating a compute environment, changing the EC2 key pair requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair
            '''
            result = self._values.get("ec2_key_pair")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.

            This parameter is overridden by the ``imageIdOverride`` member of the ``Ec2Configuration`` structure. To remove the custom AMI ID and use the default AMI ID, set this value to an empty string.

            When updating a compute environment, changing the AMI ID requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified. > The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid
            '''
            result = self._values.get("image_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_role(self) -> typing.Optional[builtins.str]:
            '''The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment.

            You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ``*ecsInstanceRole*`` or ``arn:aws:iam:: *<aws_account_id>* :instance-profile/ *ecsInstanceRole*`` . For more information, see `Amazon ECS instance role <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`_ in the *AWS Batch User Guide* .

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole
            '''
            result = self._values.get("instance_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The instances types that can be launched.

            You can specify instance families to launch any instance type within those families (for example, ``c5`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose ``optimal`` to select instance types (from the C4, M4, and R4 instance families) that match the demand of your job queues.

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified. > When you create a compute environment, the instance types that you select for the compute environment must share the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment. > Currently, ``optimal`` uses instance types from the C4, M4, and R4 instance families. In Regions that don't have instance types from those instance families, instance types from the C5, M5. and R5 instance families are used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes
            '''
            result = self._values.get("instance_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def launch_template(
            self,
        ) -> typing.Optional[typing.Union["CfnComputeEnvironment.LaunchTemplateSpecificationProperty", _IResolvable_da3f097b]]:
            '''The launch template to use for your compute resources.

            Any other compute resource parameters that you specify in a `CreateComputeEnvironment <https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html>`_ API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see `Launch Template Support <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`_ in the ** .
            .. epigraph::

               This parameter isn't applicable to jobs running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate
            '''
            result = self._values.get("launch_template")
            return typing.cast(typing.Optional[typing.Union["CfnComputeEnvironment.LaunchTemplateSpecificationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def minv_cpus(self) -> typing.Optional[jsii.Number]:
            '''The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the compute environment is ``DISABLED`` ).

            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus
            '''
            result = self._values.get("minv_cpus")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def placement_group(self) -> typing.Optional[builtins.str]:
            '''The Amazon EC2 placement group to associate with your compute resources.

            If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see `Placement groups <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`_ in the *Amazon EC2 User Guide for Linux Instances* .

            When updating a compute environment, changing the placement group requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup
            '''
            result = self._values.get("placement_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Amazon EC2 security groups associated with instances launched in the compute environment.

            This parameter is required for Fargate compute resources, where it can contain up to 5 security groups. For Fargate compute resources, providing an empty list is handled as if this parameter wasn't specified and no change is made. For EC2 compute resources, providing an empty list removes the security groups from the compute resource.

            When updating a compute environment, changing the EC2 security groups requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def spot_iam_fleet_role(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment.

            This role is required if the allocation strategy set to ``BEST_FIT`` or if the allocation strategy isn't specified. For more information, see `Amazon EC2 spot fleet role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified. > To tag your Spot Instances on creation, the Spot Fleet IAM role specified here must use the newer *AmazonEC2SpotFleetTaggingRole* managed policy. The previously recommended *AmazonEC2SpotFleetRole* managed policy doesn't have the required permissions to tag Spot Instances. For more information, see `Spot instances not tagged on creation <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#spot-instance-no-tag>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-spotiamfleetrole
            '''
            result = self._values.get("spot_iam_fleet_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
            '''Key-value pair tags to be applied to EC2 resources that are launched in the compute environment.

            For AWS Batch , these take the form of "String1": "String2", where String1 is the tag key and String2 is the tag value−for example, ``{ "Name": "Batch Instance - C4OnDemand" }`` . This is helpful for recognizing your AWS Batch instances in the Amazon EC2 console. These tags aren't seen when using the AWS Batch ``ListTagsForResource`` API operation.

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

        @builtins.property
        def update_to_latest_image_version(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the AMI ID is updated to the latest one that's supported by AWS Batch when the compute environment has an infrastructure update.

            The default value is ``false`` .
            .. epigraph::

               If an AMI ID is specified in the ``imageId`` or ``imageIdOverride`` parameters or by the launch template specified in the ``launchTemplate`` parameter, this parameter is ignored. For more information on updating AMI IDs during an infrastructure update, see `Updating the AMI ID <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html#updating-compute-environments-ami>`_ in the *AWS Batch User Guide* .

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion
            '''
            result = self._values.get("update_to_latest_image_version")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_type": "imageType",
            "image_id_override": "imageIdOverride",
        },
    )
    class Ec2ConfigurationObjectProperty:
        def __init__(
            self,
            *,
            image_type: builtins.str,
            image_id_override: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information used to select Amazon Machine Images (AMIs) for instances in the compute environment.

            If ``Ec2Configuration`` isn't specified, the default is ``ECS_AL2`` ( `Amazon Linux 2 <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ ).
            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources.

            :param image_type: The image type to match with the instance type to select an AMI. If the ``imageIdOverride`` parameter isn't specified, then a recent `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ ( ``ECS_AL2`` ) is used. If a new image type is specified in an update, but neither an ``imageId`` nor a ``imageIdOverride`` parameter is specified, then the latest Amazon ECS optimized AMI for that image type that's supported by AWS Batch is used. - **ECS_AL2** - `Amazon Linux 2 <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ − Default for all non-GPU instance families. - **ECS_AL2_NVIDIA** - `Amazon Linux 2 (GPU) <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#gpuami>`_ −Default for all GPU instance families (for example ``P4`` and ``G4`` ) and can be used for all non AWS Graviton-based instance types. - **ECS_AL1** - `Amazon Linux <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#alami>`_ . Amazon Linux is reaching the end-of-life of standard support. For more information, see `Amazon Linux AMI <https://docs.aws.amazon.com/amazon-linux-ami/>`_ .
            :param image_id_override: The AMI ID used for instances launched in the compute environment that match the image type. This setting overrides the ``imageId`` set in the ``computeResource`` object. .. epigraph:: The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                ec2_configuration_object_property = batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty(
                    image_type="imageType",
                
                    # the properties below are optional
                    image_id_override="imageIdOverride"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnComputeEnvironment.Ec2ConfigurationObjectProperty.__init__)
                check_type(argname="argument image_type", value=image_type, expected_type=type_hints["image_type"])
                check_type(argname="argument image_id_override", value=image_id_override, expected_type=type_hints["image_id_override"])
            self._values: typing.Dict[str, typing.Any] = {
                "image_type": image_type,
            }
            if image_id_override is not None:
                self._values["image_id_override"] = image_id_override

        @builtins.property
        def image_type(self) -> builtins.str:
            '''The image type to match with the instance type to select an AMI.

            If the ``imageIdOverride`` parameter isn't specified, then a recent `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ ( ``ECS_AL2`` ) is used. If a new image type is specified in an update, but neither an ``imageId`` nor a ``imageIdOverride`` parameter is specified, then the latest Amazon ECS optimized AMI for that image type that's supported by AWS Batch is used.

            - **ECS_AL2** - `Amazon Linux 2 <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ − Default for all non-GPU instance families.
            - **ECS_AL2_NVIDIA** - `Amazon Linux 2 (GPU) <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#gpuami>`_ −Default for all GPU instance families (for example ``P4`` and ``G4`` ) and can be used for all non AWS Graviton-based instance types.
            - **ECS_AL1** - `Amazon Linux <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#alami>`_ . Amazon Linux is reaching the end-of-life of standard support. For more information, see `Amazon Linux AMI <https://docs.aws.amazon.com/amazon-linux-ami/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imagetype
            '''
            result = self._values.get("image_type")
            assert result is not None, "Required property 'image_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_id_override(self) -> typing.Optional[builtins.str]:
            '''The AMI ID used for instances launched in the compute environment that match the image type.

            This setting overrides the ``imageId`` set in the ``computeResource`` object.
            .. epigraph::

               The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imageidoverride
            '''
            result = self._values.get("image_id_override")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ec2ConfigurationObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "launch_template_id": "launchTemplateId",
            "launch_template_name": "launchTemplateName",
            "version": "version",
        },
    )
    class LaunchTemplateSpecificationProperty:
        def __init__(
            self,
            *,
            launch_template_id: typing.Optional[builtins.str] = None,
            launch_template_name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object representing a launch template associated with a compute resource.

            You must specify either the launch template ID or launch template name in the request, but not both.

            If security groups are specified using both the ``securityGroupIds`` parameter of ``CreateComputeEnvironment`` and the launch template, the values in the ``securityGroupIds`` parameter of ``CreateComputeEnvironment`` will be used.
            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources.

            :param launch_template_id: The ID of the launch template.
            :param launch_template_name: The name of the launch template.
            :param version: The version number of the launch template, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , the latest version of the launch template is used. If the value is ``$Default`` , the default version of the launch template is used. .. epigraph:: If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the ``updateToLatestImageVersion`` parameter for the compute environment is set to ``true`` . During an infrastructure update, if either ``$Latest`` or ``$Default`` is specified, AWS Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . Default: ``$Default`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                launch_template_specification_property = batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnComputeEnvironment.LaunchTemplateSpecificationProperty.__init__)
                check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
                check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[str, typing.Any] = {}
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None:
                self._values["launch_template_name"] = launch_template_name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the launch template.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_name(self) -> typing.Optional[builtins.str]:
            '''The name of the launch template.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplatename
            '''
            result = self._values.get("launch_template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version number of the launch template, ``$Latest`` , or ``$Default`` .

            If the value is ``$Latest`` , the latest version of the launch template is used. If the value is ``$Default`` , the default version of the launch template is used.
            .. epigraph::

               If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the ``updateToLatestImageVersion`` parameter for the compute environment is set to ``true`` . During an infrastructure update, if either ``$Latest`` or ``$Default`` is specified, AWS Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            Default: ``$Default`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchTemplateSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.UpdatePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "job_execution_timeout_minutes": "jobExecutionTimeoutMinutes",
            "terminate_jobs_on_update": "terminateJobsOnUpdate",
        },
    )
    class UpdatePolicyProperty:
        def __init__(
            self,
            *,
            job_execution_timeout_minutes: typing.Optional[jsii.Number] = None,
            terminate_jobs_on_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies the infrastructure update policy for the compute environment.

            For more information about infrastructure updates, see `Infrastructure updates <https://docs.aws.amazon.com/batch/latest/userguide/infrastructure-updates.html>`_ in the *AWS Batch User Guide* .

            :param job_execution_timeout_minutes: Specifies the job timeout, in minutes, when the compute environment infrastructure is updated. The default value is 30.
            :param terminate_jobs_on_update: Specifies whether jobs are automatically terminated when the computer environment infrastructure is updated. The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                update_policy_property = batch.CfnComputeEnvironment.UpdatePolicyProperty(
                    job_execution_timeout_minutes=123,
                    terminate_jobs_on_update=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnComputeEnvironment.UpdatePolicyProperty.__init__)
                check_type(argname="argument job_execution_timeout_minutes", value=job_execution_timeout_minutes, expected_type=type_hints["job_execution_timeout_minutes"])
                check_type(argname="argument terminate_jobs_on_update", value=terminate_jobs_on_update, expected_type=type_hints["terminate_jobs_on_update"])
            self._values: typing.Dict[str, typing.Any] = {}
            if job_execution_timeout_minutes is not None:
                self._values["job_execution_timeout_minutes"] = job_execution_timeout_minutes
            if terminate_jobs_on_update is not None:
                self._values["terminate_jobs_on_update"] = terminate_jobs_on_update

        @builtins.property
        def job_execution_timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''Specifies the job timeout, in minutes, when the compute environment infrastructure is updated.

            The default value is 30.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html#cfn-batch-computeenvironment-updatepolicy-jobexecutiontimeoutminutes
            '''
            result = self._values.get("job_execution_timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def terminate_jobs_on_update(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether jobs are automatically terminated when the computer environment infrastructure is updated.

            The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html#cfn-batch-computeenvironment-updatepolicy-terminatejobsonupdate
            '''
            result = self._values.get("terminate_jobs_on_update")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdatePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "compute_environment_name": "computeEnvironmentName",
        "compute_resources": "computeResources",
        "replace_compute_environment": "replaceComputeEnvironment",
        "service_role": "serviceRole",
        "state": "state",
        "tags": "tags",
        "unmanagedv_cpus": "unmanagedvCpus",
        "update_policy": "updatePolicy",
    },
)
class CfnComputeEnvironmentProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        compute_environment_name: typing.Optional[builtins.str] = None,
        compute_resources: typing.Optional[typing.Union[typing.Union[CfnComputeEnvironment.ComputeResourcesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        replace_compute_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        service_role: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        unmanagedv_cpus: typing.Optional[jsii.Number] = None,
        update_policy: typing.Optional[typing.Union[typing.Union[CfnComputeEnvironment.UpdatePolicyProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnComputeEnvironment``.

        :param type: The type of the compute environment: ``MANAGED`` or ``UNMANAGED`` . For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .
        :param compute_environment_name: The name for your compute environment. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param compute_resources: The ComputeResources property type specifies details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .
        :param replace_compute_environment: Specifies whether the compute environment should be replaced if an update is made that requires replacing the instances in the compute environment. The default value is ``true`` . To enable more properties to be updated, set this property to ``false`` . When changing the value of this property to ``false`` , no other properties should be changed at the same time. If other properties are changed at the same time, and the change needs to be rolled back but it can't, it's possible for the stack to go into the ``UPDATE_ROLLBACK_FAILED`` state. You can't update a stack that is in the ``UPDATE_ROLLBACK_FAILED`` state. However, if you can continue to roll it back, you can return the stack to its original settings and then try to update it again. For more information, see `Continue rolling back an update <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`_ in the *AWS CloudFormation User Guide* . The properties that can't be changed without replacing the compute environment are in the ```ComputeResources`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html>`_ property type: ```AllocationStrategy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ , ```BidPercentage`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage>`_ , ```Ec2Configuration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```ImageId`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ , ```InstanceRole`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole>`_ , ```InstanceTypes`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes>`_ , ```LaunchTemplate`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ , ```MaxvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus>`_ , ```MinvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus>`_ , ```PlacementGroup`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup>`_ , ```SecurityGroupIds`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids>`_ , ```Subnets`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets>`_ , `Tags <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags>`_ , ```Type`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type>`_ , and ```UpdateToLatestImageVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ .
        :param service_role: The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf. For more information, see `AWS Batch service IAM role <https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html>`_ in the *AWS Batch User Guide* . .. epigraph:: If your account already created the AWS Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the AWS Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the AWS Batch service-linked role in your account. If your specified role has a path other than ``/`` , then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` then you would specify ``/foo/bar`` as the role name. For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* . .. epigraph:: Depending on how you created your AWS Batch service role, its ARN might contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
        :param state: The state of the compute environment. If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues. If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand. If the state is ``DISABLED`` , then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state don't scale out. However, they scale in to ``minvCpus`` value after instances become idle.
        :param tags: The tags applied to the compute environment.
        :param unmanagedv_cpus: The maximum number of vCPUs for an unmanaged compute environment. This parameter is only used for fair share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair share job queue, no vCPU capacity is reserved. .. epigraph:: This parameter is only supported when the ``type`` parameter is set to ``UNMANAGED`` .
        :param update_policy: Specifies the infrastructure update policy for the compute environment. For more information about infrastructure updates, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_batch as batch
            
            cfn_compute_environment_props = batch.CfnComputeEnvironmentProps(
                type="type",
            
                # the properties below are optional
                compute_environment_name="computeEnvironmentName",
                compute_resources=batch.CfnComputeEnvironment.ComputeResourcesProperty(
                    maxv_cpus=123,
                    subnets=["subnets"],
                    type="type",
            
                    # the properties below are optional
                    allocation_strategy="allocationStrategy",
                    bid_percentage=123,
                    desiredv_cpus=123,
                    ec2_configuration=[batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty(
                        image_type="imageType",
            
                        # the properties below are optional
                        image_id_override="imageIdOverride"
                    )],
                    ec2_key_pair="ec2KeyPair",
                    image_id="imageId",
                    instance_role="instanceRole",
                    instance_types=["instanceTypes"],
                    launch_template=batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty(
                        launch_template_id="launchTemplateId",
                        launch_template_name="launchTemplateName",
                        version="version"
                    ),
                    minv_cpus=123,
                    placement_group="placementGroup",
                    security_group_ids=["securityGroupIds"],
                    spot_iam_fleet_role="spotIamFleetRole",
                    tags={
                        "tags_key": "tags"
                    },
                    update_to_latest_image_version=False
                ),
                replace_compute_environment=False,
                service_role="serviceRole",
                state="state",
                tags={
                    "tags_key": "tags"
                },
                unmanagedv_cpus=123,
                update_policy=batch.CfnComputeEnvironment.UpdatePolicyProperty(
                    job_execution_timeout_minutes=123,
                    terminate_jobs_on_update=False
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnComputeEnvironmentProps.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument compute_environment_name", value=compute_environment_name, expected_type=type_hints["compute_environment_name"])
            check_type(argname="argument compute_resources", value=compute_resources, expected_type=type_hints["compute_resources"])
            check_type(argname="argument replace_compute_environment", value=replace_compute_environment, expected_type=type_hints["replace_compute_environment"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument unmanagedv_cpus", value=unmanagedv_cpus, expected_type=type_hints["unmanagedv_cpus"])
            check_type(argname="argument update_policy", value=update_policy, expected_type=type_hints["update_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if compute_environment_name is not None:
            self._values["compute_environment_name"] = compute_environment_name
        if compute_resources is not None:
            self._values["compute_resources"] = compute_resources
        if replace_compute_environment is not None:
            self._values["replace_compute_environment"] = replace_compute_environment
        if service_role is not None:
            self._values["service_role"] = service_role
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if unmanagedv_cpus is not None:
            self._values["unmanagedv_cpus"] = unmanagedv_cpus
        if update_policy is not None:
            self._values["update_policy"] = update_policy

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the compute environment: ``MANAGED`` or ``UNMANAGED`` .

        For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compute_environment_name(self) -> typing.Optional[builtins.str]:
        '''The name for your compute environment.

        It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-computeenvironmentname
        '''
        result = self._values.get("compute_environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compute_resources(
        self,
    ) -> typing.Optional[typing.Union[CfnComputeEnvironment.ComputeResourcesProperty, _IResolvable_da3f097b]]:
        '''The ComputeResources property type specifies details of the compute resources managed by the compute environment.

        This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-computeresources
        '''
        result = self._values.get("compute_resources")
        return typing.cast(typing.Optional[typing.Union[CfnComputeEnvironment.ComputeResourcesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def replace_compute_environment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the compute environment should be replaced if an update is made that requires replacing the instances in the compute environment.

        The default value is ``true`` . To enable more properties to be updated, set this property to ``false`` . When changing the value of this property to ``false`` , no other properties should be changed at the same time. If other properties are changed at the same time, and the change needs to be rolled back but it can't, it's possible for the stack to go into the ``UPDATE_ROLLBACK_FAILED`` state. You can't update a stack that is in the ``UPDATE_ROLLBACK_FAILED`` state. However, if you can continue to roll it back, you can return the stack to its original settings and then try to update it again. For more information, see `Continue rolling back an update <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`_ in the *AWS CloudFormation User Guide* .

        The properties that can't be changed without replacing the compute environment are in the ```ComputeResources`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html>`_ property type: ```AllocationStrategy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ , ```BidPercentage`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage>`_ , ```Ec2Configuration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```ImageId`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ , ```InstanceRole`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole>`_ , ```InstanceTypes`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes>`_ , ```LaunchTemplate`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ , ```MaxvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus>`_ , ```MinvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus>`_ , ```PlacementGroup`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup>`_ , ```SecurityGroupIds`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids>`_ , ```Subnets`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets>`_ , `Tags <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags>`_ , ```Type`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type>`_ , and ```UpdateToLatestImageVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-replacecomputeenvironment
        '''
        result = self._values.get("replace_compute_environment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def service_role(self) -> typing.Optional[builtins.str]:
        '''The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

        For more information, see `AWS Batch service IAM role <https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html>`_ in the *AWS Batch User Guide* .
        .. epigraph::

           If your account already created the AWS Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the AWS Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the AWS Batch service-linked role in your account.

        If your specified role has a path other than ``/`` , then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` then you would specify ``/foo/bar`` as the role name. For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* .
        .. epigraph::

           Depending on how you created your AWS Batch service role, its ARN might contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-servicerole
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the compute environment.

        If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.

        If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.

        If the state is ``DISABLED`` , then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state don't scale out. However, they scale in to ``minvCpus`` value after instances become idle.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags applied to the compute environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def unmanagedv_cpus(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of vCPUs for an unmanaged compute environment.

        This parameter is only used for fair share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair share job queue, no vCPU capacity is reserved.
        .. epigraph::

           This parameter is only supported when the ``type`` parameter is set to ``UNMANAGED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-unmanagedvcpus
        '''
        result = self._values.get("unmanagedv_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def update_policy(
        self,
    ) -> typing.Optional[typing.Union[CfnComputeEnvironment.UpdatePolicyProperty, _IResolvable_da3f097b]]:
        '''Specifies the infrastructure update policy for the compute environment.

        For more information about infrastructure updates, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-updatepolicy
        '''
        result = self._values.get("update_policy")
        return typing.cast(typing.Optional[typing.Union[CfnComputeEnvironment.UpdatePolicyProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComputeEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnJobDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition",
):
    '''A CloudFormation ``AWS::Batch::JobDefinition``.

    The ``AWS::Batch::JobDefinition`` resource specifies the parameters for an AWS Batch job definition. For more information, see `Job Definitions <https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html>`_ in the ** .

    :cloudformationResource: AWS::Batch::JobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_batch as batch
        
        # options: Any
        # parameters: Any
        # tags: Any
        
        cfn_job_definition = batch.CfnJobDefinition(self, "MyCfnJobDefinition",
            type="type",
        
            # the properties below are optional
            container_properties=batch.CfnJobDefinition.ContainerPropertiesProperty(
                image="image",
        
                # the properties below are optional
                command=["command"],
                environment=[batch.CfnJobDefinition.EnvironmentProperty(
                    name="name",
                    value="value"
                )],
                execution_role_arn="executionRoleArn",
                fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                    platform_version="platformVersion"
                ),
                instance_type="instanceType",
                job_role_arn="jobRoleArn",
                linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                    devices=[batch.CfnJobDefinition.DeviceProperty(
                        container_path="containerPath",
                        host_path="hostPath",
                        permissions=["permissions"]
                    )],
                    init_process_enabled=False,
                    max_swap=123,
                    shared_memory_size=123,
                    swappiness=123,
                    tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                        container_path="containerPath",
                        size=123,
        
                        # the properties below are optional
                        mount_options=["mountOptions"]
                    )]
                ),
                log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                    log_driver="logDriver",
        
                    # the properties below are optional
                    options=options,
                    secret_options=[batch.CfnJobDefinition.SecretProperty(
                        name="name",
                        value_from="valueFrom"
                    )]
                ),
                memory=123,
                mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                    container_path="containerPath",
                    read_only=False,
                    source_volume="sourceVolume"
                )],
                network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                    assign_public_ip="assignPublicIp"
                ),
                privileged=False,
                readonly_root_filesystem=False,
                resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                    type="type",
                    value="value"
                )],
                secrets=[batch.CfnJobDefinition.SecretProperty(
                    name="name",
                    value_from="valueFrom"
                )],
                ulimits=[batch.CfnJobDefinition.UlimitProperty(
                    hard_limit=123,
                    name="name",
                    soft_limit=123
                )],
                user="user",
                vcpus=123,
                volumes=[batch.CfnJobDefinition.VolumesProperty(
                    efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                        file_system_id="fileSystemId",
        
                        # the properties below are optional
                        authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                            access_point_id="accessPointId",
                            iam="iam"
                        ),
                        root_directory="rootDirectory",
                        transit_encryption="transitEncryption",
                        transit_encryption_port=123
                    ),
                    host=batch.CfnJobDefinition.VolumesHostProperty(
                        source_path="sourcePath"
                    ),
                    name="name"
                )]
            ),
            job_definition_name="jobDefinitionName",
            node_properties=batch.CfnJobDefinition.NodePropertiesProperty(
                main_node=123,
                node_range_properties=[batch.CfnJobDefinition.NodeRangePropertyProperty(
                    target_nodes="targetNodes",
        
                    # the properties below are optional
                    container=batch.CfnJobDefinition.ContainerPropertiesProperty(
                        image="image",
        
                        # the properties below are optional
                        command=["command"],
                        environment=[batch.CfnJobDefinition.EnvironmentProperty(
                            name="name",
                            value="value"
                        )],
                        execution_role_arn="executionRoleArn",
                        fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                            platform_version="platformVersion"
                        ),
                        instance_type="instanceType",
                        job_role_arn="jobRoleArn",
                        linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                            devices=[batch.CfnJobDefinition.DeviceProperty(
                                container_path="containerPath",
                                host_path="hostPath",
                                permissions=["permissions"]
                            )],
                            init_process_enabled=False,
                            max_swap=123,
                            shared_memory_size=123,
                            swappiness=123,
                            tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                                container_path="containerPath",
                                size=123,
        
                                # the properties below are optional
                                mount_options=["mountOptions"]
                            )]
                        ),
                        log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                            log_driver="logDriver",
        
                            # the properties below are optional
                            options=options,
                            secret_options=[batch.CfnJobDefinition.SecretProperty(
                                name="name",
                                value_from="valueFrom"
                            )]
                        ),
                        memory=123,
                        mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                            container_path="containerPath",
                            read_only=False,
                            source_volume="sourceVolume"
                        )],
                        network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                            assign_public_ip="assignPublicIp"
                        ),
                        privileged=False,
                        readonly_root_filesystem=False,
                        resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                            type="type",
                            value="value"
                        )],
                        secrets=[batch.CfnJobDefinition.SecretProperty(
                            name="name",
                            value_from="valueFrom"
                        )],
                        ulimits=[batch.CfnJobDefinition.UlimitProperty(
                            hard_limit=123,
                            name="name",
                            soft_limit=123
                        )],
                        user="user",
                        vcpus=123,
                        volumes=[batch.CfnJobDefinition.VolumesProperty(
                            efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                                file_system_id="fileSystemId",
        
                                # the properties below are optional
                                authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                    access_point_id="accessPointId",
                                    iam="iam"
                                ),
                                root_directory="rootDirectory",
                                transit_encryption="transitEncryption",
                                transit_encryption_port=123
                            ),
                            host=batch.CfnJobDefinition.VolumesHostProperty(
                                source_path="sourcePath"
                            ),
                            name="name"
                        )]
                    )
                )],
                num_nodes=123
            ),
            parameters=parameters,
            platform_capabilities=["platformCapabilities"],
            propagate_tags=False,
            retry_strategy=batch.CfnJobDefinition.RetryStrategyProperty(
                attempts=123,
                evaluate_on_exit=[batch.CfnJobDefinition.EvaluateOnExitProperty(
                    action="action",
        
                    # the properties below are optional
                    on_exit_code="onExitCode",
                    on_reason="onReason",
                    on_status_reason="onStatusReason"
                )]
            ),
            scheduling_priority=123,
            tags=tags,
            timeout=batch.CfnJobDefinition.TimeoutProperty(
                attempt_duration_seconds=123
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        container_properties: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.ContainerPropertiesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        job_definition_name: typing.Optional[builtins.str] = None,
        node_properties: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.NodePropertiesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        parameters: typing.Any = None,
        platform_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        propagate_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        retry_strategy: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.RetryStrategyProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        scheduling_priority: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        timeout: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.TimeoutProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::Batch::JobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param type: The type of job definition. For more information about multi-node parallel jobs, see `Creating a multi-node parallel job definition <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html>`_ in the *AWS Batch User Guide* . .. epigraph:: If the job is run on Fargate resources, then ``multinode`` isn't supported.
        :param container_properties: An object with various properties specific to container-based jobs.
        :param job_definition_name: The name of the job definition.
        :param node_properties: An object with various properties specific to multi-node parallel jobs. .. epigraph:: If the job runs on Fargate resources, then you must not specify ``nodeProperties`` ; use ``containerProperties`` instead.
        :param parameters: Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see `Job definition parameters <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`_ in the *AWS Batch User Guide* .
        :param platform_capabilities: The platform capabilities required by the job definition. If no value is specified, it defaults to ``EC2`` . Jobs run on Fargate resources specify ``FARGATE`` .
        :param propagate_tags: Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the ``FAILED`` state.
        :param retry_strategy: The retry strategy to use for failed jobs that are submitted with this job definition.
        :param scheduling_priority: The scheduling priority of the job definition. This only affects jobs in job queues with a fair share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.
        :param tags: The tags applied to the job definition.
        :param timeout: The timeout configuration for jobs that are submitted with this job definition. You can specify a timeout duration after which AWS Batch terminates your jobs if they haven't finished.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobDefinition.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobDefinitionProps(
            type=type,
            container_properties=container_properties,
            job_definition_name=job_definition_name,
            node_properties=node_properties,
            parameters=parameters,
            platform_capabilities=platform_capabilities,
            propagate_tags=propagate_tags,
            retry_strategy=retry_strategy,
            scheduling_priority=scheduling_priority,
            tags=tags,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobDefinition.inspect)
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
            type_hints = typing.get_type_hints(CfnJobDefinition._render_properties)
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
        '''The tags applied to the job definition.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''Default parameters or parameter substitution placeholders that are set in the job definition.

        Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see `Job definition parameters <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`_ in the *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-parameters
        '''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of job definition.

        For more information about multi-node parallel jobs, see `Creating a multi-node parallel job definition <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html>`_ in the *AWS Batch User Guide* .
        .. epigraph::

           If the job is run on Fargate resources, then ``multinode`` isn't supported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containerProperties")
    def container_properties(
        self,
    ) -> typing.Optional[typing.Union["CfnJobDefinition.ContainerPropertiesProperty", _IResolvable_da3f097b]]:
        '''An object with various properties specific to container-based jobs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-containerproperties
        '''
        return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.ContainerPropertiesProperty", _IResolvable_da3f097b]], jsii.get(self, "containerProperties"))

    @container_properties.setter
    def container_properties(
        self,
        value: typing.Optional[typing.Union["CfnJobDefinition.ContainerPropertiesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "container_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerProperties", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job definition.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "job_definition_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nodeProperties")
    def node_properties(
        self,
    ) -> typing.Optional[typing.Union["CfnJobDefinition.NodePropertiesProperty", _IResolvable_da3f097b]]:
        '''An object with various properties specific to multi-node parallel jobs.

        .. epigraph::

           If the job runs on Fargate resources, then you must not specify ``nodeProperties`` ; use ``containerProperties`` instead.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-nodeproperties
        '''
        return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.NodePropertiesProperty", _IResolvable_da3f097b]], jsii.get(self, "nodeProperties"))

    @node_properties.setter
    def node_properties(
        self,
        value: typing.Optional[typing.Union["CfnJobDefinition.NodePropertiesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "node_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeProperties", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="platformCapabilities")
    def platform_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The platform capabilities required by the job definition.

        If no value is specified, it defaults to ``EC2`` . Jobs run on Fargate resources specify ``FARGATE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-platformcapabilities
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "platformCapabilities"))

    @platform_capabilities.setter
    def platform_capabilities(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "platform_capabilities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformCapabilities", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task.

        If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the ``FAILED`` state.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-propagatetags
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "propagate_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="retryStrategy")
    def retry_strategy(
        self,
    ) -> typing.Optional[typing.Union["CfnJobDefinition.RetryStrategyProperty", _IResolvable_da3f097b]]:
        '''The retry strategy to use for failed jobs that are submitted with this job definition.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-retrystrategy
        '''
        return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.RetryStrategyProperty", _IResolvable_da3f097b]], jsii.get(self, "retryStrategy"))

    @retry_strategy.setter
    def retry_strategy(
        self,
        value: typing.Optional[typing.Union["CfnJobDefinition.RetryStrategyProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "retry_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryStrategy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedulingPriority")
    def scheduling_priority(self) -> typing.Optional[jsii.Number]:
        '''The scheduling priority of the job definition.

        This only affects jobs in job queues with a fair share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-schedulingpriority
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "schedulingPriority"))

    @scheduling_priority.setter
    def scheduling_priority(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "scheduling_priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingPriority", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeout")
    def timeout(
        self,
    ) -> typing.Optional[typing.Union["CfnJobDefinition.TimeoutProperty", _IResolvable_da3f097b]]:
        '''The timeout configuration for jobs that are submitted with this job definition.

        You can specify a timeout duration after which AWS Batch terminates your jobs if they haven't finished.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-timeout
        '''
        return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.TimeoutProperty", _IResolvable_da3f097b]], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(
        self,
        value: typing.Optional[typing.Union["CfnJobDefinition.TimeoutProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobDefinition, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.AuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"access_point_id": "accessPointId", "iam": "iam"},
    )
    class AuthorizationConfigProperty:
        def __init__(
            self,
            *,
            access_point_id: typing.Optional[builtins.str] = None,
            iam: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The authorization configuration details for the Amazon EFS file system.

            :param access_point_id: The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the ``EFSVolumeConfiguration`` must either be omitted or set to ``/`` which will enforce the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the ``EFSVolumeConfiguration`` . For more information, see `Working with Amazon EFS access points <https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html>`_ in the *Amazon Elastic File System User Guide* .
            :param iam: Whether or not to use the AWS Batch job IAM role defined in a job definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the ``EFSVolumeConfiguration`` . If this parameter is omitted, the default value of ``DISABLED`` is used. For more information, see `Using Amazon EFS access points <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints>`_ in the *AWS Batch User Guide* . EFS IAM authorization requires that ``TransitEncryption`` be ``ENABLED`` and that a ``JobRoleArn`` is specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                authorization_config_property = batch.CfnJobDefinition.AuthorizationConfigProperty(
                    access_point_id="accessPointId",
                    iam="iam"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.AuthorizationConfigProperty.__init__)
                check_type(argname="argument access_point_id", value=access_point_id, expected_type=type_hints["access_point_id"])
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
            self._values: typing.Dict[str, typing.Any] = {}
            if access_point_id is not None:
                self._values["access_point_id"] = access_point_id
            if iam is not None:
                self._values["iam"] = iam

        @builtins.property
        def access_point_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon EFS access point ID to use.

            If an access point is specified, the root directory value specified in the ``EFSVolumeConfiguration`` must either be omitted or set to ``/`` which will enforce the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the ``EFSVolumeConfiguration`` . For more information, see `Working with Amazon EFS access points <https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html>`_ in the *Amazon Elastic File System User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html#cfn-batch-jobdefinition-authorizationconfig-accesspointid
            '''
            result = self._values.get("access_point_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iam(self) -> typing.Optional[builtins.str]:
            '''Whether or not to use the AWS Batch job IAM role defined in a job definition when mounting the Amazon EFS file system.

            If enabled, transit encryption must be enabled in the ``EFSVolumeConfiguration`` . If this parameter is omitted, the default value of ``DISABLED`` is used. For more information, see `Using Amazon EFS access points <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints>`_ in the *AWS Batch User Guide* . EFS IAM authorization requires that ``TransitEncryption`` be ``ENABLED`` and that a ``JobRoleArn`` is specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html#cfn-batch-jobdefinition-authorizationconfig-iam
            '''
            result = self._values.get("iam")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.ContainerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image": "image",
            "command": "command",
            "environment": "environment",
            "execution_role_arn": "executionRoleArn",
            "fargate_platform_configuration": "fargatePlatformConfiguration",
            "instance_type": "instanceType",
            "job_role_arn": "jobRoleArn",
            "linux_parameters": "linuxParameters",
            "log_configuration": "logConfiguration",
            "memory": "memory",
            "mount_points": "mountPoints",
            "network_configuration": "networkConfiguration",
            "privileged": "privileged",
            "readonly_root_filesystem": "readonlyRootFilesystem",
            "resource_requirements": "resourceRequirements",
            "secrets": "secrets",
            "ulimits": "ulimits",
            "user": "user",
            "vcpus": "vcpus",
            "volumes": "volumes",
        },
    )
    class ContainerPropertiesProperty:
        def __init__(
            self,
            *,
            image: builtins.str,
            command: typing.Optional[typing.Sequence[builtins.str]] = None,
            environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.EnvironmentProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            execution_role_arn: typing.Optional[builtins.str] = None,
            fargate_platform_configuration: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.FargatePlatformConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            instance_type: typing.Optional[builtins.str] = None,
            job_role_arn: typing.Optional[builtins.str] = None,
            linux_parameters: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.LinuxParametersProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            log_configuration: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.LogConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            memory: typing.Optional[jsii.Number] = None,
            mount_points: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.MountPointsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            network_configuration: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.NetworkConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            privileged: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            readonly_root_filesystem: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            resource_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.ResourceRequirementProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            secrets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.SecretProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            ulimits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.UlimitProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            user: typing.Optional[builtins.str] = None,
            vcpus: typing.Optional[jsii.Number] = None,
            volumes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.VolumesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Container properties are used in job definitions to describe the container that's launched as part of a job.

            :param image: The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with ``*repository-url* / *image* : *tag*`` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``IMAGE`` parameter of `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: Docker image architecture must match the processor architecture of the compute resources that they're scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources. - Images in Amazon ECR Public repositories use the full ``registry/repository[:tag]`` or ``registry/repository[@digest]`` naming conventions. For example, ``public.ecr.aws/ *registry_alias* / *my-web-app* : *latest*`` . - Images in Amazon ECR repositories use the full registry and repository URI (for example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ). - Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). - Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). - Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ).
            :param command: The command that's passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``COMMAND`` parameter to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . For more information, see `https://docs.docker.com/engine/reference/builder/#cmd <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/builder/#cmd>`_ .
            :param environment: The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--env`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: We don't recommend using plaintext environment variables for sensitive information, such as credential data. > Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.
            :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see `AWS Batch execution IAM role <https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html>`_ in the *AWS Batch User Guide* .
            :param fargate_platform_configuration: The platform configuration for jobs that are running on Fargate resources. Jobs that are running on EC2 resources must not specify this parameter.
            :param instance_type: The instance type to use for a multi-node parallel job. All node groups in a multi-node parallel job must use the same instance type. .. epigraph:: This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.
            :param job_role_arn: The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions. For more information, see `IAM roles for tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param linux_parameters: Linux-specific modifications that are applied to the container, such as details for device mappings.
            :param log_configuration: The log configuration specification for the container. This parameter maps to ``LogConfig`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--log-driver`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.aws.amazon.com/https://docs.docker.com/engine/admin/logging/overview/>`_ in the Docker documentation. .. epigraph:: AWS Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the ``LogConfiguration`` data type). This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log into your container instance and run the following command: ``sudo docker version | grep "Server API version"`` .. epigraph:: The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS container agent configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param memory: This parameter is deprecated, use ``resourceRequirements`` to specify the memory requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs running on EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, it's terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.
            :param mount_points: The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--volume`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            :param network_configuration: The network configuration for jobs that are running on Fargate resources. Jobs that are running on EC2 resources must not specify this parameter.
            :param privileged: When this parameter is true, the container is given elevated permissions on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--privileged`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . The default value is false. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as false.
            :param readonly_root_filesystem: When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--read-only`` option to ``docker run`` .
            :param resource_requirements: The type and amount of resources to assign to a container. The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .
            :param secrets: The secrets for the container. For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .
            :param ulimits: A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--ulimit`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
            :param user: The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--user`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            :param vcpus: This parameter is deprecated, use ``resourceRequirements`` to specify the vCPU requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs running on EC2 resources, it specifies the number of vCPUs reserved for the job. Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.
            :param volumes: A list of data volumes used in a job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # options: Any
                
                container_properties_property = batch.CfnJobDefinition.ContainerPropertiesProperty(
                    image="image",
                
                    # the properties below are optional
                    command=["command"],
                    environment=[batch.CfnJobDefinition.EnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    execution_role_arn="executionRoleArn",
                    fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                        platform_version="platformVersion"
                    ),
                    instance_type="instanceType",
                    job_role_arn="jobRoleArn",
                    linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                        devices=[batch.CfnJobDefinition.DeviceProperty(
                            container_path="containerPath",
                            host_path="hostPath",
                            permissions=["permissions"]
                        )],
                        init_process_enabled=False,
                        max_swap=123,
                        shared_memory_size=123,
                        swappiness=123,
                        tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                            container_path="containerPath",
                            size=123,
                
                            # the properties below are optional
                            mount_options=["mountOptions"]
                        )]
                    ),
                    log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                        log_driver="logDriver",
                
                        # the properties below are optional
                        options=options,
                        secret_options=[batch.CfnJobDefinition.SecretProperty(
                            name="name",
                            value_from="valueFrom"
                        )]
                    ),
                    memory=123,
                    mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                        container_path="containerPath",
                        read_only=False,
                        source_volume="sourceVolume"
                    )],
                    network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                        assign_public_ip="assignPublicIp"
                    ),
                    privileged=False,
                    readonly_root_filesystem=False,
                    resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                        type="type",
                        value="value"
                    )],
                    secrets=[batch.CfnJobDefinition.SecretProperty(
                        name="name",
                        value_from="valueFrom"
                    )],
                    ulimits=[batch.CfnJobDefinition.UlimitProperty(
                        hard_limit=123,
                        name="name",
                        soft_limit=123
                    )],
                    user="user",
                    vcpus=123,
                    volumes=[batch.CfnJobDefinition.VolumesProperty(
                        efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                            file_system_id="fileSystemId",
                
                            # the properties below are optional
                            authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                access_point_id="accessPointId",
                                iam="iam"
                            ),
                            root_directory="rootDirectory",
                            transit_encryption="transitEncryption",
                            transit_encryption_port=123
                        ),
                        host=batch.CfnJobDefinition.VolumesHostProperty(
                            source_path="sourcePath"
                        ),
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.ContainerPropertiesProperty.__init__)
                check_type(argname="argument image", value=image, expected_type=type_hints["image"])
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
                check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
                check_type(argname="argument fargate_platform_configuration", value=fargate_platform_configuration, expected_type=type_hints["fargate_platform_configuration"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument job_role_arn", value=job_role_arn, expected_type=type_hints["job_role_arn"])
                check_type(argname="argument linux_parameters", value=linux_parameters, expected_type=type_hints["linux_parameters"])
                check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
                check_type(argname="argument mount_points", value=mount_points, expected_type=type_hints["mount_points"])
                check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
                check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
                check_type(argname="argument readonly_root_filesystem", value=readonly_root_filesystem, expected_type=type_hints["readonly_root_filesystem"])
                check_type(argname="argument resource_requirements", value=resource_requirements, expected_type=type_hints["resource_requirements"])
                check_type(argname="argument secrets", value=secrets, expected_type=type_hints["secrets"])
                check_type(argname="argument ulimits", value=ulimits, expected_type=type_hints["ulimits"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
                check_type(argname="argument vcpus", value=vcpus, expected_type=type_hints["vcpus"])
                check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            self._values: typing.Dict[str, typing.Any] = {
                "image": image,
            }
            if command is not None:
                self._values["command"] = command
            if environment is not None:
                self._values["environment"] = environment
            if execution_role_arn is not None:
                self._values["execution_role_arn"] = execution_role_arn
            if fargate_platform_configuration is not None:
                self._values["fargate_platform_configuration"] = fargate_platform_configuration
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if job_role_arn is not None:
                self._values["job_role_arn"] = job_role_arn
            if linux_parameters is not None:
                self._values["linux_parameters"] = linux_parameters
            if log_configuration is not None:
                self._values["log_configuration"] = log_configuration
            if memory is not None:
                self._values["memory"] = memory
            if mount_points is not None:
                self._values["mount_points"] = mount_points
            if network_configuration is not None:
                self._values["network_configuration"] = network_configuration
            if privileged is not None:
                self._values["privileged"] = privileged
            if readonly_root_filesystem is not None:
                self._values["readonly_root_filesystem"] = readonly_root_filesystem
            if resource_requirements is not None:
                self._values["resource_requirements"] = resource_requirements
            if secrets is not None:
                self._values["secrets"] = secrets
            if ulimits is not None:
                self._values["ulimits"] = ulimits
            if user is not None:
                self._values["user"] = user
            if vcpus is not None:
                self._values["vcpus"] = vcpus
            if volumes is not None:
                self._values["volumes"] = volumes

        @builtins.property
        def image(self) -> builtins.str:
            '''The image used to start a container.

            This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with ``*repository-url* / *image* : *tag*`` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``IMAGE`` parameter of `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               Docker image architecture must match the processor architecture of the compute resources that they're scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.

            - Images in Amazon ECR Public repositories use the full ``registry/repository[:tag]`` or ``registry/repository[@digest]`` naming conventions. For example, ``public.ecr.aws/ *registry_alias* / *my-web-app* : *latest*`` .
            - Images in Amazon ECR repositories use the full registry and repository URI (for example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).
            - Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ).
            - Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ).
            - Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-image
            '''
            result = self._values.get("image")
            assert result is not None, "Required property 'image' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The command that's passed to the container.

            This parameter maps to ``Cmd`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``COMMAND`` parameter to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . For more information, see `https://docs.docker.com/engine/reference/builder/#cmd <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/builder/#cmd>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-command
            '''
            result = self._values.get("command")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.EnvironmentProperty", _IResolvable_da3f097b]]]]:
            '''The environment variables to pass to a container.

            This parameter maps to ``Env`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--env`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               We don't recommend using plaintext environment variables for sensitive information, such as credential data. > Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.EnvironmentProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def execution_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume.

            For jobs that run on Fargate resources, you must provide an execution role. For more information, see `AWS Batch execution IAM role <https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-executionrolearn
            '''
            result = self._values.get("execution_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fargate_platform_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnJobDefinition.FargatePlatformConfigurationProperty", _IResolvable_da3f097b]]:
            '''The platform configuration for jobs that are running on Fargate resources.

            Jobs that are running on EC2 resources must not specify this parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-fargateplatformconfiguration
            '''
            result = self._values.get("fargate_platform_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.FargatePlatformConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''The instance type to use for a multi-node parallel job.

            All node groups in a multi-node parallel job must use the same instance type.
            .. epigraph::

               This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def job_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.

            For more information, see `IAM roles for tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-jobrolearn
            '''
            result = self._values.get("job_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def linux_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnJobDefinition.LinuxParametersProperty", _IResolvable_da3f097b]]:
            '''Linux-specific modifications that are applied to the container, such as details for device mappings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-linuxparameters
            '''
            result = self._values.get("linux_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.LinuxParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def log_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnJobDefinition.LogConfigurationProperty", _IResolvable_da3f097b]]:
            '''The log configuration specification for the container.

            This parameter maps to ``LogConfig`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--log-driver`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.aws.amazon.com/https://docs.docker.com/engine/admin/logging/overview/>`_ in the Docker documentation.
            .. epigraph::

               AWS Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the ``LogConfiguration`` data type).

            This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log into your container instance and run the following command: ``sudo docker version | grep "Server API version"``
            .. epigraph::

               The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS container agent configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-logconfiguration
            '''
            result = self._values.get("log_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.LogConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def memory(self) -> typing.Optional[jsii.Number]:
            '''This parameter is deprecated, use ``resourceRequirements`` to specify the memory requirements for the job definition.

            It's not supported for jobs running on Fargate resources. For jobs running on EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, it's terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_points(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.MountPointsProperty", _IResolvable_da3f097b]]]]:
            '''The mount points for data volumes in your container.

            This parameter maps to ``Volumes`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--volume`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-mountpoints
            '''
            result = self._values.get("mount_points")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.MountPointsProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def network_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnJobDefinition.NetworkConfigurationProperty", _IResolvable_da3f097b]]:
            '''The network configuration for jobs that are running on Fargate resources.

            Jobs that are running on EC2 resources must not specify this parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-networkconfiguration
            '''
            result = self._values.get("network_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.NetworkConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def privileged(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When this parameter is true, the container is given elevated permissions on the host container instance (similar to the ``root`` user).

            This parameter maps to ``Privileged`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--privileged`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . The default value is false.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as false.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-privileged
            '''
            result = self._values.get("privileged")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def readonly_root_filesystem(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When this parameter is true, the container is given read-only access to its root file system.

            This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--read-only`` option to ``docker run`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-readonlyrootfilesystem
            '''
            result = self._values.get("readonly_root_filesystem")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def resource_requirements(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.ResourceRequirementProperty", _IResolvable_da3f097b]]]]:
            '''The type and amount of resources to assign to a container.

            The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-resourcerequirements
            '''
            result = self._values.get("resource_requirements")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.ResourceRequirementProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def secrets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.SecretProperty", _IResolvable_da3f097b]]]]:
            '''The secrets for the container.

            For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-secrets
            '''
            result = self._values.get("secrets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.SecretProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def ulimits(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.UlimitProperty", _IResolvable_da3f097b]]]]:
            '''A list of ``ulimits`` to set in the container.

            This parameter maps to ``Ulimits`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--ulimit`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-ulimits
            '''
            result = self._values.get("ulimits")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.UlimitProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def user(self) -> typing.Optional[builtins.str]:
            '''The user name to use inside the container.

            This parameter maps to ``User`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--user`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-user
            '''
            result = self._values.get("user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vcpus(self) -> typing.Optional[jsii.Number]:
            '''This parameter is deprecated, use ``resourceRequirements`` to specify the vCPU requirements for the job definition.

            It's not supported for jobs running on Fargate resources. For jobs running on EC2 resources, it specifies the number of vCPUs reserved for the job.

            Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-vcpus
            '''
            result = self._values.get("vcpus")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volumes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.VolumesProperty", _IResolvable_da3f097b]]]]:
            '''A list of data volumes used in a job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-volumes
            '''
            result = self._values.get("volumes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.VolumesProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.DeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_path": "containerPath",
            "host_path": "hostPath",
            "permissions": "permissions",
        },
    )
    class DeviceProperty:
        def __init__(
            self,
            *,
            container_path: typing.Optional[builtins.str] = None,
            host_path: typing.Optional[builtins.str] = None,
            permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''An object representing a container instance host device.

            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :param container_path: The path inside the container that's used to expose the host device. By default, the ``hostPath`` value is used.
            :param host_path: The path for the device on the host container instance.
            :param permissions: The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                device_property = batch.CfnJobDefinition.DeviceProperty(
                    container_path="containerPath",
                    host_path="hostPath",
                    permissions=["permissions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.DeviceProperty.__init__)
                check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
                check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
                check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            self._values: typing.Dict[str, typing.Any] = {}
            if container_path is not None:
                self._values["container_path"] = container_path
            if host_path is not None:
                self._values["host_path"] = host_path
            if permissions is not None:
                self._values["permissions"] = permissions

        @builtins.property
        def container_path(self) -> typing.Optional[builtins.str]:
            '''The path inside the container that's used to expose the host device.

            By default, the ``hostPath`` value is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-containerpath
            '''
            result = self._values.get("container_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def host_path(self) -> typing.Optional[builtins.str]:
            '''The path for the device on the host container instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-hostpath
            '''
            result = self._values.get("host_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The explicit permissions to provide to the container for the device.

            By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-permissions
            '''
            result = self._values.get("permissions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EfsVolumeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "file_system_id": "fileSystemId",
            "authorization_config": "authorizationConfig",
            "root_directory": "rootDirectory",
            "transit_encryption": "transitEncryption",
            "transit_encryption_port": "transitEncryptionPort",
        },
    )
    class EfsVolumeConfigurationProperty:
        def __init__(
            self,
            *,
            file_system_id: builtins.str,
            authorization_config: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.AuthorizationConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            root_directory: typing.Optional[builtins.str] = None,
            transit_encryption: typing.Optional[builtins.str] = None,
            transit_encryption_port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''This is used when you're using an Amazon Elastic File System file system for job storage.

            For more information, see `Amazon EFS Volumes <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html>`_ in the *AWS Batch User Guide* .

            :param file_system_id: The Amazon EFS file system ID to use.
            :param authorization_config: The authorization configuration details for the Amazon EFS file system.
            :param root_directory: The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying ``/`` has the same effect as omitting this parameter. The maximum length is 4,096 characters. .. epigraph:: If an EFS access point is specified in the ``authorizationConfig`` , the root directory parameter must either be omitted or set to ``/`` , which enforces the path set on the Amazon EFS access point.
            :param transit_encryption: Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of ``DISABLED`` is used. For more information, see `Encrypting data in transit <https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html>`_ in the *Amazon Elastic File System User Guide* .
            :param transit_encryption_port: The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you don't specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see `EFS mount helper <https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html>`_ in the *Amazon Elastic File System User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                efs_volume_configuration_property = batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                    file_system_id="fileSystemId",
                
                    # the properties below are optional
                    authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                        access_point_id="accessPointId",
                        iam="iam"
                    ),
                    root_directory="rootDirectory",
                    transit_encryption="transitEncryption",
                    transit_encryption_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.EfsVolumeConfigurationProperty.__init__)
                check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
                check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
                check_type(argname="argument transit_encryption", value=transit_encryption, expected_type=type_hints["transit_encryption"])
                check_type(argname="argument transit_encryption_port", value=transit_encryption_port, expected_type=type_hints["transit_encryption_port"])
            self._values: typing.Dict[str, typing.Any] = {
                "file_system_id": file_system_id,
            }
            if authorization_config is not None:
                self._values["authorization_config"] = authorization_config
            if root_directory is not None:
                self._values["root_directory"] = root_directory
            if transit_encryption is not None:
                self._values["transit_encryption"] = transit_encryption
            if transit_encryption_port is not None:
                self._values["transit_encryption_port"] = transit_encryption_port

        @builtins.property
        def file_system_id(self) -> builtins.str:
            '''The Amazon EFS file system ID to use.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-filesystemid
            '''
            result = self._values.get("file_system_id")
            assert result is not None, "Required property 'file_system_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Optional[typing.Union["CfnJobDefinition.AuthorizationConfigProperty", _IResolvable_da3f097b]]:
            '''The authorization configuration details for the Amazon EFS file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.AuthorizationConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def root_directory(self) -> typing.Optional[builtins.str]:
            '''The directory within the Amazon EFS file system to mount as the root directory inside the host.

            If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying ``/`` has the same effect as omitting this parameter. The maximum length is 4,096 characters.
            .. epigraph::

               If an EFS access point is specified in the ``authorizationConfig`` , the root directory parameter must either be omitted or set to ``/`` , which enforces the path set on the Amazon EFS access point.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-rootdirectory
            '''
            result = self._values.get("root_directory")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transit_encryption(self) -> typing.Optional[builtins.str]:
            '''Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server.

            Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of ``DISABLED`` is used. For more information, see `Encrypting data in transit <https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html>`_ in the *Amazon Elastic File System User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-transitencryption
            '''
            result = self._values.get("transit_encryption")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transit_encryption_port(self) -> typing.Optional[jsii.Number]:
            '''The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server.

            If you don't specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see `EFS mount helper <https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html>`_ in the *Amazon Elastic File System User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-transitencryptionport
            '''
            result = self._values.get("transit_encryption_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EfsVolumeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Environment property type specifies environment variables to use in a job definition.

            :param name: The name of the environment variable.
            :param value: The value of the environment variable.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                environment_property = batch.CfnJobDefinition.EnvironmentProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.EnvironmentProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the environment variable.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html#cfn-batch-jobdefinition-environment-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the environment variable.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html#cfn-batch-jobdefinition-environment-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EvaluateOnExitProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "on_exit_code": "onExitCode",
            "on_reason": "onReason",
            "on_status_reason": "onStatusReason",
        },
    )
    class EvaluateOnExitProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            on_exit_code: typing.Optional[builtins.str] = None,
            on_reason: typing.Optional[builtins.str] = None,
            on_status_reason: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies a set of conditions to be met, and an action to take ( ``RETRY`` or ``EXIT`` ) if all conditions are met.

            :param action: Specifies the action to take if all of the specified conditions ( ``onStatusReason`` , ``onReason`` , and ``onExitCode`` ) are met. The values aren't case sensitive.
            :param on_exit_code: Contains a glob pattern to match against the decimal representation of the ``ExitCode`` returned for a job. The pattern can be up to 512 characters in length. It can contain only numbers, and can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match. The string can be between 1 and 512 characters in length.
            :param on_reason: Contains a glob pattern to match against the ``Reason`` returned for a job. The pattern can be up to 512 characters in length. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces and tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match. The string can be between 1 and 512 characters in length.
            :param on_status_reason: Contains a glob pattern to match against the ``StatusReason`` returned for a job. The pattern can be up to 512 characters in length. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces or tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match. The string can be between 1 and 512 characters in length.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                evaluate_on_exit_property = batch.CfnJobDefinition.EvaluateOnExitProperty(
                    action="action",
                
                    # the properties below are optional
                    on_exit_code="onExitCode",
                    on_reason="onReason",
                    on_status_reason="onStatusReason"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.EvaluateOnExitProperty.__init__)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument on_exit_code", value=on_exit_code, expected_type=type_hints["on_exit_code"])
                check_type(argname="argument on_reason", value=on_reason, expected_type=type_hints["on_reason"])
                check_type(argname="argument on_status_reason", value=on_status_reason, expected_type=type_hints["on_status_reason"])
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
            }
            if on_exit_code is not None:
                self._values["on_exit_code"] = on_exit_code
            if on_reason is not None:
                self._values["on_reason"] = on_reason
            if on_status_reason is not None:
                self._values["on_status_reason"] = on_status_reason

        @builtins.property
        def action(self) -> builtins.str:
            '''Specifies the action to take if all of the specified conditions ( ``onStatusReason`` , ``onReason`` , and ``onExitCode`` ) are met.

            The values aren't case sensitive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def on_exit_code(self) -> typing.Optional[builtins.str]:
            '''Contains a glob pattern to match against the decimal representation of the ``ExitCode`` returned for a job.

            The pattern can be up to 512 characters in length. It can contain only numbers, and can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.

            The string can be between 1 and 512 characters in length.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onexitcode
            '''
            result = self._values.get("on_exit_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def on_reason(self) -> typing.Optional[builtins.str]:
            '''Contains a glob pattern to match against the ``Reason`` returned for a job.

            The pattern can be up to 512 characters in length. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces and tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.

            The string can be between 1 and 512 characters in length.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onreason
            '''
            result = self._values.get("on_reason")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def on_status_reason(self) -> typing.Optional[builtins.str]:
            '''Contains a glob pattern to match against the ``StatusReason`` returned for a job.

            The pattern can be up to 512 characters in length. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces or tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.

            The string can be between 1 and 512 characters in length.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onstatusreason
            '''
            result = self._values.get("on_status_reason")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluateOnExitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.FargatePlatformConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"platform_version": "platformVersion"},
    )
    class FargatePlatformConfigurationProperty:
        def __init__(
            self,
            *,
            platform_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The platform configuration for jobs that are running on Fargate resources.

            Jobs that run on EC2 resources must not specify this parameter.

            :param platform_version: The AWS Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the ``LATEST`` platform version is used by default. This uses a recent, approved version of the AWS Fargate platform for compute resources. For more information, see `AWS Fargate platform versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                fargate_platform_configuration_property = batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                    platform_version="platformVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.FargatePlatformConfigurationProperty.__init__)
                check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            self._values: typing.Dict[str, typing.Any] = {}
            if platform_version is not None:
                self._values["platform_version"] = platform_version

        @builtins.property
        def platform_version(self) -> typing.Optional[builtins.str]:
            '''The AWS Fargate platform version where the jobs are running.

            A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the ``LATEST`` platform version is used by default. This uses a recent, approved version of the AWS Fargate platform for compute resources. For more information, see `AWS Fargate platform versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html#cfn-batch-jobdefinition-containerproperties-fargateplatformconfiguration-platformversion
            '''
            result = self._values.get("platform_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FargatePlatformConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.LinuxParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "devices": "devices",
            "init_process_enabled": "initProcessEnabled",
            "max_swap": "maxSwap",
            "shared_memory_size": "sharedMemorySize",
            "swappiness": "swappiness",
            "tmpfs": "tmpfs",
        },
    )
    class LinuxParametersProperty:
        def __init__(
            self,
            *,
            devices: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.DeviceProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            init_process_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_swap: typing.Optional[jsii.Number] = None,
            shared_memory_size: typing.Optional[jsii.Number] = None,
            swappiness: typing.Optional[jsii.Number] = None,
            tmpfs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.TmpfsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Linux-specific modifications that are applied to the container, such as details for device mappings.

            :param devices: Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--device`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
            :param init_process_enabled: If true, run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log into your container instance and run the following command: ``sudo docker version | grep "Server API version"``
            :param max_swap: The total amount of swap memory (in MiB) a container can use. This parameter is translated to the ``--memory-swap`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ where the value is the sum of the container memory plus the ``maxSwap`` value. For more information, see ```--memory-swap`` details <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details>`_ in the Docker documentation. If a ``maxSwap`` value of ``0`` is specified, the container doesn't use swap. Accepted values are ``0`` or any positive integer. If the ``maxSwap`` parameter is omitted, the container doesn't use the swap configuration for the container instance it is running on. A ``maxSwap`` value must be set for the ``swappiness`` parameter to be used. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
            :param shared_memory_size: The value for the size (in MiB) of the ``/dev/shm`` volume. This parameter maps to the ``--shm-size`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
            :param swappiness: This allows you to tune a container's memory swappiness behavior. A ``swappiness`` value of ``0`` causes swapping not to happen unless absolutely necessary. A ``swappiness`` value of ``100`` causes pages to be swapped very aggressively. Accepted values are whole numbers between ``0`` and ``100`` . If the ``swappiness`` parameter isn't specified, a default value of ``60`` is used. If a value isn't specified for ``maxSwap`` , then this parameter is ignored. If ``maxSwap`` is set to 0, the container doesn't use swap. This parameter maps to the ``--memory-swappiness`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . Consider the following when you use a per-container swap configuration. - Swap space must be enabled and allocated on the container instance for the containers to use. .. epigraph:: The Amazon ECS optimized AMIs don't have swap enabled by default. You must enable swap on the instance to use this feature. For more information, see `Instance store swap volumes <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html>`_ in the *Amazon EC2 User Guide for Linux Instances* or `How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file? <https://docs.aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/>`_ - The swap space parameters are only supported for job definitions using EC2 resources. - If the ``maxSwap`` and ``swappiness`` parameters are omitted from a job definition, each container will have a default ``swappiness`` value of 60, and the total swap usage will be limited to two times the memory reservation of the container. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
            :param tmpfs: The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the ``--tmpfs`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                linux_parameters_property = batch.CfnJobDefinition.LinuxParametersProperty(
                    devices=[batch.CfnJobDefinition.DeviceProperty(
                        container_path="containerPath",
                        host_path="hostPath",
                        permissions=["permissions"]
                    )],
                    init_process_enabled=False,
                    max_swap=123,
                    shared_memory_size=123,
                    swappiness=123,
                    tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                        container_path="containerPath",
                        size=123,
                
                        # the properties below are optional
                        mount_options=["mountOptions"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.LinuxParametersProperty.__init__)
                check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
                check_type(argname="argument init_process_enabled", value=init_process_enabled, expected_type=type_hints["init_process_enabled"])
                check_type(argname="argument max_swap", value=max_swap, expected_type=type_hints["max_swap"])
                check_type(argname="argument shared_memory_size", value=shared_memory_size, expected_type=type_hints["shared_memory_size"])
                check_type(argname="argument swappiness", value=swappiness, expected_type=type_hints["swappiness"])
                check_type(argname="argument tmpfs", value=tmpfs, expected_type=type_hints["tmpfs"])
            self._values: typing.Dict[str, typing.Any] = {}
            if devices is not None:
                self._values["devices"] = devices
            if init_process_enabled is not None:
                self._values["init_process_enabled"] = init_process_enabled
            if max_swap is not None:
                self._values["max_swap"] = max_swap
            if shared_memory_size is not None:
                self._values["shared_memory_size"] = shared_memory_size
            if swappiness is not None:
                self._values["swappiness"] = swappiness
            if tmpfs is not None:
                self._values["tmpfs"] = tmpfs

        @builtins.property
        def devices(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.DeviceProperty", _IResolvable_da3f097b]]]]:
            '''Any host devices to expose to the container.

            This parameter maps to ``Devices`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--device`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-devices
            '''
            result = self._values.get("devices")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.DeviceProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def init_process_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, run an ``init`` process inside the container that forwards signals and reaps processes.

            This parameter maps to the ``--init`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log into your container instance and run the following command: ``sudo docker version | grep "Server API version"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-initprocessenabled
            '''
            result = self._values.get("init_process_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_swap(self) -> typing.Optional[jsii.Number]:
            '''The total amount of swap memory (in MiB) a container can use.

            This parameter is translated to the ``--memory-swap`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ where the value is the sum of the container memory plus the ``maxSwap`` value. For more information, see ```--memory-swap`` details <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details>`_ in the Docker documentation.

            If a ``maxSwap`` value of ``0`` is specified, the container doesn't use swap. Accepted values are ``0`` or any positive integer. If the ``maxSwap`` parameter is omitted, the container doesn't use the swap configuration for the container instance it is running on. A ``maxSwap`` value must be set for the ``swappiness`` parameter to be used.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-maxswap
            '''
            result = self._values.get("max_swap")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shared_memory_size(self) -> typing.Optional[jsii.Number]:
            '''The value for the size (in MiB) of the ``/dev/shm`` volume.

            This parameter maps to the ``--shm-size`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-sharedmemorysize
            '''
            result = self._values.get("shared_memory_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def swappiness(self) -> typing.Optional[jsii.Number]:
            '''This allows you to tune a container's memory swappiness behavior.

            A ``swappiness`` value of ``0`` causes swapping not to happen unless absolutely necessary. A ``swappiness`` value of ``100`` causes pages to be swapped very aggressively. Accepted values are whole numbers between ``0`` and ``100`` . If the ``swappiness`` parameter isn't specified, a default value of ``60`` is used. If a value isn't specified for ``maxSwap`` , then this parameter is ignored. If ``maxSwap`` is set to 0, the container doesn't use swap. This parameter maps to the ``--memory-swappiness`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            Consider the following when you use a per-container swap configuration.

            - Swap space must be enabled and allocated on the container instance for the containers to use.

            .. epigraph::

               The Amazon ECS optimized AMIs don't have swap enabled by default. You must enable swap on the instance to use this feature. For more information, see `Instance store swap volumes <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html>`_ in the *Amazon EC2 User Guide for Linux Instances* or `How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file? <https://docs.aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/>`_

            - The swap space parameters are only supported for job definitions using EC2 resources.
            - If the ``maxSwap`` and ``swappiness`` parameters are omitted from a job definition, each container will have a default ``swappiness`` value of 60, and the total swap usage will be limited to two times the memory reservation of the container.

            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-swappiness
            '''
            result = self._values.get("swappiness")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def tmpfs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.TmpfsProperty", _IResolvable_da3f097b]]]]:
            '''The container path, mount options, and size (in MiB) of the tmpfs mount.

            This parameter maps to the ``--tmpfs`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-tmpfs
            '''
            result = self._values.get("tmpfs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.TmpfsProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinuxParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_driver": "logDriver",
            "options": "options",
            "secret_options": "secretOptions",
        },
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            log_driver: builtins.str,
            options: typing.Any = None,
            secret_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.SecretProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Log configuration options to send to a custom log driver for the container.

            :param log_driver: The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default. The supported log drivers are ``awslogs`` , ``fluentd`` , ``gelf`` , ``json-file`` , ``journald`` , ``logentries`` , ``syslog`` , and ``splunk`` . .. epigraph:: Jobs that are running on Fargate resources are restricted to the ``awslogs`` and ``splunk`` log drivers. - **awslogs** - Specifies the Amazon CloudWatch Logs logging driver. For more information, see `Using the awslogs log driver <https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html>`_ in the *AWS Batch User Guide* and `Amazon CloudWatch Logs logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/awslogs/>`_ in the Docker documentation. - **fluentd** - Specifies the Fluentd logging driver. For more information, including usage and options, see `Fluentd logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/fluentd/>`_ in the Docker documentation. - **gelf** - Specifies the Graylog Extended Format (GELF) logging driver. For more information, including usage and options, see `Graylog Extended Format logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/gelf/>`_ in the Docker documentation. - **journald** - Specifies the journald logging driver. For more information, including usage and options, see `Journald logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/journald/>`_ in the Docker documentation. - **json-file** - Specifies the JSON file logging driver. For more information, including usage and options, see `JSON File logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/json-file/>`_ in the Docker documentation. - **splunk** - Specifies the Splunk logging driver. For more information, including usage and options, see `Splunk logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/splunk/>`_ in the Docker documentation. - **syslog** - Specifies the syslog logging driver. For more information, including usage and options, see `Syslog logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/syslog/>`_ in the Docker documentation. .. epigraph:: If you have a custom driver that's not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that's `available on GitHub <https://docs.aws.amazon.com/https://github.com/aws/amazon-ecs-agent>`_ and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesn't currently support running modified copies of this software. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log into your container instance and run the following command: ``sudo docker version | grep "Server API version"``
            :param options: The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log into your container instance and run the following command: ``sudo docker version | grep "Server API version"``
            :param secret_options: The secrets to pass to the log configuration. For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # options: Any
                
                log_configuration_property = batch.CfnJobDefinition.LogConfigurationProperty(
                    log_driver="logDriver",
                
                    # the properties below are optional
                    options=options,
                    secret_options=[batch.CfnJobDefinition.SecretProperty(
                        name="name",
                        value_from="valueFrom"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.LogConfigurationProperty.__init__)
                check_type(argname="argument log_driver", value=log_driver, expected_type=type_hints["log_driver"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
                check_type(argname="argument secret_options", value=secret_options, expected_type=type_hints["secret_options"])
            self._values: typing.Dict[str, typing.Any] = {
                "log_driver": log_driver,
            }
            if options is not None:
                self._values["options"] = options
            if secret_options is not None:
                self._values["secret_options"] = secret_options

        @builtins.property
        def log_driver(self) -> builtins.str:
            '''The log driver to use for the container.

            The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.

            The supported log drivers are ``awslogs`` , ``fluentd`` , ``gelf`` , ``json-file`` , ``journald`` , ``logentries`` , ``syslog`` , and ``splunk`` .
            .. epigraph::

               Jobs that are running on Fargate resources are restricted to the ``awslogs`` and ``splunk`` log drivers.

            - **awslogs** - Specifies the Amazon CloudWatch Logs logging driver. For more information, see `Using the awslogs log driver <https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html>`_ in the *AWS Batch User Guide* and `Amazon CloudWatch Logs logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/awslogs/>`_ in the Docker documentation.
            - **fluentd** - Specifies the Fluentd logging driver. For more information, including usage and options, see `Fluentd logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/fluentd/>`_ in the Docker documentation.
            - **gelf** - Specifies the Graylog Extended Format (GELF) logging driver. For more information, including usage and options, see `Graylog Extended Format logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/gelf/>`_ in the Docker documentation.
            - **journald** - Specifies the journald logging driver. For more information, including usage and options, see `Journald logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/journald/>`_ in the Docker documentation.
            - **json-file** - Specifies the JSON file logging driver. For more information, including usage and options, see `JSON File logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/json-file/>`_ in the Docker documentation.
            - **splunk** - Specifies the Splunk logging driver. For more information, including usage and options, see `Splunk logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/splunk/>`_ in the Docker documentation.
            - **syslog** - Specifies the syslog logging driver. For more information, including usage and options, see `Syslog logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/syslog/>`_ in the Docker documentation.

            .. epigraph::

               If you have a custom driver that's not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that's `available on GitHub <https://docs.aws.amazon.com/https://github.com/aws/amazon-ecs-agent>`_ and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesn't currently support running modified copies of this software.

            This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log into your container instance and run the following command: ``sudo docker version | grep "Server API version"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html#cfn-batch-jobdefinition-containerproperties-logconfiguration-logdriver
            '''
            result = self._values.get("log_driver")
            assert result is not None, "Required property 'log_driver' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def options(self) -> typing.Any:
            '''The configuration options to send to the log driver.

            This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log into your container instance and run the following command: ``sudo docker version | grep "Server API version"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html#cfn-batch-jobdefinition-containerproperties-logconfiguration-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Any, result)

        @builtins.property
        def secret_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.SecretProperty", _IResolvable_da3f097b]]]]:
            '''The secrets to pass to the log configuration.

            For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html#cfn-batch-jobdefinition-containerproperties-logconfiguration-secretoptions
            '''
            result = self._values.get("secret_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.SecretProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.MountPointsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_path": "containerPath",
            "read_only": "readOnly",
            "source_volume": "sourceVolume",
        },
    )
    class MountPointsProperty:
        def __init__(
            self,
            *,
            container_path: typing.Optional[builtins.str] = None,
            read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            source_volume: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details on a Docker volume mount point that's used in a job's container properties.

            This parameter maps to ``Volumes`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`_ section of the Docker Remote API and the ``--volume`` option to docker run.

            :param container_path: The path on the container where the host volume is mounted.
            :param read_only: If this value is ``true`` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is ``false`` .
            :param source_volume: The name of the volume to mount.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                mount_points_property = batch.CfnJobDefinition.MountPointsProperty(
                    container_path="containerPath",
                    read_only=False,
                    source_volume="sourceVolume"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.MountPointsProperty.__init__)
                check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
                check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
                check_type(argname="argument source_volume", value=source_volume, expected_type=type_hints["source_volume"])
            self._values: typing.Dict[str, typing.Any] = {}
            if container_path is not None:
                self._values["container_path"] = container_path
            if read_only is not None:
                self._values["read_only"] = read_only
            if source_volume is not None:
                self._values["source_volume"] = source_volume

        @builtins.property
        def container_path(self) -> typing.Optional[builtins.str]:
            '''The path on the container where the host volume is mounted.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-containerpath
            '''
            result = self._values.get("container_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def read_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If this value is ``true`` , the container has read-only access to the volume.

            Otherwise, the container can write to the volume. The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-readonly
            '''
            result = self._values.get("read_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def source_volume(self) -> typing.Optional[builtins.str]:
            '''The name of the volume to mount.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-sourcevolume
            '''
            result = self._values.get("source_volume")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MountPointsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"assign_public_ip": "assignPublicIp"},
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            assign_public_ip: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The network configuration for jobs that are running on Fargate resources.

            Jobs that are running on EC2 resources must not specify this parameter.

            :param assign_public_ip: Indicates whether the job should have a public IP address. For a job that is running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see `Amazon ECS task networking <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`_ . The default value is "DISABLED".

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                network_configuration_property = batch.CfnJobDefinition.NetworkConfigurationProperty(
                    assign_public_ip="assignPublicIp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.NetworkConfigurationProperty.__init__)
                check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            self._values: typing.Dict[str, typing.Any] = {}
            if assign_public_ip is not None:
                self._values["assign_public_ip"] = assign_public_ip

        @builtins.property
        def assign_public_ip(self) -> typing.Optional[builtins.str]:
            '''Indicates whether the job should have a public IP address.

            For a job that is running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see `Amazon ECS task networking <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`_ . The default value is "DISABLED".

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html#cfn-batch-jobdefinition-containerproperties-networkconfiguration-assignpublicip
            '''
            result = self._values.get("assign_public_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.NodePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "main_node": "mainNode",
            "node_range_properties": "nodeRangeProperties",
            "num_nodes": "numNodes",
        },
    )
    class NodePropertiesProperty:
        def __init__(
            self,
            *,
            main_node: jsii.Number,
            node_range_properties: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.NodeRangePropertyProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            num_nodes: jsii.Number,
        ) -> None:
            '''An object representing the node properties of a multi-node parallel job.

            :param main_node: Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.
            :param node_range_properties: A list of node ranges and their properties associated with a multi-node parallel job.
            :param num_nodes: The number of nodes associated with a multi-node parallel job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # options: Any
                
                node_properties_property = batch.CfnJobDefinition.NodePropertiesProperty(
                    main_node=123,
                    node_range_properties=[batch.CfnJobDefinition.NodeRangePropertyProperty(
                        target_nodes="targetNodes",
                
                        # the properties below are optional
                        container=batch.CfnJobDefinition.ContainerPropertiesProperty(
                            image="image",
                
                            # the properties below are optional
                            command=["command"],
                            environment=[batch.CfnJobDefinition.EnvironmentProperty(
                                name="name",
                                value="value"
                            )],
                            execution_role_arn="executionRoleArn",
                            fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                                platform_version="platformVersion"
                            ),
                            instance_type="instanceType",
                            job_role_arn="jobRoleArn",
                            linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                                devices=[batch.CfnJobDefinition.DeviceProperty(
                                    container_path="containerPath",
                                    host_path="hostPath",
                                    permissions=["permissions"]
                                )],
                                init_process_enabled=False,
                                max_swap=123,
                                shared_memory_size=123,
                                swappiness=123,
                                tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                                    container_path="containerPath",
                                    size=123,
                
                                    # the properties below are optional
                                    mount_options=["mountOptions"]
                                )]
                            ),
                            log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                                log_driver="logDriver",
                
                                # the properties below are optional
                                options=options,
                                secret_options=[batch.CfnJobDefinition.SecretProperty(
                                    name="name",
                                    value_from="valueFrom"
                                )]
                            ),
                            memory=123,
                            mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                                container_path="containerPath",
                                read_only=False,
                                source_volume="sourceVolume"
                            )],
                            network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                                assign_public_ip="assignPublicIp"
                            ),
                            privileged=False,
                            readonly_root_filesystem=False,
                            resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                                type="type",
                                value="value"
                            )],
                            secrets=[batch.CfnJobDefinition.SecretProperty(
                                name="name",
                                value_from="valueFrom"
                            )],
                            ulimits=[batch.CfnJobDefinition.UlimitProperty(
                                hard_limit=123,
                                name="name",
                                soft_limit=123
                            )],
                            user="user",
                            vcpus=123,
                            volumes=[batch.CfnJobDefinition.VolumesProperty(
                                efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                                    file_system_id="fileSystemId",
                
                                    # the properties below are optional
                                    authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                        access_point_id="accessPointId",
                                        iam="iam"
                                    ),
                                    root_directory="rootDirectory",
                                    transit_encryption="transitEncryption",
                                    transit_encryption_port=123
                                ),
                                host=batch.CfnJobDefinition.VolumesHostProperty(
                                    source_path="sourcePath"
                                ),
                                name="name"
                            )]
                        )
                    )],
                    num_nodes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.NodePropertiesProperty.__init__)
                check_type(argname="argument main_node", value=main_node, expected_type=type_hints["main_node"])
                check_type(argname="argument node_range_properties", value=node_range_properties, expected_type=type_hints["node_range_properties"])
                check_type(argname="argument num_nodes", value=num_nodes, expected_type=type_hints["num_nodes"])
            self._values: typing.Dict[str, typing.Any] = {
                "main_node": main_node,
                "node_range_properties": node_range_properties,
                "num_nodes": num_nodes,
            }

        @builtins.property
        def main_node(self) -> jsii.Number:
            '''Specifies the node index for the main node of a multi-node parallel job.

            This node index value must be fewer than the number of nodes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-mainnode
            '''
            result = self._values.get("main_node")
            assert result is not None, "Required property 'main_node' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def node_range_properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.NodeRangePropertyProperty", _IResolvable_da3f097b]]]:
            '''A list of node ranges and their properties associated with a multi-node parallel job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-noderangeproperties
            '''
            result = self._values.get("node_range_properties")
            assert result is not None, "Required property 'node_range_properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.NodeRangePropertyProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def num_nodes(self) -> jsii.Number:
            '''The number of nodes associated with a multi-node parallel job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-numnodes
            '''
            result = self._values.get("num_nodes")
            assert result is not None, "Required property 'num_nodes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.NodeRangePropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"target_nodes": "targetNodes", "container": "container"},
    )
    class NodeRangePropertyProperty:
        def __init__(
            self,
            *,
            target_nodes: builtins.str,
            container: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.ContainerPropertiesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''An object representing the properties of the node range for a multi-node parallel job.

            :param target_nodes: The range of nodes, using node index values. A range of ``0:3`` indicates nodes with index values of ``0`` through ``3`` . If the starting range value is omitted ( ``:n`` ), then ``0`` is used to start the range. If the ending range value is omitted ( ``n:`` ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes ( ``0:n`` ). You can nest node ranges, for example ``0:10`` and ``4:5`` , in which case the ``4:5`` range properties override the ``0:10`` properties.
            :param container: The container details for the node range.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # options: Any
                
                node_range_property_property = batch.CfnJobDefinition.NodeRangePropertyProperty(
                    target_nodes="targetNodes",
                
                    # the properties below are optional
                    container=batch.CfnJobDefinition.ContainerPropertiesProperty(
                        image="image",
                
                        # the properties below are optional
                        command=["command"],
                        environment=[batch.CfnJobDefinition.EnvironmentProperty(
                            name="name",
                            value="value"
                        )],
                        execution_role_arn="executionRoleArn",
                        fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                            platform_version="platformVersion"
                        ),
                        instance_type="instanceType",
                        job_role_arn="jobRoleArn",
                        linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                            devices=[batch.CfnJobDefinition.DeviceProperty(
                                container_path="containerPath",
                                host_path="hostPath",
                                permissions=["permissions"]
                            )],
                            init_process_enabled=False,
                            max_swap=123,
                            shared_memory_size=123,
                            swappiness=123,
                            tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                                container_path="containerPath",
                                size=123,
                
                                # the properties below are optional
                                mount_options=["mountOptions"]
                            )]
                        ),
                        log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                            log_driver="logDriver",
                
                            # the properties below are optional
                            options=options,
                            secret_options=[batch.CfnJobDefinition.SecretProperty(
                                name="name",
                                value_from="valueFrom"
                            )]
                        ),
                        memory=123,
                        mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                            container_path="containerPath",
                            read_only=False,
                            source_volume="sourceVolume"
                        )],
                        network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                            assign_public_ip="assignPublicIp"
                        ),
                        privileged=False,
                        readonly_root_filesystem=False,
                        resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                            type="type",
                            value="value"
                        )],
                        secrets=[batch.CfnJobDefinition.SecretProperty(
                            name="name",
                            value_from="valueFrom"
                        )],
                        ulimits=[batch.CfnJobDefinition.UlimitProperty(
                            hard_limit=123,
                            name="name",
                            soft_limit=123
                        )],
                        user="user",
                        vcpus=123,
                        volumes=[batch.CfnJobDefinition.VolumesProperty(
                            efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                                file_system_id="fileSystemId",
                
                                # the properties below are optional
                                authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                    access_point_id="accessPointId",
                                    iam="iam"
                                ),
                                root_directory="rootDirectory",
                                transit_encryption="transitEncryption",
                                transit_encryption_port=123
                            ),
                            host=batch.CfnJobDefinition.VolumesHostProperty(
                                source_path="sourcePath"
                            ),
                            name="name"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.NodeRangePropertyProperty.__init__)
                check_type(argname="argument target_nodes", value=target_nodes, expected_type=type_hints["target_nodes"])
                check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            self._values: typing.Dict[str, typing.Any] = {
                "target_nodes": target_nodes,
            }
            if container is not None:
                self._values["container"] = container

        @builtins.property
        def target_nodes(self) -> builtins.str:
            '''The range of nodes, using node index values.

            A range of ``0:3`` indicates nodes with index values of ``0`` through ``3`` . If the starting range value is omitted ( ``:n`` ), then ``0`` is used to start the range. If the ending range value is omitted ( ``n:`` ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes ( ``0:n`` ). You can nest node ranges, for example ``0:10`` and ``4:5`` , in which case the ``4:5`` range properties override the ``0:10`` properties.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html#cfn-batch-jobdefinition-noderangeproperty-targetnodes
            '''
            result = self._values.get("target_nodes")
            assert result is not None, "Required property 'target_nodes' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container(
            self,
        ) -> typing.Optional[typing.Union["CfnJobDefinition.ContainerPropertiesProperty", _IResolvable_da3f097b]]:
            '''The container details for the node range.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html#cfn-batch-jobdefinition-noderangeproperty-container
            '''
            result = self._values.get("container")
            return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.ContainerPropertiesProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeRangePropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.ResourceRequirementProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class ResourceRequirementProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The type and amount of a resource to assign to a container.

            The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :param type: The type of resource to assign to a container. The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .
            :param value: The quantity of the specified resource to reserve for the container. The values vary based on the ``type`` specified. - **type="GPU"** - The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job shouldn't exceed the number of available GPUs on the compute resource that the job is launched on. .. epigraph:: GPUs are not available for jobs that are running on Fargate resources. - **type="MEMORY"** - The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: If you're trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory management <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`_ in the *AWS Batch User Guide* . For jobs that are running on Fargate resources, then ``value`` is the hard limit (in MiB), and must match one of the supported values and the ``VCPU`` values must be one of the values supported for that memory value. - **value = 512** - ``VCPU`` = 0.25 - **value = 1024** - ``VCPU`` = 0.25 or 0.5 - **value = 2048** - ``VCPU`` = 0.25, 0.5, or 1 - **value = 3072** - ``VCPU`` = 0.5, or 1 - **value = 4096** - ``VCPU`` = 0.5, 1, or 2 - **value = 5120, 6144, or 7168** - ``VCPU`` = 1 or 2 - **value = 8192** - ``VCPU`` = 1, 2, or 4 - **value = 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384** - ``VCPU`` = 2 or 4 - **value = 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720** - ``VCPU`` = 4 - **type="VCPU"** - The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . Each vCPU is equivalent to 1,024 CPU shares. For EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once. For jobs that are running on Fargate resources, then ``value`` must match one of the supported values and the ``MEMORY`` values must be one of the values supported for that ``VCPU`` value. The supported values are 0.25, 0.5, 1, 2, and 4 - **value = 0.25** - ``MEMORY`` = 512, 1024, or 2048 - **value = 0.5** - ``MEMORY`` = 1024, 2048, 3072, or 4096 - **value = 1** - ``MEMORY`` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192 - **value = 2** - ``MEMORY`` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384 - **value = 4** - ``MEMORY`` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                resource_requirement_property = batch.CfnJobDefinition.ResourceRequirementProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.ResourceRequirementProperty.__init__)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of resource to assign to a container.

            The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html#cfn-batch-jobdefinition-resourcerequirement-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The quantity of the specified resource to reserve for the container. The values vary based on the ``type`` specified.

            - **type="GPU"** - The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job shouldn't exceed the number of available GPUs on the compute resource that the job is launched on.

            .. epigraph::

               GPUs are not available for jobs that are running on Fargate resources.

            - **type="MEMORY"** - The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            .. epigraph::

               If you're trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory management <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`_ in the *AWS Batch User Guide* .

            For jobs that are running on Fargate resources, then ``value`` is the hard limit (in MiB), and must match one of the supported values and the ``VCPU`` values must be one of the values supported for that memory value.

            - **value = 512** - ``VCPU`` = 0.25
            - **value = 1024** - ``VCPU`` = 0.25 or 0.5
            - **value = 2048** - ``VCPU`` = 0.25, 0.5, or 1
            - **value = 3072** - ``VCPU`` = 0.5, or 1
            - **value = 4096** - ``VCPU`` = 0.5, 1, or 2
            - **value = 5120, 6144, or 7168** - ``VCPU`` = 1 or 2
            - **value = 8192** - ``VCPU`` = 1, 2, or 4
            - **value = 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384** - ``VCPU`` = 2 or 4
            - **value = 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720** - ``VCPU`` = 4
            - **type="VCPU"** - The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . Each vCPU is equivalent to 1,024 CPU shares. For EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once.

            For jobs that are running on Fargate resources, then ``value`` must match one of the supported values and the ``MEMORY`` values must be one of the values supported for that ``VCPU`` value. The supported values are 0.25, 0.5, 1, 2, and 4

            - **value = 0.25** - ``MEMORY`` = 512, 1024, or 2048
            - **value = 0.5** - ``MEMORY`` = 1024, 2048, 3072, or 4096
            - **value = 1** - ``MEMORY`` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192
            - **value = 2** - ``MEMORY`` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384
            - **value = 4** - ``MEMORY`` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html#cfn-batch-jobdefinition-resourcerequirement-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceRequirementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.RetryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"attempts": "attempts", "evaluate_on_exit": "evaluateOnExit"},
    )
    class RetryStrategyProperty:
        def __init__(
            self,
            *,
            attempts: typing.Optional[jsii.Number] = None,
            evaluate_on_exit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobDefinition.EvaluateOnExitProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The retry strategy associated with a job.

            For more information, see `Automated job retries <https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html>`_ in the *AWS Batch User Guide* .

            :param attempts: The number of times to move a job to the ``RUNNABLE`` status. You can specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the same number of attempts as the value.
            :param evaluate_on_exit: Array of up to 5 objects that specify conditions under which the job should be retried or failed. If this parameter is specified, then the ``attempts`` parameter must also be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                retry_strategy_property = batch.CfnJobDefinition.RetryStrategyProperty(
                    attempts=123,
                    evaluate_on_exit=[batch.CfnJobDefinition.EvaluateOnExitProperty(
                        action="action",
                
                        # the properties below are optional
                        on_exit_code="onExitCode",
                        on_reason="onReason",
                        on_status_reason="onStatusReason"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.RetryStrategyProperty.__init__)
                check_type(argname="argument attempts", value=attempts, expected_type=type_hints["attempts"])
                check_type(argname="argument evaluate_on_exit", value=evaluate_on_exit, expected_type=type_hints["evaluate_on_exit"])
            self._values: typing.Dict[str, typing.Any] = {}
            if attempts is not None:
                self._values["attempts"] = attempts
            if evaluate_on_exit is not None:
                self._values["evaluate_on_exit"] = evaluate_on_exit

        @builtins.property
        def attempts(self) -> typing.Optional[jsii.Number]:
            '''The number of times to move a job to the ``RUNNABLE`` status.

            You can specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the same number of attempts as the value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html#cfn-batch-jobdefinition-retrystrategy-attempts
            '''
            result = self._values.get("attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def evaluate_on_exit(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.EvaluateOnExitProperty", _IResolvable_da3f097b]]]]:
            '''Array of up to 5 objects that specify conditions under which the job should be retried or failed.

            If this parameter is specified, then the ``attempts`` parameter must also be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html#cfn-batch-jobdefinition-retrystrategy-evaluateonexit
            '''
            result = self._values.get("evaluate_on_exit")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobDefinition.EvaluateOnExitProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.SecretProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value_from": "valueFrom"},
    )
    class SecretProperty:
        def __init__(self, *, name: builtins.str, value_from: builtins.str) -> None:
            '''An object representing the secret to expose to your container.

            Secrets can be exposed to a container in the following ways:

            - To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter.
            - To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter.

            For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .

            :param name: The name of the secret.
            :param value_from: The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store. .. epigraph:: If the AWS Systems Manager Parameter Store parameter exists in the same Region as the job you're launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                secret_property = batch.CfnJobDefinition.SecretProperty(
                    name="name",
                    value_from="valueFrom"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.SecretProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value_from", value=value_from, expected_type=type_hints["value_from"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value_from": value_from,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the secret.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html#cfn-batch-jobdefinition-secret-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_from(self) -> builtins.str:
            '''The secret to expose to the container.

            The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
            .. epigraph::

               If the AWS Systems Manager Parameter Store parameter exists in the same Region as the job you're launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html#cfn-batch-jobdefinition-secret-valuefrom
            '''
            result = self._values.get("value_from")
            assert result is not None, "Required property 'value_from' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.TimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"attempt_duration_seconds": "attemptDurationSeconds"},
    )
    class TimeoutProperty:
        def __init__(
            self,
            *,
            attempt_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An object representing a job timeout configuration.

            :param attempt_duration_seconds: The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp) after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is 60 seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                timeout_property = batch.CfnJobDefinition.TimeoutProperty(
                    attempt_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.TimeoutProperty.__init__)
                check_type(argname="argument attempt_duration_seconds", value=attempt_duration_seconds, expected_type=type_hints["attempt_duration_seconds"])
            self._values: typing.Dict[str, typing.Any] = {}
            if attempt_duration_seconds is not None:
                self._values["attempt_duration_seconds"] = attempt_duration_seconds

        @builtins.property
        def attempt_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp) after which AWS Batch terminates your jobs if they have not finished.

            The minimum value for the timeout is 60 seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html#cfn-batch-jobdefinition-timeout-attemptdurationseconds
            '''
            result = self._values.get("attempt_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.TmpfsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_path": "containerPath",
            "size": "size",
            "mount_options": "mountOptions",
        },
    )
    class TmpfsProperty:
        def __init__(
            self,
            *,
            container_path: builtins.str,
            size: jsii.Number,
            mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The container path, mount options, and size of the tmpfs mount.

            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources.

            :param container_path: The absolute file path in the container where the tmpfs volume is mounted.
            :param size: The size (in MiB) of the tmpfs volume.
            :param mount_options: The list of tmpfs volume mount options. Valid values: " ``defaults`` " | " ``ro`` " | " ``rw`` " | " ``suid`` " | " ``nosuid`` " | " ``dev`` " | " ``nodev`` " | " ``exec`` " | " ``noexec`` " | " ``sync`` " | " ``async`` " | " ``dirsync`` " | " ``remount`` " | " ``mand`` " | " ``nomand`` " | " ``atime`` " | " ``noatime`` " | " ``diratime`` " | " ``nodiratime`` " | " ``bind`` " | " ``rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime`` " | " ``norelatime`` " | " ``strictatime`` " | " ``nostrictatime`` " | " ``mode`` " | " ``uid`` " | " ``gid`` " | " ``nr_inodes`` " | " ``nr_blocks`` " | " ``mpol`` "

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                tmpfs_property = batch.CfnJobDefinition.TmpfsProperty(
                    container_path="containerPath",
                    size=123,
                
                    # the properties below are optional
                    mount_options=["mountOptions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.TmpfsProperty.__init__)
                check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
                check_type(argname="argument size", value=size, expected_type=type_hints["size"])
                check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            self._values: typing.Dict[str, typing.Any] = {
                "container_path": container_path,
                "size": size,
            }
            if mount_options is not None:
                self._values["mount_options"] = mount_options

        @builtins.property
        def container_path(self) -> builtins.str:
            '''The absolute file path in the container where the tmpfs volume is mounted.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-containerpath
            '''
            result = self._values.get("container_path")
            assert result is not None, "Required property 'container_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def size(self) -> jsii.Number:
            '''The size (in MiB) of the tmpfs volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-size
            '''
            result = self._values.get("size")
            assert result is not None, "Required property 'size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of tmpfs volume mount options.

            Valid values: " ``defaults`` " | " ``ro`` " | " ``rw`` " | " ``suid`` " | " ``nosuid`` " | " ``dev`` " | " ``nodev`` " | " ``exec`` " | " ``noexec`` " | " ``sync`` " | " ``async`` " | " ``dirsync`` " | " ``remount`` " | " ``mand`` " | " ``nomand`` " | " ``atime`` " | " ``noatime`` " | " ``diratime`` " | " ``nodiratime`` " | " ``bind`` " | " ``rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime`` " | " ``norelatime`` " | " ``strictatime`` " | " ``nostrictatime`` " | " ``mode`` " | " ``uid`` " | " ``gid`` " | " ``nr_inodes`` " | " ``nr_blocks`` " | " ``mpol`` "

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-mountoptions
            '''
            result = self._values.get("mount_options")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TmpfsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.UlimitProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hard_limit": "hardLimit",
            "name": "name",
            "soft_limit": "softLimit",
        },
    )
    class UlimitProperty:
        def __init__(
            self,
            *,
            hard_limit: jsii.Number,
            name: builtins.str,
            soft_limit: jsii.Number,
        ) -> None:
            '''The ``ulimit`` settings to pass to the container.

            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources.

            :param hard_limit: The hard limit for the ``ulimit`` type.
            :param name: The ``type`` of the ``ulimit`` .
            :param soft_limit: The soft limit for the ``ulimit`` type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                ulimit_property = batch.CfnJobDefinition.UlimitProperty(
                    hard_limit=123,
                    name="name",
                    soft_limit=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.UlimitProperty.__init__)
                check_type(argname="argument hard_limit", value=hard_limit, expected_type=type_hints["hard_limit"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument soft_limit", value=soft_limit, expected_type=type_hints["soft_limit"])
            self._values: typing.Dict[str, typing.Any] = {
                "hard_limit": hard_limit,
                "name": name,
                "soft_limit": soft_limit,
            }

        @builtins.property
        def hard_limit(self) -> jsii.Number:
            '''The hard limit for the ``ulimit`` type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-hardlimit
            '''
            result = self._values.get("hard_limit")
            assert result is not None, "Required property 'hard_limit' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The ``type`` of the ``ulimit`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def soft_limit(self) -> jsii.Number:
            '''The soft limit for the ``ulimit`` type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-softlimit
            '''
            result = self._values.get("soft_limit")
            assert result is not None, "Required property 'soft_limit' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UlimitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.VolumesHostProperty",
        jsii_struct_bases=[],
        name_mapping={"source_path": "sourcePath"},
    )
    class VolumesHostProperty:
        def __init__(
            self,
            *,
            source_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Determine whether your data volume persists on the host container instance and where it is stored.

            If this parameter is empty, then the Docker daemon assigns a host path for your data volume, but the data isn't guaranteed to persist after the containers associated with it stop running.

            :param source_path: The path on the host container instance that's presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported. .. epigraph:: This parameter isn't applicable to jobs that run on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                volumes_host_property = batch.CfnJobDefinition.VolumesHostProperty(
                    source_path="sourcePath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.VolumesHostProperty.__init__)
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
            self._values: typing.Dict[str, typing.Any] = {}
            if source_path is not None:
                self._values["source_path"] = source_path

        @builtins.property
        def source_path(self) -> typing.Optional[builtins.str]:
            '''The path on the host container instance that's presented to the container.

            If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
            .. epigraph::

               This parameter isn't applicable to jobs that run on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html#cfn-batch-jobdefinition-volumeshost-sourcepath
            '''
            result = self._values.get("source_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumesHostProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.VolumesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "efs_volume_configuration": "efsVolumeConfiguration",
            "host": "host",
            "name": "name",
        },
    )
    class VolumesProperty:
        def __init__(
            self,
            *,
            efs_volume_configuration: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.EfsVolumeConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            host: typing.Optional[typing.Union[typing.Union["CfnJobDefinition.VolumesHostProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A list of volumes associated with the job.

            :param efs_volume_configuration: This is used when you're using an Amazon Elastic File System file system for job storage. For more information, see `Amazon EFS Volumes <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html>`_ in the *AWS Batch User Guide* .
            :param host: The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers associated with it stop running. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
            :param name: The name of the volume. It can be up to 255 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                volumes_property = batch.CfnJobDefinition.VolumesProperty(
                    efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                        file_system_id="fileSystemId",
                
                        # the properties below are optional
                        authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                            access_point_id="accessPointId",
                            iam="iam"
                        ),
                        root_directory="rootDirectory",
                        transit_encryption="transitEncryption",
                        transit_encryption_port=123
                    ),
                    host=batch.CfnJobDefinition.VolumesHostProperty(
                        source_path="sourcePath"
                    ),
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobDefinition.VolumesProperty.__init__)
                check_type(argname="argument efs_volume_configuration", value=efs_volume_configuration, expected_type=type_hints["efs_volume_configuration"])
                check_type(argname="argument host", value=host, expected_type=type_hints["host"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if efs_volume_configuration is not None:
                self._values["efs_volume_configuration"] = efs_volume_configuration
            if host is not None:
                self._values["host"] = host
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def efs_volume_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnJobDefinition.EfsVolumeConfigurationProperty", _IResolvable_da3f097b]]:
            '''This is used when you're using an Amazon Elastic File System file system for job storage.

            For more information, see `Amazon EFS Volumes <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html>`_ in the *AWS Batch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-efsvolumeconfiguration
            '''
            result = self._values.get("efs_volume_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.EfsVolumeConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def host(
            self,
        ) -> typing.Optional[typing.Union["CfnJobDefinition.VolumesHostProperty", _IResolvable_da3f097b]]:
            '''The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored.

            If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers associated with it stop running.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-host
            '''
            result = self._values.get("host")
            return typing.cast(typing.Optional[typing.Union["CfnJobDefinition.VolumesHostProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the volume.

            It can be up to 255 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "container_properties": "containerProperties",
        "job_definition_name": "jobDefinitionName",
        "node_properties": "nodeProperties",
        "parameters": "parameters",
        "platform_capabilities": "platformCapabilities",
        "propagate_tags": "propagateTags",
        "retry_strategy": "retryStrategy",
        "scheduling_priority": "schedulingPriority",
        "tags": "tags",
        "timeout": "timeout",
    },
)
class CfnJobDefinitionProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        container_properties: typing.Optional[typing.Union[typing.Union[CfnJobDefinition.ContainerPropertiesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        job_definition_name: typing.Optional[builtins.str] = None,
        node_properties: typing.Optional[typing.Union[typing.Union[CfnJobDefinition.NodePropertiesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        parameters: typing.Any = None,
        platform_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        propagate_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        retry_strategy: typing.Optional[typing.Union[typing.Union[CfnJobDefinition.RetryStrategyProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        scheduling_priority: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        timeout: typing.Optional[typing.Union[typing.Union[CfnJobDefinition.TimeoutProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnJobDefinition``.

        :param type: The type of job definition. For more information about multi-node parallel jobs, see `Creating a multi-node parallel job definition <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html>`_ in the *AWS Batch User Guide* . .. epigraph:: If the job is run on Fargate resources, then ``multinode`` isn't supported.
        :param container_properties: An object with various properties specific to container-based jobs.
        :param job_definition_name: The name of the job definition.
        :param node_properties: An object with various properties specific to multi-node parallel jobs. .. epigraph:: If the job runs on Fargate resources, then you must not specify ``nodeProperties`` ; use ``containerProperties`` instead.
        :param parameters: Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see `Job definition parameters <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`_ in the *AWS Batch User Guide* .
        :param platform_capabilities: The platform capabilities required by the job definition. If no value is specified, it defaults to ``EC2`` . Jobs run on Fargate resources specify ``FARGATE`` .
        :param propagate_tags: Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the ``FAILED`` state.
        :param retry_strategy: The retry strategy to use for failed jobs that are submitted with this job definition.
        :param scheduling_priority: The scheduling priority of the job definition. This only affects jobs in job queues with a fair share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.
        :param tags: The tags applied to the job definition.
        :param timeout: The timeout configuration for jobs that are submitted with this job definition. You can specify a timeout duration after which AWS Batch terminates your jobs if they haven't finished.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_batch as batch
            
            # options: Any
            # parameters: Any
            # tags: Any
            
            cfn_job_definition_props = batch.CfnJobDefinitionProps(
                type="type",
            
                # the properties below are optional
                container_properties=batch.CfnJobDefinition.ContainerPropertiesProperty(
                    image="image",
            
                    # the properties below are optional
                    command=["command"],
                    environment=[batch.CfnJobDefinition.EnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    execution_role_arn="executionRoleArn",
                    fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                        platform_version="platformVersion"
                    ),
                    instance_type="instanceType",
                    job_role_arn="jobRoleArn",
                    linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                        devices=[batch.CfnJobDefinition.DeviceProperty(
                            container_path="containerPath",
                            host_path="hostPath",
                            permissions=["permissions"]
                        )],
                        init_process_enabled=False,
                        max_swap=123,
                        shared_memory_size=123,
                        swappiness=123,
                        tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                            container_path="containerPath",
                            size=123,
            
                            # the properties below are optional
                            mount_options=["mountOptions"]
                        )]
                    ),
                    log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                        log_driver="logDriver",
            
                        # the properties below are optional
                        options=options,
                        secret_options=[batch.CfnJobDefinition.SecretProperty(
                            name="name",
                            value_from="valueFrom"
                        )]
                    ),
                    memory=123,
                    mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                        container_path="containerPath",
                        read_only=False,
                        source_volume="sourceVolume"
                    )],
                    network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                        assign_public_ip="assignPublicIp"
                    ),
                    privileged=False,
                    readonly_root_filesystem=False,
                    resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                        type="type",
                        value="value"
                    )],
                    secrets=[batch.CfnJobDefinition.SecretProperty(
                        name="name",
                        value_from="valueFrom"
                    )],
                    ulimits=[batch.CfnJobDefinition.UlimitProperty(
                        hard_limit=123,
                        name="name",
                        soft_limit=123
                    )],
                    user="user",
                    vcpus=123,
                    volumes=[batch.CfnJobDefinition.VolumesProperty(
                        efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                            file_system_id="fileSystemId",
            
                            # the properties below are optional
                            authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                access_point_id="accessPointId",
                                iam="iam"
                            ),
                            root_directory="rootDirectory",
                            transit_encryption="transitEncryption",
                            transit_encryption_port=123
                        ),
                        host=batch.CfnJobDefinition.VolumesHostProperty(
                            source_path="sourcePath"
                        ),
                        name="name"
                    )]
                ),
                job_definition_name="jobDefinitionName",
                node_properties=batch.CfnJobDefinition.NodePropertiesProperty(
                    main_node=123,
                    node_range_properties=[batch.CfnJobDefinition.NodeRangePropertyProperty(
                        target_nodes="targetNodes",
            
                        # the properties below are optional
                        container=batch.CfnJobDefinition.ContainerPropertiesProperty(
                            image="image",
            
                            # the properties below are optional
                            command=["command"],
                            environment=[batch.CfnJobDefinition.EnvironmentProperty(
                                name="name",
                                value="value"
                            )],
                            execution_role_arn="executionRoleArn",
                            fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                                platform_version="platformVersion"
                            ),
                            instance_type="instanceType",
                            job_role_arn="jobRoleArn",
                            linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                                devices=[batch.CfnJobDefinition.DeviceProperty(
                                    container_path="containerPath",
                                    host_path="hostPath",
                                    permissions=["permissions"]
                                )],
                                init_process_enabled=False,
                                max_swap=123,
                                shared_memory_size=123,
                                swappiness=123,
                                tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                                    container_path="containerPath",
                                    size=123,
            
                                    # the properties below are optional
                                    mount_options=["mountOptions"]
                                )]
                            ),
                            log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                                log_driver="logDriver",
            
                                # the properties below are optional
                                options=options,
                                secret_options=[batch.CfnJobDefinition.SecretProperty(
                                    name="name",
                                    value_from="valueFrom"
                                )]
                            ),
                            memory=123,
                            mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                                container_path="containerPath",
                                read_only=False,
                                source_volume="sourceVolume"
                            )],
                            network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                                assign_public_ip="assignPublicIp"
                            ),
                            privileged=False,
                            readonly_root_filesystem=False,
                            resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                                type="type",
                                value="value"
                            )],
                            secrets=[batch.CfnJobDefinition.SecretProperty(
                                name="name",
                                value_from="valueFrom"
                            )],
                            ulimits=[batch.CfnJobDefinition.UlimitProperty(
                                hard_limit=123,
                                name="name",
                                soft_limit=123
                            )],
                            user="user",
                            vcpus=123,
                            volumes=[batch.CfnJobDefinition.VolumesProperty(
                                efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                                    file_system_id="fileSystemId",
            
                                    # the properties below are optional
                                    authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                        access_point_id="accessPointId",
                                        iam="iam"
                                    ),
                                    root_directory="rootDirectory",
                                    transit_encryption="transitEncryption",
                                    transit_encryption_port=123
                                ),
                                host=batch.CfnJobDefinition.VolumesHostProperty(
                                    source_path="sourcePath"
                                ),
                                name="name"
                            )]
                        )
                    )],
                    num_nodes=123
                ),
                parameters=parameters,
                platform_capabilities=["platformCapabilities"],
                propagate_tags=False,
                retry_strategy=batch.CfnJobDefinition.RetryStrategyProperty(
                    attempts=123,
                    evaluate_on_exit=[batch.CfnJobDefinition.EvaluateOnExitProperty(
                        action="action",
            
                        # the properties below are optional
                        on_exit_code="onExitCode",
                        on_reason="onReason",
                        on_status_reason="onStatusReason"
                    )]
                ),
                scheduling_priority=123,
                tags=tags,
                timeout=batch.CfnJobDefinition.TimeoutProperty(
                    attempt_duration_seconds=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobDefinitionProps.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument container_properties", value=container_properties, expected_type=type_hints["container_properties"])
            check_type(argname="argument job_definition_name", value=job_definition_name, expected_type=type_hints["job_definition_name"])
            check_type(argname="argument node_properties", value=node_properties, expected_type=type_hints["node_properties"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument platform_capabilities", value=platform_capabilities, expected_type=type_hints["platform_capabilities"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument retry_strategy", value=retry_strategy, expected_type=type_hints["retry_strategy"])
            check_type(argname="argument scheduling_priority", value=scheduling_priority, expected_type=type_hints["scheduling_priority"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if container_properties is not None:
            self._values["container_properties"] = container_properties
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if node_properties is not None:
            self._values["node_properties"] = node_properties
        if parameters is not None:
            self._values["parameters"] = parameters
        if platform_capabilities is not None:
            self._values["platform_capabilities"] = platform_capabilities
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if retry_strategy is not None:
            self._values["retry_strategy"] = retry_strategy
        if scheduling_priority is not None:
            self._values["scheduling_priority"] = scheduling_priority
        if tags is not None:
            self._values["tags"] = tags
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of job definition.

        For more information about multi-node parallel jobs, see `Creating a multi-node parallel job definition <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html>`_ in the *AWS Batch User Guide* .
        .. epigraph::

           If the job is run on Fargate resources, then ``multinode`` isn't supported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_properties(
        self,
    ) -> typing.Optional[typing.Union[CfnJobDefinition.ContainerPropertiesProperty, _IResolvable_da3f097b]]:
        '''An object with various properties specific to container-based jobs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-containerproperties
        '''
        result = self._values.get("container_properties")
        return typing.cast(typing.Optional[typing.Union[CfnJobDefinition.ContainerPropertiesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job definition.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_properties(
        self,
    ) -> typing.Optional[typing.Union[CfnJobDefinition.NodePropertiesProperty, _IResolvable_da3f097b]]:
        '''An object with various properties specific to multi-node parallel jobs.

        .. epigraph::

           If the job runs on Fargate resources, then you must not specify ``nodeProperties`` ; use ``containerProperties`` instead.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-nodeproperties
        '''
        result = self._values.get("node_properties")
        return typing.cast(typing.Optional[typing.Union[CfnJobDefinition.NodePropertiesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''Default parameters or parameter substitution placeholders that are set in the job definition.

        Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see `Job definition parameters <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`_ in the *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def platform_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The platform capabilities required by the job definition.

        If no value is specified, it defaults to ``EC2`` . Jobs run on Fargate resources specify ``FARGATE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-platformcapabilities
        '''
        result = self._values.get("platform_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def propagate_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task.

        If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the ``FAILED`` state.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-propagatetags
        '''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def retry_strategy(
        self,
    ) -> typing.Optional[typing.Union[CfnJobDefinition.RetryStrategyProperty, _IResolvable_da3f097b]]:
        '''The retry strategy to use for failed jobs that are submitted with this job definition.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-retrystrategy
        '''
        result = self._values.get("retry_strategy")
        return typing.cast(typing.Optional[typing.Union[CfnJobDefinition.RetryStrategyProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def scheduling_priority(self) -> typing.Optional[jsii.Number]:
        '''The scheduling priority of the job definition.

        This only affects jobs in job queues with a fair share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-schedulingpriority
        '''
        result = self._values.get("scheduling_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The tags applied to the job definition.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def timeout(
        self,
    ) -> typing.Optional[typing.Union[CfnJobDefinition.TimeoutProperty, _IResolvable_da3f097b]]:
        '''The timeout configuration for jobs that are submitted with this job definition.

        You can specify a timeout duration after which AWS Batch terminates your jobs if they haven't finished.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[typing.Union[CfnJobDefinition.TimeoutProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnJobQueue(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_batch.CfnJobQueue",
):
    '''A CloudFormation ``AWS::Batch::JobQueue``.

    The ``AWS::Batch::JobQueue`` resource specifies the parameters for an AWS Batch job queue definition. For more information, see `Job Queues <https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html>`_ in the ** .

    :cloudformationResource: AWS::Batch::JobQueue
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_batch as batch
        
        cfn_job_queue = batch.CfnJobQueue(self, "MyCfnJobQueue",
            compute_environment_order=[batch.CfnJobQueue.ComputeEnvironmentOrderProperty(
                compute_environment="computeEnvironment",
                order=123
            )],
            priority=123,
        
            # the properties below are optional
            job_queue_name="jobQueueName",
            scheduling_policy_arn="schedulingPolicyArn",
            state="state",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        compute_environment_order: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnJobQueue.ComputeEnvironmentOrderProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        priority: jsii.Number,
        job_queue_name: typing.Optional[builtins.str] = None,
        scheduling_policy_arn: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Batch::JobQueue``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param compute_environment_order: The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed. .. epigraph:: All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.
        :param priority: The priority of the job queue. Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` . All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
        :param job_queue_name: The name of the job queue. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param scheduling_policy_arn: The Amazon Resource Name (ARN) of the scheduling policy. The format is ``aws: *Partition* :batch: *Region* : *Account* :scheduling-policy/ *Name*`` . For example, ``aws:aws:batch:us-west-2:012345678910:scheduling-policy/MySchedulingPolicy`` .
        :param state: The state of the job queue. If the job queue state is ``ENABLED`` , it is able to accept jobs. If the job queue state is ``DISABLED`` , new jobs can't be added to the queue, but jobs already in the queue can finish.
        :param tags: The tags applied to the job queue. For more information, see `Tagging your AWS Batch resources <https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html>`_ in *AWS Batch User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobQueue.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobQueueProps(
            compute_environment_order=compute_environment_order,
            priority=priority,
            job_queue_name=job_queue_name,
            scheduling_policy_arn=scheduling_policy_arn,
            state=state,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobQueue.inspect)
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
            type_hints = typing.get_type_hints(CfnJobQueue._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobQueueArn")
    def attr_job_queue_arn(self) -> builtins.str:
        '''Returns the job queue ARN, such as ``batch: *us-east-1* : *111122223333* :job-queue/ *JobQueueName*`` .

        :cloudformationAttribute: JobQueueArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobQueueArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags applied to the job queue.

        For more information, see `Tagging your AWS Batch resources <https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html>`_ in *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="computeEnvironmentOrder")
    def compute_environment_order(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobQueue.ComputeEnvironmentOrderProperty", _IResolvable_da3f097b]]]:
        '''The set of compute environments mapped to a job queue and their order relative to each other.

        The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
        .. epigraph::

           All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-computeenvironmentorder
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobQueue.ComputeEnvironmentOrderProperty", _IResolvable_da3f097b]]], jsii.get(self, "computeEnvironmentOrder"))

    @compute_environment_order.setter
    def compute_environment_order(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJobQueue.ComputeEnvironmentOrderProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobQueue, "compute_environment_order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeEnvironmentOrder", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''The priority of the job queue.

        Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` . All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-priority
        '''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobQueue, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobQueueName")
    def job_queue_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job queue.

        It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-jobqueuename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobQueueName"))

    @job_queue_name.setter
    def job_queue_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobQueue, "job_queue_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobQueueName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedulingPolicyArn")
    def scheduling_policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the scheduling policy.

        The format is ``aws: *Partition* :batch: *Region* : *Account* :scheduling-policy/ *Name*`` . For example, ``aws:aws:batch:us-west-2:012345678910:scheduling-policy/MySchedulingPolicy`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-schedulingpolicyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulingPolicyArn"))

    @scheduling_policy_arn.setter
    def scheduling_policy_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobQueue, "scheduling_policy_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingPolicyArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the job queue.

        If the job queue state is ``ENABLED`` , it is able to accept jobs. If the job queue state is ``DISABLED`` , new jobs can't be added to the queue, but jobs already in the queue can finish.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobQueue, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobQueue.ComputeEnvironmentOrderProperty",
        jsii_struct_bases=[],
        name_mapping={"compute_environment": "computeEnvironment", "order": "order"},
    )
    class ComputeEnvironmentOrderProperty:
        def __init__(
            self,
            *,
            compute_environment: builtins.str,
            order: jsii.Number,
        ) -> None:
            '''The order in which compute environments are tried for job placement within a queue.

            Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
            .. epigraph::

               All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.

            :param compute_environment: The Amazon Resource Name (ARN) of the compute environment.
            :param order: The order of the compute environment. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower ``order`` integer value is tried for job placement first.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                compute_environment_order_property = batch.CfnJobQueue.ComputeEnvironmentOrderProperty(
                    compute_environment="computeEnvironment",
                    order=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnJobQueue.ComputeEnvironmentOrderProperty.__init__)
                check_type(argname="argument compute_environment", value=compute_environment, expected_type=type_hints["compute_environment"])
                check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            self._values: typing.Dict[str, typing.Any] = {
                "compute_environment": compute_environment,
                "order": order,
            }

        @builtins.property
        def compute_environment(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the compute environment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html#cfn-batch-jobqueue-computeenvironmentorder-computeenvironment
            '''
            result = self._values.get("compute_environment")
            assert result is not None, "Required property 'compute_environment' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def order(self) -> jsii.Number:
            '''The order of the compute environment.

            Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower ``order`` integer value is tried for job placement first.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html#cfn-batch-jobqueue-computeenvironmentorder-order
            '''
            result = self._values.get("order")
            assert result is not None, "Required property 'order' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeEnvironmentOrderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_batch.CfnJobQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "compute_environment_order": "computeEnvironmentOrder",
        "priority": "priority",
        "job_queue_name": "jobQueueName",
        "scheduling_policy_arn": "schedulingPolicyArn",
        "state": "state",
        "tags": "tags",
    },
)
class CfnJobQueueProps:
    def __init__(
        self,
        *,
        compute_environment_order: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnJobQueue.ComputeEnvironmentOrderProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        priority: jsii.Number,
        job_queue_name: typing.Optional[builtins.str] = None,
        scheduling_policy_arn: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnJobQueue``.

        :param compute_environment_order: The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed. .. epigraph:: All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.
        :param priority: The priority of the job queue. Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` . All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
        :param job_queue_name: The name of the job queue. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param scheduling_policy_arn: The Amazon Resource Name (ARN) of the scheduling policy. The format is ``aws: *Partition* :batch: *Region* : *Account* :scheduling-policy/ *Name*`` . For example, ``aws:aws:batch:us-west-2:012345678910:scheduling-policy/MySchedulingPolicy`` .
        :param state: The state of the job queue. If the job queue state is ``ENABLED`` , it is able to accept jobs. If the job queue state is ``DISABLED`` , new jobs can't be added to the queue, but jobs already in the queue can finish.
        :param tags: The tags applied to the job queue. For more information, see `Tagging your AWS Batch resources <https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html>`_ in *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_batch as batch
            
            cfn_job_queue_props = batch.CfnJobQueueProps(
                compute_environment_order=[batch.CfnJobQueue.ComputeEnvironmentOrderProperty(
                    compute_environment="computeEnvironment",
                    order=123
                )],
                priority=123,
            
                # the properties below are optional
                job_queue_name="jobQueueName",
                scheduling_policy_arn="schedulingPolicyArn",
                state="state",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobQueueProps.__init__)
            check_type(argname="argument compute_environment_order", value=compute_environment_order, expected_type=type_hints["compute_environment_order"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument job_queue_name", value=job_queue_name, expected_type=type_hints["job_queue_name"])
            check_type(argname="argument scheduling_policy_arn", value=scheduling_policy_arn, expected_type=type_hints["scheduling_policy_arn"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "compute_environment_order": compute_environment_order,
            "priority": priority,
        }
        if job_queue_name is not None:
            self._values["job_queue_name"] = job_queue_name
        if scheduling_policy_arn is not None:
            self._values["scheduling_policy_arn"] = scheduling_policy_arn
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def compute_environment_order(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJobQueue.ComputeEnvironmentOrderProperty, _IResolvable_da3f097b]]]:
        '''The set of compute environments mapped to a job queue and their order relative to each other.

        The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
        .. epigraph::

           All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-computeenvironmentorder
        '''
        result = self._values.get("compute_environment_order")
        assert result is not None, "Required property 'compute_environment_order' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJobQueue.ComputeEnvironmentOrderProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The priority of the job queue.

        Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` . All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def job_queue_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job queue.

        It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-jobqueuename
        '''
        result = self._values.get("job_queue_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduling_policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the scheduling policy.

        The format is ``aws: *Partition* :batch: *Region* : *Account* :scheduling-policy/ *Name*`` . For example, ``aws:aws:batch:us-west-2:012345678910:scheduling-policy/MySchedulingPolicy`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-schedulingpolicyarn
        '''
        result = self._values.get("scheduling_policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the job queue.

        If the job queue state is ``ENABLED`` , it is able to accept jobs. If the job queue state is ``DISABLED`` , new jobs can't be added to the queue, but jobs already in the queue can finish.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags applied to the job queue.

        For more information, see `Tagging your AWS Batch resources <https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html>`_ in *AWS Batch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSchedulingPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_batch.CfnSchedulingPolicy",
):
    '''A CloudFormation ``AWS::Batch::SchedulingPolicy``.

    The ``AWS::Batch::SchedulingPolicy`` resource specifies the parameters for an AWS Batch scheduling policy. For more information, see `Scheduling Policies <https://docs.aws.amazon.com/batch/latest/userguide/scheduling_policies.html>`_ in the ** .

    :cloudformationResource: AWS::Batch::SchedulingPolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_batch as batch
        
        cfn_scheduling_policy = batch.CfnSchedulingPolicy(self, "MyCfnSchedulingPolicy",
            fairshare_policy=batch.CfnSchedulingPolicy.FairsharePolicyProperty(
                compute_reservation=123,
                share_decay_seconds=123,
                share_distribution=[batch.CfnSchedulingPolicy.ShareAttributesProperty(
                    share_identifier="shareIdentifier",
                    weight_factor=123
                )]
            ),
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        fairshare_policy: typing.Optional[typing.Union[typing.Union["CfnSchedulingPolicy.FairsharePolicyProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Batch::SchedulingPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param fairshare_policy: The fair share policy of the scheduling policy.
        :param name: The name of the scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param tags: The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in *AWS General Reference* . These tags can be updated or removed using the `TagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html>`_ and `UntagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html>`_ API operations.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSchedulingPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchedulingPolicyProps(
            fairshare_policy=fairshare_policy, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSchedulingPolicy.inspect)
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
            type_hints = typing.get_type_hints(CfnSchedulingPolicy._render_properties)
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
        '''Returns the scheduling policy ARN, such as ``batch: *us-east-1* : *111122223333* :scheduling-policy/ *HighPriority*`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags that you apply to the scheduling policy to help you categorize and organize your resources.

        Each tag consists of a key and an optional value. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in *AWS General Reference* .

        These tags can be updated or removed using the `TagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html>`_ and `UntagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html>`_ API operations.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fairsharePolicy")
    def fairshare_policy(
        self,
    ) -> typing.Optional[typing.Union["CfnSchedulingPolicy.FairsharePolicyProperty", _IResolvable_da3f097b]]:
        '''The fair share policy of the scheduling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy
        '''
        return typing.cast(typing.Optional[typing.Union["CfnSchedulingPolicy.FairsharePolicyProperty", _IResolvable_da3f097b]], jsii.get(self, "fairsharePolicy"))

    @fairshare_policy.setter
    def fairshare_policy(
        self,
        value: typing.Optional[typing.Union["CfnSchedulingPolicy.FairsharePolicyProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSchedulingPolicy, "fairshare_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fairsharePolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the scheduling policy.

        It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSchedulingPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnSchedulingPolicy.FairsharePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compute_reservation": "computeReservation",
            "share_decay_seconds": "shareDecaySeconds",
            "share_distribution": "shareDistribution",
        },
    )
    class FairsharePolicyProperty:
        def __init__(
            self,
            *,
            compute_reservation: typing.Optional[jsii.Number] = None,
            share_decay_seconds: typing.Optional[jsii.Number] = None,
            share_distribution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnSchedulingPolicy.ShareAttributesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The fair share policy for a scheduling policy.

            :param compute_reservation: A value used to reserve some of the available maximum vCPU for fair share identifiers that have not yet been used. The reserved ratio is ``( *computeReservation* /100)^ *ActiveFairShares*`` where ``*ActiveFairShares*`` is the number of active fair share identifiers. For example, a ``computeReservation`` value of 50 indicates that AWS Batch should reserve 50% of the maximum available vCPU if there is only one fair share identifier, 25% if there are two fair share identifiers, and 12.5% if there are three fair share identifiers. A ``computeReservation`` value of 25 indicates that AWS Batch should reserve 25% of the maximum available vCPU if there is only one fair share identifier, 6.25% if there are two fair share identifiers, and 1.56% if there are three fair share identifiers. The minimum value is 0 and the maximum value is 99.
            :param share_decay_seconds: The time period to use to calculate a fair share percentage for each fair share identifier in use, in seconds. A value of zero (0) indicates that only current usage should be measured. The decay allows for more recently run jobs to have more weight than jobs that ran earlier. The maximum supported value is 604800 (1 week).
            :param share_distribution: An array of ``SharedIdentifier`` objects that contain the weights for the fair share identifiers for the fair share policy. Fair share identifiers that aren't included have a default weight of ``1.0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                fairshare_policy_property = batch.CfnSchedulingPolicy.FairsharePolicyProperty(
                    compute_reservation=123,
                    share_decay_seconds=123,
                    share_distribution=[batch.CfnSchedulingPolicy.ShareAttributesProperty(
                        share_identifier="shareIdentifier",
                        weight_factor=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSchedulingPolicy.FairsharePolicyProperty.__init__)
                check_type(argname="argument compute_reservation", value=compute_reservation, expected_type=type_hints["compute_reservation"])
                check_type(argname="argument share_decay_seconds", value=share_decay_seconds, expected_type=type_hints["share_decay_seconds"])
                check_type(argname="argument share_distribution", value=share_distribution, expected_type=type_hints["share_distribution"])
            self._values: typing.Dict[str, typing.Any] = {}
            if compute_reservation is not None:
                self._values["compute_reservation"] = compute_reservation
            if share_decay_seconds is not None:
                self._values["share_decay_seconds"] = share_decay_seconds
            if share_distribution is not None:
                self._values["share_distribution"] = share_distribution

        @builtins.property
        def compute_reservation(self) -> typing.Optional[jsii.Number]:
            '''A value used to reserve some of the available maximum vCPU for fair share identifiers that have not yet been used.

            The reserved ratio is ``( *computeReservation* /100)^ *ActiveFairShares*`` where ``*ActiveFairShares*`` is the number of active fair share identifiers.

            For example, a ``computeReservation`` value of 50 indicates that AWS Batch should reserve 50% of the maximum available vCPU if there is only one fair share identifier, 25% if there are two fair share identifiers, and 12.5% if there are three fair share identifiers. A ``computeReservation`` value of 25 indicates that AWS Batch should reserve 25% of the maximum available vCPU if there is only one fair share identifier, 6.25% if there are two fair share identifiers, and 1.56% if there are three fair share identifiers.

            The minimum value is 0 and the maximum value is 99.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-computereservation
            '''
            result = self._values.get("compute_reservation")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def share_decay_seconds(self) -> typing.Optional[jsii.Number]:
            '''The time period to use to calculate a fair share percentage for each fair share identifier in use, in seconds.

            A value of zero (0) indicates that only current usage should be measured. The decay allows for more recently run jobs to have more weight than jobs that ran earlier. The maximum supported value is 604800 (1 week).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-sharedecayseconds
            '''
            result = self._values.get("share_decay_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def share_distribution(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedulingPolicy.ShareAttributesProperty", _IResolvable_da3f097b]]]]:
            '''An array of ``SharedIdentifier`` objects that contain the weights for the fair share identifiers for the fair share policy.

            Fair share identifiers that aren't included have a default weight of ``1.0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-sharedistribution
            '''
            result = self._values.get("share_distribution")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSchedulingPolicy.ShareAttributesProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FairsharePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnSchedulingPolicy.ShareAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "share_identifier": "shareIdentifier",
            "weight_factor": "weightFactor",
        },
    )
    class ShareAttributesProperty:
        def __init__(
            self,
            *,
            share_identifier: typing.Optional[builtins.str] = None,
            weight_factor: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the weights for the fair share identifiers for the fair share policy.

            Fair share identifiers that aren't included have a default weight of ``1.0`` .

            :param share_identifier: A fair share identifier or fair share identifier prefix. If the string ends with an asterisk (*), this entry specifies the weight factor to use for fair share identifiers that start with that prefix. The list of fair share identifiers in a fair share policy cannot overlap. For example, you can't have one that specifies a ``shareIdentifier`` of ``UserA*`` and another that specifies a ``shareIdentifier`` of ``UserA-1`` . There can be no more than 500 fair share identifiers active in a job queue. The string is limited to 255 alphanumeric characters, optionally followed by an asterisk (*).
            :param weight_factor: The weight factor for the fair share identifier. The default value is 1.0. A lower value has a higher priority for compute resources. For example, jobs that use a share identifier with a weight factor of 0.125 (1/8) get 8 times the compute resources of jobs that use a share identifier with a weight factor of 1. The smallest supported value is 0.0001, and the largest supported value is 999.9999.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                share_attributes_property = batch.CfnSchedulingPolicy.ShareAttributesProperty(
                    share_identifier="shareIdentifier",
                    weight_factor=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSchedulingPolicy.ShareAttributesProperty.__init__)
                check_type(argname="argument share_identifier", value=share_identifier, expected_type=type_hints["share_identifier"])
                check_type(argname="argument weight_factor", value=weight_factor, expected_type=type_hints["weight_factor"])
            self._values: typing.Dict[str, typing.Any] = {}
            if share_identifier is not None:
                self._values["share_identifier"] = share_identifier
            if weight_factor is not None:
                self._values["weight_factor"] = weight_factor

        @builtins.property
        def share_identifier(self) -> typing.Optional[builtins.str]:
            '''A fair share identifier or fair share identifier prefix.

            If the string ends with an asterisk (*), this entry specifies the weight factor to use for fair share identifiers that start with that prefix. The list of fair share identifiers in a fair share policy cannot overlap. For example, you can't have one that specifies a ``shareIdentifier`` of ``UserA*`` and another that specifies a ``shareIdentifier`` of ``UserA-1`` .

            There can be no more than 500 fair share identifiers active in a job queue.

            The string is limited to 255 alphanumeric characters, optionally followed by an asterisk (*).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html#cfn-batch-schedulingpolicy-shareattributes-shareidentifier
            '''
            result = self._values.get("share_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def weight_factor(self) -> typing.Optional[jsii.Number]:
            '''The weight factor for the fair share identifier.

            The default value is 1.0. A lower value has a higher priority for compute resources. For example, jobs that use a share identifier with a weight factor of 0.125 (1/8) get 8 times the compute resources of jobs that use a share identifier with a weight factor of 1.

            The smallest supported value is 0.0001, and the largest supported value is 999.9999.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html#cfn-batch-schedulingpolicy-shareattributes-weightfactor
            '''
            result = self._values.get("weight_factor")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ShareAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_batch.CfnSchedulingPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "fairshare_policy": "fairsharePolicy",
        "name": "name",
        "tags": "tags",
    },
)
class CfnSchedulingPolicyProps:
    def __init__(
        self,
        *,
        fairshare_policy: typing.Optional[typing.Union[typing.Union[CfnSchedulingPolicy.FairsharePolicyProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchedulingPolicy``.

        :param fairshare_policy: The fair share policy of the scheduling policy.
        :param name: The name of the scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param tags: The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in *AWS General Reference* . These tags can be updated or removed using the `TagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html>`_ and `UntagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html>`_ API operations.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_batch as batch
            
            cfn_scheduling_policy_props = batch.CfnSchedulingPolicyProps(
                fairshare_policy=batch.CfnSchedulingPolicy.FairsharePolicyProperty(
                    compute_reservation=123,
                    share_decay_seconds=123,
                    share_distribution=[batch.CfnSchedulingPolicy.ShareAttributesProperty(
                        share_identifier="shareIdentifier",
                        weight_factor=123
                    )]
                ),
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSchedulingPolicyProps.__init__)
            check_type(argname="argument fairshare_policy", value=fairshare_policy, expected_type=type_hints["fairshare_policy"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fairshare_policy is not None:
            self._values["fairshare_policy"] = fairshare_policy
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def fairshare_policy(
        self,
    ) -> typing.Optional[typing.Union[CfnSchedulingPolicy.FairsharePolicyProperty, _IResolvable_da3f097b]]:
        '''The fair share policy of the scheduling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy
        '''
        result = self._values.get("fairshare_policy")
        return typing.cast(typing.Optional[typing.Union[CfnSchedulingPolicy.FairsharePolicyProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the scheduling policy.

        It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags that you apply to the scheduling policy to help you categorize and organize your resources.

        Each tag consists of a key and an optional value. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in *AWS General Reference* .

        These tags can be updated or removed using the `TagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html>`_ and `UntagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html>`_ API operations.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchedulingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComputeEnvironment",
    "CfnComputeEnvironmentProps",
    "CfnJobDefinition",
    "CfnJobDefinitionProps",
    "CfnJobQueue",
    "CfnJobQueueProps",
    "CfnSchedulingPolicy",
    "CfnSchedulingPolicyProps",
]

publication.publish()
