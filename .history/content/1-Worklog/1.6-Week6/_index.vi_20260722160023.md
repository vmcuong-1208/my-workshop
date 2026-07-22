---
title: "Worklog Tuần 6"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | - Chuẩn bị môi trường lab bằng CloudFormation trong Lab20: <br>&emsp; + Tạo bốn VPC cùng các subnets và máy chủ EC2. <br>&emsp; + Cấu hình security groups cho SSH và ICMP. <br> - Khởi tạo SSH key pair để truy cập các máy chủ EC2. <br> - Tạo AWS Transit Gateway với các thiết lập tùy chỉnh. <br> - Thiết lập Transit Gateway Attachments kết nối tới cả bốn VPC. <br> - Cấu hình Transit Gateway Route Table: <br>&emsp; + Tạo các liên kết (associations) và lan truyền tuyến đường (propagations) cho từng VPC. <br> - Cập nhật route tables của VPC để định tuyến lưu lượng thông qua Transit Gateway. <br> - Kiểm thử kết nối: <br>&emsp; + Xác minh truy cập internet từ các máy chủ EC2. <br>&emsp; + Kiểm tra giao tiếp liên VPC qua Transit Gateway. | 25/05/2026 | 25/05/2026 |
| 2 | - Tạo VPC, subnets và security group cho lab Lambda trong Lab22. <br> - Khởi chạy máy chủ EC2 với các thiết lập mạng và bảo mật phù hợp. <br> - Cấu hình Slack Incoming Webhooks để nhận thông báo. <br> - Gắn thẻ (tag) cho máy chủ EC2 **(environment_auto=true)** để định danh tự động hóa. <br> - Tạo IAM Role **(dc-common-lambda-role)** cấp quyền cho EC2 và CloudWatch. <br> - Phát triển hai hàm Lambda (Lambda functions): <br>&emsp; + **dc-common-lambda-auto-sstop** → dừng các máy chủ EC2. <br>&emsp; + **dc-common-lambda-auto-start** → khởi động các máy chủ EC2. <br> - Cấu hình các biến môi trường và tích hợp gửi thông báo qua Slack. <br> - Lập lịch chạy các hàm Lambda bằng CloudWatch rules (dừng mỗi 9 giờ, khởi động mỗi 8 giờ). | 26/05/2026 | 26/05/2026 |
| 3 | - Hoàn thành Lab23: <br> - Chuẩn bị hạ tầng (VPC, Security Group, RDS, EC2). <br> - Tạo S3 bucket lưu trữ các bản đóng gói (build artifacts) và cấu hình bucket policy. <br> - Khởi tạo Git credentials và thiết lập kết nối tới GitHub. <br> - Tạo IAM service role cho CodeDeploy và cấp phát IAM user kèm policies. <br> - Cấu hình IAM instance profile và gán role cho EC2. <br> - Cài đặt CodeDeploy Agent trên các máy chủ EC2. <br> - Thiết lập kho lưu trữ AWS CodeCommit (có tùy chọn chuyển đổi sang GitHub/GitLab/Bitbucket). <br> - Cấu hình dự án AWS CodeBuild: nguồn (GitHub), môi trường, buildspec, artifacts (S3), logs (CloudWatch). <br> - Tạo ứng dụng AWS CodeDeploy và deployment group cho EC2. <br> - Triển khai các bản đóng gói ứng dụng từ S3 lên EC2 thông qua CodeDeploy. <br> - Xây dựng quy trình CI/CD hoàn chỉnh (end-to-end) với AWS CodePipeline: <br>&emsp; + Nguồn (Source) → CodeCommit <br>&emsp; + Đóng gói (Build) → CodeBuild <br>&emsp; + Triển khai (Deploy) → CodeDeploy | 27/05/2026 | 27/05/2026 |
| 4 | - Hoàn thành Lab24: <br> - Tạo S3 bucket (**s3-instancestoragegw-2023**) để lưu trữ tệp. <br> - Khởi chạy máy chủ EC2 bằng AWS Storage Gateway AMI. <br> - Cấu hình security group (**storagegw-instance-sg**) và gắn dung lượng cache (≥150 GiB). <br> - Thiết lập dịch vụ AWS Storage Gateway: <br>&emsp; + Đặt tên gateway (**filesgw**). <br>&emsp; + Cấu hình bộ nhớ đệm (cache storage). <br>&emsp; + Điều chỉnh cài đặt truy cập khách (guest access) SMB. <br> - Tạo File Share: <br>&emsp; + Loại: SMB (liên kết tới S3 bucket). <br>&emsp; + Bật xác thực khách (guest authentication). <br> - Mount File Share lên máy Windows on-premises bằng lệnh net use. <br> - Xác minh đồng bộ: tạo các tệp trên ổ đĩa đã mount và xác nhận dữ liệu đã được sao chép lên S3 bucket. | 28/05/2026 | 28/05/2026 |
| 5 | - Hoàn thành Lab25: <br> - Nghiên cứu kiến trúc Amazon FSx, chuẩn bị VPC, security groups và Active Directory. <br> - Tạo các hệ thống tệp FSx Multi-AZ dạng SSD và HDD với các cấu hình bắt buộc. <br> - Kết nối tới Windows EC2, ánh xạ ổ đĩa chia sẻ và tạo các thư mục chia sẻ SMB. <br> - Kiểm thử hiệu năng đọc/ghi bằng công cụ DiskSpd và fio. <br> - Giám sát hiệu năng FSx bằng dashboards và alarms trên CloudWatch. <br> - Bật tính năng chống trùng lặp dữ liệu (data deduplication) và thiết lập lịch tối ưu hóa. | 29/05/2026 | 29/05/2026 |
| 6 | - Tiếp tục với Lab25: <br> - Bật tính năng shadow copies và tạo các điểm khôi phục (restore points). <br> - Quản lý các phiên người dùng (user sessions) và tệp đang mở bằng giao diện GUI và PowerShell. <br> - Bật và kiểm thử hạn ngạch lưu trữ người dùng (user storage quotas). <br> - Tạo một thư mục chia sẻ SMB độ sẵn sàng cao (Continuous Availability) cho SQL Server. <br> - Co giãn băng thông (throughput capacity) của FSx và giám sát quá trình chuyển vùng sự cố (failover). <br> - Tăng 10% dung lượng lưu trữ của FSx và giám sát tiến trình tối ưu hóa. | 30/05/2026 | 30/05/2026 |
| 7 | - Hoàn thành Lab26: <br> - Tạo S3 bucket (**aws-waf-logs-001**) để lưu trữ log của WAF. <br> - Triển khai ứng dụng web mẫu có lỗ hổng (OWASP Juice Shop) thông qua CloudFormation. <br> - Cấu hình AWS WAF: <br>&emsp; + Tạo Web ACL (**waf-workshop-juice-shop**). <br>&emsp; + Liên kết Web ACL với CloudFront distribution. <br>&emsp; + Thêm các nhóm quy tắc do AWS quản lý (Core Rule Set, SQL Database). <br> - Kiểm thử các quy tắc WAF bằng các cuộc tấn công giả lập: <br>&emsp; + Tạo Kinesis Data Firehose delivery stream (**aws-waf-logs-workshop-26**). <br>&emsp; + Cấu hình đích đến của log là S3 bucket. <br>&emsp; + Áp dụng cơ chế ẩn danh/che thông tin (redaction) cho các request headers nhạy cảm (Cookie). <br> - Xác minh log bằng cách thực hiện các yêu cầu kiểm thử và kiểm tra các tệp log được lưu trữ trong S3. | 31/05/2026 | 31/05/2026 |

---

### Thành tựu đạt được trong Tuần 6:

* Lab20: 
  * Triển khai thành công AWS Transit Gateway để kết nối bốn VPC.
  * Đơn giản hóa kiến trúc mạng đáng kể so với việc thiết lập nhiều kết nối VPC Peering thủ công.
  * Cho phép quản lý và định tuyến tập trung giữa các VPC.
  * Đạt được khả năng giao tiếp an toàn, có thể mở rộng và độ trễ thấp giữa các VPC.
  * Xác minh thành công cả kết nối internet lẫn kết nối nội bộ giữa các VPC.
  * Thể hiện kỹ năng thực hành thực tế với Transit Gateway trong môi trường đa VPC.

* Lab22: 
  * Tự động hóa quá trình bật/tắt máy chủ EC2 bằng AWS Lambda và CloudWatch.
  * Tối ưu hóa chi phí vận hành bằng cách chỉ khởi chạy máy chủ khi có nhu cầu sử dụng.
  * Tích hợp gửi thông báo qua Slack để theo dõi thời gian thực các trạng thái tự động hóa.
  * Áp dụng chiến lược gắn thẻ (tagging) để phân loại tài nguyên tự động hóa chính xác.
  * Đảm bảo truy cập an toàn dựa trên quyền IAM policies.
  * Xác minh tự động hóa hoạt động chính xác qua sự thay đổi trạng thái của EC2 và cảnh báo trên Slack.

* Lab24: 
  * Triển khai thành công AWS Storage Gateway trên EC2.
  * Thiết lập thư mục chia sẻ SMB File Share kết nối trực tiếp với S3 bucket.
  * Mount thành công SMB File Share lên máy local/on-premises để truy cập dữ liệu liền mạch.
  * Bật cơ chế đồng bộ hai chiều giữa các tệp nội bộ và kho lưu trữ S3.
  * Thể hiện khả năng tích hợp mô hình lưu trữ đám mây lai (hybrid cloud) với AWS.
  * Đánh giá và xác minh giải pháp chia sẻ tệp an toàn, có khả năng mở rộng nối liền hạ tầng local và cloud.

* Lab25: 
  * Chuẩn bị thành công môi trường AWS sẵn sàng cho việc triển khai FSx.
  * Triển khai thành công cả hai hệ thống tệp FSx (SSD & HDD) với tính sẵn sàng cao (Multi-AZ).
  * Tạo và quản lý các thư mục chia sẻ bằng cả giao diện GUI và các lệnh PowerShell.
  * Thu thập và phân tích các chỉ số đo lường hiệu năng về throughput, IOPS và độ trễ (latency).
  * Cấu hình hệ thống giám sát theo thời gian thực và gửi thông báo qua email.
  * Tối ưu hóa dung lượng lưu trữ và xác minh trạng thái chống trùng lặp dữ liệu (deduplication).
  * Khôi phục thành công các phiên bản tệp cũ nhờ tính năng shadow copies.
  * Giám sát và ngắt thành công các phiên làm việc SMB đang hoạt động.
  * Xác minh và áp dụng thành công các tính năng theo dõi, giới hạn hạn ngạch (quota) lưu trữ.
  * Cấu hình thư mục chia sẻ SMB mã hóa, độ sẵn sàng cao dành cho SQL Server.
  * Nâng dung lượng băng thông (throughput) thành công với gián đoạn dịch vụ tối thiểu.
  * Mở rộng dung lượng lưu trữ thành công và theo dõi tiến trình tối ưu hóa.

* Lab26: 
  * Triển khai thành công AWS WAF để bảo vệ ứng dụng web mẫu.
  * Áp dụng các nhóm quy tắc managed rules để ngăn chặn các đợt tấn công phổ biến theo tiêu chuẩn OWASP Top 10.
  * Kiểm chứng hiệu quả của WAF thông qua các kịch bản tấn công khai thác giả lập.
  * Bật hệ thống tập trung log truy cập WAF qua luồng Kinesis Firehose → S3.
  * Áp dụng quy tắc ẩn danh dữ liệu (header redaction) để bảo vệ các thông tin nhạy cảm trong log.
  * Thể hiện chiến lược phòng thủ chiều sâu (defense-in-depth) trong bảo mật ứng dụng web với AWS WAF.