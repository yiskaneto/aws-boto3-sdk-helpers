import argparse

AWS_REGION_CONST = "Target AWS region where to perform the action"

## Bucket
###############################################################################
def bucket_args():
    """
    Initializes the arguments needed to excecute operations on a given S3 bucket.

    Example
    -------
    a_bucket_function(bucket_args())
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", required=True, help="Name of the bucket")
    parser.add_argument("--aws-region", required=True, help=AWS_REGION_CONST)
    parser.add_argument("--prefix", required=True, help="Buckets Prefix")
    args = parser.parse_args()
    return args

###############################################################################

## CloudWatch Logs
###############################################################################
def cloudwatch_logs_args():
    """
    Initializes the arguments needed to excecute operations on a given cloudwatch log group.

    Example
    -------
    a_cloudwatch_log_group_function(cloudwatch_logs_args())
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--group-name", required=True, help="CloudWatch log group name")
    parser.add_argument("--aws-region", required=True, help=AWS_REGION_CONST)
    args = parser.parse_args()
    return args
#################################################################################

if __name__ == "__main__":
    print("Test")
