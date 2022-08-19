#!/usr/bin/env python3
import os
import constants

import aws_cdk as cdk

from redshift_streaming.ingestion_stack import IngestionStack
from redshift_streaming.redshift_stack import RedshiftStack
from redshift_streaming.stepfunction_stack import StepFunctionStack

app = cdk.App(context=constants.context_constants)
environment = app.node.try_get_context("environment")
env=cdk.Environment(
        account=constants.context_constants[f'{environment}_global_config']['account_id'], 
        region=constants.context_constants[f'{environment}_global_config']['region'])

#add S3 in ingestion stack      
ingestion_stack = IngestionStack(app,  "IngestionStack", env=env)
#add ec2 in redshift stack
redshift_stack = RedshiftStack(app, "RedshiftStack", env=env, ingestion_stack=ingestion_stack)

#StepFunctionStack(app, "StepFunctionStack", env=env, redshift_stack=redshift_stack)

app.synth()
