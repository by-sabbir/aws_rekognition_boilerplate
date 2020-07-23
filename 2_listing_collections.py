import json
import boto3

maxResult = 5

client = boto3.client('rekognition')

print("Displaying Collection: ")

response = client.list_collections(MaxResults=maxResult)
print(response)
with open('collection_list.log', 'w')as log:
    log.write(json.dumps(response))

while True:
    collections = response['CollectionIds']

    for collection in collections:
        print(collection)
    if 'NextToken' in response:
        nextToken = response['NextToken']
        response = client.list_collections(NextToken=nextToken, MaxResult=maxResult)
        print("tokeninzed: ", response)
    else:
        break
print("Done!...")
