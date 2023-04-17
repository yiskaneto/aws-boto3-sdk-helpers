import boto3, botocore
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--bucket", help="Name of the bucket")
parser.add_argument("--aws_region", help="aws region where to look for the bucket")
args = parser.parse_args()

try:
    s3 = boto3.client('s3', region_name=args.aws_region)
    response = s3.get_bucket_location(Bucket = args.bucket)
    # print(response) # get the full response
    print(f"LocationConstraint: {response['LocationConstraint']}")

except botocore.exceptions.ClientError as err:
    # print(response) # get the full response
    if err.response['Error']['Code'] == 'NoSuchBucket':
        print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
        print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
        print(f"\nThe bucket named {args.bucket} doesn't exist on {args.aws_region}\n")
    else:
        print("Error occured : ", err)
