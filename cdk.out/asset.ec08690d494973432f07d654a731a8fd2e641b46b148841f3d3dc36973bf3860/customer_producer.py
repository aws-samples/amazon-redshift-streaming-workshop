import logging
import os
import time

import boto3
import json
import random
import uuid
from datetime import datetime
from faker import Faker


def send_data(client, data, key, stream_name):
    resp = client.put_records(
        Records=[
            {
                "Data": json.dumps(data),
                "PartitionKey": key},
        ],
        StreamName=stream_name

    )
    LOGGER.info(f"Response:{resp}")


def lambda_handler(event, context):
    logging.basicConfig()
    global LOGGER
    LOGGER = logging.getLogger(__name__)
    resp = {"status": False, "resp": ""}
    LOGGER.setLevel(logging.DEBUG)
    stream_name = 'customer_stream'
    table_name = 'latest_customer_key'
    try:
        region = os.environ.get('AWS_REGION')
        client_dynamodb = boto3.resource('dynamodb')
        table = client_dynamodb.Table(table_name)
        client_kinesis = boto3.client('kinesis', region)
        fake = Faker()

        
        curkey = table.get_item(Key={'id':1})

        if "Item" in curkey:
            cur_key = int(curkey['Item']['info']['latest'])
        else:
            table.put_item(Item={'id':1, 'info':{'latest':0}})
            cur_key = 0

        try:
            record_count = 0
            for i in range(random.randint(1, 50)):
                profile_rec = {}
                profile_rec['userid'] = cur_key + record_count
                profile_rec.update(fake.profile(['username','job', 'company', 'ssn', 'name', 'sex', 'birthdate', 'mail']))
                customer_address = fake.location_on_land()
                profile_rec['latitude'] = customer_address[0]
                profile_rec['longitude'] = customer_address[1]
                profile_rec['city'] = customer_address[2]
                profile_rec['country'] = customer_address[3]
                profile_rec['birthdate'] = profile_rec['birthdate'].isoformat()
                send_data(client_kinesis, profile_rec,
                            str(uuid.uuid4()), stream_name)
                record_count += 1
                time.sleep(1)
            resp["resp"] = record_count
            resp["status"] = True
            table.put_item(Item={'id':1, 'info':{'latest':int(cur_key + record_count)}})

        except Exception as e:
            LOGGER.error(f"ERROR:{str(e)}")
            resp["error_message"] = str(e)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": resp
            })
        }

    # catch connection exceptions
    except Exception as e:
        LOGGER.error(e)
        raise e
