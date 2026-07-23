---
title : "Chính sách endpoint của VPC"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.5 </b> "
---

# Hạn chế truy cập S3 bằng endpoint policy

Khi bạn tạo gateway endpoint hoặc interface endpoint cho Amazon S3, bạn có thể gắn một endpoint policy để giới hạn bucket hoặc hành động nào được phép đi qua đường truyền riêng tư đó. Đây là mẫu thiết kế hữu ích khi bạn muốn giữ quyền truy cập hẹp và tránh rò rỉ dữ liệu.

## Vì sao điều này quan trọng

Một endpoint policy mặc định thường cho phép truy cập khá rộng. Bằng cách dùng policy tùy chỉnh, bạn có thể đảm bảo chỉ bucket mong muốn mới có thể truy cập qua endpoint, còn các bucket khác vẫn được bảo vệ.

## Bạn sẽ làm gì

1. Tạo hoặc tái sử dụng một bucket S3 thứ hai cho mục đích kiểm tra.
2. Cập nhật endpoint policy của VPC để chỉ cho phép bucket đó.
3. Xác minh rằng việc truy cập vào bucket được phép thành công, còn bucket ban đầu bị từ chối.

Bài lab bonus này cho thấy cách biến một đường truyền riêng tư thông thường thành một mẫu truy cập theo nguyên tắc least privilege.
