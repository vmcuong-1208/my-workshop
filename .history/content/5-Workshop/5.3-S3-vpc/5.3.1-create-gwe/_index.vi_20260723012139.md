---
title : "Tạo một Gateway Endpoint"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.3.1 </b> "
---

# Cấu hình Cognito và API Gateway

#### Tạo một Cognito user pool

1. Mở **Amazon Cognito** và chọn **User pools**.
2. Chọn **Create user pool**.
3. Trong **Define your application**, chọn **Single-page application (SPA)**.
4. Trong **Options for sign-in identifiers**, chọn **Email**.
5. Trong **Required attributes for sign-up**, chọn **email** và **name**.
6. Tạo thư mục người dùng (user directory).
7. Cập nhật chính sách mật khẩu để yêu cầu tối thiểu 10 ký tự, có chữ hoa và số.

#### Cấu hình Hosted UI và đăng nhập bằng Google

1. Tạo một Cognito domain cho Hosted UI.
2. Trong Google Cloud, cấu hình màn hình đồng ý OAuth (OAuth consent screen).
3. Tạo một OAuth Client ID cho Cognito Hosted UI.
4. Thêm Google client ID và secret vào Cognito.
5. Bật Google làm nhà cung cấp danh tính (identity provider) trong Hosted UI.
6. Cấu hình callback URL và sign-out URL:

```text
Allowed callback URL: http://localhost:5173/auth/google/callback
Allowed sign-out URL: http://localhost:5173
```

#### Tạo Lambda API chính

1. Mở **AWS Lambda** và chọn **Create function**.
2. Chọn **Author from scratch**.
3. Tên function: `AI-Personal-Learning-Handle`.
4. Runtime: Node.js 22.x hoặc phiên bản Node.js mới nhất được hỗ trợ trong tài khoản của bạn.
5. Tạo function và triển khai (deploy) mã xử lý (handler code).

Sử dụng đoạn mã handler đầy đủ sau cho `index.mjs`. Cập nhật `BUCKET_NAME`, các queue URL, và tên bảng nếu bạn dùng tên khác.

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
  DynamoDBDocumentClient,
  QueryCommand,
  GetCommand,
  PutCommand,
  DeleteCommand,
} from "@aws-sdk/lib-dynamodb";
import { S3Client, PutObjectCommand, GetObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import { SQSClient, SendMessageCommand } from "@aws-sdk/client-sqs";

const REGION = process.env.AWS_REGION || "ap-southeast-1";
const TABLE_NAME = process.env.JOURNAL_TABLE || "JournalLogs";
const BUCKET_NAME = process.env.IMAGE_BUCKET || "learnflow-journal-images-demo";
const AI_REPORT_TABLE = process.env.AI_REPORT_TABLE || "AiReports";
const QUIZ_TABLE = process.env.QUIZ_TABLE || "Quizzes";
const QUIZ_ATTEMPT_TABLE = process.env.QUIZ_ATTEMPT_TABLE || "QuizAttempts";
const AI_REPORT_QUEUE_URL = process.env.AI_REPORT_QUEUE_URL;
const QUIZ_QUEUE_URL = process.env.QUIZ_QUEUE_URL;

const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({ region: REGION }));
const s3Client = new S3Client({ region: REGION });
const sqsClient = new SQSClient({ region: REGION });

const headers = {
  "Content-Type": "application/json",
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Content-Type,Authorization",
  "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT,DELETE",
};

const response = (statusCode, body) => ({
  statusCode,
  headers,
  body: JSON.stringify(body),
});

async function attachSignedUrlsToImages(images = []) {
  if (!Array.isArray(images)) return [];

  return Promise.all(
    images.map(async (img) => {
      const imageKey =
        typeof img === "string" ? img : img.image_key || img.imageKey || img.key || img.image_url;

      if (!imageKey || imageKey.startsWith("http")) {
        return typeof img === "string" ? { image_key: img, image_url: img } : img;
      }

      const command = new GetObjectCommand({ Bucket: BUCKET_NAME, Key:
      // (đoạn mã bị cắt ngang trong HTML gốc — không đầy đủ)
```