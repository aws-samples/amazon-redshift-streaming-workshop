from aws_cdk import (
    # Duration,
    Aws,
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_cloud9 as _c9,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb,
    aws_logs as _logs,
    aws_lakeformation as _lakeformation,
    aws_ec2 as _ec2,
    aws_sagemaker as _sg,
    custom_resources as _cr,
    aws_events as _events,
    aws_glue as _glue,
    aws_events_targets as _events_targets,
    aws_s3_deployment as _s3_deploy,
    aws_kinesis as _kinesis,
    aws_redshiftserverless as _rss,
    aws_redshift as _rs,
    aws_s3 as _s3,
    aws_rds as _rds,
    aws_secretsmanager as _sm,
    aws_mwaa as _mwaa,
    CfnOutput,
    SecretValue,
    Tags
    # aws_sqs as sqs,
)
from constructs import Construct

import json

from pathlib import Path

import urllib.request

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        cdkapp="rs"
        glue_raw_db='raw_db'
        glue_transformed_db='transformed_db'
        rs_admin_username="admin"
        rs_workgroup_name=f"{cdkapp}-wg"
        rs_namespace_name=f"{cdkapp}-ns"
        rs_db_name="dev"
        rs_base_capacity=8
        mwaa_env_name = f"{cdkapp}-dev"
        mwaa_env_class = "mw1.small"
        mwaa_env_version = "2.5.1"
        c9_ip = urllib.request.urlopen("http://ident.me").read().decode("utf8")

        vpc = _ec2.Vpc(
            self,
            "VpcId",
            max_azs = 3,
        )

        rs_security_group = _ec2.SecurityGroup(
            self,
            "redshiftSecurityGroup",
            vpc=vpc
        )
        
        qs_security_group = _ec2.SecurityGroup(
            self,
            "QuicksightSecurityGroup",
            vpc=vpc
        )
        
        af_security_group = _ec2.SecurityGroup(
            self,
            "AirflowSecurityGroup",
            vpc=vpc
        )
        
        qs_security_group.add_ingress_rule(rs_security_group, _ec2.Port.all_traffic())
        rs_security_group.add_ingress_rule(rs_security_group, _ec2.Port.all_traffic())
        rs_security_group.add_ingress_rule(qs_security_group, _ec2.Port.tcp(5439))
        rs_security_group.add_ingress_rule(af_security_group, _ec2.Port.tcp(5439))
        
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4(vpc.vpc_cidr_block), 
            _ec2.Port.tcp(5439)
        )
        
        #Cloud9 IP
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4(f'{c9_ip}/32'), 
            _ec2.Port.tcp(5439)
        )
        #Quicksight us-west-2
        rs_security_group.add_ingress_rule(
            _ec2.Peer.ipv4('54.70.204.128/27'), 
            _ec2.Port.tcp(5439)
        )
        
        # Create Glue Security Group *future use*

        glue_security_group = _ec2.SecurityGroup(
            self,
            "glueSecurityGroup",
            vpc=vpc
        )

        # define permisssions
        
        glue_security_group.add_ingress_rule(glue_security_group,_ec2.Port.all_traffic())
        rs_security_group.add_ingress_rule(rs_security_group, _ec2.Port.all_traffic())
        rs_security_group.add_ingress_rule(glue_security_group, _ec2.Port.tcp(5439))
        
        # Auto generate Redshift password
        redshift_password = _sm.Secret.from_secret_name_v2(
            self,
            "redshift_password",
            secret_name="REDSHIFT_PASSWORD"
        )
        
        # Create another secret in format required by RS Data API

        redshift_credentials = _sm.Secret(
            self,
            "redshift_credentials",
            description="Redshift credentials",
            secret_string_value=SecretValue.unsafe_plain_text(
                json.dumps({'username':rs_admin_username, 
                'password':redshift_password.secret_value.unsafe_unwrap()
                #'password':rs_admin_password
                })
                ),
            removal_policy=RemovalPolicy.DESTROY,
        )
        
        # Created Redshift IAM Role
        
        rs_role = _iam.Role(
            self, "redshiftClusterRole",
            assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("sagemaker.amazonaws.com")),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftAllCommandsFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "SecretsManagerReadWrite"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"
                )
            ]
        )
        
        # Add custom policy that is used by Redshift to allow access to entire Glue Data Catalog and Lake Formation

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
            roles=[rs_role],
        )
        
        # Create Redshift Serverless Namespace
        
        consumer_rs_namespace = _rss.CfnNamespace(
            self,
            "consumer_redshiftServerlessNamespace",
            namespace_name=f"{rs_namespace_name}",
            db_name=rs_db_name,
            default_iam_role_arn=rs_role.role_arn,
            iam_roles=[rs_role.role_arn],
            admin_username=rs_admin_username,
            admin_user_password=redshift_password.secret_value.unsafe_unwrap(),
            # admin_user_password=redshift_password.secret_value.unsafe_unwrap(),
        )

        
        
        # Create Redshift Serverless Workgroup

        consumer_rs_workgroup = _rss.CfnWorkgroup(
            self,
            "consumer_redshiftServerlessWorkgroup",
            workgroup_name=f"{rs_workgroup_name}",
            base_capacity=rs_base_capacity,
            publicly_accessible=True,
            namespace_name=f"{rs_namespace_name}",
            security_group_ids=[rs_security_group.security_group_id],
            subnet_ids=vpc.select_subnets(
                subnet_type=_ec2.SubnetType.PRIVATE_WITH_NAT
            ).subnet_ids,
        )
        
        consumer_rs_workgroup.node.add_dependency(consumer_rs_namespace)
        
        # Create S3 bucket for raw data
        
        
        s3_bucket_raw = _s3.Bucket(
            self,
            "raw",
            encryption=_s3.BucketEncryption.S3_MANAGED,
            public_read_access=False,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
        
        s3_bucket_transformed = _s3.Bucket(
            self,
            "transformed",
            encryption=_s3.BucketEncryption.S3_MANAGED,
            public_read_access=False,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
        
        # Deploy objects in S3 bucket

        s3_bucket_deployment = _s3_deploy.BucketDeployment(
            self,
            "s3_deploy_raw",
            destination_bucket=s3_bucket_raw,
            sources=[
                _s3_deploy.Source.asset(
                    str(Path(__file__).parent.parent.joinpath("data"))
                )
            ],
            exclude=[".DS_Store"],
            
        )
        
        # Grant Redshift role access to the bucket
        
        s3_bucket_raw.grant_read_write(rs_role)
        
        # Create Glue Database
        
        raw_db = _glue.CfnDatabase(
            self,
            "raw_db",
            catalog_id=Aws.ACCOUNT_ID,
            database_input=_glue.CfnDatabase.DatabaseInputProperty(
                name=glue_raw_db
            ),
        )
        raw_db.apply_removal_policy(policy=RemovalPolicy.DESTROY)
        
        transformed_db = _glue.CfnDatabase(
            self,
            "transformed_db",
            catalog_id=Aws.ACCOUNT_ID,
            database_input=_glue.CfnDatabase.DatabaseInputProperty(
                name=glue_transformed_db
            ),
        )
        transformed_db.apply_removal_policy(policy=RemovalPolicy.DESTROY)
        
        # Create CSV Classifier for crawler
        
        csv_classifier = _glue.CfnClassifier(self, "csv_Classifier",
            csv_classifier=_glue.CfnClassifier.CsvClassifierProperty(
                allow_single_column=False,
                contains_header="PRESENT",
                delimiter=",",
                quote_symbol='"'
            )
        )

        # Grant Crawler Role access to the bucket
        
                # Create Glue Crawler Role
        
        crawler_role = _iam.Role(
            self,
            "crawler_role",
            role_name='GlueServiceRole',
            assumed_by=_iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSGlueServiceRole"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"
                )
            ],
        )
        
        s3_bucket_raw.grant_read_write(crawler_role)
        
        # Create Glue Crawler for raw data
        
        crawler_raw = _glue.CfnCrawler(
            self,
            "crawler_raw",
            targets=_glue.CfnCrawler.TargetsProperty(
                s3_targets=[
                    _glue.CfnCrawler.S3TargetProperty(path=s3_bucket_raw.bucket_name)
                ],
            ),
            database_name=glue_raw_db,
            role=crawler_role.role_name,
            classifiers=[csv_classifier.ref]
        )
        
      
        
        # Start Glue Crawler
        
        aws_custom_crawler = _cr.AwsCustomResource(
            self, "aws-custom-start-crawler",
            on_update=_cr.AwsSdkCall(
                service="Glue",
                action="startCrawler",
                parameters={
                    "Name": crawler_raw.ref
                },
                physical_resource_id=_cr.PhysicalResourceId.of("physicalResourceStateMachine")
            ),
            policy=_cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=_cr.AwsCustomResourcePolicy.ANY_RESOURCE
            )
        ) 
        
        aws_custom_crawler.node.add_dependency(raw_db)
        aws_custom_crawler.node.add_dependency(s3_bucket_deployment)
        
        # create s3 bucket for mwaa
        s3_bucket_mwaa = _s3.Bucket(
            self,
            "mwaa",
            encryption=_s3.BucketEncryption.S3_MANAGED,
            public_read_access=False,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            versioned=True,
            enforce_ssl=True,
        )
        # tag the bucket
        Tags.of(s3_bucket_mwaa).add("purpose", "MWAA")

        # deploy files to mwaa bucket
        airflow_files = _s3_deploy.BucketDeployment(
            self,
            "deploy_requirements",
            destination_bucket=s3_bucket_mwaa,
            sources=[
                _s3_deploy.Source.asset(str(Path(__file__).parent.parent.joinpath("mwaa"))),
            ],
            include=["requirements.txt", "plugins.zip", "dags/*"],
            exclude=["requirements.in", "dags.zip", "plugins/*",".DS_Store"],
        )

        # create vpc endpoints for mwaa
        mwwa_api_endpoint = vpc.add_interface_endpoint(
            "mwaa_api_endpoint",
            service=_ec2.InterfaceVpcEndpointAwsService(name="airflow.api"),
        )
        vpc.add_interface_endpoint(
            "mwaa_env_endpoint",
            service=_ec2.InterfaceVpcEndpointAwsService(name="airflow.env"),
        )
        vpc.add_interface_endpoint(
            "mwaa_ops_endpoint",
            service=_ec2.InterfaceVpcEndpointAwsService(name="airflow.ops"),
        )

        # role for mwaa
        airflow_role = _iam.Role(
            self,
            "airflow_role",
            assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("airflow-env.amazonaws.com"),
                _iam.ServicePrincipal("airflow.amazonaws.com"),
            ),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "SecretsManagerReadWrite"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSGlueConsoleFullAccess"
                ),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonRedshiftDataFullAccess"
                )
            ],
        )

        s3_bucket_mwaa.grant_read_write(airflow_role)
        
        airflow_role.add_to_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["airflow:PublishMetrics"],
                resources=["*"],
            )
        )
        
        
        airflow_role.add_to_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=[
                    "logs:CreateLogStream",
                    "logs:CreateLogGroup",
                    "logs:PutLogEvents",
                    "logs:GetLogEvents",
                    "logs:GetLogRecord",
                    "logs:GetLogGroupFields",
                    "logs:GetQueryResults",
                    "logs:DescribeLogGroups",
                ],
                resources=["*"],
            )
        )
        
        airflow_role.add_to_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["cloudwatch:PutMetricData"],
                resources=["*"],
            )
        )
        
        airflow_role.add_to_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["iam:PassRole"],
                resources=["*"],
            )
        )
        
        airflow_role.add_to_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=[
                    "sqs:ChangeMessageVisibility",
                    "sqs:DeleteMessage",
                    "sqs:GetQueueUrl",
                    "sqs:GetQueueAttributes",
                    "sqs:ReceiveMessage",
                    "sqs:SendMessage",
                ],
                resources=[f"arn:aws:sqs:{Aws.REGION}:*:airflow-celery-*"],
            )
        )
            
        airflow_role.add_to_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=[
                    "kms:Decrypt",
                    "kms:DescribeKey",
                    "kms:GenerateDataKey*",
                    "kms:Encrypt",
                ],
                not_resources=[f"arn:aws:kms:*:{Aws.ACCOUNT_ID}:key/*"],
                conditions={
                    "StringLike": {
                        "kms:ViaService": [
                            f"sqs.{Aws.REGION}.amazonaws.com"
                        ]
                    }
                },
            )
        )

        af_security_group.connections.allow_internally(_ec2.Port.all_traffic(), "within MWAA")
        
        airflow_env = _mwaa.CfnEnvironment(
            self,
            "airflow_env",
            name=mwaa_env_name,
            environment_class=mwaa_env_class,
            airflow_version=mwaa_env_version,
            airflow_configuration_options={
                "core.load_default_connections": False,
                "core.load_examples": False,
                "webserver.dag_default_view": "tree",
                "webserver.dag_orientation": "TB",
                "core.lazy_load_plugins": False,
                "secrets.backend": "airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend",
                "secrets.backend_kwargs": {
                    "connections_prefix": "airflow/connections",
                    "variables_prefix": "airflow/variables",
                },
            },
            dag_s3_path="dags",
            #plugins_s3_path="plugins.zip",
            requirements_s3_path="requirements.txt",
            source_bucket_arn=airflow_files.deployed_bucket.bucket_arn,
            network_configuration=_mwaa.CfnEnvironment.NetworkConfigurationProperty(
                security_group_ids=[af_security_group.security_group_id],
                subnet_ids=vpc.select_subnets(
                    subnet_type=_ec2.SubnetType.PRIVATE_WITH_NAT,
                ).subnet_ids[:2],
            ),
            execution_role_arn=airflow_role.role_arn,
            max_workers=10,
            webserver_access_mode="PUBLIC_ONLY",
            logging_configuration=_mwaa.CfnEnvironment.LoggingConfigurationProperty(
                task_logs={"enabled": True, "logLevel": "INFO"},
                worker_logs={"enabled": True, "logLevel": "INFO"},
                scheduler_logs={"enabled": True, "logLevel": "INFO"},
                dag_processing_logs={"enabled": True, "logLevel": "INFO"},
                webserver_logs={"enabled": True, "logLevel": "INFO"},
            ),
            # weekly_maintenance_window_start="MON:03:30"
        )
        
        # output the airflow ux
        CfnOutput(
            self,
            "MWAAWebserverUrl",
            value=f"https://{airflow_env.attr_webserver_url}/home",
            description="MWAA URL",
        )
        
        CfnOutput(
            self,
            "RedshiftServerlessEndpoint",
            value=f"{rs_workgroup_name}.{Aws.ACCOUNT_ID}.{Aws.REGION}.redshift-serverless.amazonaws.com",
            description=f"Redshift serverless endpoint",
        )
        
        CfnOutput(
            self,
            "RedshiftMasterUser",
            value=rs_admin_username,
            description=f"Redshift username",
        )

        CfnOutput(
            self,
            "RedshiftClusterPassword",
            value=(redshift_password.secret_value.unsafe_unwrap()),
            description=f"Redshift password",
        )
        
        CfnOutput(
            self,
            "out-s3-raw",
            value=s3_bucket_raw.bucket_name,
            description="Raw bucket name",
        )
        
        CfnOutput(
            self,
            "out-s3-mwaa",
            value=s3_bucket_mwaa.bucket_name,
            description="MWAA bucket name",
        )
        
        CfnOutput(
            self,
            "out-s3-transformed",
            value=s3_bucket_transformed.bucket_name,
            description="Transformed bucket name",
        )
        
        CfnOutput(
            self,
            "out-crawler",
            value=crawler_raw.name,
            description="Crawler name",
        )
