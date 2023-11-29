import boto3 

s3_client = boto3.client('s3')
file_reader = open('/home/ec2-user/environment/python/S3_Upload/file.txt').read()

response = s3_client.put_object(
    ACL='private',
    Body=file_reader,
    Bucket='new-python-sdk-training',
    Key='demo'
    )
    
print(response)
