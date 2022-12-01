import boto3
import time
import os
from dotenv import load_dotenv

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
    
    model_arn=os.getenv("MODEL_ARN")
    print(model_arn)
    stop_model(model_arn)

if __name__ == "__main__":
    load_dotenv()
    main()
