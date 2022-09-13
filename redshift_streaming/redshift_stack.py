
from aws_cdk import (
    Stack,
    aws_ec2 as _ec2,
    aws_iam as _iam,
    aws_redshift as _redshift,
    aws_secretsmanager as _sm,
    aws_redshiftserverless as _rs,
    aws_sagemaker as _sg,
    aws_lambda as _lambda,
    Duration,
    aws_events as _events,
    aws_events_targets as _events_targets,
)

from constructs import Construct

class RedshiftStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        environment = self.node.try_get_context('environment')
        redshift_config = self.node.try_get_context(f'{environment}_redshift_config')
        sagemaker_config = self.node.try_get_context(f'{environment}_sagemaker_config')



        vpc = _ec2.Vpc.from_lookup(
            self,
            "VpcId",
            is_default=True
        )

        rs_security_group = _ec2.SecurityGroup.from_lookup_by_name(
            self,
            "redshiftSecurityGroup",
            security_group_name=redshift_config['security_group_name'],
            vpc=vpc
        )

        sg_security_group = _ec2.SecurityGroup(
            self,
            "sagemakerSecurityGroup",
            vpc=vpc
        )

        rs_security_group.add_ingress_rule(sg_security_group, _ec2.Port.tcp(5439))
        rs_security_group.add_ingress_rule(rs_security_group, _ec2.Port.tcp(5439))
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4(f"{redshift_config['quicksight_ip']}"), 
            _ec2.Port.tcp(5439)
        )

        lambda_layer = _lambda.LayerVersion(self, 
            'refreshmv-lambda-layer',
            code = _lambda.AssetCode('lambda/layer/python.zip'),
            compatible_runtimes = [_lambda.Runtime.PYTHON_3_8],
        )

        refreshmv_lambda = _lambda.Function(
            self, 'refreshmv-lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='refreshmv-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.AssetCode('./lambda/code/refreshmv'),
            handler='refreshmv.lambda_handler',
            layers = [lambda_layer],
            environment={
                "WORKGROUP_NAME" : redshift_config['workgroup_name'],
                "DB_NAME" : redshift_config['db_name'],
                "REFRESHMV" : redshift_config['refreshmv'],
                "SECRET_NAME": redshift_config['secret_name']

            },
            timeout=Duration.seconds(60),
            reserved_concurrent_executions=1,
        )

        refreshmv_lambda.add_to_role_policy(
            statement=_iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["redshift-data:*", "secretsmanager:*"],
                resources=["*"],
            )
        )

        step_trigger = _events.Rule(
            self, 'refreshmv-StepTrigger',
            schedule=_events.Schedule.rate(Duration.seconds(60))
        )

        step_trigger.add_target(
            _events_targets.LambdaFunction(refreshmv_lambda)
        )


        sg_role = _iam.Role(
            self, "sagemakerRole",
            assumed_by=_iam.ServicePrincipal(
                "sagemaker.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSageMakerFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftDataFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "SecretsManagerReadWrite"
                ),
            ]
        )

        cfn_notebook_instance_lifecycle_config = _sg.CfnNotebookInstanceLifecycleConfig(
            self, 
            "sagemakerLifecycleConfig",
            notebook_instance_lifecycle_config_name=sagemaker_config['lifecycle_config_name'],
            on_create=[_sg.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty(
                content=sagemaker_config['content']
            )]
        )

        cfn_notebook_instance = _sg.CfnNotebookInstance(
            self, 
            "sagemakerNotebook",
            instance_type=sagemaker_config['instance_type'],
            role_arn=sg_role.role_arn,
            lifecycle_config_name=cfn_notebook_instance_lifecycle_config.notebook_instance_lifecycle_config_name,
            platform_identifier=sagemaker_config['platform_identifier'],
            security_group_ids=[sg_security_group.security_group_id],
            subnet_id=vpc.select_subnets(
                subnet_type=_ec2.SubnetType.PUBLIC
            ).subnet_ids[0]
        )

        

