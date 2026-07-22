---
title: "Worklog Tuần 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | - **Tìm hiểu sâu hơn về AWS Budgets trong Lab07 để hỗ trợ quản lý chi phí trên tài khoản AWS:** <br>&emsp; + Cấu hình AWS Budgets để giám sát và kiểm soát chi phí tài khoản AWS. <br>&emsp; + Tạo các loại ngân sách khác nhau (Ngân sách chi phí, Sử dụng, RI, Savings Plans). <br>&emsp; + Thiết lập các ngưỡng ngân sách và mức cảnh báo phù hợp. <br>&emsp; + Bật cảnh báo thông báo khi vi phạm ngưỡng chi phí hoặc mức sử dụng. <br>&emsp; + Giám sát mức chi tiêu và điều chỉnh ngân sách để tối ưu hóa việc quản lý chi phí cloud. | 27/04/2026 | 27/04/2026 |
| 2 | - **Tìm hiểu về CloudWatch trong Lab08:** <br>&emsp; + Tìm hiểu và khám phá khả năng giám sát và quan sát (observability) của Amazon CloudWatch. <br>&emsp; + Cấu hình và phân tích chỉ số CloudWatch Metrics cho các tài nguyên AWS. <br>&emsp; + Thu thập, xem và quản lý log ứng dụng cũng như hệ thống bằng CloudWatch Logs. <br>&emsp; + Tạo và cấu hình cảnh báo CloudWatch Alarms cho các ngưỡng giám sát. <br>&emsp; + Xây dựng CloudWatch Dashboards để trực quan hóa tập trung sức khỏe và hiệu năng hệ thống. <br>&emsp; + Hiểu các chiến lược giám sát cho ứng dụng, hạ tầng và môi trường container. | 28/04/2026 | 28/04/2026 |
| 3 | - Tìm hiểu về các công cụ cốt lõi của Route 53 Resolver (Inbound Endpoints và Outbound Endpoints) cùng các quy tắc Route 53 Resolver Rules trong Lab10. <br>&emsp; + Thiết lập kiến trúc DNS lai (Hybrid DNS) bằng Amazon Route 53 Resolver. <br>&emsp; + Cấu hình Inbound Endpoints để cho phép các truy vấn DNS từ on-premises phân giải các tên miền được lưu trữ trên AWS. <br>&emsp; + Cấu hình Outbound Endpoints để chuyển tiếp các truy vấn DNS từ AWS tới hệ thống DNS on-premises. <br>&emsp; + Định nghĩa và áp dụng các quy tắc Route 53 Resolver Rules để chuyển tiếp truy vấn tên miền. <br>&emsp; + Xác thực luồng phân giải DNS giữa môi trường on-premises và AWS. | 29/04/2026 | 29/04/2026 |
| 4 | - Học cách sử dụng giao diện dòng lệnh AWS CLI để tương tác với các dịch vụ AWS thông qua câu lệnh trong Lab11 <br>&emsp; + Cài đặt và cấu hình AWS CLI để tương tác với các dịch vụ AWS bằng dòng lệnh. <br>&emsp; + Thiết lập IAM users, groups và access keys để xác thực an toàn cho CLI. <br> &emsp; + Cấu hình AWS CLI profiles, region mặc định và định dạng đầu ra (output formats). <br> &emsp; + Sử dụng AWS CLI để quản lý và tương tác với tài nguyên AWS qua terminal (Linux, Windows, hoặc EC2 SSH). <br> &emsp; + Hiểu và áp dụng các thực tiễn tốt nhất về bảo mật như quyền tối thiểu (Least Privilege) và lưu trữ thông tin xác thực an toàn. <br> &emsp; + Thực hiện quản lý tài nguyên AWS cơ bản bằng lệnh CLI thay vì dùng AWS Management Console. | 30/04/2026 | 30/04/2026 |
| 5 | - Học cách sử dụng AWS Backup để tạo các kế hoạch sao lưu (backup plans) cho các tài nguyên AWS đang hoạt động như ổ đĩa EBS, cơ sở dữ liệu RDS, bảng DynamoDB hoặc hệ thống tệp EFS. Học cách phục hồi dữ liệu từ các bản sao lưu và tự động hóa toàn bộ quy trình trong Lab13. | 01/05/2026 | 01/05/2026 |
| 6 | - Học cách cấp quyền cho ứng dụng truy cập vào các dịch vụ AWS trong Lab48: <br>&emsp; + Tạo một máy chủ EC2 và một S3 bucket cho việc tích hợp ứng dụng. <br>&emsp; + Cấp quyền truy cập S3 bằng Access Keys của IAM User và đánh giá các rủi ro bảo mật liên quan. <br>&emsp; + Tạo và gắn IAM Role (EC2 Instance Profile) cho máy chủ EC2. <br>&emsp; + Cho phép ứng dụng truy cập an toàn vào Amazon S3 mà không cần lưu cứng thông tin xác thực (credentials). <br>&emsp; + Xác minh thông tin xác thực tạm thời qua AWS STS và kiểm thử quyền truy cập AWS CLI bằng IAM Role. | 02/05/2026 | 03/05/2026 |
| 7 | - Hoàn thành Lab49: <br>&emsp; + Tạo một máy chủ EC2 và một S3 bucket cho việc tích hợp ứng dụng. <br>&emsp; + Tạo và cấu hình môi trường phát triển AWS Cloud9. <br>&emsp; + Khám phá Cloud9 IDE, terminal và các lệnh Linux cơ bản. <br>&emsp; + Tạo, chỉnh sửa và quản lý các tệp tin trong không gian làm việc Cloud9. <br>&emsp; + Điều hướng giữa Cloud9 IDE và AWS Management Console. <br>&emsp; + Thực thi các lệnh AWS CLI từ Cloud9 để tương tác với tài nguyên AWS. | 03/05/2026 | 03/05/2026 |

---

### Thành tựu đạt được trong Tuần 2:

* Cấu hình thành công AWS Budgets để giám sát chi phí, mức sử dụng và các gói Savings Plans đi kèm cảnh báo chủ động, cho phép kiểm soát chi phí hiệu quả, lập kế hoạch tài chính và tối ưu hóa tài nguyên trên toàn bộ khối lượng công việc AWS.

* Triển khai thành công hệ thống giám sát Amazon CloudWatch bằng cách cấu hình chỉ số (metrics), logs, cảnh báo (alarms) và dashboards để đạt được khả năng quan sát toàn diện (full observability) và nắm bắt thông tin theo thời gian thực về hạ tầng AWS cũng như hiệu năng ứng dụng.

* Triển khai thành công kiến trúc DNS lai (Hybrid DNS) bằng Amazon Route 53 Resolver, cho phép phân giải DNS hai chiều liền mạch giữa hệ thống on-premises và AWS thông qua Inbound/Outbound Endpoints và các quy tắc Resolver Rules: 
  * Cấu hình thành công các quy tắc chuyển tiếp Route 53 Resolver cho tên miền `onprem.example.com`, cho phép định tuyến truy vấn DNS tự động từ AWS về Active Directory on-premises thông qua Outbound Endpoint có tính sẵn sàng cao.
  * Triển khai Route 53 Resolver Inbound Endpoint trên các subnet Multi-AZ, cho phép phân giải truy vấn DNS an toàn từ hệ thống on-premises vào AWS, hoàn thiện kiến trúc Hybrid DNS hai chiều.

* Cấu hình và sử dụng thành công AWS CLI đi kèm xác thực IAM để quản lý tài nguyên AWS một cách hiệu quả qua dòng lệnh, cho phép thực hiện các thao tác cloud an toàn, tự động và có thể viết kịch bản (scriptable).

* Triển khai thành công AWS Backup với các kế hoạch sao lưu tự động, xác minh các thao tác phục hồi dữ liệu và cấu hình thông báo SNS để đảm bảo dữ liệu được bảo vệ tin cậy, tự động và có khả năng khôi phục trên toàn bộ tài nguyên AWS.

* Triển khai thành công cơ chế phân quyền dịch vụ AWS an toàn bằng cách thay thế các khóa truy cập (access keys) lưu cứng bằng IAM Role cho EC2, cho phép truy cập S3 liền mạch thông qua thông tin xác thực tạm thời từ AWS STS và tuân thủ các thực tiễn tốt nhất về bảo mật của AWS.

* Triển khai và cấu hình thành công AWS Cloud9 IDE, thực hiện các thao tác quản lý tệp tin và lệnh Linux, đồng thời sử dụng AWS CLI được cấu hình sẵn để quản lý tài nguyên AWS ngay trên môi trường phát triển dựa trên trình duyệt web.