import boto3 

ses_client = boto3.client('ses')
response = ses_client.verify_email_address(
    EmailAddress='xxxxx@yyyy.com' #Replace it with your email address in order to verify it on AWS
    )
    
print(response)
