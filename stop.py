import boto3
import time


def stop_model(model_arn):

    client=boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    #Stop the model
    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Done...')
    
def main():
    
    model_arn='arn:aws:rekognition:us-east-1:843645451050:project/face_recognition_model/version/face_recognition_model.2022-11-30T21.22.27/1669823552738'
    stop_model(model_arn)

if __name__ == "__main__":
    main() 