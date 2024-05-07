import sys, time, argparse
from datetime import datetime
import boto3, botocore
sys.path.append( '../')
from common.banners import cleanup_init_msg
from list_bucket_functions import *

# def a_bucket_function(bucket_name):
#     """
#     Empty S3 bucket
#     """
#     start_time = datetime.now()
#     cleanup_start_msg(bucket_name)
#     clean_bucket(bucket_name)
#     total_time =  datetime.now() - start_time
#     cleanup_success_banner(bucket_name, 0, total_time)
#     return None

# def list_bucket_objects():
#     """
#     Returns the provided bucket's objects.\n
#     See more about this operation at:\n
#     https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects_v2.html
#     """
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--bucket", required=True, help="Name of the bucket")
#     parser.add_argument("--aws_region", required=True, help="aws region where to look for the bucket")
#     parser.add_argument("--prefix", required=False, help="Buckets Prefix")
#     args = parser.parse_args()
#     try:
#         s3 = boto3.client('s3', region_name=args.aws_region)
#         response = s3.list_objects_v2(
#                         Bucket=args.bucket,
#                         Prefix=args.prefix
#                     )
#         # print(response) # get the full response
#         for entry in response['Contents']:
#             print(entry["Key"])

#     except botocore.exceptions.ClientError as err:
#         if err.response['Error']['Code'] == 'NoSuchBucket':
#             print(f"\nThe bucket named {args.bucket} does not exist on the {args.aws_region} region\n")
#             print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
#             print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
#         else:
#             print("Error occured : ", err)

if __name__ == "__main__":
    print(list_bucket_objects())
