---
title: "Worklog Tuần 8"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---
### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | - Hoàn thành Lab33: <br> - Thiết lập IAM: <br>&emsp; + Tạo IAM policy tùy chỉnh cấp quyền cho S3, CloudTrail, CloudWatch, Config, IAM và KMS chỉ giới hạn tại region us-east-1. <br>&emsp; + Tạo IAM role (kms-key-role) và gán policy tùy chỉnh vừa tạo. <br>&emsp; + Tạo IAM group (GroupLimit) gán policy AmazonS3FullAccess và user (User-S3) để kiểm thử quyền truy cập. <br> - Khởi tạo KMS Key: <br>&emsp; + Tạo một khóa đối xứng CMK (kms-key-encrypt-decrypt) phục vụ mã hóa/giải mã. <br>&emsp; + Cấu hình quản trị viên quản lý khóa và phân quyền sử dụng khóa thông qua IAM role. <br>&emsp; + Bật tùy chọn tự động xoay vòng khóa (key rotation). <br> - Thiết lập S3 Bucket: <br>&emsp; + Tạo S3 bucket (kms-key-s3) cấu hình mã hóa phía máy chủ (SSE-KMS) sử dụng CMK đã tạo. <br>&emsp; + Tải dữ liệu lên bucket với các thiết lập bắt buộc mã hóa. <br> - CloudTrail & Athena: <br>&emsp; + Tạo CloudTrail trail (kms-key-cloudtrail) để ghi lại các sự kiện S3 vào cùng bucket. <br>&emsp; + Xác minh các bản ghi log được lưu trữ tại thư mục cloudtrail/ trên S3. <br>&emsp; + Tạo bảng Athena để truy vấn các bản ghi log từ CloudTrail. <br>&emsp; + Chạy các truy vấn SQL trong Athena để lấy danh sách event names và kiểm tra nhật ký. <br> - Kiểm thử & Chia sẻ: <br>&emsp; + Kiểm thử quyền truy cập các đối tượng đã mã hóa với các IAM users khác nhau (chủ sở hữu vs. User-S3). <br>&emsp; + Xác minh truy cập bị từ chối khi thiếu quyền giải mã. <br>&emsp; + Tạo và kiểm thử pre-signed URLs để chia sẻ tạm thời các đối tượng S3 mã hóa một cách an toàn. | 08/06/2026 | 08/06/2026 |
| 2 | - Hoàn thành Lab34: <br> - Xem chi phí và mức độ sử dụng theo dịch vụ: <br>&emsp; + Truy cập AWS Billing Dashboard → Cost Explorer. <br>&emsp; + Xuất các báo cáo chi phí hàng tháng theo dịch vụ, tùy chỉnh các bộ lọc và dạng biểu đồ. <br> - Xem chi phí và mức độ sử dụng theo tài khoản: <br>&emsp; + Kiểm tra báo cáo các tài khoản liên kết (linked accounts) với phân tích chi tiết theo tháng. <br>&emsp; + Áp dụng các bộ lọc và nhóm chi phí theo loại instance hoặc mức độ sử dụng. <br> - Phân tích Savings Plans & Reserved Instances: <br>&emsp; + Xem báo cáo mức độ bao phủ (coverage) và tỷ lệ sử dụng (utilization) của Savings Plans và RIs. <br>&emsp; + Phát hiện các điểm bất thường và khoảng trống bảo phủ chi phí.<br> - Phân tích tính co giãn (Elasticity Analysis): <br>&emsp; + Điều chỉnh khoảng thời gian trong Cost Explorer (ví dụ: 3 tháng). <br>&emsp; + Tùy chỉnh bộ lọc và hiển thị biểu đồ để phân tích xu hướng co giãn tài nguyên. <br> - Tạo báo cáo EC2 tùy chỉnh: <br>&emsp; + Xây dựng và lưu các báo cáo chi phí EC2 tùy chỉnh. <br>&emsp; + Quản lý vòng đời báo cáo (tạo, lưu, xóa). <br> - Phân tích chi phí chi tiết: <br>&emsp; + Sử dụng Cost Explorer để đào sâu dữ liệu xuống cấp độ dịch vụ/tài nguyên (EC2 Instance ID). <br>&emsp; + Bật các thẻ phân bổ chi phí (cost allocation tags) để phân tích chi phí theo môi trường (Prod, UAT). <br>&emsp; + Theo dõi chi phí truyền dữ liệu ra ngoài (“Data Transfer Out”) theo dịch vụ và loại hình sử dụng. <br> - Tổng quan chi phí truyền dữ liệu (Data Transfer): <br>&emsp; + Xem xét các kịch bản phát sinh chi phí truyền dữ liệu: <br>&emsp;&emsp; * Truyền dữ liệu AWS ↔ Internet. <br>&emsp;&emsp; * Giao tiếp giữa các Regions và giữa các AZs. <br>&emsp;&emsp; * Kết nối qua VPC Peering và Transit Gateway. <br>&emsp;&emsp; * Kết nối Site-to-Site VPN và Direct Connect. <br>&emsp; * Áp dụng các thực tiễn kiến trúc tốt nhất để tối thiểu hóa chi phí truyền dữ liệu. | 09/06/2026 | 09/06/2026 |
| 3 | - Hoàn thành Lab35: <br> - Tìm hiểu các khái niệm và kiến trúc AWS Data Lake. <br> - Tạo các IAM roles và policies cho AWS Glue. <br> - Tạo S3 bucket làm kho lưu trữ dữ liệu. <br> - Cấu hình Kinesis Firehose phục vụ tiếp nhận dữ liệu (data ingestion). <br> - Tạo và chạy AWS Glue Crawler. <br> - Truy vấn dữ liệu sử dụng Amazon Athena. <br> - Thực hiện biến đổi dữ liệu (data transformation) bằng Glue Notebook. <br> - Trực quan hóa dữ liệu bằng Amazon QuickSight. | 10/06/2026 | 09/06/2026 |
| 4 | - Hoàn thành Lab36: <br> - Nghiên cứu các tính năng và khái niệm giám sát của Amazon CloudWatch. <br> - Triển khai tài nguyên AWS sử dụng CloudFormation. <br> - Khám phá các chỉ số (metrics) và biểu đồ trên CloudWatch. <br> - Sử dụng tính năng tìm kiếm, công thức toán học (math) và biểu thức gán nhãn động (dynamic labels). <br> - Xem và truy vấn dữ liệu CloudWatch Logs. <br> - Tạo các bộ lọc chỉ số (metric filters) và cảnh báo (CloudWatch alarms). <br> - Xây dựng CloudWatch dashboard. | 11/06/2026 | 11/06/2026 |
| 5 | - Hoàn thành Lab37: <br> - Nghiên cứu các khái niệm và tính năng của AWS X-Ray. <br> - Cấu hình tài nguyên AWS cho X-Ray. <br> - Khám phá các chỉ số và biểu đồ CloudWatch. <br> - Bật tính năng vết truy vết (tracing) X-Ray cho ứng dụng. <br> - Khởi tạo các yêu cầu (requests) và dấu truy vết (traces) của ứng dụng. <br> - Phân tích các dấu truy vết và bản đồ dịch vụ (service map). <br> - Xem xét chi tiết các trace và các lỗi phát sinh. <br> - Giám sát các yêu cầu ứng dụng bằng X-Ray. | 12/06/2026 | 12/06/2026 |
| 6 | - Hoàn thành Lab38: <br> - Nghiên cứu các khái niệm AWS CDK và khả năng tích hợp với CloudFormation. <br> - Tạo IAM role và cấu hình môi trường Cloud9. <br> - Tạo một VPC và các public subnets bằng AWS CDK. <br> - Khởi tạo và triển khai một CDK stack. <br> - Cập nhật CDK template để thêm một máy chủ EC2. <br> - Cấu hình EC2 user data để tự động cài đặt Apache. <br> - Xác minh triển khai thành công bằng các lệnh CDK và kiểm tra EC2. | 13/06/2026 | 13/06/2026 |
| 7 | - Hoàn thành Lab40: <br> - Nghiên cứu các khái niệm AWS Glue và Amazon Athena. <br> - Tạo các Amazon S3 buckets và tải lên dữ liệu Báo cáo Chi phí & Sử dụng (Cost & Usage Report). <br> - Cấu hình AWS Glue Crawler, IAM role và Data Catalog. <br> - Kết nối Amazon Athena với Glue Data Catalog. <br> - Thực thi các truy vấn SQL để xem trước và xác minh dữ liệu báo cáo. <br> - Phân tích chi phí dịch vụ AWS, mức độ sử dụng tài khoản và các báo cáo hóa đơn. <br> - Thực hiện phân tích phân bổ chi phí bằng cách sử dụng các resource tags. <br> - So sánh mức độ sử dụng giữa Reserved Instances, Savings Plans và On-Demand. <br> - Xem xét kết quả truy vấn và tổng hợp các chiến lược tối ưu hóa chi phí. | 14/06/2026 | 14/06/2026 |

---

### Thành tựu đạt được trong Tuần 8:

* Lab33: 
  * Triển khai thành công cơ chế mã hóa dữ liệu lưu trữ (encryption at rest) cho các đối tượng S3 sử dụng AWS KMS.
  * Thiết lập cơ chế kiểm soát truy cập chi tiết bằng các IAM policies, roles và groups.
  * Thu thập và phân tích log hoạt động bằng CloudTrail kết hợp với Athena phục vụ mục đích kiểm toán (auditing).
  * Kiểm chứng việc bắt buộc mã hóa bằng cách kiểm thử quyền truy cập với các IAM users khác nhau.
  * Thể hiện khả năng chia sẻ dữ liệu mã hóa an toàn thông qua các pre-signed URLs.
  * Hoàn thành quy trình làm việc khép kín: Mã hóa → Ghi log → Truy vấn → Chia sẻ an toàn.

* Lab34:
  * Đạt được mức độ minh bạch cao về chi phí AWS theo từng dịch vụ, tài khoản và tài nguyên.
  * Nhận diện các cơ hội tối ưu chi phí bằng Savings Plans và Reserved Instances.
  * Tạo các báo cáo chi phí EC2 tùy chỉnh phục vụ việc giám sát liên tục.
  * Tận dụng thẻ phân bổ chi phí (cost allocation tags) để theo dõi chi phí ở cấp độ chi tiết.
  * Hiểu và theo dõi chi phí truyền dữ liệu ra ngoài (Data Transfer Out) – một khoản chi phí thường bị bỏ sót.
  * Áp dụng các nguyên tắc từ AWS Well-Architected Framework để tối ưu hóa chi phí.
  * Xây dựng nền tảng cho việc quản lý chi phí chủ động và phát hiện các điểm bất thường.

* Lab35:
  * Xây dựng thành công kiến trúc Data Lake trên AWS sử dụng S3, Glue, Athena và QuickSight.
  * Tự động hóa quá trình tiếp nhận dữ liệu với Kinesis Firehose và tạo dữ liệu luồng giả lập (synthetic streaming data).
  * Phân loại và cấu trúc dữ liệu thô bằng AWS Glue Crawlers.
  * Truy vấn tương tác các tập dữ liệu lớn bằng ngôn ngữ SQL trên Athena.
  * Biến đổi dữ liệu thô thành các thông tin có giá trị bằng Glue Notebooks.
  * Tạo các bảng biểu trực quan trên QuickSight phục vụ phân tích kinh doanh (Business Intelligence).
  * Thể hiện quy trình làm việc hoàn chỉnh: Thu thập → Phân loại → Truy vấn → Biến đổi → Trực quan hóa.

* Lab36:
  * Triển khai thành công hạ tầng giám sát CloudWatch bằng CloudFormation.
  * Giám sát hiệu năng EC2 sử dụng chỉ số (metrics), công cụ tìm kiếm, tính toán và các nhãn động.
  * Truy vấn và phân tích log với Logs Insights, giúp nâng cao khả năng xử lý sự cố.
  * Chuyển đổi các chuỗi mẫu trong log thành các chỉ số đo lường bằng Metric Filters.
  * Tự động hóa việc giám sát bằng CloudWatch Alarms và thông báo qua email.
  * Xây dựng CloudWatch Dashboard phục vụ trực quan hóa tập trung.
  * Thể hiện quy trình giám sát toàn diện: Chỉ số → Logs → Phân tích chuyên sâu → Cảnh báo → Dashboard.

* Lab37:
  * Khởi tạo và triển khai thành công các CloudFormation templates để cấp phát hạ tầng EC2.
  * Kiểm tra cú pháp và logic templates bằng các công cụ tự động (linting) để đảm bảo độ chính xác.
  * Tự động hóa quá trình tạo stack và cấp phát tài nguyên thông qua AWS CLI.
  * Triển khai các khái niệm nâng cao trong CloudFormation bằng các tài nguyên tùy chỉnh (custom resources) kết hợp với Lambda.
  * Thể hiện quản lý khóa an toàn bằng cách tích hợp EC2 key pairs với SSM Parameter Store.
  * Tích lũy kinh nghiệm thực tế với toàn bộ vòng đời của CloudFormation: Thiết kế → Kiểm tra → Triển khai → Mở rộng.

* Lab38:
  * Thiết lập thành công môi trường AWS CDK trong Cloud9.
  * Triển khai hạ tầng (VPC, subnets, máy chủ EC2) bằng mã nguồn CDK.
  * Tự động hóa cấu hình EC2 bằng kịch bản user data để cài đặt web server Apache.
  * Kiểm chứng quy trình làm việc với CDK: init → synth → diff → deploy.
  * Thể hiện mô hình Hạ tầng dưới dạng Mã (Infrastructure as Code - IaC) sử dụng CDK bằng ngôn ngữ Python.
  * Hoàn thành triển khai một web server hoạt động hoàn chỉnh từ đầu đến cuối thông qua CDK.

* Lab40:
  * Xây dựng thành công nền tảng phân tích dữ liệu sử dụng AWS Glue kết hợp với Athena.
  * Tự động hóa quá trình tiếp nhận và phân loại các Báo cáo Chi phí & Sử dụng (AWS Cost & Usage Reports).
  * Truy vấn hiệu quả các tập dữ liệu lớn bằng công cụ SQL Serverless của Athena.
  * Nhận diện các yếu tố chính gây phát sinh chi phí hàng đầu trên các tài khoản, dịch vụ và việc sử dụng EC2.
  * Tận dụng các thẻ (tags) để phân bổ chi phí, cung cấp góc nhìn phân tích ở cấp độ từng đơn vị kinh doanh.
  * So sánh các mô hình giá (On-Demand vs. Reserved vs. Savings Plans) để đưa ra phương án tối ưu.
  * Phát hiện các Reserved Instances không được sử dụng, chỉ ra các cơ hội tiết kiệm chi phí tiềm năng.
  * Thể hiện quy trình phân tích hoàn chỉnh: Thu thập → Phân loại → Truy vấn → Phân tích → Tối ưu hóa.
