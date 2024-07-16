import base64
import datetime
import json

import boto3

Bucket = "movieposterdesign13"


def lambda_handler(event, context):
    print("boto3 version", boto3.__version__)

    input_prompt = event['prompt']
    print("input_prompt", input_prompt)

    client_bedrock = boto3.client('bedrock-runtime')
    client_s3 = boto3.client('s3')

    with open("my_img.jpg", "rb") as image_file:
        init_image = base64.b64encode(image_file.read()).decode('utf8')

    response_bedrock = client_bedrock.invoke_model(contentType='application/json', accept='application/json',
                                                   modelId='stability.stable-diffusion-xl-v1',
                                                   body=json.dumps(
                                                       {
                                                           "text_prompts": [
                                                               {
                                                                   "text": input_prompt,
                                                                   "weight": 1
                                                               }
                                                           ],
                                                           "cfg_scale": 10,
                                                           "seed": 0,
                                                           "steps": 50,
                                                           "width": 512,
                                                           "height": 512,
                                                           "init_image": init_image,
                                                           "style_preset": "anime"
                                                       }
                                                   ))

    response_bedrock_byte = json.loads(response_bedrock['body'].read())
    response_bedrock_base64 = response_bedrock_byte['artifacts'][0]['base64']
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)
    poster_name = 'posterName_' + datetime.datetime.today().strftime('%Y-%m-%d/%H-%M-%S') + ".jpg"
    client_s3.put_object(
        Bucket=Bucket,
        Body=response_bedrock_finalimage,
        Key=poster_name)

    generate_presigned_url = client_s3.generate_presigned_url('get_object', Params={'Bucket': Bucket,
                                                                                    'Key': poster_name}, ExpiresIn=3600)
    print("generate_presigned_url", generate_presigned_url)
    return {
        'statusCode': 200,
        'body': generate_presigned_url
    }


lambda_handler(event={"prompt": "Make the person in the photo look really handsome"}, context=None)
