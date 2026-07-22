---
title: "Blog 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---

---
title: "Blog 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---

# **CloudFront trong Game Backend: Tăng tốc và bảo vệ một số thành phần, nhưng không thay thế những thành phần khác?**

Khi nghĩ đến game online, mình thường nghĩ ngay đến game server, matchmaking, cơ sở dữ liệu hoặc độ trễ giữa người chơi và máy chủ. Tuy nhiên, khi nhìn kỹ hơn, một hệ thống game hiện nay còn có rất nhiều loại request không trực tiếp xử lý gameplay như: đăng nhập, tải bản cập nhật (patch), tải asset, hồ sơ người chơi, kho đồ, bảng xếp hạng, cửa hàng, tính năng mạng xã hội, API cho launcher hoặc website.

Ban đầu mình từng nghĩ Amazon CloudFront có thể được xem như một lớp tăng tốc cho toàn bộ game backend. Nhưng sau khi tách các luồng lưu lượng theo giao thức và mục đích sử dụng, mình nhận ra cách hiểu chính xác hơn là:

**CloudFront phù hợp để tăng tốc và bảo vệ các lưu lượng web-facing của game backend; nó không thay thế hạ tầng xử lý gameplay thời gian thực.**

Bài viết này là phần tổng hợp những gì mình tìm hiểu về kiến trúc AWS, cách CloudFront hỗ trợ game backend, những phần nó làm rất tốt và những phần vẫn cần được thiết kế theo hướng khác.

---

## **1. Game backend không chỉ có game server**

Một hệ thống game online thông thường sẽ có ít nhất hai nhóm lưu lượng khác nhau.

**Nhóm 1: Web-facing traffic**

Đây là các request thường sử dụng HTTP/HTTPS hoặc WebSocket, ví dụ:

- Đăng nhập và xác thực người chơi.
- Tải launcher, bản vá (patch), texture, âm thanh, mô hình 3D.
- API hồ sơ người chơi, kho đồ, thành tích.
- Leaderboard.
- Shop, thanh toán, sự kiện trong game.
- Website hoặc trang quản trị game.
- Một số tính năng chat, thông báo hoặc mạng xã hội sử dụng WebSocket.

Đây là nhóm lưu lượng rất phù hợp để đặt CloudFront ở phía trước.

---

## **2. CloudFront đứng ở đâu trong kiến trúc Game Backend?**

Ở mức đơn giản nhất, luồng request có thể hình dung như sau:

**Player Client → CloudFront Edge Location → CloudFront → Origin/Backend**

CloudFront có nhiều Edge Location đặt gần người dùng. Khi người chơi gửi HTTP/HTTPS request tới game backend, request sẽ được chuyển đến Edge Location gần nhất thay vì luôn kết nối trực tiếp tới Region chứa backend.

CloudFront có thể sử dụng nhiều Origin khác nhau như:

- Amazon S3: lưu patch, launcher, hình ảnh, âm thanh, video và các static asset.
- Amazon API Gateway: các Serverless API như login, profile, inventory.
- Application Load Balancer (ALB): điều phối request tới backend chạy trên EC2, ECS hoặc EKS.
- Amazon EC2, Amazon ECS, Amazon EKS: vận hành các backend service.
- AWS Lambda: xử lý một số API hoặc business logic theo mô hình event-driven.

CloudFront không thay thế backend xử lý request mà đóng vai trò là lớp phía trước, giúp phân phối nội dung, cache khi phù hợp, định tuyến request và bổ sung các lớp bảo vệ.

---

## **3. CloudFront hỗ trợ Game Backend như thế nào?**

### Tăng tốc việc tải patch và game asset

Đây là use case dễ hình dung nhất.

Một trò chơi có thể có các bản cập nhật dung lượng nhiều GB, bao gồm texture, model, animation, âm thanh, video hoặc file cấu hình. Nếu toàn bộ người chơi tải trực tiếp từ một Region duy nhất thì backend và đường truyền gốc sẽ chịu tải rất lớn, đặc biệt khi phát hành bản cập nhật mới.

Khi sử dụng CloudFront với Amazon S3 làm Origin:

- File được phân phối từ Edge Location gần người chơi.
- Các file phổ biến được cache tại Edge.
- Giảm số lượng request phải quay về Origin.
- Backend không cần trực tiếp xử lý các request tải file tĩnh.
- Trải nghiệm tải patch ổn định hơn khi số lượng người chơi tăng.

Ví dụ, khi phát hành một bản cập nhật mới vào cuối tuần, thay vì hàng nghìn người chơi cùng tải từ một S3 Bucket hoặc server duy nhất, CloudFront sẽ phục vụ phần lớn các request này từ Edge Cache sau khi nội dung đã được cache.

---

## **4. CloudFront Functions và Lambda@Edge dùng để làm gì?**

Trong kiến trúc AWS có hai thành phần khá dễ nhầm lẫn là **CloudFront Functions** và **Lambda@Edge**.

Cả hai đều cho phép chạy logic ngay tại Edge trước khi request đi vào Origin, nhưng phù hợp với các mức xử lý khác nhau.

### CloudFront Functions

CloudFront Functions phù hợp với các xử lý nhẹ và có thời gian thực thi rất nhanh, chẳng hạn:

- Rewrite URL.
- Redirect người dùng.
- Thêm hoặc chỉnh sửa Header.
- Kiểm tra request cơ bản.
- Route request theo đường dẫn.
- Thực hiện các logic đơn giản dựa trên quốc gia hoặc thiết bị.

### Lambda@Edge

Lambda@Edge phù hợp khi cần xử lý linh hoạt hơn CloudFront Functions nhưng vẫn nên được xem là lớp xử lý tại Edge thay vì nơi đặt business logic lớn.

Ví dụ:

- Điều chỉnh request hoặc response phức tạp hơn.
- Chọn Origin theo điều kiện.
- Xử lý Authorization tại Edge trong một số trường hợp.
- Sinh response dựa trên request.

Đối với game backend, các nghiệp vụ liên quan đến tài khoản, kho đồ, giao dịch hoặc trạng thái trận đấu vẫn nên nằm tại backend chính. Các Edge Function chỉ nên đảm nhiệm các công việc giúp tối ưu định tuyến và xử lý request.

---

## **5. CloudFront có thay thế thành phần nào của hệ thống không?**

Đây là phần mình thấy cần làm rõ nhất.

CloudFront không phải là Game Server, không thay thế Amazon GameLift Servers và cũng không giải quyết toàn bộ vấn đề về độ trễ trong game thời gian thực.

CloudFront **không trực tiếp xử lý**:

- Gameplay sử dụng giao thức UDP.
- Game Loop.
- Trạng thái Authoritative của trận đấu.
- Logic Matchmaking.
- Physics hoặc Combat Validation.
- Đồng bộ trạng thái liên tục giữa người chơi và Game Server.
- Dedicated Server Session.

Ví dụ, trong một game FPS, người chơi liên tục gửi input và nhận trạng thái trận đấu theo thời gian thực. Phần này phải được xử lý bởi Game Server chuyên dụng.

CloudFront vẫn có thể xử lý các API phụ trợ như:

- Login.
- Profile.
- Patch.
- Shop.
- Leaderboard.

Nhưng không phải là tuyến mặc định dành cho gameplay packet.

Có thể hiểu đơn giản:

- **CloudFront:** lớp phân phối và bảo vệ cho phần web của game.
- **API/Backend Services:** xử lý nghiệp vụ như tài khoản, kho đồ, leaderboard, thanh toán.
- **Game Server/GameLift Servers:** xử lý trận đấu và gameplay thời gian thực.

---

## **6. Kiến trúc tối giản cho Game Backend**

Nếu chỉ xây dựng một game nhỏ hoặc một prototype multiplayer, bạn không nhất thiết phải sử dụng toàn bộ các dịch vụ trong kiến trúc AWS.

Một mô hình đơn giản có thể gồm:

- Amazon S3 lưu patch, asset và file cấu hình.
- CloudFront phân phối asset từ S3.
- API Gateway + Lambda hoặc ALB + Backend Service xử lý login, profile và leaderboard.
- Amazon DynamoDB hoặc cơ sở dữ liệu phù hợp để lưu thông tin người chơi.
- Game Server chạy riêng trên EC2, Container hoặc Amazon GameLift Servers nếu game có multiplayer.
- AWS WAF tích hợp với CloudFront hoặc API nhằm bảo vệ các Public Endpoint.

Khi số lượng người chơi tăng lên, kiến trúc có thể mở rộng dần. Điều quan trọng là cần phân biệt rõ:

- Request nào là nội dung tĩnh.
- Request nào là API.
- Request nào là gameplay thời gian thực.

---

## **7. Checklist trước khi tích hợp CloudFront vào Game Backend**

Trước khi bổ sung CloudFront, mình nghĩ nên kiểm tra các câu hỏi sau:

- Lưu lượng này sử dụng HTTP/HTTPS, WebSocket hay UDP/TCP?
- Nội dung có thể cache được không?
- Response có chứa dữ liệu cá nhân hoặc dữ liệu nhạy cảm không?
- Origin là Amazon S3, API Gateway, ALB hay Backend tự triển khai?
- Có cần sử dụng AWS WAF để Rate Limit hoặc chặn request bất thường không?
- Có cần duy trì kết nối WebSocket trong thời gian dài không?
- Có cần Signed URL hoặc Signed Cookie để bảo vệ Patch và Asset không?
- Khi xảy ra lỗi thì Log và hệ thống Monitoring sẽ được theo dõi ở đâu?
- Chi phí Data Transfer và Request có phù hợp với quy mô hiện tại không?

Checklist này giúp tránh việc sử dụng CloudFront chỉ vì đây là dịch vụ CDN của AWS, trong khi workload thực tế có thể không phù hợp.

---

## **8. Kết luận**

CloudFront là một thành phần rất hữu ích trong Game Backend, nhưng giá trị của nó nằm ở việc sử dụng đúng mục đích.

CloudFront phù hợp để:

- Phân phối patch và asset.
- Tăng tốc các HTTP/HTTPS API khi phù hợp.
- Cache nội dung công khai hoặc dữ liệu đọc nhiều.
- Hỗ trợ WebSocket cho một số tính năng chat hoặc mạng xã hội.
- Kết hợp với AWS WAF và AWS Shield để bảo vệ lớp Public Request.
- Giảm tải cho Origin và Backend.

Tuy nhiên, CloudFront không thay thế Game Server, không xử lý Game Loop và cũng không phải giải pháp cho toàn bộ gameplay thời gian thực.

Điều mình học được sau khi tìm hiểu kiến trúc này là: thay vì hỏi **"Game có cần CloudFront không?"**, nên đặt câu hỏi cụ thể hơn:

**Phần nào của Game Backend là Web-facing Traffic, phần nào cần Cache và bảo vệ tại Edge, phần nào cần đi trực tiếp đến hạ tầng xử lý thời gian thực?**

Khi tách rõ các luồng này, việc lựa chọn giữa CloudFront, API Gateway, ALB, GameLift hay Dedicated Game Server sẽ trở nên rõ ràng hơn rất nhiều.

Nguồn tham khảo:

- https://aws.amazon.com/vi/blogs/gametech/building-resilient-and-secure-game-backends-with-amazon-cloudfront/

</div>