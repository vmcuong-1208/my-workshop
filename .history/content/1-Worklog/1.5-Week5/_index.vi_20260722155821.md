---
title: "Worklog Tuần 5"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---

### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | - Hoàn thành Lab15: <br>&emsp; + Triển khai và kiểm thử ứng dụng trong môi trường cục bộ (local). <br>&emsp; + Cấu hình hạ tầng mạng AWS (VPC, subnets và security groups). <br>&emsp; + Tạo IAM roles và policies cấp quyền truy cập Amazon ECR. <br>&emsp; + Khởi tạo và cấu hình một cơ sở dữ liệu Amazon RDS MySQL Instance. <br>&emsp; + Cấp phát và cấu hình một máy chủ EC2 có cài đặt Docker, Git, AWS CLI và MySQL Client. | 18/05/2026 | 18/05/2026 |
| 2 | - Tiếp tục với Lab15: <br>&emsp; + Khởi tạo cơ sở dữ liệu cho ứng dụng trên Amazon RDS. <br>&emsp; + Đóng gói (build) và triển khai các Docker images cho frontend và backend trên EC2. <br>&emsp; + Triển khai ứng dụng bằng Docker Compose. <br>&emsp; + Tạo các kho lưu trữ (repositories) trên Amazon ECR và Docker Hub. <br>&emsp; + Đẩy (push) các Docker images lên Amazon ECR và Docker Hub. | 19/05/2026 | 19/05/2026 |
| 3 | - Hoàn thành Lab16: <br>&emsp; + Chuẩn bị hạ tầng AWS cho việc triển khai Amazon ECS. <br>&emsp; + Cấu hình hạ tầng mạng, NAT Gateway, route tables và security groups. <br>&emsp; + Đóng gói lại và đẩy các Docker images lên Amazon ECR và Docker Hub. <br>&emsp; + Cấu hình AWS Cloud Map phục vụ cơ chế định danh dịch vụ (service discovery). <br>&emsp; + Tạo một Amazon ECS cluster sử dụng AWS Fargate (Serverless). <br>&emsp; + Tạo các ECS task definitions cho dịch vụ frontend và backend. <br>&emsp; + Cấu hình Application Load Balancer (ALB) và các target groups. <br>&emsp; + Triển khai frontend và backend dưới dạng các ECS services. <br>&emsp; + Cấu hình triển khai Blue/Green và tự động co giãn dịch vụ (service auto scaling). <br>&emsp; + Xác minh việc triển khai ứng dụng thông qua Application Load Balancer. | 20/05/2026 | 20/05/2026 |
| 4 | - Hoàn thành Lab17: <br>&emsp; + Nghiên cứu quy trình CI/CD trên Amazon ECS. <br>&emsp; + So sánh các giải pháp CI/CD: GitLab CI/CD, GitHub Actions, AWS CodeBuild/CodeDeploy/CodePipeline. <br>&emsp; + Khám phá các công cụ giám sát & ghi log: CloudWatch Container Insights, FireLens Logs Router. <br>&emsp; + Xác minh hạ tầng đã triển khai trước đó: VPC, RDS, ECR/Docker Hub, Cloud Map, ECS Cluster, ALB, ứng dụng ECS. <br>&emsp; + GitLab CI/CD: Fork repo, chỉnh sửa code, cài đặt GitLab Runner, cấu hình IAM Role & CI/CD Variables, tạo Git Tag, giám sát pipeline, xác minh triển khai. | 21/05/2026 | 21/05/2026 |
| 5 | - Tiếp tục với Lab17: <br>&emsp; + GitHub Actions: Clone dự án mẫu, phân tích workflows, tạo repo mới, cấu hình GitHub Secrets, tạo Git Tag/Release, giám sát workflow, xác minh triển khai. <br>&emsp; + AWS CodeBuild: Fork repo, chỉnh sửa code, tạo các dự án CodeBuild cho Frontend & Backend, cấu hình IAM, tạo Git Tag, giám sát build/deploy, xác minh kết quả. <br>&emsp; + Giám sát (Monitoring): Bật CloudWatch Container Insights, theo dõi chỉ số (CPU, Memory, Network, Disk), kiểm tra logs. <br>&emsp; + FireLens Log Router: Tạo S3 bucket, IAM Role, cập nhật Task Definition, triển khai phiên bản revision mới, xác minh log được lưu trữ trong S3. | 22/05/2026 | 22/05/2026 |
| 6 | - Nghiên cứu tổng quan về AWS Security Hub và mô hình định giá trong Lab18. <br> - Xem xét các tiêu chuẩn bảo mật được hỗ trợ: <br>&emsp; + AWS Foundational Security Best Practices. <br>&emsp; + CIS AWS Foundations Benchmark. <br>&emsp; + PCI DSS. <br> - Bật Security Hub thông qua AWS Console. <br> - Cấu hình dịch vụ AWS Config để đánh giá mức độ tuân thủ (compliance). <br> - Giám sát điểm số bảo mật (Security Score) và các phát hiện sự cố (findings) theo tiêu chuẩn. <br> - Khám phá việc loại trừ các quy tắc kiểm soát cụ thể khỏi quá trình đánh giá. | 23/05/2026 | 23/05/2026 |
| 7 | - Hoàn thành Lab19: <br>&emsp; + Tạo hai VPC sử dụng mẫu CloudFormation (My VPC & HG VPC). <br>&emsp; + Cấu hình Security Groups với các quy tắc cho SSH, ICMP và truy cập theo dải CIDR tùy chỉnh. <br>&emsp; + Khởi chạy các máy chủ EC2 trong từng VPC và kiểm thử kết nối. <br>&emsp; + Cập nhật Network ACLs để giới hạn lưu lượng và xác minh bảo mật ở cấp độ subnet. <br>&emsp; + Thiết lập kết nối VPC Peering giữa My VPC và HG VPC. <br>&emsp; + Cấu hình các route tables để cho phép giao tiếp giữa các VPC đã kết nối peering. <br>&emsp; + Bật tính năng Cross-Peer DNS để phân giải tên miền (hostname) giữa các VPC. <br>&emsp; + Xác minh kết nối bằng cả địa chỉ IP và tên miền DNS. | 24/05/2026 | 24/05/2026 |

---

### Thành tựu đạt được trong Tuần 5:

* Lab15: 
  * Triển khai thành công ứng dụng full-stack trên AWS sử dụng Docker.
  * Tích hợp ứng dụng với Amazon RDS cho dịch vụ cơ sở dữ liệu managed.
  * Triển khai ứng dụng bằng cả Docker containers độc lập và Docker Compose.
  * Phát hành các Docker images lên Amazon ECR và Docker Hub để quản lý tập trung.
  * Đạt được kinh nghiệm thực tế về triển khai ứng dụng container hóa và thiết lập hạ tầng AWS.

* Lab16:
  * Triển khai thành công ứng dụng container hóa trên Amazon ECS với AWS Fargate.
  * Áp dụng cơ chế định danh dịch vụ (service discovery) bằng AWS Cloud Map cho việc giao tiếp giữa các services.
  * Cấu hình Application Load Balancer, tự động co giãn và triển khai Blue/Green đảm bảo tính sẵn sàng cao.
  * Tích hợp các ECS services với Amazon RDS và Amazon ECR.
  * Tích lũy kinh nghiệm thực tế về triển khai và quản lý container chuẩn Production trên AWS.

* Lab17:
  * Thiết lập thành công quy trình CI/CD cho các ứng dụng ECS sử dụng GitLab CI/CD, GitHub Actions và AWS CodeBuild.
  * Tự động hóa các quy trình Build, Push Image và Deploy lên ECS.
  * Quản lý các phiên bản ứng dụng thông qua Git Tags và ECS Task Definition Revisions.
  * Giám sát tài nguyên ECS bằng CloudWatch Container Insights.
  * Thu thập và lưu trữ log của container vào Amazon S3 thông qua FireLens.
  * Xác minh hiệu năng ứng dụng hoạt động ổn định sau mỗi lần tự động triển khai.

* Lab18:
  * Bật thành công AWS Security Hub và AWS Config.
  * Đánh giá các tài nguyên AWS so với các thực tiễn bảo mật tốt nhất và các tiêu chuẩn tuân thủ.
  * Nhận diện các phát hiện bảo mật và xem xét kết quả tuân thủ.
  * Tùy chỉnh các quy tắc kiểm soát bảo mật dựa trên yêu cầu dự án.

* Lab19:
  * Kết nối thành công hai VPC cô lập thông qua VPC Peering.
  * Cho phép giao tiếp an toàn, độ trễ thấp mà không cần đi qua mạng internet công cộng.
  * Áp dụng bảo mật phân tầng với Security Groups và Network ACLs.
  * Xác minh định tuyến và phân giải DNS giữa các VPC đã kết nối peering.
  * Chứng minh mô hình giao tiếp liên VPC hiệu quả về chi phí và có khả năng mở rộng.
  * Đảm bảo trạng thái bảo mật tối ưu bằng cách áp dụng nguyên tắc quyền tối thiểu (Least Privilege).