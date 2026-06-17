---
title: "Python Tutorial"
description: "Python 接入 LLM API 的完整教程：從 SDK 安裝、認證配置、prompt 設計、到生產級部署的所有坑點。"
pillar: python-tutorial
---

Python 是 AI 開發的事實標準語言。這個 Pillar 收錄所有 LLM API 的 Python 接入教程：從 `pip install` 到生產環境的錯誤處理、token 管理、批量調用優化。

無論你用的是 OpenAI SDK 兼容的 API（[DeepSeek V4](/blog/posts/deepseek-v4-guide/) / [MiniMax M3](/blog/posts/minimax-m3-guide/) / [Qwen](/blog/posts/qwen-36-35b-a3b/)）還是 Anthropic SDK（Claude / Claude Code），這裡都有對應的遷移指南。

## 核心教程文章

- **[DeepSeek API 完整指南](/blog/posts/deepseek-api-guide/)** — OpenAI 兼容 SDK 遷移、API key 申請、上下文管理、批量調用。涵蓋從 `deepseek-chat` 到 `deepseek-v4` 的所有坑點。
- **[DeepSeek V4 完全指南](/blog/posts/deepseek-v4-guide/)** — 1M 上下文處理、384K 輸出管理、V4-Flash vs V4-Pro 的 Python SDK 差異。
- **[MiniMax M3 完全指南](/blog/posts/minimax-m3-guide/)** — 200K 長上下文的 streaming 處理、cache miss 場景的成本控制。
- **[Edgee Turbo Models](/blog/posts/edgee-turbo-models-guide/)** — Claude Code 切換 Kimi K2.7 / MiniMax M2.7 的 3 步配置。
- **[Context Engineering 2026](/blog/posts/context-engineering-2026/)** — Prompt 到 Context 範式轉移的 Python 實踐：上下文管理、記憶結構、工具定義、八要素框架。

## 快速開始

```python
# DeepSeek V4 Flash — 最便宜的 OpenAI 兼容接入
from openai import OpenAI

client = OpenAI(
    api_key="<YOUR_KEY>",
    base_url="https://akrmio.com/v1"  # 中轉入口
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=1024
)
print(response.choices[0].message.content)
```

```python
# MiniMax M3 — 200K 長上下文
response = client.chat.completions.create(
    model="MiniMax-M3",
    messages=[{"role": "user", "content": "<200K context here>"}],
    max_tokens=4096,
    stream=True
)
for chunk in response:
    print(chunk.choices[0].delta.content or "", end="")
```

## 教程覆蓋的場景

- **基礎接入** — SDK 安裝、認證、第一次調用
- **長上下文處理** — 100K+ token 的 streaming、分塊、cache 優化
- **Agent 編程** — Ralph Loop 風格的閉環迭代（[詳見](/blog/posts/ralph-loop-coding/)）
- **生產部署** — 錯誤重試、配額管理、成本監控、多模型路由
- **遷移指南** — OpenAI → 中轉、Anthropic → 中轉的 API 兼容性處理

完整的 Python 教程系列見 [akrmio.com/blog](https://akrmio.com/blog/)。
