import os
import urllib.request

from aws_cdk import Environment
from aws_cdk import (
    aws_ec2 as _ec2,
    aws_kinesis as _kinesis,
    aws_dynamodb as _dynamodb,
)


DEV_ENV=Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)

CDK_APP_NAME="rsstream"
CDK_APP_PYTHON_VERSION="3.8"

DEV_KINESIS_RETENTION_PERIOD=72
DEV_KINESIS_STREAM_MODE=_kinesis.StreamMode.ON_DEMAND
DEV_KINESIS_ENCRYPTION=_kinesis.StreamEncryption.UNENCRYPTED

DEV_GLUE_DATABASE_NAME="ext_s3"

DEV_DYNAMODB_BILLING_MODE=_dynamodb.BillingMode.PAY_PER_REQUEST

DEV_PERMISSIONS="IAM"
DEV_REDSHIFT_MAX_AZS=2
DEV_REDSHIFT_CLUSTER_TYPE="multi-node"
DEV_REDSHIFT_MASTER_USERNAME=f"{CDK_APP_NAME}_user"
DEV_REDSHIFT_DB_NAME=f"dev"
DEV_REDSHIFT_NUM_NODES=2
DEV_REDSHIFT_NODE_TYPE="ra3.4xlarge"
DEV_REDSHIFT_NAMESPACE=f"{CDK_APP_NAME}ns"
DEV_REDSHIFT_WORKGROUP=f"{CDK_APP_NAME}wg"


