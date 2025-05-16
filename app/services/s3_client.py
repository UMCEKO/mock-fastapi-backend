import boto3
from mypy_boto3_s3.client import S3Client

from app.core.config import S3_ENDPOINT, S3_REGION, S3_ACCESS_KEY, S3_SECRET_KEY, S3_BUCKET

# We will use this client whenever s3 client is necessary.

s3_client: S3Client = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    region_name=S3_REGION,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY
)

# Check if the bucket exists and create if it does not.

print("Getting all available s3 buckets.")
buckets = s3_client.list_buckets()
if S3_BUCKET not in [b["Name"] for b in buckets["Buckets"]]:
    print("S3 Bucket not found. Creating it...")
    s3_client.create_bucket(Bucket=S3_BUCKET)
    print("Successfully created the S3 bucket.")