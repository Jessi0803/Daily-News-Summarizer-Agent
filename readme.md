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

