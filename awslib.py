import json
import boto3
import botocore


def search_by_id(search_id):
    """
        data.json - assuming format
        {
            'name': (str) name,
            'search_id': (int) search_id
            'profile_pic': (str) public_url; 
        }
    """
    with open('data.json', 'r') as u:
        all_data = json.load(u)

    for data in all_data:
        if data['search_id'] == search_id:
            print(data['name'])


def detect(frame):

    collectionId = None # Your Collection ID

    threshold = 70
    maxFaces = 10

    client = boto3.client('rekognition')

    response = client.search_faces_by_image(CollectionId=collectionId,
                                            Image={"Bytes": frame},
                                            FaceMatchThreshold=threshold,
                                            MaxFaces=maxFaces)

    faceMatches = response['FaceMatches']
    print('Matching faces')
    for match in faceMatches:
        # print('FaceId:' + match['Face']['ExternalImageId'])
        search_id = match['Face']['ExternalImageId'].split('.')[0]
        if match['Similarity'] > 85:
            print('*' * 80)
            search_by_id(int(search_id))
            print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            print('*' * 80)


if __name__ == '__main__':
    # replace 'test/test2.jpg' with your test image
    img = open('test/test2.jpg', 'rb').read()
    detect(img)
