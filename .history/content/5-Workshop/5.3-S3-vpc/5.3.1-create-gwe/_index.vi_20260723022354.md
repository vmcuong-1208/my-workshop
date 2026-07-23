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
HTML gốc
```