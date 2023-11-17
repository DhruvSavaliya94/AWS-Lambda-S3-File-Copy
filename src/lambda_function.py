import boto3
import botocore
import os
import logging
from urllib.parse import unquote_plus

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    logger.info("New files uploaded to the source bucket.")
        
    # Decode the key
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    destination_bucket = os.environ['DESTINATION_BUCKET']
    
    source = {'Bucket': source_bucket, 'Key': key}
        
    try:
        response = s3.meta.client.copy(source, destination_bucket, key)
        logger.info("File copied to the destination bucket successfully!")
        
    except botocore.exceptions.ClientError as error:
        logger.error("There was an error copying the file to the destination bucket")
        logger.error('Error Message: {}'.format(error))
        
    except botocore.exceptions.ParamValidationError as error:
        logger.error("Missing required parameters while calling the API.")
        logger.error('Error Message: {}'.format(error))
