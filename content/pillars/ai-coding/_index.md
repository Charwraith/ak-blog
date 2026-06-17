---
title: "AI Coding"
description: "AI 辅助编码、自主 Agent 编程、递迴自我改進等 AI coding 主题文章集合。"
pillar: ai-coding
---

AI 編碼正在從「輔助工具」進化為「主作者」。這個 Pillar 收錄所有關於 AI 如何寫程式碼、AI 如何改進 AI、以及開發者如何與 AI agent 協作完成生產級軟件的深度分析。

從 2024 年的代碼補全（GitHub Copilot 補一行），到 2025 年的 agent loop（[Ralph Loop](/blog/posts/ralph-loop-coding/)），再到 2026 年的遞迴自我改進（[Anthropic 80% 代碼由 Claude 產出](/blog/posts/recursive-self-improvement/)），AI 編碼的範式在兩年內完成了三次跳躍。

## 核心文章

- **[Ralph Loop 完全指南](/blog/posts/ralph-loop-coding/)** — 2026 年真正能落地的自主 AI 編碼範式。Geoffrey Huntley 命名的「傻循環」工作流，5-10x 效率提升的真相與陷阱。
- **[Recursive Self-Improvement 深度解讀](/blog/posts/recursive-self-improvement/)** — Anthropic 自曝 80% 合併程式碼由 Claude 撰寫、52x 訓練提速、76% 開放式任務成功率。遞迴自我改進時代對開發者的結構性衝擊與對沖策略。
- **[Qwen3.6-35B-A3B 評測](/blog/posts/qwen-36-35b-a3b/)** — 阿里開源 MoE 為何是閉源編碼模型的第一個真正威脅？35B 總參 / 3B 激活的 MoE 架構對 AI coding 成本模型的衝擊。
- **[AI Coding Agents 2026 全景圖](/blog/posts/ai-coding-agents-2026/)** — Claude Code / Codex / Cursor / Copilot 為何都收斂到同一個 agent 架構？CLI / IDE / Cloud 三大原型 + token 成本對沖。
- **[Context Engineering 2026](/blog/posts/context-engineering-2026/)** — 為什麼 AI 團隊集體從 Prompt Engineering 遷移到 Context Engineering？八要素框架 + Karpathy 的 OS 比喻。

## AI Coding 的三個階段

**Stage 1: 補全（2022-2024）** — 模型給出下一行 / 下幾行的代碼建議，人類開發者是主筆。

**Stage 2: Agent Loop（2025）** — 模型在「寫 → 測 → 修」閉環裡自主迭代，人類只負責 PRD 和邊界設定。

**Stage 3: 遞迴自我改進（2026+）** — 模型開始寫「用來訓練下一代模型的程式碼」。AI 不只寫應用，也寫自己。

## 實戰建議

無論你處於哪個階段，三件事並進能讓你在 AI coding 浪潮裡保持領先：

1. **用閉環 agent 提升個人產出** — 從 Ralph Loop 開始，把 5-10x 的加速用在你重複性的編碼任務上
2. **用模型路由中轉壓住成本** — [akrmio 中轉 API](https://akrmio.com/) 讓你按任務類型動態切換 DeepSeek V4 / MiniMax M3 / Claude
3. **跟進遞迴範式的工具更新** — Cursor、Claude Code、Cline、Copilot 都在快速迭代，半年內的能力差距可能是 2-3 倍
