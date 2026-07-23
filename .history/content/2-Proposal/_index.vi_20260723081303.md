---
title: "Bản đề xuất"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# AI Personal Learning Journal Platform

## Nền tảng nhật ký học tập cá nhân tích hợp AI trên kiến trúc AWS serverless

### 1. Tổng Quan Đề Tài

Đề tài xây dựng một **AI Personal Learning Journal Platform**, một ứng dụng web giúp người học ghi nhật ký học tập hằng ngày, đính kèm ảnh hoặc screenshot, sau đó dùng AI để tạo tóm tắt, báo cáo học tập, quiz ôn tập, tìm kiếm và thống kê tiến độ.

Kiến trúc hiện tại được triển khai theo hướng serverless trên AWS. Frontend được deploy bằng **AWS Amplify Hosting**, phân phối qua **Amazon CloudFront** và bảo vệ bằng **AWS WAF**. Người dùng xác thực bằng **Amazon Cognito**. Backend sử dụng **Amazon API Gateway**, **AWS Lambda**, **Amazon DynamoDB**, **Amazon S3**, **Amazon SQS**, DLQ, **Amazon CloudWatch**, **Amazon SNS**, **AWS Budgets** và **Groq API** để xử lý AI.

Mục tiêu là tạo ra một sản phẩm hỗ trợ học tập có ích, đồng thời thể hiện khả năng thiết kế kiến trúc cloud hiện đại, bảo mật, tối ưu chi phí, xử lý bất đồng bộ và dễ vận hành cho nhóm nhỏ.

### 2. Vấn Đề Cần Giải Quyết

#### Hiện Trạng

Nhật ký học tập thường bị phân tán trong Notion, Google Docs, ảnh chụp màn hình, tin nhắn với mentor hoặc hội thoại AI. Người học khó nhìn lại tiến độ theo thời gian, còn mentor phải đọc nhiều log rời rạc nếu muốn đánh giá quá trình học, lỗi lặp lại và mức độ tiến bộ.

Các công cụ AI chat thông thường có thể tóm tắt nội dung, nhưng không nắm được timeline, tag, task, category và lịch sử học tập có cấu trúc của từng người. Vì vậy phản hồi thường chung chung và khó chuyển thành hành động cụ thể.

#### Giải Pháp Đề Xuất

Nền tảng tập trung dữ liệu học tập vào một ứng dụng duy nhất. Mỗi journal entry có các trường như title, content, date, category, tags, commands, errors, solutions, mood, difficulty, thời gian học và ảnh minh họa.

Các tính năng AI được xây trên dữ liệu có cấu trúc này:

- Báo cáo học tập theo tuần hoặc tháng.
- Phân tích điểm mạnh, điểm yếu và khuyến nghị cải thiện.
- Sinh quiz để ôn tập.
- Tìm kiếm trong nhật ký cá nhân.
- Thống kê theo category, tag, mood, difficulty và thời gian học.

Các tác vụ AI chạy lâu được xử lý bất đồng bộ bằng SQS và Lambda AI Worker, giúp frontend phản hồi nhanh và chỉ cần polling trạng thái hoàn thành.

### 3. Kiến Trúc Giải Pháp

![AI Personal Learning Architecture](/images/2-Proposal/ai_personal_learning_architecture.png)

#### Lớp Edge Và Frontend

- **AWS Amplify Hosting** deploy React/Vite SPA trực tiếp từ GitHub.
- **Amazon CloudFront** phân phối static assets qua HTTPS.
- **AWS WAF** bảo vệ lớp public edge bằng managed rules và rate-based rules.

#### Lớp Xác Thực

- **Amazon Cognito User Pool** xử lý đăng ký, đăng nhập và Google federation.
- SPA nhận JWT token từ Cognito.
- **API Gateway JWT Authorizer** bảo vệ các API route chứa dữ liệu riêng của người dùng.

#### Lớp Ứng Dụng

- **Amazon API Gateway HTTP API** mở các route như `/health`, `/me`, `/logs`, `/ai/reports`, `/quiz`, `/search` và `/analytics/summary`.
- **Lambda API (`AI-Personal-Learning-Handle`)** xử lý request đồng bộ, CRUD journal, tạo presigned URL ảnh và gửi job vào SQS.
- **Lambda Search Handler** hỗ trợ tìm kiếm theo keyword, topic, tag và ngày.
- **Lambda Analytics Handler** tổng hợp dữ liệu journal thành các chỉ số dashboard.

#### Lớp Dữ Liệu Và File

- **DynamoDB** lưu journal logs, AI reports, quizzes và quiz attempts.
- **S3** lưu ảnh học tập do người dùng upload.
- Ảnh được upload bằng presigned URL để không đi qua Lambda hoặc API Gateway.

#### Lớp Xử Lý AI

- **SQS** lưu job tạo AI report và quiz.
- **DLQ** lưu message lỗi để kiểm tra.
- **Lambda AI Worker (`AI-Personal-Learning-Worker`)** đọc job từ SQS, lấy dữ liệu journal liên quan trong DynamoDB, gọi **Groq API**, sau đó lưu kết quả AI về DynamoDB.

#### Giám Sát Và Kiểm Soát Chi Phí

- **CloudWatch Logs, Metrics và Alarms** giám sát Lambda errors, duration, throttles và SQS backlog.
- **SNS** gửi cảnh báo qua email.
- **AWS Budgets** cảnh báo khi chi phí chạm ngưỡng.
- API Gateway throttling và Lambda reserved concurrency giúp hạn chế sử dụng quá mức.

### 4. Triển Khai Kỹ Thuật

#### Tính Năng Chính

- Đăng ký, đăng nhập, đăng xuất và Google sign-in qua Cognito.
- CRUD nhật ký học tập với dữ liệu có cấu trúc.
- Upload ảnh lên S3 bằng presigned URL.
- Tạo AI report thông qua SQS và Lambda Worker.
- Sinh quiz và chấm điểm quiz attempt.
- Search endpoint để tìm journal.
- Analytics endpoint để hiển thị dashboard tiến độ.
- Deploy frontend bằng Amplify với environment variables.
- WAF, throttling, CloudWatch alarms, SNS và Budgets.

#### Dịch Vụ AWS Chính

- **Amplify Hosting**: deploy frontend.
- **CloudFront + WAF**: phân phối public và bảo vệ edge.
- **Cognito**: xác thực và cấp JWT token.
- **API Gateway**: HTTP API entry point.
- **Lambda**: API handler, AI worker, search handler, analytics handler.
- **DynamoDB**: cơ sở dữ liệu NoSQL serverless.
- **S3**: lưu ảnh.
- **SQS + DLQ**: xử lý job AI bất đồng bộ.
- **CloudWatch + SNS + Budgets**: giám sát và kiểm soát chi phí.
- **Groq API**: AI completion cho report và quiz.

### 5. Timeline Và Milestones

#### Giai Đoạn 1 - Phân Tích Và Thiết Kế

- Xác định user flow cho journal, upload ảnh, AI report, quiz, search và analytics.
- Thiết kế bảng DynamoDB và API routes.
- Hoàn thiện kiến trúc AWS serverless và cost guardrails.

#### Giai Đoạn 2 - Frontend Và Authentication

- Xây dựng các màn hình SPA.
- Cấu hình Cognito User Pool, Hosted UI, app client, callback URLs và Google provider.
- Kết nối trạng thái đăng nhập frontend với API calls.

#### Giai Đoạn 3 - Backend API Và Storage

- Tạo API Gateway và Lambda API.
- Implement journal CRUD.
- Tạo các bảng DynamoDB.
- Tạo S3 image bucket và luồng upload bằng presigned URL.

#### Giai Đoạn 4 - AI Pipeline

- Tạo SQS queues và DLQs.
- Thêm route AI report và quiz.
- Tạo Lambda AI Worker và tích hợp Groq API.
- Lưu AI output vào DynamoDB và hỗ trợ frontend polling.

#### Giai Đoạn 5 - Search, Analytics Và Deployment

- Tạo Lambda handler cho search và analytics.
- Deploy frontend bằng Amplify.
- Cấu hình environment variables và Cognito production callback URLs.

#### Giai Đoạn 6 - Monitoring, Cost Và Bàn Giao

- Cấu hình CloudWatch alarms, SNS notifications, API throttling, Lambda timeouts và AWS Budgets.
- Chuẩn bị dữ liệu demo và tài liệu.
- Dọn dẹp hoặc bàn giao tài nguyên.

### 6. Ước Lượng Chi Phí

Với môi trường demo/thực tập nhỏ, chi phí dự kiến thấp vì hầu hết dịch vụ đều serverless và pay-per-use.

- Lambda, API Gateway, SQS, DynamoDB, S3, CloudWatch, SNS và Amplify có thể nằm trong vài USD mỗi tháng với traffic nhẹ.
- Chi phí Groq API phụ thuộc số lượng AI report và quiz được tạo.
- Ngân sách demo đề xuất là **USD 5-10/tháng**, kèm AWS Budgets alert ở mức 50%, 80% và 100%.

Các biện pháp kiểm soát chi phí:

- API Gateway throttling cho route AI.
- Reserved concurrency cho AI Worker.
- SQS DLQ để tránh retry loop vô hạn.
- S3 lifecycle rule cho ảnh upload.
- CloudWatch alarms cho error rate và queue backlog.

### 7. Rủi Ro Và Hướng Xử Lý

#### Chi Phí Vượt Dự Kiến

AI generation và request lặp lại có thể làm tăng chi phí. Cách xử lý: throttling, giới hạn concurrency, Budgets alert và frontend retry behavior rõ ràng.

#### Dữ Liệu Học Tập Nhạy Cảm

Journal có thể chứa ghi chú cá nhân hoặc screenshot. Cách xử lý: Cognito authentication, JWT authorizer, S3 bucket private, presigned URL và IAM least privilege.

#### Chất Lượng Output AI

AI report hoặc quiz có thể thiếu chính xác. Cách xử lý: prompt có cấu trúc, yêu cầu JSON-only output, validate trong Lambda Worker và cho phép người dùng phản hồi.

#### Độ Phức Tạp Vận Hành

Nhiều thành phần serverless có thể gây khó debug. Cách xử lý: CloudWatch logs, DLQ inspection, naming convention rõ ràng và tài liệu bàn giao.

### 8. Kết Quả Kỳ Vọng

- Một ứng dụng nhật ký học tập có AI hỗ trợ hoạt động end-to-end.
- Xác thực an toàn và cô lập dữ liệu theo từng user.
- Frontend phản hồi nhanh qua Amplify và CloudFront.
- Backend có khả năng mở rộng bằng API Gateway, Lambda, DynamoDB, S3 và SQS.
- AI report và quiz được xử lý bất đồng bộ thông qua Groq.
- Có monitoring và cost guardrails phù hợp môi trường demo/thực tập.
