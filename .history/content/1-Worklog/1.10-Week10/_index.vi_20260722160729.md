---
title: "Worklog Tuần 10"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.10. </b> "
---

### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | Hoàn thành Lab41: <br> - Tìm hiểu các khái niệm AWS IAM Federation, SAML và Single Sign-On (SSO). <br> - Tạo và cấu hình Azure Active Directory tenant cùng các người dùng. <br> - Tạo một Enterprise Application và cấu hình SSO dựa trên SAML. <br> - Tạo một AWS Identity Provider sử dụng dữ liệu đặc tả (metadata) từ Azure AD. | 22/06/2026 | 22/06/2026 |
| 2 | Tiếp tục với Lab41: <br> - Tạo các IAM roles với các quyền truy cập Amazon S3 và Amazon EC2. <br> - Cấu hình Azure provisioning và đồng bộ hóa các AWS IAM roles. <br> - Gán các IAM roles cho Azure AD users và kiểm thử đăng nhập vào AWS. <br> - Xác minh quyền truy cập dịch vụ AWS của người dùng dựa trên vai trò được gán. | 23/06/2026 | 23/06/2026 |
| 3 | Hoàn thành Lab42: <br> - Tìm hiểu các khái niệm AWS Savings Plans, Reserved Instances và Reserved DB Instances. <br> - Khám phá các gói Compute và EC2 Instance Savings Plans với các tùy chọn thanh toán khác nhau. <br> - Xem xét các khuyến nghị Savings Plan bằng công cụ AWS Cost Management. <br> - Thực hành tạo, lên lịch và quản lý các gói Savings Plans. <br> - Tìm hiểu các tính năng của Standard Reserved Instance và Convertible Reserved Instance. <br> - Khám phá quy trình mua và cấu hình Reserved DB Instance. <br> - So sánh các hình thức On-Demand, Savings Plans, Reserved Instances và Reserved DB Instances. <br> - Xem xét các thực tiễn tốt nhất khi lựa chọn các tùy chọn định giá dài hạn. | 24/06/2026 | 24/06/2026 |
| 4 | Hoàn thành Lab44: <br> - Tìm hiểu các khái niệm AWS IAM, bao gồm Users, Groups, Roles và Policies. <br> - Tạo các IAM groups và users với các cấp độ phân quyền khác nhau. <br> - Gán các AWS managed policies cho người dùng và nhóm. <br> - Kiểm thử quyền truy cập của người dùng đối với các dịch vụ EC2 và RDS. <br> - Tạo một IAM role với quyền AdministratorAccess. <br> - Cấu hình mối quan hệ tin cậy (trust relationships) và tính năng chuyển đổi vai trò (Switch Role) trong IAM Role. <br> - Áp dụng các điều kiện dựa trên địa chỉ IP và thời gian cho IAM roles. <br> - Xác minh các giới hạn truy cập vai trò và tổng hợp các thực tiễn tốt nhất cho IAM. | 25/06/2026 | 25/06/2026 |
| 5 | Hoàn thành Lab47: <br> - Tìm hiểu các khái niệm AWS Step Functions và quy trình điều phối công việc (workflow orchestration). <br> - Học kiến trúc State Machine và quy trình nghiệp vụ. <br> - Tạo một workflow sử dụng các trạng thái Task, Choice và Parallel. <br> - Tích hợp các hàm AWS Lambda vào state machine. <br> - Kiểm thử việc thực thi workflow thông qua giao diện Step Functions console. | 26/06/2026 | 26/06/2026 |
| 6 | Tiếp tục với Lab47: <br> - Cấu hình mẫu Wait for Task Token và mô hình callback. <br> - Triển khai quy trình Tạm dừng/Tiếp tục (Pause/Resume) cho phê duyệt thủ công. <br> - Thêm các cơ chế Thử lại (Retry) và Bắt lỗi (Catch) để xử lý ngoại lệ. <br> - Kiểm thử các kịch bản workflow khác nhau và xử lý lỗi. <br> - Giám sát lịch sử thực thi và thông tin gỡ lỗi (debugging). | 27/06/2026 | 27/06/2026 |
| 7 | Hoàn thành Lab47: <br> - Tìm hiểu các khái niệm AWS Elastic Beanstalk và CloudFormation. <br> - Tạo một CloudFormation stack và triển khai hạ tầng AWS. <br> - Cấu hình AWS CLI, cặp khóa (key pair) và các quyền IAM. <br> - Kết nối tới máy chủ Windows EC2 và cấu hình cơ sở dữ liệu MySQL. <br> - Nhập dự án TravelBuddy vào Eclipse và hoàn tất cấu hình ứng dụng. | 28/06/2026 | 28/06/2026 |

---

### Thành tựu đạt được trong Tuần 10:

* Lab41: 
  * Tích hợp thành công Azure AD với AWS IAM Federation sử dụng chuẩn SAML.
  * Bật tính năng Đăng nhập một lần (Single Sign-On - SSO) cho người dùng Azure AD vào hệ thống AWS.
  * Thiết lập cơ chế kiểm soát truy cập dựa trên vai trò (RBAC) trên các dịch vụ AWS (S3, EC2).
  * Tự động hóa quá trình đồng bộ hóa các AWS IAM roles vào Azure AD.
  * Kiểm chứng quá trình đăng nhập liên định danh an toàn và việc thực thi phân quyền chuẩn xác.
  * Thể hiện quy trình liên định danh hoàn chỉnh: Azure AD → SAML → AWS IAM → Truy cập theo vai trò.

* Lab42:
  * Nắm vững các mô hình tối ưu hóa chi phí của AWS: Savings Plans, Reserved Instances và Reserved DB Instances.
  * Thực hành mua và quản lý các gói Savings Plans, bao gồm việc lập kế hoạch và hủy các cam kết đang trong hàng chờ.
  * Phân biệt rõ sự khác nhau giữa Standard RIs và Convertible RIs, cũng như cách thức hoạt động của thị trường bán lại (marketplace resale).
  * Hiểu cách Reserved DB Instances mang lại ưu đãi giảm giá nhưng yêu cầu sự tương thích chính xác về mặt cấu hình.
  * Rèn luyện kỹ năng thực tế khi sử dụng các giao diện AWS Cost Management, EC2 và RDS console để thực hiện các cam kết tiết kiệm chi phí.
  * Củng cố kiến thức về trụ cột Tối ưu hóa chi phí trong AWS Well-Architected Framework.

* Lab44:
  * Triển khai nguyên tắc quyền tối thiểu (Least Privilege) bằng cách tách biệt người dùng quản trị EC2 và RDS.
  * Thể hiện khả năng đảm nhận vai trò (role assumption) với thông tin xác thực tạm thời thông qua AWS STS.
  * Tăng cường bảo mật bằng cách áp dụng các điều kiện ràng buộc (IP và thời gian) cho các IAM roles.
  * Kiểm chứng việc chặn thành công các nỗ lực truy cập vai trò trái phép.
  * Tích lũy kinh nghiệm thực tế trong việc kết hợp IAM Users, Groups, Roles và Conditions để kiểm soát truy cập chi tiết.
  * Thể hiện cách kết hợp IAM federation và chính sách điều kiện để nâng cao an toàn bảo mật mà vẫn đảm bảo tính linh hoạt.

* Lab47:
  * Thiết lập thành công môi trường Cloud9 + SAM cho phát triển ứng dụng Serverless.
  * Xây dựng và kiểm thử các dịch vụ dựa trên Lambda cho việc đăng ký tài khoản và xác thực dữ liệu.
  * Học cách thiết kế và thực thi các máy trạng thái (state machines) trong Step Functions sử dụng các trạng thái Pass và Task.
  * Tích hợp các hàm Lambda vào quy trình làm việc với đầy đủ quyền hạn từ IAM role.
  * Trực quan hóa quá trình thực thi workflow, dữ liệu đầu vào/đầu ra và xử lý lỗi trên Step Functions console.
  * Thể hiện khả năng điều phối dịch vụ với các tính năng rẽ nhánh, xử lý song song và tạm dừng/tiếp tục.
  * Tích lũy kinh nghiệm thực tế khi kết hợp Lambda, DynamoDB, SAM và Step Functions cho tự động hóa quy trình.

* Lab50:
  * Di dời thành công một ứng dụng Spring Boot đơn khối (monolithic) - TravelBuddy lên hạ tầng AWS.
  * Kiểm chứng khả năng chạy cục bộ kết hợp với cơ sở dữ liệu RDS trước khi triển khai chính thức lên Cloud.
  * Triển khai ứng dụng lên Elastic Beanstalk đạt độ sẵn sàng cao (High Availability) và tự động mở rộng (Auto-scaling).
  * Thực hành cập nhật ứng dụng thông qua Elastic Beanstalk CLI, hỗ trợ quá trình triển khai tự động.