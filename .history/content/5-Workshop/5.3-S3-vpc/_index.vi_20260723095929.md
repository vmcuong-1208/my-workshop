---
title: "Truy cập S3 từ VPC"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# Tạo đường truy cập riêng cho S3 từ trong VPC

Trong bài lab này, bạn sẽ thấy cách các workload riêng tư nằm trong Amazon VPC có thể truy cập Amazon S3 mà không cần đi qua internet công cộng. Mục tiêu là tạo một đường truyền bảo mật, nhanh và riêng tư cho việc đọc/ghi dữ liệu.

## Bạn sẽ học được gì

- Cách gateway endpoint cho phép các EC2 instance trong VPC truy cập S3 một cách riêng tư.
- Cách tạo endpoint, gắn nó vào route table phù hợp và kiểm tra kết nối.
- Cách kiểm thử truy cập S3 từ bên trong VPC bằng AWS CLI.

## Nội dung

- [Tạo gateway endpoint](3.1-create-gwe/)
- [Tạo bucket, kiểm tra truy cập và xác nhận kết quả](3.2-test-gwe/)
