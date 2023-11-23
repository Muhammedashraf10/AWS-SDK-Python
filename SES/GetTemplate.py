import boto3
from pprint import pprint 

ses_client = boto3.client('ses')

response = ses_client.get_template(
    TemplateName='CustomTemplate' #Replace it with Template name to get the template information
    )
    
pprint(response)
