import argparse
import boto3, botocore

def get_bucket_region():
    """
    Returns the provided bucket's aws region, which comes from the LocationConstraint response field.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", required=True, help="Name of the bucket")
    parser.add_argument("--aws_region", required=True, help="aws region where to look for the bucket")
    args = parser.parse_args()
    try:
        s3 = boto3.client('s3', region_name=args.aws_region)
        response = s3.get_bucket_location(Bucket = args.bucket)
        # print(response) # get the full response
        print(f"LocationConstraint: {response['LocationConstraint']}, see more about this operation at: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html")

    except botocore.exceptions.ClientError as err:
        if err.response['Error']['Code'] == 'NoSuchBucket':
            print(f"\nThe bucket named {args.bucket} does not exist on the {args.aws_region} region\n")
            print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
            print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
        else:
            print("Error occured : ", err)

if __name__ == "__main__":
    # This code will only be executed 
    # if the script is run as the main program
    get_bucket_region()
