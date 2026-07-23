---
title: "Truy cập S3 từ VPC"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

## Nền tảng backend

Trong phần này, bạn sẽ tạo lớp API dành cho người dùng của ứng dụng nhật ký học tập. Frontend xác thực bằng Cognito, sau đó gọi các route của API Gateway. API Gateway kích hoạt hàm Lambda chính, và Lambda lưu hoặc truy xuất dữ liệu từ DynamoDB và S3.

Trách nhiệm chính:

- Xác thực người dùng bằng Cognito và bảo vệ các route bằng JWT authorizer.
- Tạo Lambda API handler cho các chức năng kiểm tra trạng thái, thông tin hồ sơ, CRUD nhật ký, URL presigned cho hình ảnh, gửi job AI, các route quiz, tìm kiếm và phân tích.
- Tạo các bảng DynamoDB cho nhật ký học tập và kết quả AI.
- Tạo một bucket S3 để lưu hình ảnh học tập do người dùng tải lên.

## Nội dung

- [Cấu hình Cognito và API Gateway](/5-workshop/5.3-s3-vpc/5.3.1-create-gwe/)
- [Tạo DynamoDB, S3 và kiểm thử API](/5-workshop/5.3-s3-vpc/5.3.2-test-gwe/)

## Nội dung

- [Tạo gateway endpoint](3.1-create-gwe/)
- [Tạo bucket, kiểm tra truy cập và xác nhận kết quả](3.2-test-gwe/)
