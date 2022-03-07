import json
import boto3
import os

# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
#ddbTableName = os.environ['databaseName']
ddbTableName = 'databaseName'
table = dynamodb.Table(ddbTableName)

def lambda_handler(event, context):

    response = table.get_item(Key= {'id' : 'visitor_count'} )
    
    count = response["Item"]["vis_counter"]

    # Update item in table or add if doesn't exist
    new_count = str(int(count)+1)
    ddbResponse = table.update_item(
        Key={
            'id':'visitor_count'
        },
        UpdateExpression='SET vis_counter = vis_counter + :value',
        ExpressionAttributeValues={
            ':value':1
        },
        ReturnValues="UPDATED_NEW"
    )
    
    return {
        "count" : new_count
    }