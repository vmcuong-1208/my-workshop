---
title: "Chuẩn bị"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

## Tài khoản và công cụ cần có

Chuẩn bị những thứ sau trước khi bắt đầu:

- Tài khoản AWS có quyền tạo **Cognito**, **Lambda**, **API Gateway**, **DynamoDB**, **S3**, **SQS**, **CloudWatch**, **SNS**, **Budgets**, **Amplify**, **CloudFront** và **WAF**.
- Kho lưu trữ frontend, ví dụ một React/Vite SPA đã push lên GitHub để Amplify triển khai.
- Dự án Google Cloud nếu bạn muốn Cognito Hosted UI hỗ trợ đăng nhập bằng Google.
- Tài khoản Groq và API key để gọi mô hình AI.
- URL phát triển cục bộ như `http://localhost:5173` để test frontend.

## Quy ước đặt tên đề xuất

Dùng tên thống nhất để làm workshop dễ theo dõi hơn:

- Cognito user pool: `AI-Personal-Learning-UserPool`
- Lambda API chính: `AI-Personal-Learning-Handle`
- Lambda AI Worker: `AI-Personal-Learning-Worker`
- HTTP API: `AI-Personal-Learning-API`
- Bucket S3: `learnflow-journal-images-<unique-suffix>`
- Bảng DynamoDB: `JournalLogs`, `AiReports`, `Quizzes`, `QuizAttempts`
- Queue SQS: `ai-report-jobs`, `quiz-jobs` và DLQ như `ai-report-dlq`, `quiz-dlq`

## Chuẩn bị bảo mật

- Không hardcode Groq API key vào source code. Nên lưu trong Lambda environment variables hoặc AWS Secrets Manager.
- Dùng Cognito JWT authorizer cho tất cả các route riêng tư của người dùng.
- Giữ S3 Block Public Access bật và chỉ cho phép truy cập ảnh qua presigned URL.
- Với workshop ngắn, có thể dùng IAM managed policy tạm thời, nhưng nên thu hẹp quyền trước khi đưa vào production.

## Region

Nên dùng một AWS Region thống nhất. Trong sample workshop, region mặc định là **ap-southeast-1 (Singapore)** cho Lambda, S3, SQS và DynamoDB.
