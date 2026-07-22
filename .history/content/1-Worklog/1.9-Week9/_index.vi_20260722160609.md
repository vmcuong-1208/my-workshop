---
title: "Worklog Tuần 9"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---
### Các nhiệm vụ thực hiện trong tuần này:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành |
| --- | --- | ---------- | --------------- |
| 1 | Hoàn thành Lab40: <br> - Tìm hiểu các khái niệm AWS Glue và Amazon Athena. <br> - Nghiên cứu quy trình làm việc ETL và kiến trúc xử lý dữ liệu. <br> - Hiểu rõ sự tích hợp giữa Amazon S3, Glue Crawler, Glue Data Catalog và Athena. <br> - Khám phá AWS Well-Architected Framework phục vụ tối ưu hóa chi phí. | 15/06/2026 | 15/06/2026 |
| 2 | Tiếp tục với Lab40: <br> - Tạo các Amazon S3 buckets để lưu trữ Báo cáo Chi phí & Sử dụng (Cost & Usage Reports). <br> - Tổ chức các thư mục báo cáo và tải lên tập dữ liệu định dạng Parquet. <br> - Xác minh các tệp đã tải lên và cấu trúc lưu trữ. <br> - Chuẩn bị môi trường cho việc phân tích dữ liệu. | 16/06/2026 | 16/06/2026 |
| 3 | Tiếp tục với Lab40: <br> - Tạo một AWS Glue Crawler. <br> - Cấu hình các IAM roles và nguồn dữ liệu (data sources). <br> - Tạo Glue database và các bảng dữ liệu đặc tả (metadata tables). <br> - Thực thi crawler để quét các tệp Parquet. <br> - Xác minh các bảng Data Catalog được tạo tự động. | 17/06/2026 | 17/06/2026 |
| 4 | Tiếp tục với Lab40: <br> - Cấu hình nơi lưu trữ kết quả truy vấn trong Amazon Athena. <br> - Kết nối Athena với Glue Data Catalog. <br> - Thực thi lệnh MSCK REPAIR TABLE. <br> - Xem trước nội dung các bảng bằng ngôn ngữ SQL. <br> - Thực hành các câu lệnh SQL cơ bản như SELECT, WHERE, GROUP BY, ORDER BY và LIMIT. | 18/06/2026 | 18/06/2026 |
| 5 | Tiếp tục với Lab40: <br> - Truy vấn dữ liệu Báo cáo Chi phí & Sử dụng (Cost & Usage Report). <br> - Phân tích các tài khoản AWS phát sinh chi phí cao nhất. <br> - Nhận diện các dịch vụ AWS đắt đỏ nhất. <br> - So sánh chi phí dịch vụ EC2 và mô tả chi tiết mức độ sử dụng. <br> - Xem xét thông tin hóa đơn AWS bằng SQL. | 19/06/2026 | 19/06/2026 |
| 6 | Tiếp tục với Lab40: <br> - Phân tích các thẻ tài nguyên (resource tags) và phân bổ chi phí. <br> - Truy vấn các tài nguyên đã gắn thẻ và chưa gắn thẻ. <br> - Đánh giá sự phân bổ chi phí giữa các phòng ban. <br> - So sánh mức độ sử dụng tài nguyên đã gắn thẻ. <br> - Thực hành các hàm gom nhóm (aggregation) và sắp xếp (sorting). | 20/06/2026 | 21/06/2026 |
| 7 | Tiếp tục với Lab40: <br> - Phân tích mức sử dụng EC2, Reserved Instances, Savings Plans và mô hình giá On-Demand. <br> - So sánh chi phí theo giờ và mô hình sử dụng. <br> - Nhận diện các Reserved Instances chưa được khai thác. <br> - Xem xét các cơ hội tối ưu hóa chi phí. <br> - Tổng kết toàn bộ bài lab và xác minh kết quả truy vấn. | 21/06/2026 | 21/06/2026 |

---

### Thành tựu đạt được trong Tuần 9:

* Lab40: 
  * Hiểu rõ vai trò của AWS Glue và Athena.
  * Nắm được cơ chế hoạt động của phân tích dữ liệu Serverless trên AWS.
  * Đạt được kiến thức về quy trình ETL và khái niệm Data Catalog.
  * Hiểu tổng quan về kiến trúc phân tích chi phí.
  * Cấu hình thành công bộ lưu trữ Amazon S3.
  * Tải lên các tập dữ liệu Báo cáo Chi phí & Sử dụng.
  * Tổ chức dữ liệu phục vụ xử lý trên AWS Glue.
  * Hoàn thành giai đoạn chuẩn bị bộ lưu trữ dữ liệu.
  * Xây dựng thành công Glue Data Catalog.
  * Khởi tạo tự động các bảng dữ liệu đặc tả (metadata tables).
  * Học được cách Glue Crawler quét và phát hiện các tập dữ liệu.
  * Chuẩn bị cơ sở dữ liệu sẵn sàng cho các truy vấn từ Athena.
  * Truy vấn dữ liệu thành công bằng Amazon Athena.
  * Xác minh tính đồng bộ của các bảng dữ liệu.
  * Nâng cao kỹ năng viết truy vấn SQL.
  * Nắm vững kỹ thuật truy vấn Serverless trên các tập dữ liệu lớn.
  * Nhận diện được các yếu tố chính gây phát sinh chi phí.
  * Xuất các báo cáo chi phí thông qua ngôn ngữ SQL.
  * Học hỏi được các kỹ thuật phân tích chi phí AWS.
  * Cải thiện kỹ năng phân tích bằng cách sử dụng Athena.
  * Nắm vững các chiến lược phân bổ chi phí.
  * Hiểu tầm quan trọng của việc gắn thẻ tài nguyên (resource tagging).
  * Tạo ra các báo cáo chi phí được phân loại rõ ràng.
  * Nâng cao kiến thức quản lý chi phí điện toán đám mây.
  * Đánh giá hiệu quả mức độ sử dụng tài nguyên AWS.
  * Nhận diện các cơ hội tiềm năng để tối ưu hóa chi phí.
  * Hiểu rõ các mô hình giá và báo cáo mức độ sử dụng.
  * Hoàn thành xuất sắc bài lab phân tích chi phí với AWS Glue & Athena.


