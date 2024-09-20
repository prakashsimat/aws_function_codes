import boto3

def create_iam_users():
    iam = boto3.client('iam')
    for i in range(51, 60):
        user_name = f"user{i}"
        try:
            iam.create_user(UserName=user_name)
            print(f"Created user: {user_name}")
        except Exception as e:
            print(f"Could not create user {user_name}: {e}")

if __name__ == "__main__":
    create_iam_users()
