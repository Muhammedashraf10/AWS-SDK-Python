# AWS-SDK-Python

# Prerequisites for EC2 Sechdular
- Python 3.9
- Lambda function with Role of EC2 {Start,Stop, Describe), CloudWatch Send logs and SES to send emails ( can be modified to be more fine grained access with permissions of describe EC2, volumes & create a snapshot of the volume.
- IDE ( used cloud9 to develop this code )

# EC2 Schedular V1 ( No email Notification )
![alt text](https://github.com/Muhammedashraf10/AWS-SDK-Python/blob/main/Instance-Schedular/Lambda-EC2-SchedularV1.png?raw=true)

# EC2 Schedular V2 ( With SES Notification )
![alt text](https://github.com/Muhammedashraf10/AWS-SDK-Python/blob/main/Instance-Schedular/Lambda-EC2-SchedularV2.png?raw=true)

This lambda function will help you to Schedular start & stop the EC2 instance based on the trigger pattern of the EventBridge

The solution is available with two options ( with and without sending email notification with the instance Ids )



