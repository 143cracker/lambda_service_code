import json
from typing import Optional  # Importing Optional from the typing module

def lambda_handler(event, context):
    # Retrieve data from request body
    try:
        body = json.loads(event['body'])
        id = body.get('id')
        weather = body.get('Weather')
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Request body is missing.'})
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid JSON format in request body.'})
        }
    
    # Validate presence of 'id' and 'Weather' attributes
    if not id or not weather:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Both "id" and "Weather" attributes are required.'})
        }
    
    # Validate absence of any other attributes
    if set(body.keys()) - {'id', 'Weather'}:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Only "id" and "Weather" attributes are allowed.'})
        }

    # Update DynamoDB
    # Your code to update DynamoDB here

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data updated successfully.'})
    }
