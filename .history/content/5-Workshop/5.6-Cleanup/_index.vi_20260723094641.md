---
title : "Dọn dẹp tài nguyên"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

# Dọn dẹp tài nguyên của workshop

Chúc mừng bạn đã hoàn thành workshop. Bạn đã khám phá cách dùng mạng riêng tư để kết nối các workload trên AWS và hệ thống on-premises với Amazon S3 mà không cần dựa vào internet công cộng.

## Những thứ nên xóa bỏ

1. Xóa private hosted zone và các Route 53 Resolver rule đã tạo cho bài lab.
2. Xóa các CloudFormation stack dùng để tạo môi trường mạng mẫu.
3. Làm trống và xóa các bucket S3 đã dùng trong buổi thực hành.
4. Xác nhận các VPC endpoint và security group liên quan không còn cần thiết.

Bước cuối này giúp giữ tài khoản AWS sạch sẽ và tránh phát sinh chi phí không cần thiết sau workshop.