import boto3

# Connect to LocalStack S3
s3 = boto3.resource(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Create bucket
bucket_name = 'my-local-bucket'
#s3.create_bucket(Bucket=bucket_name)

# Upload file
file_name = 'test_python.txt'
with open(file_name, 'w') as f:
    f.write("Hello LocalStack via Python!")

s3.Bucket(bucket_name).upload_file(file_name, file_name)

# List files
for obj in s3.Bucket(bucket_name).objects.all():
    print(obj.key)
