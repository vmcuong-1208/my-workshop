---
title : "Truy cập S3 từ VPC"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Nền tảng backend

Trong phần này, bạn sẽ xây dựng lớp API phục vụ người dùng cho ứng dụng nhật ký học tập. Frontend xác thực thông qua Cognito, sau đó gọi các route của API Gateway. API Gateway sẽ gọi đến hàm Lambda chính, và Lambda thực hiện lưu trữ hoặc truy xuất dữ liệu từ DynamoDB và S3.

Các nhiệm vụ chính:

- Xác thực người dùng bằng Cognito và bảo vệ các route bằng một JWT authorizer.
- Tạo một Lambda API handler xử lý health check, thông tin hồ sơ người dùng, CRUD cho journal, presigned URL cho ảnh, gửi job AI, các route quiz, tìm kiếm và phân tích (analytics).
- Tạo các bảng DynamoDB để lưu journal logs và kết quả AI.
- Tạo một S3 bucket để lưu ảnh học tập do người dùng tải lên.

#### Nội dung

- [Tạo gateway endpoint](3.1-create-gwe/)
- [Test gateway endpoint](3.2-test-gwe/)