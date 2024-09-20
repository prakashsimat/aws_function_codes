import boto3
import json

# Initialize boto3 clients
iam_client = boto3.client('iam')
policy_name = 'PutMetricDataPolicy'

# Define the IAM policy
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData"
            ],
            "Resource": "*"
        }
    ]
}

def create_policy(policy_name, policy_document):
    try:
        response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document)
        )
        policy_arn = response['Policy']['Arn']
        print(f"Created policy: {policy_name} with ARN: {policy_arn}")
        return policy_arn
    except iam_client.exceptions.EntityAlreadyExistsException:
        response = iam_client.get_policy(PolicyArn=f'arn:aws:iam::aws:policy/{policy_name}')
        policy_arn = response['Policy']['Arn']
        print(f"Policy {policy_name} already exists with ARN: {policy_arn}")
        return policy_arn

def attach_policy_to_user(user_name, policy_arn):
    try:
        iam_client.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
        print(f"Attached policy {policy_arn} to user {user_name}")
    except Exception as e:
        print(f"Failed to attach policy to user {user_name}: {e}")

def attach_policy_to_existing_users(user_list):
    policy_arn = create_policy(policy_name, policy_document)
    for user_name in user_list:
        attach_policy_to_user(user_name, policy_arn)

if __name__ == "__main__":
    # List of existing user names
    existing_users = [f"user{i}" for i in range(51, 59)]
    attach_policy_to_existing_users(existing_users)
