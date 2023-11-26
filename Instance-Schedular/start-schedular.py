import boto3
ec2 = boto3.resource('ec2')
filters=[
            {
                'Name': 'instance-state-name', 
                'Values': ['stopped']
                
            },
            {
                'Name': 'tag:Type', 
                'Values': ['Scheduled']
                
            }
        ]
try:
    instances = ec2.instances.filter(Filters=filters) # get the instances which matches the filter 
    for instance in instances:
          print(instance.id, instance.instance_type) # print the instance id & type 
          instance.start() #stop the instances with the tag Type: Scheduled
          print('Instance started successfully')
    print('Success')
except Exception as e:
    print("There is an error {}".format(e))

