from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    Aws,
    aws_ec2 as _ec2,
    aws_iam as _iam,
    aws_redshift as _redshift,
    aws_secretsmanager as _sm,
    aws_redshiftserverless as _rs,
)

from constructs import Construct

class RedshiftStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, ingestion_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        environment = self.node.try_get_context('environment')
        redshift_config = self.node.try_get_context(f'{environment}_redshift_config')

        vpc = _ec2.Vpc(
            self,
            "VpcId",
            max_azs=redshift_config['max_azs']
        )

        # Create new security group to be used by redshift
        rs_security_group = _ec2.SecurityGroup(
            self,
            "redshiftSecurityGroup",
            vpc=vpc
        )

        rs_role = _iam.Role(
            self, "redshiftClusterRole",
            assumed_by=_iam.ServicePrincipal(
                "redshift.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftAllCommandsFullAccess"
                )
            ]
        )

        order_stream = ingestion_stack.get_order_stream
        order_stream.grant_read_write(rs_role)
        
        self.rs_namespace = _rs.CfnNamespace(
            self,
            "redshiftServerlessNamespace",
            namespace_name="ns-streaming",
            default_iam_role_arn=rs_role.role_arn,
            iam_roles=[rs_role.role_arn]
        )

        self.rs_workgroup = _rs.CfnWorkgroup(
            self,
            "redshiftServerlessWorkgroup",
            workgroup_name="wg-streaming",
            base_capacity=32,
            namespace_name=self.rs_namespace.ref,
            security_group_ids=[rs_security_group.security_group_id],
            subnet_ids=vpc.select_subnets(
                subnet_type=_ec2.SubnetType.PRIVATE_WITH_NAT
            ).subnet_ids,
        )

