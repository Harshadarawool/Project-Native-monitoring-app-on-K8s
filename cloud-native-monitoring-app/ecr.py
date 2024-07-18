import boto3

# Initialize a session using Amazon ECR
ecr_client = boto3.client('ecr')

# Specify the repository name
repository_name = "my_monitoring_app_image_new-1"

# Create the repository
response = ecr_client.create_repository(repositoryName=repository_name)

# Extract and print the repository URI
repository_uri = response['repository']['repositoryUri']
print(repository_uri)
