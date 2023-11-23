import boto3

ses_client = boto3.client('ses')

response = ses_client.create_template(
    Template={
        'TemplateName': 'TemplateName',
        'SubjectPart': 'Welcome ',
        'TextPart': 'Text Part of the Template',
        'HtmlPart': 'Html Part of the Template'
    }
    
)

print(response)
