import argparse

def args_init():
    """
    Initializes the arguments needed for the bucket operations.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", required=True, help="Name of the bucket")
    parser.add_argument("--aws_region", required=True, help="aws region where to look for the bucket")
    parser.add_argument("--prefix", required=False, help="Buckets Prefix")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    print(args_init())
