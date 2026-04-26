# 个人网站 MVP

这是一个零第三方依赖的最小静态网站版本。先用本地 Markdown 内容生成 HTML，后续可以把内容来源替换成 Notion API 或 Notion 导出的 Markdown/CSV。

## 本地生成

```powershell
python sitegen.py
python -m http.server 8000 -d site
```

打开 `http://localhost:8000`。

## 内容目录

- `content/notes/`：笔记 Markdown
- `content/projects/`：项目 Markdown
- `site/`：生成后的静态网站

每个 Markdown 文件的第一个 `# 标题` 会作为页面标题。

## 发布到 GitHub Pages

1. 新建 GitHub 仓库并推送当前目录。
2. 在仓库设置中启用 GitHub Pages，Source 选择 GitHub Actions。
3. 每次 push 到 `main`，workflow 会重新生成并发布 `site/`。
