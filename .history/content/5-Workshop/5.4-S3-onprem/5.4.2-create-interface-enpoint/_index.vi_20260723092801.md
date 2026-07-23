---
title : "Tạo một S3 Interface endpoint"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.4.2 </b> "
---

Trong phần này, bạn sẽ tạo và cấu hình Lambda worker để xử lý các tác vụ AI từ SQS.

## Tạo hàm worker

1. Mở **AWS Lambda** và chọn **Create function**.
2. Tên hàm: `AI-Personal-Learning-Worker`.
3. Runtime: Node.js 22.x.
4. Chọn execution role có quyền truy cập DynamoDB, SQS và CloudWatch.
5. Tạo hàm.

## Cấu hình timeout và concurrency

Các lệnh gọi AI có thể mất nhiều thời gian hơn mức timeout mặc định của Lambda. Hãy cấu hình:

- Timeout: 30 giây hoặc nhiều hơn
- Reserved concurrency: một giá trị nhỏ như 2–5 trong thời gian workshop

Reserved concurrency giúp ngăn việc sử dụng AI song song quá mức ngoài ý muốn và giữ cho chi phí dễ dự đoán hơn.

## Lưu trữ an toàn Groq API key

Trong **Configuration** > **Environment variables**, thêm:

- `GROQ_API_KEY=<groq-api-key-của-bạn>`
- `GROQ_MODEL=llama-3.1-8b-instant`

Trong mã nguồn, đọc khóa từ `process.env.GROQ_API_KEY`. Tránh đưa khóa này lên GitHub hoặc dán nó vào báo cáo workshop.

## Mã nguồn worker

Sử dụng toàn bộ đoạn mã sau cho tệp `index.mjs`:

````js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
  DynamoDBDocumentClient,
  QueryCommand,
  UpdateCommand,
} from "@aws-sdk/lib-dynamodb";

const REGION = process.env.AWS_REGION || "ap-southeast-1";
const JOURNAL_TABLE = process.env.JOURNAL_TABLE || "JournalLogs";
const AI_REPORT_TABLE = process.env.AI_REPORT_TABLE || "AiReports";
const QUIZ_TABLE = process.env.QUIZ_TABLE || "Quizzes";
const GROQ_API_KEY = process.env.GROQ_API_KEY;
const GROQ_MODEL = process.env.GROQ_MODEL || "llama-3.1-8b-instant";

const docClient = DynamoDBDocumentClient.from(
  new DynamoDBClient({ region: REGION }),
);

async function callGroqAI(prompt) {
  if (!GROQ_API_KEY) {
    throw new Error("Missing GROQ_API_KEY environment variable");
  }

  const response = await fetch(
    "https://api.groq.com/openai/v1/chat/completions",
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${GROQ_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: GROQ_MODEL,
        messages: [
          {
            role: "system",
            content:
              "You are a learning assistant. Return valid JSON only. Do not wrap JSON in markdown fences.",
          },
          { role: "user", content: prompt },
        ],
        temperature: 0.3,
      }),
    },
  );

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Groq API Error ${response.status}: ${errorText}`);
  }

  const data = await response.json();
  return data.choices?.?.message?.content || "{}";
}

async function getUserLogs(userId, startDate, endDate, tags = []) {
  const result = await docClient.send(
    new QueryCommand({
      TableName: JOURNAL_TABLE,
      KeyConditionExpression: "userId = :uid",
      ExpressionAttributeValues: { ":uid": userId },
    }),
  );

  return (result.Items || []).filter((item) => {
    const inDateRange =
      (!startDate || item.date >= startDate) &&
      (!endDate || item.date <= endDate);
    const hasTags =
      tags.length === 0 ||
      tags.some((tag) =>
        (item.tags || [])
          .map((value) => String(value).toLowerCase())
          .includes(String(tag).toLowerCase()),
      );

    return inDateRange && hasTags;
  });
}

function parseJson(text) {
  const clean = text
    .replace(/```json/g, "")
    .replace(/```/g, "")
    .trim();
  return JSON.parse(clean);
}

async function handleReportJob(message) {
  const { userId, reportId, type, startDate, endDate, tags = [] } = message;

  await docClient.send(
    new UpdateCommand({
      TableName: AI_REPORT_TABLE,
      Key: { userId, reportId },
      UpdateExpression: "SET #status = :status, updatedAt = :updatedAt",
      ExpressionAttributeNames: { "#status": "status" },
      ExpressionAttributeValues: {
        ":status": "processing",
        ":updatedAt": new Date().toISOString(),
      },
    }),
  );

  const logs = await getUserLogs(userId, startDate, endDate, tags);
  const logsText = logs
    .map(
      (log) =>
        `Date: ${log.date}\nTitle: ${log.title}\nContent: ${log.content}`,
    )
    .join("\n\n");

  const prompt = `Analyze these learning journal entries and return JSON:
{
  "summary": "short learning progress summary",
  "strengths": ["strength 1", "strength 2"],
  "weaknesses": ["weakness 1", "weakness 2"],
  "recommendations": ["recommendation 1", "recommendation 2"]
}

Report type: ${type || "weekly"}
Journal entries:
${logsText || "No journal entries found."}`;

  const aiResult = parseJson(await callGroqAI(prompt));

  await docClient.send(
    new UpdateCommand({
      TableName: AI_REPORT_TABLE,
      Key: { userId, reportId },
      UpdateExpression:
        "SET #status = :status, summary = :summary, strengths = :strengths, weaknesses = :weaknesses, recommendations = :recommendations, updatedAt = :updatedAt",
      ExpressionAttributeNames: { "#status": "status" },
      ExpressionAttributeValues: {
        ":status": "completed",
        ":summary": aiResult.summary || "",
        ":strengths": aiResult.strengths || [],
        ":weaknesses": aiResult.weaknesses || [],
        ":recommendations": aiResult.recommendations || [],
        ":updatedAt": new Date().toISOString(),
      },
    }),
  );
}

async function handleQuizJob(message) {
  const {
    userId,
    quizId,
    topic,
    questionCount = 5,
    difficulty = "medium",
    startDate,
    endDate,
    tags = [],
  } = message;

  await docClient.send(
    new UpdateCommand({
      TableName: QUIZ_TABLE,
      Key: { userId, quizId },
      UpdateExpression: "SET #status = :status, updatedAt = :updatedAt",
      ExpressionAttributeNames: { "#status": "status" },
      ExpressionAttributeValues: {
        ":status": "processing",
        ":updatedAt": new Date().toISOString(),
      },
    }),
  );

  const logs = await getUserLogs(userId, startDate, endDate, tags);
  const logsText = logs
    .map((log) => `${log.title}: ${log.content}`)
    .join("\n\n");

  const prompt = `Create ${questionCount} multiple-choice questions for topic "${topic}".
Return JSON only:
{
  "questions": [
    {
      "topic": "${topic}",
      "prompt": "question text",
      "options": ["A", "B", "C", "D"],
      "answer_index": 0,
      "explanation": "why this answer is correct"
    }
  ]
}

Difficulty: ${difficulty}
Learning notes:
${logsText || topic}`;

  const aiResult = parseJson(await callGroqAI(prompt));

  await docClient.send(
    new UpdateCommand({
      TableName: QUIZ_TABLE,
      Key: { userId, quizId },
      UpdateExpression:
        "SET #status = :status, questions = :questions, updatedAt = :updatedAt",
      ExpressionAttributeNames: { "#status": "status" },
      ExpressionAttributeValues: {
        ":status": "completed",
        ":questions": aiResult.questions || [],
        ":updatedAt": new Date().toISOString(),
      },
    }),
  );
}

async function markFailed(message, error) {
  const now = new Date().toISOString();

  if (message.reportId) {
    await docClient.send(
      new UpdateCommand({
        TableName: AI_REPORT_TABLE,
        Key: { userId: message.userId, reportId: message.reportId },
        UpdateExpression:
          "SET #status = :status, errorMessage = :error, updatedAt = :updatedAt",
        ExpressionAttributeNames: { "#status": "status" },
        ExpressionAttributeValues: {
          ":status": "failed",
          ":error": error.message,
          ":updatedAt": now,
        },
      }),
    );
  }

  if (message.quizId) {
    await docClient.send(
      new UpdateCommand({
        TableName: QUIZ_TABLE,
        Key: { userId: message.userId, quizId: message.quizId },
        UpdateExpression:
          "SET #status = :status, errorMessage = :error, updatedAt = :updatedAt",
        ExpressionAttributeNames: { "#status": "status" },
        ExpressionAttributeValues: {
          ":status": "failed",
          ":error": error.message,
          ":updatedAt": now,
        },
      }),
    );
  }
}

export const handler = async (event) => {
  for (const record of event.Records || []) {
    const message = JSON.parse(record.body || "{}");

    try {
      if (message.reportId) {
        await handleReportJob(message);
      } else if (message.quizId) {
        await handleQuizJob(message);
      } else {
        throw new Error("Unknown AI job type");
      }
    } catch (error) {
      console.error("Lambda AI Worker error:", error);
      await markFailed(message, error);
      throw error;
    }
  }

  return { ok: true };
};
````

## Thêm trigger SQS

1. Trong phần thiết kế của hàm Lambda, chọn **Add trigger**.
2. Nguồn: **SQS**.
3. Queue: `ai-report-jobs`.
4. Thêm trigger.
5. Lặp lại các bước trên với `quiz-jobs`.

## Cách worker hoạt động

Worker sẽ:

1. Phân tích từng SQS message.
2. Đánh dấu report hoặc quiz tương ứng là `processing`.
3. Truy vấn `JournalLogs` cho người dùng hiện tại theo khoảng thời gian, tag hoặc chủ đề đã chọn.
4. Tạo prompt gửi tới Groq.
5. Lưu phản hồi AI vào DynamoDB.
6. Đánh dấu mục đó là `completed`, hoặc `failed` nếu có ngoại lệ xảy ra.

## Ảnh chụp tham khảo

![Thiết lập SQS queue](/images/5-Workshop/docx/image38.png)

![Thiết lập Worker Lambda](/images/5-Workshop/docx/image57.png)

![Cấu hình timeout cho worker](/images/5-Workshop/docx/image58.png)

![SQS trigger](/images/5-Workshop/docx/image59.png)