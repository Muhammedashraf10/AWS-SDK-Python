import boto3

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_attachment():
    msg = MIMEMultipart()
    
    msg["Subject"]="Enter your Subject"
    msg["From"]="muhammedashraf192@gmail.com"
    msg["To"]="eng.muhammadashraf1@gmail.com"
    
    
    body = MIMEText("Enter your Body Message Here ")
    msg.attach(body)
    
    
    file_name = "/home/ec2-user/environment/python/SES/file.txt"
    with open(file_name, "rb") as f:
        part = MIMEApplication(f.read())
        part.add_header("Content-",
                        "attachment",
                        filename=file_name
        )
        
    msg.attach(part)
    
    ses_client = boto3.client('ses')
    response = ses_client.send_raw_email(
        Source="muhammedashraf192@gmail.com",
        Destinations=['eng.muhammadashraf1@gmail.com'],
        RawMessage={
            "Data":msg.as_string()
        }
    )
    
    print(response)
    
send_email_attachment()
