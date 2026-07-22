---
title: "Worklog Tuần 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---
### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | Tạo tài khoản AWS để nhận $100, hoàn thành 5 nhiệm vụ để nhận thêm $100 và hoàn thành Lab01 để nhận đủ $200. | 20/04/2026 | 20/04/2026 |
| 2 | - Hoàn thành bài thực hành Lab02 và tạo các tài khoản/định danh như: <br>&emsp; + Nhóm quản trị (Admin Group) <br>&emsp; + Người dùng quản trị (Admin User) <br>&emsp; + Vai trò quản trị (Admin Role) <br>&emsp; + Người dùng vận hành (OperatorUser) <br>&emsp; + Đăng nhập, cơ chế xác thực phiên làm việc, v.v. <br> | 21/04/2026 | 21/04/2026 |
| 3 | - Nghiên cứu kiến trúc mạng AWS - Nền tảng Amazon VPC <br> - Nghiên cứu về Tường lửa ảo (Virtual Firewall) để bảo mật hệ thống <br> - Phân biệt cơ chế giữa Security Group (SG) và Network ACL (NACL). <br> - **Học cách khởi tạo trong Lab03:** <br>&emsp; + VPC <br>&emsp; + Subnet <br> &emsp; + Internet Gateway <br> &emsp; + Route Table <br> &emsp; + Security Group <br> &emsp; + VPC Flow Logs <br> - Học cách triển khai hạ tầng EC2 toàn diện <br> - Học cách kết nối trung tâm dữ liệu on-premises với Amazon VPC bằng phần cứng VPN hoặc phần mềm VPN. | 22/04/2026 | 22/04/2026 |
| 4 | - Tìm hiểu Amazon EC2 và hoàn thành bài thực hành Lab04 | 23/04/2026 | 23/04/2026 |
| 5 | - Tìm hiểu về Amazon RDS <br> - **Hoàn thành bài thực hành Lab05:** <br>&emsp; + Xây dựng kiến trúc mạng Virtual Private Cloud (VPC) cho cơ sở dữ liệu <br>&emsp; + Tạo Security Group (Tường lửa ảo) cho các máy chủ EC2 <br>&emsp; + Tạo Security Group chuyên dụng cho Amazon RDS <br>&emsp; + Khởi tạo DB Subnet Group cho Amazon RDS <br>&emsp; + Khởi tạo và cấu hình máy chủ ứng dụng (Amazon EC2 Instance) <br>&emsp; + Triển khai môi trường Node.js trên EC2 và khởi tạo Amazon RDS Instance <br>&emsp; + Triển khai mã nguồn backend và kết nối với hệ quản trị cơ sở dữ liệu Amazon RDS. <br>&emsp; + Thực thi quy trình sao lưu (backup) và phục hồi (restore) dữ liệu trên Amazon RDS. | 24/04/2026 | 24/04/2026 |
| 6 | - Hiểu cách sử dụng Launch Template làm khuôn mẫu, để Auto Scaling tự động khởi tạo máy chủ dựa trên nhu cầu của khách hàng, và để Load Balancer phân phối đều lượng truy cập tới các máy chủ đó; hoàn thành Lab06. | 25/04/2026 | 25/04/2026 |
| 7 | Tiếp tục hoàn thiện Lab06 | 26/04/2026 | 26/04/2026 |

---

### Thành tựu đạt được trong Tuần 1:

* Tạo tài khoản thành công và hoàn thành các nhiệm vụ để nhận $200 tín dụng miễn phí.

* Hiểu rõ bản chất và chức năng của các nhóm người dùng IAM (IAM Groups):
  * Hiểu cơ chế phân quyền dựa trên vai trò (Role-Based Access Control - RBAC).
  * Sử dụng người dùng IAM (IAM Users) thay vì tài khoản root cho tất cả các hoạt động AWS hàng ngày.
  * Hiểu và áp dụng thực tiễn tốt nhất (Best practice) về việc sử dụng IAM Roles để truy cập an toàn bằng thông tin xác thực tạm thời từ STS thay vì dùng thông tin xác thực cố định.
  * Thiết lập OperatorUser có quyền chuyển đổi sang AdminRole, tuân thủ Nguyên tắc quyền tối thiểu (Principle of Least Privilege) bằng cách chỉ cấp duy nhất quyền đảm nhận vai trò (AssumeRole).
  * Chuyển đổi thành công sang AdminRole sử dụng thông tin xác thực bảo mật tạm thời với quyền AdministratorAccess, tuân thủ đúng thực tiễn tốt nhất về phân quyền quản trị qua IAM Roles.

* Xây dựng thành công hạ tầng Amazon VPC an toàn, sẵn sàng cho môi trường Production với kết nối Site-to-Site VPN bằng cách áp dụng các thực tiễn tốt nhất về mạng của AWS và Hạ tầng dưới dạng mã (Infrastructure as Code - IaC).

* Triển khai và quản lý thành công các máy chủ Amazon EC2 trên cả hai hệ điều hành Windows và Linux, đồng thời lưu trữ ứng dụng Node.js tuân thủ các thực tiễn bảo mật của AWS:
  * Khởi chạy và cấu hình thành công các máy chủ EC2 Windows và Linux với kết nối RDP/SSH ổn định.
  * Hoàn thành Sysprep, tạo các bản đóng gói AMIs, EBS snapshots và triển khai các máy chủ nhân bản (cloned instances) mà không bị mất dữ liệu.
  * Khôi phục quyền truy cập an toàn (RDP/SSH) thông qua SSM, cloud-init và các cặp khóa (key pairs) mới, đảm bảo tính liên tục cho hoạt động kinh doanh.
  * Truy cập giao diện người dùng Ubuntu GUI thông qua xRDP, cho phép quản lý máy chủ linh hoạt qua 2 chế độ.
  * Triển khai Apache, MariaDB và toàn bộ LAMP stack với các cấu hình gia cố bảo mật.
  * Thiết lập phpMyAdmin, tạo cơ sở dữ liệu `awsuser` và chuẩn bị tích hợp backend cho Node.js.
  * Cài đặt NVM, Node.js, npm và triển khai thành công ứng dụng AWS User Management fullstack với các thao tác CRUD hoạt động ổn định.
  * Cấu hình XAMPP và Windows Server 2025 cho việc triển khai backend, bao gồm Git, Node.js và VS Code.
  * Triển khai Node.js backend trên Windows Server kết nối đồng bộ với MySQL, hoàn thiện kiến trúc phân tầng.
  * Áp dụng các chính sách IAM phân quyền chi tiết:
    * Giới hạn theo vùng địa lý (chỉ cho phép khu vực Singapore).
    * Kiểm soát loại máy chủ (cho phép dòng chip ARM, chặn các dòng x86 cấu hình cao).
    * Rào chắn tài nguyên (cho phép `t3.small` + `gp3`, chặn `m5.4xlarge` + `gp2`).
    * Giới hạn truy cập theo địa chỉ IP và khung thời gian để ngăn chặn hành vi xóa/tắt máy chủ EC2 trái phép hoặc ngoài giờ làm việc.

* Triển khai và quản lý thành công Amazon RDS với cấu hình cơ sở dữ liệu quan hệ an toàn, có khả năng mở rộng và tính sẵn sàng cao theo thực tiễn tốt nhất của AWS:
  * Triển khai thành công hạ tầng mạng Lab05 VPC với các public/private subnets an toàn, Internet Gateway, Route Tables và VPC Endpoints, tạo nền tảng tối ưu chi phí cho Amazon RDS.
  * Tạo Security Group `EC2-Web-App-SG` để bảo vệ lớp frontend và thiết lập Security Group riêng `RDS-MySQL-SG` để kiểm soát truy cập từ EC2 tới cơ sở dữ liệu.
  * Áp dụng bảo mật phân tầng bằng cách chỉ cho phép duy nhất các máy chủ EC2 truy cập vào RDS, giúp kết nối CSDL linh hoạt và không phụ thuộc vào IP cố định.
  * Xây dựng DB Subnet Group hợp lệ cho RDS trải dài trên nhiều Availability Zones (AZs), hoàn thiện lớp hạ tầng sẵn sàng cấp phát RDS.
  * Khởi chạy và truy cập thành công máy chủ EC2 Node.js backend nằm trong VPC, cấu hình đúng quy tắc Security Group và SSH, sẵn sàng cho việc thiết lập môi trường chạy ứng dụng và tích hợp RDS.
  * Kết nối thành công backend với Amazon RDS nằm trong private subnet, hiển thị dữ liệu người dùng động và xác nhận hiệu năng CSDL ổn định, sẵn sàng cho quy trình sao lưu và khôi phục snapshot.
  * Phục hồi thành công CSDL RDS từ bản snapshot với đầy đủ cấu trúc schema và dữ liệu, thiết lập lại kết nối an toàn từ EC2 tới RDS, hoàn thành quy trình quản lý vòng đời ứng dụng chuẩn Production.

* Triển khai thành công VPC Multi-AZ với kiến trúc subnet hoàn chỉnh, bật tự động gán IP public và thiết lập tường lửa an toàn, chuẩn bị cho việc tích hợp Launch Template và Elastic Load Balancer.
* Khởi chạy máy chủ EC2 `FCJ-Management` tích hợp chuẩn xác vào VPC, cấp phát IP public, vượt qua các kiểm tra sức khỏe của AWS, sẵn sàng cho việc cấu hình SSH và tạo AMI phục vụ Auto Scaling.
* Cấp phát cơ sở dữ liệu Amazon RDS MySQL (`fcj-management-db-instance`) trên subnet group Multi-AZ, trích xuất endpoint/port và chuẩn bị tích hợp backend kèm kế hoạch dọn dẹp tài nguyên chuẩn Production để tối ưu chi phí.
* Cấu hình môi trường EC2 CLI, xác minh bảng `user` chứa 18 bản ghi dữ liệu và xác nhận kết nối ổn định giữa EC2 và RDS thông qua Security Groups.
* Triển khai ứng dụng web chạy ngầm trên cổng 5000 bằng PM2, bật tự động khởi động lại khi reboot máy chủ và chuẩn bị máy chủ EC2 làm ảnh mẫu (base image) cho Launch Template.
* Tạo bản đóng gói AMI tùy chỉnh (`FCJ-Management-AMI`) và Launch Template v1, đặt nền tảng cho Auto Scaling trong môi trường Node.js backend Multi-AZ.
* Xây dựng Target Group `FCJ-Management`, đăng ký máy chủ ứng dụng trên cổng 5000 và hoàn tất cấu hình định tuyến cho tích hợp Application Load Balancer (ALB).
* Triển khai Application Load Balancer ở trạng thái Active, cấu hình DNS endpoint và xác minh khả năng định tuyến lưu lượng qua Listener và Target Group tới backend EC2.
* Kiểm thử thành công hạ tầng bất biến (immutable infrastructure) dựa trên Launch Template và AMI, chuẩn bị cho việc cấu hình Auto Scaling Group và các chính sách mở rộng tự động.
* Xác nhận kiểm tra sức khỏe (health checks) của ALB trả về HTTP 200 OK, đảm bảo luồng lưu lượng thông suốt và kiến trúc ổn định sẵn sàng cho Auto Scaling.
* Cấu hình Auto Scaling Group đi kèm thông báo qua email bằng Amazon SNS, kích hoạt khởi tạo máy chủ EC2 ban đầu và bật giám sát CloudWatch cho việc tự động co giãn.
* Kiểm thử và xác minh hành vi cân bằng tải cùng co giãn: phân phối tải CPU ổn định khi có 2 máy chủ, hiệu năng giảm khi giảm xuống 1 máy chủ — xác nhận tính cấp thiết của cơ chế tự động co giãn động (Dynamic Scaling).
* Thực thi cơ chế co giãn theo lịch trình (Scheduled Scaling) vào lúc 17:15, hệ thống tự động thêm 1 máy chủ EC2 mới; CloudWatch xác nhận lưu lượng được phân bổ lại và tải CPU nhanh chóng ổn định.
* Kiểm thử thành công cơ chế co giãn động (Dynamic Scaling): tự động tăng từ 1 lên 3 máy chủ khi tải tăng cao, phân phối lại lưu lượng sau thời gian làm nóng (warmup), và giảm số lượng máy chủ khi hết tải (cooldown) để tiết kiệm chi phí.
* Kết hợp thành công giữa co giãn theo lịch trình và co giãn động để đạt được một hạ tầng có tính linh hoạt cao và thiết kế tối ưu (Well-Architected).
* Áp dụng thành công cơ chế co giãn dự đoán (Predictive Scaling) với khả năng dự báo tải chính xác, chủ động cấp phát tài nguyên và lập kế hoạch dung lượng, đảm bảo hệ thống AWS hoàn toàn linh hoạt và tối ưu hóa chi phí.