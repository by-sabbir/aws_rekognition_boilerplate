import os
import json
import boto3

if __name__ == "__main__":
    bucket = None # your bucket
    collectionId = None # your collection
    photos = os.listdir('imgs/')  # replace with your image path

    client = boto3.client('rekognition')

    for photo in photos:
        response = client.index_faces(CollectionId=collectionId,
                                      Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                      ExternalImageId=photo,
                                      MaxFaces=1,
                                      QualityFilter="AUTO",
                                      DetectionAttributes=['ALL'])

        print('Results for ' + photo)
        print('Faces indexed:')
        # use json format I was just too lazy to do it back then
        with open('face_index.log', 'a') as log:
            data = photo.split('.')[0] + " --> " + json.dumps(response) + ', '
            log.write(data)

        for faceRecord in response['FaceRecords']:
            print('  Face ID: ' + faceRecord['Face']['FaceId'])
            print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

        print('Faces not indexed:')
        for unindexedFace in response['UnindexedFaces']:
            print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
            print(' Reasons:')
            for reason in unindexedFace['Reasons']:
                print('   ' + reason)
