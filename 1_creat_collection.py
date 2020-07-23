
import json
import boto3

if __name__ == "__main__":

    maxResults = 2
    collectionId = None # use your collectionID

    client = boto3.client('rekognition')

    # Create a collection
    print('Creating collection:' + collectionId)
    response = client.create_collection(CollectionId=collectionId)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')

    with open('collection_det.log', 'w') as log:
        log.write(json.dumps(response))
