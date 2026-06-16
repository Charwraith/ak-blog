---
title: "DeepSeek API 完整指南"
date: 2026-06-10T08:00:00+08:00
draft: false
pillar: deepseek-api
clusters:
  - vs-gpt4o
  - python-tutorial
description: "深入解析 DeepSeek API 的调用方式与最佳实践"
---

这是一篇测试文章，用于验证内链模块。

## 什么是 DeepSeek API

DeepSeek API 是一个强大的 LLM API 服务...

## 调用示例

```python
import openai
openai.api_key = "your-key"
response = openai.ChatCompletion.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

## 相关话题

本文属于 `deepseek-api` pillar，同时属于 `vs-gpt4o` 和 `python-tutorial` clusters。
