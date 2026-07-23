---
title : "Truy cập S3 từ môi trường truyền thống"
date : 2024-01-01 
weight : 4 
chapter : false
pre : " <b> 5.4. </b> "
---

#### Tổng quan

# Xử lý AI bất đồng bộ

## Tại sao cần xử lý bất đồng bộ

Việc tạo báo cáo AI và quiz có thể mất vài giây. Nếu frontend chờ toàn bộ phản hồi AI trong một lần gọi API đồng bộ, người dùng có thể gặp lỗi timeout hoặc màn hình phản hồi chậm. Phần này chuyển các tác vụ chạy dài sang SQS và một Lambda worker.

API Lambda chính chỉ tạo một job ở trạng thái chờ và trả về ngay lập tức. Worker sẽ tiêu thụ message từ SQS, gọi Groq, và cập nhật DynamoDB khi kết quả đã sẵn sàng. Sau đó, frontend sẽ liên tục truy vấn `GET /ai/reports/{id}` hoặc `GET /quiz/{id}` cho đến khi trạng thái trở thành `completed`.

## Nội dung

- [Chuẩn bị bảng dữ liệu AI và hàng đợi](5-workshop/5.4-s3-onprem/5.4.1-prepare/)
- [Tạo Lambda AI Worker](5-workshop/5.4-s3-onprem/5.4.2-create-interface-enpoint/)
- [Kết nối các route API với các job bất đồng bộ](5-workshop/5.4-s3-onprem/5.4.3-test-endpoint/)
- [Thêm tìm kiếm, phân tích và triển khai frontend](5-workshop/5.4-s3-onprem/5.4.4-dns-simulation/)



