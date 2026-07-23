---
title: "Các bước chuẩn bị"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

#### Các công cụ và tài khoản cần thiết

Hãy chuẩn bị các tài nguyên sau trước khi bắt đầu:

- Một tài khoản AWS có quyền khởi tạo các tài nguyên: Cognito, Lambda, API Gateway, DynamoDB, S3, SQS, CloudWatch, SNS, Budgets, Amplify, CloudFront và WAF.
- Một repository chứa mã nguồn frontend, ví dụ ứng dụng React/Vite SPA, đã được push lên GitHub để Amplify có thể tiến hành triển khai.
- Một dự án Google Cloud nếu bạn muốn Cognito Hosted UI hỗ trợ tính năng đăng nhập bằng Google.
- Một tài khoản và API key từ Groq để xử lý hoàn thiện mô hình AI (AI model completion).
- Một URL thử nghiệm cục bộ, chẳng hạn như `http://localhost:5173`, phục vụ cho quá trình phát triển frontend.

#### Quy chuẩn đặt tên

Sử dụng tên gọi thống nhất để các bước tiếp theo dễ theo dõi hơn:

- Cognito user pool: `AI-Personal-Learning-UserPool`
- Main Lambda API: `AI-Personal-Learning-Handle`
- Lambda AI Worker: `AI-Personal-Learning-Worker`
- HTTP API: `AI-Personal-Learning-API`
- S3 bucket: `learnflow-journal-images-<hậu-tố-duy-nhất>`
- Bảng DynamoDB: `JournalLogs`, `AiReports`, `Quizzes`, `QuizAttempts`
- Hàng chờ SQS: `ai-report-jobs`, `quiz-jobs`, cùng với một DLQ dùng chung hoặc riêng cho từng tác vụ

#### Chuẩn bị về bảo mật

- Tuyệt đối không lưu trực tiếp Groq API key trong mã nguồn. Hãy lưu trữ trong biến môi trường của Lambda hoặc sử dụng AWS Secrets Manager.
- Sử dụng Cognito JWT authorizers cho tất cả các tuyến API dành riêng cho người dùng.
- Luôn bật tính năng Block Public Access của S3 và chỉ cung cấp quyền truy cập hình ảnh thông qua presigned URL.
- Áp dụng chính sách phân quyền IAM tối thiểu (least-privilege) bất cứ khi nào có thể. Các chính sách cấp toàn quyền có sẵn (managed full-access) có thể chấp nhận cho mục đích demo workshop ngắn hạn, nhưng cần được thu hẹp lại trước khi đưa vào môi trường sản phẩm (production).

#### Khu vực (Region)

Nội dung workshop gốc sử dụng khu vực **ap-southeast-1 (Singapore)** cho Lambda, S3, SQS và DynamoDB. Hãy nhất quán sử dụng một Khu vực duy nhất trừ khi bạn cố ý tách riêng các dịch vụ cạnh (edge services) như CloudFront và WAF.
