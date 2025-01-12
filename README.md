📌 Overview
This project demonstrates a serverless image processing pipeline using AWS Lambda, Amazon S3, and Amazon SNS. The pipeline automatically:

🖼️ Resizes images uploaded to an S3 bucket.
📂 Stores the resized images in a target S3 bucket.
✉️ Sends notifications via SNS when processing is complete.

✨ Features

⚡ Fully serverless architecture using AWS.
🛠️ Automatically resizes images to a predefined width while keeping the aspect ratio.
📤 Stores processed images in a separate S3 bucket.
🔔 Sends notifications via Amazon SNS.
🕒 Scalable, cost-effective, and highly available.

🛠️ Architecture
This pipeline uses the following AWS services:

📂 S3 Buckets:

my-original-images: Stores original uploaded images.
my-processed-images: Stores resized images.

⚡ AWS Lambda: Automatically triggered by new uploads to the source S3 bucket.
Resizes images using the Python Pillow library.

🔔 Amazon SNS: Notifies users via email after successful image processing.

💻 Technologies Used
AWS Services:
📂 S3
⚡ Lambda
🔔 SNS
📊 CloudWatch (for logging)

Python Libraries:
🐍 Boto3 (AWS SDK for Python)
🖼️ Pillow (for image processing)

🚀 Setup Instructions
✅ Prerequisites
🌐 An AWS account with access to Lambda, S3, and SNS.
🐍 Python 3.8+ installed locally for testing and deployment.

📂 Step 1: Set Up AWS Resources
Create two S3 buckets:
🟦 my-original-images: For uploaded images.
🟩 my-processed-images: For resized images.
Create an SNS topic:
✉️ Add your email as a subscriber for notifications.
IAM Role:
Assign permissions to your Lambda function:
🛡️ AmazonS3FullAccess
🛡️ AmazonSNSFullAccess

⚡ Step 2: Deploy the Lambda Function
Create a Lambda function in the AWS Console.
Copy and paste the Lambda function code into the editor.
Add the environment variable:
🔧 SNS_TOPIC_ARN: The ARN of your SNS topic.

🔗 Step 3: Configure S3 Trigger
Go to the my-original-images bucket.
Set up a trigger to invoke your Lambda function on PUT events.

📤 Step 4: Test the Pipeline
Upload an image to the my-original-images bucket.
🔍 Check the my-processed-images bucket for the resized image.
📧 Verify you received an SNS email notification.



