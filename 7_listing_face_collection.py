import json
import boto3
from time import sleep

if __name__ == "__main__":
    bucket = None
    collectionId = None
    maxResults = 2
    tokens = True

    client = boto3.client('rekognition')
    response = client.list_faces(CollectionId=collectionId,
                                 MaxResults=maxResults)

    print('Faces in collection ' + collectionId)
    emp_biometrics = []
    count = 0
    while tokens:
        if count % 10 == 0:
            sleep(2)
        faces = response['Faces']
        for face in faces:
            count += 1
            biometrics = dict(emp_id=face['ExternalImageId'].split('.')[0], face_id=face['FaceId'])
            print(biometrics)
            emp_biometrics.append(biometrics)

        if 'NextToken' in response:
            nextToken = response['NextToken']
            response = client.list_faces(CollectionId=collectionId,
                                         NextToken=nextToken, MaxResults=maxResults)
        else:
            tokens = False
    print("Total Face Id: ", len(emp_biometrics))
    with open('biometrics.log', 'w') as log:
        data = json.dumps(emp_biometrics)
        log.write(data)
