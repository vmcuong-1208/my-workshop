---
title: "Chuẩn bị tài nguyên"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 5.4.1 </b> "
---

# Chuẩn bị các bảng dữ liệu AI và hàng đợi

## Các bảng DynamoDB cho AI

Nếu bạn chưa tạo các bảng này ở phần trước, hãy tạo ngay bây giờ:

```text
AiReports
Khóa phân vùng: userId
Khóa sắp xếp: reportId

Quizzes
Khóa phân vùng: userId
Khóa sắp xếp: quizId

QuizAttempts
Khóa phân vùng: userId
Khóa sắp xếp: attemptId
```

Các giá trị trạng thái được khuyến nghị:

```text
pending
processing
completed
failed
```

## Hàng đợi SQS

Mở **Amazon SQS** và tạo:

- `ai-report-jobs` cho các job tạo báo cáo.
- `quiz-jobs` cho các job tạo quiz.
- `ai-jobs-dlq` hoặc DLQ riêng cho các message thất bại.

Với mỗi hàng đợi chính:

1. Dùng **Standard queue**.
2. Cấu hình visibility timeout dài hơn thời gian xử lý dự kiến của worker.
3. Gắn DLQ với số lần nhận tối đa, ví dụ `3`.

## Quyền IAM

Lambda API chính cần quyền gửi message tới hai hàng đợi chính. Worker cần quyền để:

- Nhận và xóa message từ SQS.
- Đọc dữ liệu nhật ký từ DynamoDB.
- Ghi kết quả AI vào `AiReports`, `Quizzes`, và `QuizAttempts`.
- Ghi log vào CloudWatch.
- Đọc khóa Groq từ biến môi trường hoặc Secrets Manager.
