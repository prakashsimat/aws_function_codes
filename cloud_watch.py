import boto3
import random
import time

def simulate_user_activity(cloudwatch, user_name):
    cpu_usage = random.uniform(0, 100)
    memory_usage = random.uniform(0, 100)
    network_usage = random.uniform(0, 100)
    login_time = random.uniform(0, 24 * 3600)  # login time in seconds
    file_access_count = random.randint(0, 20)

    cloudwatch.put_metric_data(
        Namespace='UserActivity',
        MetricData=[
            {
                'MetricName': 'CPUUsage',
                'Dimensions': [
                    {
                        'Name': 'UserName',
                        'Value': user_name
                    },
                ],
                'Value': cpu_usage,
                'Unit': 'Percent'
            },
            {
                'MetricName': 'MemoryUsage',
                'Dimensions': [
                    {
                        'Name': 'UserName',
                        'Value': user_name
                    },
                ],
                'Value': memory_usage,
                'Unit': 'Percent'
            },
            {
                'MetricName': 'NetworkUsage',
                'Dimensions': [
                    {
                        'Name': 'UserName',
                        'Value': user_name
                    },
                ],
                'Value': network_usage,
                'Unit': 'Percent'
            },
            {
                'MetricName': 'LoginTime',
                'Dimensions': [
                    {
                        'Name': 'UserName',
                        'Value': user_name
                    },
                ],
                'Value': login_time,
                'Unit': 'Seconds'
            },
            {
                'MetricName': 'FileAccessCount',
                'Dimensions': [
                    {
                        'Name': 'UserName',
                        'Value': user_name
                    },
                ],
                'Value': file_access_count,
                'Unit': 'Count'
            },
        ]
    )
    print(f"Simulated activity for {user_name}: CPU {cpu_usage}, Memory {memory_usage}, Network {network_usage}, Login {login_time}, Files {file_access_count}")

def simulate_activities_for_all_users():
    cloudwatch = boto3.client('cloudwatch')
    for i in range(1, 51):
        user_name = f"user{i}"
        simulate_user_activity(cloudwatch, user_name)
        time.sleep(random.uniform(1, 5))  # Simulate time delay between activities

if __name__ == "__main__":
    simulate_activities_for_all_users()
