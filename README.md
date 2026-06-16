# AKRMIO Blog

SEO blog powered by Hugo, deployed via Cloudflare Pages.

## 技术栈

- **框架**: Hugo (Extended)
- **部署**: Cloudflare Pages (GitHub 触发自动构建)
- **域名**: akrmio.com/blog/

## 文章规范

每篇文章 front matter 需包含：

```yaml
---
title: "文章标题"
date: 2026-06-10T08:00:00+08:00
draft: false
pillar: deepseek-api    # 单值，主题柱
clusters:               # 多值，所属簇
  - vs-gpt4o
  - python-tutorial
description: "SEO 描述"
---
```

词汇表见 `PILLARS.md`。

## 本地构建

```bash
hugo server        # 开发预览
hugo build         # 生产构建（输出到 public/）
```

## 内链机制

文章底部的"相关文章"模块自动根据 `pillar` + `clusters` 关联，无需手动填写。
