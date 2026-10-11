---
title: "n8n AI 大佬日报工作流使用指南"
description: "本工作流旨在帮助你自动收集 Twitter 和知乎上 AI 领域大佬的最新动态，并利用 OpenAI 生成中文日报，最后通过邮件发送给你。"
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\01_code\\code\\antigravity\\README_n8n_report.md"
---
# n8n AI 大佬日报工作流使用指南

本工作流旨在帮助你自动收集 Twitter 和知乎上 AI 领域大佬的最新动态，并利用 OpenAI 生成中文日报，最后通过邮件发送给你。

## 📋 功能特性
- **多源采集**：支持 Twitter (via RSSHub) 和知乎 (via RSSHub)。
- **智能总结**：使用 OpenAI (GPT-4o/mini) 对过去 24 小时的内容进行摘要。
- **定时推送**：每天早上 9:00 自动运行。
- **邮件通知**：直接将日报发送到你的邮箱。

## 🛠️ 准备工作

### 1. n8n 环境
确保你已经安装并运行了 n8n (建议版本 1.0+)。

### 2. RSSHub 服务
由于 Twitter 和知乎的反爬策略，你需要一个可用的 RSSHub 实例。
- **公共实例**：`https://rsshub.app` (可能不稳定或被墙)
- **自建实例 (推荐)**：建议使用 Docker 自建 RSSHub 以保证稳定性。
  - 部署文档：[RSSHub 部署指南](https://docs.rsshub.app/install/)

### 3. OpenAI API Key
你需要一个有效的 OpenAI API Key 用于生成摘要。

## 🚀 导入与配置

### 第一步：导入工作流
1. 下载本仓库中的 `n8n_ai_daily_report.json` 文件。
2. 打开 n8n 编辑器界面。
3. 点击右上角菜单 -> **Import from File**，选择下载的 JSON 文件。

### 第二步：配置节点

#### 1. 修改数据源 (HTTP Request 节点)
- **Fetch Twitter (RSSHub)**:
  - URL 默认为 `https://rsshub.app/twitter/user/karpathy`。
  - 请将 `karpathy` 替换为你关注的大佬 ID，或使用 RSSHub 支持的其他 Twitter 路由。
  - 如果使用自建 RSSHub，请将 `https://rsshub.app` 替换为你的服务器地址。
- **Fetch Zhihu (RSSHub)**:
  - URL 默认为 `https://rsshub.app/zhihu/people/activities/kaifulee` (李开复)。
  - 请替换为你关注的知乎用户 ID。

#### 2. 配置 OpenAI (AI Summarize 节点)
- 双击 **AI Summarize (OpenAI)** 节点。
- 在 **Credentials** 下拉框中选择 **Create New**。
- 填入你的 OpenAI API Key。
- (可选) 在 Model 中选择你偏好的模型 (默认 gpt-4o-mini)。

#### 3. 配置邮件发送 (Send Email 节点)
- 双击 **Send Email** 节点。
- **From Email**: 发件人邮箱 (需要在 n8n 中配置 SMTP 凭证)。
- **To Email**: 接收日报的邮箱地址。
- **Credentials**: 选择或新建 SMTP 凭证 (支持 Gmail, Outlook 等)。

## 🔍 测试运行
1. 点击编辑器底部的 **Execute Workflow** 按钮。
2. 观察各个节点的执行状态。
3. 检查你的邮箱是否收到了生成的日报。

## ⚠️ 常见问题
- **抓取失败 (403/429 Error)**: 通常是 RSSHub 实例被目标网站限制。尝试更换 RSSHub 实例或配置代理。
- **内容为空**: 可能是过去 24 小时内没有新动态，或者 RSS 解析失败。检查 Filter 节点的输出。
