from aws_cdk import (
    Stack,
    aws_iam as _iam,
    aws_kinesis as _kinesis,
    aws_s3 as _s3,
    RemovalPolicy,
    Duration,
)


from constructs import Construct

from pathlib import Path

class InitStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        environment = self.node.try_get_context('environment')
        kinesis_config = self.node.try_get_context(f'{environment}_kinesis_config')

        self.rs_role = _iam.Role(
            self, "redshiftClusterRole",
            assumed_by=_iam.ServicePrincipal(
                "redshift.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftAllCommandsFullAccess"
                )
            ]
        )

        _iam.ManagedPolicy(
            self,
            "spectrum_lake_formation_policy",
            description="Provide access between Redshift Spectrum and Lake Formation",
            statements=[
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=[
                        "glue:CreateDatabase",
                        "glue:DeleteDatabase",
                        "glue:GetDatabase",
                        "glue:GetDatabases",
                        "glue:UpdateDatabase",
                        "glue:CreateTable",
                        "glue:DeleteTable",
                        "glue:BatchDeleteTable",
                        "glue:UpdateTable",
                        "glue:GetTable",
                        "glue:GetTables",
                        "glue:BatchCreatePartition",
                        "glue:CreatePartition",
                        "glue:DeletePartition",
                        "glue:BatchDeletePartition",
                        "glue:UpdatePartition",
                        "glue:GetPartition",
                        "glue:GetPartitions",
                        "glue:BatchGetPartition",
                        "lakeformation:GetDataAccess",
                    ],
                    resources=["*"],
                )
            ],
            roles=[self.rs_role],
        )


        self.s3_bucket_raw = _s3.Bucket(
            self,
            "s3_raw",
            encryption=_s3.BucketEncryption.S3_MANAGED,
            public_read_access=False,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        self.order_stream = _kinesis.Stream(
            self,
            "order-stream",
            stream_name="order_stream",
            retention_period=Duration.hours(kinesis_config['retention_period']),
            stream_mode=_kinesis.StreamMode.ON_DEMAND,
            encryption=_kinesis.StreamEncryption.UNENCRYPTED
        )

        self.s3_bucket_raw.grant_read_write(self.rs_role)
        self.order_stream.grant_read(self.rs_role)

    @property
    def get_rs_role(self):
        return self.rs_role 

    @property
    def get_s3_bucket_raw(self):
        return self.s3_bucket_raw 
    
    @property
    def get_order_stream(self):
        return self.order_stream
