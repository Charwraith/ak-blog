---
title: "china-ai-outbound - recursive-self-improvement"
displayTitle: "當 AI 自己寫自己:Anthropic 自曝 80% 程式碼由 Claude 產出,遞迴自我改進時代降臨"
date: 2026-06-18T11:00:00+08:00
draft: false
pillar: china-ai-outbound
clusters:
  - model-review
  - newsjack
author: "AKRMIO"
description: "當 AI 自己寫自己:Anthropic 自曝 80% 程式碼由 Claude 產出,遞迴自我改進時代降臨"
---

2026 年 5 月底,Anthropic 研究院發布了《When AI builds itself》一文。標題平淡,內容卻是 2026 年迄今最重磅的 AI 編碼行業信號:Claude 現在寫了 Anthropic 內部超過 80% 的合併程式碼,工程師每季度交付量提升 8 倍,Claude Mythos Preview 在訓練程式碼任務上達成 52 倍加速,開放式任務成功率衝上 76%。

## 四個數字背後:Anthropic 在用 AI 寫 AI

80% 這個數字特別震撼:這意味著進入 Anthropic 程式碼庫(Claude 構建組織本身)的大部分程式碼,現在都是 Claude 自己寫的。這已經不是助理,是主筆。

## 為什麼遞迴自我改進 2026 年才跑通

1950 年代理論化的遞迴自我改進 (RSP) 需要 3 個前提,只有 2025-2026 年的架構同時滿足:(1) 足夠長的上下文(1M+ tokens)理解整個程式碼庫;(2) 元認知能力(Claude 能評估自己的程式碼);(3) 閉環訓練基礎設施 (RLHF + RLAIF)。

## 對開發者的結構性衝擊

三階段跳躍:補全(2022-2024,AI 給下一行建議)、Agent Loop(2025,AI 在 write→test→fix 迭代)、遞迴自我改進(2026+,AI 寫訓練下一代 AI 的程式碼)。

## 對沖策略:用中轉 API 對沖單一模型風險

對於擔心單一模型依賴的團隊,[akrmio](https://akrmio.com/) 提供 [DeepSeek V4 Pro](https://akrmio.com/blog/posts/deepseek-v4-guide/) + [MiniMax M3](https://akrmio.com/blog/posts/minimax-m3-guide/) 的多模型路由組合。
