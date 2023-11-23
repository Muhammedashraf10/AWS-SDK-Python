import boto3

ses_client = boto3.client('ses')
response = ses_client.send_templated_email(
    Source= 'wwww@yyyy.com', #Replace it with your verified email address at AWS SES
    Destination={
        'ToAddresses':['xxxxx@zzzz.com'], #Enter your destination, you can use list of emails as destintation ['xxxxx@zzzz.com', 'xxxxx2@zzzz.com'],
        'CcAddresses':['wwww@yyyy.com']
    },
    ReplyToAddresses=['wwww@yyyy.com'],
    Template='CustomTemplate', #Replace it with your predefined template
    TemplateData='{"replace":"value"}'
    
)
print(response)
