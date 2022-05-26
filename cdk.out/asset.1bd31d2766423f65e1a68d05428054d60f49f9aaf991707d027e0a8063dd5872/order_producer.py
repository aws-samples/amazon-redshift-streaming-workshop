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
    stream_name = 'order_stream'
    table_name = 'latest_key'
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
        
        orderkey = table.get_item(Key={'id':2})

        if "Item" in orderkey:
            order_key = int(orderkey['Item']['info']['latest'])
        else:
            table.put_item(Item={'id':2, 'info':{'latest':0}})
            order_key = 0

        with open('./product.json', 'r') as file:
            product_dict = json.loads(file.read())
            file.close()
            
        try:
            record_count = 0
            for i in range(random.randint(1,500)):
                product_id = random.randint(1, len(product_dict))
                profile_rec = {}
                profile_rec['orderid'] = order_key + record_count
                profile_rec['user_agent'] = fake.user_agent()
                profile_rec['ipv4'] = fake.ipv4_public()
                profile_rec['userid'] = random.randint(0, cur_key)
                profile_rec['productid'] = product_id
                profile_rec['timestamp'] = datetime.now().isoformat()
                profile_rec.update(product_dict[str(product_id)])
                send_data(client_kinesis, profile_rec,
                            str(uuid.uuid4()), stream_name)
                record_count += 1
                #time.sleep(1)
            resp["resp"] = record_count
            resp["status"] = True
            table.put_item(Item={'id':2, 'info':{'latest':int(order_key + record_count)}})

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
