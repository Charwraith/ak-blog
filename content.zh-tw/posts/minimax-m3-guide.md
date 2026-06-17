---
title: "MiniMax M3 Complete Guide: 200K Long Context at 1/10 the Cost"
displayTitle: "MiniMax M3 完全指南：10 倍價格優勢的 200K 長上下文模型"
date: 2026-06-16T12:00:00+08:00
draft: false
pillar: minimax-api
clusters:
  - model-review
  - pricing-analysis
author: "AKRMIO"
description: "MiniMax M3 實測：200K context + 原生多模態，價格僅為 Claude/GPT 的 1/10"
---

MiniMax M3 於 2026 年 6 月 1 日開源釋出，是首款同時具備 1M token 上下文、原生多模態（文字 / 圖像 / 影片）與代理編碼前沿表現（SWE-Bench Pro 59.0%）的開源權重模型。技術核心是 MiniMax Sparse Attention (MSA)，將長上下文的單 token 計算成本壓到上一代的 1/20，首 token 延遲降低 9×、解碼速度提升 15×。

定價方面，promo 期 $0.30/$1.20（輸入/輸出，每百萬 token），標準價 $0.60/$2.40。以 500K 輸入 + 100K 輸出的代理任務計算，promo 價約 $0.27、標準價 $0.54，僅為 Claude Opus 4.8 的 5–10%。實測在 380K token 的 Node.js repo 一次性分析中，正確率 7/9 環狀依賴，refactoring 建議具體到檔案路徑與函式簽章。

適合長時程編碼代理、大文檔分析、批次處理 pipeline；不適合對多檔推理準確率有極端要求、或需要即時聊天的場景。

[閱讀完整版 →](/blog/posts/minimax-m3-guide/)
