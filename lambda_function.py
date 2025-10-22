import json
import boto3
import requests
from datetime import datetime

# 初始化 AWS 客戶端
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
s3 = boto3.client("s3")

# 替換為你的 S3 bucket 名稱
BUCKET = "my-news-summary-bucket"

# 取得即時新聞
def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=9a534f9ca42e4a128b361d333cc4eb84"
    response = requests.get(url, timeout=10)
    data = response.json()

    if "articles" not in data:
        return "Failed to fetch news."
    articles = data["articles"][:5]
    headlines = [f"{a['title']}: {a.get('description','')}" for a in articles if a.get("title")]
    return "\n".join(filter(None, headlines))

# 調用 Claude 3 Haiku 生成摘要
def summarize_text(text):
    # Claude 3 使用 Messages API
    body = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": (
                    "Summarize the following news headlines into a clean, natural three‑sentence English summary. "
                    "Write in one or two concise paragraphs, no numbering, no bullet points.\n\n"
                    f"{text}"
                )
            }
        ],
        "max_tokens": 200,
        "temperature": 0.7,
        "anthropic_version": "bedrock-2023-05-31"
    })

    # 呼叫 Bedrock Claude 模型
    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body=body
    )

    result = json.loads(response["body"].read())
    content = result["content"][0]["text"].strip()
    
    # 去除多餘換行讓格式更漂亮
    formatted = " ".join(content.split())
    return formatted

# Lambda 主入口函式
def lambda_handler(event, context):
    news = fetch_news()
    summary = summarize_text(news)
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")

    # 儲存到 S3
    s3_key = f"summaries/{timestamp}.json"
    s3.put_object(
        Bucket=BUCKET,
        Key=s3_key,
        Body=json.dumps({"summary": summary}, indent=2)
    )

    print("Summary:", summary)
    return {
        "statusCode": 200,
        "body": json.dumps({"summary": summary, "s3_key": s3_key})
    }
