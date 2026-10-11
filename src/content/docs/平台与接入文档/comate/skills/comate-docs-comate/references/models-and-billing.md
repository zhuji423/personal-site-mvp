---
title: "Comate 模型列表与计费"
description: "辅助参考文件。模型上线情况随产品迭代变化，以知识库「使用账单」页面和「开始使用 模型」页面的实时内容为准。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\comate-docs-comate\\references\\models-and-billing.md"
---
# Comate 模型列表与计费

> 辅助参考文件。模型上线情况随产品迭代变化，以知识库「使用账单」页面和「开始使用 > 模型」页面的实时内容为准。

## 模型选择与管理

- **Models 管理页面**：可启用/禁用不需要的模型，过滤出你常用的列表；修改后需 Reload 或 Restart IDE 生效
- **Auto 模式**：根据用户 Query 自动选择最合适的模型（推荐日常使用）
- **切换路径**：打开 Agent → 模型下拉选择
- 看不到某些模型？参考「Model > 看不到外部模型怎么办」：登录账号、关联资源账户、检查代码库密级、Workspace 类型、版本更新、Reload IDE

## 按代码库密级的模型权限

| 密级 | 是否允许海外模型 | 说明 |
|------|-----------------|------|
| 保密 L1 / 个人库 / GitHub 代码库 | ❌ | 仅可使用国内模型 |
| 保密 L0 / 开源库 / 三方库 / 基础库 | ✅ | 国内 + 海外模型均可用 |
| 纯目录（无 .git 或非保密） | ✅ | 国内 + 海外模型均可用 |

> 未绑定资源账户的用户无法使用海外模型。绑定入口：`https://oneapi-comate.baidu-int.com/mine`

## 当前可用模型列表

> 以知识库「开始使用 > 快速开始」和「开始使用 > 模型」页面为准，下表为最新快照。

### 海外模型（需 L0/开源/纯目录 + 已绑资源账户）

| 模型 | 默认上下文 | 简介 | Tokens 倍数 | 功能 |
|------|-----------|------|------------|------|
| Claude Opus 4.6 | 200k | 最强大的模型，适合解决高难编码任务 | 1.6x | Thinking、Image |
| Claude Opus 4.5 | 200k | 面向深度编码与复杂问题求解的高性能模型 | 1.6x | Thinking、Image |
| Claude Sonnet 4.6 | 200k | Claude 系列最新模型，编码任务性能卓越 | 1x | Thinking、Image |
| Claude Sonnet 4.5 | 200k | 在性能与成本之间保持较好平衡，适合复杂任务处理 | 1x | Thinking、Image |
| Claude Haiku 4.5 | 200k | 面向简单任务的高效模型，响应速度快 | 0.3x | Thinking、Image |
| Gemini 3.1 Pro | 200k | Google 最新旗舰模型，非常适合日常使用 | 0.45x | Thinking、Image |
| Gemini 3.0 Pro | 200k | 高级通用模型，适合复杂问题和 Web 页面开发 | 0.45x | Thinking、Image |
| Gemini 3.0 Flash | 200k | 低延迟与高效率，适合高并发或实时场景 | 0.3x | Thinking、Image |
| GPT-5.2 Codex | 200k | 适合复杂、长时间运行的编码任务 | 1x | Thinking、Image |
| GPT-5.3 Codex | 272k | OpenAI 最新的编程模型，适合高难度编程任务 | — | Thinking、Image |
| GPT-5.4 | 272k | OpenAI 最新旗舰模型，适合复杂任务 | — | Thinking、Image |

### 国内模型（所有密级可用）

| 模型 | 默认上下文 | 简介 | Tokens 倍数 | 功能 |
|------|-----------|------|------------|------|
| MiniMax M2.5 | 200k | 兼具编码能力、数据处理和复杂问题分解，速度极快 | 0.2x | Thinking |
| MiniMax M2.7 | 200k | 强化复杂工程系统深层理解和编码，善于调度多 Agent 协作 | — | Thinking |
| Kimi K2.5 | 200k | 原生多模态模型，长文本理解与多类型输入表现突出 | 0.2x | Thinking、Image |
| GLM-4.7 | 200k | 适用于复杂推理、代码理解等场景，能力均衡 | 0.2x | Thinking |
| GLM-5 | 200k | 适合复杂、长时间运行的编码任务 | 0.3x | Thinking |
| GLM-5-Turbo | 200k | 对复杂、长链路指令理解更强，提升大量 Skills 下精准识别准确度 | — | Thinking |

> 以上 Tokens 倍数为相对费用参考，以知识库实时价格为准。

## 使用额度

| 用户类型 | 额度 |
|----------|------|
| 无资源账户 | 全局总计 600元 |
| 有资源账户 | 每人每月 1500元 |

- 资源账户绑定/提额入口：`https://oneapi-comate.baidu-int.com/mine`
- 注意：未绑定资源账户的用户无法使用海外模型

## Zulu CLI 额度

| 用户类型 | 额度 |
|----------|------|
| 有资源账户 | 每人每月 5000 requests |
| 无资源账户 | 全局总计 2000 requests |
