import boto3

ec2 = boto3.resource('ec2')
ses_client = boto3.client('ses')

total_instances = []
CHARSET='UTF-8'

filters=[
            {
                'Name': 'tag:Type', 
                'Values': ['Scheduled']
                
            }
        ]
email_body = """
            <html>
                <head></head>
                <h1 style='text_aligned:center'>Instance Schedular</h1>
                <p style='color:red'>below list contains Instance Ids which schedular takes action on</p>
            </html>
        """
try:
    instances = ec2.instances.filter(Filters=filters) # get the instances which matches the filter 
    for instance in instances:
        if instance.state['Name'] == 'stopped':
            print(instance.state['Name']) # print the instance id & type 
            instance.start() #stop the instances with the tag Type: Scheduled
            total_instances.append(instance.id)
            email_body = email_body + "InstanceId Started {} \n".format(instance.id)
            print('Instance started successfully')
        elif instance.state['Name'] == 'running':
            print(instance.id, instance.instance_type)
            instance.stop()
            total_instances.append(instance.id)
            email_body = email_body + "InstanceId Stopped {} \n".format(instance.id)
            print('Instance stopped successfully')
        else:
            print("Unexpected Error")
            
    print('Success')
except Exception as e:
    print("There is an error {}".format(e))
    

response = ses_client.send_email(
            Destination={
                "ToAddresses": ['xxxxx@yyyy.com','zzzz@wwww.com']
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
                        "Data": "This email address notify you with the Instance Id which Schedular took action on into your account"
                    }
                },
                Source = "xxxxx@yyyy.com"
        )

