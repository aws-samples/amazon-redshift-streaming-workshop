from aws_cdk import (
    Stack,
    aws_iam as _iam,
)


from constructs import Construct

from pathlib import Path

class InitStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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

    @property
    def get_rs_role(self):
        return self.rs_role 
