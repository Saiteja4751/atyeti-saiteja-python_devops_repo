import boto3
import os
from config.aws_config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET_NAME

def upload_to_s3(file_path):
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

    s3 = session.client('s3')

    file_name = os.path.basename(file_path)

    try:
        s3.upload_file(file_path, S3_BUCKET_NAME, file_name)
        print(f"Uploaded {file_name} to s3://{S3_BUCKET_NAME}/{file_name}")
    except Exception as e:
        print(f"Failed to upload {file_name}: {e}")
