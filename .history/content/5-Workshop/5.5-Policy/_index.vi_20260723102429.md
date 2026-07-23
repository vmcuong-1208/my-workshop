---
title: "Chính sách endpoint của VPC"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5.5 </b> "
---

# Bảo mật, giám sát và các giới hạn kiểm soát chi phí

## AWS Budgets

Tạo một ngân sách chi phí để bạn nhận được cảnh báo trước khi workshop vượt quá mức chi tiêu dự kiến.

1. Mở **AWS Budgets**.
2. Chọn **Create budget**.
3. Chọn **Cost budget**.
4. Đặt một ngân sách hàng tháng nhỏ, ví dụ 5 USD hoặc 10 USD.
5. Thêm cảnh báo email tại các mức 50%, 80% và 100%.
6. Tạo ngân sách.

## Giới hạn tốc độ API Gateway

Giới hạn tốc độ API để giảm lưu lượng truy cập vô tình hoặc mang tính lạm dụng.

```text
Rate limit: 5-10 request mỗi giây cho workshop
Burst limit: 10-20 request
```

Áp dụng giới hạn chặt hơn cho các route AI như `/ai/reports` và `/quiz` vì chúng có thể kích hoạt việc sử dụng Groq ở các bước xử lý phía sau.

## Giới hạn Lambda

Cấu hình từng hàm Lambda một cách có chủ đích.

- Main API Lambda: timeout ngắn, ví dụ 10-15 giây.
- AI Worker Lambda: timeout dài hơn, ví dụ 30-60 giây.
- Reserved concurrency cho AI Worker: giá trị nhỏ, chẳng hạn 2-5.

## SQS DLQ

Đảm bảo `ai-report-jobs` và `quiz-jobs` đã được cấu hình DLQ. Sử dụng DLQ để kiểm tra các payload bị lỗi và tránh làm mất các yêu cầu AI một cách âm thầm.

## CloudWatch và SNS

1. Kiểm tra CloudWatch Logs cho từng hàm Lambda.
2. Tạo metric filter hoặc alarm cho lỗi Lambda, throttling và thời gian thực thi.
3. Gửi thông báo cảnh báo đến một SNS topic.
4. Đăng ký email của bạn vào SNS topic và xác nhận đăng ký.

## Kiểm soát chi phí S3 và DynamoDB

- Giữ lifecycle rule của S3 cho ảnh được tải lên nếu workshop diễn ra trong nhiều ngày.
- Sử dụng capacity mặc định/on-demand của DynamoDB trong giai đoạn phát triển.
- Xóa dữ liệu test không còn dùng sau khi xác thực.
- Giữ S3 Block Public Access luôn được bật.

## Bảo vệ bằng WAF

Ở lớp edge của frontend, gắn các rule WAF để chặn những request xấu phổ biến và giới hạn tốc độ của lưu lượng lặp lại. Hãy bắt đầu với các AWS managed rule groups rồi tinh chỉnh dựa trên các request mẫu.
