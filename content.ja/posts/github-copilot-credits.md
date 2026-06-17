---
title: "github-copilot-credits"
displayTitle: "GitHub Copilot AI Credits:Premium Request の終わりとチームの請求書への影響"
date: 2026-06-18T08:30:00+08:00
draft: false
pillar: llm-cost
clusters:
  - pricing-analysis
  - migration-guide
author: "AKRMIO"
description: "GitHub Copilot AI Credits:Premium Request の終わりとチームの請求書への影響"
---

2026 年 4 月 27 日、GitHub CPO Mario Rodriguez は、地味なタイトルですが業界全体を揺るがす内容のお知らせを発表しました :**GitHub Copilot は 2026 年 6 月 1 日から使用量ベースの課金に移行します**。Premium Request 単位は GitHub AI Credits に正式に置き換えられ、各モデルの公開 API 料金でトークン(入力、出力、キャッシュ)に対して計算されます。

## なぜ GitHub は変更する必要があるのか

Mario Rodriguez はお知らせに書いています :「現在、簡単なチャットの質問と複数時間にわたる自律的なコーディングセッションがユーザーにとって同じコストです。GitHub は推論コストの大部分を吸収してきましたが、現在の premium request モデルは持続可能ではありません。」

2024 年末からの Copilot のエージェント化により、ユーザーごとの推論コストが 5-10 倍に増加しました。PRU は「200 トークンを消費するチャットの質問」と「3 時間実行されて 200 万トークンを消費する Ralph Loop」を区別できませんでした。

## 課金ルール

**常に無料** : コード補完と Next Edit 提案(すべての有料プラン)

**Credits を消費する** : 会話、自律的なエージェントタスク、モデル切り替え、コンテキスト拡張。Opus 4.6 vs Sonnet 4.5 を同じタスクで実行 = 5-8 倍の差

**Code Review は Actions minutes も消費する** : 追加コスト
