import boto3

ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')

unused_volumes = []
CHARSET='UTF-8'

volumes = ec2_client.describe_volumes()

for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0:
        unused_volumes.append(volume['VolumeId'])
        #print(unused_volumes) #you can print for troubleshooting
        #print("-------"*5) #for a beter view

email_body = """
        <html>
            <head></head>
            <h1 style='text_aligned:center'>Unused Volumes in your account </h1>
            <p style='color:red'>below list contains the unused volumes </p>
        </html>
    """
for vol in unused_volumes:
    email_body = email_body + "VolumeId {} \n".format(vol)
    
#print(email_body) # for troubleshooting & tracing

response = ses_client.send_email(
        Destination={
            "ToAddresses": ['xxxxx@zzzz.com','wwww@yyyy.com'] #recipients 
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
                    "Data": "This email address notify you with the unused volumes into your account"
                }
            },
            Source = "src_email@zzzz.com" #your verified email address
    )
