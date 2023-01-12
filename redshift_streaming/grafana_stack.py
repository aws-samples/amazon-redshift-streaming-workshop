from aws_cdk import (
    Stack,
    CfnOutput,
    CfnTag,
    RemovalPolicy,
    Aws,
    aws_grafana as _grafana,
    aws_iam as _iam,
)

from constructs import Construct


class GrafanaStack(Stack):
    def __init__(self,
                scope: Construct,
                construct_id: str,
                **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cfn_workspace = _grafana.CfnWorkspace(
            self, 
            "MyCfnWorkspace",
            permission_type='SERVICE_MANAGED',
            authentication_providers=['AWS_SSO'],
            account_access_type='CURRENT_ACCOUNT',
            data_sources=['REDSHIFT'],
            notification_destinations=['SNS']
        )