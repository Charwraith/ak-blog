---
title: "qwen-36-35b-a3b"
displayTitle: "Qwen3.6-35B-A3B : Pourquoi le MoE 3B-Actif d'Alibaba est la Première Vraie Menace pour les Modèles de Codage Fermés"
date: 2026-06-18T09:00:00+08:00
draft: false
pillar: china-ai-outbound
clusters:
  - model-review
  - migration-guide
author: "AKRMIO"
description: "Qwen3.6-35B-A3B : Pourquoi le MoE 3B-Actif d'Alibaba est la Première Vraie Menace pour les Modèles de Codage Fermés"
---

Mi-juin 2026, Alibaba a discrètement mis en ligne la version quantifiée FP8 de Qwen3.6-35B-A3B sur Hugging Face — la première variante open source de la série Qwen3.6. Architecture MoE sparse 35B total / 3B actif, contexte natif 262K (extensible à 1M token), 73.4% sur SWE-bench, 51.5% sur Terminal-Bench.

## Pourquoi un MoE à 3B actif est une vraie menace

Le dilemme des modèles open source était « petits modèles incapables de tâches complexes, grands modèles trop chers à déployer ». Qwen3.6-35B-A3B met 35B de « capacité de connaissance » dans 3B de « coût de raisonnement ». Seuls ~8.5% des paramètres sont activés par inférence, donc le coût par token est proche d'un modèle dense 3B ; mais la capacité globale atteint 35B grâce au routage sparse.

Pour [Ralph Loop](https://akrmio.com/blog/posts/ralph-loop-coding/), le coût d'activation 3B fait que chaque itération coûte 70-80% moins cher que Claude Sonnet 4.5, mais l'écart de capacité SWE-bench reste sous 10%.

## Impact sur le modèle de coût API

Qwen3.6-35B-A3B comble un point idéal sur le spectre « capacité de codage - coût de déploiement » : les modèles 4B-8B sont très bon marché mais SWE-bench < 50% ; les modèles 30B+ sont puissants mais nécessitent plusieurs GPU H100. Qwen3.6-35B-A3B tourne sur un seul H100 avec la version quantifiée FP8, coût de déploiement proche d'un 7B dense, capacité proche d'un 30B+.
