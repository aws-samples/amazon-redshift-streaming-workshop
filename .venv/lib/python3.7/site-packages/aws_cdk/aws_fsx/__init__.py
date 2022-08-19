'''
# Amazon FSx Construct Library

[Amazon FSx](https://docs.aws.amazon.com/fsx/?id=docs_gateway) provides fully managed third-party file systems with the
native compatibility and feature sets for workloads such as Microsoft Windows–based storage, high-performance computing,
machine learning, and electronic design automation.

Amazon FSx supports two file system types: [Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/index.html) and
[Windows](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/index.html) File Server.

## FSx for Lustre

Amazon FSx for Lustre makes it easy and cost-effective to launch and run the popular, high-performance Lustre file
system. You use Lustre for workloads where speed matters, such as machine learning, high performance computing (HPC),
video processing, and financial modeling.

The open-source Lustre file system is designed for applications that require fast storage—where you want your storage
to keep up with your compute. Lustre was built to solve the problem of quickly and cheaply processing the world's
ever-growing datasets. It's a widely used file system designed for the fastest computers in the world. It provides
submillisecond latencies, up to hundreds of GBps of throughput, and up to millions of IOPS. For more information on
Lustre, see the [Lustre website](http://lustre.org/).

As a fully managed service, Amazon FSx makes it easier for you to use Lustre for workloads where storage speed matters.
Amazon FSx for Lustre eliminates the traditional complexity of setting up and managing Lustre file systems, enabling
you to spin up and run a battle-tested high-performance file system in minutes. It also provides multiple deployment
options so you can optimize cost for your needs.

Amazon FSx for Lustre is POSIX-compliant, so you can use your current Linux-based applications without having to make
any changes. Amazon FSx for Lustre provides a native file system interface and works as any file system does with your
Linux operating system. It also provides read-after-write consistency and supports file locking.

### Installation

Import to your project:

```python
import aws_cdk.aws_fsx as fsx
```

### Basic Usage

Setup required properties and create:

```python
# vpc: ec2.Vpc


file_system = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
    lustre_configuration=fsx.LustreConfiguration(deployment_type=fsx.LustreDeploymentType.SCRATCH_2),
    storage_capacity_gi_b=1200,
    vpc=vpc,
    vpc_subnet=vpc.private_subnets[0]
)
```

### Connecting

To control who can access the file system, use the `.connections` attribute. FSx has a fixed default port, so you don't
need to specify the port. This example allows an EC2 instance to connect to a file system:

```python
# file_system: fsx.LustreFileSystem
# instance: ec2.Instance


file_system.connections.allow_default_port_from(instance)
```

### Mounting

The LustreFileSystem Construct exposes both the DNS name of the file system as well as its mount name, which can be
used to mount the file system on an EC2 instance. The following example shows how to bring up a file system and EC2
instance, and then use User Data to mount the file system on the instance at start-up:

```python
import aws_cdk.aws_iam as iam

# vpc: ec2.Vpc

lustre_configuration = {
    "deployment_type": fsx.LustreDeploymentType.SCRATCH_2
}

fs = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
    lustre_configuration=lustre_configuration,
    storage_capacity_gi_b=1200,
    vpc=vpc,
    vpc_subnet=vpc.private_subnets[0]
)

inst = ec2.Instance(self, "inst",
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.LARGE),
    machine_image=ec2.AmazonLinuxImage(
        generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
    ),
    vpc=vpc,
    vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PUBLIC
    )
)
fs.connections.allow_default_port_from(inst)

# Need to give the instance access to read information about FSx to determine the file system's mount name.
inst.role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonFSxReadOnlyAccess"))

mount_path = "/mnt/fsx"
dns_name = fs.dns_name
mount_name = fs.mount_name

inst.user_data.add_commands("set -eux", "yum update -y", "amazon-linux-extras install -y lustre2.10", f"mkdir -p {mountPath}", f"chmod 777 {mountPath}", f"chown ec2-user:ec2-user {mountPath}", f"echo \"{dnsName}@tcp:/{mountName} {mountPath} lustre defaults,noatime,flock,_netdev 0 0\" >> /etc/fstab", "mount -a")
```

### Importing an existing Lustre filesystem

An FSx for Lustre file system can be imported with `fromLustreFileSystemAttributes(stack, id, attributes)`. The
following example lays out how you could import the SecurityGroup a file system belongs to, use that to import the file
system, and then also import the VPC the file system is in and add an EC2 instance to it, giving it access to the file
system.

```python
sg = ec2.SecurityGroup.from_security_group_id(self, "FsxSecurityGroup", "{SECURITY-GROUP-ID}")
fs = fsx.LustreFileSystem.from_lustre_file_system_attributes(self, "FsxLustreFileSystem",
    dns_name="{FILE-SYSTEM-DNS-NAME}",
    file_system_id="{FILE-SYSTEM-ID}",
    security_group=sg
)

vpc = ec2.Vpc.from_vpc_attributes(self, "Vpc",
    availability_zones=["us-west-2a", "us-west-2b"],
    public_subnet_ids=["{US-WEST-2A-SUBNET-ID}", "{US-WEST-2B-SUBNET-ID}"],
    vpc_id="{VPC-ID}"
)

inst = ec2.Instance(self, "inst",
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.LARGE),
    machine_image=ec2.AmazonLinuxImage(
        generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
    ),
    vpc=vpc,
    vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PUBLIC
    )
)

fs.connections.allow_default_port_from(inst)
```

### Lustre Data Repository Association support

The LustreFilesystem Construct supports one [Data Repository Association](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-data-repositories.html) (DRA) to an S3 bucket.  This allows Lustre hierarchical storage management to S3 buckets, which in turn makes it possible to use S3 as a permanent backing store, and use FSx for Lustre as a temporary high performance cache.

Note: CloudFormation does not currently support for `PERSISTENT_2` filesystems, and so neither does CDK.

The following example illustrates setting up a DRA to an S3 bucket, including automated metadata import whenever a file is changed, created or deleted in the S3 bucket:

```python
# Example automatically generated from non-compiling source. May contain errors.
# vpc: ec2.Vpc
# bucket: s3.Bucket


lustre_configuration = {
    "deployment_type": fsx.LustreDeploymentType.SCRATCH_2,
    "export_path": bucket.s3_url_for_object(),
    "import_path": bucket.s3_url_for_object(),
    "auto_import_policy": fsx.LustreAutoImportPolicy.NEW_CHANGED_DELETED
}

fs = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
    vpc=vpc,
    vpc_subnet=vpc.private_subnets[0],
    storage_capacity_gi_b=1200,
    lustre_configuration=lustre_configuration
)
```

### Compression

By default, transparent compression of data within FSx for Lustre is switched off.  To enable it, add the following to your `lustreConfiguration`:

```python
lustre_configuration = {
    # ...
    "data_compression_type": fsx.LustreDataCompressionType.LZ4
}
```

When you turn data compression on for an existing file system, only newly written files are compressed.  Existing files are not compressed. For more information, see [Compressing previously written files](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html#migrate-compression).```

## FSx for Windows File Server

The L2 construct for the FSx for Windows File Server has not yet been implemented. To instantiate an FSx for Windows
file system, the L1 constructs can be used as defined by CloudFormation.
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
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    ResourceProps as _ResourceProps_15a65b4e,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_ec2 import (
    Connections as _Connections_0f31fce8,
    IConnectable as _IConnectable_10015a05,
    ISecurityGroup as _ISecurityGroup_acf8a799,
    ISubnet as _ISubnet_d57d1229,
    IVpc as _IVpc_f30d5663,
)
from ..aws_kms import IKey as _IKey_5f11635f


@jsii.implements(_IInspectable_c2943556)
class CfnFileSystem(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem",
):
    '''A CloudFormation ``AWS::FSx::FileSystem``.

    The ``AWS::FSx::FileSystem`` resource is an Amazon FSx resource type that specifies an Amazon FSx file system. You can create any of the following supported file system types:

    - Amazon FSx for Lustre
    - Amazon FSx for NetApp ONTAP
    - Amazon FSx for OpenZFS
    - Amazon FSx for Windows File Server

    :cloudformationResource: AWS::FSx::FileSystem
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fsx as fsx
        
        cfn_file_system = fsx.CfnFileSystem(self, "MyCfnFileSystem",
            file_system_type="fileSystemType",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            backup_id="backupId",
            file_system_type_version="fileSystemTypeVersion",
            kms_key_id="kmsKeyId",
            lustre_configuration=fsx.CfnFileSystem.LustreConfigurationProperty(
                auto_import_policy="autoImportPolicy",
                automatic_backup_retention_days=123,
                copy_tags_to_backups=False,
                daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                data_compression_type="dataCompressionType",
                deployment_type="deploymentType",
                drive_cache_type="driveCacheType",
                export_path="exportPath",
                imported_file_chunk_size=123,
                import_path="importPath",
                per_unit_storage_throughput=123,
                weekly_maintenance_start_time="weeklyMaintenanceStartTime"
            ),
            ontap_configuration=fsx.CfnFileSystem.OntapConfigurationProperty(
                deployment_type="deploymentType",
        
                # the properties below are optional
                automatic_backup_retention_days=123,
                daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                disk_iops_configuration=fsx.CfnFileSystem.DiskIopsConfigurationProperty(
                    iops=123,
                    mode="mode"
                ),
                endpoint_ip_address_range="endpointIpAddressRange",
                fsx_admin_password="fsxAdminPassword",
                preferred_subnet_id="preferredSubnetId",
                route_table_ids=["routeTableIds"],
                throughput_capacity=123,
                weekly_maintenance_start_time="weeklyMaintenanceStartTime"
            ),
            open_zfs_configuration=fsx.CfnFileSystem.OpenZFSConfigurationProperty(
                deployment_type="deploymentType",
        
                # the properties below are optional
                automatic_backup_retention_days=123,
                copy_tags_to_backups=False,
                copy_tags_to_volumes=False,
                daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                disk_iops_configuration=fsx.CfnFileSystem.DiskIopsConfigurationProperty(
                    iops=123,
                    mode="mode"
                ),
                options=["options"],
                root_volume_configuration=fsx.CfnFileSystem.RootVolumeConfigurationProperty(
                    copy_tags_to_snapshots=False,
                    data_compression_type="dataCompressionType",
                    nfs_exports=[fsx.CfnFileSystem.NfsExportsProperty(
                        client_configurations=[fsx.CfnFileSystem.ClientConfigurationsProperty(
                            clients="clients",
                            options=["options"]
                        )]
                    )],
                    read_only=False,
                    record_size_ki_b=123,
                    user_and_group_quotas=[fsx.CfnFileSystem.UserAndGroupQuotasProperty(
                        id=123,
                        storage_capacity_quota_gi_b=123,
                        type="type"
                    )]
                ),
                throughput_capacity=123,
                weekly_maintenance_start_time="weeklyMaintenanceStartTime"
            ),
            security_group_ids=["securityGroupIds"],
            storage_capacity=123,
            storage_type="storageType",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            windows_configuration=fsx.CfnFileSystem.WindowsConfigurationProperty(
                throughput_capacity=123,
        
                # the properties below are optional
                active_directory_id="activeDirectoryId",
                aliases=["aliases"],
                audit_log_configuration=fsx.CfnFileSystem.AuditLogConfigurationProperty(
                    file_access_audit_log_level="fileAccessAuditLogLevel",
                    file_share_access_audit_log_level="fileShareAccessAuditLogLevel",
        
                    # the properties below are optional
                    audit_log_destination="auditLogDestination"
                ),
                automatic_backup_retention_days=123,
                copy_tags_to_backups=False,
                daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                deployment_type="deploymentType",
                preferred_subnet_id="preferredSubnetId",
                self_managed_active_directory_configuration=fsx.CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty(
                    dns_ips=["dnsIps"],
                    domain_name="domainName",
                    file_system_administrators_group="fileSystemAdministratorsGroup",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName",
                    password="password",
                    user_name="userName"
                ),
                weekly_maintenance_start_time="weeklyMaintenanceStartTime"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        file_system_type: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        backup_id: typing.Optional[builtins.str] = None,
        file_system_type_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lustre_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.LustreConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ontap_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.OntapConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        open_zfs_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.OpenZFSConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        windows_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.WindowsConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::FSx::FileSystem``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param file_system_type: The type of Amazon FSx file system, which can be ``LUSTRE`` , ``WINDOWS`` , ``ONTAP`` , or ``OPENZFS`` .
        :param subnet_ids: Specifies the IDs of the subnets that the file system will be accessible from. For Windows and ONTAP ``MULTI_AZ_1`` deployment types,provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the ``WindowsConfiguration > PreferredSubnetID`` or ``OntapConfiguration > PreferredSubnetID`` properties. For more information about Multi-AZ file system configuration, see `Availability and durability: Single-AZ and Multi-AZ file systems <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html>`_ in the *Amazon FSx for Windows User Guide* and `Availability and durability <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html>`_ in the *Amazon FSx for ONTAP User Guide* . For Windows ``SINGLE_AZ_1`` and ``SINGLE_AZ_2`` and all Lustre deployment types, provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.
        :param backup_id: The ID of the file system backup that you are using to create a file system. For more information, see `CreateFileSystemFromBackup <https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystemFromBackup.html>`_ .
        :param file_system_type_version: (Optional) For FSx for Lustre file systems, sets the Lustre version for the file system that you're creating. Valid values are ``2.10`` and ``2.12`` : - 2.10 is supported by the Scratch and Persistent_1 Lustre deployment types. - 2.12 is supported by all Lustre deployment types. ``2.12`` is required when setting FSx for Lustre ``DeploymentType`` to ``PERSISTENT_2`` . Default value = ``2.10`` , except when ``DeploymentType`` is set to ``PERSISTENT_2`` , then the default is ``2.12`` . .. epigraph:: If you set ``FileSystemTypeVersion`` to ``2.10`` for a ``PERSISTENT_2`` Lustre deployment type, the ``CreateFileSystem`` operation fails.
        :param kms_key_id: The ID of the AWS Key Management Service ( AWS KMS ) key used to encrypt Amazon FSx file system data. Used as follows with Amazon FSx file system types: - Amazon FSx for Lustre ``PERSISTENT_1`` and ``PERSISTENT_2`` deployment types only. ``SCRATCH_1`` and ``SCRATCH_2`` types are encrypted using the Amazon FSx service AWS KMS key for your account. - Amazon FSx for NetApp ONTAP - Amazon FSx for OpenZFS - Amazon FSx for Windows File Server
        :param lustre_configuration: The Lustre configuration for the file system being created. .. epigraph:: The following parameters are not supported for file systems with the Lustre ``Persistent_2`` deployment type. - ``AutoImportPolicy`` - ``ExportPath`` - ``ImportedChunkSize`` - ``ImportPath``
        :param ontap_configuration: The ONTAP configuration properties of the FSx for ONTAP file system that you are creating.
        :param open_zfs_configuration: The Amazon FSx for OpenZFS configuration properties for the file system that you are creating.
        :param security_group_ids: A list of IDs specifying the security groups to apply to all network interfaces created for file system access. This list isn't returned in later requests to describe the file system.
        :param storage_capacity: Sets the storage capacity of the file system that you're creating. ``StorageCapacity`` is required if you are creating a new file system. Do not include ``StorageCapacity`` if you are creating a file system from a backup. *FSx for Lustre file systems* - The amount of storage capacity that you can configure depends on the value that you set for ``StorageType`` and the Lustre ``DeploymentType`` , as follows: - For ``SCRATCH_2`` , ``PERSISTENT_2`` and ``PERSISTENT_1`` deployment types using SSD storage type, the valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB. - For ``PERSISTENT_1`` HDD file systems, valid values are increments of 6000 GiB for 12 MB/s/TiB file systems and increments of 1800 GiB for 40 MB/s/TiB file systems. - For ``SCRATCH_1`` deployment type, valid values are 1200 GiB, 2400 GiB, and increments of 3600 GiB. *FSx for ONTAP file systems* - The amount of storage capacity that you can configure is from 1024 GiB up to 196,608 GiB (192 TiB). *FSx for OpenZFS file systems* - The amount of storage capacity that you can configure is from 64 GiB up to 524,288 GiB (512 TiB). *FSx for Windows File Server file systems* - The amount of storage capacity that you can configure depends on the value that you set for ``StorageType`` as follows: - For SSD storage, valid values are 32 GiB-65,536 GiB (64 TiB). - For HDD storage, valid values are 2000 GiB-65,536 GiB (64 TiB).
        :param storage_type: Sets the storage type for the file system that you're creating. Valid values are ``SSD`` and ``HDD`` . - Set to ``SSD`` to use solid state drive storage. SSD is supported on all Windows, Lustre, ONTAP, and OpenZFS deployment types. - Set to ``HDD`` to use hard disk drive storage. HDD is supported on ``SINGLE_AZ_2`` and ``MULTI_AZ_1`` Windows file system deployment types, and on ``PERSISTENT_1`` Lustre file system deployment types. Default value is ``SSD`` . For more information, see `Storage type options <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/optimize-fsx-costs.html#storage-type-options>`_ in the *FSx for Windows File Server User Guide* and `Multiple storage options <https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html#storage-options>`_ in the *FSx for Lustre User Guide* .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param windows_configuration: The configuration object for the Microsoft Windows file system you are creating. This value is required if ``FileSystemType`` is set to ``WINDOWS`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFileSystem.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFileSystemProps(
            file_system_type=file_system_type,
            subnet_ids=subnet_ids,
            backup_id=backup_id,
            file_system_type_version=file_system_type_version,
            kms_key_id=kms_key_id,
            lustre_configuration=lustre_configuration,
            ontap_configuration=ontap_configuration,
            open_zfs_configuration=open_zfs_configuration,
            security_group_ids=security_group_ids,
            storage_capacity=storage_capacity,
            storage_type=storage_type,
            tags=tags,
            windows_configuration=windows_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFileSystem.inspect)
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
            type_hints = typing.get_type_hints(CfnFileSystem._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDnsName")
    def attr_dns_name(self) -> builtins.str:
        '''Returns the FSx for Windows file system's DNSName.

        Example: ``amznfsxp1honlek.corp.example.com``

        :cloudformationAttribute: DNSName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLustreMountName")
    def attr_lustre_mount_name(self) -> builtins.str:
        '''Returns the file system's LustreMountName.

        Example for SCRATCH_1 deployment types: This value is always ``fsx`` .

        Example for SCRATCH_2 and PERSISTENT deployment types: ``2p3fhbmv``

        :cloudformationAttribute: LustreMountName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLustreMountName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRootVolumeId")
    def attr_root_volume_id(self) -> builtins.str:
        '''Returns the root volume ID of the FSx for OpenZFS file system.

        Example: ``fsvol-0123456789abcdefa``

        :cloudformationAttribute: RootVolumeId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRootVolumeId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileSystemType")
    def file_system_type(self) -> builtins.str:
        '''The type of Amazon FSx file system, which can be ``LUSTRE`` , ``WINDOWS`` , ``ONTAP`` , or ``OPENZFS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-filesystemtype
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemType"))

    @file_system_type.setter
    def file_system_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "file_system_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Specifies the IDs of the subnets that the file system will be accessible from.

        For Windows and ONTAP ``MULTI_AZ_1`` deployment types,provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the ``WindowsConfiguration > PreferredSubnetID`` or ``OntapConfiguration > PreferredSubnetID`` properties. For more information about Multi-AZ file system configuration, see `Availability and durability: Single-AZ and Multi-AZ file systems <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html>`_ in the *Amazon FSx for Windows User Guide* and `Availability and durability <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html>`_ in the *Amazon FSx for ONTAP User Guide* .

        For Windows ``SINGLE_AZ_1`` and ``SINGLE_AZ_2`` and all Lustre deployment types, provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="backupId")
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the file system backup that you are using to create a file system.

        For more information, see `CreateFileSystemFromBackup <https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystemFromBackup.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-backupid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupId"))

    @backup_id.setter
    def backup_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "backup_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileSystemTypeVersion")
    def file_system_type_version(self) -> typing.Optional[builtins.str]:
        '''(Optional) For FSx for Lustre file systems, sets the Lustre version for the file system that you're creating.

        Valid values are ``2.10`` and ``2.12`` :

        - 2.10 is supported by the Scratch and Persistent_1 Lustre deployment types.
        - 2.12 is supported by all Lustre deployment types. ``2.12`` is required when setting FSx for Lustre ``DeploymentType`` to ``PERSISTENT_2`` .

        Default value = ``2.10`` , except when ``DeploymentType`` is set to ``PERSISTENT_2`` , then the default is ``2.12`` .
        .. epigraph::

           If you set ``FileSystemTypeVersion`` to ``2.10`` for a ``PERSISTENT_2`` Lustre deployment type, the ``CreateFileSystem`` operation fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-filesystemtypeversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemTypeVersion"))

    @file_system_type_version.setter
    def file_system_type_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "file_system_type_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemTypeVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service ( AWS KMS ) key used to encrypt Amazon FSx file system data.

        Used as follows with Amazon FSx file system types:

        - Amazon FSx for Lustre ``PERSISTENT_1`` and ``PERSISTENT_2`` deployment types only.

        ``SCRATCH_1`` and ``SCRATCH_2`` types are encrypted using the Amazon FSx service AWS KMS key for your account.

        - Amazon FSx for NetApp ONTAP
        - Amazon FSx for OpenZFS
        - Amazon FSx for Windows File Server

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lustreConfiguration")
    def lustre_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnFileSystem.LustreConfigurationProperty", _IResolvable_da3f097b]]:
        '''The Lustre configuration for the file system being created.

        .. epigraph::

           The following parameters are not supported for file systems with the Lustre ``Persistent_2`` deployment type.

           - ``AutoImportPolicy``
           - ``ExportPath``
           - ``ImportedChunkSize``
           - ``ImportPath``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-lustreconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFileSystem.LustreConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "lustreConfiguration"))

    @lustre_configuration.setter
    def lustre_configuration(
        self,
        value: typing.Optional[typing.Union["CfnFileSystem.LustreConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "lustre_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lustreConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ontapConfiguration")
    def ontap_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnFileSystem.OntapConfigurationProperty", _IResolvable_da3f097b]]:
        '''The ONTAP configuration properties of the FSx for ONTAP file system that you are creating.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-ontapconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFileSystem.OntapConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "ontapConfiguration"))

    @ontap_configuration.setter
    def ontap_configuration(
        self,
        value: typing.Optional[typing.Union["CfnFileSystem.OntapConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "ontap_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ontapConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="openZfsConfiguration")
    def open_zfs_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnFileSystem.OpenZFSConfigurationProperty", _IResolvable_da3f097b]]:
        '''The Amazon FSx for OpenZFS configuration properties for the file system that you are creating.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-openzfsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFileSystem.OpenZFSConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "openZfsConfiguration"))

    @open_zfs_configuration.setter
    def open_zfs_configuration(
        self,
        value: typing.Optional[typing.Union["CfnFileSystem.OpenZFSConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "open_zfs_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openZfsConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IDs specifying the security groups to apply to all network interfaces created for file system access.

        This list isn't returned in later requests to describe the file system.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-securitygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="storageCapacity")
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        '''Sets the storage capacity of the file system that you're creating.

        ``StorageCapacity`` is required if you are creating a new file system. Do not include ``StorageCapacity`` if you are creating a file system from a backup.

        *FSx for Lustre file systems* - The amount of storage capacity that you can configure depends on the value that you set for ``StorageType`` and the Lustre ``DeploymentType`` , as follows:

        - For ``SCRATCH_2`` , ``PERSISTENT_2`` and ``PERSISTENT_1`` deployment types using SSD storage type, the valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.
        - For ``PERSISTENT_1`` HDD file systems, valid values are increments of 6000 GiB for 12 MB/s/TiB file systems and increments of 1800 GiB for 40 MB/s/TiB file systems.
        - For ``SCRATCH_1`` deployment type, valid values are 1200 GiB, 2400 GiB, and increments of 3600 GiB.

        *FSx for ONTAP file systems* - The amount of storage capacity that you can configure is from 1024 GiB up to 196,608 GiB (192 TiB).

        *FSx for OpenZFS file systems* - The amount of storage capacity that you can configure is from 64 GiB up to 524,288 GiB (512 TiB).

        *FSx for Windows File Server file systems* - The amount of storage capacity that you can configure depends on the value that you set for ``StorageType`` as follows:

        - For SSD storage, valid values are 32 GiB-65,536 GiB (64 TiB).
        - For HDD storage, valid values are 2000 GiB-65,536 GiB (64 TiB).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagecapacity
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacity"))

    @storage_capacity.setter
    def storage_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "storage_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''Sets the storage type for the file system that you're creating. Valid values are ``SSD`` and ``HDD`` .

        - Set to ``SSD`` to use solid state drive storage. SSD is supported on all Windows, Lustre, ONTAP, and OpenZFS deployment types.
        - Set to ``HDD`` to use hard disk drive storage. HDD is supported on ``SINGLE_AZ_2`` and ``MULTI_AZ_1`` Windows file system deployment types, and on ``PERSISTENT_1`` Lustre file system deployment types.

        Default value is ``SSD`` . For more information, see `Storage type options <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/optimize-fsx-costs.html#storage-type-options>`_ in the *FSx for Windows File Server User Guide* and `Multiple storage options <https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html#storage-options>`_ in the *FSx for Lustre User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "storage_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="windowsConfiguration")
    def windows_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnFileSystem.WindowsConfigurationProperty", _IResolvable_da3f097b]]:
        '''The configuration object for the Microsoft Windows file system you are creating.

        This value is required if ``FileSystemType`` is set to ``WINDOWS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-windowsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFileSystem.WindowsConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "windowsConfiguration"))

    @windows_configuration.setter
    def windows_configuration(
        self,
        value: typing.Optional[typing.Union["CfnFileSystem.WindowsConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFileSystem, "windows_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowsConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.AuditLogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "file_access_audit_log_level": "fileAccessAuditLogLevel",
            "file_share_access_audit_log_level": "fileShareAccessAuditLogLevel",
            "audit_log_destination": "auditLogDestination",
        },
    )
    class AuditLogConfigurationProperty:
        def __init__(
            self,
            *,
            file_access_audit_log_level: builtins.str,
            file_share_access_audit_log_level: builtins.str,
            audit_log_destination: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.

            :param file_access_audit_log_level: Sets which attempt type is logged by Amazon FSx for file and folder accesses. - ``SUCCESS_ONLY`` - only successful attempts to access files or folders are logged. - ``FAILURE_ONLY`` - only failed attempts to access files or folders are logged. - ``SUCCESS_AND_FAILURE`` - both successful attempts and failed attempts to access files or folders are logged. - ``DISABLED`` - access auditing of files and folders is turned off.
            :param file_share_access_audit_log_level: Sets which attempt type is logged by Amazon FSx for file share accesses. - ``SUCCESS_ONLY`` - only successful attempts to access file shares are logged. - ``FAILURE_ONLY`` - only failed attempts to access file shares are logged. - ``SUCCESS_AND_FAILURE`` - both successful attempts and failed attempts to access file shares are logged. - ``DISABLED`` - access auditing of file shares is turned off.
            :param audit_log_destination: The Amazon Resource Name (ARN) for the destination of the audit logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN. The name of the Amazon CloudWatch Logs log group must begin with the ``/aws/fsx`` prefix. The name of the Amazon Kinesis Data Firehouse delivery stream must begin with the ``aws-fsx`` prefix. The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same AWS partition, AWS Region , and AWS account as your Amazon FSx file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                audit_log_configuration_property = fsx.CfnFileSystem.AuditLogConfigurationProperty(
                    file_access_audit_log_level="fileAccessAuditLogLevel",
                    file_share_access_audit_log_level="fileShareAccessAuditLogLevel",
                
                    # the properties below are optional
                    audit_log_destination="auditLogDestination"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.AuditLogConfigurationProperty.__init__)
                check_type(argname="argument file_access_audit_log_level", value=file_access_audit_log_level, expected_type=type_hints["file_access_audit_log_level"])
                check_type(argname="argument file_share_access_audit_log_level", value=file_share_access_audit_log_level, expected_type=type_hints["file_share_access_audit_log_level"])
                check_type(argname="argument audit_log_destination", value=audit_log_destination, expected_type=type_hints["audit_log_destination"])
            self._values: typing.Dict[str, typing.Any] = {
                "file_access_audit_log_level": file_access_audit_log_level,
                "file_share_access_audit_log_level": file_share_access_audit_log_level,
            }
            if audit_log_destination is not None:
                self._values["audit_log_destination"] = audit_log_destination

        @builtins.property
        def file_access_audit_log_level(self) -> builtins.str:
            '''Sets which attempt type is logged by Amazon FSx for file and folder accesses.

            - ``SUCCESS_ONLY`` - only successful attempts to access files or folders are logged.
            - ``FAILURE_ONLY`` - only failed attempts to access files or folders are logged.
            - ``SUCCESS_AND_FAILURE`` - both successful attempts and failed attempts to access files or folders are logged.
            - ``DISABLED`` - access auditing of files and folders is turned off.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-auditlogconfiguration-fileaccessauditloglevel
            '''
            result = self._values.get("file_access_audit_log_level")
            assert result is not None, "Required property 'file_access_audit_log_level' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def file_share_access_audit_log_level(self) -> builtins.str:
            '''Sets which attempt type is logged by Amazon FSx for file share accesses.

            - ``SUCCESS_ONLY`` - only successful attempts to access file shares are logged.
            - ``FAILURE_ONLY`` - only failed attempts to access file shares are logged.
            - ``SUCCESS_AND_FAILURE`` - both successful attempts and failed attempts to access file shares are logged.
            - ``DISABLED`` - access auditing of file shares is turned off.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-auditlogconfiguration-fileshareaccessauditloglevel
            '''
            result = self._values.get("file_share_access_audit_log_level")
            assert result is not None, "Required property 'file_share_access_audit_log_level' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def audit_log_destination(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the destination of the audit logs.

            The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.

            The name of the Amazon CloudWatch Logs log group must begin with the ``/aws/fsx`` prefix. The name of the Amazon Kinesis Data Firehouse delivery stream must begin with the ``aws-fsx`` prefix.

            The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same AWS partition, AWS Region , and AWS account as your Amazon FSx file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-auditlogconfiguration-auditlogdestination
            '''
            result = self._values.get("audit_log_destination")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditLogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.ClientConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={"clients": "clients", "options": "options"},
    )
    class ClientConfigurationsProperty:
        def __init__(
            self,
            *,
            clients: typing.Optional[builtins.str] = None,
            options: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies who can mount an OpenZFS file system and the options available while mounting the file system.

            :param clients: A value that specifies who can mount the file system. You can provide a wildcard character ( ``*`` ), an IP address ( ``0.0.0.0`` ), or a CIDR address ( ``192.0.2.0/24`` ). By default, Amazon FSx uses the wildcard character when specifying the client.
            :param options: The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the `exports(5) - Linux man page <https://docs.aws.amazon.com/https://linux.die.net/man/5/exports>`_ . When choosing your options, consider the following: - ``crossmnt`` is used by default. If you don't specify ``crossmnt`` when changing the client configuration, you won't be able to see or access snapshots in your file system's snapshot directory. - ``sync`` is used by default. If you instead specify ``async`` , the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                client_configurations_property = fsx.CfnFileSystem.ClientConfigurationsProperty(
                    clients="clients",
                    options=["options"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.ClientConfigurationsProperty.__init__)
                check_type(argname="argument clients", value=clients, expected_type=type_hints["clients"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            self._values: typing.Dict[str, typing.Any] = {}
            if clients is not None:
                self._values["clients"] = clients
            if options is not None:
                self._values["options"] = options

        @builtins.property
        def clients(self) -> typing.Optional[builtins.str]:
            '''A value that specifies who can mount the file system.

            You can provide a wildcard character ( ``*`` ), an IP address ( ``0.0.0.0`` ), or a CIDR address ( ``192.0.2.0/24`` ). By default, Amazon FSx uses the wildcard character when specifying the client.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations-clients
            '''
            result = self._values.get("clients")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def options(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The options to use when mounting the file system.

            For a list of options that you can use with Network File System (NFS), see the `exports(5) - Linux man page <https://docs.aws.amazon.com/https://linux.die.net/man/5/exports>`_ . When choosing your options, consider the following:

            - ``crossmnt`` is used by default. If you don't specify ``crossmnt`` when changing the client configuration, you won't be able to see or access snapshots in your file system's snapshot directory.
            - ``sync`` is used by default. If you instead specify ``async`` , the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.DiskIopsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"iops": "iops", "mode": "mode"},
    )
    class DiskIopsConfigurationProperty:
        def __init__(
            self,
            *,
            iops: typing.Optional[jsii.Number] = None,
            mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS file system.

            The default is 3 IOPS per GB of storage capacity, but you can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how the amount was provisioned (by the customer or by the system).

            :param iops: The total number of SSD IOPS provisioned for the file system.
            :param mode: Specifies whether the number of IOPS for the file system is using the system default ( ``AUTOMATIC`` ) or was provisioned by the customer ( ``USER_PROVISIONED`` ).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                disk_iops_configuration_property = fsx.CfnFileSystem.DiskIopsConfigurationProperty(
                    iops=123,
                    mode="mode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.DiskIopsConfigurationProperty.__init__)
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            self._values: typing.Dict[str, typing.Any] = {}
            if iops is not None:
                self._values["iops"] = iops
            if mode is not None:
                self._values["mode"] = mode

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The total number of SSD IOPS provisioned for the file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''Specifies whether the number of IOPS for the file system is using the system default ( ``AUTOMATIC`` ) or was provisioned by the customer ( ``USER_PROVISIONED`` ).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DiskIopsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.LustreConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_import_policy": "autoImportPolicy",
            "automatic_backup_retention_days": "automaticBackupRetentionDays",
            "copy_tags_to_backups": "copyTagsToBackups",
            "daily_automatic_backup_start_time": "dailyAutomaticBackupStartTime",
            "data_compression_type": "dataCompressionType",
            "deployment_type": "deploymentType",
            "drive_cache_type": "driveCacheType",
            "export_path": "exportPath",
            "imported_file_chunk_size": "importedFileChunkSize",
            "import_path": "importPath",
            "per_unit_storage_throughput": "perUnitStorageThroughput",
            "weekly_maintenance_start_time": "weeklyMaintenanceStartTime",
        },
    )
    class LustreConfigurationProperty:
        def __init__(
            self,
            *,
            auto_import_policy: typing.Optional[builtins.str] = None,
            automatic_backup_retention_days: typing.Optional[jsii.Number] = None,
            copy_tags_to_backups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            daily_automatic_backup_start_time: typing.Optional[builtins.str] = None,
            data_compression_type: typing.Optional[builtins.str] = None,
            deployment_type: typing.Optional[builtins.str] = None,
            drive_cache_type: typing.Optional[builtins.str] = None,
            export_path: typing.Optional[builtins.str] = None,
            imported_file_chunk_size: typing.Optional[jsii.Number] = None,
            import_path: typing.Optional[builtins.str] = None,
            per_unit_storage_throughput: typing.Optional[jsii.Number] = None,
            weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for the Amazon FSx for Lustre file system.

            :param auto_import_policy: (Optional) Available with ``Scratch`` and ``Persistent_1`` deployment types. When you create your file system, your existing S3 objects appear as file and directory listings. Use this property to choose how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. ``AutoImportPolicy`` can have the following values: - ``NONE`` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option. - ``NEW`` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system. - ``NEW_CHANGED`` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option. - ``NEW_CHANGED_DELETED`` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket. For more information, see `Automatically import updates from your S3 bucket <https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoimport-data-repo.html>`_ . .. epigraph:: This parameter is not supported for Lustre file systems using the ``Persistent_2`` deployment type.
            :param automatic_backup_retention_days: The number of days to retain automatic backups. Setting this property to ``0`` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is ``0`` .
            :param copy_tags_to_backups: A Boolean flag indicating whether tags for the file system should be copied to backups. This value defaults to false. If it's set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. Only valid for use with ``PERSISTENT_1`` deployment types.
            :param daily_automatic_backup_start_time: A recurring daily time, in the format ``HH:MM`` . ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``05:00`` specifies 5 AM daily.
            :param data_compression_type: Sets the data compression configuration for the file system. ``DataCompressionType`` can have the following values:. - ``NONE`` - (Default) Data compression is turned off when the file system is created. - ``LZ4`` - Data compression is turned on with the LZ4 algorithm. For more information, see `Lustre data compression <https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html>`_ in the *Amazon FSx for Lustre User Guide* .
            :param deployment_type: (Optional) Choose ``SCRATCH_1`` and ``SCRATCH_2`` deployment types when you need temporary storage and shorter-term processing of data. The ``SCRATCH_2`` deployment type provides in-transit encryption of data and higher burst throughput capacity than ``SCRATCH_1`` . Choose ``PERSISTENT_1`` for longer-term storage and for throughput-focused workloads that aren’t latency-sensitive. ``PERSISTENT_1`` supports encryption of data in transit, and is available in all AWS Regions in which FSx for Lustre is available. Choose ``PERSISTENT_2`` for longer-term storage and for latency-sensitive workloads that require the highest levels of IOPS/throughput. ``PERSISTENT_2`` supports SSD storage, and offers higher ``PerUnitStorageThroughput`` (up to 1000 MB/s/TiB). ``PERSISTENT_2`` is available in a limited number of AWS Regions . For more information, and an up-to-date list of AWS Regions in which ``PERSISTENT_2`` is available, see `File system deployment options for FSx for Lustre <https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html#lustre-deployment-types>`_ in the *Amazon FSx for Lustre User Guide* . .. epigraph:: If you choose ``PERSISTENT_2`` , and you set ``FileSystemTypeVersion`` to ``2.10`` , the ``CreateFileSystem`` operation fails. Encryption of data in transit is automatically turned on when you access ``SCRATCH_2`` , ``PERSISTENT_1`` and ``PERSISTENT_2`` file systems from Amazon EC2 instances that [support automatic encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data- protection.html) in the AWS Regions where they are available. For more information about encryption in transit for FSx for Lustre file systems, see `Encrypting data in transit <https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-in-transit-fsxl.html>`_ in the *Amazon FSx for Lustre User Guide* . (Default = ``SCRATCH_1`` )
            :param drive_cache_type: The type of drive cache used by ``PERSISTENT_1`` file systems that are provisioned with HDD storage devices. This parameter is required when storage type is HDD. Set this property to ``READ`` to improve the performance for frequently accessed files by caching up to 20% of the total storage capacity of the file system. This parameter is required when ``StorageType`` is set to ``HDD`` and ``DeploymentType`` is ``PERSISTENT_1`` .
            :param export_path: (Optional) Available with ``Scratch`` and ``Persistent_1`` deployment types. Specifies the path in the Amazon S3 bucket where the root of your Amazon FSx file system is exported. The path must use the same Amazon S3 bucket as specified in ImportPath. You can provide an optional prefix to which new and changed data is to be exported from your Amazon FSx for Lustre file system. If an ``ExportPath`` value is not provided, Amazon FSx sets a default export path, ``s3://import-bucket/FSxLustre[creation-timestamp]`` . The timestamp is in UTC format, for example ``s3://import-bucket/FSxLustre20181105T222312Z`` . The Amazon S3 export bucket must be the same as the import bucket specified by ``ImportPath`` . If you specify only a bucket name, such as ``s3://import-bucket`` , you get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is overwritten on export. If you provide a custom prefix in the export path, such as ``s3://import-bucket/[custom-optional-prefix]`` , Amazon FSx exports the contents of your file system to that export prefix in the Amazon S3 bucket. .. epigraph:: This parameter is not supported for file systems using the ``Persistent_2`` deployment type.
            :param imported_file_chunk_size: (Optional) For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system. The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB. .. epigraph:: This parameter is not supported for Lustre file systems using the ``Persistent_2`` deployment type.
            :param import_path: (Optional) The path to the Amazon S3 bucket (including the optional prefix) that you're using as the data repository for your Amazon FSx for Lustre file system. The root of your FSx for Lustre file system will be mapped to the root of the Amazon S3 bucket you select. An example is ``s3://import-bucket/optional-prefix`` . If you specify a prefix after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system. .. epigraph:: This parameter is not supported for Lustre file systems using the ``Persistent_2`` deployment type.
            :param per_unit_storage_throughput: Required with ``PERSISTENT_1`` and ``PERSISTENT_2`` deployment types, provisions the amount of read and write throughput for each 1 tebibyte (TiB) of file system storage capacity, in MB/s/TiB. File system throughput capacity is calculated by multiplying ﬁle system storage capacity (TiB) by the ``PerUnitStorageThroughput`` (MB/s/TiB). For a 2.4-TiB ﬁle system, provisioning 50 MB/s/TiB of ``PerUnitStorageThroughput`` yields 120 MB/s of ﬁle system throughput. You pay for the amount of throughput that you provision. Valid values: - For ``PERSISTENT_1`` SSD storage: 50, 100, 200 MB/s/TiB. - For ``PERSISTENT_1`` HDD storage: 12, 40 MB/s/TiB. - For ``PERSISTENT_2`` SSD storage: 125, 250, 500, 1000 MB/s/TiB.
            :param weekly_maintenance_start_time: A recurring weekly time, in the format ``D:HH:MM`` . ``D`` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see `the ISO-8601 spec as described on Wikipedia <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_week_date>`_ . ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``1:05:00`` specifies maintenance at 5 AM Monday.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                lustre_configuration_property = fsx.CfnFileSystem.LustreConfigurationProperty(
                    auto_import_policy="autoImportPolicy",
                    automatic_backup_retention_days=123,
                    copy_tags_to_backups=False,
                    daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                    data_compression_type="dataCompressionType",
                    deployment_type="deploymentType",
                    drive_cache_type="driveCacheType",
                    export_path="exportPath",
                    imported_file_chunk_size=123,
                    import_path="importPath",
                    per_unit_storage_throughput=123,
                    weekly_maintenance_start_time="weeklyMaintenanceStartTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.LustreConfigurationProperty.__init__)
                check_type(argname="argument auto_import_policy", value=auto_import_policy, expected_type=type_hints["auto_import_policy"])
                check_type(argname="argument automatic_backup_retention_days", value=automatic_backup_retention_days, expected_type=type_hints["automatic_backup_retention_days"])
                check_type(argname="argument copy_tags_to_backups", value=copy_tags_to_backups, expected_type=type_hints["copy_tags_to_backups"])
                check_type(argname="argument daily_automatic_backup_start_time", value=daily_automatic_backup_start_time, expected_type=type_hints["daily_automatic_backup_start_time"])
                check_type(argname="argument data_compression_type", value=data_compression_type, expected_type=type_hints["data_compression_type"])
                check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
                check_type(argname="argument drive_cache_type", value=drive_cache_type, expected_type=type_hints["drive_cache_type"])
                check_type(argname="argument export_path", value=export_path, expected_type=type_hints["export_path"])
                check_type(argname="argument imported_file_chunk_size", value=imported_file_chunk_size, expected_type=type_hints["imported_file_chunk_size"])
                check_type(argname="argument import_path", value=import_path, expected_type=type_hints["import_path"])
                check_type(argname="argument per_unit_storage_throughput", value=per_unit_storage_throughput, expected_type=type_hints["per_unit_storage_throughput"])
                check_type(argname="argument weekly_maintenance_start_time", value=weekly_maintenance_start_time, expected_type=type_hints["weekly_maintenance_start_time"])
            self._values: typing.Dict[str, typing.Any] = {}
            if auto_import_policy is not None:
                self._values["auto_import_policy"] = auto_import_policy
            if automatic_backup_retention_days is not None:
                self._values["automatic_backup_retention_days"] = automatic_backup_retention_days
            if copy_tags_to_backups is not None:
                self._values["copy_tags_to_backups"] = copy_tags_to_backups
            if daily_automatic_backup_start_time is not None:
                self._values["daily_automatic_backup_start_time"] = daily_automatic_backup_start_time
            if data_compression_type is not None:
                self._values["data_compression_type"] = data_compression_type
            if deployment_type is not None:
                self._values["deployment_type"] = deployment_type
            if drive_cache_type is not None:
                self._values["drive_cache_type"] = drive_cache_type
            if export_path is not None:
                self._values["export_path"] = export_path
            if imported_file_chunk_size is not None:
                self._values["imported_file_chunk_size"] = imported_file_chunk_size
            if import_path is not None:
                self._values["import_path"] = import_path
            if per_unit_storage_throughput is not None:
                self._values["per_unit_storage_throughput"] = per_unit_storage_throughput
            if weekly_maintenance_start_time is not None:
                self._values["weekly_maintenance_start_time"] = weekly_maintenance_start_time

        @builtins.property
        def auto_import_policy(self) -> typing.Optional[builtins.str]:
            '''(Optional) Available with ``Scratch`` and ``Persistent_1`` deployment types.

            When you create your file system, your existing S3 objects appear as file and directory listings. Use this property to choose how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. ``AutoImportPolicy`` can have the following values:

            - ``NONE`` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
            - ``NEW`` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system.
            - ``NEW_CHANGED`` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
            - ``NEW_CHANGED_DELETED`` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.

            For more information, see `Automatically import updates from your S3 bucket <https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoimport-data-repo.html>`_ .
            .. epigraph::

               This parameter is not supported for Lustre file systems using the ``Persistent_2`` deployment type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-autoimportpolicy
            '''
            result = self._values.get("auto_import_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def automatic_backup_retention_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days to retain automatic backups.

            Setting this property to ``0`` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is ``0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-automaticbackupretentiondays
            '''
            result = self._values.get("automatic_backup_retention_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def copy_tags_to_backups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean flag indicating whether tags for the file system should be copied to backups.

            This value defaults to false. If it's set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. Only valid for use with ``PERSISTENT_1`` deployment types.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-copytagstobackups
            '''
            result = self._values.get("copy_tags_to_backups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def daily_automatic_backup_start_time(self) -> typing.Optional[builtins.str]:
            '''A recurring daily time, in the format ``HH:MM`` .

            ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``05:00`` specifies 5 AM daily.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-dailyautomaticbackupstarttime
            '''
            result = self._values.get("daily_automatic_backup_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_compression_type(self) -> typing.Optional[builtins.str]:
            '''Sets the data compression configuration for the file system. ``DataCompressionType`` can have the following values:.

            - ``NONE`` - (Default) Data compression is turned off when the file system is created.
            - ``LZ4`` - Data compression is turned on with the LZ4 algorithm.

            For more information, see `Lustre data compression <https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html>`_ in the *Amazon FSx for Lustre User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-datacompressiontype
            '''
            result = self._values.get("data_compression_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def deployment_type(self) -> typing.Optional[builtins.str]:
            '''(Optional) Choose ``SCRATCH_1`` and ``SCRATCH_2`` deployment types when you need temporary storage and shorter-term processing of data.

            The ``SCRATCH_2`` deployment type provides in-transit encryption of data and higher burst throughput capacity than ``SCRATCH_1`` .

            Choose ``PERSISTENT_1`` for longer-term storage and for throughput-focused workloads that aren’t latency-sensitive. ``PERSISTENT_1`` supports encryption of data in transit, and is available in all AWS Regions in which FSx for Lustre is available.

            Choose ``PERSISTENT_2`` for longer-term storage and for latency-sensitive workloads that require the highest levels of IOPS/throughput. ``PERSISTENT_2`` supports SSD storage, and offers higher ``PerUnitStorageThroughput`` (up to 1000 MB/s/TiB). ``PERSISTENT_2`` is available in a limited number of AWS Regions . For more information, and an up-to-date list of AWS Regions in which ``PERSISTENT_2`` is available, see `File system deployment options for FSx for Lustre <https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html#lustre-deployment-types>`_ in the *Amazon FSx for Lustre User Guide* .
            .. epigraph::

               If you choose ``PERSISTENT_2`` , and you set ``FileSystemTypeVersion`` to ``2.10`` , the ``CreateFileSystem`` operation fails.

            Encryption of data in transit is automatically turned on when you access ``SCRATCH_2`` , ``PERSISTENT_1`` and ``PERSISTENT_2`` file systems from Amazon EC2 instances that [support automatic encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-                 protection.html) in the AWS Regions where they are available. For more information about encryption in transit for FSx for Lustre file systems, see `Encrypting data in transit <https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-in-transit-fsxl.html>`_ in the *Amazon FSx for Lustre User Guide* .

            (Default = ``SCRATCH_1`` )

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-deploymenttype
            '''
            result = self._values.get("deployment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def drive_cache_type(self) -> typing.Optional[builtins.str]:
            '''The type of drive cache used by ``PERSISTENT_1`` file systems that are provisioned with HDD storage devices.

            This parameter is required when storage type is HDD. Set this property to ``READ`` to improve the performance for frequently accessed files by caching up to 20% of the total storage capacity of the file system.

            This parameter is required when ``StorageType`` is set to ``HDD`` and ``DeploymentType`` is ``PERSISTENT_1`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-drivecachetype
            '''
            result = self._values.get("drive_cache_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def export_path(self) -> typing.Optional[builtins.str]:
            '''(Optional) Available with ``Scratch`` and ``Persistent_1`` deployment types.

            Specifies the path in the Amazon S3 bucket where the root of your Amazon FSx file system is exported. The path must use the same Amazon S3 bucket as specified in ImportPath. You can provide an optional prefix to which new and changed data is to be exported from your Amazon FSx for Lustre file system. If an ``ExportPath`` value is not provided, Amazon FSx sets a default export path, ``s3://import-bucket/FSxLustre[creation-timestamp]`` . The timestamp is in UTC format, for example ``s3://import-bucket/FSxLustre20181105T222312Z`` .

            The Amazon S3 export bucket must be the same as the import bucket specified by ``ImportPath`` . If you specify only a bucket name, such as ``s3://import-bucket`` , you get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is overwritten on export. If you provide a custom prefix in the export path, such as ``s3://import-bucket/[custom-optional-prefix]`` , Amazon FSx exports the contents of your file system to that export prefix in the Amazon S3 bucket.
            .. epigraph::

               This parameter is not supported for file systems using the ``Persistent_2`` deployment type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-exportpath
            '''
            result = self._values.get("export_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def imported_file_chunk_size(self) -> typing.Optional[jsii.Number]:
            '''(Optional) For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk.

            The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.

            The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.
            .. epigraph::

               This parameter is not supported for Lustre file systems using the ``Persistent_2`` deployment type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-importedfilechunksize
            '''
            result = self._values.get("imported_file_chunk_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def import_path(self) -> typing.Optional[builtins.str]:
            '''(Optional) The path to the Amazon S3 bucket (including the optional prefix) that you're using as the data repository for your Amazon FSx for Lustre file system.

            The root of your FSx for Lustre file system will be mapped to the root of the Amazon S3 bucket you select. An example is ``s3://import-bucket/optional-prefix`` . If you specify a prefix after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.
            .. epigraph::

               This parameter is not supported for Lustre file systems using the ``Persistent_2`` deployment type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-importpath
            '''
            result = self._values.get("import_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def per_unit_storage_throughput(self) -> typing.Optional[jsii.Number]:
            '''Required with ``PERSISTENT_1`` and ``PERSISTENT_2`` deployment types, provisions the amount of read and write throughput for each 1 tebibyte (TiB) of file system storage capacity, in MB/s/TiB.

            File system throughput capacity is calculated by multiplying ﬁle system storage capacity (TiB) by the ``PerUnitStorageThroughput`` (MB/s/TiB). For a 2.4-TiB ﬁle system, provisioning 50 MB/s/TiB of ``PerUnitStorageThroughput`` yields 120 MB/s of ﬁle system throughput. You pay for the amount of throughput that you provision.

            Valid values:

            - For ``PERSISTENT_1`` SSD storage: 50, 100, 200 MB/s/TiB.
            - For ``PERSISTENT_1`` HDD storage: 12, 40 MB/s/TiB.
            - For ``PERSISTENT_2`` SSD storage: 125, 250, 500, 1000 MB/s/TiB.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput
            '''
            result = self._values.get("per_unit_storage_throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def weekly_maintenance_start_time(self) -> typing.Optional[builtins.str]:
            '''A recurring weekly time, in the format ``D:HH:MM`` .

            ``D`` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see `the ISO-8601 spec as described on Wikipedia <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_week_date>`_ .

            ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour.

            For example, ``1:05:00`` specifies maintenance at 5 AM Monday.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-weeklymaintenancestarttime
            '''
            result = self._values.get("weekly_maintenance_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LustreConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.NfsExportsProperty",
        jsii_struct_bases=[],
        name_mapping={"client_configurations": "clientConfigurations"},
    )
    class NfsExportsProperty:
        def __init__(
            self,
            *,
            client_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnFileSystem.ClientConfigurationsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The configuration object for mounting a file system.

            :param client_configurations: A list of configuration objects that contain the client and options for mounting the OpenZFS file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                nfs_exports_property = fsx.CfnFileSystem.NfsExportsProperty(
                    client_configurations=[fsx.CfnFileSystem.ClientConfigurationsProperty(
                        clients="clients",
                        options=["options"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.NfsExportsProperty.__init__)
                check_type(argname="argument client_configurations", value=client_configurations, expected_type=type_hints["client_configurations"])
            self._values: typing.Dict[str, typing.Any] = {}
            if client_configurations is not None:
                self._values["client_configurations"] = client_configurations

        @builtins.property
        def client_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFileSystem.ClientConfigurationsProperty", _IResolvable_da3f097b]]]]:
            '''A list of configuration objects that contain the client and options for mounting the OpenZFS file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations
            '''
            result = self._values.get("client_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFileSystem.ClientConfigurationsProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NfsExportsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.OntapConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deployment_type": "deploymentType",
            "automatic_backup_retention_days": "automaticBackupRetentionDays",
            "daily_automatic_backup_start_time": "dailyAutomaticBackupStartTime",
            "disk_iops_configuration": "diskIopsConfiguration",
            "endpoint_ip_address_range": "endpointIpAddressRange",
            "fsx_admin_password": "fsxAdminPassword",
            "preferred_subnet_id": "preferredSubnetId",
            "route_table_ids": "routeTableIds",
            "throughput_capacity": "throughputCapacity",
            "weekly_maintenance_start_time": "weeklyMaintenanceStartTime",
        },
    )
    class OntapConfigurationProperty:
        def __init__(
            self,
            *,
            deployment_type: builtins.str,
            automatic_backup_retention_days: typing.Optional[jsii.Number] = None,
            daily_automatic_backup_start_time: typing.Optional[builtins.str] = None,
            disk_iops_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.DiskIopsConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            endpoint_ip_address_range: typing.Optional[builtins.str] = None,
            fsx_admin_password: typing.Optional[builtins.str] = None,
            preferred_subnet_id: typing.Optional[builtins.str] = None,
            route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            throughput_capacity: typing.Optional[jsii.Number] = None,
            weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for this Amazon FSx for NetApp ONTAP file system.

            :param deployment_type: Specifies the FSx for ONTAP file system deployment type to use in creating the file system. - ``MULTI_AZ_1`` - (Default) A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. - ``SINGLE_AZ_1`` - A file system configured for Single-AZ redundancy. For information about the use cases for Multi-AZ and Single-AZ deployments, refer to `Choosing a file system deployment type <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html>`_ .
            :param automatic_backup_retention_days: The number of days to retain automatic backups. Setting this property to ``0`` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is ``0`` .
            :param daily_automatic_backup_start_time: A recurring daily time, in the format ``HH:MM`` . ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``05:00`` specifies 5 AM daily.
            :param disk_iops_configuration: The SSD IOPS configuration for the FSx for ONTAP file system.
            :param endpoint_ip_address_range: (Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default, Amazon FSx selects an unused IP address range for you from the 198.19.* range. .. epigraph:: The Endpoint IP address range you select for your file system must exist outside the VPC's CIDR range and must be at least /30 or larger.
            :param fsx_admin_password: The ONTAP administrative password for the ``fsxadmin`` user with which you administer your file system using the NetApp ONTAP CLI and REST API.
            :param preferred_subnet_id: Required when ``DeploymentType`` is set to ``MULTI_AZ_1`` . This specifies the subnet in which you want the preferred file server to be located.
            :param route_table_ids: (Multi-AZ only) Specifies the virtual private cloud (VPC) route tables in which your file system's endpoints will be created. You should specify all VPC route tables associated with the subnets in which your clients are located. By default, Amazon FSx selects your VPC's default route table.
            :param throughput_capacity: Sets the throughput capacity for the file system that you're creating. Valid values are 128, 256, 512, 1024, and 2048 MBps.
            :param weekly_maintenance_start_time: A recurring weekly time, in the format ``D:HH:MM`` . ``D`` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see `the ISO-8601 spec as described on Wikipedia <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_week_date>`_ . ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``1:05:00`` specifies maintenance at 5 AM Monday.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                ontap_configuration_property = fsx.CfnFileSystem.OntapConfigurationProperty(
                    deployment_type="deploymentType",
                
                    # the properties below are optional
                    automatic_backup_retention_days=123,
                    daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                    disk_iops_configuration=fsx.CfnFileSystem.DiskIopsConfigurationProperty(
                        iops=123,
                        mode="mode"
                    ),
                    endpoint_ip_address_range="endpointIpAddressRange",
                    fsx_admin_password="fsxAdminPassword",
                    preferred_subnet_id="preferredSubnetId",
                    route_table_ids=["routeTableIds"],
                    throughput_capacity=123,
                    weekly_maintenance_start_time="weeklyMaintenanceStartTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.OntapConfigurationProperty.__init__)
                check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
                check_type(argname="argument automatic_backup_retention_days", value=automatic_backup_retention_days, expected_type=type_hints["automatic_backup_retention_days"])
                check_type(argname="argument daily_automatic_backup_start_time", value=daily_automatic_backup_start_time, expected_type=type_hints["daily_automatic_backup_start_time"])
                check_type(argname="argument disk_iops_configuration", value=disk_iops_configuration, expected_type=type_hints["disk_iops_configuration"])
                check_type(argname="argument endpoint_ip_address_range", value=endpoint_ip_address_range, expected_type=type_hints["endpoint_ip_address_range"])
                check_type(argname="argument fsx_admin_password", value=fsx_admin_password, expected_type=type_hints["fsx_admin_password"])
                check_type(argname="argument preferred_subnet_id", value=preferred_subnet_id, expected_type=type_hints["preferred_subnet_id"])
                check_type(argname="argument route_table_ids", value=route_table_ids, expected_type=type_hints["route_table_ids"])
                check_type(argname="argument throughput_capacity", value=throughput_capacity, expected_type=type_hints["throughput_capacity"])
                check_type(argname="argument weekly_maintenance_start_time", value=weekly_maintenance_start_time, expected_type=type_hints["weekly_maintenance_start_time"])
            self._values: typing.Dict[str, typing.Any] = {
                "deployment_type": deployment_type,
            }
            if automatic_backup_retention_days is not None:
                self._values["automatic_backup_retention_days"] = automatic_backup_retention_days
            if daily_automatic_backup_start_time is not None:
                self._values["daily_automatic_backup_start_time"] = daily_automatic_backup_start_time
            if disk_iops_configuration is not None:
                self._values["disk_iops_configuration"] = disk_iops_configuration
            if endpoint_ip_address_range is not None:
                self._values["endpoint_ip_address_range"] = endpoint_ip_address_range
            if fsx_admin_password is not None:
                self._values["fsx_admin_password"] = fsx_admin_password
            if preferred_subnet_id is not None:
                self._values["preferred_subnet_id"] = preferred_subnet_id
            if route_table_ids is not None:
                self._values["route_table_ids"] = route_table_ids
            if throughput_capacity is not None:
                self._values["throughput_capacity"] = throughput_capacity
            if weekly_maintenance_start_time is not None:
                self._values["weekly_maintenance_start_time"] = weekly_maintenance_start_time

        @builtins.property
        def deployment_type(self) -> builtins.str:
            '''Specifies the FSx for ONTAP file system deployment type to use in creating the file system.

            - ``MULTI_AZ_1`` - (Default) A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability.
            - ``SINGLE_AZ_1`` - A file system configured for Single-AZ redundancy.

            For information about the use cases for Multi-AZ and Single-AZ deployments, refer to `Choosing a file system deployment type <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-deploymenttype
            '''
            result = self._values.get("deployment_type")
            assert result is not None, "Required property 'deployment_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def automatic_backup_retention_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days to retain automatic backups.

            Setting this property to ``0`` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is ``0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-automaticbackupretentiondays
            '''
            result = self._values.get("automatic_backup_retention_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def daily_automatic_backup_start_time(self) -> typing.Optional[builtins.str]:
            '''A recurring daily time, in the format ``HH:MM`` .

            ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``05:00`` specifies 5 AM daily.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-dailyautomaticbackupstarttime
            '''
            result = self._values.get("daily_automatic_backup_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def disk_iops_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnFileSystem.DiskIopsConfigurationProperty", _IResolvable_da3f097b]]:
            '''The SSD IOPS configuration for the FSx for ONTAP file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-diskiopsconfiguration
            '''
            result = self._values.get("disk_iops_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnFileSystem.DiskIopsConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def endpoint_ip_address_range(self) -> typing.Optional[builtins.str]:
            '''(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created.

            By default, Amazon FSx selects an unused IP address range for you from the 198.19.* range.
            .. epigraph::

               The Endpoint IP address range you select for your file system must exist outside the VPC's CIDR range and must be at least /30 or larger.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-endpointipaddressrange
            '''
            result = self._values.get("endpoint_ip_address_range")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fsx_admin_password(self) -> typing.Optional[builtins.str]:
            '''The ONTAP administrative password for the ``fsxadmin`` user with which you administer your file system using the NetApp ONTAP CLI and REST API.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-fsxadminpassword
            '''
            result = self._values.get("fsx_admin_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preferred_subnet_id(self) -> typing.Optional[builtins.str]:
            '''Required when ``DeploymentType`` is set to ``MULTI_AZ_1`` .

            This specifies the subnet in which you want the preferred file server to be located.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-preferredsubnetid
            '''
            result = self._values.get("preferred_subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def route_table_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''(Multi-AZ only) Specifies the virtual private cloud (VPC) route tables in which your file system's endpoints will be created.

            You should specify all VPC route tables associated with the subnets in which your clients are located. By default, Amazon FSx selects your VPC's default route table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-routetableids
            '''
            result = self._values.get("route_table_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def throughput_capacity(self) -> typing.Optional[jsii.Number]:
            '''Sets the throughput capacity for the file system that you're creating.

            Valid values are 128, 256, 512, 1024, and 2048 MBps.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-throughputcapacity
            '''
            result = self._values.get("throughput_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def weekly_maintenance_start_time(self) -> typing.Optional[builtins.str]:
            '''A recurring weekly time, in the format ``D:HH:MM`` .

            ``D`` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see `the ISO-8601 spec as described on Wikipedia <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_week_date>`_ .

            ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour.

            For example, ``1:05:00`` specifies maintenance at 5 AM Monday.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-weeklymaintenancestarttime
            '''
            result = self._values.get("weekly_maintenance_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OntapConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.OpenZFSConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deployment_type": "deploymentType",
            "automatic_backup_retention_days": "automaticBackupRetentionDays",
            "copy_tags_to_backups": "copyTagsToBackups",
            "copy_tags_to_volumes": "copyTagsToVolumes",
            "daily_automatic_backup_start_time": "dailyAutomaticBackupStartTime",
            "disk_iops_configuration": "diskIopsConfiguration",
            "options": "options",
            "root_volume_configuration": "rootVolumeConfiguration",
            "throughput_capacity": "throughputCapacity",
            "weekly_maintenance_start_time": "weeklyMaintenanceStartTime",
        },
    )
    class OpenZFSConfigurationProperty:
        def __init__(
            self,
            *,
            deployment_type: builtins.str,
            automatic_backup_retention_days: typing.Optional[jsii.Number] = None,
            copy_tags_to_backups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            copy_tags_to_volumes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            daily_automatic_backup_start_time: typing.Optional[builtins.str] = None,
            disk_iops_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.DiskIopsConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            options: typing.Optional[typing.Sequence[builtins.str]] = None,
            root_volume_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.RootVolumeConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            throughput_capacity: typing.Optional[jsii.Number] = None,
            weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The OpenZFS configuration for the file system that's being created.

            :param deployment_type: Specifies the file system deployment type. Amazon FSx for OpenZFS supports ``SINGLE_AZ_1`` . ``SINGLE_AZ_1`` deployment type is configured for redundancy within a single Availability Zone.
            :param automatic_backup_retention_days: The number of days to retain automatic backups. Setting this property to ``0`` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is ``0`` .
            :param copy_tags_to_backups: A Boolean value indicating whether tags for the file system should be copied to backups. This value defaults to ``false`` . If it's set to ``true`` , all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is ``true`` , and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.
            :param copy_tags_to_volumes: A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to ``false`` . If it's set to ``true`` , all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is ``true`` , and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.
            :param daily_automatic_backup_start_time: A recurring daily time, in the format ``HH:MM`` . ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``05:00`` specifies 5 AM daily.
            :param disk_iops_configuration: The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS file system. The default is 3 IOPS per GB of storage capacity, but you can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how the amount was provisioned (by the customer or by the system).
            :param options: To delete a file system if there are child volumes present below the root volume, use the string ``DELETE_CHILD_VOLUMES_AND_SNAPSHOTS`` . If your file system has child volumes and you don't use this option, the delete request will fail.
            :param root_volume_configuration: The configuration Amazon FSx uses when creating the root value of the Amazon FSx for OpenZFS file system. All volumes are children of the root volume.
            :param throughput_capacity: Specifies the throughput of an Amazon FSx for OpenZFS file system, measured in megabytes per second (MB/s). Valid values are 64, 128, 256, 512, 1024, 2048, 3072, or 4096 MB/s. You pay for additional throughput capacity that you provision.
            :param weekly_maintenance_start_time: A recurring weekly time, in the format ``D:HH:MM`` . ``D`` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see `the ISO-8601 spec as described on Wikipedia <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_week_date>`_ . ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``1:05:00`` specifies maintenance at 5 AM Monday.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                open_zFSConfiguration_property = fsx.CfnFileSystem.OpenZFSConfigurationProperty(
                    deployment_type="deploymentType",
                
                    # the properties below are optional
                    automatic_backup_retention_days=123,
                    copy_tags_to_backups=False,
                    copy_tags_to_volumes=False,
                    daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                    disk_iops_configuration=fsx.CfnFileSystem.DiskIopsConfigurationProperty(
                        iops=123,
                        mode="mode"
                    ),
                    options=["options"],
                    root_volume_configuration=fsx.CfnFileSystem.RootVolumeConfigurationProperty(
                        copy_tags_to_snapshots=False,
                        data_compression_type="dataCompressionType",
                        nfs_exports=[fsx.CfnFileSystem.NfsExportsProperty(
                            client_configurations=[fsx.CfnFileSystem.ClientConfigurationsProperty(
                                clients="clients",
                                options=["options"]
                            )]
                        )],
                        read_only=False,
                        record_size_ki_b=123,
                        user_and_group_quotas=[fsx.CfnFileSystem.UserAndGroupQuotasProperty(
                            id=123,
                            storage_capacity_quota_gi_b=123,
                            type="type"
                        )]
                    ),
                    throughput_capacity=123,
                    weekly_maintenance_start_time="weeklyMaintenanceStartTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.OpenZFSConfigurationProperty.__init__)
                check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
                check_type(argname="argument automatic_backup_retention_days", value=automatic_backup_retention_days, expected_type=type_hints["automatic_backup_retention_days"])
                check_type(argname="argument copy_tags_to_backups", value=copy_tags_to_backups, expected_type=type_hints["copy_tags_to_backups"])
                check_type(argname="argument copy_tags_to_volumes", value=copy_tags_to_volumes, expected_type=type_hints["copy_tags_to_volumes"])
                check_type(argname="argument daily_automatic_backup_start_time", value=daily_automatic_backup_start_time, expected_type=type_hints["daily_automatic_backup_start_time"])
                check_type(argname="argument disk_iops_configuration", value=disk_iops_configuration, expected_type=type_hints["disk_iops_configuration"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
                check_type(argname="argument root_volume_configuration", value=root_volume_configuration, expected_type=type_hints["root_volume_configuration"])
                check_type(argname="argument throughput_capacity", value=throughput_capacity, expected_type=type_hints["throughput_capacity"])
                check_type(argname="argument weekly_maintenance_start_time", value=weekly_maintenance_start_time, expected_type=type_hints["weekly_maintenance_start_time"])
            self._values: typing.Dict[str, typing.Any] = {
                "deployment_type": deployment_type,
            }
            if automatic_backup_retention_days is not None:
                self._values["automatic_backup_retention_days"] = automatic_backup_retention_days
            if copy_tags_to_backups is not None:
                self._values["copy_tags_to_backups"] = copy_tags_to_backups
            if copy_tags_to_volumes is not None:
                self._values["copy_tags_to_volumes"] = copy_tags_to_volumes
            if daily_automatic_backup_start_time is not None:
                self._values["daily_automatic_backup_start_time"] = daily_automatic_backup_start_time
            if disk_iops_configuration is not None:
                self._values["disk_iops_configuration"] = disk_iops_configuration
            if options is not None:
                self._values["options"] = options
            if root_volume_configuration is not None:
                self._values["root_volume_configuration"] = root_volume_configuration
            if throughput_capacity is not None:
                self._values["throughput_capacity"] = throughput_capacity
            if weekly_maintenance_start_time is not None:
                self._values["weekly_maintenance_start_time"] = weekly_maintenance_start_time

        @builtins.property
        def deployment_type(self) -> builtins.str:
            '''Specifies the file system deployment type.

            Amazon FSx for OpenZFS supports ``SINGLE_AZ_1`` . ``SINGLE_AZ_1`` deployment type is configured for redundancy within a single Availability Zone.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-deploymenttype
            '''
            result = self._values.get("deployment_type")
            assert result is not None, "Required property 'deployment_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def automatic_backup_retention_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days to retain automatic backups.

            Setting this property to ``0`` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is ``0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-automaticbackupretentiondays
            '''
            result = self._values.get("automatic_backup_retention_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def copy_tags_to_backups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether tags for the file system should be copied to backups.

            This value defaults to ``false`` . If it's set to ``true`` , all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is ``true`` , and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-copytagstobackups
            '''
            result = self._values.get("copy_tags_to_backups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def copy_tags_to_volumes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether tags for the volume should be copied to snapshots.

            This value defaults to ``false`` . If it's set to ``true`` , all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is ``true`` , and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-copytagstovolumes
            '''
            result = self._values.get("copy_tags_to_volumes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def daily_automatic_backup_start_time(self) -> typing.Optional[builtins.str]:
            '''A recurring daily time, in the format ``HH:MM`` .

            ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``05:00`` specifies 5 AM daily.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-dailyautomaticbackupstarttime
            '''
            result = self._values.get("daily_automatic_backup_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def disk_iops_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnFileSystem.DiskIopsConfigurationProperty", _IResolvable_da3f097b]]:
            '''The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS file system.

            The default is 3 IOPS per GB of storage capacity, but you can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how the amount was provisioned (by the customer or by the system).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration
            '''
            result = self._values.get("disk_iops_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnFileSystem.DiskIopsConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def options(self) -> typing.Optional[typing.List[builtins.str]]:
            '''To delete a file system if there are child volumes present below the root volume, use the string ``DELETE_CHILD_VOLUMES_AND_SNAPSHOTS`` .

            If your file system has child volumes and you don't use this option, the delete request will fail.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def root_volume_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnFileSystem.RootVolumeConfigurationProperty", _IResolvable_da3f097b]]:
            '''The configuration Amazon FSx uses when creating the root value of the Amazon FSx for OpenZFS file system.

            All volumes are children of the root volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration
            '''
            result = self._values.get("root_volume_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnFileSystem.RootVolumeConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def throughput_capacity(self) -> typing.Optional[jsii.Number]:
            '''Specifies the throughput of an Amazon FSx for OpenZFS file system, measured in megabytes per second (MB/s).

            Valid values are 64, 128, 256, 512, 1024, 2048, 3072, or 4096 MB/s. You pay for additional throughput capacity that you provision.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-throughputcapacity
            '''
            result = self._values.get("throughput_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def weekly_maintenance_start_time(self) -> typing.Optional[builtins.str]:
            '''A recurring weekly time, in the format ``D:HH:MM`` .

            ``D`` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see `the ISO-8601 spec as described on Wikipedia <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_week_date>`_ .

            ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour.

            For example, ``1:05:00`` specifies maintenance at 5 AM Monday.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-weeklymaintenancestarttime
            '''
            result = self._values.get("weekly_maintenance_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenZFSConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.RootVolumeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "copy_tags_to_snapshots": "copyTagsToSnapshots",
            "data_compression_type": "dataCompressionType",
            "nfs_exports": "nfsExports",
            "read_only": "readOnly",
            "record_size_kib": "recordSizeKiB",
            "user_and_group_quotas": "userAndGroupQuotas",
        },
    )
    class RootVolumeConfigurationProperty:
        def __init__(
            self,
            *,
            copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            data_compression_type: typing.Optional[builtins.str] = None,
            nfs_exports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnFileSystem.NfsExportsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            record_size_kib: typing.Optional[jsii.Number] = None,
            user_and_group_quotas: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnFileSystem.UserAndGroupQuotasProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The configuration of an Amazon FSx for OpenZFS root volume.

            :param copy_tags_to_snapshots: A Boolean value indicating whether tags for the volume should be copied to snapshots of the volume. This value defaults to ``false`` . If it's set to ``true`` , all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is ``true`` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.
            :param data_compression_type: Specifies the method used to compress the data on the volume. The compression type is ``NONE`` by default. - ``NONE`` - Doesn't compress the data on the volume. ``NONE`` is the default. - ``ZSTD`` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization. - ``LZ4`` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.
            :param nfs_exports: The configuration object for mounting a file system.
            :param read_only: A Boolean value indicating whether the volume is read-only. Setting this value to ``true`` can be useful after you have completed changes to a volume and no longer want changes to occur.
            :param record_size_kib: Specifies the record size of an OpenZFS root volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. Database workflows can benefit from a smaller record size, while streaming workflows can benefit from a larger record size. For additional guidance on setting a custom record size, see `Tips for maximizing performance <https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs>`_ in the *Amazon FSx for OpenZFS User Guide* .
            :param user_and_group_quotas: An object specifying how much storage users or groups can use on the volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                root_volume_configuration_property = fsx.CfnFileSystem.RootVolumeConfigurationProperty(
                    copy_tags_to_snapshots=False,
                    data_compression_type="dataCompressionType",
                    nfs_exports=[fsx.CfnFileSystem.NfsExportsProperty(
                        client_configurations=[fsx.CfnFileSystem.ClientConfigurationsProperty(
                            clients="clients",
                            options=["options"]
                        )]
                    )],
                    read_only=False,
                    record_size_ki_b=123,
                    user_and_group_quotas=[fsx.CfnFileSystem.UserAndGroupQuotasProperty(
                        id=123,
                        storage_capacity_quota_gi_b=123,
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.RootVolumeConfigurationProperty.__init__)
                check_type(argname="argument copy_tags_to_snapshots", value=copy_tags_to_snapshots, expected_type=type_hints["copy_tags_to_snapshots"])
                check_type(argname="argument data_compression_type", value=data_compression_type, expected_type=type_hints["data_compression_type"])
                check_type(argname="argument nfs_exports", value=nfs_exports, expected_type=type_hints["nfs_exports"])
                check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
                check_type(argname="argument record_size_kib", value=record_size_kib, expected_type=type_hints["record_size_kib"])
                check_type(argname="argument user_and_group_quotas", value=user_and_group_quotas, expected_type=type_hints["user_and_group_quotas"])
            self._values: typing.Dict[str, typing.Any] = {}
            if copy_tags_to_snapshots is not None:
                self._values["copy_tags_to_snapshots"] = copy_tags_to_snapshots
            if data_compression_type is not None:
                self._values["data_compression_type"] = data_compression_type
            if nfs_exports is not None:
                self._values["nfs_exports"] = nfs_exports
            if read_only is not None:
                self._values["read_only"] = read_only
            if record_size_kib is not None:
                self._values["record_size_kib"] = record_size_kib
            if user_and_group_quotas is not None:
                self._values["user_and_group_quotas"] = user_and_group_quotas

        @builtins.property
        def copy_tags_to_snapshots(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether tags for the volume should be copied to snapshots of the volume.

            This value defaults to ``false`` . If it's set to ``true`` , all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is ``true`` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-copytagstosnapshots
            '''
            result = self._values.get("copy_tags_to_snapshots")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def data_compression_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the method used to compress the data on the volume. The compression type is ``NONE`` by default.

            - ``NONE`` - Doesn't compress the data on the volume. ``NONE`` is the default.
            - ``ZSTD`` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
            - ``LZ4`` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-datacompressiontype
            '''
            result = self._values.get("data_compression_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def nfs_exports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFileSystem.NfsExportsProperty", _IResolvable_da3f097b]]]]:
            '''The configuration object for mounting a file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports
            '''
            result = self._values.get("nfs_exports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFileSystem.NfsExportsProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def read_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether the volume is read-only.

            Setting this value to ``true`` can be useful after you have completed changes to a volume and no longer want changes to occur.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-readonly
            '''
            result = self._values.get("read_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def record_size_kib(self) -> typing.Optional[jsii.Number]:
            '''Specifies the record size of an OpenZFS root volume, in kibibytes (KiB).

            Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. Database workflows can benefit from a smaller record size, while streaming workflows can benefit from a larger record size. For additional guidance on setting a custom record size, see `Tips for maximizing performance <https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs>`_ in the *Amazon FSx for OpenZFS User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-recordsizekib
            '''
            result = self._values.get("record_size_kib")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def user_and_group_quotas(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFileSystem.UserAndGroupQuotasProperty", _IResolvable_da3f097b]]]]:
            '''An object specifying how much storage users or groups can use on the volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas
            '''
            result = self._values.get("user_and_group_quotas")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnFileSystem.UserAndGroupQuotasProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RootVolumeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_ips": "dnsIps",
            "domain_name": "domainName",
            "file_system_administrators_group": "fileSystemAdministratorsGroup",
            "organizational_unit_distinguished_name": "organizationalUnitDistinguishedName",
            "password": "password",
            "user_name": "userName",
        },
    )
    class SelfManagedActiveDirectoryConfigurationProperty:
        def __init__(
            self,
            *,
            dns_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
            domain_name: typing.Optional[builtins.str] = None,
            file_system_administrators_group: typing.Optional[builtins.str] = None,
            organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
            password: typing.Optional[builtins.str] = None,
            user_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory.

            For more information, see `Using Amazon FSx with your self-managed Microsoft Active Directory <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html>`_ or `Managing SVMs <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html>`_ .

            :param dns_ips: A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.
            :param domain_name: The fully qualified domain name of the self-managed AD directory, such as ``corp.example.com`` .
            :param file_system_administrators_group: (Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don't provide one, your AD domain's Domain Admins group is used.
            :param organizational_unit_distinguished_name: (Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory. Amazon FSx only accepts OU as the direct parent of the file system. An example is ``OU=FSx,DC=yourdomain,DC=corp,DC=com`` . To learn more, see `RFC 2253 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc2253>`_ . If none is provided, the FSx file system is created in the default location of your self-managed AD directory. .. epigraph:: Only Organizational Unit (OU) objects can be the direct parent of the file system that you're creating.
            :param password: The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
            :param user_name: The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in ``OrganizationalUnitDistinguishedName`` , or in the default location of your AD domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                self_managed_active_directory_configuration_property = fsx.CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty(
                    dns_ips=["dnsIps"],
                    domain_name="domainName",
                    file_system_administrators_group="fileSystemAdministratorsGroup",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName",
                    password="password",
                    user_name="userName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty.__init__)
                check_type(argname="argument dns_ips", value=dns_ips, expected_type=type_hints["dns_ips"])
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument file_system_administrators_group", value=file_system_administrators_group, expected_type=type_hints["file_system_administrators_group"])
                check_type(argname="argument organizational_unit_distinguished_name", value=organizational_unit_distinguished_name, expected_type=type_hints["organizational_unit_distinguished_name"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if dns_ips is not None:
                self._values["dns_ips"] = dns_ips
            if domain_name is not None:
                self._values["domain_name"] = domain_name
            if file_system_administrators_group is not None:
                self._values["file_system_administrators_group"] = file_system_administrators_group
            if organizational_unit_distinguished_name is not None:
                self._values["organizational_unit_distinguished_name"] = organizational_unit_distinguished_name
            if password is not None:
                self._values["password"] = password
            if user_name is not None:
                self._values["user_name"] = user_name

        @builtins.property
        def dns_ips(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-dnsips
            '''
            result = self._values.get("dns_ips")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def domain_name(self) -> typing.Optional[builtins.str]:
            '''The fully qualified domain name of the self-managed AD directory, such as ``corp.example.com`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-domainname
            '''
            result = self._values.get("domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_system_administrators_group(self) -> typing.Optional[builtins.str]:
            '''(Optional) The name of the domain group whose members are granted administrative privileges for the file system.

            Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don't provide one, your AD domain's Domain Admins group is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup
            '''
            result = self._values.get("file_system_administrators_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit_distinguished_name(
            self,
        ) -> typing.Optional[builtins.str]:
            '''(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory.

            Amazon FSx only accepts OU as the direct parent of the file system. An example is ``OU=FSx,DC=yourdomain,DC=corp,DC=com`` . To learn more, see `RFC 2253 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc2253>`_ . If none is provided, the FSx file system is created in the default location of your self-managed AD directory.
            .. epigraph::

               Only Organizational Unit (OU) objects can be the direct parent of the file system that you're creating.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname
            '''
            result = self._values.get("organizational_unit_distinguished_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_name(self) -> typing.Optional[builtins.str]:
            '''The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.

            This account must have the permission to join computers to the domain in the organizational unit provided in ``OrganizationalUnitDistinguishedName`` , or in the default location of your AD domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-username
            '''
            result = self._values.get("user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelfManagedActiveDirectoryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.UserAndGroupQuotasProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "storage_capacity_quota_gib": "storageCapacityQuotaGiB",
            "type": "type",
        },
    )
    class UserAndGroupQuotasProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[jsii.Number] = None,
            storage_capacity_quota_gib: typing.Optional[jsii.Number] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for how much storage a user or group can use on the volume.

            :param id: The ID of the user or group.
            :param storage_capacity_quota_gib: The amount of storage that the user or group can use in gibibytes (GiB).
            :param type: A value that specifies whether the quota applies to a user or group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                user_and_group_quotas_property = fsx.CfnFileSystem.UserAndGroupQuotasProperty(
                    id=123,
                    storage_capacity_quota_gi_b=123,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.UserAndGroupQuotasProperty.__init__)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument storage_capacity_quota_gib", value=storage_capacity_quota_gib, expected_type=type_hints["storage_capacity_quota_gib"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if storage_capacity_quota_gib is not None:
                self._values["storage_capacity_quota_gib"] = storage_capacity_quota_gib
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def id(self) -> typing.Optional[jsii.Number]:
            '''The ID of the user or group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def storage_capacity_quota_gib(self) -> typing.Optional[jsii.Number]:
            '''The amount of storage that the user or group can use in gibibytes (GiB).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas-storagecapacityquotagib
            '''
            result = self._values.get("storage_capacity_quota_gib")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''A value that specifies whether the quota applies to a user or group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserAndGroupQuotasProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystem.WindowsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "throughput_capacity": "throughputCapacity",
            "active_directory_id": "activeDirectoryId",
            "aliases": "aliases",
            "audit_log_configuration": "auditLogConfiguration",
            "automatic_backup_retention_days": "automaticBackupRetentionDays",
            "copy_tags_to_backups": "copyTagsToBackups",
            "daily_automatic_backup_start_time": "dailyAutomaticBackupStartTime",
            "deployment_type": "deploymentType",
            "preferred_subnet_id": "preferredSubnetId",
            "self_managed_active_directory_configuration": "selfManagedActiveDirectoryConfiguration",
            "weekly_maintenance_start_time": "weeklyMaintenanceStartTime",
        },
    )
    class WindowsConfigurationProperty:
        def __init__(
            self,
            *,
            throughput_capacity: jsii.Number,
            active_directory_id: typing.Optional[builtins.str] = None,
            aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
            audit_log_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.AuditLogConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            automatic_backup_retention_days: typing.Optional[jsii.Number] = None,
            copy_tags_to_backups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            daily_automatic_backup_start_time: typing.Optional[builtins.str] = None,
            deployment_type: typing.Optional[builtins.str] = None,
            preferred_subnet_id: typing.Optional[builtins.str] = None,
            self_managed_active_directory_configuration: typing.Optional[typing.Union[typing.Union["CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Microsoft Windows configuration for the file system that's being created.

            :param throughput_capacity: Sets the throughput capacity of an Amazon FSx file system, measured in megabytes per second (MB/s), in 2 to the *n* th increments, between 2^3 (8) and 2^11 (2048).
            :param active_directory_id: The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file system should join when it's created. Required if you are joining the file system to an existing AWS Managed Microsoft AD.
            :param aliases: An array of one or more DNS alias names that you want to associate with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. For more information, see `Working with DNS Aliases <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html>`_ and `Walkthrough 5: Using DNS aliases to access your file system <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthrough05-file-system-custom-CNAME.html>`_ , including additional steps you must take to be able to access your file system using a DNS alias. An alias name has to meet the following requirements: - Formatted as a fully-qualified domain name (FQDN), ``hostname.domain`` , for example, ``accounting.example.com`` . - Can contain alphanumeric characters, the underscore (_), and the hyphen (-). - Cannot start or end with a hyphen. - Can start with a numeric. For DNS alias names, Amazon FSx stores alphabetical characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.
            :param audit_log_configuration: The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.
            :param automatic_backup_retention_days: The number of days to retain automatic backups. Setting this property to ``0`` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is ``0`` .
            :param copy_tags_to_backups: A boolean flag indicating whether tags for the file system should be copied to backups. This value defaults to false. If it's set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.
            :param daily_automatic_backup_start_time: A recurring daily time, in the format ``HH:MM`` . ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``05:00`` specifies 5 AM daily.
            :param deployment_type: Specifies the file system deployment type, valid values are the following:. - ``MULTI_AZ_1`` - Deploys a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. You can only deploy a Multi-AZ file system in AWS Regions that have a minimum of three Availability Zones. Also supports HDD storage type - ``SINGLE_AZ_1`` - (Default) Choose to deploy a file system that is configured for single AZ redundancy. - ``SINGLE_AZ_2`` - The latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports HDD storage type. For more information, see `Availability and Durability: Single-AZ and Multi-AZ File Systems <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html>`_ .
            :param preferred_subnet_id: Required when ``DeploymentType`` is set to ``MULTI_AZ_1`` . This specifies the subnet in which you want the preferred file server to be located. For in- AWS applications, we recommend that you launch your clients in the same availability zone as your preferred file server to reduce cross-availability zone data transfer costs and minimize latency.
            :param self_managed_active_directory_configuration: The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory. For more information, see `Using Amazon FSx with your self-managed Microsoft Active Directory <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html>`_ or `Managing SVMs <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html>`_ .
            :param weekly_maintenance_start_time: A recurring weekly time, in the format ``D:HH:MM`` . ``D`` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see `the ISO-8601 spec as described on Wikipedia <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_week_date>`_ . ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``1:05:00`` specifies maintenance at 5 AM Monday.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                windows_configuration_property = fsx.CfnFileSystem.WindowsConfigurationProperty(
                    throughput_capacity=123,
                
                    # the properties below are optional
                    active_directory_id="activeDirectoryId",
                    aliases=["aliases"],
                    audit_log_configuration=fsx.CfnFileSystem.AuditLogConfigurationProperty(
                        file_access_audit_log_level="fileAccessAuditLogLevel",
                        file_share_access_audit_log_level="fileShareAccessAuditLogLevel",
                
                        # the properties below are optional
                        audit_log_destination="auditLogDestination"
                    ),
                    automatic_backup_retention_days=123,
                    copy_tags_to_backups=False,
                    daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                    deployment_type="deploymentType",
                    preferred_subnet_id="preferredSubnetId",
                    self_managed_active_directory_configuration=fsx.CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty(
                        dns_ips=["dnsIps"],
                        domain_name="domainName",
                        file_system_administrators_group="fileSystemAdministratorsGroup",
                        organizational_unit_distinguished_name="organizationalUnitDistinguishedName",
                        password="password",
                        user_name="userName"
                    ),
                    weekly_maintenance_start_time="weeklyMaintenanceStartTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFileSystem.WindowsConfigurationProperty.__init__)
                check_type(argname="argument throughput_capacity", value=throughput_capacity, expected_type=type_hints["throughput_capacity"])
                check_type(argname="argument active_directory_id", value=active_directory_id, expected_type=type_hints["active_directory_id"])
                check_type(argname="argument aliases", value=aliases, expected_type=type_hints["aliases"])
                check_type(argname="argument audit_log_configuration", value=audit_log_configuration, expected_type=type_hints["audit_log_configuration"])
                check_type(argname="argument automatic_backup_retention_days", value=automatic_backup_retention_days, expected_type=type_hints["automatic_backup_retention_days"])
                check_type(argname="argument copy_tags_to_backups", value=copy_tags_to_backups, expected_type=type_hints["copy_tags_to_backups"])
                check_type(argname="argument daily_automatic_backup_start_time", value=daily_automatic_backup_start_time, expected_type=type_hints["daily_automatic_backup_start_time"])
                check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
                check_type(argname="argument preferred_subnet_id", value=preferred_subnet_id, expected_type=type_hints["preferred_subnet_id"])
                check_type(argname="argument self_managed_active_directory_configuration", value=self_managed_active_directory_configuration, expected_type=type_hints["self_managed_active_directory_configuration"])
                check_type(argname="argument weekly_maintenance_start_time", value=weekly_maintenance_start_time, expected_type=type_hints["weekly_maintenance_start_time"])
            self._values: typing.Dict[str, typing.Any] = {
                "throughput_capacity": throughput_capacity,
            }
            if active_directory_id is not None:
                self._values["active_directory_id"] = active_directory_id
            if aliases is not None:
                self._values["aliases"] = aliases
            if audit_log_configuration is not None:
                self._values["audit_log_configuration"] = audit_log_configuration
            if automatic_backup_retention_days is not None:
                self._values["automatic_backup_retention_days"] = automatic_backup_retention_days
            if copy_tags_to_backups is not None:
                self._values["copy_tags_to_backups"] = copy_tags_to_backups
            if daily_automatic_backup_start_time is not None:
                self._values["daily_automatic_backup_start_time"] = daily_automatic_backup_start_time
            if deployment_type is not None:
                self._values["deployment_type"] = deployment_type
            if preferred_subnet_id is not None:
                self._values["preferred_subnet_id"] = preferred_subnet_id
            if self_managed_active_directory_configuration is not None:
                self._values["self_managed_active_directory_configuration"] = self_managed_active_directory_configuration
            if weekly_maintenance_start_time is not None:
                self._values["weekly_maintenance_start_time"] = weekly_maintenance_start_time

        @builtins.property
        def throughput_capacity(self) -> jsii.Number:
            '''Sets the throughput capacity of an Amazon FSx file system, measured in megabytes per second (MB/s), in 2 to the *n* th increments, between 2^3 (8) and 2^11 (2048).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-throughputcapacity
            '''
            result = self._values.get("throughput_capacity")
            assert result is not None, "Required property 'throughput_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def active_directory_id(self) -> typing.Optional[builtins.str]:
            '''The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file system should join when it's created.

            Required if you are joining the file system to an existing AWS Managed Microsoft AD.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-activedirectoryid
            '''
            result = self._values.get("active_directory_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aliases(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of one or more DNS alias names that you want to associate with the Amazon FSx file system.

            Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time.

            For more information, see `Working with DNS Aliases <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html>`_ and `Walkthrough 5: Using DNS aliases to access your file system <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthrough05-file-system-custom-CNAME.html>`_ , including additional steps you must take to be able to access your file system using a DNS alias.

            An alias name has to meet the following requirements:

            - Formatted as a fully-qualified domain name (FQDN), ``hostname.domain`` , for example, ``accounting.example.com`` .
            - Can contain alphanumeric characters, the underscore (_), and the hyphen (-).
            - Cannot start or end with a hyphen.
            - Can start with a numeric.

            For DNS alias names, Amazon FSx stores alphabetical characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-aliases
            '''
            result = self._values.get("aliases")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def audit_log_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnFileSystem.AuditLogConfigurationProperty", _IResolvable_da3f097b]]:
            '''The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-auditlogconfiguration
            '''
            result = self._values.get("audit_log_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnFileSystem.AuditLogConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def automatic_backup_retention_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days to retain automatic backups.

            Setting this property to ``0`` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is ``0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-automaticbackupretentiondays
            '''
            result = self._values.get("automatic_backup_retention_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def copy_tags_to_backups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A boolean flag indicating whether tags for the file system should be copied to backups.

            This value defaults to false. If it's set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-copytagstobackups
            '''
            result = self._values.get("copy_tags_to_backups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def daily_automatic_backup_start_time(self) -> typing.Optional[builtins.str]:
            '''A recurring daily time, in the format ``HH:MM`` .

            ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour. For example, ``05:00`` specifies 5 AM daily.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-dailyautomaticbackupstarttime
            '''
            result = self._values.get("daily_automatic_backup_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def deployment_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the file system deployment type, valid values are the following:.

            - ``MULTI_AZ_1`` - Deploys a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. You can only deploy a Multi-AZ file system in AWS Regions that have a minimum of three Availability Zones. Also supports HDD storage type
            - ``SINGLE_AZ_1`` - (Default) Choose to deploy a file system that is configured for single AZ redundancy.
            - ``SINGLE_AZ_2`` - The latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports HDD storage type.

            For more information, see `Availability and Durability: Single-AZ and Multi-AZ File Systems <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-deploymenttype
            '''
            result = self._values.get("deployment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preferred_subnet_id(self) -> typing.Optional[builtins.str]:
            '''Required when ``DeploymentType`` is set to ``MULTI_AZ_1`` .

            This specifies the subnet in which you want the preferred file server to be located. For in- AWS applications, we recommend that you launch your clients in the same availability zone as your preferred file server to reduce cross-availability zone data transfer costs and minimize latency.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-preferredsubnetid
            '''
            result = self._values.get("preferred_subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def self_managed_active_directory_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty", _IResolvable_da3f097b]]:
            '''The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory.

            For more information, see `Using Amazon FSx with your self-managed Microsoft Active Directory <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html>`_ or `Managing SVMs <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration
            '''
            result = self._values.get("self_managed_active_directory_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def weekly_maintenance_start_time(self) -> typing.Optional[builtins.str]:
            '''A recurring weekly time, in the format ``D:HH:MM`` .

            ``D`` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see `the ISO-8601 spec as described on Wikipedia <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_week_date>`_ .

            ``HH`` is the zero-padded hour of the day (0-23), and ``MM`` is the zero-padded minute of the hour.

            For example, ``1:05:00`` specifies maintenance at 5 AM Monday.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-weeklymaintenancestarttime
            '''
            result = self._values.get("weekly_maintenance_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WindowsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.CfnFileSystemProps",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_type": "fileSystemType",
        "subnet_ids": "subnetIds",
        "backup_id": "backupId",
        "file_system_type_version": "fileSystemTypeVersion",
        "kms_key_id": "kmsKeyId",
        "lustre_configuration": "lustreConfiguration",
        "ontap_configuration": "ontapConfiguration",
        "open_zfs_configuration": "openZfsConfiguration",
        "security_group_ids": "securityGroupIds",
        "storage_capacity": "storageCapacity",
        "storage_type": "storageType",
        "tags": "tags",
        "windows_configuration": "windowsConfiguration",
    },
)
class CfnFileSystemProps:
    def __init__(
        self,
        *,
        file_system_type: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        backup_id: typing.Optional[builtins.str] = None,
        file_system_type_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lustre_configuration: typing.Optional[typing.Union[typing.Union[CfnFileSystem.LustreConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ontap_configuration: typing.Optional[typing.Union[typing.Union[CfnFileSystem.OntapConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        open_zfs_configuration: typing.Optional[typing.Union[typing.Union[CfnFileSystem.OpenZFSConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        windows_configuration: typing.Optional[typing.Union[typing.Union[CfnFileSystem.WindowsConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFileSystem``.

        :param file_system_type: The type of Amazon FSx file system, which can be ``LUSTRE`` , ``WINDOWS`` , ``ONTAP`` , or ``OPENZFS`` .
        :param subnet_ids: Specifies the IDs of the subnets that the file system will be accessible from. For Windows and ONTAP ``MULTI_AZ_1`` deployment types,provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the ``WindowsConfiguration > PreferredSubnetID`` or ``OntapConfiguration > PreferredSubnetID`` properties. For more information about Multi-AZ file system configuration, see `Availability and durability: Single-AZ and Multi-AZ file systems <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html>`_ in the *Amazon FSx for Windows User Guide* and `Availability and durability <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html>`_ in the *Amazon FSx for ONTAP User Guide* . For Windows ``SINGLE_AZ_1`` and ``SINGLE_AZ_2`` and all Lustre deployment types, provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.
        :param backup_id: The ID of the file system backup that you are using to create a file system. For more information, see `CreateFileSystemFromBackup <https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystemFromBackup.html>`_ .
        :param file_system_type_version: (Optional) For FSx for Lustre file systems, sets the Lustre version for the file system that you're creating. Valid values are ``2.10`` and ``2.12`` : - 2.10 is supported by the Scratch and Persistent_1 Lustre deployment types. - 2.12 is supported by all Lustre deployment types. ``2.12`` is required when setting FSx for Lustre ``DeploymentType`` to ``PERSISTENT_2`` . Default value = ``2.10`` , except when ``DeploymentType`` is set to ``PERSISTENT_2`` , then the default is ``2.12`` . .. epigraph:: If you set ``FileSystemTypeVersion`` to ``2.10`` for a ``PERSISTENT_2`` Lustre deployment type, the ``CreateFileSystem`` operation fails.
        :param kms_key_id: The ID of the AWS Key Management Service ( AWS KMS ) key used to encrypt Amazon FSx file system data. Used as follows with Amazon FSx file system types: - Amazon FSx for Lustre ``PERSISTENT_1`` and ``PERSISTENT_2`` deployment types only. ``SCRATCH_1`` and ``SCRATCH_2`` types are encrypted using the Amazon FSx service AWS KMS key for your account. - Amazon FSx for NetApp ONTAP - Amazon FSx for OpenZFS - Amazon FSx for Windows File Server
        :param lustre_configuration: The Lustre configuration for the file system being created. .. epigraph:: The following parameters are not supported for file systems with the Lustre ``Persistent_2`` deployment type. - ``AutoImportPolicy`` - ``ExportPath`` - ``ImportedChunkSize`` - ``ImportPath``
        :param ontap_configuration: The ONTAP configuration properties of the FSx for ONTAP file system that you are creating.
        :param open_zfs_configuration: The Amazon FSx for OpenZFS configuration properties for the file system that you are creating.
        :param security_group_ids: A list of IDs specifying the security groups to apply to all network interfaces created for file system access. This list isn't returned in later requests to describe the file system.
        :param storage_capacity: Sets the storage capacity of the file system that you're creating. ``StorageCapacity`` is required if you are creating a new file system. Do not include ``StorageCapacity`` if you are creating a file system from a backup. *FSx for Lustre file systems* - The amount of storage capacity that you can configure depends on the value that you set for ``StorageType`` and the Lustre ``DeploymentType`` , as follows: - For ``SCRATCH_2`` , ``PERSISTENT_2`` and ``PERSISTENT_1`` deployment types using SSD storage type, the valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB. - For ``PERSISTENT_1`` HDD file systems, valid values are increments of 6000 GiB for 12 MB/s/TiB file systems and increments of 1800 GiB for 40 MB/s/TiB file systems. - For ``SCRATCH_1`` deployment type, valid values are 1200 GiB, 2400 GiB, and increments of 3600 GiB. *FSx for ONTAP file systems* - The amount of storage capacity that you can configure is from 1024 GiB up to 196,608 GiB (192 TiB). *FSx for OpenZFS file systems* - The amount of storage capacity that you can configure is from 64 GiB up to 524,288 GiB (512 TiB). *FSx for Windows File Server file systems* - The amount of storage capacity that you can configure depends on the value that you set for ``StorageType`` as follows: - For SSD storage, valid values are 32 GiB-65,536 GiB (64 TiB). - For HDD storage, valid values are 2000 GiB-65,536 GiB (64 TiB).
        :param storage_type: Sets the storage type for the file system that you're creating. Valid values are ``SSD`` and ``HDD`` . - Set to ``SSD`` to use solid state drive storage. SSD is supported on all Windows, Lustre, ONTAP, and OpenZFS deployment types. - Set to ``HDD`` to use hard disk drive storage. HDD is supported on ``SINGLE_AZ_2`` and ``MULTI_AZ_1`` Windows file system deployment types, and on ``PERSISTENT_1`` Lustre file system deployment types. Default value is ``SSD`` . For more information, see `Storage type options <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/optimize-fsx-costs.html#storage-type-options>`_ in the *FSx for Windows File Server User Guide* and `Multiple storage options <https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html#storage-options>`_ in the *FSx for Lustre User Guide* .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param windows_configuration: The configuration object for the Microsoft Windows file system you are creating. This value is required if ``FileSystemType`` is set to ``WINDOWS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fsx as fsx
            
            cfn_file_system_props = fsx.CfnFileSystemProps(
                file_system_type="fileSystemType",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                backup_id="backupId",
                file_system_type_version="fileSystemTypeVersion",
                kms_key_id="kmsKeyId",
                lustre_configuration=fsx.CfnFileSystem.LustreConfigurationProperty(
                    auto_import_policy="autoImportPolicy",
                    automatic_backup_retention_days=123,
                    copy_tags_to_backups=False,
                    daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                    data_compression_type="dataCompressionType",
                    deployment_type="deploymentType",
                    drive_cache_type="driveCacheType",
                    export_path="exportPath",
                    imported_file_chunk_size=123,
                    import_path="importPath",
                    per_unit_storage_throughput=123,
                    weekly_maintenance_start_time="weeklyMaintenanceStartTime"
                ),
                ontap_configuration=fsx.CfnFileSystem.OntapConfigurationProperty(
                    deployment_type="deploymentType",
            
                    # the properties below are optional
                    automatic_backup_retention_days=123,
                    daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                    disk_iops_configuration=fsx.CfnFileSystem.DiskIopsConfigurationProperty(
                        iops=123,
                        mode="mode"
                    ),
                    endpoint_ip_address_range="endpointIpAddressRange",
                    fsx_admin_password="fsxAdminPassword",
                    preferred_subnet_id="preferredSubnetId",
                    route_table_ids=["routeTableIds"],
                    throughput_capacity=123,
                    weekly_maintenance_start_time="weeklyMaintenanceStartTime"
                ),
                open_zfs_configuration=fsx.CfnFileSystem.OpenZFSConfigurationProperty(
                    deployment_type="deploymentType",
            
                    # the properties below are optional
                    automatic_backup_retention_days=123,
                    copy_tags_to_backups=False,
                    copy_tags_to_volumes=False,
                    daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                    disk_iops_configuration=fsx.CfnFileSystem.DiskIopsConfigurationProperty(
                        iops=123,
                        mode="mode"
                    ),
                    options=["options"],
                    root_volume_configuration=fsx.CfnFileSystem.RootVolumeConfigurationProperty(
                        copy_tags_to_snapshots=False,
                        data_compression_type="dataCompressionType",
                        nfs_exports=[fsx.CfnFileSystem.NfsExportsProperty(
                            client_configurations=[fsx.CfnFileSystem.ClientConfigurationsProperty(
                                clients="clients",
                                options=["options"]
                            )]
                        )],
                        read_only=False,
                        record_size_ki_b=123,
                        user_and_group_quotas=[fsx.CfnFileSystem.UserAndGroupQuotasProperty(
                            id=123,
                            storage_capacity_quota_gi_b=123,
                            type="type"
                        )]
                    ),
                    throughput_capacity=123,
                    weekly_maintenance_start_time="weeklyMaintenanceStartTime"
                ),
                security_group_ids=["securityGroupIds"],
                storage_capacity=123,
                storage_type="storageType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                windows_configuration=fsx.CfnFileSystem.WindowsConfigurationProperty(
                    throughput_capacity=123,
            
                    # the properties below are optional
                    active_directory_id="activeDirectoryId",
                    aliases=["aliases"],
                    audit_log_configuration=fsx.CfnFileSystem.AuditLogConfigurationProperty(
                        file_access_audit_log_level="fileAccessAuditLogLevel",
                        file_share_access_audit_log_level="fileShareAccessAuditLogLevel",
            
                        # the properties below are optional
                        audit_log_destination="auditLogDestination"
                    ),
                    automatic_backup_retention_days=123,
                    copy_tags_to_backups=False,
                    daily_automatic_backup_start_time="dailyAutomaticBackupStartTime",
                    deployment_type="deploymentType",
                    preferred_subnet_id="preferredSubnetId",
                    self_managed_active_directory_configuration=fsx.CfnFileSystem.SelfManagedActiveDirectoryConfigurationProperty(
                        dns_ips=["dnsIps"],
                        domain_name="domainName",
                        file_system_administrators_group="fileSystemAdministratorsGroup",
                        organizational_unit_distinguished_name="organizationalUnitDistinguishedName",
                        password="password",
                        user_name="userName"
                    ),
                    weekly_maintenance_start_time="weeklyMaintenanceStartTime"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFileSystemProps.__init__)
            check_type(argname="argument file_system_type", value=file_system_type, expected_type=type_hints["file_system_type"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument backup_id", value=backup_id, expected_type=type_hints["backup_id"])
            check_type(argname="argument file_system_type_version", value=file_system_type_version, expected_type=type_hints["file_system_type_version"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument lustre_configuration", value=lustre_configuration, expected_type=type_hints["lustre_configuration"])
            check_type(argname="argument ontap_configuration", value=ontap_configuration, expected_type=type_hints["ontap_configuration"])
            check_type(argname="argument open_zfs_configuration", value=open_zfs_configuration, expected_type=type_hints["open_zfs_configuration"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument storage_capacity", value=storage_capacity, expected_type=type_hints["storage_capacity"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument windows_configuration", value=windows_configuration, expected_type=type_hints["windows_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "file_system_type": file_system_type,
            "subnet_ids": subnet_ids,
        }
        if backup_id is not None:
            self._values["backup_id"] = backup_id
        if file_system_type_version is not None:
            self._values["file_system_type_version"] = file_system_type_version
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if lustre_configuration is not None:
            self._values["lustre_configuration"] = lustre_configuration
        if ontap_configuration is not None:
            self._values["ontap_configuration"] = ontap_configuration
        if open_zfs_configuration is not None:
            self._values["open_zfs_configuration"] = open_zfs_configuration
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if storage_capacity is not None:
            self._values["storage_capacity"] = storage_capacity
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if tags is not None:
            self._values["tags"] = tags
        if windows_configuration is not None:
            self._values["windows_configuration"] = windows_configuration

    @builtins.property
    def file_system_type(self) -> builtins.str:
        '''The type of Amazon FSx file system, which can be ``LUSTRE`` , ``WINDOWS`` , ``ONTAP`` , or ``OPENZFS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-filesystemtype
        '''
        result = self._values.get("file_system_type")
        assert result is not None, "Required property 'file_system_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Specifies the IDs of the subnets that the file system will be accessible from.

        For Windows and ONTAP ``MULTI_AZ_1`` deployment types,provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the ``WindowsConfiguration > PreferredSubnetID`` or ``OntapConfiguration > PreferredSubnetID`` properties. For more information about Multi-AZ file system configuration, see `Availability and durability: Single-AZ and Multi-AZ file systems <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html>`_ in the *Amazon FSx for Windows User Guide* and `Availability and durability <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html>`_ in the *Amazon FSx for ONTAP User Guide* .

        For Windows ``SINGLE_AZ_1`` and ``SINGLE_AZ_2`` and all Lustre deployment types, provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the file system backup that you are using to create a file system.

        For more information, see `CreateFileSystemFromBackup <https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystemFromBackup.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-backupid
        '''
        result = self._values.get("backup_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system_type_version(self) -> typing.Optional[builtins.str]:
        '''(Optional) For FSx for Lustre file systems, sets the Lustre version for the file system that you're creating.

        Valid values are ``2.10`` and ``2.12`` :

        - 2.10 is supported by the Scratch and Persistent_1 Lustre deployment types.
        - 2.12 is supported by all Lustre deployment types. ``2.12`` is required when setting FSx for Lustre ``DeploymentType`` to ``PERSISTENT_2`` .

        Default value = ``2.10`` , except when ``DeploymentType`` is set to ``PERSISTENT_2`` , then the default is ``2.12`` .
        .. epigraph::

           If you set ``FileSystemTypeVersion`` to ``2.10`` for a ``PERSISTENT_2`` Lustre deployment type, the ``CreateFileSystem`` operation fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-filesystemtypeversion
        '''
        result = self._values.get("file_system_type_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service ( AWS KMS ) key used to encrypt Amazon FSx file system data.

        Used as follows with Amazon FSx file system types:

        - Amazon FSx for Lustre ``PERSISTENT_1`` and ``PERSISTENT_2`` deployment types only.

        ``SCRATCH_1`` and ``SCRATCH_2`` types are encrypted using the Amazon FSx service AWS KMS key for your account.

        - Amazon FSx for NetApp ONTAP
        - Amazon FSx for OpenZFS
        - Amazon FSx for Windows File Server

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lustre_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnFileSystem.LustreConfigurationProperty, _IResolvable_da3f097b]]:
        '''The Lustre configuration for the file system being created.

        .. epigraph::

           The following parameters are not supported for file systems with the Lustre ``Persistent_2`` deployment type.

           - ``AutoImportPolicy``
           - ``ExportPath``
           - ``ImportedChunkSize``
           - ``ImportPath``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-lustreconfiguration
        '''
        result = self._values.get("lustre_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnFileSystem.LustreConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def ontap_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnFileSystem.OntapConfigurationProperty, _IResolvable_da3f097b]]:
        '''The ONTAP configuration properties of the FSx for ONTAP file system that you are creating.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-ontapconfiguration
        '''
        result = self._values.get("ontap_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnFileSystem.OntapConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def open_zfs_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnFileSystem.OpenZFSConfigurationProperty, _IResolvable_da3f097b]]:
        '''The Amazon FSx for OpenZFS configuration properties for the file system that you are creating.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-openzfsconfiguration
        '''
        result = self._values.get("open_zfs_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnFileSystem.OpenZFSConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IDs specifying the security groups to apply to all network interfaces created for file system access.

        This list isn't returned in later requests to describe the file system.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        '''Sets the storage capacity of the file system that you're creating.

        ``StorageCapacity`` is required if you are creating a new file system. Do not include ``StorageCapacity`` if you are creating a file system from a backup.

        *FSx for Lustre file systems* - The amount of storage capacity that you can configure depends on the value that you set for ``StorageType`` and the Lustre ``DeploymentType`` , as follows:

        - For ``SCRATCH_2`` , ``PERSISTENT_2`` and ``PERSISTENT_1`` deployment types using SSD storage type, the valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.
        - For ``PERSISTENT_1`` HDD file systems, valid values are increments of 6000 GiB for 12 MB/s/TiB file systems and increments of 1800 GiB for 40 MB/s/TiB file systems.
        - For ``SCRATCH_1`` deployment type, valid values are 1200 GiB, 2400 GiB, and increments of 3600 GiB.

        *FSx for ONTAP file systems* - The amount of storage capacity that you can configure is from 1024 GiB up to 196,608 GiB (192 TiB).

        *FSx for OpenZFS file systems* - The amount of storage capacity that you can configure is from 64 GiB up to 524,288 GiB (512 TiB).

        *FSx for Windows File Server file systems* - The amount of storage capacity that you can configure depends on the value that you set for ``StorageType`` as follows:

        - For SSD storage, valid values are 32 GiB-65,536 GiB (64 TiB).
        - For HDD storage, valid values are 2000 GiB-65,536 GiB (64 TiB).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagecapacity
        '''
        result = self._values.get("storage_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''Sets the storage type for the file system that you're creating. Valid values are ``SSD`` and ``HDD`` .

        - Set to ``SSD`` to use solid state drive storage. SSD is supported on all Windows, Lustre, ONTAP, and OpenZFS deployment types.
        - Set to ``HDD`` to use hard disk drive storage. HDD is supported on ``SINGLE_AZ_2`` and ``MULTI_AZ_1`` Windows file system deployment types, and on ``PERSISTENT_1`` Lustre file system deployment types.

        Default value is ``SSD`` . For more information, see `Storage type options <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/optimize-fsx-costs.html#storage-type-options>`_ in the *FSx for Windows File Server User Guide* and `Multiple storage options <https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html#storage-options>`_ in the *FSx for Lustre User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagetype
        '''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def windows_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnFileSystem.WindowsConfigurationProperty, _IResolvable_da3f097b]]:
        '''The configuration object for the Microsoft Windows file system you are creating.

        This value is required if ``FileSystemType`` is set to ``WINDOWS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-windowsconfiguration
        '''
        result = self._values.get("windows_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnFileSystem.WindowsConfigurationProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFileSystemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSnapshot(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fsx.CfnSnapshot",
):
    '''A CloudFormation ``AWS::FSx::Snapshot``.

    A snapshot of an Amazon FSx for OpenZFS volume.

    :cloudformationResource: AWS::FSx::Snapshot
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fsx as fsx
        
        cfn_snapshot = fsx.CfnSnapshot(self, "MyCfnSnapshot",
            name="name",
            volume_id="volumeId",
        
            # the properties below are optional
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
        name: builtins.str,
        volume_id: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::FSx::Snapshot``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the snapshot.
        :param volume_id: The ID of the volume that the snapshot is of.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSnapshot.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSnapshotProps(name=name, volume_id=volume_id, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSnapshot.inspect)
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
            type_hints = typing.get_type_hints(CfnSnapshot._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''Returns the snapshot's Amazon Resource Name (ARN).

        Example: ``arn:aws:fsx:us-east-2:111133334444:snapshot/fsvol-01234567890123456/fsvolsnap-0123456789abcedf5``

        :cloudformationAttribute: ResourceARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the snapshot.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSnapshot, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        '''The ID of the volume that the snapshot is of.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-volumeid
        '''
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSnapshot, "volume_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.CfnSnapshotProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "volume_id": "volumeId", "tags": "tags"},
)
class CfnSnapshotProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        volume_id: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSnapshot``.

        :param name: The name of the snapshot.
        :param volume_id: The ID of the volume that the snapshot is of.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fsx as fsx
            
            cfn_snapshot_props = fsx.CfnSnapshotProps(
                name="name",
                volume_id="volumeId",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSnapshotProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "volume_id": volume_id,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the snapshot.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The ID of the volume that the snapshot is of.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-volumeid
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSnapshotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStorageVirtualMachine(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fsx.CfnStorageVirtualMachine",
):
    '''A CloudFormation ``AWS::FSx::StorageVirtualMachine``.

    Creates a storage virtual machine (SVM) for an Amazon FSx for ONTAP file system.

    :cloudformationResource: AWS::FSx::StorageVirtualMachine
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fsx as fsx
        
        cfn_storage_virtual_machine = fsx.CfnStorageVirtualMachine(self, "MyCfnStorageVirtualMachine",
            file_system_id="fileSystemId",
            name="name",
        
            # the properties below are optional
            active_directory_configuration=fsx.CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty(
                net_bios_name="netBiosName",
                self_managed_active_directory_configuration=fsx.CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty(
                    dns_ips=["dnsIps"],
                    domain_name="domainName",
                    file_system_administrators_group="fileSystemAdministratorsGroup",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName",
                    password="password",
                    user_name="userName"
                )
            ),
            root_volume_security_style="rootVolumeSecurityStyle",
            svm_admin_password="svmAdminPassword",
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
        file_system_id: builtins.str,
        name: builtins.str,
        active_directory_configuration: typing.Optional[typing.Union[typing.Union["CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        root_volume_security_style: typing.Optional[builtins.str] = None,
        svm_admin_password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::FSx::StorageVirtualMachine``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param file_system_id: Specifies the FSx for ONTAP file system on which to create the SVM.
        :param name: The name of the SVM.
        :param active_directory_configuration: Describes the Microsoft Active Directory configuration to which the SVM is joined, if applicable.
        :param root_volume_security_style: The security style of the root volume of the SVM. Specify one of the following values:. - ``UNIX`` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account. - ``NTFS`` if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account. - ``MIXED`` if the file system is managed by both UNIX and Windows administrators and users consist of both NFS and SMB clients.
        :param svm_admin_password: Specifies the password to use when logging on to the SVM using a secure shell (SSH) connection to the SVM's management endpoint. Doing so enables you to manage the SVM using the NetApp ONTAP CLI or REST API. If you do not specify a password, you can still use the file system's ``fsxadmin`` user to manage the SVM. For more information, see `Managing SVMs using the NetApp ONTAP CLI <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html#vsadmin-ontap-cli>`_ in the *FSx for ONTAP User Guide* .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnStorageVirtualMachine.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStorageVirtualMachineProps(
            file_system_id=file_system_id,
            name=name,
            active_directory_configuration=active_directory_configuration,
            root_volume_security_style=root_volume_security_style,
            svm_admin_password=svm_admin_password,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnStorageVirtualMachine.inspect)
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
            type_hints = typing.get_type_hints(CfnStorageVirtualMachine._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''Returns the storage virtual machine's Amazon Resource Name (ARN).

        Example: ``arn:aws:fsx:us-east-2:111111111111:storage-virtual-machine/fs-0123456789abcdef1/svm-01234567890123456``

        :cloudformationAttribute: ResourceARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStorageVirtualMachineId")
    def attr_storage_virtual_machine_id(self) -> builtins.str:
        '''Returns the storgage virtual machine's system generated ID.

        Example: ``svm-0123456789abcedf1``

        :cloudformationAttribute: StorageVirtualMachineId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageVirtualMachineId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUuid")
    def attr_uuid(self) -> builtins.str:
        '''Returns the storage virtual machine's system generated unique identifier (UUID).

        Example: ``abcd0123-cd45-ef67-11aa-1111aaaa23bc``

        :cloudformationAttribute: UUID
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUuid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''Specifies the FSx for ONTAP file system on which to create the SVM.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-filesystemid
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStorageVirtualMachine, "file_system_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the SVM.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStorageVirtualMachine, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="activeDirectoryConfiguration")
    def active_directory_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty", _IResolvable_da3f097b]]:
        '''Describes the Microsoft Active Directory configuration to which the SVM is joined, if applicable.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "activeDirectoryConfiguration"))

    @active_directory_configuration.setter
    def active_directory_configuration(
        self,
        value: typing.Optional[typing.Union["CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStorageVirtualMachine, "active_directory_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeDirectoryConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rootVolumeSecurityStyle")
    def root_volume_security_style(self) -> typing.Optional[builtins.str]:
        '''The security style of the root volume of the SVM. Specify one of the following values:.

        - ``UNIX`` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account.
        - ``NTFS`` if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account.
        - ``MIXED`` if the file system is managed by both UNIX and Windows administrators and users consist of both NFS and SMB clients.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-rootvolumesecuritystyle
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootVolumeSecurityStyle"))

    @root_volume_security_style.setter
    def root_volume_security_style(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStorageVirtualMachine, "root_volume_security_style").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootVolumeSecurityStyle", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="svmAdminPassword")
    def svm_admin_password(self) -> typing.Optional[builtins.str]:
        '''Specifies the password to use when logging on to the SVM using a secure shell (SSH) connection to the SVM's management endpoint.

        Doing so enables you to manage the SVM using the NetApp ONTAP CLI or REST API. If you do not specify a password, you can still use the file system's ``fsxadmin`` user to manage the SVM. For more information, see `Managing SVMs using the NetApp ONTAP CLI <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html#vsadmin-ontap-cli>`_ in the *FSx for ONTAP User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-svmadminpassword
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "svmAdminPassword"))

    @svm_admin_password.setter
    def svm_admin_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStorageVirtualMachine, "svm_admin_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "svmAdminPassword", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "net_bios_name": "netBiosName",
            "self_managed_active_directory_configuration": "selfManagedActiveDirectoryConfiguration",
        },
    )
    class ActiveDirectoryConfigurationProperty:
        def __init__(
            self,
            *,
            net_bios_name: typing.Optional[builtins.str] = None,
            self_managed_active_directory_configuration: typing.Optional[typing.Union[typing.Union["CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the self-managed Microsoft Active Directory to which you want to join the SVM.

            Joining an Active Directory provides user authentication and access control for SMB clients, including Microsoft Windows and macOS client accessing the file system.

            :param net_bios_name: The NetBIOS name of the Active Directory computer object that will be created for your SVM.
            :param self_managed_active_directory_configuration: The configuration that Amazon FSx uses to join the ONTAP storage virtual machine (SVM) to your self-managed (including on-premises) Microsoft Active Directory (AD) directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                active_directory_configuration_property = fsx.CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty(
                    net_bios_name="netBiosName",
                    self_managed_active_directory_configuration=fsx.CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty(
                        dns_ips=["dnsIps"],
                        domain_name="domainName",
                        file_system_administrators_group="fileSystemAdministratorsGroup",
                        organizational_unit_distinguished_name="organizationalUnitDistinguishedName",
                        password="password",
                        user_name="userName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty.__init__)
                check_type(argname="argument net_bios_name", value=net_bios_name, expected_type=type_hints["net_bios_name"])
                check_type(argname="argument self_managed_active_directory_configuration", value=self_managed_active_directory_configuration, expected_type=type_hints["self_managed_active_directory_configuration"])
            self._values: typing.Dict[str, typing.Any] = {}
            if net_bios_name is not None:
                self._values["net_bios_name"] = net_bios_name
            if self_managed_active_directory_configuration is not None:
                self._values["self_managed_active_directory_configuration"] = self_managed_active_directory_configuration

        @builtins.property
        def net_bios_name(self) -> typing.Optional[builtins.str]:
            '''The NetBIOS name of the Active Directory computer object that will be created for your SVM.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-netbiosname
            '''
            result = self._values.get("net_bios_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def self_managed_active_directory_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty", _IResolvable_da3f097b]]:
            '''The configuration that Amazon FSx uses to join the ONTAP storage virtual machine (SVM) to your self-managed (including on-premises) Microsoft Active Directory (AD) directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration
            '''
            result = self._values.get("self_managed_active_directory_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActiveDirectoryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_ips": "dnsIps",
            "domain_name": "domainName",
            "file_system_administrators_group": "fileSystemAdministratorsGroup",
            "organizational_unit_distinguished_name": "organizationalUnitDistinguishedName",
            "password": "password",
            "user_name": "userName",
        },
    )
    class SelfManagedActiveDirectoryConfigurationProperty:
        def __init__(
            self,
            *,
            dns_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
            domain_name: typing.Optional[builtins.str] = None,
            file_system_administrators_group: typing.Optional[builtins.str] = None,
            organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
            password: typing.Optional[builtins.str] = None,
            user_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory.

            For more information, see `Using Amazon FSx with your self-managed Microsoft Active Directory <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html>`_ or `Managing SVMs <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html>`_ .

            :param dns_ips: A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.
            :param domain_name: The fully qualified domain name of the self-managed AD directory, such as ``corp.example.com`` .
            :param file_system_administrators_group: (Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don't provide one, your AD domain's Domain Admins group is used.
            :param organizational_unit_distinguished_name: (Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory. Amazon FSx only accepts OU as the direct parent of the file system. An example is ``OU=FSx,DC=yourdomain,DC=corp,DC=com`` . To learn more, see `RFC 2253 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc2253>`_ . If none is provided, the FSx file system is created in the default location of your self-managed AD directory. .. epigraph:: Only Organizational Unit (OU) objects can be the direct parent of the file system that you're creating.
            :param password: The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
            :param user_name: The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in ``OrganizationalUnitDistinguishedName`` , or in the default location of your AD domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                self_managed_active_directory_configuration_property = fsx.CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty(
                    dns_ips=["dnsIps"],
                    domain_name="domainName",
                    file_system_administrators_group="fileSystemAdministratorsGroup",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName",
                    password="password",
                    user_name="userName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty.__init__)
                check_type(argname="argument dns_ips", value=dns_ips, expected_type=type_hints["dns_ips"])
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument file_system_administrators_group", value=file_system_administrators_group, expected_type=type_hints["file_system_administrators_group"])
                check_type(argname="argument organizational_unit_distinguished_name", value=organizational_unit_distinguished_name, expected_type=type_hints["organizational_unit_distinguished_name"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if dns_ips is not None:
                self._values["dns_ips"] = dns_ips
            if domain_name is not None:
                self._values["domain_name"] = domain_name
            if file_system_administrators_group is not None:
                self._values["file_system_administrators_group"] = file_system_administrators_group
            if organizational_unit_distinguished_name is not None:
                self._values["organizational_unit_distinguished_name"] = organizational_unit_distinguished_name
            if password is not None:
                self._values["password"] = password
            if user_name is not None:
                self._values["user_name"] = user_name

        @builtins.property
        def dns_ips(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-dnsips
            '''
            result = self._values.get("dns_ips")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def domain_name(self) -> typing.Optional[builtins.str]:
            '''The fully qualified domain name of the self-managed AD directory, such as ``corp.example.com`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-domainname
            '''
            result = self._values.get("domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_system_administrators_group(self) -> typing.Optional[builtins.str]:
            '''(Optional) The name of the domain group whose members are granted administrative privileges for the file system.

            Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don't provide one, your AD domain's Domain Admins group is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup
            '''
            result = self._values.get("file_system_administrators_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit_distinguished_name(
            self,
        ) -> typing.Optional[builtins.str]:
            '''(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory.

            Amazon FSx only accepts OU as the direct parent of the file system. An example is ``OU=FSx,DC=yourdomain,DC=corp,DC=com`` . To learn more, see `RFC 2253 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc2253>`_ . If none is provided, the FSx file system is created in the default location of your self-managed AD directory.
            .. epigraph::

               Only Organizational Unit (OU) objects can be the direct parent of the file system that you're creating.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname
            '''
            result = self._values.get("organizational_unit_distinguished_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_name(self) -> typing.Optional[builtins.str]:
            '''The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.

            This account must have the permission to join computers to the domain in the organizational unit provided in ``OrganizationalUnitDistinguishedName`` , or in the default location of your AD domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-username
            '''
            result = self._values.get("user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelfManagedActiveDirectoryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.CfnStorageVirtualMachineProps",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "name": "name",
        "active_directory_configuration": "activeDirectoryConfiguration",
        "root_volume_security_style": "rootVolumeSecurityStyle",
        "svm_admin_password": "svmAdminPassword",
        "tags": "tags",
    },
)
class CfnStorageVirtualMachineProps:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        name: builtins.str,
        active_directory_configuration: typing.Optional[typing.Union[typing.Union[CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        root_volume_security_style: typing.Optional[builtins.str] = None,
        svm_admin_password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStorageVirtualMachine``.

        :param file_system_id: Specifies the FSx for ONTAP file system on which to create the SVM.
        :param name: The name of the SVM.
        :param active_directory_configuration: Describes the Microsoft Active Directory configuration to which the SVM is joined, if applicable.
        :param root_volume_security_style: The security style of the root volume of the SVM. Specify one of the following values:. - ``UNIX`` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account. - ``NTFS`` if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account. - ``MIXED`` if the file system is managed by both UNIX and Windows administrators and users consist of both NFS and SMB clients.
        :param svm_admin_password: Specifies the password to use when logging on to the SVM using a secure shell (SSH) connection to the SVM's management endpoint. Doing so enables you to manage the SVM using the NetApp ONTAP CLI or REST API. If you do not specify a password, you can still use the file system's ``fsxadmin`` user to manage the SVM. For more information, see `Managing SVMs using the NetApp ONTAP CLI <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html#vsadmin-ontap-cli>`_ in the *FSx for ONTAP User Guide* .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fsx as fsx
            
            cfn_storage_virtual_machine_props = fsx.CfnStorageVirtualMachineProps(
                file_system_id="fileSystemId",
                name="name",
            
                # the properties below are optional
                active_directory_configuration=fsx.CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty(
                    net_bios_name="netBiosName",
                    self_managed_active_directory_configuration=fsx.CfnStorageVirtualMachine.SelfManagedActiveDirectoryConfigurationProperty(
                        dns_ips=["dnsIps"],
                        domain_name="domainName",
                        file_system_administrators_group="fileSystemAdministratorsGroup",
                        organizational_unit_distinguished_name="organizationalUnitDistinguishedName",
                        password="password",
                        user_name="userName"
                    )
                ),
                root_volume_security_style="rootVolumeSecurityStyle",
                svm_admin_password="svmAdminPassword",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnStorageVirtualMachineProps.__init__)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument active_directory_configuration", value=active_directory_configuration, expected_type=type_hints["active_directory_configuration"])
            check_type(argname="argument root_volume_security_style", value=root_volume_security_style, expected_type=type_hints["root_volume_security_style"])
            check_type(argname="argument svm_admin_password", value=svm_admin_password, expected_type=type_hints["svm_admin_password"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "file_system_id": file_system_id,
            "name": name,
        }
        if active_directory_configuration is not None:
            self._values["active_directory_configuration"] = active_directory_configuration
        if root_volume_security_style is not None:
            self._values["root_volume_security_style"] = root_volume_security_style
        if svm_admin_password is not None:
            self._values["svm_admin_password"] = svm_admin_password
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''Specifies the FSx for ONTAP file system on which to create the SVM.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-filesystemid
        '''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the SVM.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_directory_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty, _IResolvable_da3f097b]]:
        '''Describes the Microsoft Active Directory configuration to which the SVM is joined, if applicable.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration
        '''
        result = self._values.get("active_directory_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnStorageVirtualMachine.ActiveDirectoryConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def root_volume_security_style(self) -> typing.Optional[builtins.str]:
        '''The security style of the root volume of the SVM. Specify one of the following values:.

        - ``UNIX`` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account.
        - ``NTFS`` if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account.
        - ``MIXED`` if the file system is managed by both UNIX and Windows administrators and users consist of both NFS and SMB clients.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-rootvolumesecuritystyle
        '''
        result = self._values.get("root_volume_security_style")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def svm_admin_password(self) -> typing.Optional[builtins.str]:
        '''Specifies the password to use when logging on to the SVM using a secure shell (SSH) connection to the SVM's management endpoint.

        Doing so enables you to manage the SVM using the NetApp ONTAP CLI or REST API. If you do not specify a password, you can still use the file system's ``fsxadmin`` user to manage the SVM. For more information, see `Managing SVMs using the NetApp ONTAP CLI <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html#vsadmin-ontap-cli>`_ in the *FSx for ONTAP User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-svmadminpassword
        '''
        result = self._values.get("svm_admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStorageVirtualMachineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnVolume(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fsx.CfnVolume",
):
    '''A CloudFormation ``AWS::FSx::Volume``.

    Creates an FSx for ONTAP or Amazon FSx for OpenZFS storage volume.

    :cloudformationResource: AWS::FSx::Volume
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fsx as fsx
        
        cfn_volume = fsx.CfnVolume(self, "MyCfnVolume",
            name="name",
        
            # the properties below are optional
            backup_id="backupId",
            ontap_configuration=fsx.CfnVolume.OntapConfigurationProperty(
                junction_path="junctionPath",
                size_in_megabytes="sizeInMegabytes",
                storage_efficiency_enabled="storageEfficiencyEnabled",
                storage_virtual_machine_id="storageVirtualMachineId",
        
                # the properties below are optional
                security_style="securityStyle",
                tiering_policy=fsx.CfnVolume.TieringPolicyProperty(
                    cooling_period=123,
                    name="name"
                )
            ),
            open_zfs_configuration=fsx.CfnVolume.OpenZFSConfigurationProperty(
                parent_volume_id="parentVolumeId",
        
                # the properties below are optional
                copy_tags_to_snapshots=False,
                data_compression_type="dataCompressionType",
                nfs_exports=[fsx.CfnVolume.NfsExportsProperty(
                    client_configurations=[fsx.CfnVolume.ClientConfigurationsProperty(
                        clients="clients",
                        options=["options"]
                    )]
                )],
                options=["options"],
                origin_snapshot=fsx.CfnVolume.OriginSnapshotProperty(
                    copy_strategy="copyStrategy",
                    snapshot_arn="snapshotArn"
                ),
                read_only=False,
                record_size_ki_b=123,
                storage_capacity_quota_gi_b=123,
                storage_capacity_reservation_gi_b=123,
                user_and_group_quotas=[fsx.CfnVolume.UserAndGroupQuotasProperty(
                    id=123,
                    storage_capacity_quota_gi_b=123,
                    type="type"
                )]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            volume_type="volumeType"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        backup_id: typing.Optional[builtins.str] = None,
        ontap_configuration: typing.Optional[typing.Union[typing.Union["CfnVolume.OntapConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        open_zfs_configuration: typing.Optional[typing.Union[typing.Union["CfnVolume.OpenZFSConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::FSx::Volume``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the volume.
        :param backup_id: Specifies the ID of the volume backup to use to create a new volume.
        :param ontap_configuration: The configuration of an Amazon FSx for NetApp ONTAP volume.
        :param open_zfs_configuration: The configuration of an Amazon FSx for OpenZFS volume.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param volume_type: The type of the volume.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVolume.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVolumeProps(
            name=name,
            backup_id=backup_id,
            ontap_configuration=ontap_configuration,
            open_zfs_configuration=open_zfs_configuration,
            tags=tags,
            volume_type=volume_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVolume.inspect)
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
            type_hints = typing.get_type_hints(CfnVolume._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''Returns the volume's Amazon Resource Name (ARN).

        Example: ``arn:aws:fsx:us-east-2:111122223333:volume/fs-0123456789abcdef9/fsvol-01234567891112223``

        :cloudformationAttribute: ResourceARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUuid")
    def attr_uuid(self) -> builtins.str:
        '''Returns the volume's universally unique identifier (UUID).

        Example: ``abcd0123-cd45-ef67-11aa-1111aaaa23bc``

        :cloudformationAttribute: UUID
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUuid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVolumeId")
    def attr_volume_id(self) -> builtins.str:
        '''Returns the volume's ID.

        Example: ``fsvol-0123456789abcdefa``

        :cloudformationAttribute: VolumeId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVolumeId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVolume, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="backupId")
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the ID of the volume backup to use to create a new volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-backupid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupId"))

    @backup_id.setter
    def backup_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVolume, "backup_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ontapConfiguration")
    def ontap_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnVolume.OntapConfigurationProperty", _IResolvable_da3f097b]]:
        '''The configuration of an Amazon FSx for NetApp ONTAP volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-ontapconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnVolume.OntapConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "ontapConfiguration"))

    @ontap_configuration.setter
    def ontap_configuration(
        self,
        value: typing.Optional[typing.Union["CfnVolume.OntapConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVolume, "ontap_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ontapConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="openZfsConfiguration")
    def open_zfs_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnVolume.OpenZFSConfigurationProperty", _IResolvable_da3f097b]]:
        '''The configuration of an Amazon FSx for OpenZFS volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-openzfsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnVolume.OpenZFSConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "openZfsConfiguration"))

    @open_zfs_configuration.setter
    def open_zfs_configuration(
        self,
        value: typing.Optional[typing.Union["CfnVolume.OpenZFSConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVolume, "open_zfs_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openZfsConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''The type of the volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-volumetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnVolume, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnVolume.ClientConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={"clients": "clients", "options": "options"},
    )
    class ClientConfigurationsProperty:
        def __init__(
            self,
            *,
            clients: builtins.str,
            options: typing.Sequence[builtins.str],
        ) -> None:
            '''Specifies who can mount an OpenZFS file system and the options available while mounting the file system.

            :param clients: A value that specifies who can mount the file system. You can provide a wildcard character ( ``*`` ), an IP address ( ``0.0.0.0`` ), or a CIDR address ( ``192.0.2.0/24`` ). By default, Amazon FSx uses the wildcard character when specifying the client.
            :param options: The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the `exports(5) - Linux man page <https://docs.aws.amazon.com/https://linux.die.net/man/5/exports>`_ . When choosing your options, consider the following: - ``crossmnt`` is used by default. If you don't specify ``crossmnt`` when changing the client configuration, you won't be able to see or access snapshots in your file system's snapshot directory. - ``sync`` is used by default. If you instead specify ``async`` , the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                client_configurations_property = fsx.CfnVolume.ClientConfigurationsProperty(
                    clients="clients",
                    options=["options"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnVolume.ClientConfigurationsProperty.__init__)
                check_type(argname="argument clients", value=clients, expected_type=type_hints["clients"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            self._values: typing.Dict[str, typing.Any] = {
                "clients": clients,
                "options": options,
            }

        @builtins.property
        def clients(self) -> builtins.str:
            '''A value that specifies who can mount the file system.

            You can provide a wildcard character ( ``*`` ), an IP address ( ``0.0.0.0`` ), or a CIDR address ( ``192.0.2.0/24`` ). By default, Amazon FSx uses the wildcard character when specifying the client.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations.html#cfn-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations-clients
            '''
            result = self._values.get("clients")
            assert result is not None, "Required property 'clients' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def options(self) -> typing.List[builtins.str]:
            '''The options to use when mounting the file system.

            For a list of options that you can use with Network File System (NFS), see the `exports(5) - Linux man page <https://docs.aws.amazon.com/https://linux.die.net/man/5/exports>`_ . When choosing your options, consider the following:

            - ``crossmnt`` is used by default. If you don't specify ``crossmnt`` when changing the client configuration, you won't be able to see or access snapshots in your file system's snapshot directory.
            - ``sync`` is used by default. If you instead specify ``async`` , the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations.html#cfn-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations-options
            '''
            result = self._values.get("options")
            assert result is not None, "Required property 'options' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnVolume.NfsExportsProperty",
        jsii_struct_bases=[],
        name_mapping={"client_configurations": "clientConfigurations"},
    )
    class NfsExportsProperty:
        def __init__(
            self,
            *,
            client_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnVolume.ClientConfigurationsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        ) -> None:
            '''The configuration object for mounting a Network File System (NFS) file system.

            :param client_configurations: A list of configuration objects that contain the client and options for mounting the OpenZFS file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                nfs_exports_property = fsx.CfnVolume.NfsExportsProperty(
                    client_configurations=[fsx.CfnVolume.ClientConfigurationsProperty(
                        clients="clients",
                        options=["options"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnVolume.NfsExportsProperty.__init__)
                check_type(argname="argument client_configurations", value=client_configurations, expected_type=type_hints["client_configurations"])
            self._values: typing.Dict[str, typing.Any] = {
                "client_configurations": client_configurations,
            }

        @builtins.property
        def client_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnVolume.ClientConfigurationsProperty", _IResolvable_da3f097b]]]:
            '''A list of configuration objects that contain the client and options for mounting the OpenZFS file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports.html#cfn-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations
            '''
            result = self._values.get("client_configurations")
            assert result is not None, "Required property 'client_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnVolume.ClientConfigurationsProperty", _IResolvable_da3f097b]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NfsExportsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnVolume.OntapConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "junction_path": "junctionPath",
            "size_in_megabytes": "sizeInMegabytes",
            "storage_efficiency_enabled": "storageEfficiencyEnabled",
            "storage_virtual_machine_id": "storageVirtualMachineId",
            "security_style": "securityStyle",
            "tiering_policy": "tieringPolicy",
        },
    )
    class OntapConfigurationProperty:
        def __init__(
            self,
            *,
            junction_path: builtins.str,
            size_in_megabytes: builtins.str,
            storage_efficiency_enabled: builtins.str,
            storage_virtual_machine_id: builtins.str,
            security_style: typing.Optional[builtins.str] = None,
            tiering_policy: typing.Optional[typing.Union[typing.Union["CfnVolume.TieringPolicyProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies the configuration of the ONTAP volume that you are creating.

            :param junction_path: Specifies the location in the SVM's namespace where the volume is mounted. The ``JunctionPath`` must have a leading forward slash, such as ``/vol3`` .
            :param size_in_megabytes: Specifies the size of the volume, in megabytes (MB), that you are creating.
            :param storage_efficiency_enabled: Set to true to enable deduplication, compression, and compaction storage efficiency features on the volume.
            :param storage_virtual_machine_id: Specifies the ONTAP SVM in which to create the volume.
            :param security_style: The security style for the volume. Specify one of the following values:. - ``UNIX`` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account. ``UNIX`` is the default. - ``NTFS`` if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account. - ``MIXED`` if the file system is managed by both UNIX and Windows administrators and users consist of both NFS and SMB clients.
            :param tiering_policy: Describes the data tiering policy for an ONTAP volume. When enabled, Amazon FSx for ONTAP's intelligent tiering automatically transitions a volume's data between the file system's primary storage and capacity pool storage based on your access patterns. Valid tiering policies are the following: - ``SNAPSHOT_ONLY`` - (Default value) moves cold snapshots to the capacity pool storage tier. - ``AUTO`` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns. - ``ALL`` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier. - ``NONE`` - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                ontap_configuration_property = fsx.CfnVolume.OntapConfigurationProperty(
                    junction_path="junctionPath",
                    size_in_megabytes="sizeInMegabytes",
                    storage_efficiency_enabled="storageEfficiencyEnabled",
                    storage_virtual_machine_id="storageVirtualMachineId",
                
                    # the properties below are optional
                    security_style="securityStyle",
                    tiering_policy=fsx.CfnVolume.TieringPolicyProperty(
                        cooling_period=123,
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnVolume.OntapConfigurationProperty.__init__)
                check_type(argname="argument junction_path", value=junction_path, expected_type=type_hints["junction_path"])
                check_type(argname="argument size_in_megabytes", value=size_in_megabytes, expected_type=type_hints["size_in_megabytes"])
                check_type(argname="argument storage_efficiency_enabled", value=storage_efficiency_enabled, expected_type=type_hints["storage_efficiency_enabled"])
                check_type(argname="argument storage_virtual_machine_id", value=storage_virtual_machine_id, expected_type=type_hints["storage_virtual_machine_id"])
                check_type(argname="argument security_style", value=security_style, expected_type=type_hints["security_style"])
                check_type(argname="argument tiering_policy", value=tiering_policy, expected_type=type_hints["tiering_policy"])
            self._values: typing.Dict[str, typing.Any] = {
                "junction_path": junction_path,
                "size_in_megabytes": size_in_megabytes,
                "storage_efficiency_enabled": storage_efficiency_enabled,
                "storage_virtual_machine_id": storage_virtual_machine_id,
            }
            if security_style is not None:
                self._values["security_style"] = security_style
            if tiering_policy is not None:
                self._values["tiering_policy"] = tiering_policy

        @builtins.property
        def junction_path(self) -> builtins.str:
            '''Specifies the location in the SVM's namespace where the volume is mounted.

            The ``JunctionPath`` must have a leading forward slash, such as ``/vol3`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-junctionpath
            '''
            result = self._values.get("junction_path")
            assert result is not None, "Required property 'junction_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def size_in_megabytes(self) -> builtins.str:
            '''Specifies the size of the volume, in megabytes (MB), that you are creating.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-sizeinmegabytes
            '''
            result = self._values.get("size_in_megabytes")
            assert result is not None, "Required property 'size_in_megabytes' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def storage_efficiency_enabled(self) -> builtins.str:
            '''Set to true to enable deduplication, compression, and compaction storage efficiency features on the volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-storageefficiencyenabled
            '''
            result = self._values.get("storage_efficiency_enabled")
            assert result is not None, "Required property 'storage_efficiency_enabled' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def storage_virtual_machine_id(self) -> builtins.str:
            '''Specifies the ONTAP SVM in which to create the volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-storagevirtualmachineid
            '''
            result = self._values.get("storage_virtual_machine_id")
            assert result is not None, "Required property 'storage_virtual_machine_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def security_style(self) -> typing.Optional[builtins.str]:
            '''The security style for the volume. Specify one of the following values:.

            - ``UNIX`` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account. ``UNIX`` is the default.
            - ``NTFS`` if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account.
            - ``MIXED`` if the file system is managed by both UNIX and Windows administrators and users consist of both NFS and SMB clients.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-securitystyle
            '''
            result = self._values.get("security_style")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tiering_policy(
            self,
        ) -> typing.Optional[typing.Union["CfnVolume.TieringPolicyProperty", _IResolvable_da3f097b]]:
            '''Describes the data tiering policy for an ONTAP volume.

            When enabled, Amazon FSx for ONTAP's intelligent tiering automatically transitions a volume's data between the file system's primary storage and capacity pool storage based on your access patterns.

            Valid tiering policies are the following:

            - ``SNAPSHOT_ONLY`` - (Default value) moves cold snapshots to the capacity pool storage tier.
            - ``AUTO`` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
            - ``ALL`` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
            - ``NONE`` - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-tieringpolicy
            '''
            result = self._values.get("tiering_policy")
            return typing.cast(typing.Optional[typing.Union["CfnVolume.TieringPolicyProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OntapConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnVolume.OpenZFSConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parent_volume_id": "parentVolumeId",
            "copy_tags_to_snapshots": "copyTagsToSnapshots",
            "data_compression_type": "dataCompressionType",
            "nfs_exports": "nfsExports",
            "options": "options",
            "origin_snapshot": "originSnapshot",
            "read_only": "readOnly",
            "record_size_kib": "recordSizeKiB",
            "storage_capacity_quota_gib": "storageCapacityQuotaGiB",
            "storage_capacity_reservation_gib": "storageCapacityReservationGiB",
            "user_and_group_quotas": "userAndGroupQuotas",
        },
    )
    class OpenZFSConfigurationProperty:
        def __init__(
            self,
            *,
            parent_volume_id: builtins.str,
            copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            data_compression_type: typing.Optional[builtins.str] = None,
            nfs_exports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnVolume.NfsExportsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            options: typing.Optional[typing.Sequence[builtins.str]] = None,
            origin_snapshot: typing.Optional[typing.Union[typing.Union["CfnVolume.OriginSnapshotProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            record_size_kib: typing.Optional[jsii.Number] = None,
            storage_capacity_quota_gib: typing.Optional[jsii.Number] = None,
            storage_capacity_reservation_gib: typing.Optional[jsii.Number] = None,
            user_and_group_quotas: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnVolume.UserAndGroupQuotasProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Specifies the configuration of the Amazon FSx for OpenZFS volume that you are creating.

            :param parent_volume_id: The ID of the volume to use as the parent volume of the volume that you are creating.
            :param copy_tags_to_snapshots: A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to ``false`` . If it's set to ``true`` , all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is ``true`` , and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.
            :param data_compression_type: Specifies the method used to compress the data on the volume. The compression type is ``NONE`` by default. - ``NONE`` - Doesn't compress the data on the volume. ``NONE`` is the default. - ``ZSTD`` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization. - ``LZ4`` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.
            :param nfs_exports: The configuration object for mounting a Network File System (NFS) file system.
            :param options: To delete the volume's child volumes, snapshots, and clones, use the string ``DELETE_CHILD_VOLUMES_AND_SNAPSHOTS`` .
            :param origin_snapshot: The configuration object that specifies the snapshot to use as the origin of the data for the volume.
            :param read_only: A Boolean value indicating whether the volume is read-only.
            :param record_size_kib: Specifies the suggested block size for a volume in a ZFS dataset, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. We recommend using the default setting for the majority of use cases. Generally, workloads that write in fixed small or large record sizes may benefit from setting a custom record size, like database workloads (small record size) or media streaming workloads (large record size). For additional guidance on when to set a custom record size, see `ZFS Record size <https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#record-size-performance>`_ in the *Amazon FSx for OpenZFS User Guide* .
            :param storage_capacity_quota_gib: Sets the maximum storage size in gibibytes (GiB) for the volume. You can specify a quota that is larger than the storage on the parent volume. A volume quota limits the amount of storage that the volume can consume to the configured amount, but does not guarantee the space will be available on the parent volume. To guarantee quota space, you must also set ``StorageCapacityReservationGiB`` . To *not* specify a storage capacity quota, set this to ``-1`` . For more information, see `Volume properties <https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties>`_ in the *Amazon FSx for OpenZFS User Guide* .
            :param storage_capacity_reservation_gib: Specifies the amount of storage in gibibytes (GiB) to reserve from the parent volume. Setting ``StorageCapacityReservationGiB`` guarantees that the specified amount of storage space on the parent volume will always be available for the volume. You can't reserve more storage than the parent volume has. To *not* specify a storage capacity reservation, set this to ``0`` or ``-1`` . For more information, see `Volume properties <https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties>`_ in the *Amazon FSx for OpenZFS User Guide* .
            :param user_and_group_quotas: An object specifying how much storage users or groups can use on the volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                open_zFSConfiguration_property = fsx.CfnVolume.OpenZFSConfigurationProperty(
                    parent_volume_id="parentVolumeId",
                
                    # the properties below are optional
                    copy_tags_to_snapshots=False,
                    data_compression_type="dataCompressionType",
                    nfs_exports=[fsx.CfnVolume.NfsExportsProperty(
                        client_configurations=[fsx.CfnVolume.ClientConfigurationsProperty(
                            clients="clients",
                            options=["options"]
                        )]
                    )],
                    options=["options"],
                    origin_snapshot=fsx.CfnVolume.OriginSnapshotProperty(
                        copy_strategy="copyStrategy",
                        snapshot_arn="snapshotArn"
                    ),
                    read_only=False,
                    record_size_ki_b=123,
                    storage_capacity_quota_gi_b=123,
                    storage_capacity_reservation_gi_b=123,
                    user_and_group_quotas=[fsx.CfnVolume.UserAndGroupQuotasProperty(
                        id=123,
                        storage_capacity_quota_gi_b=123,
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnVolume.OpenZFSConfigurationProperty.__init__)
                check_type(argname="argument parent_volume_id", value=parent_volume_id, expected_type=type_hints["parent_volume_id"])
                check_type(argname="argument copy_tags_to_snapshots", value=copy_tags_to_snapshots, expected_type=type_hints["copy_tags_to_snapshots"])
                check_type(argname="argument data_compression_type", value=data_compression_type, expected_type=type_hints["data_compression_type"])
                check_type(argname="argument nfs_exports", value=nfs_exports, expected_type=type_hints["nfs_exports"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
                check_type(argname="argument origin_snapshot", value=origin_snapshot, expected_type=type_hints["origin_snapshot"])
                check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
                check_type(argname="argument record_size_kib", value=record_size_kib, expected_type=type_hints["record_size_kib"])
                check_type(argname="argument storage_capacity_quota_gib", value=storage_capacity_quota_gib, expected_type=type_hints["storage_capacity_quota_gib"])
                check_type(argname="argument storage_capacity_reservation_gib", value=storage_capacity_reservation_gib, expected_type=type_hints["storage_capacity_reservation_gib"])
                check_type(argname="argument user_and_group_quotas", value=user_and_group_quotas, expected_type=type_hints["user_and_group_quotas"])
            self._values: typing.Dict[str, typing.Any] = {
                "parent_volume_id": parent_volume_id,
            }
            if copy_tags_to_snapshots is not None:
                self._values["copy_tags_to_snapshots"] = copy_tags_to_snapshots
            if data_compression_type is not None:
                self._values["data_compression_type"] = data_compression_type
            if nfs_exports is not None:
                self._values["nfs_exports"] = nfs_exports
            if options is not None:
                self._values["options"] = options
            if origin_snapshot is not None:
                self._values["origin_snapshot"] = origin_snapshot
            if read_only is not None:
                self._values["read_only"] = read_only
            if record_size_kib is not None:
                self._values["record_size_kib"] = record_size_kib
            if storage_capacity_quota_gib is not None:
                self._values["storage_capacity_quota_gib"] = storage_capacity_quota_gib
            if storage_capacity_reservation_gib is not None:
                self._values["storage_capacity_reservation_gib"] = storage_capacity_reservation_gib
            if user_and_group_quotas is not None:
                self._values["user_and_group_quotas"] = user_and_group_quotas

        @builtins.property
        def parent_volume_id(self) -> builtins.str:
            '''The ID of the volume to use as the parent volume of the volume that you are creating.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-parentvolumeid
            '''
            result = self._values.get("parent_volume_id")
            assert result is not None, "Required property 'parent_volume_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def copy_tags_to_snapshots(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether tags for the volume should be copied to snapshots.

            This value defaults to ``false`` . If it's set to ``true`` , all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is ``true`` , and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-copytagstosnapshots
            '''
            result = self._values.get("copy_tags_to_snapshots")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def data_compression_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the method used to compress the data on the volume. The compression type is ``NONE`` by default.

            - ``NONE`` - Doesn't compress the data on the volume. ``NONE`` is the default.
            - ``ZSTD`` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
            - ``LZ4`` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-datacompressiontype
            '''
            result = self._values.get("data_compression_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def nfs_exports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnVolume.NfsExportsProperty", _IResolvable_da3f097b]]]]:
            '''The configuration object for mounting a Network File System (NFS) file system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-nfsexports
            '''
            result = self._values.get("nfs_exports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnVolume.NfsExportsProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def options(self) -> typing.Optional[typing.List[builtins.str]]:
            '''To delete the volume's child volumes, snapshots, and clones, use the string ``DELETE_CHILD_VOLUMES_AND_SNAPSHOTS`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def origin_snapshot(
            self,
        ) -> typing.Optional[typing.Union["CfnVolume.OriginSnapshotProperty", _IResolvable_da3f097b]]:
            '''The configuration object that specifies the snapshot to use as the origin of the data for the volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-originsnapshot
            '''
            result = self._values.get("origin_snapshot")
            return typing.cast(typing.Optional[typing.Union["CfnVolume.OriginSnapshotProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def read_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether the volume is read-only.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-readonly
            '''
            result = self._values.get("read_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def record_size_kib(self) -> typing.Optional[jsii.Number]:
            '''Specifies the suggested block size for a volume in a ZFS dataset, in kibibytes (KiB).

            Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. We recommend using the default setting for the majority of use cases. Generally, workloads that write in fixed small or large record sizes may benefit from setting a custom record size, like database workloads (small record size) or media streaming workloads (large record size). For additional guidance on when to set a custom record size, see `ZFS Record size <https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#record-size-performance>`_ in the *Amazon FSx for OpenZFS User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-recordsizekib
            '''
            result = self._values.get("record_size_kib")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def storage_capacity_quota_gib(self) -> typing.Optional[jsii.Number]:
            '''Sets the maximum storage size in gibibytes (GiB) for the volume.

            You can specify a quota that is larger than the storage on the parent volume. A volume quota limits the amount of storage that the volume can consume to the configured amount, but does not guarantee the space will be available on the parent volume. To guarantee quota space, you must also set ``StorageCapacityReservationGiB`` . To *not* specify a storage capacity quota, set this to ``-1`` .

            For more information, see `Volume properties <https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties>`_ in the *Amazon FSx for OpenZFS User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-storagecapacityquotagib
            '''
            result = self._values.get("storage_capacity_quota_gib")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def storage_capacity_reservation_gib(self) -> typing.Optional[jsii.Number]:
            '''Specifies the amount of storage in gibibytes (GiB) to reserve from the parent volume.

            Setting ``StorageCapacityReservationGiB`` guarantees that the specified amount of storage space on the parent volume will always be available for the volume. You can't reserve more storage than the parent volume has. To *not* specify a storage capacity reservation, set this to ``0`` or ``-1`` . For more information, see `Volume properties <https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties>`_ in the *Amazon FSx for OpenZFS User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-storagecapacityreservationgib
            '''
            result = self._values.get("storage_capacity_reservation_gib")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def user_and_group_quotas(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnVolume.UserAndGroupQuotasProperty", _IResolvable_da3f097b]]]]:
            '''An object specifying how much storage users or groups can use on the volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-userandgroupquotas
            '''
            result = self._values.get("user_and_group_quotas")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnVolume.UserAndGroupQuotasProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenZFSConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnVolume.OriginSnapshotProperty",
        jsii_struct_bases=[],
        name_mapping={"copy_strategy": "copyStrategy", "snapshot_arn": "snapshotArn"},
    )
    class OriginSnapshotProperty:
        def __init__(
            self,
            *,
            copy_strategy: builtins.str,
            snapshot_arn: builtins.str,
        ) -> None:
            '''The configuration object that specifies the snapshot to use as the origin of the data for the volume.

            :param copy_strategy: The strategy used when copying data from the snapshot to the new volume. - ``CLONE`` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesn't consume disk throughput. However, the origin snapshot can't be deleted if there is a volume using its copied data. - ``FULL_COPY`` - Copies all data from the snapshot to the new volume.
            :param snapshot_arn: Specifies the snapshot to use when creating an OpenZFS volume from a snapshot.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-originsnapshot.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                origin_snapshot_property = fsx.CfnVolume.OriginSnapshotProperty(
                    copy_strategy="copyStrategy",
                    snapshot_arn="snapshotArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnVolume.OriginSnapshotProperty.__init__)
                check_type(argname="argument copy_strategy", value=copy_strategy, expected_type=type_hints["copy_strategy"])
                check_type(argname="argument snapshot_arn", value=snapshot_arn, expected_type=type_hints["snapshot_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "copy_strategy": copy_strategy,
                "snapshot_arn": snapshot_arn,
            }

        @builtins.property
        def copy_strategy(self) -> builtins.str:
            '''The strategy used when copying data from the snapshot to the new volume.

            - ``CLONE`` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesn't consume disk throughput. However, the origin snapshot can't be deleted if there is a volume using its copied data.
            - ``FULL_COPY`` - Copies all data from the snapshot to the new volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-originsnapshot.html#cfn-fsx-volume-openzfsconfiguration-originsnapshot-copystrategy
            '''
            result = self._values.get("copy_strategy")
            assert result is not None, "Required property 'copy_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def snapshot_arn(self) -> builtins.str:
            '''Specifies the snapshot to use when creating an OpenZFS volume from a snapshot.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-originsnapshot.html#cfn-fsx-volume-openzfsconfiguration-originsnapshot-snapshotarn
            '''
            result = self._values.get("snapshot_arn")
            assert result is not None, "Required property 'snapshot_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginSnapshotProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnVolume.TieringPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"cooling_period": "coolingPeriod", "name": "name"},
    )
    class TieringPolicyProperty:
        def __init__(
            self,
            *,
            cooling_period: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the data tiering policy for an ONTAP volume.

            When enabled, Amazon FSx for ONTAP's intelligent tiering automatically transitions a volume's data between the file system's primary storage and capacity pool storage based on your access patterns.

            Valid tiering policies are the following:

            - ``SNAPSHOT_ONLY`` - (Default value) moves cold snapshots to the capacity pool storage tier.
            - ``AUTO`` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
            - ``ALL`` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
            - ``NONE`` - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.

            :param cooling_period: Specifies the number of days that user data in a volume must remain inactive before it is considered "cold" and moved to the capacity pool. Used with the ``AUTO`` and ``SNAPSHOT_ONLY`` tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for ``AUTO`` and 2 days for ``SNAPSHOT_ONLY`` .
            :param name: Specifies the tiering policy used to transition data. Default value is ``SNAPSHOT_ONLY`` . - ``SNAPSHOT_ONLY`` - moves cold snapshots to the capacity pool storage tier. - ``AUTO`` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns. - ``ALL`` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier. - ``NONE`` - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-tieringpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                tiering_policy_property = fsx.CfnVolume.TieringPolicyProperty(
                    cooling_period=123,
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnVolume.TieringPolicyProperty.__init__)
                check_type(argname="argument cooling_period", value=cooling_period, expected_type=type_hints["cooling_period"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if cooling_period is not None:
                self._values["cooling_period"] = cooling_period
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def cooling_period(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of days that user data in a volume must remain inactive before it is considered "cold" and moved to the capacity pool.

            Used with the ``AUTO`` and ``SNAPSHOT_ONLY`` tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for ``AUTO`` and 2 days for ``SNAPSHOT_ONLY`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-tieringpolicy.html#cfn-fsx-volume-ontapconfiguration-tieringpolicy-coolingperiod
            '''
            result = self._values.get("cooling_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Specifies the tiering policy used to transition data. Default value is ``SNAPSHOT_ONLY`` .

            - ``SNAPSHOT_ONLY`` - moves cold snapshots to the capacity pool storage tier.
            - ``AUTO`` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
            - ``ALL`` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
            - ``NONE`` - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-tieringpolicy.html#cfn-fsx-volume-ontapconfiguration-tieringpolicy-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TieringPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fsx.CfnVolume.UserAndGroupQuotasProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "storage_capacity_quota_gib": "storageCapacityQuotaGiB",
            "type": "type",
        },
    )
    class UserAndGroupQuotasProperty:
        def __init__(
            self,
            *,
            id: jsii.Number,
            storage_capacity_quota_gib: jsii.Number,
            type: builtins.str,
        ) -> None:
            '''An object specifying how much storage users or groups can use on the volume.

            :param id: The ID of the user or group.
            :param storage_capacity_quota_gib: The amount of storage that the user or group can use in gibibytes (GiB).
            :param type: A value that specifies whether the quota applies to a user or group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fsx as fsx
                
                user_and_group_quotas_property = fsx.CfnVolume.UserAndGroupQuotasProperty(
                    id=123,
                    storage_capacity_quota_gi_b=123,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnVolume.UserAndGroupQuotasProperty.__init__)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument storage_capacity_quota_gib", value=storage_capacity_quota_gib, expected_type=type_hints["storage_capacity_quota_gib"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {
                "id": id,
                "storage_capacity_quota_gib": storage_capacity_quota_gib,
                "type": type,
            }

        @builtins.property
        def id(self) -> jsii.Number:
            '''The ID of the user or group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html#cfn-fsx-volume-openzfsconfiguration-userandgroupquotas-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def storage_capacity_quota_gib(self) -> jsii.Number:
            '''The amount of storage that the user or group can use in gibibytes (GiB).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html#cfn-fsx-volume-openzfsconfiguration-userandgroupquotas-storagecapacityquotagib
            '''
            result = self._values.get("storage_capacity_quota_gib")
            assert result is not None, "Required property 'storage_capacity_quota_gib' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''A value that specifies whether the quota applies to a user or group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html#cfn-fsx-volume-openzfsconfiguration-userandgroupquotas-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserAndGroupQuotasProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.CfnVolumeProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "backup_id": "backupId",
        "ontap_configuration": "ontapConfiguration",
        "open_zfs_configuration": "openZfsConfiguration",
        "tags": "tags",
        "volume_type": "volumeType",
    },
)
class CfnVolumeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        backup_id: typing.Optional[builtins.str] = None,
        ontap_configuration: typing.Optional[typing.Union[typing.Union[CfnVolume.OntapConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        open_zfs_configuration: typing.Optional[typing.Union[typing.Union[CfnVolume.OpenZFSConfigurationProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVolume``.

        :param name: The name of the volume.
        :param backup_id: Specifies the ID of the volume backup to use to create a new volume.
        :param ontap_configuration: The configuration of an Amazon FSx for NetApp ONTAP volume.
        :param open_zfs_configuration: The configuration of an Amazon FSx for OpenZFS volume.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param volume_type: The type of the volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fsx as fsx
            
            cfn_volume_props = fsx.CfnVolumeProps(
                name="name",
            
                # the properties below are optional
                backup_id="backupId",
                ontap_configuration=fsx.CfnVolume.OntapConfigurationProperty(
                    junction_path="junctionPath",
                    size_in_megabytes="sizeInMegabytes",
                    storage_efficiency_enabled="storageEfficiencyEnabled",
                    storage_virtual_machine_id="storageVirtualMachineId",
            
                    # the properties below are optional
                    security_style="securityStyle",
                    tiering_policy=fsx.CfnVolume.TieringPolicyProperty(
                        cooling_period=123,
                        name="name"
                    )
                ),
                open_zfs_configuration=fsx.CfnVolume.OpenZFSConfigurationProperty(
                    parent_volume_id="parentVolumeId",
            
                    # the properties below are optional
                    copy_tags_to_snapshots=False,
                    data_compression_type="dataCompressionType",
                    nfs_exports=[fsx.CfnVolume.NfsExportsProperty(
                        client_configurations=[fsx.CfnVolume.ClientConfigurationsProperty(
                            clients="clients",
                            options=["options"]
                        )]
                    )],
                    options=["options"],
                    origin_snapshot=fsx.CfnVolume.OriginSnapshotProperty(
                        copy_strategy="copyStrategy",
                        snapshot_arn="snapshotArn"
                    ),
                    read_only=False,
                    record_size_ki_b=123,
                    storage_capacity_quota_gi_b=123,
                    storage_capacity_reservation_gi_b=123,
                    user_and_group_quotas=[fsx.CfnVolume.UserAndGroupQuotasProperty(
                        id=123,
                        storage_capacity_quota_gi_b=123,
                        type="type"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                volume_type="volumeType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnVolumeProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument backup_id", value=backup_id, expected_type=type_hints["backup_id"])
            check_type(argname="argument ontap_configuration", value=ontap_configuration, expected_type=type_hints["ontap_configuration"])
            check_type(argname="argument open_zfs_configuration", value=open_zfs_configuration, expected_type=type_hints["open_zfs_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if backup_id is not None:
            self._values["backup_id"] = backup_id
        if ontap_configuration is not None:
            self._values["ontap_configuration"] = ontap_configuration
        if open_zfs_configuration is not None:
            self._values["open_zfs_configuration"] = open_zfs_configuration
        if tags is not None:
            self._values["tags"] = tags
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the ID of the volume backup to use to create a new volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-backupid
        '''
        result = self._values.get("backup_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ontap_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnVolume.OntapConfigurationProperty, _IResolvable_da3f097b]]:
        '''The configuration of an Amazon FSx for NetApp ONTAP volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-ontapconfiguration
        '''
        result = self._values.get("ontap_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnVolume.OntapConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def open_zfs_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnVolume.OpenZFSConfigurationProperty, _IResolvable_da3f097b]]:
        '''The configuration of an Amazon FSx for OpenZFS volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-openzfsconfiguration
        '''
        result = self._values.get("open_zfs_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnVolume.OpenZFSConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''The type of the volume.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-volumetype
        '''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.FileSystemAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "dns_name": "dnsName",
        "file_system_id": "fileSystemId",
        "security_group": "securityGroup",
    },
)
class FileSystemAttributes:
    def __init__(
        self,
        *,
        dns_name: builtins.str,
        file_system_id: builtins.str,
        security_group: _ISecurityGroup_acf8a799,
    ) -> None:
        '''Properties that describe an existing FSx file system.

        :param dns_name: The DNS name assigned to this file system.
        :param file_system_id: The ID of the file system, assigned by Amazon FSx.
        :param security_group: The security group of the file system.

        :exampleMetadata: infused

        Example::

            sg = ec2.SecurityGroup.from_security_group_id(self, "FsxSecurityGroup", "{SECURITY-GROUP-ID}")
            fs = fsx.LustreFileSystem.from_lustre_file_system_attributes(self, "FsxLustreFileSystem",
                dns_name="{FILE-SYSTEM-DNS-NAME}",
                file_system_id="{FILE-SYSTEM-ID}",
                security_group=sg
            )
            
            vpc = ec2.Vpc.from_vpc_attributes(self, "Vpc",
                availability_zones=["us-west-2a", "us-west-2b"],
                public_subnet_ids=["{US-WEST-2A-SUBNET-ID}", "{US-WEST-2B-SUBNET-ID}"],
                vpc_id="{VPC-ID}"
            )
            
            inst = ec2.Instance(self, "inst",
                instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.LARGE),
                machine_image=ec2.AmazonLinuxImage(
                    generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
                ),
                vpc=vpc,
                vpc_subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PUBLIC
                )
            )
            
            fs.connections.allow_default_port_from(inst)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FileSystemAttributes.__init__)
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns_name": dns_name,
            "file_system_id": file_system_id,
            "security_group": security_group,
        }

    @builtins.property
    def dns_name(self) -> builtins.str:
        '''The DNS name assigned to this file system.'''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system, assigned by Amazon FSx.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group(self) -> _ISecurityGroup_acf8a799:
        '''The security group of the file system.'''
        result = self._values.get("security_group")
        assert result is not None, "Required property 'security_group' is missing"
        return typing.cast(_ISecurityGroup_acf8a799, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.FileSystemProps",
    jsii_struct_bases=[],
    name_mapping={
        "storage_capacity_gib": "storageCapacityGiB",
        "vpc": "vpc",
        "backup_id": "backupId",
        "kms_key": "kmsKey",
        "removal_policy": "removalPolicy",
        "security_group": "securityGroup",
    },
)
class FileSystemProps:
    def __init__(
        self,
        *,
        storage_capacity_gib: jsii.Number,
        vpc: _IVpc_f30d5663,
        backup_id: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    ) -> None:
        '''Properties for the FSx file system.

        :param storage_capacity_gib: The storage capacity of the file system being created. For Windows file systems, valid values are 32 GiB to 65,536 GiB. For SCRATCH_1 deployment types, valid values are 1,200, 2,400, 3,600, then continuing in increments of 3,600 GiB. For SCRATCH_2 and PERSISTENT_1 types, valid values are 1,200, 2,400, then continuing in increments of 2,400 GiB.
        :param vpc: The VPC to launch the file system in.
        :param backup_id: The ID of the backup. Specifies the backup to use if you're creating a file system from an existing backup. Default: - no backup will be used.
        :param kms_key: The KMS key used for encryption to protect your data at rest. Default: - the aws/fsx default KMS key for the AWS account being deployed into.
        :param removal_policy: Policy to apply when the file system is removed from the stack. Default: RemovalPolicy.RETAIN
        :param security_group: Security Group to assign to this file system. Default: - creates new security group which allows all outbound traffic.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_ec2 as ec2
            from aws_cdk import aws_fsx as fsx
            from aws_cdk import aws_kms as kms
            
            # key: kms.Key
            # security_group: ec2.SecurityGroup
            # vpc: ec2.Vpc
            
            file_system_props = fsx.FileSystemProps(
                storage_capacity_gi_b=123,
                vpc=vpc,
            
                # the properties below are optional
                backup_id="backupId",
                kms_key=key,
                removal_policy=cdk.RemovalPolicy.DESTROY,
                security_group=security_group
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FileSystemProps.__init__)
            check_type(argname="argument storage_capacity_gib", value=storage_capacity_gib, expected_type=type_hints["storage_capacity_gib"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument backup_id", value=backup_id, expected_type=type_hints["backup_id"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage_capacity_gib": storage_capacity_gib,
            "vpc": vpc,
        }
        if backup_id is not None:
            self._values["backup_id"] = backup_id
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_group is not None:
            self._values["security_group"] = security_group

    @builtins.property
    def storage_capacity_gib(self) -> jsii.Number:
        '''The storage capacity of the file system being created.

        For Windows file systems, valid values are 32 GiB to 65,536 GiB.
        For SCRATCH_1 deployment types, valid values are 1,200, 2,400, 3,600, then continuing in increments of 3,600 GiB.
        For SCRATCH_2 and PERSISTENT_1 types, valid values are 1,200, 2,400, then continuing in increments of 2,400 GiB.
        '''
        result = self._values.get("storage_capacity_gib")
        assert result is not None, "Required property 'storage_capacity_gib' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vpc(self) -> _IVpc_f30d5663:
        '''The VPC to launch the file system in.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_IVpc_f30d5663, result)

    @builtins.property
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the backup.

        Specifies the backup to use if you're creating a file system from an existing backup.

        :default: - no backup will be used.
        '''
        result = self._values.get("backup_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS key used for encryption to protect your data at rest.

        :default: - the aws/fsx default KMS key for the AWS account being deployed into.
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Policy to apply when the file system is removed from the stack.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_acf8a799]:
        '''Security Group to assign to this file system.

        :default: - creates new security group which allows all outbound traffic.
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[_ISecurityGroup_acf8a799], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_fsx.IFileSystem")
class IFileSystem(_IConnectable_10015a05, typing_extensions.Protocol):
    '''Interface to implement FSx File Systems.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system, assigned by Amazon FSx.

        :attribute: true
        '''
        ...


class _IFileSystemProxy(
    jsii.proxy_for(_IConnectable_10015a05) # type: ignore[misc]
):
    '''Interface to implement FSx File Systems.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_fsx.IFileSystem"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system, assigned by Amazon FSx.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFileSystem).__jsii_proxy_class__ = lambda : _IFileSystemProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_fsx.LustreAutoImportPolicy")
class LustreAutoImportPolicy(enum.Enum):
    '''The different auto import policies which are allowed.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # vpc: ec2.Vpc
        # bucket: s3.Bucket
        
        
        lustre_configuration = {
            "deployment_type": fsx.LustreDeploymentType.SCRATCH_2,
            "export_path": bucket.s3_url_for_object(),
            "import_path": bucket.s3_url_for_object(),
            "auto_import_policy": fsx.LustreAutoImportPolicy.NEW_CHANGED_DELETED
        }
        
        fs = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
            vpc=vpc,
            vpc_subnet=vpc.private_subnets[0],
            storage_capacity_gi_b=1200,
            lustre_configuration=lustre_configuration
        )
    '''

    NONE = "NONE"
    '''AutoImport is off.

    Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
    '''
    NEW = "NEW"
    '''AutoImport is on.

    Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system.
    '''
    NEW_CHANGED = "NEW_CHANGED"
    '''AutoImport is on.

    Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
    '''
    NEW_CHANGED_DELETED = "NEW_CHANGED_DELETED"
    '''AutoImport is on.

    Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.LustreConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_type": "deploymentType",
        "auto_import_policy": "autoImportPolicy",
        "data_compression_type": "dataCompressionType",
        "export_path": "exportPath",
        "imported_file_chunk_size_mib": "importedFileChunkSizeMiB",
        "import_path": "importPath",
        "per_unit_storage_throughput": "perUnitStorageThroughput",
        "weekly_maintenance_start_time": "weeklyMaintenanceStartTime",
    },
)
class LustreConfiguration:
    def __init__(
        self,
        *,
        deployment_type: "LustreDeploymentType",
        auto_import_policy: typing.Optional[LustreAutoImportPolicy] = None,
        data_compression_type: typing.Optional["LustreDataCompressionType"] = None,
        export_path: typing.Optional[builtins.str] = None,
        imported_file_chunk_size_mib: typing.Optional[jsii.Number] = None,
        import_path: typing.Optional[builtins.str] = None,
        per_unit_storage_throughput: typing.Optional[jsii.Number] = None,
        weekly_maintenance_start_time: typing.Optional["LustreMaintenanceTime"] = None,
    ) -> None:
        '''The configuration for the Amazon FSx for Lustre file system.

        :param deployment_type: The type of backing file system deployment used by FSx.
        :param auto_import_policy: Available with ``Scratch`` and ``Persistent_1`` deployment types. When you create your file system, your existing S3 objects appear as file and directory listings. Use this property to choose how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. ``AutoImportPolicy`` can have the following values: For more information, see `Automatically import updates from your S3 bucket <https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoimport-data-repo.html>`_ . .. epigraph:: This parameter is not supported for Lustre file systems using the ``Persistent_2`` deployment type. Default: - no import policy
        :param data_compression_type: Sets the data compression configuration for the file system. For more information, see `Lustre data compression <https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html>`_ in the *Amazon FSx for Lustre User Guide* . Default: - no compression
        :param export_path: The path in Amazon S3 where the root of your Amazon FSx file system is exported. The path must use the same Amazon S3 bucket as specified in ImportPath. If you only specify a bucket name, such as s3://import-bucket, you get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is overwritten on export. If you provide a custom prefix in the export path, such as s3://import-bucket/[custom-optional-prefix], Amazon FSx exports the contents of your file system to that export prefix in the Amazon S3 bucket. Default: s3://import-bucket/FSxLustre[creation-timestamp]
        :param imported_file_chunk_size_mib: For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. Allowed values are between 1 and 512,000. Default: 1024
        :param import_path: The path to the Amazon S3 bucket (including the optional prefix) that you're using as the data repository for your Amazon FSx for Lustre file system. Must be of the format "s3://{bucketName}/optional-prefix" and cannot exceed 900 characters. Default: - no bucket is imported
        :param per_unit_storage_throughput: Required for the PERSISTENT_1 deployment type, describes the amount of read and write throughput for each 1 tebibyte of storage, in MB/s/TiB. Valid values are 50, 100, 200. Default: - no default, conditionally required for PERSISTENT_1 deployment type
        :param weekly_maintenance_start_time: The preferred day and time to perform weekly maintenance. The first digit is the day of the week, starting at 1 for Monday, then the following are hours and minutes in the UTC time zone, 24 hour clock. For example: '2:20:30' is Tuesdays at 20:30. Default: - no preference

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html
        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # vpc: ec2.Vpc
            # bucket: s3.Bucket
            
            
            lustre_configuration = {
                "deployment_type": fsx.LustreDeploymentType.SCRATCH_2,
                "export_path": bucket.s3_url_for_object(),
                "import_path": bucket.s3_url_for_object(),
                "auto_import_policy": fsx.LustreAutoImportPolicy.NEW_CHANGED_DELETED
            }
            
            fs = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
                vpc=vpc,
                vpc_subnet=vpc.private_subnets[0],
                storage_capacity_gi_b=1200,
                lustre_configuration=lustre_configuration
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LustreConfiguration.__init__)
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
            check_type(argname="argument auto_import_policy", value=auto_import_policy, expected_type=type_hints["auto_import_policy"])
            check_type(argname="argument data_compression_type", value=data_compression_type, expected_type=type_hints["data_compression_type"])
            check_type(argname="argument export_path", value=export_path, expected_type=type_hints["export_path"])
            check_type(argname="argument imported_file_chunk_size_mib", value=imported_file_chunk_size_mib, expected_type=type_hints["imported_file_chunk_size_mib"])
            check_type(argname="argument import_path", value=import_path, expected_type=type_hints["import_path"])
            check_type(argname="argument per_unit_storage_throughput", value=per_unit_storage_throughput, expected_type=type_hints["per_unit_storage_throughput"])
            check_type(argname="argument weekly_maintenance_start_time", value=weekly_maintenance_start_time, expected_type=type_hints["weekly_maintenance_start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "deployment_type": deployment_type,
        }
        if auto_import_policy is not None:
            self._values["auto_import_policy"] = auto_import_policy
        if data_compression_type is not None:
            self._values["data_compression_type"] = data_compression_type
        if export_path is not None:
            self._values["export_path"] = export_path
        if imported_file_chunk_size_mib is not None:
            self._values["imported_file_chunk_size_mib"] = imported_file_chunk_size_mib
        if import_path is not None:
            self._values["import_path"] = import_path
        if per_unit_storage_throughput is not None:
            self._values["per_unit_storage_throughput"] = per_unit_storage_throughput
        if weekly_maintenance_start_time is not None:
            self._values["weekly_maintenance_start_time"] = weekly_maintenance_start_time

    @builtins.property
    def deployment_type(self) -> "LustreDeploymentType":
        '''The type of backing file system deployment used by FSx.'''
        result = self._values.get("deployment_type")
        assert result is not None, "Required property 'deployment_type' is missing"
        return typing.cast("LustreDeploymentType", result)

    @builtins.property
    def auto_import_policy(self) -> typing.Optional[LustreAutoImportPolicy]:
        '''Available with ``Scratch`` and ``Persistent_1`` deployment types.

        When you create your file system, your existing S3 objects appear as file and directory listings. Use this property to choose how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. ``AutoImportPolicy`` can have the following values:

        For more information, see `Automatically import updates from your S3 bucket <https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoimport-data-repo.html>`_ .
        .. epigraph::

           This parameter is not supported for Lustre file systems using the ``Persistent_2`` deployment type.

        :default: - no import policy

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-autoimportpolicy
        '''
        result = self._values.get("auto_import_policy")
        return typing.cast(typing.Optional[LustreAutoImportPolicy], result)

    @builtins.property
    def data_compression_type(self) -> typing.Optional["LustreDataCompressionType"]:
        '''Sets the data compression configuration for the file system.

        For more information, see `Lustre data compression <https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html>`_ in the *Amazon FSx for Lustre User Guide* .

        :default: - no compression

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-datacompressiontype
        '''
        result = self._values.get("data_compression_type")
        return typing.cast(typing.Optional["LustreDataCompressionType"], result)

    @builtins.property
    def export_path(self) -> typing.Optional[builtins.str]:
        '''The path in Amazon S3 where the root of your Amazon FSx file system is exported.

        The path must use the same
        Amazon S3 bucket as specified in ImportPath. If you only specify a bucket name, such as s3://import-bucket, you
        get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is
        overwritten on export. If you provide a custom prefix in the export path, such as
        s3://import-bucket/[custom-optional-prefix], Amazon FSx exports the contents of your file system to that export
        prefix in the Amazon S3 bucket.

        :default: s3://import-bucket/FSxLustre[creation-timestamp]
        '''
        result = self._values.get("export_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def imported_file_chunk_size_mib(self) -> typing.Optional[jsii.Number]:
        '''For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk.

        Allowed values are between 1 and 512,000.

        :default: 1024
        '''
        result = self._values.get("imported_file_chunk_size_mib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def import_path(self) -> typing.Optional[builtins.str]:
        '''The path to the Amazon S3 bucket (including the optional prefix) that you're using as the data repository for your Amazon FSx for Lustre file system.

        Must be of the format "s3://{bucketName}/optional-prefix" and cannot
        exceed 900 characters.

        :default: - no bucket is imported
        '''
        result = self._values.get("import_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def per_unit_storage_throughput(self) -> typing.Optional[jsii.Number]:
        '''Required for the PERSISTENT_1 deployment type, describes the amount of read and write throughput for each 1 tebibyte of storage, in MB/s/TiB.

        Valid values are 50, 100, 200.

        :default: - no default, conditionally required for PERSISTENT_1 deployment type
        '''
        result = self._values.get("per_unit_storage_throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weekly_maintenance_start_time(self) -> typing.Optional["LustreMaintenanceTime"]:
        '''The preferred day and time to perform weekly maintenance.

        The first digit is the day of the week, starting at 1
        for Monday, then the following are hours and minutes in the UTC time zone, 24 hour clock. For example: '2:20:30'
        is Tuesdays at 20:30.

        :default: - no preference
        '''
        result = self._values.get("weekly_maintenance_start_time")
        return typing.cast(typing.Optional["LustreMaintenanceTime"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LustreConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_fsx.LustreDataCompressionType")
class LustreDataCompressionType(enum.Enum):
    '''The permitted Lustre data compression algorithms.

    :exampleMetadata: infused

    Example::

        lustre_configuration = {
            # ...
            "data_compression_type": fsx.LustreDataCompressionType.LZ4
        }
    '''

    NONE = "NONE"
    '''``NONE`` - (Default) Data compression is turned off when the file system is created.'''
    LZ4 = "LZ4"
    '''``LZ4`` - Data compression is turned on with the LZ4 algorithm.

    Note: When you turn data compression on for an existing file system, only newly written files are compressed. Existing files are not compressed.
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_fsx.LustreDeploymentType")
class LustreDeploymentType(enum.Enum):
    '''The different kinds of file system deployments used by Lustre.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # vpc: ec2.Vpc
        # bucket: s3.Bucket
        
        
        lustre_configuration = {
            "deployment_type": fsx.LustreDeploymentType.SCRATCH_2,
            "export_path": bucket.s3_url_for_object(),
            "import_path": bucket.s3_url_for_object(),
            "auto_import_policy": fsx.LustreAutoImportPolicy.NEW_CHANGED_DELETED
        }
        
        fs = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
            vpc=vpc,
            vpc_subnet=vpc.private_subnets[0],
            storage_capacity_gi_b=1200,
            lustre_configuration=lustre_configuration
        )
    '''

    SCRATCH_1 = "SCRATCH_1"
    '''Original type for shorter term data processing.

    Data is not replicated and does not persist on server fail.
    '''
    SCRATCH_2 = "SCRATCH_2"
    '''Newer type for shorter term data processing.

    Data is not replicated and does not persist on server fail.
    Provides better support for spiky workloads.
    '''
    PERSISTENT_1 = "PERSISTENT_1"
    '''Long term storage.

    Data is replicated and file servers are replaced if they fail.
    '''
    PERSISTENT_2 = "PERSISTENT_2"
    '''Newer type of long term storage with higher throughput tiers.

    Data is replicated and file servers are replaced if they fail.
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.LustreFileSystemProps",
    jsii_struct_bases=[FileSystemProps],
    name_mapping={
        "storage_capacity_gib": "storageCapacityGiB",
        "vpc": "vpc",
        "backup_id": "backupId",
        "kms_key": "kmsKey",
        "removal_policy": "removalPolicy",
        "security_group": "securityGroup",
        "lustre_configuration": "lustreConfiguration",
        "vpc_subnet": "vpcSubnet",
    },
)
class LustreFileSystemProps(FileSystemProps):
    def __init__(
        self,
        *,
        storage_capacity_gib: jsii.Number,
        vpc: _IVpc_f30d5663,
        backup_id: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
        lustre_configuration: typing.Union[LustreConfiguration, typing.Dict[str, typing.Any]],
        vpc_subnet: _ISubnet_d57d1229,
    ) -> None:
        '''Properties specific to the Lustre version of the FSx file system.

        :param storage_capacity_gib: The storage capacity of the file system being created. For Windows file systems, valid values are 32 GiB to 65,536 GiB. For SCRATCH_1 deployment types, valid values are 1,200, 2,400, 3,600, then continuing in increments of 3,600 GiB. For SCRATCH_2 and PERSISTENT_1 types, valid values are 1,200, 2,400, then continuing in increments of 2,400 GiB.
        :param vpc: The VPC to launch the file system in.
        :param backup_id: The ID of the backup. Specifies the backup to use if you're creating a file system from an existing backup. Default: - no backup will be used.
        :param kms_key: The KMS key used for encryption to protect your data at rest. Default: - the aws/fsx default KMS key for the AWS account being deployed into.
        :param removal_policy: Policy to apply when the file system is removed from the stack. Default: RemovalPolicy.RETAIN
        :param security_group: Security Group to assign to this file system. Default: - creates new security group which allows all outbound traffic.
        :param lustre_configuration: Additional configuration for FSx specific to Lustre.
        :param vpc_subnet: The subnet that the file system will be accessible from.

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # vpc: ec2.Vpc
            # bucket: s3.Bucket
            
            
            lustre_configuration = {
                "deployment_type": fsx.LustreDeploymentType.SCRATCH_2,
                "export_path": bucket.s3_url_for_object(),
                "import_path": bucket.s3_url_for_object(),
                "auto_import_policy": fsx.LustreAutoImportPolicy.NEW_CHANGED_DELETED
            }
            
            fs = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
                vpc=vpc,
                vpc_subnet=vpc.private_subnets[0],
                storage_capacity_gi_b=1200,
                lustre_configuration=lustre_configuration
            )
        '''
        if isinstance(lustre_configuration, dict):
            lustre_configuration = LustreConfiguration(**lustre_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(LustreFileSystemProps.__init__)
            check_type(argname="argument storage_capacity_gib", value=storage_capacity_gib, expected_type=type_hints["storage_capacity_gib"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument backup_id", value=backup_id, expected_type=type_hints["backup_id"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument lustre_configuration", value=lustre_configuration, expected_type=type_hints["lustre_configuration"])
            check_type(argname="argument vpc_subnet", value=vpc_subnet, expected_type=type_hints["vpc_subnet"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage_capacity_gib": storage_capacity_gib,
            "vpc": vpc,
            "lustre_configuration": lustre_configuration,
            "vpc_subnet": vpc_subnet,
        }
        if backup_id is not None:
            self._values["backup_id"] = backup_id
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_group is not None:
            self._values["security_group"] = security_group

    @builtins.property
    def storage_capacity_gib(self) -> jsii.Number:
        '''The storage capacity of the file system being created.

        For Windows file systems, valid values are 32 GiB to 65,536 GiB.
        For SCRATCH_1 deployment types, valid values are 1,200, 2,400, 3,600, then continuing in increments of 3,600 GiB.
        For SCRATCH_2 and PERSISTENT_1 types, valid values are 1,200, 2,400, then continuing in increments of 2,400 GiB.
        '''
        result = self._values.get("storage_capacity_gib")
        assert result is not None, "Required property 'storage_capacity_gib' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vpc(self) -> _IVpc_f30d5663:
        '''The VPC to launch the file system in.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_IVpc_f30d5663, result)

    @builtins.property
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the backup.

        Specifies the backup to use if you're creating a file system from an existing backup.

        :default: - no backup will be used.
        '''
        result = self._values.get("backup_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS key used for encryption to protect your data at rest.

        :default: - the aws/fsx default KMS key for the AWS account being deployed into.
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Policy to apply when the file system is removed from the stack.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_acf8a799]:
        '''Security Group to assign to this file system.

        :default: - creates new security group which allows all outbound traffic.
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[_ISecurityGroup_acf8a799], result)

    @builtins.property
    def lustre_configuration(self) -> LustreConfiguration:
        '''Additional configuration for FSx specific to Lustre.'''
        result = self._values.get("lustre_configuration")
        assert result is not None, "Required property 'lustre_configuration' is missing"
        return typing.cast(LustreConfiguration, result)

    @builtins.property
    def vpc_subnet(self) -> _ISubnet_d57d1229:
        '''The subnet that the file system will be accessible from.'''
        result = self._values.get("vpc_subnet")
        assert result is not None, "Required property 'vpc_subnet' is missing"
        return typing.cast(_ISubnet_d57d1229, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LustreFileSystemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LustreMaintenanceTime(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fsx.LustreMaintenanceTime",
):
    '''Class for scheduling a weekly manitenance time.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fsx as fsx
        
        lustre_maintenance_time = fsx.LustreMaintenanceTime(
            day=fsx.Weekday.MONDAY,
            hour=123,
            minute=123
        )
    '''

    def __init__(
        self,
        *,
        day: "Weekday",
        hour: jsii.Number,
        minute: jsii.Number,
    ) -> None:
        '''
        :param day: The day of the week for maintenance to be performed.
        :param hour: The hour of the day (from 0-24) for maintenance to be performed.
        :param minute: The minute of the hour (from 0-59) for maintenance to be performed.
        '''
        props = LustreMaintenanceTimeProps(day=day, hour=hour, minute=minute)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toTimestamp")
    def to_timestamp(self) -> builtins.str:
        '''Converts a day, hour, and minute into a timestamp as used by FSx for Lustre's weeklyMaintenanceStartTime field.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toTimestamp", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fsx.LustreMaintenanceTimeProps",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "hour": "hour", "minute": "minute"},
)
class LustreMaintenanceTimeProps:
    def __init__(
        self,
        *,
        day: "Weekday",
        hour: jsii.Number,
        minute: jsii.Number,
    ) -> None:
        '''Properties required for setting up a weekly maintenance time.

        :param day: The day of the week for maintenance to be performed.
        :param hour: The hour of the day (from 0-24) for maintenance to be performed.
        :param minute: The minute of the hour (from 0-59) for maintenance to be performed.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fsx as fsx
            
            lustre_maintenance_time_props = fsx.LustreMaintenanceTimeProps(
                day=fsx.Weekday.MONDAY,
                hour=123,
                minute=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LustreMaintenanceTimeProps.__init__)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
        self._values: typing.Dict[str, typing.Any] = {
            "day": day,
            "hour": hour,
            "minute": minute,
        }

    @builtins.property
    def day(self) -> "Weekday":
        '''The day of the week for maintenance to be performed.'''
        result = self._values.get("day")
        assert result is not None, "Required property 'day' is missing"
        return typing.cast("Weekday", result)

    @builtins.property
    def hour(self) -> jsii.Number:
        '''The hour of the day (from 0-24) for maintenance to be performed.'''
        result = self._values.get("hour")
        assert result is not None, "Required property 'hour' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minute(self) -> jsii.Number:
        '''The minute of the hour (from 0-59) for maintenance to be performed.'''
        result = self._values.get("minute")
        assert result is not None, "Required property 'minute' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LustreMaintenanceTimeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_fsx.Weekday")
class Weekday(enum.Enum):
    '''Enum for representing all the days of the week.'''

    MONDAY = "MONDAY"
    '''Monday.'''
    TUESDAY = "TUESDAY"
    '''Tuesday.'''
    WEDNESDAY = "WEDNESDAY"
    '''Wednesday.'''
    THURSDAY = "THURSDAY"
    '''Thursday.'''
    FRIDAY = "FRIDAY"
    '''Friday.'''
    SATURDAY = "SATURDAY"
    '''Saturday.'''
    SUNDAY = "SUNDAY"
    '''Sunday.'''


@jsii.implements(IFileSystem)
class FileSystemBase(
    _Resource_45bc6135,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_fsx.FileSystemBase",
):
    '''A new or imported FSx file system.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FileSystemBase.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _ResourceProps_15a65b4e(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connections")
    @abc.abstractmethod
    def connections(self) -> _Connections_0f31fce8:
        '''The security groups/rules used to allow network connections to the file system.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    @abc.abstractmethod
    def dns_name(self) -> builtins.str:
        '''The DNS name assigned to this file system.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileSystemId")
    @abc.abstractmethod
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system, assigned by Amazon FSx.

        :attribute: true
        '''
        ...


class _FileSystemBaseProxy(
    FileSystemBase, jsii.proxy_for(_Resource_45bc6135) # type: ignore[misc]
):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_0f31fce8:
        '''The security groups/rules used to allow network connections to the file system.

        :attribute: true
        '''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''The DNS name assigned to this file system.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system, assigned by Amazon FSx.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, FileSystemBase).__jsii_proxy_class__ = lambda : _FileSystemBaseProxy


class LustreFileSystem(
    FileSystemBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fsx.LustreFileSystem",
):
    '''The FSx for Lustre File System implementation of IFileSystem.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html
    :exampleMetadata: infused
    :resource: AWS::FSx::FileSystem

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # vpc: ec2.Vpc
        # bucket: s3.Bucket
        
        
        lustre_configuration = {
            "deployment_type": fsx.LustreDeploymentType.SCRATCH_2,
            "export_path": bucket.s3_url_for_object(),
            "import_path": bucket.s3_url_for_object(),
            "auto_import_policy": fsx.LustreAutoImportPolicy.NEW_CHANGED_DELETED
        }
        
        fs = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
            vpc=vpc,
            vpc_subnet=vpc.private_subnets[0],
            storage_capacity_gi_b=1200,
            lustre_configuration=lustre_configuration
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        lustre_configuration: typing.Union[LustreConfiguration, typing.Dict[str, typing.Any]],
        vpc_subnet: _ISubnet_d57d1229,
        storage_capacity_gib: jsii.Number,
        vpc: _IVpc_f30d5663,
        backup_id: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param lustre_configuration: Additional configuration for FSx specific to Lustre.
        :param vpc_subnet: The subnet that the file system will be accessible from.
        :param storage_capacity_gib: The storage capacity of the file system being created. For Windows file systems, valid values are 32 GiB to 65,536 GiB. For SCRATCH_1 deployment types, valid values are 1,200, 2,400, 3,600, then continuing in increments of 3,600 GiB. For SCRATCH_2 and PERSISTENT_1 types, valid values are 1,200, 2,400, then continuing in increments of 2,400 GiB.
        :param vpc: The VPC to launch the file system in.
        :param backup_id: The ID of the backup. Specifies the backup to use if you're creating a file system from an existing backup. Default: - no backup will be used.
        :param kms_key: The KMS key used for encryption to protect your data at rest. Default: - the aws/fsx default KMS key for the AWS account being deployed into.
        :param removal_policy: Policy to apply when the file system is removed from the stack. Default: RemovalPolicy.RETAIN
        :param security_group: Security Group to assign to this file system. Default: - creates new security group which allows all outbound traffic.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LustreFileSystem.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LustreFileSystemProps(
            lustre_configuration=lustre_configuration,
            vpc_subnet=vpc_subnet,
            storage_capacity_gib=storage_capacity_gib,
            vpc=vpc,
            backup_id=backup_id,
            kms_key=kms_key,
            removal_policy=removal_policy,
            security_group=security_group,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromLustreFileSystemAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_lustre_file_system_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dns_name: builtins.str,
        file_system_id: builtins.str,
        security_group: _ISecurityGroup_acf8a799,
    ) -> IFileSystem:
        '''Import an existing FSx for Lustre file system from the given properties.

        :param scope: -
        :param id: -
        :param dns_name: The DNS name assigned to this file system.
        :param file_system_id: The ID of the file system, assigned by Amazon FSx.
        :param security_group: The security group of the file system.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LustreFileSystem.from_lustre_file_system_attributes)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = FileSystemAttributes(
            dns_name=dns_name,
            file_system_id=file_system_id,
            security_group=security_group,
        )

        return typing.cast(IFileSystem, jsii.sinvoke(cls, "fromLustreFileSystemAttributes", [scope, id, attrs]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_0f31fce8:
        '''The security groups/rules used to allow network connections to the file system.'''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''The DNS name assigned to this file system.'''
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID that AWS assigns to the file system.'''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mountName")
    def mount_name(self) -> builtins.str:
        '''The mount name of the file system, generated by FSx.

        :attribute: LustreMountName
        '''
        return typing.cast(builtins.str, jsii.get(self, "mountName"))


__all__ = [
    "CfnFileSystem",
    "CfnFileSystemProps",
    "CfnSnapshot",
    "CfnSnapshotProps",
    "CfnStorageVirtualMachine",
    "CfnStorageVirtualMachineProps",
    "CfnVolume",
    "CfnVolumeProps",
    "FileSystemAttributes",
    "FileSystemBase",
    "FileSystemProps",
    "IFileSystem",
    "LustreAutoImportPolicy",
    "LustreConfiguration",
    "LustreDataCompressionType",
    "LustreDeploymentType",
    "LustreFileSystem",
    "LustreFileSystemProps",
    "LustreMaintenanceTime",
    "LustreMaintenanceTimeProps",
    "Weekday",
]

publication.publish()
