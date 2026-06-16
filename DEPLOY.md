# Cloudflare Pages 部署指南 — AK Blog

## 当前部署状态（2026-06-16）

✅ Pages 项目：`ak-blog`
✅ 部署地址：
  - `https://blog.akrmio.com/`（主域名，CNAME 已配置）
  - `https://akrmio.com/blog/`（子目录，由 akrmio Worker 反向代理）
  - `https://ak-blog-64t.pages.dev/`（Pages 默认子域）

## 重新部署流程

### 方法 A：直接推送（最快）
```bash
cd /root/ak-blog
hugo --gc --minify
CLOUDFLARE_API_TOKEN=<Workers-Pages-Token> \
CLOUDFLARE_ACCOUNT_ID=2809c7f52221962d1a9821f65648881e \
wrangler pages deploy public --project-name=ak-blog --branch=master
```

### 方法 B：GitHub 触发（需先在 Dashboard 配 OAuth）
1. Cloudflare Dashboard → Workers & Pages → ak-blog → Settings → Builds
2. Connect to GitHub → 选 `Charwraith/ak-blog`
3. Build command: `hugo`，Output: `public`，Branch: `master`
4. 之后 push 即触发自动部署

## 关键文件

- `layouts/partials/related-posts.html` — 相关文章内链模块
- `PILLARS.md` — pillar/cluster 词汇表
- `hugo.toml` — Hugo 配置（baseURL = "https://akrmio.com/blog/"）

## 架构说明

```
用户访问 akrmio.com/blog/posts/foo/
    ↓
akrmio Worker (CF Worker)
    ↓ 检测到 /blog/ 前缀
    ↓ 重写为 blog.akrmio.com/posts/foo/ 并代理
blog.akrmio.com (CNAME → ak-blog-64t.pages.dev)
    ↓
Cloudflare Pages 项目 ak-blog
    ↓
Hugo 静态文件 public/posts/foo/index.html
```

子目录代理通过 `akrmio` Worker 实现：把 `/blog/*` 反向代理到 `blog.akrmio.com`，再由 Pages 项目提供静态内容。

## 写文章流程

1. 在 `content/posts/` 创建新 .md 文件
2. 填 front matter（参考 `deepseek-api-guide.md`）：
   ```yaml
   ---
   title: "文章标题"
   date: 2026-06-16T20:00:00+08:00
   draft: false
   pillar: deepseek-api    # 单值
   clusters:              # 多值
     - vs-gpt4o
     - python-tutorial
   description: "SEO 描述"
   ---
   ```
3. `hugo --gc --minify` 本地预览
4. git push → 触发 Pages 重新构建
5. 内链模块自动关联同 pillar / cluster 的其他文章

## pillar / cluster 词汇表

见 `PILLARS.md`（4 个 pillar + 7 个 cluster）。
