import json
import boto3
import os

# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
#ddbTableName = os.environ['databaseName']
ddbTableName = 'databaseName'
