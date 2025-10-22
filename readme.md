# AWS Daily News Summarizer Agent

An autonomous AI agent that automatically fetches daily headlines, summarizes them with Amazon Bedrock Claude 3 Haiku, and stores concise summaries in Amazon S3.

## Architecture
EventBridge → Lambda → Bedrock → S3 → (optional) API Gateway

## Features
- Fully serverless design
- Uses Bedrock large language model for reasoning
- Stores results automatically in S3
- Easy to deploy, low cost (<$0.05/day)

## Tools
- AWS Lambda
- Amazon Bedrock Claude 3 Haiku
- Amazon S3
- Amazon EventBridge
- (Optional) API Gateway

## Output Example

{
  "summary": "CNN's future is uncertain as its parent company Warner Bros. Discovery explores a potential sale, which could lead to the network being acquired by Paramount Skydance CEO David Ellison. Controversy surrounds a political candidate in Arizona, as the state's attorney general has sued the US House of Representatives over the refusal to seat a newly elected member due to the government shutdown. Quarterback Russell Wilson has responded to criticism from his former coach Sean Payton, invoking a previous NFL scandal in his pointed rebuttal.",
  "s3_key": "summaries/2025-10-22-2327.json"
}
