# aws-lambda-cdk-training 
This AWS CDK project is developed with Python.
## Description
When a CSV file uploaded to AWS S3 bucket, the AWS Lambda function will trigger and parse the contant of the CSV file and the data will be added to DynamoDB. The entire infrastructure of the application is created with AWS CDK.
## Usage
Setup AWS and CDK for the development environment<br/>
Before starting, you will need to do three things;<br/>

- Set up AWS CLI<br/>
- Configure AWS CLI with IAM Credentials<br/>
- Set up AWS CDK
##### How to run the project
`git clone https://github.com/Burakolum/aws-lambda-cdk-training.git`<br/>

Activate your virtualenv for Linux and MacOS<br/>
`source .venv/bin/activate`<br/>

Run the below command to install the required dependencies<br/>
`pip install -r requirements.txt`<br/>

Deploy our app on the cloud<br/>
`cdk deploy`<br/>
