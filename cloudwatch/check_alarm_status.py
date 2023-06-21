"""
check_alarm_status.py determines whether the passed alarm is in the expected state, which is passed to the --alarm_status flag.
All options can be found at https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/describe_alarms.html
Be aware that not all options can be use at the same time
"""

import boto3, botocore
import argparse


exceptions = ["InvalidNextToken"]

def flag_init():
    """
    Init flags required by the module
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--alarm_name", required=True, help="Name of the alarm")
    parser.add_argument("--alarm-status", required=True, help="Alarm status")
    parser.add_argument("--aws_region", required=True, help="AWS region where to run the script")
    args = parser.parse_args()
    return args

def cw_describe_alarms():
    """
    cw_describe_alarms describes the passed alarm
    """
    args = flag_init()
    client = boto3.client('cloudwatch',region_name=args.aws_region)
    try:
        response = client.describe_alarms(
            AlarmNames=[f"{args.alarm_name}"],
            AlarmTypes=['MetricAlarm'],
            StateValue=f"{args.alarm_status}",
            MaxRecords=1,
        )
        if len(response['MetricAlarms']) < 1:
            return f'''                
            ERROR: The {args.alarm_name} alarm does not have a record with status "{args.alarm_status}"
            '''
        elif response['MetricAlarms'][0]['StateValue'] == args.alarm_status:
            return f'''
            SUCCESS: The current state of the {response['MetricAlarms'][0]['AlarmName']} alarm is: {args.alarm_status}
            '''
    except botocore.exceptions.ClientError as error_found:
        if error_found.response['Error']['Code'] in exceptions:
            print(f"Error Code: {format(error_found.response['Error']['Code'])}")
            print(f"Message: {format(error_found.response['Error']['Message'])}")
            print(f"Request ID: {format(error_found.response['ResponseMetadata']['RequestId'])}")
            print(f"Http code: {format(error_found.response['ResponseMetadata']['HTTPStatusCode'])}")   
        else:
            print(f"Error occured : {error_found}")

print(cw_describe_alarms())
