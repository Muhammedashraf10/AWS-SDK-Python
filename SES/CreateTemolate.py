import boto3

ses_client = boto3.client('ses')

response = ses_client.create_template(
    Template={
        'TemplateName': 'CustomTemplate',
        'SubjectPart': 'Welcome to the Course',
        'TextPart': 'Thanks for buying',
        'HtmlPart': 'Thanks for buying'
    }
    
)

print(response)
