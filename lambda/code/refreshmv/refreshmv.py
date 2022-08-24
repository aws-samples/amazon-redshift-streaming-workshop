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
    secret_name = os.getenv("SECRET_NAME")
    db_name = os.getenv("DB_NAME")
    refreshmv = os.getenv("REFRESHMV")
    
    try:
        redshift_data_client = boto3.client('redshift-data')
        secretsmanager_client = boto3.client('secretsmanager')
        secret_arn = secretsmanager_client.describe_secret(SecretId=secret_name)['ARN']
        
        for i in range(10):
            response = redshift_data_client.execute_statement(
                Database=db_name,
                SecretArn=secret_arn,
                Sql=f'REFRESH MATERIALIZED VIEW {refreshmv}',
                WorkgroupName=workgroup_name
            )
            for i in range(5):
                cur_status = redshift_data_client.describe_statement(Id=response['Id'])['Status']
                if cur_status == 'FINISHED':
                    break
                time.sleep(1)
            time.sleep(1)
            
    # catch connection exceptions
    except Exception as e:
        LOGGER.error(e)
        raise e