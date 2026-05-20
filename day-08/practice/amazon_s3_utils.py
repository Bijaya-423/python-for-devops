import boto3
import pdb

s3_client = boto3.client("s3") #creating a client for s3 access

s3 = s3_client.list_buckets()

# pdb.set_trace()
for key, value in s3["Buckets"]:
    # print(key, value)
    if key == "Buckets":
        print(value)
    else:
        pass



