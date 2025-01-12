
# 🌟 Serverless Image Processing Pipeline

## 📌 Overview
This project demonstrates a serverless image processing pipeline using **AWS Lambda**, **Amazon S3**, and **Amazon SNS**. The pipeline automatically:
- 🖼️ Resizes images uploaded to an S3 bucket.
- 📂 Stores the resized images in a target S3 bucket.
- ✉️ Sends notifications via SNS upon successful processing.

---

## ✨ Features
- ⚡ Fully serverless architecture using AWS.
- 🛠️ Automatically resizes images to a predefined width while maintaining aspect ratio.
- 📤 Stores processed images in a separate S3 bucket.
- 🔔 Sends notifications via Amazon SNS.
- 🕒 Scalable, cost-effective, and highly available.

---

## 🛠️ Architecture
- **📂 S3 Buckets**:
  - `my-original-images`: Stores original uploaded images.
  - `my-processed-images`: Stores resized images.
- **⚡ AWS Lambda**:
  - Automatically triggered by new uploads to the source S3 bucket.
  - Resizes images using the Python **Pillow** library.
- **🔔 Amazon SNS**:
  - Sends notifications when images are processed successfully.

---

## 💻 Technologies Used
- **AWS Services**:
  - 📂 S3
  - ⚡ Lambda
  - 🔔 SNS
  - 📊 CloudWatch (for logging)
- **Python Libraries**:
  - 🐍 Boto3 (AWS SDK for Python)
  - 🖼️ Pillow (for image processing)

---

## 🚀 Setup Instructions

### ✅ Prerequisites
- 🌐 An AWS account with access to Lambda, S3, and SNS.
- 🐍 Python 3.8+ installed locally for testing and deployment.

### 📂 Step 1: Set Up AWS Resources
1. **Create two S3 buckets**:
   - 🟦 `my-original-images`: For uploaded images.
   - 🟩 `my-processed-images`: For resized images.
2. **Create an SNS topic**:
   - ✉️ Add your email as a subscriber for notifications.
3. **IAM Role**:
   - Assign permissions to your Lambda function:
     - 🛡️ `AmazonS3FullAccess`
     - 🛡️ `AmazonSNSFullAccess`.

---

### ⚡ Step 2: Deploy the Lambda Function
1. **Create a Lambda function** in the AWS Console.
2. Copy and paste the function code into the editor.
3. Add the environment variable:
   - 🔧 `SNS_TOPIC_ARN`: The ARN of your SNS topic.

---

### 🔗 Step 3: Configure S3 Trigger
1. Go to the `my-original-images` bucket.
2. Set up a trigger to invoke your Lambda function on `PUT` events.

---

### 📤 Step 4: Test the Pipeline
1. Upload an image to the `my-original-images` bucket.
2. 🔍 Check the `my-processed-images` bucket for the resized image.
3. 📧 Verify you received an SNS email notification.

---

## 📈 Results
- 🖼️ Resized images are successfully uploaded to the target bucket.
- 🔔 Notifications are sent via SNS for each processed image.
- 📊 Logs are available in CloudWatch for troubleshooting and monitoring.

---

## 🤝 Contributions
Feel free to:
- Report issues 🐛
- Submit pull requests ✨
- Suggest improvements 🚀

---


