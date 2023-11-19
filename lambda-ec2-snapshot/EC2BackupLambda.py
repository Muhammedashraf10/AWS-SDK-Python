import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger() #Set your log to get logs in case of any failures 
logger.setLevel(logging.INFO) # Set logging level to INFO 

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    try:
        response = ec2.create_snapshot(
            VolumeId=event['VolumeId'],
            Description='My EC2 Snapshot',
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': f"My EC2 Snapshot {current_date}"
                         
                        }
                   ]
                }
             ]
            )
        logger.info(f"Successfully Created Snapshot: {json.dumps(response, default=str)}") # this will dump the response into our logger 
    except Exception as e: 
        logger.error(f"Error Creating snapshot: {str(e)}")
 
