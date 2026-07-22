---
title: "Worklog Tuần 7"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | - Hoàn thành Lab27: <br> - Tạo các máy chủ EC2 kèm các thẻ (tags: Owner, Service, Environment). <br> - Thao tác thêm, sửa và xóa tags trên tài nguyên đơn lẻ cũng như nhiều tài nguyên cùng lúc qua AWS Console. <br> - Lọc danh sách EC2 theo tags (ví dụ: Owner, Environment). <br> - Sử dụng AWS CLI để: <br>&emsp; + Thêm tags vào các tài nguyên EC2 hiện có. <br>&emsp; + Thêm tags trực tiếp trong quá trình khởi tạo tài nguyên (instances, volumes). <br>&emsp; + Truy vấn danh sách tài nguyên được lọc theo tags. <br> - Tạo Resource Group sử dụng truy vấn dựa trên tag (**BusinessUnit=Marketing**). <br> - Xác minh các tài nguyên đã được nhóm lại trong Resource Group (**MarketingBu**). | 01/06/2026 | 01/06/2026 |
| 2 | - Hoàn thành Lab28: <br> - Tạo IAM AdminGroup gán policy **AdministratorAccess**. <br> - Tạo IAM **AdminUser** có quyền truy cập console và đã bật xác thực MFA. <br> - Định nghĩa các IAM policies với các điều kiện (conditions) dựa trên Regions và Resource Tags: <br>&emsp; + **ec2-list-read** → quyền chỉ đọc EC2 trong regions **us-east-1** & **us-west-1**. <br>&emsp; + **ec2-create-tags** → chỉ cho phép tạo tag khi đang khởi chạy máy chủ EC2. <br>&emsp; + **ec2-create-tags-existing** → áp đặt điều kiện tag (**Team=Alpha**, với các keys **Team** & **Name**). <br>&emsp; + **ec2-run-instances** → chỉ cho phép tạo instance tại các regions được phép và phải gắn đúng tags. <br>&emsp; + **ec2-manage-instances** → cho phép start/stop/reboot/terminate nếu có tag **Team=Alpha**. <br> - Tạo IAM Role **ec2-admin-team-alpha** và gán toàn bộ các policies trên. <br> - Cấu hình mối quan hệ tin cậy (trust relationships) bắt buộc có MFA. <br> - Kiểm thử các IAM policies bằng cách: <br>&emsp; + Thử truy cập ở region không được phép (Tokyo → bị từ chối). <br>&emsp; + Truy cập region được phép (North Virginia → thành công). <br>&emsp; + Khởi chạy EC2 với tags không chính xác (thất bại). <br>&emsp; + Khởi chạy EC2 với tags chính xác (**Team=Alpha**) → thành công. <br>&emsp; + Chỉnh sửa tags thành giá trị không hợp lệ → bị từ chối. <br>&emsp; + Thực hiện quản lý máy chủ EC2 (terminate) → thành công. | 02/06/2026 | 02/06/2026 |
| 3 | - Hoàn thành Lab29: <br> - Tìm hiểu các tính năng, dashboards của Grafana và các khái niệm giám sát. <br> - Tạo một VPC và cấu hình một public subnet. <br> - Cấu hình các quy tắc security group để truy cập EC2. <br> - Triển khai một máy chủ Amazon Linux EC2. <br> - Tạo một IAM user với quyền quản trị viên (administrator access). <br> - Tạo policy truy cập CloudWatch và IAM role tương ứng. <br> - Gán IAM role cho máy chủ EC2. <br> - Cài đặt và khởi chạy Grafana trên Amazon Linux. <br> - Thêm CloudWatch làm nguồn dữ liệu (data source) cho Grafana. <br> - Xây dựng dashboard giám sát hiệu suất sử dụng CPU của EC2. <br> - Chia sẻ dashboard và khám phá các chỉ số (metrics) của CloudWatch. <br> - Giám sát hiệu năng EC2 bằng các biểu bảng (panels) trên Grafana. | 03/06/2026 | 03/06/2026 |
| 4 | - Hoàn thành Lab30: <br> - Tìm hiểu khái niệm IAM Permission Boundary và vai trò của nó trong việc giới hạn quyền hạn tối đa. <br> - Tạo policy giới hạn chỉ cho phép các thao tác EC2 tại region **ap-southeast-1 (Singapore)**. <br> - Áp dụng Permission Boundary cho IAM user **ec2-admin**. <br> - Kiểm thử quyền truy cập của IAM user: <br>&emsp; + Xác minh dịch vụ EC2 hoạt động bình thường tại region Singapore. <br>&emsp; + Xác nhận truy cập EC2 bị từ chối tại region Sydney mặc dù user có policy full EC2 admin. | 04/06/2026 | 04/06/2026 |
| 5 | - Hoàn thành Lab31: <br> - Chuẩn bị hạ tầng: <br>&emsp; + Tạo một VPC và các Subnets riêng biệt, bật tự động gán IPv4 public. <br>&emsp; + Khởi chạy 2 máy chủ Windows EC2 (Windows-Lab-SSM-1 và Windows-Lab-SSM-2) ở các subnets khác nhau. <br>&emsp; + Tạo và gán một IAM Role có chứa policy **AmazonSSMManagedInstanceCore** cho cả hai máy chủ. <br> - Thiết lập Systems Manager: <br>&emsp; + Xác minh cả hai máy chủ đã xuất hiện dưới dạng Managed Nodes trong Fleet Manager. <br>&emsp; + Khởi tạo các phiên terminal để xác nhận kết nối thành công tới cả hai máy chủ Windows EC2. <br> - Patch Manager: <br>&emsp; + Sử dụng tính năng “Patch now” với tùy chọn Scan & Install. <br>&emsp; + Chọn cả hai máy chủ Windows EC2 làm mục tiêu nâng cấp bản vá. <br>&emsp; + Theo dõi và xác nhận kết quả vá lỗi thành công. <br> - Run Command: <br>&emsp; + Thực thi tài liệu AWS-RunPowerShellScript với lệnh net user trên cả hai máy chủ. <br>&emsp; + Cấu hình kết quả xuất ra (output) để lưu trữ trong một S3 bucket. <br>&emsp; + Xem lại kết quả thực thi lệnh và log lỗi từ từng máy chủ. | 05/06/2026 | 05/06/2026 |
| 6 | - Hoàn thành Lab32: <br> - Giám sát các chỉ số hiệu năng EC2 bằng Amazon CloudWatch (CPU, memory, network, disk). <br> - Tạo IAM Role với policy CloudWatchAgentServerPolicy và gán cho EC2. <br> - Cài đặt và cấu hình CloudWatch Agent để thu thập các chỉ số sử dụng bộ nhớ (memory usage). <br> - Xác minh các chỉ số trong CloudWatch dưới namespace CWAgent. | 06/06/2026 | 06/06/2026 |
| 7 | - Tiếp tục với Lab32: <br> - Sử dụng Amazon EC2 Resource Optimization để xem các khuyến nghị tối ưu quy mô (right-sizing) (xóa các máy chủ nhàn rỗi, hạ cấp các máy chủ chưa dùng hết hiệu năng). <br> - Áp dụng các thực tiễn tốt nhất về right-sizing (kiểm thử khối lượng công việc, thay đổi kích thước trước khi dịch chuyển, kết hợp với Savings Plans/Reserved Instances). <br> - Bật dịch vụ AWS Compute Optimizer: <br>&emsp; + Tạo service-linked IAM policy. <br>&emsp; + Cấp quyền truy cập (ComputeOptimizerReadOnlyAccess). <br>&emsp; + Đăng ký kích hoạt Compute Optimizer cho tài khoản. <br> - Xem xét các khuyến nghị từ Compute Optimizer cho EC2, Auto Scaling groups, EBS volumes, Lambda và Fargate. | 07/06/2026 | 07/06/2026 |

---

### Thành tựu đạt được trong Tuần 7:

* Lab28: 
  * Thực thi nguyên tắc quyền tối thiểu (least privilege) trong IAM bằng các conditional policies.
  * Áp đặt các giới hạn truy cập theo khu vực địa lý (region) đối với các thao tác trên EC2.
  * Áp dụng cơ chế kiểm soát truy cập dựa trên tag (ABAC) để đảm bảo chỉ những tài nguyên được gắn tag đúng quy chuẩn mới được tạo/quản lý.
  * Kiểm chứng thành công cơ chế chuyển đổi IAM role yêu cầu xác thực MFA nhằm tăng cường bảo mật.
  * Kiểm thử thành công và xác nhận các IAM policies hoạt động chính xác như thiết kế.
  * Thể hiện khả năng quản lý quyền chi tiết kết hợp giữa Resource Tags và IAM Conditions.

* Lab29: 
  * Nắm vững kiến trúc và khả năng trực quan hóa dữ liệu của Grafana.
  * Chuẩn bị thành công môi trường hạ tầng mạng.
  * Bật kết nối mạng an toàn.
  * Triển khai thành công máy chủ Grafana.
  * Khởi tạo thông tin đăng nhập phục vụ xác thực vào Grafana.
  * Cấp quyền cho EC2 để truy cập các chỉ số của CloudWatch.
  * Cho phép kết nối thành công tới CloudWatch từ máy chủ EC2.
  * Truy cập thành công vào giao diện web của Grafana.
  * Xác minh tích hợp thành công dữ liệu từ CloudWatch.
  * Hiển thị thành công các chỉ số đo lường AWS theo thời gian thực.
  * Xác minh khả năng truy cập dashboard và kết quả truy vấn.
  * Tích lũy kinh nghiệm thực tế về giám sát và trực quan hóa dữ liệu trên AWS.

* Lab30:
  * Áp dụng thành công IAM Permission Boundary để thắt chặt các giới hạn truy cập theo region.
  * Thể hiện sự kết hợp hiệu quả giữa identity-based policy và permission boundary để kiểm soát quyền hạn một cách chi tiết.
  * Ngăn chặn rủi ro leo thang đặc quyền (privilege escalation) bằng cách giới hạn quyền hạn thực tế của user không vượt quá boundary cho phép.
  * Xác nhận IAM Permission Boundary là một công cụ mạnh mẽ để quản lý quyền hàng loạt và gia cố bảo mật hạ tầng.

* Lab31:
  * Khởi tạo thành công môi trường mạng (VPC, Subnets) và triển khai 2 máy chủ Windows EC2 cho bài lab.
  * Gán IAM Role chính xác, cho phép Systems Manager quản lý trực tiếp các máy chủ.
  * Xác minh kết nối giữa Systems Manager và cả hai nút Windows EC2 thông qua Fleet Manager.
  * Cập nhật bản vá (patch) đồng thời trên nhiều máy chủ mà không cần đăng nhập thủ công vào từng máy.
  * Thực thi từ xa các lệnh PowerShell trên nhiều máy chủ và thu thập kết quả tập trung tại S3 bucket.
  * Hoàn thành toàn bộ quy trình quản lý, vá lỗi và điều khiển từ xa các máy chủ Windows bằng AWS Systems Manager.

* Lab32:
  * Thu thập thành công các chỉ số CPU + Memory bằng CloudWatch Agent phục vụ việc đánh giá quy mô chính xác.
  * Nhận diện các máy chủ EC2 nhàn rỗi hoặc hoạt động dưới công suất nhờ tính năng Resource Optimization.
  * Áp dụng các chiến lược tối ưu chi phí (Savings Plans, Reserved Instances) song song với việc điều chỉnh quy mô (right-sizing).
  * Kích hoạt AWS Compute Optimizer để tự động đưa ra khuyến nghị tối ưu trên toàn bộ các dịch vụ tính toán (compute services).
  * Chứng minh khả năng cải thiện hiệu quả chi phí và hiệu năng vận hành bằng cách tinh chỉnh kích thước EC2 phù hợp với nhu cầu sử dụng thực tế.
  * Kiểm chứng mô hình tối ưu hóa kết hợp: Giám sát (Monitoring) → Điều chỉnh quy mô (Right-sizing) → Cam kết chi phí (Savings Plans/RI).