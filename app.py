#!/usr/bin/env python3
import os
import constants

import aws_cdk as cdk
from cdk_nag import AwsSolutionsChecks
from aws_cdk import Aspects

from redshift_streaming.ingestion_stack import IngestionStack
from redshift_streaming.redshift_stack import RedshiftStack
from redshift_streaming.init_stack import InitStack

app = cdk.App(context=constants.context_constants)
#Aspects.of(app).add(AwsSolutionsChecks(verbose=True))
environment = app.node.try_get_context("environment")
env=cdk.Environment(
        account=constants.context_constants[f'{environment}_global_config']['account_id'], 
        region=constants.context_constants[f'{environment}_global_config']['region'])

#add init  stack      
init_stack = InitStack(app,  "InitStack", env=env)
#add S3 in ingestion stack      
ingestion_stack = IngestionStack(app,  "IngestionStack", env=env, init_stack=init_stack)
#add ec2 in redshift stack
redshift_stack = RedshiftStack(app, "RedshiftStack", env=env, init_stack=init_stack)


app.synth()
