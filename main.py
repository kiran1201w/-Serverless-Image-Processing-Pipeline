import boto3
from PIL import Image
import os
import io

# Initialize AWS clients
s3 = boto3.client('s3')
sns = boto3.client('sns')
topic_arn = os.environ['SNS_TOPIC_ARN']

def resize_image(image_data, resize_width):
    """
    Resize the image to the specified width while maintaining aspect ratio.
    """
    with Image.open(io.BytesIO(image_data)) as img:
        width, height = img.size
        aspect_ratio = height / width
        new_height = int(resize_width * aspect_ratio)
        img_resized = img.resize((resize_width, new_height))
        buffer = io.BytesIO()
        img_resized.save(buffer, format=img.format)
        buffer.seek(0)
        return buffer

def lambda_handler(event, context):
    """
    Triggered by an S3 upload event. Resizes the image and stores it in another S3 bucket.
    """
    try:
        # Parse the S3 event
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        print(f"Processing file {object_key} from bucket {source_bucket}")
        
        # Download the original image
        response = s3.get_object(Bucket=source_bucket, Key=object_key)
        image_data = response['Body'].read()
        
        # Resize the image
        resized_image = resize_image(image_data, resize_width=800)
        
        # Upload the resized image to the target bucket
        target_bucket = 'my-processed-images'
        s3.put_object(
            Bucket=target_bucket,
            Key=f"resized-{object_key}",
            Body=resized_image,
            ContentType=response['ContentType']
        )
        print(f"Resized image uploaded to {target_bucket}/resized-{object_key}")
        
        # Notify via SNS
        sns.publish(
            TopicArn=topic_arn,
            Message=f"Image {object_key} has been resized and uploaded to {target_bucket}/resized-{object_key}"
        )
        print("Notification sent via SNS")
        
        return {
            'statusCode': 200,
            'body': 'Image processed successfully!'
        }
    
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return {
            'statusCode': 500,
            'body': 'Error processing image'
        }
