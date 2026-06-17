---
title: "qwen-36-35b-a3b"
displayTitle: "Qwen3.6-35B-A3B:Alibaba の 3B アクティブ MoE がクローズドコーディングモデルへの最初の真の脅威である理由"
date: 2026-06-18T09:00:00+08:00
draft: false
pillar: china-ai-outbound
clusters:
  - model-review
  - migration-guide
author: "AKRMIO"
description: "Qwen3.6-35B-A3B:Alibaba の 3B アクティブ MoE がクローズドコーディングモデルへの最初の真の脅威である理由"
---

2026 年 6 月中旬、Alibaba は Hugging Face に Qwen3.6-35B-A3B の FP8 量子化版をこっそり公開しました — Qwen3.6 シリーズの最初のオープンソースバリアント。35B 合計 / 3B アクティブのスパース MoE アーキテクチャ、ネイティブ 262K コンテキスト(1M トークンに拡張可能)、SWE-bench で 73.4%、Terminal-Bench で 51.5%。

## なぜ 3B アクティブの MoE が真の脅威なのか

オープンモデルのジレンマは「小型モデルは複雑なタスクが実行できない、大型モデルは展開コストが高すぎる」でした。Qwen3.6-35B-A3B は 35B の「知識キャパシティ」を 3B の「推論コスト」に詰め込みます。推論ごとに約 8.5% のパラメータのみが活性化されるため、トークンあたりのコストは 3B dense モデルに近い；但是、スパースルーティングにより全体的な能力は 35B に達します。

[Ralph Loop](https://akrmio.com/blog/posts/ralph-loop-coding/) にとって、3B アクティブコストは各イテレーションのコストを Claude Sonnet 4.5 より 70-80% 安くしますが、SWE-bench の能力差は 10% 以内に収まります。

## API コストモデルへの影響

Qwen3.6-35B-A3B は「コーディング能力 - 展開コスト」スペクトルのスイートスポットを埋めます:4B-8B モデルは非常に安価ですが SWE-bench < 50%;30B+ モデルは強力ですが複数の H100 が必要です。Qwen3.6-35B-A3B は FP8 量子化版で 1 枚の H100 で動作し、展開コストは 7B dense に近く、能力は 30B+ に近い。
