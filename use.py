import boto3
import os
from dotenv import load_dotenv

def show_custom_labels(model,bucket,photo, min_confidence):
    client=boto3.client('rekognition')
    response = client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, ProjectVersionArn=model)
    print(response["CustomLabels"])
    return len(response['CustomLabels'])

def get_label(bytes):
    load_dotenv()
    model=os.getenv("MODEL_ARN")
    client=boto3.client('rekognition')
    response = client.detect_custom_labels(Image={'Bytes' : bytes}, MaxResults=1, ProjectVersionArn=model)
    print(response["CustomLabels"])
    return response["CustomLabels"][0]["Name"]

# def main():
#     bucket='face-rekognition-testing'
#     photo='collage.jpg'
#     model='arn:aws:rekognition:us-east-1:843645451050:project/face_recognition_model/version/face_recognition_model.2022-11-30T21.22.27/1669823552738'
#     min_confidence=0
#     label_count=show_custom_labels(model,bucket,photo, min_confidence)
#     print("Custom labels detected: " + str(label_count))


if __name__ == "__main__":
    main()
