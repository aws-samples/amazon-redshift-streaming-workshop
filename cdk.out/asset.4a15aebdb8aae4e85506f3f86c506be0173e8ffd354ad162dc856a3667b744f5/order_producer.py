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
        fake = Faker(['en-AU'])

        
        curkey = table.get_item(Key={'id':1})

        if "Item" in curkey:
            cur_key = int(curkey['Item']['info']['latest'])
        else:
            table.put_item(Item={'id':1, 'info':{'latest':0}})
            cur_key = 0
        
        if cur_key == 0:
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": resp
                })
            }
        
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
                now = datetime.now()
                prob = 0
                if now.hour < 12:
                    prob = now.hour
                elif now.hour == 12:
                    prob = now.hour + now.minute
                elif now.hour > 12:
                    prob = now.hour + 60
                prob = prob/100
                product_id = random.randint(1, len(product_dict))
                profile_rec = {}
                profile_rec['consignmentid'] = order_key + record_count
                customer_address = fake.address()
                customer_state = customer_address.split(',')[-2]
                order_address = fake.address()
                order_state = customer_address.split(',')[-2]
                profile_rec['delivery_address'] = customer_address
                profile_rec['delivery_state'] = customer_state
                profile_rec['origin_address'] = order_address
                profile_rec['origin_state'] = order_state
                profile_rec['userid'] = random.randint(0, cur_key)
                profile_rec['timestamp'] = datetime.now().isoformat()
                days_to_deliver = random.choice(range(2,7))
                profile_rec['days_to_deliver'] = days_to_deliver
                mean_distance = 10 +  (days_to_deliver * 100)
                profile_rec['delivery_distance'] = random.gauss(mean_distance, mean_distance/5)
                profile_rec['revenue'] = random.gauss(mean_distance/6, mean_distance/18)
                profile_rec['cost'] =  profile_rec['revenue'] - (random.random() *  profile_rec['revenue'] /2)
                profile_rec['delay_probability'] = 'LOW'
                if random.random()  < 0.3:
                    profile_rec['delay_probability'] = 'MEDIUM'
                if random.random()  < (0.05 + prob):
                    profile_rec['delay_probability'] = 'HIGH'
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
