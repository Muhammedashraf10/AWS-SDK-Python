import boto3

ses_client = boto3.client('ses')
response = ses_client.send_templated_email(
    Source= 'muhammedashraf192@gmail.com',
    Destination={
        'ToAddresses':['eng.muhammadashraf1@gmail.com'],
        'CcAddresses':['muhammedashraf192@gmail.com']
    },
    ReplyToAddresses=['muhammedashraf192@gmail.com'],
    Template='CustomTemplate',
    TemplateData='{"replace":"value"}'
    
)
print(response)
