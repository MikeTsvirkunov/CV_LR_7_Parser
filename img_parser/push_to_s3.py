import boto3
s3 = boto3.client(
    's3',
    endpoint_url='https://s3.timeweb.cloud',
    aws_access_key_id='CMUNF0HMN7E81PRVHP8O',
    aws_secret_access_key= '1p0Yl6UYABuOyOCVNtf0q7aQmwAiYU82N9UlKpgC'
)

# for bucket in s3.buckets.all():
#     print(bucket.name)

with open("./images/0a31e296-4792-4ddb-bb6e-ccbf38005465.pt", "rb") as f:
    s3.upload_fileobj(f, "66ef2141-d2710b50-9d4e-4f2a-8dda-95a37ac453bf", "0a31e296-4792-4ddb-bb6e-ccbf38005465.pt")