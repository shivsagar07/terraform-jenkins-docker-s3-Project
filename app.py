import boto3

s3 = boto3.client('s3')

bucket_name = "shivsagar-devops-s3-backend-12345"

s3.put_object(
    Bucket=bucket_name,
    Key="app-data.txt",
    Body="Data stored in S3 backend without database"
)

print("Data stored in S3 successfully")
