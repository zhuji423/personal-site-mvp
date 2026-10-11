---
title: "基于 HTML 静态项目开发"
description: "当需要使用 HTML 模式开发时（降级场景或用户指定 HTML 技术栈），必须遵循以下规范："
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\build-web-page-comate\\setup-html-scaffold.md"
---
# 基于 HTML 静态项目开发

当需要使用 HTML 模式开发时（降级场景或用户指定 HTML 技术栈），必须遵循以下规范：

## 1. 项目结构

- **必须**新建项目文件夹并进入，在新文件夹里面书写 html 文件
- **允许多个 HTML 文件**：可根据需求创建多个页面（如 `index.html`、`about.html`、`contact.html`），通过 `<a href="about.html">` 实现页面跳转
- **禁止独立的 CSS/JS 文件**：每个 HTML 文件必须是自包含的，样式和脚本内联在文件中

## 2. 单页模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><!-- 页面标题 --></title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            // ⚠️ 必须定义完整 50-900 色阶，根据项目风格选择合适的配色
            primary: {
              50: '', 100: '', 200: '', 300: '', 400: '',
              500: '', 600: '', 700: '', 800: '', 900: ''
            },
            // 可按需添加 secondary、accent 等色阶
          }
        }
      }
    }
  </script>
  <style>/* 仅用于 Tailwind 无法实现的特殊样式 */</style>
</head>
<body class="bg-gray-50 min-h-screen">
  <!-- 页面内容
  图片引用示例（通过 web_search 搜索获取图片链接）：
  <img src="https://images.unsplash.com/..." alt="描述" class="w-full h-64 object-cover rounded-lg">
  -->
  <script>/* 交互逻辑 */</script>
</body>
</html>
```
