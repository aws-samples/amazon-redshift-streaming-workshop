#!/usr/bin/env python3
import aws_cdk as cdk

from redshift_streaming.ingestion_stack import IngestionStack
from redshift_streaming.redshift_stack import RedshiftStack
from redshift_streaming.stepfunction_stack import StepFunctionStack
from redshift_streaming.grafana_stack import GrafanaStack

import constants

app = cdk.App()

ingestion_stack = IngestionStack(app,
                                 "IngestionStack",
                                 glue_database_name=constants.DEV_GLUE_DATABASE_NAME,
                                 kinesis_retention_period=constants.DEV_KINESIS_RETENTION_PERIOD,
                                 kinesis_stream_mode=constants.DEV_KINESIS_STREAM_MODE,
                                 kinesis_encryption=constants.DEV_KINESIS_ENCRYPTION,
                                 dynamodb_billing_mode=constants.DEV_DYNAMODB_BILLING_MODE,
                                 env=constants.DEV_ENV)
redshift_stack = RedshiftStack(app,
                               "RedshiftStack",
                               consignment_stream=ingestion_stack.consignment_stream,
                               s3_bucket_raw=ingestion_stack.s3_bucket_raw,
                               redshift_max_azs=constants.DEV_REDSHIFT_MAX_AZS,
                               redshift_cluster_type=constants.DEV_REDSHIFT_CLUSTER_TYPE,
                               redshift_number_of_nodes=constants.DEV_REDSHIFT_NUM_NODES,
                               redshift_db_name=constants.DEV_REDSHIFT_DB_NAME,
                               redshift_master_username=constants.DEV_REDSHIFT_MASTER_USERNAME,
                               redshift_node_type=constants.DEV_REDSHIFT_NODE_TYPE,
                               env=constants.DEV_ENV)
sf_stack = StepFunctionStack(app,
                             "StepFunctionStack",
                             rs_cluster=redshift_stack.rs_cluster,
                             env=constants.DEV_ENV)

app.synth()
