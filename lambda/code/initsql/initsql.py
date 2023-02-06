import os
import boto3
import time
import logging

def lambda_handler(event, context):
    
    logging.basicConfig()
    global LOGGER
    LOGGER = logging.getLogger(__name__)
    resp = {"status": False, "resp": ""}
    LOGGER.setLevel(logging.DEBUG)
    
    workgroup_name = os.getenv("WORKGROUP_NAME")
    secret_arn = os.getenv("SECRET_ARN")
    db_name = os.getenv("DB_NAME")
    sql = os.getenv("SQL")
    
    try:
        redshift_data_client = boto3.client('redshift-data')
        response = redshift_data_client.execute_statement(
            Database=db_name,
            SecretArn=secret_arn,
            Sql=sql,
            WorkgroupName=workgroup_name
        )
            
    # catch connection exceptions
    except Exception as e:
        LOGGER.error(e)
        raise e