---
title: "Truy cập S3 từ môi trường on-premises"
date: 2024-01-01
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

# Thêm chức năng tìm kiếm, phân tích và triển khai frontend

## Trình xử lý tìm kiếm

Tạo một hàm Lambda nhỏ có tên `AI-Learning-Search-Handler` cho endpoint:

```text
GET /search
```

Trình xử lý này đọc `userId` của người dùng đã được xác thực, tìm kiếm các mục nhật ký của người dùng trong DynamoDB và trả về:

```json
{
  "results": [],
  "count": 0
}
```

Trong phạm vi workshop, chỉ cần lọc đơn giản theo tiêu đề, nội dung, thẻ và danh mục là đủ. Với hệ thống tìm kiếm ở quy mô production, nên cân nhắc dùng OpenSearch hoặc một search index chuyên biệt.

Sử dụng đoạn mã sau cho `AI-Learning-Search-Handler`:

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, QueryCommand } from "@aws-sdk/lib-dynamodb";

const JOURNAL_TABLE = process.env.JOURNAL_TABLE || "JournalLogs";
const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

const headers = {
  "Content-Type": "application/json",
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Content-Type,Authorization",
};

export const handler = async (event) => {
  const claims = event.requestContext?.authorizer?.jwt?.claims || {};
  const userId = claims.sub;

  if (!userId) {
    return {
      statusCode: 401,
      headers,
      body: JSON.stringify({ message: "Unauthorized" }),
    };
  }

  try {
    const {
      q = "",
      topic = "",
      tags = "",
      from = "",
      to = "",
    } = event.queryStringParameters || {};

    const result = await docClient.send(
      new QueryCommand({
        TableName: JOURNAL_TABLE,
        KeyConditionExpression: "userId = :uid",
        ExpressionAttributeValues: { ":uid": userId },
      }),
    );

    const query = q.trim().toLowerCase();
    const searchTopic = topic.trim().toLowerCase();
    const searchTags = tags
      .split(",")
      .map((tag) => tag.trim().toLowerCase())
      .filter(Boolean);

    const results = (result.Items || [])
      .filter((item) => {
        const title = String(item.title || "").toLowerCase();
        const content = String(item.content || "").toLowerCase();
        const category = String(item.category || "").toLowerCase();
        const itemTags = (item.tags || []).map((tag) =>
          String(tag).toLowerCase(),
        );

        const matchesQuery =
          !query || title.includes(query) || content.includes(query);
        const matchesTopic =
          !searchTopic ||
          category.includes(searchTopic) ||
          title.includes(searchTopic) ||
          content.includes(searchTopic);
        const matchesTags =
          searchTags.length === 0 ||
          searchTags.some((tag) =>
            itemTags.some((itemTag) => itemTag.includes(tag)),
          );
        const matchesDate =
          (!from || item.date >= from) && (!to || item.date <= to);

        return matchesQuery && matchesTopic && matchesTags && matchesDate;
      })
      .map((item) => ({
        id: item.entryId,
        title: item.title,
        date: item.date,
        category: item.category,
        tags: item.tags || [],
        snippet: String(item.content || "").slice(0, 160),
      }));

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ results, count: results.length }),
    };
  } catch (err) {
    console.error("Lambda Search error:", err);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ message: "Search failed", error: err.message }),
    };
  }
};
```

## Trình xử lý phân tích

Tạo thêm một hàm Lambda khác có tên `AI-Learning-Analytics-Handler` cho endpoint:

```text
GET /analytics/summary
```

Trình xử lý này tổng hợp các bản ghi của người dùng và trả về các chỉ số tóm tắt như tổng số log, các danh mục học tập, tần suất thẻ, tâm trạng, độ khó và thời gian học.

Sử dụng đoạn mã sau cho `AI-Learning-Analytics-Handler`:

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, QueryCommand } from "@aws-sdk/lib-dynamodb";

const JOURNAL_TABLE = process.env.JOURNAL_TABLE || "JournalLogs";
const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

const headers = {
  "Content-Type": "application/json",
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Content-Type,Authorization",
};

function increment(map, key) {
  const safeKey = key || "Unknown";
  map[safeKey] = (map[safeKey] || 0) + 1;
}

function minutesBetween(startTime, endTime) {
  if (!startTime || !endTime) return 0;
  const [sh, sm] = startTime.split(":").map(Number);
  const [eh, em] = endTime.split(":").map(Number);
  if ([sh, sm, eh, em].some(Number.isNaN)) return 0;
  return Math.max(0, eh * 60 + em - (sh * 60 + sm));
}

export const handler = async (event) => {
  const claims = event.requestContext?.authorizer?.jwt?.claims || {};
  const userId = claims.sub;

  if (!userId) {
    return {
      statusCode: 401,
      headers,
      body: JSON.stringify({ message: "Unauthorized" }),
    };
  }

  try {
    const result = await docClient.send(
      new QueryCommand({
        TableName: JOURNAL_TABLE,
        KeyConditionExpression: "userId = :uid",
        ExpressionAttributeValues: { ":uid": userId },
      }),
    );

    const logs = result.Items || [];
    const byCategory = {};
    const byTag = {};
    const byMood = {};
    const byDifficulty = {};
    let totalMinutes = 0;

    for (const log of logs) {
      increment(byCategory, log.category);
      increment(byMood, log.mood);
      increment(byDifficulty, log.difficulty);
      totalMinutes += minutesBetween(log.startTime, log.endTime);

      for (const tag of log.tags || []) {
        increment(byTag, tag);
      }
    }

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        totalLogs: logs.length,
        totalStudyMinutes: totalMinutes,
        byCategory,
        byTag,
        byMood,
        byDifficulty,
        latestLogs: logs
          .sort((a, b) => String(b.date).localeCompare(String(a.date)))
          .slice(0, 5),
      }),
    };
  } catch (err) {
    console.error("Lambda Analytics error:", err);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ message: "Analytics failed", error: err.message }),
    };
  }
};
```

## Cấu hình API Gateway

Trong API Gateway:

1. Tạo `GET /search`.
2. Tạo `GET /analytics/summary`.
3. Gắn từng route với đúng Lambda integration.
4. Gắn Cognito authorizer.
5. Xác minh rằng CORS cho phép frontend origin.

## Triển khai frontend với Amplify

1. Đẩy mã nguồn frontend lên GitHub.
2. Mở **AWS Amplify** và chọn **Amplify Hosting**.
3. Kết nối repository và branch trên GitHub.
4. Thêm các biến môi trường cho frontend, bao gồm API base URL, Cognito user pool ID, app client ID, Hosted UI domain và tên bucket S3.
5. Chọn **Save and deploy**.

Sau khi triển khai, hãy cập nhật các URL callback và sign-out được phép trong Cognito để bao gồm domain của Amplify.

## Thêm lớp bảo vệ ở edge

Bật CloudFront và AWS WAF để bảo vệ frontend công khai. Tối thiểu nên thêm:

- Các managed rule group của AWS.
- Các rule dạng rate-based để giảm lưu lượng lạm dụng.
- Logging hoặc sampled requests để phục vụ việc kiểm tra.

## Ảnh chụp tham khảo

