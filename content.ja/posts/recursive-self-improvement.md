---
title: "china-ai-outbound - recursive-self-improvement"
displayTitle: "AI が自分自身を構築するとき:Anthropic の 80% コード公開が 2026 年の全開発者に意味するこ"
date: 2026-06-18T11:00:00+08:00
draft: false
pillar: china-ai-outbound
clusters:
  - model-review
  - newsjack
author: "AKRMIO"
description: "AI が自分自身を構築するとき:Anthropic の 80% コード公開が 2026 年の全開発者に意味するこ"
---

2026 年 5 月末、Anthropic 研究所は「When AI builds itself」と題する長い文章を発表しました。タイトルは地味ですが、内容は 2026 年の AI コーディング業界で最も重要なシグナルです:Claude は現在、Anthropic 内部の 80% 以上のマージ済みコードを作成し、エンジニアの四半期生産性は 8 倍に向上し、Claude Mythos Preview はトレーニングコードタスクで 52 倍の高速化を達成し、オープンタスクの成功率は 76% に達しています。

## 4 つの数字:Anthropic は AI で AI を書いている

Anthropic の研究チームは壊滅的な内部公開を発表しました。80% という数字は特に衝撃的です:これは、Anthropic のコードベースに入るコードの大半 — Claude を構築している組織 — が現在 Claude 自身によって書かれていることを意味します。これはもはやアシスタントではなく、筆者です。

## なぜ再帰的自己改善は 2026 年に初めて実現したのか

1950 年代から理論化されていた再帰的自己改善 (RSP) には、2025-2026 年のアーキテクチャのみが満たす 3 つの前提条件が必要でした:(1) コードベース全体を理解するための十分な長コンテキスト (1M+ トークン) ;(2) メタ認知能力 (Claude は自分のコードを評価できる) ;(3) 閉ループ訓練インフラ (RLHF + RLAIF)。

## 開発者への構造的影響

移行は 3 段階で進行します:補完 (2022-2024、AI が次の行を提案)、エージェントループ (2025、AI が write→test→fix ループで反復)、再帰的自己改善 (2026+、AI が次世代 AI を訓練するコードを書く)。

## ヘッジ戦略:リレー API を使って多様化する

単一モデル依存を懸念するチームのために、[akrmio](https://akrmio.com/) は [DeepSeek V4 Pro](https://akrmio.com/blog/posts/deepseek-v4-guide/) と [MiniMax M3](https://akrmio.com/blog/posts/minimax-m3-guide/) によるマルチモデルルーティングを提供しています。
