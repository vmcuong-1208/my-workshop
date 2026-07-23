---
title : "Tạo DynamoDB, S3 và thử nghiệm API"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.3.2 </b> "
---

#### Tạo các bảng DynamoDB

Trước tiên, tạo bảng journal cơ bản:

```text
Tên bảng: JournalLogs
Partition key: userId
Sort key: entryId
Cài đặt bảng: Mặc định
```

Sau đó tạo các bảng liên quan đến AI sẽ được dùng ở phần tiếp theo:

```text
Tên bảng: AiReports
Partition key: userId
Sort key: reportId

Tên bảng: Quizzes
Partition key: userId
Sort key: quizId

Tên bảng: QuizAttempts
Partition key: userId
Sort key: attemptId
```

#### Cấp quyền truy cập dữ liệu cho Lambda

Mở execution role của `AI-Personal-Learning-Handle` và gắn các quyền sau:

- Quyền đọc và ghi DynamoDB cho bốn bảng trên.
- Quyền đọc và ghi S3 cho bucket lưu ảnh.
- Quyền gửi message (send-message) tới các SQS queue của AI.
- Quyền CloudWatch Logs để phục vụ debug.

Đối với một workshop ngắn, có thể dùng managed policies để đẩy nhanh tiến độ xây dựng. Với môi trường production, nên thay bằng các policy giới hạn phạm vi theo resource (resource-scoped policies).

#### Tạo S3 bucket lưu ảnh

1. Mở **Amazon S3** và chọn **Create bucket**.
2. Tên bucket: `learnflow-journal-images-<hậu-tố-duy-nhất>`.
3. Region: cùng Region với Lambda API.
4. Giữ **Block Public Access** ở trạng thái bật.
5. Tạo bucket.

Cấu hình CORS cho bucket để frontend có thể upload thông qua presigned URL:

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "POST"],
    "AllowedOrigins": ["http://localhost:5173"],
    "ExposeHeaders": ["ETag"],
    "MaxAgeSeconds": 3000
  }
]
```

#### Thêm route cho journal và upload ảnh

Trong API Gateway, tạo và gắn Lambda integration cho các route sau:

```text
GET /logs
POST /logs
GET /logs/{id}
PUT /logs/{id}
DELETE /logs/{id}
POST /logs/{id}/images/presigned-url
```

Gắn `CognitoAuth` cho tất cả các route trên.

#### Kiểm thử toàn trình (end-to-end)

1. Gọi `GET /health` từ trình duyệt. Phản hồi thành công sẽ trả về JSON tương tự `{"ok":true}`.
2. Đăng nhập qua Cognito Hosted UI.
3. Gọi `GET /me` kèm JWT token và kiểm tra API trả về đúng thông tin người dùng.
4. Tạo một bản ghi journal thông qua `POST /logs`.
5. Yêu cầu một presigned URL, upload ảnh lên S3, và lưu image key vào bản ghi journal.
6. Tải lại frontend và kiểm tra dữ liệu journal cùng ảnh chỉ hiển thị đúng cho người dùng đã đăng nhập.