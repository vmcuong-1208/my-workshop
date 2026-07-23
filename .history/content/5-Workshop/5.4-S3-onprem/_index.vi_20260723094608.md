---
title : "Truy cập S3 từ môi trường on-premises"
date : 2024-01-01 
weight : 4 
chapter : false
pre : " <b> 5.4. </b> "
---

# Mở rộng truy cập S3 riêng tư sang môi trường on-premises

Bài lab này cho thấy cách một môi trường on-premises có thể truy cập Amazon S3 thông qua kết nối riêng tư của AWS. Thay vì đi qua internet công cộng, bạn sẽ dùng interface endpoint và routing DNS để giữ cho kết nối vẫn an toàn và riêng tư.

## Bạn sẽ học được gì

- Cách interface endpoint cung cấp kết nối riêng tư cho S3 từ mạng on-premises.
- Cách Route 53 Resolver và private hosted zone giúp giải tên endpoint S3 đúng cách.
- Cách kiểm tra kết nối từ một host mô phỏng on-premises.

## Nội dung

- [Chuẩn bị môi trường và cấu hình kết nối](5.4.1-prepare/)
- [Tạo interface endpoint](5.4.2-create-interface-enpoint/)
- [Kiểm tra endpoint từ phía on-premises](5.4.3-test-endpoint/)
- [Xác thực hành vi DNS và định tuyến](5.4.4-dns-simulation/)



