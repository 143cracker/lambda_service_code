import json

def lambda_handler(event, context):
    # Assuming 'id' is passed in the path parameters
    id = event.get('pathParameters', {}).get('id')

    # Validate presence of 'id'
    if not id:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Missing "id" parameter in path.'})
        }

    # Delete record from DynamoDB
    # Your code to delete from DynamoDB here

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Record with id {id} deleted successfully.'})
    }
