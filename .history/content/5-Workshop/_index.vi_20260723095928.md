---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Xây dựng AI Personal Learning Platform trên AWS

Trong workshop này, bạn sẽ xây dựng một ứng dụng nhật ký học tập serverless cho phép người dùng đăng nhập, tạo nhật ký học tập, tải lên hình ảnh và tạo các tóm tắt AI, báo cáo, quiz, kết quả tìm kiếm và phân tích dữ liệu.

Triển khai theo kiến trúc AWS thực tế gồm:

- **Amazon Cognito** để xác thực người dùng và hỗ trợ đăng nhập Hosted UI.
- **Amazon API Gateway + AWS Lambda** để triển khai các API được bảo vệ và logic nghiệp vụ.
- **Amazon DynamoDB** để lưu trữ dữ liệu nhật ký, báo cáo, quiz và lượt làm bài.
- **Amazon S3** để lưu ảnh bằng cơ chế presigned URL.
- **Amazon SQS** và Lambda worker để xử lý công việc AI bất đồng bộ.
- **Groq API** để tạo nội dung AI nhanh chóng.
- **CloudWatch, SNS, AWS Budgets, CloudFront và WAF** để theo dõi, cảnh báo và bảo mật.

## Luồng workshop

1. **Xác thực và nền tảng API** – cấu hình Cognito, tạo Lambda API chính và bảo vệ route bằng JWT authorizer.
2. **Lớp lưu trữ và dữ liệu** – tạo bảng DynamoDB, bucket S3 và các route cho nhật ký.
3. **Xử lý AI bất đồng bộ** – tạo hàng đợi SQS, Lambda worker và các route AI report/quiz.
4. **Tìm kiếm, triển khai và vận hành** – thêm handler search/analytics, deploy frontend với Amplify và cấu hình các biện pháp kiểm soát chi phí và bảo mật.

## Nội dung

1. [Tổng quan về workshop](5.1-Workshop-overview/)
2. [Chuẩn bị](5.2-Prerequiste/)
3. [Truy cập đến S3 từ VPC](5.3-S3-vpc/)
4. [Truy cập đến S3 từ on-premises](5.4-S3-onprem/)
5. [VPC Endpoint Policies (Bonus)](5.5-Policy/)
6. [Dọn dẹp](5.6-Cleanup/)
