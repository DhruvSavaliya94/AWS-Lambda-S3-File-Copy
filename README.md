# AWS Lambda S3 File Copy Tutorial
## Overview

This tutorial guides you through creating an AWS Lambda function to automatically copy new files from one S3 bucket (source) to another (destination). This is an example to learn AWS Lambda and S3 integration.

## Prerequisites
- An AWS account.
- Basic knowledge of Python.
- Git installed on your machine.
- AWS CLI installed and configured (optional but recommended).

## Step 1: Clone the Repository
1. Clone the project repository from Git.
```bash
git clone https://github.com/DhruvSavaliya94/AWS-Lambda-S3-File-Copy.git
```
2. Navigate to the project root directory.
```bash
cd AWS-Lambda-S3-File-Copy
```
## Step 2: Install Dependencies
1. Install required Python packages from requirements.txt.
```bash
pip install -r requirements.txt
```
## Step 3: Set Up Your S3 Buckets
1. Log into **AWS Management Console**.
2. Navigate to **S3** and create two buckets: one for the source and one for the destination. **Note** the names of these buckets.

## Step 4: Create IAM Role and Policy
### Create the IAM Policy
1. Open the **AccessS3SourceDestinationPolicy.json** file from the project folder. This file contains the necessary permissions for the Lambda function.
2. Log into the AWS Management Console and go to the **IAM** service.
3. Navigate to **Policies** and click **Create policy**. Switch to the **JSON** tab.
4. Copy and paste the content of AccessS3SourceDestinationPolicy.json into the JSON editor.
5. Click **Review policy**.
6. Name the policy **AccessS3SourceDestinationPolicy** and provide a description. Click **Create policy**.

### Create the IAM Role for Lambda
1. In the IAM console, navigate to **Roles** and click **Create role**.
2. Choose **Lambda** as the **trusted entity** for the role.
3. Click Next: **Permissions**.
4. Search for and attach the **AccessS3SourceDestinationPolicy** policy you just created.
5. Click Next: Review.
6. Name the role (e.g., **LambdaS3CopyRole**) and provide a description.
7. Click **Create role**.

## Step 5: Create the Lambda Function
1. Navigate to the **AWS Lambda** service in the AWS Management Console.
2. Click **Create Function**.
3. Choose **Author from scratch**, enter a function name, and select **Python** as the runtime.
4. Select role **LambdaS3CopyRole**.
5. Click **Create Function**.

## Step 6: Deploy the Lambda Function
1. Open the Lambda function you created earlier.
2. In the **Function code** section, find the option to upload a file from your machine.
3. Copy python code from project and past it in lambda function.
4. Deploy the function by clicking **Deploy**.
5. Your function is now ready.

## Step 7: Configure Environment Variables
1. In your Lambda function, under the **Configuration** tab, find **Environment** variables.
2. Add a new variable: Key as **DESTINATION_BUCKET** and Value as your destination bucket name.

## Step 8: Set Up the Trigger
1. In your Lambda function, under the Designer section, click **Add trigger**.
2. Select **S3** from the dropdown.
3. Choose your **source S3 bucket** and set the Event type to **PUT**.
4. Click **Add**.

## Step 9: Test and Verify
1. Upload a file to your source S3 bucket.
2. Check the destination S3 bucket to see if the file has been copied.
3. Optionally, check CloudWatch logs for your Lambda function for logs and potential errors.