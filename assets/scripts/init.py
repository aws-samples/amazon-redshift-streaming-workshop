import boto3
import json
import sqlalchemy as sa
from sqlalchemy.engine.url import URL
workgroup_name = 'default'
namespace_name = 'default'
secret_name = 'REDSHIFT_PASSWORD'
admin_username = 'admin'
db_name = 'dev'
port = 5439
redshift_client = boto3.client('redshift-serverless')
secretsmanager_client = boto3.client('secretsmanager')
endpoint = redshift_client.get_workgroup(workgroupName=workgroup_name)['workgroup']['endpoint']['address']
secret_value = secretsmanager_client.get_secret_value(
    SecretId=secret_name,
    )['SecretString']
admin_password = json.loads(secret_value)['password']
redshift_url = URL.create(
drivername='redshift+redshift_connector', 
host=endpoint, 
port=port, 
database=db_name, 
username=admin_username,
password=admin_password
)