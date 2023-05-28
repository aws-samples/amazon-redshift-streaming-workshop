
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
import boto3

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


client = boto3.client('glue')


s3bucket = '<REPLACE WITH TRANSFORMED BUCKET>'
sourcedatabaseName = 'raw_db'
targetdatabaseName = 'transformed_db'



Tables = client.get_tables(DatabaseName=sourcedatabaseName)

tableList = Tables['TableList']

for table in tableList:
    tableName = table['Name']
    print ('\n-- tableName: ' + tableName)

    datasource0 = glueContext.create_dynamic_frame.from_catalog(
        database=sourcedatabaseName, 
        table_name=tableName, 
        transformation_ctx="datasource0"
    )
    
    s3output = glueContext.getSink(
      path=f"s3://{s3bucket}/tickit/{tableName}/",
      connection_type="s3",
      updateBehavior="UPDATE_IN_DATABASE",
      partitionKeys=[],
      compression="snappy",
      enableUpdateCatalog=True,
      transformation_ctx="s3output",
    )
    s3output.setCatalogInfo(
      catalogDatabase=targetdatabaseName, catalogTableName=tableName
    )
    s3output.setFormat("glueparquet")
    s3output.writeFrame(datasource0)
job.commit()