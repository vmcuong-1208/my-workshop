---
title: "Giới thiệu"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

## Luồng kiến trúc

Workshop này xây dựng một ứng dụng nhật ký học tập tích hợp AI trên AWS. Người dùng truy cập frontend qua CloudFront, AWS WAF bảo vệ lớp biên, Amplify host ứng dụng web và Cognito xác thực người dùng trước khi frontend gọi các route API Gateway được bảo vệ.

![architecture](../../images/5-Workshop/5.1-Workshop-overview/ai_personal_learning_architecture.png)

## Luồng yêu cầu

1. Người dùng mở ứng dụng frontend.
2. AWS WAF lọc lưu lượng không mong muốn trước khi tới CloudFront.
3. CloudFront phân phối tài nguyên SPA từ Amplify.
4. Cognito xác thực người dùng và trả về JWT token.
5. SPA gọi API Gateway kèm access token.
6. API Gateway chuyển request tới Lambda API chính.
7. Lambda lưu trữ hoặc lấy dữ liệu từ DynamoDB.
8. Lambda tạo presigned S3 URL cho tải ảnh lên và tải xuống.
9. Các công việc AI dài hạn được gửi tới SQS để xử lý bất đồng bộ.
10. Job lỗi được chuyển tới DLQ để kiểm tra.
11. SQS kích hoạt Lambda AI Worker.
12. Worker gọi Groq để hoàn thành yêu cầu AI.
13. Worker lưu báo cáo, quiz và tóm tắt vào DynamoDB.
14. CloudWatch, SNS và AWS Budgets cung cấp log, cảnh báo và biện pháp kiểm soát chi phí.

## Các thành phần chính

- **Amazon Cognito** xử lý đăng ký, đăng nhập, federation với Google và xác thực bằng JWT.
- **API Gateway + Lambda API** mở các route cho health check, thông tin người dùng, CRUD nhật ký, upload ảnh, báo cáo AI, quiz, tìm kiếm và analytics.
- **DynamoDB** lưu nhật ký học tập, báo cáo AI, quiz, lượt làm bài và dữ liệu cho analytics.
- **S3** lưu ảnh người dùng, truy cập chỉ thông qua presigned URL.
- **SQS + Lambda Worker** tách việc tạo AI khỏi độ trễ của API trực tiếp.
- **Groq API** cung cấp mô hình Llama tốc độ cao cho báo cáo và quiz.
