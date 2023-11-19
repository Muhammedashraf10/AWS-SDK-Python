# AWS-SDK-Python

# Prerequisites for EC2 Backup through Lambda 
- Python 3.9
- Role with EC2 Full Access for our lambda function ( can be modified to be more fine grained access with permissions of describe EC2, volumes & create a snapshot of the volume.
- IDE ( used cloud9 to develop this code )

# EC2 Lambda Backup
![alt text](https://github.com/Muhammedashraf10/AWS-SDK-Python/blob/main/lambda-ec2-snapshot/ec2-snapshot-lambda.drawio.png?raw=true)

This lambda function will help you to create a snapshot of your EC2 instance volunme using Lambda function, you can integrate the lambda function with AWS EventBridge to schedule the run of the lambda function on a regular basis,

There will be 3 files as below 

# EC2BackupLamda.py

This our main python file which we will execute to create a snapshot

# event.json

This file will contains our VolumeIds which the lambda function will take a snapshot from 

# Template.yaml 

This contains information related to AWS for our Lambda function

You can use AWS SAM command to invoke the lambda locally in case of you have downladed the lambda locally through Cloud09 

sam local invoke -e event.json 
