#!/usr/bin/env python3
import os

import aws_cdk as cdk

from redshift_streaming.ingestion_stack import IngestionStack
from redshift_streaming.redshift_stack import RedshiftStack
from redshift_streaming.stepfunction_stack import StepFunctionStack

app = cdk.App(
    context={
        "ingestion_config": {
            "retention_period": 72,
        },
        "redshift_config": {
            "max_azs": 2,
            "number_of_nodes": 2,
            "node_type": "ra3.4xlarge",
            "cluster_type":"multi-node",
            "db_name": "streaming_db",
            "master_username": "admin",
        },
    }
)

ingestion_stack = IngestionStack(app, "IngestionStack")
redshift_stack = RedshiftStack(app, "RedshiftStack", ingestion_stack=ingestion_stack)
StepFunctionStack(app, "StepFunctionStack", redshift_stack=redshift_stack)

app.synth()
