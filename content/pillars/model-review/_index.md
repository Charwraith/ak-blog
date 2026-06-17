---
title: "Model Review"
description: "LLM 模型評測、能力對比、benchmark 分析。所有主流模型在編碼、推理、長上下文、agent 場景的實測結果。"
pillar: model-review
---

選模型不是比 benchmark 分數，是比「在你的任務上、你的預算下、你的延遲容忍度內，哪個模型最划算」。這個 Pillar 收錄所有主流 LLM 的實戰評測、橫向對比、以及不同場景下的選型建議。

2026 年的模型市場已經進入「價差 300 倍」+「能力矩陣化」的階段。Claude Opus 4 的 $75/M output 與 DeepSeek V4 Flash 的 $0.40/M output 相差近 200 倍，但兩者各自有不可替代的場景。

## 核心評測文章

- **[DeepSeek V4 完全指南](/blog/posts/deepseek-v4-guide/)** — 1M token 上下文、384K 最大輸出，MIT 開源。V4-Flash vs V4-Pro 選型對比。
- **[MiniMax M3 完全指南](/blog/posts/minimax-m3-guide/)** — 200K 長上下文 + 1/10 價格。在長文檔處理、批量分析場景下的性價比之王。
- **[Qwen3.6-35B-A3B 評測](/blog/posts/qwen-36-35b-a3b/)** — 35B 總參 / 3B 激活的 MoE 架構，SWE-bench 73.4% / Terminal-Bench 51.5%，262K 上下文。
- **[GPT-4o vs DeepSeek 深度對比](/blog/posts/deepseek-vs-gpt4o/)** — 能力、成本、延遲、context window 四維度完整對照表。
- **[Edgee Turbo Models](/blog/posts/edgee-turbo-models-guide/)** — Claude Code 無縫切換 Kimi K2.7 / MiniMax M2.7 的中轉方案。
- **[Gemma 4 評測](/blog/posts/gemma-4/)** — Google DeepMind Apache 2.0 開源、4 變體覆蓋 2B-31B、31B 全球開源第 3。對 DeepSeek V4 / Qwen3.6 的真實衝擊。
- **[LLM API Pricing 2026](/blog/posts/llm-pricing-2026/)** — 所有主流模型按每百萬 token 真實成本排名，模型路由 + 上下文壓縮可節省 70-85%。

## 2026 年選型決策樹

按任務類型分三層：

**頂級推理（$3-30/M）** — 架構設計、複雜調試、安全審計 → Claude Sonnet 4.5 / Opus 4
**中端主力（$0.5-2/M）** — code review、文件生成、agent loop → [DeepSeek V4 Pro](/blog/posts/deepseek-v4-guide/) / MiniMax M3
**性價比層（$0.1-0.5/M）** — 補全、轉換、抽取、批量分析 → DeepSeek V4 Flash / Qwen3.6-35B-A3B

## 評測方法論

我們的評測堅持三個原則：

1. **真實任務** — 不只用 SWE-bench / MMLU 等公開 benchmark，更用實際業務場景（CRUD 生成、API 集成、log 分析）做盲測
2. **成本對齊** — 同一個任務跑完後，不只比成功率，比「成功率 × 平均 token 消耗 × 單價」三者的乘積
3. **場景細分** — 不說「A 比 B 好」，只說「在 X 場景下 A 比 B 好 30%，在 Y 場景下 B 比 A 好 15%」

更多評測數據見 [akrmio.com/blog](https://akrmio.com/blog/)。
