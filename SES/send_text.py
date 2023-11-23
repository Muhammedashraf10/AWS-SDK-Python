import boto3

#ses_client = boto3.client('ses')

def send_email_text():
    ses_client = boto3.client('ses')
    CHARSET='UTF-8'
    response = ses_client.send_email(
        Destination={
            "ToAddresses": ['muhammedashraf192@gmail.com','eng.muhammadashraf1@gmail.com']
         },
        Message={
            "Body":{
                "Text":{
                    "Charset":CHARSET,
                    "Data": "Thanks for Buying !"
                }
            },
            "Subject":{
                    "Charset":CHARSET,
                    "Data": "Helllo !, This is a test message !"
                }
            },
            Source = "muhammedashraf192@gmail.com"
    )
print(send_email_text())
