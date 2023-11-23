import boto3

ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')

unused_volumes = []
CHARSET='UTF-8'

volumes = ec2_client.describe_volumes()

for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0:
        unused_volumes.append(volume['VolumeId'])

email_body = """
        <html>
            <head></head>
            <h1 style='text_aligned:center'>Unused Volumes in your account </h1>
            <p style='color:red'>below list contains the unused & deleted volumes into your account </p>
        </html>
    """
for vol in unused_volumes:
    email_body = email_body + "VolumeId {} \n".format(vol)
    
for delete_vol in unused_volumes:
    response_delete = ec2_client.delete_volume(
            VolumeId=delete_vol,
            DryRun=False
    )

response = ses_client.send_email(
        Destination={
            "ToAddresses": ['xxxxx@yyyy.com','wwww@zzzz.com']
         },
        Message={
            "Body":{
                "Html":{
                    "Charset":CHARSET,
                    "Data": email_body
                }
            },
            "Subject":{
                    "Charset":CHARSET,
                    "Data": "This email address notify you with the deleted volumes into your account"
                }
            },
            Source = "src_email@zzzz.com"
    )
