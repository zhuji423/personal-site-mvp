# 个人网站

这是一个 Astro 静态个人网站，用来发布项目、笔记、本科论文和 PDF 等静态资料。网站部署在 GitHub Pages。

## 本地生成

```powershell
npm install
npm run dev
```

开发预览默认打开 `http://localhost:4321/personal-site-mvp/`。

## 内容目录

- `src/content/notes/`：笔记 Markdown
- `src/content/projects/`：项目 Markdown
- `public/assets/`：PDF、图片等静态资源
- `dist/`：`npm run build` 生成后的静态网站

Markdown 文件需要 frontmatter，例如：

```markdown
---
title: 页面标题
description: 页面简介
---
```

## 发布到 GitHub Pages

每次 push 到 `main` 后，GitHub Actions 会运行：

```powershell
npm ci
npm run build
```

然后把 `dist/` 发布到 GitHub Pages。
