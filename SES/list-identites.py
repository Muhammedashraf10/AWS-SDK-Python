import boto3

ses_client = boto3.client('ses')

response = ses_client.list_identities(
    IdentityType = 'EmailAddress' #List all verified Identites
    
    )
    
print(response)
