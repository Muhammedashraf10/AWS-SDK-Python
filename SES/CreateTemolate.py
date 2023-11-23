import boto3

ses_client = boto3.client('ses')

response = ses_client.create_template(
    Template={
        'TemplateName': 'TemplateName', #Enter the Template Name
        'SubjectPart': 'Welcome ', # Enter the Subject that will be used
        'TextPart': 'Text Part of the Template', #Replace the Template Text
        'HtmlPart': 'Html Part of the Template' #Replace the Html Text
    }
    
)

print(response)
