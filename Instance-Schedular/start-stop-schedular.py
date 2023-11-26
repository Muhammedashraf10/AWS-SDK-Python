import boto3

ec2 = boto3.resource('ec2')

filters=[
            {
                'Name': 'tag:Type', 
                'Values': ['Scheduled']
                
            }
        ]
try:
    instances = ec2.instances.filter(Filters=filters) # get the instances which matches the filter 
    for instance in instances:
        if instance.state['Name'] == 'stopped':
            print(instance.state['Name']) # print the instance id & type 
            instance.start() #stop the instances with the tag Type: Scheduled
            print('Instance started successfully')
        elif instance.state['Name'] == 'running':
            print(instance.id, instance.instance_type)
            instance.stop()
            print('Instance stopped successfully')
        else:
            print("Unexpected Error")
            
    
    print('Success')
except Exception as e:
    print("There is an error {}".format(e))
