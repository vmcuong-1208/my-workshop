---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# **Amazon công bố công cụ tìm kiếm web trên Bedrock AgentCore dành cho truy xuất web theo hướng tác tử**

Amazon công bố công cụ tìm kiếm web trên Bedrock AgentCore dành cho truy xuất web theo hướng tác tử.

Ngày 16/06/2026, AWS công bố Web Search trên Amazon Bedrock AgentCore – một công cụ tìm kiếm web được quản lý hoàn toàn (fully managed), được thiết kế riêng cho AI Agent, giúp các tác tử có thể truy xuất kiến thức mới nhất từ web, cung cấp câu trả lời có trích dẫn nguồn và đảm bảo dữ liệu không bị đưa ra ngoài môi trường AWS của khách hàng (zero data egress). Đây là một tính năng rất đáng chú ý nếu bạn đang xây dựng các AI Agent theo hướng production: cần cập nhật thông tin mới, có dẫn chứng rõ ràng và đáp ứng các yêu cầu về bảo mật cũng như tuân thủ trong doanh nghiệp.

Trong bài viết này, tôi sẽ phân tích những nội dung chính của tài liệu và tổng hợp lại theo góc nhìn của một người học để chia sẻ cùng cộng đồng.

## **1) Vấn đề cũ của AI Agent: "biết" nhưng không "cập nhật"**

LLM càng mạnh thì kỳ vọng của người dùng càng cao: câu trả lời phải chính xác, cập nhật và có căn cứ. Tuy nhiên, các mô hình chỉ được huấn luyện trên dữ liệu trong quá khứ. Khi gặp những câu hỏi như:

- "Tuần này AWS vừa ra mắt những tính năng nào liên quan đến AgentCore?"
- "Chi phí của Web Search được tính như thế nào?"
- "Thông tin nào là chính thức và có nguồn đáng tin cậy?"

...thì AI Agent buộc phải truy cập ra bên ngoài mô hình để tìm kiếm thông tin trên Internet. Đây cũng là lúc các nhóm phát triển thường gặp ba vấn đề lớn:

- Tích hợp các nhà cung cấp dịch vụ tìm kiếm bên ngoài (API khác nhau, cơ chế xác thực khác nhau).
- Tự xây dựng quy trình điều phối việc gọi công cụ, xử lý retry, rate limit, xếp hạng kết quả, phân tích snippet,...
- Bảo mật và tuân thủ: dữ liệu truy vấn và thông tin có thể bị gửi ra ngoài hạ tầng do doanh nghiệp quản lý.

AWS định vị Web Search trên AgentCore như một giải pháp giúp loại bỏ các thành phần phức tạp nhưng không tạo ra giá trị khác biệt, để nhà phát triển có thể tập trung xây dựng logic của AI Agent.

## **2) Web Search trên AgentCore là gì?**

Web Search là một công cụ được AWS quản lý hoàn toàn, cho phép AI Agent:

- Gửi truy vấn bằng ngôn ngữ tự nhiên.

- Nhận về kết quả đã được xếp hạng bao gồm:
  - Đoạn trích (snippet) ngắn và liên quan.
  - Đường dẫn nguồn (URL).
  - Tiêu đề.
  - Ngày xuất bản.

Từ đó, mô hình ngôn ngữ có thể suy luận và tạo ra câu trả lời có căn cứ (grounded answer).

Điểm nổi bật nhất là AWS nhấn mạnh cơ chế **zero data egress**, tức dữ liệu vẫn được giữ trong môi trường AWS an toàn của khách hàng thay vì phải gửi truy vấn sang các công cụ tìm kiếm của bên thứ ba.

## **3) "Khác gì so với công cụ tìm kiếm thông thường?": Multi-source Grounding + Knowledge Graph**

Thay vì chỉ trả về danh sách các liên kết như công cụ tìm kiếm truyền thống, Web Search được xây dựng dựa trên:

- Amazon's Web Index.
- Kết hợp với dữ liệu Knowledge Graph có cấu trúc.

Nói cách khác, ngoài các liên kết và đoạn trích, AI Agent còn có thể khai thác dữ liệu về thực thể (entity data) cũng như các thông tin đã được xác minh từ Amazon Knowledge Graph. Điều này mang lại các lợi ích:

- Kết quả tìm kiếm liên quan hơn.
- Câu trả lời chính xác hơn.
- Giảm nguy cơ sử dụng các nguồn thông tin không đáng tin cậy dẫn đến kết luận sai.

Đối với các quy trình Agentic Workflow, việc sử dụng đúng nguồn thông tin và đảm bảo tính chính xác quan trọng hơn nhiều so với việc chỉ tìm được một liên kết.

## **4) Tối ưu cho AI Agent: "High-value Snippets" giúp tiết kiệm Token**

Một điểm khá thú vị là Web Search được tối ưu để trả về các đoạn trích có giá trị thông tin cao, giúp cung cấp nhiều thông tin hữu ích hơn trên mỗi token.

Những ai từng xây dựng AI Agent đều hiểu rằng:

**Token = Chi phí + Độ trễ (Latency).**

Nếu công cụ trả về quá nhiều nội dung, Agent sẽ tốn nhiều context và xử lý chậm hơn. Theo AWS, Web Search sẽ đóng gói thông tin dưới dạng snippet nhằm:

- Giúp mô hình đọc nhanh hơn.
- Suy luận nhanh hơn.
- Vẫn cung cấp URL để kiểm chứng hoặc trích dẫn nguồn.

## **5) Tích hợp thông qua MCP và AgentCore Gateway: đúng nghĩa một "Agent Platform"**

Web Search được cung cấp như một Connector tích hợp sẵn trong Bedrock AgentCore Gateway thông qua giao thức **Model Context Protocol (MCP)**.

Luồng hoạt động có thể hình dung như sau:

1. Tạo AgentCore Gateway.

2. Lựa chọn:
   - Target protocol: MCP.
   - Target type: Connectors.
   - Tool: Web Search (được cấu hình sẵn).

3. AI Agent gửi truy vấn bằng ngôn ngữ tự nhiên.

4. Công cụ trả về kết quả đã xếp hạng cùng snippet và metadata.

5. AI Agent tổng hợp thành câu trả lời có căn cứ.

AWS cũng cho biết người dùng có thể kiểm thử và gỡ lỗi thông qua **MCP Inspector**, một công cụ tương tác hỗ trợ chạy thử các tool rất thuận tiện cho nhà phát triển.

## **6) Web Search nằm ở đâu trong hệ sinh thái AgentCore?**

Tài liệu cũng mô tả AgentCore là một nền tảng Fully Managed dành cho AI Agent với nhiều thành phần quan trọng:

- Harness: Quản lý vòng đời Agent (Memory, Tool, môi trường cô lập).
- Runtime: Môi trường chạy Agent và MCP Server an toàn.
- Memory: Bộ nhớ ngắn hạn và dài hạn.
- Gateway: Kết nối các công cụ như API, Lambda, MCP,...
- Identity: Quản lý danh tính và phân quyền.
- Browser: Trình duyệt Cloud phục vụ tự động hóa.
- Code Interpreter: Thực thi mã trong môi trường Sandbox.
- Observability: Theo dõi, Debug và Monitoring.

Trong toàn bộ hệ sinh thái này, Web Search đóng vai trò là một công cụ (tool-native capability) được tích hợp trực tiếp vào nền tảng AgentCore thay vì phải tích hợp từ các dịch vụ bên ngoài.

## **7) Khía cạnh doanh nghiệp: Governance và Compliance**

AWS tập trung giải quyết những yêu cầu quan trọng trong môi trường doanh nghiệp:

- Không gửi Prompt và Retrieval Query đến các nhà cung cấp công cụ tìm kiếm bên thứ ba.
- Vẫn đáp ứng các chính sách quản trị (Governance Policies).
- Dễ dàng quản lý trong môi trường AWS.

Đối với các doanh nghiệp có yêu cầu cao về tuân thủ, đây là điểm khác biệt lớn giữa một bản Demo và một hệ thống có thể triển khai thực tế trong môi trường Production.

## **8) Khách hàng nói gì? (Customer Voices)**

Bài viết gốc cũng chia sẻ một số phản hồi từ các khách hàng tham gia chương trình Early Access, ví dụ:

- **Benchling:** Các nhà khoa học có thể đặt câu hỏi liên quan đến mục tiêu nghiên cứu và nhận được câu trả lời kết hợp giữa dữ liệu nội bộ và các tài liệu nghiên cứu đã công bố trong một môi trường an toàn.

- **Gen Digital (Norton):** Sử dụng Web Search để xây dựng các ý tưởng nội dung dựa trên những thông tin đang diễn ra ngoài thực tế và đánh giá cao việc toàn bộ truy vấn đều được thực hiện trong môi trường AWS.

Qua các ví dụ này có thể thấy AWS đang hướng đến những trường hợp sử dụng rất thực tế, nơi AI Agent cần vừa có dữ liệu cập nhật vừa đảm bảo yêu cầu về quản trị và bảo mật.

## **9) Availability & Pricing: Thông tin quan trọng cho người muốn trải nghiệm**

- Region hỗ trợ: **US East (N. Virginia)**.
- Giá dịch vụ: **7 USD / 1.000 truy vấn**.
- AWS cũng đề cập đến chương trình **Free Tier Credits** lên đến **200 USD** dành cho khách hàng mới (áp dụng theo điều kiện của AWS).

Việc tính phí theo số lượng truy vấn giúp người phát triển dễ dàng dự toán chi phí khi thiết kế AI Agent và kiểm soát thời điểm cần thực hiện tìm kiếm.

## **10) Góc nhìn cá nhân: Ai nên quan tâm đến tính năng này?**

Nếu bạn thuộc một trong các nhóm dưới đây thì Web Search trên AgentCore là một tính năng rất đáng để tìm hiểu:

1. Xây dựng AI Agent hỏi đáp về các sự kiện mới (tin tức, cập nhật sản phẩm, chính sách,...).

2. AI Agent cần đưa ra câu trả lời có dẫn chứng (Support, Compliance, Research Assistant).

3. Doanh nghiệp yêu cầu cao về bảo mật và không muốn gửi Prompt ra ngoài AWS.

4. Nhà phát triển muốn tiết kiệm thời gian tích hợp các thành phần như Search, Authentication và Orchestration.

## **Kết luận**

Có thể thấy AWS đang từng bước xây dựng AgentCore trở thành nền tảng dành cho AI Agent theo hướng Production: không chỉ vận hành ổn định mà còn đảm bảo khả năng quan sát hệ thống, tích hợp công cụ theo tiêu chuẩn, đồng thời bổ sung Web Search để AI Agent có thể truy xuất thông tin mới nhất trên Internet kèm theo nguồn trích dẫn mà vẫn đảm bảo dữ liệu được giữ an toàn trong môi trường AWS.

**Tài liệu tham khảo chính thức:**

- Docs: https://docs.aws.amazon.com/bedrock-agentcore/
- Product page: https://aws.amazon.com/bedrock/agentcore/
- AWS News Blog:
  - https://aws.amazon.com/vi/blogs/aws/announcing-web-search-on-amazon-bedrock-agentcore-ground-your-ai-agents-in-current-accurate-web-knowledge/
  - https://aws.amazon.com/en/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-web-search/?fbclid=IwY2xjawS43ehleHRuA2FlbQIxMABicmlkETFpV1plODlJYWQxeU5qYkI2c3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHvTonm5uiEKwfq428klu0yXiHSOJdWy_LWCmFicAAiK5b4kLXXHJNa6ruY5f_aem_wFzKISfwQBP3lmnsKF4flg

**Link bài đăng trên nhóm:**

https://www.facebook.com/groups/awsstudygroupfcj/posts/2203816677049959

</div>