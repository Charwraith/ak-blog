---
title: "Qwen3.6-35B-A3B: Why Alibaba's 3B-Active MoE is the First Real Threat to Closed Coding Models"
displayTitle: "Qwen3.6-35B-A3B 評測：阿里開源 MoE 為何是閉源編碼模型的第一個真正威脅？"
date: 2026-06-18T09:00:00+08:00
draft: false
pillar: china-ai-outbound
clusters:
  - model-review
  - migration-guide
author: "AKRMIO"
description: "Qwen3.6-35B-A3B 評測：阿里開源 MoE 為何是閉源編碼模型的第一個真正威脅？"
---

2026 年 6 月中旬，阿里巴巴在 Hugging Face 靜默上線了 Qwen3.6-35B-A3B 的 FP8 量化版——Qwen3.6 系列首個開源變體。35B 總參數 / 3B 激活的稀疏 MoE 架構，262K 原生上下文（可擴展到 1M），SWE-bench 73.4%、Terminal-Bench 51.5%。

## 為什麼 3B 激活的 MoE 是真正的威脅

過去兩年開源模型的困境是「小模型跑不動複雜任務、大模型部署成本太高」。Qwen3.6-35B-A3B 的設計哲學：把 35B 的「知識容量」裝在 3B 的「推理成本」裡。每次推理只激活約 8.5% 參數，單次 token 計算量接近 3B dense 模型；MoE 稀疏路由讓整個模型的「記憶容量」達到 35B 量級。

對 [Ralph Loop](/blog/posts/ralph-loop-coding/) 這種 PRD → code → test → fix 循環，Qwen3.6-35B-A3B 的 3B 激活成本讓每輪迭代的 API 開銷比 Claude Sonnet 4.5 低 70-80%，但 SWE-bench 編碼能力差距在 10% 以內。

## 對 API 成本模型的衝擊

Qwen3.6-35B-A3B 填補了「編碼能力 - 部署成本」光譜上的甜蜜點空缺：4B-8B 開源模型成本極低但 SWE-bench < 50%；30B+ 開源模型能力強但單卡跑不動。Qwen3.6-35B-A3B 單卡 H100 就能跑 FP8 量化版，部署成本接近 7B dense，能力接近 30B+。

對正在做 [DeepSeek V4 遷移](/blog/posts/deepseek-v4-guide/) 或 [MiniMax M3 中轉評估](/blog/posts/minimax-m3-guide/) 的企業 IT，Qwen3.6-35B-A3B 提供了新選項：在「完全閉源中轉 API」和「自建開源推理集群」之間，多了「用中轉方式跑 Qwen3.6-35B-A3B」的中間層。

## 部署選項

**自建 FP8 推理集群**：單卡 H100 80GB 跑 FP8 量化版，吞吐量約 200 token/秒。對月 token 消耗 > 5 億的中大型企業，自建 TCO 在 6 個月後回本。

**中轉 API**：[akrmio](https://akrmio.com/) 計劃 7 月接入 Qwen3.6-35B-A3B 中轉服務，按 token 計費、零月費、批量折扣。對月 token < 5 億的團隊，中轉比自建便宜 30-50%。

## 結論：開源閉源的邊界正在消失

Qwen3.6-35B-A3B 的真正意義是「開源模型在編碼賽道上第一次具備替代閉源旗艦的性價比」。2026 年下半年預計更多企業從 Claude / GPT-4o 遷移到 Qwen3.6-35B-A3B + 自主可控部署的混合架構。

👉 [看 akrmio 中轉定價：DeepSeek V4 + MiniMax M3 + 即將接入的 Qwen3.6-35B-A3B](/pricing/)
