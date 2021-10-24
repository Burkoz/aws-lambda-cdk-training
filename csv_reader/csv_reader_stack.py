from aws_cdk import (aws_iam as iam,
             aws_lambda as _lambda,
             aws_s3 as s3,
             aws_s3_notifications as s3_notify,
             aws_dynamodb as dynamodb,
             core as cdk)


class CsvReaderStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
     
        role = iam.Role(self, "LambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"))

        bucket = s3.Bucket(self, 'bucket',
                        removal_policy=cdk.RemovalPolicy.DESTROY,
                        auto_delete_objects=True
        )

        table = dynamodb.Table(self, "Table",
                        table_name='csvTable',
                        removal_policy=cdk.RemovalPolicy.DESTROY,
                        partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING))


        lambda_func = _lambda.Function(self, 'csvreader',
                       runtime=_lambda.Runtime.PYTHON_3_8,
                       handler='csvreader.handler',
                       role=role,
                       code=_lambda.Code.asset('lambda'),
                       environment={'BUCKET_NAME':
                                    bucket.bucket_name})

         
        notification = s3_notify.LambdaDestination(lambda_func)
        notification.bind(self, bucket)
        bucket.add_object_created_notification(
            notification, s3.NotificationKeyFilter(suffix='.csv'))