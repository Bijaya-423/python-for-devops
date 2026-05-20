import boto3

s3_client = boto3.client("s3") #creating a client for s3 access

s3 = s3_client.list_buckets()
print(s3)