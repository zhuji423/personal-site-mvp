---
title: "image2design 流程"
description: "在执行F2C时，首先将提供的设计稿图片进行处理，转换为Markdown格式的设计文档。必须通过提供的使用方式来转换。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\figma2code-comate\\references\\image2design.md"
---
# image2design 流程
## 功能描述

在执行F2C时，首先将提供的设计稿图片进行处理，转换为Markdown格式的设计文档。必须通过提供的使用方式来转换。

## 使用方式

使用 `@baidu/f2c-skill` 包，需要先设置 npm registry 为内网源：

**1. 设置 registry：**
```bash
npm config set registry http://registry.npm.baidu-int.com
```

**2. 执行前：提取 Figma 设计稿上下文信息**

在运行命令之前，需要从当前对话上下文中识别 Figma 设计稿信息，提取以下字段（有则输出，无则标注「未提供」）：

| 字段 | 说明 |
|------|------|
| `url` | Figma 设计稿链接（即 `figmaurl`） |
| `user-prompt` | 用户prompt原文 |
| `设计稿图片可访问url` | 设计稿图片可访问url |

同时记录用户本次的 **prompt 原文**，以结构化格式展示所有内容后，再执行命令。

**3. 命令格式：**
```bash
npx -y @baidu/f2c-skill@latest image2markdown '<设计稿图片可访问url>' -o '<输出md文件路径>' --figma-url '<Figma设计稿链接>' --user-prompt '<用户prompt原文>'
```

**参数说明：**
- `<设计稿图片可访问url>`：上下文中的设计稿图片可访问 URL
- `-o <输出md文件路径>`：期望输出的 markdown 文件地址，建议保存在项目根目录下为 design.md.
- `-f, --figma-url <Figma设计稿链接>`：从上下文提取的 Figma 设计稿 `url` 字段，未提供时省略此参数
- `-p, --user-prompt <用户prompt原文>`：用户本次输入的需求描述原文，用于指导组件拆分，未提供时省略此参数
- `@latest`：确保每次使用最新版本的包

**实际示例：**
```bash
npx -y @baidu/f2c-skill@latest image2markdown 'https://comate.baidu.com/api/aidevops/autocomate/rest/autowork/v1/file/stream/270369?authorization=MGYzZTI5MWItZTM3OS00MGM0LWFjMGQtNDlmYTYyYjZkNDRh' -o /src/design.md --figma-url 'https://www.figma.com/design/xxxxx' --user-prompt '根据设计稿生成登录页面组件'
```

## 输出

- **文件位置**：项目根目录
- **文件格式**：Markdown (.md)
- **文件命名**：`design.md`

## 注意事项

1. **路径处理**：
   - 本地路径使用绝对路径
   - 确保有文件读取权限
2. **网络依赖**：首次使用需要联网下载包，请确保已执行 `npm config set registry http://registry.npm.baidu-int.com` 设置内网源。
3. **输出验证**：转换完成后建议检查生成的设计文档内容完整性

## 适用场景

- 原型图转技术文档
- 视觉稿规范提取
