import json
import boto3

if __name__ == "__main__":

    maxResults = 2
    collectionId = None # replace with your collectionId
    client = boto3.client('rekognition')

    # Create a collection
    print('Creating collection:' + collectionId)
    response = client.create_collection(CollectionId=collectionId)
    with open('collection.log', 'w') as log:
        log.write(json.dumps(response))
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
