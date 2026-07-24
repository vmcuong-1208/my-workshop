---
title: "Blog 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---

# **Vì sao và cách migrate sang AWS Network Firewall gắn trực tiếp với Transit Gateway (TGW-attached)**

Nếu bạn đang vận hành hạ tầng AWS theo mô hình nhiều VPC (Spoke VPC) và sử dụng AWS Transit Gateway (TGW) để định tuyến tập trung, thì rất có thể bạn đã (hoặc sắp) gặp bài toán: làm thế nào để kiểm tra (inspect) lưu lượng mạng tập trung mà không cần phải xây dựng một **Inspection VPC** khá phức tạp?

Hiện nay, **AWS Network Firewall** đã hỗ trợ gắn trực tiếp (native attachment) với **Transit Gateway**. Nói đơn giản, firewall có thể được gắn trực tiếp vào TGW dưới dạng một **Network Function Attachment**, giúp loại bỏ Inspection VPC trong nhiều kiến trúc truyền thống.

Trong bài viết này, mình sẽ tóm tắt và phân tích:

- TGW-attached Network Firewall là gì?
- Vì sao nên migrate?
- Cần chuẩn bị những gì?
- Quá trình migrate diễn ra như thế nào (2 kiến trúc phổ biến)?
- Các best practices giúp giảm downtime và tránh sự cố routing.

---

## **1. Kiến trúc cũ: Centralized Inspection VPC (đúng nhưng... khá nặng)**

Trước đây, nếu muốn kiểm tra lưu lượng tập trung (đặc biệt là lưu lượng đi Internet), mô hình phổ biến thường là:

- Tạo một **Inspection VPC**.
- Tạo các Firewall Subnet và triển khai các **Network Firewall Endpoint** tại đó.
- Sử dụng định tuyến của Transit Gateway để chuyển lưu lượng từ các Spoke VPC đi qua Inspection VPC trước khi đến đích.

Mô hình này hoạt động tốt nhưng tồn tại nhiều hạn chế:

- Phải quản lý nhiều Route Table, Subnet và VPC.
- Khó mở rộng trong môi trường Multi-AZ.
- Khó phân bổ (chargeback) chi phí AWS Network Firewall cho từng tài khoản hoặc từng nhóm.

---

## **2. Transit Gateway-attached Network Firewall là gì?**

Với cơ chế **Native Attachment**, bạn không còn phải tạo Inspection VPC nữa.

Thay vào đó:

- Tạo một **AWS Network Firewall**.
- Chỉ định **Transit Gateway ID** cần gắn.

AWS sẽ tự động triển khai các Firewall Endpoint trong một **AWS-managed VPC** (bạn không sở hữu và cũng không cần quản lý VPC này).

Từ góc nhìn của người dùng, Firewall sẽ xuất hiện như:

- Một **Transit Gateway Network Function Attachment**.
- Có thể định tuyến lưu lượng đến Firewall giống như các TGW Attachment khác.

Lợi ích lớn nhất là giảm bớt một tầng kiến trúc và giảm đáng kể khối lượng vận hành.

---

## **3. Vì sao nên migrate? (2 lợi ích nổi bật)**

AWS đưa ra hai lý do đáng chú ý nhất.

### **(1) Phân bổ chi phí linh hoạt hơn (Flexible Cost Allocation)**

Khi sử dụng Native Attachment, bạn có thể áp dụng **Transit Gateway Metering Policies** để phân bổ chi phí dựa trên lưu lượng thực tế đi qua Firewall.

Điểm quan trọng là:

- Trước đây chỉ có thể phân bổ chi phí xử lý dữ liệu của TGW.
- Chi phí của AWS Network Firewall khó phân bổ chi tiết.
- Native Attachment giúp thực hiện chargeback theo đúng nguyên tắc **"ai sử dụng thì người đó trả"**.

### **(2) Giảm độ phức tạp của kiến trúc**

- Loại bỏ Inspection VPC.
- Giảm số lượng Route Table và Subnet cần quản lý.
- Tập trung quản trị bảo mật mạng nhưng với kiến trúc đơn giản hơn.

---

## **4. Chuẩn bị trước khi migrate: Checklist ngắn**

Trước khi triển khai trên môi trường Production, AWS khuyến nghị chuẩn bị:

### Điều kiện cần

- Transit Gateway ID sẽ được Firewall gắn vào.
- Cấu hình Logging mới (CloudWatch Log Group mới để tách log cũ và log mới trong quá trình chạy song song).
- Firewall Policy mới (không nên tái sử dụng ngay policy cũ nhằm tránh ảnh hưởng hệ thống đang hoạt động).

### Những điểm cần lưu ý

- **Transit Gateway Encryption:** nếu hệ thống bắt buộc sử dụng tính năng này thì Native Attachment hiện chưa hỗ trợ, vì vậy cần tiếp tục sử dụng kiến trúc cũ.
- **Elastic IP của NAT Gateway:** nếu cần giữ nguyên Public IP (ví dụ đối tác đã whitelist), cần lập kế hoạch bảo toàn EIP.
- **Maintenance Window:** một số bước như thay đổi Route Table Association hoặc thay NAT Gateway sẽ gây gián đoạn ngắn, vì vậy cần lên lịch bảo trì phù hợp.

---

## **5. Chiến lược migrate đúng cách: Chạy song song, kiểm thử trước, chuyển đổi theo từng giai đoạn**

AWS khuyến nghị quy trình sau:

- Không thay đổi Firewall cũ ngay từ đầu.
- Triển khai Firewall mới chạy song song.
- Thử nghiệm trước với một Spoke VPC.
- Sau khi xác nhận ổn định mới chuyển dần hoặc thực hiện cutover toàn bộ.

Cách tiếp cận này giúp dễ rollback và giảm rủi ro khi triển khai.

---

## **6. Hai kiến trúc migrate phổ biến**

### **Kiến trúc 1: Inspection VPC và Egress VPC tách biệt**

Bao gồm:

- Inspection VPC chứa Firewall Endpoint.
- Egress VPC chứa NAT Gateway.

Các bước tổng quan:

1. Triển khai Egress VPC mới với NAT Gateway tạm thời.
2. Tạo AWS Network Firewall mới và gắn trực tiếp vào TGW.
3. Tạo ba Transit Gateway Route Table mới:

- Inspection Route Table (gắn với Firewall Attachment).
- Egress Route Table (gắn với Egress VPC mới).
- Migrated Spoke Route Table (dùng để kiểm thử từng Spoke).

4. Chuyển một Spoke VPC sang đường mới để kiểm thử.
5. Di chuyển các Spoke còn lại theo từng giai đoạn hoặc chuyển toàn bộ.
6. (Tùy chọn) Giữ nguyên NAT Gateway EIP bằng cách định tuyến lại về Egress VPC cũ.
7. Xóa các tài nguyên cũ sau khi hệ thống hoạt động ổn định.

Ưu điểm của kiến trúc này là việc giữ nguyên Elastic IP khá đơn giản vì Egress VPC cũ hoạt động độc lập.

---

### **Kiến trúc 2: Inspection và Egress dùng chung một VPC**

Một VPC sẽ chứa:

- Firewall Endpoint.
- NAT Gateway.

Các bước migrate gần tương tự Kiến trúc 1, tuy nhiên việc giữ nguyên Elastic IP sẽ khó khăn hơn.

Thông thường cần:

- Xóa NAT Gateway cũ để giải phóng Elastic IP.
- Tạo NAT Gateway mới tại Egress VPC mới.
- Gắn lại Elastic IP cũ.

Quá trình này thường yêu cầu Maintenance Window cho từng Availability Zone do việc khởi tạo NAT Gateway cần thời gian.

---

## **7. Một mẹo kiểm tra rất quan trọng: Phát hiện Asymmetric Routing**

AWS khuyến nghị sử dụng Log để kiểm tra.

Khi chuyển một Spoke VPC sang đường mới:

- Nếu Firewall Alert Log hiển thị đầy đủ thông tin Layer 7 (Application Layer), điều đó chứng tỏ Firewall quan sát được lưu lượng ở cả hai chiều → Routing đối xứng (Symmetric Routing).
- Nếu chỉ quan sát được một chiều thì rất có thể hệ thống đang gặp **Asymmetric Routing**, khiến Stateful Inspection hoạt động không chính xác và có thể làm rớt lưu lượng.

Đây là một tín hiệu rất hữu ích trước khi thực hiện cutover trên diện rộng.

---

## **8. Best Practices giúp giảm downtime và tránh sự cố East-West Traffic**

AWS nhấn mạnh ba khuyến nghị quan trọng:

### **1. Thử nghiệm trên môi trường Dev/Test trước**

Repository hướng dẫn Migration có sẵn các mẫu Terraform và CloudFormation để xây dựng môi trường thử nghiệm gần giống Production.

### **2. Migrate theo từng giai đoạn**

- Bắt đầu với các Spoke không quan trọng.
- Theo dõi sát cùng với chủ sở hữu ứng dụng.

### **3. Chú ý lưu lượng East-West giữa các Spoke**

Nếu hai Spoke đang đi qua hai Stateful Firewall khác nhau trong giai đoạn chuyển đổi:

- Lưu lượng East-West có thể đi qua hai Firewall khác nhau.
- Return Traffic có thể bị xem là **Untracked** và bị Firewall chặn.

Vì vậy nên migrate các Spoke có lưu lượng East-West cùng một thời điểm nếu có thể.

Ngoài ra luôn cần:

- Sao lưu cấu hình Routing hiện tại trước khi thay đổi.
- Giữ Firewall cũ hoạt động cho đến khi xác nhận hệ thống ổn định.
- Chuẩn bị sẵn kế hoạch Rollback.

---

## **Kết luận**

Transit Gateway-attached AWS Network Firewall là một bước tiến giúp:

- Đơn giản hóa kiến trúc.
- Dễ quản trị hơn.
- Phân bổ chi phí rõ ràng hơn.
- AWS tự quản lý Firewall Endpoint và Managed VPC.

Điều quan trọng là cần thực hiện migration đúng quy trình: triển khai song song, kiểm thử kỹ lưỡng, chuyển đổi theo từng giai đoạn và đặc biệt chú ý đến **Asymmetric Routing** cũng như **East-West Traffic** để hạn chế rủi ro.

Nguồn tham khảo:

- https://aws.amazon.com/vi/blogs/security/why-and-how-to-migrate-to-a-transit-gateway-attached-aws-network-firewall/
