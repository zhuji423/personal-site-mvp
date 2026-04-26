# Personal Site

这是一个使用 Astro 构建的静态个人网站，用于发布个人简介、项目、笔记、本科论文、PDF 和图片等资料。

线上地址：

- 网站首页：https://zhuji423.github.io/personal-site-mvp/
- 论文页面：https://zhuji423.github.io/personal-site-mvp/projects/undergraduate-thesis/
- 论文 PDF：https://zhuji423.github.io/personal-site-mvp/assets/undergraduate-thesis.pdf

## 技术栈

- Astro：静态站点框架，负责页面路由、Markdown 渲染和构建。
- Markdown Content Collections：管理 `notes` 和 `projects` 内容。
- CSS：全站样式在 `src/styles/global.css`。
- GitHub Actions：每次 push 到 `main` 后自动构建。
- GitHub Pages：托管构建后的静态网站。

这个项目没有后端。所有页面、PDF、图片都会在构建时生成或复制成静态文件。

## 本地使用

先安装依赖：

```powershell
npm install
```

启动开发服务器：

```powershell
npm run dev
```

本地访问：

```text
http://localhost:4321/personal-site-mvp/
```

构建生产版本：

```powershell
npm run build
```

构建结果会输出到：

```text
dist/
```

本地预览生产版本：

```powershell
npm run preview
```

## 如何更新内容

### 新增一篇笔记

在 `src/content/notes/` 下新增 Markdown 文件，例如：

```text
src/content/notes/my-note.md
```

文件格式：

```markdown
---
title: 我的笔记标题
description: 一句话简介
---

# 我的笔记标题

正文内容。
```

保存后运行：

```powershell
npm run dev
```

访问：

```text
http://localhost:4321/personal-site-mvp/notes/my-note/
```

### 新增一个项目

在 `src/content/projects/` 下新增 Markdown 文件，例如：

```text
src/content/projects/my-project.md
```

文件格式：

```markdown
---
title: 项目名称
description: 项目简介
featured: true
---

# 项目名称

项目详情。
```

访问路径会根据文件名生成：

```text
/personal-site-mvp/projects/my-project/
```

### 更新 About 页面

About 页面不是 Markdown，而是 Astro 页面：

```text
src/pages/about.astro
```

如果要改个人简介、本科论文介绍、联系方式，改这个文件。

### 更新论文页面

论文正文在：

```text
src/content/projects/undergraduate-thesis.md
```

论文 PDF 在：

```text
public/assets/undergraduate-thesis.pdf
```

论文图片在：

```text
public/assets/thesis-images/
```

Markdown 里引用 PDF：

```markdown
[打开 PDF 论文](/personal-site-mvp/assets/undergraduate-thesis.pdf)
```

Markdown 里引用图片：

```markdown
![](/personal-site-mvp/assets/thesis-images/figure-01.png)
```

## 如何发布

正常更新流程：

```powershell
git status
git add .
git commit -m "your message"
git push
```

push 到 `main` 后，GitHub Actions 会自动运行：

```powershell
npm ci
npm run build
```

然后把 `dist/` 发布到 GitHub Pages。

发布配置文件：

```text
.github/workflows/pages.yml
```

GitHub Pages 发布地址：

```text
https://zhuji423.github.io/personal-site-mvp/
```

## 代码结构

```text
.
├── astro.config.mjs
├── package.json
├── package-lock.json
├── tsconfig.json
├── public/
│   └── assets/
│       ├── undergraduate-thesis.pdf
│       └── thesis-images/
├── src/
│   ├── components/
│   │   └── EntryCard.astro
│   ├── content/
│   │   ├── notes/
│   │   └── projects/
│   ├── content.config.ts
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── lib/
│   │   └── paths.ts
│   ├── pages/
│   │   ├── about.astro
│   │   ├── index.astro
│   │   ├── notes/
│   │   └── projects/
│   └── styles/
│       └── global.css
└── .github/
    └── workflows/
        └── pages.yml
```

### 关键文件说明

`astro.config.mjs`

配置站点域名、GitHub Pages base path、Markdown 插件。这里的 `base: "/personal-site-mvp"` 很重要，因为这是 GitHub Pages 项目站点，不是根域名站点。

`src/lib/paths.ts`

统一处理 `/personal-site-mvp/` 路径前缀，避免链接被拼成 `/personal-site-mvpprojects/...` 这种错误路径。

`src/layouts/BaseLayout.astro`

全站基础布局，包含 HTML 结构、顶部导航、footer 和全局 CSS 引入。

`src/components/EntryCard.astro`

项目卡片和笔记卡片组件。

`src/pages/`

Astro 路由目录。文件路径决定 URL：

- `src/pages/index.astro` -> `/personal-site-mvp/`
- `src/pages/about.astro` -> `/personal-site-mvp/about/`
- `src/pages/projects/index.astro` -> `/personal-site-mvp/projects/`
- `src/pages/projects/[slug].astro` -> 项目详情页
- `src/pages/notes/[slug].astro` -> 笔记详情页

`src/content.config.ts`

定义内容集合 schema。当前有两个集合：

- `notes`
- `projects`

`src/content/`

存放 Markdown 内容。新增笔记或项目时主要改这里。

`public/assets/`

静态资源目录。放在这里的文件会原样复制到最终网站，例如 PDF 和论文图片。

`src/styles/global.css`

全站样式，包括布局、卡片、正文、表格、图片、代码块、KaTeX 公式样式等。

`.github/workflows/pages.yml`

GitHub Pages 自动发布流程。

## 常见问题

### 为什么本地链接必须带 `/personal-site-mvp/`

因为这个网站发布在 GitHub Pages 的项目路径下：

```text
https://zhuji423.github.io/personal-site-mvp/
```

所以本地开发也使用同样的 base path：

```text
http://localhost:4321/personal-site-mvp/
```

### 为什么不用 Python 生成 HTML

之前的 Python 版本只是最小可运行原型。它不适合长期维护 Markdown、图片、表格和公式。Astro 对内容型个人网站更合适，结构也更接近正常前端项目。

### 为什么没有后端

当前网站是静态内容站，不需要登录、数据库、评论系统或动态接口。GitHub Pages 只能托管静态文件，但这正好满足当前需求。
