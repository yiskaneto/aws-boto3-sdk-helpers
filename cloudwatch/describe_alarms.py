import boto3, botocore
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--alarm_name", help="Name of the alarm")
parser.add_argument("--aws_region", help="aws region where to look for the bucket")
args = parser.parse_args()

exceptions = ["InvalidNextToken"]

try:
    client = boto3.client('cloudwatch', region_name=args.aws_region)
    response = client.describe_alarms(
        AlarmNames=[
            'string',
        ],
        AlarmNamePrefix='string',
        AlarmTypes=[
            'CompositeAlarm'|'MetricAlarm',
        ],
        ChildrenOfAlarmName='string',
        ParentsOfAlarmName='string',
        StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
        ActionPrefix='string',
        MaxRecords=123,
        NextToken='string'
    )
    # print(f"LocationConstraint: {response['LocationConstraint']}")

except botocore.exceptions.Clienterror_foundor as error_found:
    if error_found.response['error_foundor']['Code'] in exceptions:
        print(f"error_foundor Code: {format(error_found.response['error_foundor']['Code'])}")
        print(f"Message: {format(error_found.response['error_foundor']['Message'])}")
        print(f"Request ID: {format(error_found.response['ResponseMetadata']['RequestId'])}")
        print(f"Http code: {format(error_found.response['ResponseMetadata']['HTTPStatusCode'])}")   
    else:
        print(f"error_foundor occured : {error_found}")
