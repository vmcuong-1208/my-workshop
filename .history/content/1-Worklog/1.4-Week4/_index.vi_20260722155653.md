---
title: "Worklog Tuần 4"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | - Hoàn thành Lab61: <br>&emsp; + Tìm hiểu nền tảng về Amazon ElastiCache và kiến trúc Redis (clusters, nodes và shards). <br>&emsp; + Nghiên cứu cách vận hành của Redis clusters ở các cấu hình bật/tắt chế độ cluster (cluster mode enabled/disabled). <br>&emsp; + Triển khai AWS Managed Microsoft AD trong Amazon VPC (Multi-AZ, private subnets). <br>&emsp; + Cấu hình tên miền (domain name), NetBIOS name và thông tin quản trị viên cho Directory Service. <br>&emsp; + Triển khai EC2 Bastion Host (public subnet) và EC2 AD Manager (private subnet). <br>&emsp; + Cấu hình IAM roles cho các máy chủ EC2 để tích hợp với AWS Directory Service. <br>&emsp; + Gia nhập (join) các máy chủ EC2 vào domain AWS Managed AD. | 11/05/2026 | 11/05/2026 |
| 2 | Tiếp tục với Lab61: <br>&emsp; + Cài đặt và sử dụng các công cụ Active Directory (AD Users and Computers, DNS, Group Policy Management). <br>&emsp; + Cấu hình DNS và xác minh kết nối giữa các máy chủ EC2 trong domain. <br>&emsp; + Chỉnh sửa tệp hosts và cài đặt mạng để đảm bảo phân giải tên miền chính xác. <br>&emsp; + Kiểm thử giao tiếp máy chủ bằng lệnh ping (địa chỉ IP và hostname). <br>&emsp; + Quản lý người dùng và xác thực chức năng Active Directory trên AWS. <br>&emsp; + Xác minh các máy chủ EC2 hoạt động chính xác trong môi trường AWS Managed AD. | 12/05/2026 | 12/05/2026 |
| 3 | - Hoàn thành Lab14: <br>&emsp; + Tạo và cấu hình máy ảo Ubuntu VM trên VMware. <br>&emsp; + Xuất (export) máy ảo và tải lên Amazon S3. <br>&emsp; + Cấu hình IAM role **vmimport** phục vụ quy trình VM Import/Export. <br>&emsp; + Nhập (import) máy ảo thành bản đóng gói AMI bằng AWS CLI. <br>&emsp; + Khởi chạy và xác minh máy chủ EC2 từ AMI đã import. <br>&emsp; + Cấu hình S3 bucket và ACL phục vụ xuất máy ảo. <br>&emsp; + Xuất các máy chủ EC2 và AMIs về Amazon S3. <br>&emsp; + Xác minh các tệp máy ảo đã xuất và giám sát các tác vụ import/export. | 13/05/2026 | 13/05/2026 |
| 4 | - Hoàn thành Lab95: <br>&emsp; + Nghiên cứu tổng quan về AWS Directory Service và mô hình AWS Managed Microsoft Active Directory. <br>&emsp; + Phân tích kiến trúc của AWS Managed AD trong mô hình trách nhiệm chung (Shared Responsibility Model). <br>&emsp; + Hiểu các tính năng cốt lõi của ElastiCache như tự động chuyển vùng sự cố (automatic failover), co giãn (scaling) và tính sẵn sàng cao trên các Availability Zones. <br>&emsp; + Tạo AWS IAM access keys và cấu hình AWS CLI để truy cập dịch vụ. <br>&emsp; + Cài đặt và cấu hình AWS CLI để tương tác với các dịch vụ AWS từ dòng lệnh. <br>&emsp; + Thực hành kết nối tới Redis clusters bằng AWS SDK (Boto3). <br>&emsp; + Thực hiện các thao tác Redis cơ bản như set/get chuỗi giá trị, truyền nhận tin nhắn Pub/Sub và các thao tác đọc/ghi stream. | 14/05/2026 | 14/05/2026 |
| 5 | - Hiểu CloudFront dưới vai trò CDN giúp cải thiện tốc độ và bảo mật trong phân phối nội dung trong Lab130. Chuẩn bị tài nguyên AWS (S3/EC2 và IAM) làm CloudFront origins. <br> - Tạo và cấu hình CloudFront distribution sử dụng S3 làm origin chính cho nội dung. <br>&emsp; + Thêm EC2 làm origin thứ hai và cấu hình cache behavior cho nội dung động (/api). <br>&emsp; + Xác minh CloudFront bằng cách truy cập URL, so sánh hiệu năng và kết quả lưu bản tạm (caching). <br> - Tối ưu hóa CloudFront với các cài đặt nâng cao như ghi log, bảo mật và giám sát hiệu năng. <br> - Cấu hình các trang lỗi tùy chỉnh trong CloudFront (403/504) sử dụng các tệp HTML lưu trên S3 và thiết lập phản hồi lỗi để nâng cao trải nghiệm người dùng cùng khả năng xử lý sự cố. <br> - Thiết lập nhiều S3 origins trong một Origin Group để bật cơ chế tự động chuyển vùng sự cố (automatic failover) khi origin chính không khả dụng. <br> - Cấu hình CloudFront response headers policy để tự động thêm các security headers, tăng cường bảo mật cho ứng dụng. <br> - Tạo cache behavior mới (/serverless) để định tuyến các yêu cầu tới EC2 origin và chuẩn bị tích hợp với Lambda@Edge cho việc xử lý nội dung động. | 15/05/2026 | 15/05/2026 |
| 6 | - Nghiên cứu tổng quan về Amazon CloudFront và kiến trúc CDN tích hợp với Amazon S3 trong Lab94. <br> - Tạo và cấu hình Amazon S3 bucket để lưu trữ nội dung web tĩnh (index.html). <br> - Cấu hình các thiết lập bảo mật S3 cơ bản (Block Public Access và bucket policy). <br> - Tải lên và kiểm thử nội dung HTML trong S3 bucket. <br> - Phân tích hiệu năng tải trang khi sử dụng trực tiếp URL đối tượng S3. <br> - Tạo CloudFront distribution với S3 làm origin. | 16/05/2026 | 16/05/2026 |
| 7 | Tiếp tục với Lab 94: <br> - Cấu hình Origin Access Identity (OAI) để bảo mật truy cập S3, chỉ cho phép truy cập thông qua CloudFront. <br> - Thiết lập đối tượng gốc mặc định (default root object) cho CloudFront distribution. <br> - Triển khai và xác minh trạng thái của CloudFront distribution. <br> - Truy cập trang web thông qua tên miền CloudFront. <br> - So sánh hiệu năng giữa truy cập S3 trực tiếp và truy cập qua CloudFront CDN. <br> - Kiểm tra vị trí CloudFront Edge Location (POP) được sử dụng khi truy cập từ Việt Nam. | 17/05/2026 | 17/05/2026 |

---

### Thành tựu đạt được trong Tuần 4:

* Đạt được kinh nghiệm thực tế với Amazon ElastiCache cho Redis thông qua việc thiết lập các cluster, cấu hình truy cập bằng AWS CLI và thực hiện các thao tác key-value, Pub/Sub cũng như stream bằng Python SDK.

* Triển khai thành công AWS Managed Microsoft Active Directory trên AWS, nắm rõ cách tích hợp domain với các máy chủ EC2 và thể hiện khả năng quản lý một môi trường Windows Server Active Directory hoàn chỉnh trên cloud với cơ chế quản trị an toàn, linh hoạt và tập trung.

* Triển khai thành công hệ thống phân phối nội dung tĩnh an toàn và tối ưu bằng Amazon S3 tích hợp với CloudFront, hiểu rõ kiến trúc CDN của AWS và cải thiện đáng kể hiệu năng phân phối nội dung thông qua mạng lưới Edge Locations toàn cầu.

* Trong Lab14:
  * Chuyển dịch thành công một máy ảo on-premises lên AWS dưới dạng bản đóng gói AMI.
  * Triển khai và truy cập thành công máy chủ EC2 từ AMI đã import thông qua SSH.
  * Xuất thành công các máy chủ EC2 và AMIs ngược lại về định dạng đĩa máy ảo (VMDK/OVA).
  * Tích lũy kinh nghiệm thực tế về toàn bộ quy trình AWS VM Import/Export bằng Amazon S3, IAM, EC2 và AWS CLI.