---
title : "Giới thiệu"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Luồng kiến trúc

Workshop này tuân theo kiến trúc dưới đây. Người dùng truy cập SPA thông qua CloudFront. AWS WAF bảo vệ tầng public edge, Amplify lưu trữ ứng dụng frontend, và Cognito xác thực người dùng trước khi frontend gọi tới các tuyến API Gateway được bảo vệ.

![architecture](/images/5-Workshop/5.1-Workshop-overview/architecture.png)

#### Đường đi của yêu cầu (Request path)

1. Người dùng mở ứng dụng frontend.
2. AWS WAF lọc lưu lượng truy cập không mong muốn trước khi đến CloudFront.
3. CloudFront phân phối tài nguyên SPA từ Amplify.
4. Cognito xác thực người dùng và trả về các mã báo xác thực JWT (JWT tokens).
5. Ứng dụng SPA gọi API Gateway kèm theo access token.
6. API Gateway chuyển tiếp yêu cầu đến Lambda API chính.
7. Lambda thực hiện các thao tác CRUD trên DynamoDB.
8. Lambda tạo các đường dẫn S3 presigned URL để tải lên và tải xuống hình ảnh.
9. Đối với các tính năng AI xử lý lâu, Lambda gửi các công việc (jobs) vào SQS.
10. Các công việc bị lỗi sẽ được chuyển hướng sang DLQ để khắc phục sự cố.
11. SQS kích hoạt Lambda AI Worker.
12. Worker gọi Groq API để hoàn thành phản hồi prompt (prompt completion).
13. Worker lưu trữ các báo cáo AI, dữ liệu bài trắc nghiệm (quiz) và bản tóm tắt vào DynamoDB.
14. CloudWatch, SNS và AWS Budgets cung cấp nhật ký (logs), cảnh báo (alerts) và các rào chắn kiểm soát chi phí (cost guardrails).

#### Các thành phần chính

* **Amazon Cognito**: Quản lý đăng ký, đăng nhập, liên kết tài khoản Google (Google federation) và phân quyền dựa trên JWT.
* **API Gateway + Lambda API**: Cung cấp các tuyến API cho `/health`, `/me`, `/logs`, tải ảnh lên, báo cáo AI, bài trắc nghiệm, tìm kiếm và phân tích dữ liệu.
* **DynamoDB**: Lưu trữ nhật ký học tập (journal logs), báo cáo AI, bài trắc nghiệm, các lượt làm bài trắc nghiệm và dữ liệu tối ưu cho việc phân tích.
* **S3**: Lưu trữ hình ảnh học tập được tải lên, với quyền truy cập được kiểm soát thông qua các đường dẫn presigned URLs.
* **SQS + Lambda Worker**: Tách biệt quá trình tạo nội dung AI khỏi độ trễ của API tiếp xúc trực tiếp với người dùng.
* **Groq API**: Cung cấp phản hồi nhanh từ mô hình Llama cho các bản tóm tắt, báo cáo và bài trắc nghiệm.
