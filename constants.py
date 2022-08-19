import os
import json
import urllib.request

APP_NAME = "rs-qs"
context_constants = {
    "environment" : "dev",
    "dev_global_config": {
        "account_id": os.environ["CDK_DEFAULT_ACCOUNT"],
        "region": os.environ["CDK_DEFAULT_REGION"],
        "app_name": APP_NAME
    },
    # Kinesis Configuration,
    "dev_kinesis_config": {
        "stream_name": f"order-stream",
        "retention_period": 72,
    },
    # Redshift Configuration
    "dev_redshift_config": {
        "max_azs": 3,
        "nat_gateways": 1,
        "redshift_vpc_cidr": "10.1.0.0/16",
        "subnet_cidr_mask": 24,
        "namespace_name": f"{APP_NAME}-ns",
        "workgroup_name": f"{APP_NAME}-wg",
        "base_capacity": 32,
        "db_name": "dev",
        "cluster_type": "multi-node",
        "number_of_nodes": 2,
        "master_username": f"{APP_NAME}-user",
        "node_type": "ra3.4xlarge",
    },
    "dev_jumpbox_config":{
        "instance_type_identifier": "t3.xlarge",
        "instance_name": "Jump Box",
        "key_name": "poc",
        "ebs_volume_size": 100,
    }
}
