---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


# Xây dựng AI Personal Learning trên AWS

#### Tổng quan

Trong buổi thực hành này, bạn sẽ xây dựng một ứng dụng nhật ký học tập serverless cho phép người dùng đăng nhập, tạo nhật ký học tập, tải lên hình ảnh và tạo các tóm tắt AI, báo cáo, bài kiểm tra (quiz), kết quả tìm kiếm cùng phân tích dữ liệu.

Kiến trúc ứng dụng sử dụng **AWS Amplify**, **Amazon CloudFront**, **AWS WAF**, **Amazon Cognito**, **Amazon API Gateway**, **AWS Lambda**, **Amazon DynamoDB**, **Amazon S3**, **Amazon SQS**, **Amazon CloudWatch**, **Amazon SNS**, **AWS Budgets** và **Groq API**.

Bạn sẽ triển khai buổi thực hành theo từng lớp (layers):

* **Giao diện người dùng và Xác thực** - Lưu trữ SPA với Amplify, bảo vệ lớp biên với CloudFront và WAF, đồng thời xác thực người dùng bằng Cognito.
* **API và Dữ liệu** - Mở các tuyến HTTP thông qua API Gateway, xử lý yêu cầu trong Lambda, lưu trữ dữ liệu nhật ký trong DynamoDB và tải hình ảnh lên S3 thông qua presigned URLs.
* **Khối lượng công việc AI** - Gửi các tác vụ AI mất nhiều thời gian (báo cáo và bài kiểm tra) tới SQS, xử lý bất đồng bộ trong Lambda worker và gọi Groq để hoàn thành prompt.
* **Vận hành** - Thêm các biện pháp kiểm soát chi phí, nhật ký (logs), giới hạn lưu lượng (throttling), xử lý DLQ và các bước dọn dẹp tài nguyên.

#### Nội dung

1. [Tổng quan về workshop](5.1-Workshop-overview/)
2. [Chuẩn bị](5.2-Prerequiste/)
3. [Truy cập đến S3 từ VPC](5.3-S3-vpc/)
4. [Truy cập đến S3 từ TTDL On-premises](5.4-S3-onprem/)
5. [VPC Endpoint Policies (làm thêm)](5.5-Policy/)
6. [Dọn dẹp tài nguyên](5.6-Cleanup/)