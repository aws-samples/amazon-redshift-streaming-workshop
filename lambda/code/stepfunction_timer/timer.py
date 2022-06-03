import json
import datetime

def lambda_handler(event, context): 

    # Check if time element is in event parameter. If not, assume run to be incomplete
    if 'time' in event:
        # Extract time element as a datetime
        dt = datetime.datetime.strptime(event['time'], "%Y-%m-%dT%H:%M:%SZ")

        # Get time of running Lambda
        now = datetime.datetime.now().replace(microsecond=0)
        
        # Calculate difference between start of Step Function and now in seconds
        timediff = (now-dt).total_seconds()
        
        # Check if DesiredRuntimeSec is present in event. If not present, assume desired runtime of 50sec
        if 'DesiredRuntimeSec' in event:
            desiredRuntimeSec = event["DesiredRuntimeSec"]
        else:
            desiredRuntimeSec = 50
        
        # Return true if Step Function has run for longer than desired runtime and False otherwise
        return {
            'completeFlag': timediff > desiredRuntimeSec
            }
    else:
        return {
            'completeFlag': False
            }