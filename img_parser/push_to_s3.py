from dotenv import load_dotenv
from os import environ
from img_parser.constants import Archive, S3Storage
import boto3


s3 = boto3.client(
    's3',
    endpoint_url=S3Storage.endpoint_url,
    aws_access_key_id=S3Storage.aws_access_key_id,
    aws_secret_access_key= S3Storage.aws_secret_access_key
)


def push_to_s3_storage():
    fn = f'{Archive.archive_name}.{Archive.archive_type}'
    with open(fn, "rb") as f:
        s3.upload_fileobj(f, S3Storage.bucket_name, fn)
