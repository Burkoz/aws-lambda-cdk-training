import boto3
import os
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('csvTable')

def handler(event, context):
    bucket_name = (os.environ['BUCKET_NAME'])
    key = event['Records'][0]['s3']['object']['key']

    csv = s3.get_object(Bucket=bucket_name,Key=key)
    content = csv['Body'].read().decode("utf-8")
    rows=content.split("\n")


    for row in rows:
        rows_data = row.split(",")
        
        try:

            table.put_item(
            Item = {
                "id" : rows_data[0],
                "last_name" : rows_data[1],
                "name" : rows_data[2]
            }
        )

        except Exception as e:
            print(e)

