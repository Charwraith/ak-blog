# Cloudflare Pages 部署指南

## 前置条件

- Cloudflare 账号已登录
- GitHub 仓库已就绪：https://github.com/Charwraith/ak-blog
- CF_API_TOKEN 需要以下权限：
  - `Cloudflare Pages: Edit`
  - `Account Settings: Read"

## 步骤 1：在 Cloudflare Dashboard 创建 Pages 项目

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 进入 **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**
3. 选择仓库 `Charwraith/ak-blog`
4. 配置构建：
   - **Project name**: `ak-blog`
   - **Production branch**: `master`
   - **Build command**: `hugo`
   - **Build output目录**: `public`
   - **Hugo version**: `0.137.1`（在环境变量中设置 `HUGO_VERSION=0.137.1`）
5. 点击 **Save and Deploy**

## 步骤 2：配置自定义域名

1. 项目创建后，进入 **Custom domains**
2. 添加域名 `blog.akrmio.com` 或 `akrmio.com/blog`（取决于路由需求）
3. 如果 Cloudflare Pages 不支持子目录路由，需要在 `akrmio.com` 主站上配置反向代理或重定向到 Pages 域名

## 步骤 3：验证部署

```bash
curl -I https://akrmio.com/blog/
# 应返回 200 OK
```

## 注意事项

- Hugo Extended 版本已安装（支持 SCSS 等）
- `public/` 目录已加入 .gitignore，每次 push 后 Cloudflare Pages 自动重新构建
- 内链模块（related-posts）在构建时执行，无需额外配置
