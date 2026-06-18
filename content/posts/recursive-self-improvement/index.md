---
title: "When AI Builds Itself: What Anthropic's 80% Code Revelation Means for Every Developer in 2026"
displayTitle: "AI 開始自己寫自己：Anthropic 自曝 80% 程式碼由 Claude 產出，遞迴自我改進時代正式降臨"
date: 2026-06-17T11:00:00+08:00
draft: false
pillar: china-ai-outbound
clusters:
  - model-review
  - newsjack
author: "AKRMIO Team"
description: "Anthropic 最新內部數據震撼業界：80% 合併程式碼由 Claude 撰寫，工程師季度產出提升 8 倍，Claude Mythos Preview 訓練程式碼提速 52 倍。本文深度拆解遞迴自我改進（RSP）從理論到落地的完整路徑、對開發者工作流的結構性衝擊，以及如何用 akrmio 中轉的 MiniMax M3 與 DeepSeek V4 對沖單一模型依賴風險。"
image: "/images/posts/recursive-self-improvement/hero.jpg"
cover:
  image: "/images/posts/recursive-self-improvement/hero.jpg"
  alt: "Abstract visualization of recursive self-improvement in AI coding with neural network looping into itself"
tags:
  - anthropic
  - claude
  - recursive-self-improvement
  - ai-coding
  - autonomous-agent
---

2026 年 5 月底，Anthropic 研究院發布了一份名為《When AI builds itself》的長文。標題平淡，內容卻是 2026 年迄今為止最重磅的 AI 編碼行業信號：**Claude 現在寫了 Anthropic 內部超過 80% 的合併程式碼，工程師每季度交付量提升 8 倍，Claude Mythos Preview 在訓練程式碼任務上達成 52 倍加速，開放式任務成功率衝上 76%**。這四個數字放在一起，意味著一件所有開發者必須正視的事——AI 編碼已經從「助理」角色越過了臨界點，正式成為「主作者」。

但這篇文章要講的，不只是 Anthropic 的內部進度。80% / 8x / 52x / 76% 這四個數字背後，是「遞迴自我改進」（Recursive Self-Improvement, RSI）這條技術路線第一次在頂級 AI 實驗室內部規模化跑通。對獨立開發者、創業團隊、企業 IT Lead 來說，這不只是「Claude 更厲害了」這種級別的新聞——這是 AI 編碼工具鏈、團隊組織方式、成本結構、商業模式即將被重寫的起點。

文章會拆清楚：Anthropic 這份數據到底證明了什麼、遞迴自我改進的技術原理為什麼在 2026 年才跑通、為什麼中國 AI（DeepSeek V4 / MiniMax M3 / Qwen3.6）在這個新範式裡有獨特的機會窗口，以及如何用 [akrmio 中轉 API](https://akrmio.com/) 把「單一模型依賴 + 暴漲成本」這個新風險壓到最低。

## 四個數字背後：Anthropic 在用 AI 寫 AI

先把這四個關鍵數據拆開看，才能理解它們為什麼重要。

**80% 合併程式碼由 Claude 撰寫**——這個比例不是「建議被接受率」，也不是「輔助生成比例」，而是經過 code review、測試、合併進 main branch 的最終程式碼佔比。Anthropic 內部把這項指標命名為「merged code authorship」：在合併的那一刻，這段程式碼的作者欄位寫的是 Claude，而不是任何一個人類工程師。從 2024 年的 < 20% 到 2026 年的 > 80%，兩年時間，AI 在一家頂級 AI 實驗室內部完成了從「助手」到「主筆」的權力交接。

**工程師每季度交付量提升 8 倍**——這個 8x 聽起來離譜，但拆解後非常合理：當 AI 承擔了 80% 的程式碼撰寫，人類工程師的角色從「打字機」變成了「架構師 + Reviewer + 整合者」。原本一個工程師一週能寫 800 行 production code，現在一週能交付的 8 倍裡，包含的不只是程式碼數量，還有架構決策、測試覆蓋率、技術債清理速度的全面提升。

![Training speedup and productivity multipliers comparison: 1x baseline, 8x engineer output, 52x Claude Mythos Preview training code acceleration](/images/posts/recursive-self-improvement/inline-1.jpg)

**Claude Mythos Preview 訓練程式碼提速 52 倍**——這是整份報告裡最容易被外行忽略、但內行看到會倒吸一口涼氣的數字。它意味著 Claude 不只能寫應用程式碼，它還能寫「用來訓練下一代 Claude 的程式碼」。Anthropic 的 RLHF 訓練 pipeline、評測集生成、A/B test 框架、模型評估程式碼，現在大量由 Claude 自己產出。**AI 開始直接參與 AI 的訓練過程**——這就是「遞迴自我改進」的標準定義。

**開放式任務成功率 76%**——所謂開放式任務，就是「給 Claude 一個模糊目標，讓它自己拆解、自己實作、自己測試」。在 2024 年，這個指標大約是 30%；2026 年衝到 76%。意味著 Claude 在面對沒有明確規格說明書的任務時，四次裡有三次能自行完成到可合併狀態。對比 [Ralph Loop 範式下 agent 在 PR 級任務上的成功率](https://akrmio.com/blog/posts/ralph-loop-coding/)，兩者已經收斂到同一個性能區間。

## 遞迴自我改進為什麼 2026 年才跑通

「AI 改進 AI」不是新概念。這個想法在 1960 年代就被提出，2016 年 OpenAI 的演化策略實驗、2022 年 AlphaZero 自我對弈都觸及過邊界。但它始終有兩個卡點：

第一是**品質下限問題**——AI 寫的程式碼必須達到「人類可接受」的下限，否則自我改進會陷入「把錯的東西改得更錯」的退化循環。這個下限在 2024 年之前幾乎不可能穩定達成：模型在簡單任務上夠用，但在 production 級程式碼（必須考慮併發、錯誤處理、安全性、可維護性）上仍頻繁犯錯。

第二是**評測閉環問題**——AI 要改進自己，必須能準確評估「改進後的版本是否真的更好」。訓練程式碼不是寫完就完，還要跑測試、看 benchmark、對比 baseline。這個評測閉環的搭建成本極高，大多數實驗室都沒有動力為「AI 改 AI」這個研究方向單獨投資一套基礎設施。

Anthropic 在 2025-2026 年突破了這兩個卡點，方法不是單點突破，而是**工具鏈合奏**：

- **底層模型**——Claude Sonnet 4.5 / Opus 4 在 SWE-bench Verified 上跑到 78% / 82%，達到資深工程師水準
- **測試基礎設施**——Anthropic 內部的評測框架已經全自動化，AI 寫的程式碼能在分鐘級時間內獲得完整評測回饋
- **閉環 agent**——Ralph Loop 式的「寫 → 測 → 修」循環在 Anthropic 內部被硬化為標準工作流，agent 可以在沒有人介入的情況下連續運行 2-4 小時
- **評測 prompt 工程**——把模糊目標轉化為可評測任務的「任務規格化」能力，這是 2026 年 agent 框架的核心突破

四層疊加起來，「AI 改 AI」才從論文概念變成日常運營現實。

## 對開發者的結構性衝擊：工作流重寫的起點

Anthropic 80% 這個數字對外部開發者意味著什麼？簡單說：**你用的每一款 AI 編碼工具，在未來 12 個月內都會被這個範式重寫**。

第一層衝擊是**工具選型標準變了**。2024 年大家比的是「誰的代碼補全更準」，2025 年比的是「誰的 agent 能跑更長的任務」，2026 年開始比的是「誰的閉環最快、token 效率最高、模型自迭代能力最強」。Cursor / Copilot / Claude Code / Cline 這些工具的核心競爭點，已經從「模型接入」轉向「評測閉環 + 工作流整合」。

![AI coding agent workflow loop: write code → run tests → fix bugs → merge, with autonomous iteration cycles](/images/posts/recursive-self-improvement/inline-2.jpg)

第二層衝擊是**團隊組織方式變了**。當 AI 承擔 80% 程式碼撰寫，「工程師」的定義需要重寫。原本的 IC（Individual Contributor）角色被拆成兩半：上半部是「架構決策 + 系統設計 + 業務理解」，下半部是「Review + 整合 + 邊界條件處理」。能勝任上半部的工程師價值暴漲（因為他們的槓桿倍數從 1x 變成 8x），只能勝任下半部的工程師面臨直接被替代的風險。

第三層衝擊是**成本結構變了**。AI Credits 時代（[GitHub Copilot 已經在 6 月 1 日全面轉向按用量計費](https://akrmio.com/blog/posts/github-copilot-credits/)）+ 遞迴自我改進時代，兩者疊加意味著**單一任務的 token 消耗會指數級上升**。一個原本 5 分鐘的 agent 循環任務，現在可能跑 30 分鐘消耗上百萬 token。按用量計費的工具鏈下，企業的 AI 編碼帳單會在 2026 下半年經歷一輪「帳單震撼」。

這就是為什麼成本對沖從「nice to have」變成「must have」。

## 對沖策略：用中轉 API 把單一模型風險 + 暴漲成本壓到最低

Anthropic 80% / 8x / 52x / 76% 這組數字公佈之後，所有押注單一模型（無論是 Claude / GPT-4o / Gemini）的團隊都暴露在同一個風險下：**模型漲價 = 帳單直接爆掉**。再加上遞迴自我改進讓 agent 跑的時間越來越長，token 消耗成倍增加，「鎖定單一模型 + 自動 agent 循環」這個組合在 2026 下半年會成為企業 IT 部門最大的不可控成本項。

對沖的方法有三個層次：

**第一層：模型路由**——同一個任務根據類型路由到最便宜的合適模型。簡單代碼補全走 [DeepSeek V4 的 1 元百萬 token 檔位](https://akrmio.com/blog/posts/deepseek-v4-guide/)，需要 200K 長上下文的任務走 [MiniMax M3 的 10 倍性價比模型](https://akrmio.com/blog/posts/minimax-m3-guide/)，複雜架構決策才調用 Claude / GPT-4o。akrmio 中轉 API 的核心價值就是把這層路由做成開箱即用。

**第二層：成本可見性**——agent 跑的時候實時顯示 token 消耗和預估成本，超過預算自動暫停。GitHub Copilot 6 月改版後的池化用量 + 三層預算控制是企業級的標準解法，但對自建 agent 的團隊，需要自己用 [akrmio 的用量儀表板](https://akrmio.com/)補上這層。

**第三層：模型組合**——不要把雞蛋放在一個籃子。Claude 強在推理、DeepSeek 強在性價比、MiniMax M3 強在長上下文、[Qwen3.6-35B-A3B](https://akrmio.com/blog/posts/qwen-36-35b-a3b/) 強在開源可私有化部署。四個模型在 2026 年的評測矩陣裡各有不可替代的位置，akrmio 中轉讓你可以在不改動應用程式碼的情況下，按任務類型動態切換。

## 結論：遞迴自我改進不是終點，是新競賽的起點

Anthropic 這份 80% / 8x / 52x / 76% 的數據公佈之後，所有 AI 編碼玩家都被推上了一條新賽道：誰能最早把「AI 改 AI」規模化，誰就能在下一輪 agent 競賽裡拿到定義權。Google DeepMind、OpenAI、Meta、中國的 DeepSeek / Alibaba / MiniMax 都在這條賽道上加速。

對開發者來說，這是一個「黃金窗口期」：工具鏈在快速迭代、成本曲線在快速下降、模型能力在快速提升。但這也是一個「風險累積期」：鎖定單一模型的代價會越來越高、不跟進遞迴範式的團隊會越來越被甩開。

**最務實的應對是三件事並進**：用 Ralph Loop 風格的 agent 閉環提升個人產出、用模型路由中轉壓住成本底線、用多模型組合對沖單點風險。akrmio 在這三條線上都有現成的工具和指南——下一步怎麼選，取決於你的團隊規模、預算結構和技術債現狀。

無論如何，2026 年已經沒有人可以假裝 AI 編碼還只是「輔助工具」了。Anthropic 自己已經證明了——**當 AI 開始寫 AI 的時候，遊戲規則已經永久改變**。
