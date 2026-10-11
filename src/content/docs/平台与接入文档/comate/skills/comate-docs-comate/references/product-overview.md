---
title: "Comate 产品概览"
description: "辅助参考文件，以知识库实时内容为准。当前快照反映 Comate 4.x（2026年4月）情况。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\comate-docs-comate\\references\\product-overview.md"
---
# Comate 产品概览

> 辅助参考文件，以知识库实时内容为准。当前快照反映 Comate 4.x（2026年4月）情况。

## 产品定位

Comate（内部研发代号 Zulu）是百度内部 AI 编程智能体，基于 VSCode IDE 插件形态，支持厂内部署、SaaS、VPC 等多种环境，面向研发全流程提供 AI 辅助。支持 VSCode、JetBrains 系列、Android Studio、Xcode、Visual Studio 多个 IDE，以及专属 Comate AI IDE。

## 核心架构：One Agent, Three Modes

| 模式 | 英文 | 适用场景 |
|------|------|----------|
| 智能体模式 | Agent | 复杂任务：自主探索代码库、多文件编辑、运行命令（默认模式） |
| 只读问答模式 | Ask | 代码解释、问题解答，不做任何文件修改 |
| 计划模式 | Plan | 先分析代码库、提出澄清性问题、生成可编辑计划，再执行 |

按 `Shift+Tab` 快速切换模式。

## Agent 核心能力

- **工具**：读取文件、搜索文件、编辑文件、运行 Shell 命令、语义搜索、网络检索、调用子代理等
- **Checkpoints**：Agent 变更自动快照，随时通过 `Restore Checkpoint` 按钮回滚，本地存储、独立于 Git
- **并行 Tab**：多标签页并行执行不同 Agent 任务，每个 Tab 独立上下文和会话历史
- **消息压缩**：对话变长时自动生成摘要，也支持手动触发内容总结
- **代码审查界面**：Agent 生成的变更以 diff 格式展示，支持逐块保留/撤销；内置 `/code-review` 命令让 Agent 提出改进建议

## Context 系统

### Skills

- **定义**：可移植、受版本控制的技能包，每个 Skill 是一个包含 `SKILL.md` 的文件夹
- **自动加载目录**：
  - 项目级：`.agents/skills/` 或 `.comate/skills/`
  - 个人级（全局）：`~/.comate/skills/`
- **发现与安装**：在 Comate 输入框输入 `/find-skills`，从远端 Skills 市场搜索并安装
- **创建**：使用内置 `/create-skill` 指令，支持项目级或个人级
- **兼容**：同时兼容 `.claude/skills/`、`.codex/skills/`、`~/.claude/skills/` 等目录

### Subagents

- 并行执行子任务的独立 Agent 实例，每个 Subagent 有自己独立的上下文窗口
- **内置 Explore Agent**：专为代码库探索而生，多步推理、并行工具调度，最终返回带精确文件路径的结构化回答；作为 SubAgent 运行，不污染主 Agent 上下文
- **自定义 Subagent**：在 `.comate/agents/`（项目级）或 `~/.comate/agents/`（个人级）定义带 YAML 头的 Markdown 文件

### Rules

- 项目或个人级编码规范文件，定义 Agent 行为（代码规范、框架偏好、项目约定）
- 支持通过 `/create-skill` 将已有 Rules 迁移为 Skills

### Commands

- 使用 `/` 在输入框中调用
- **内置命令**：`/code-review`、`/debug`、`/unit-test`（系统级，预计开放自定义）
- **Skill 调用**：`/find-skills`、`/create-skill` 等

### MCP（Model Context Protocol）

- 支持自定义安装 MCP Server，连接外部工具
- **MCP 市场 UI**：在 Comate 页面点击 MCP 选项，通过市场一键添加或手动配置
- **渐进式加载**：以 MCP Server 为粒度按需加载，避免全量 400+ 工具塞满上下文
- **配置方式**：个人级（`~/.comate/mcp.json`）或项目级（`.comate/mcp.json`）
- 支持 STDIO、SSE、Streamable HTTP 三种传输类型

### @ 关联上下文

- 使用 `@` 在输入框中关联 File、Folder、Terminal、Doc、Rules 等上下文
- 支持 `/` 和 `@` 多选搭配

### Semantic Search

- 全代码库语义检索，支持精准定位相关代码片段；秒级索引构建和检索
- 结合 Explore Agent 实现 Agentic Search（多步推理检索）

## 模型管理

- **Models 管理页面**：可启用/禁用模型，过滤出你需要的模型列表
- 修改后需 Reload 或 Restart IDE 生效
- **常见问题**：看不到外部模型 → 参考「Model > 看不到外部模型怎么办」6步排查

## 并行化策略

| 级别 | 说明 |
|------|------|
| 工具级并行 | 同一轮推理中多个工具并发调用 |
| Subagent 级并行 | 多个子 Agent 并发执行不同子任务 |
| 并行 Tab | 多标签页同时运行不同 Agent 对话 |

## 周边生态

- **Zulu CLI**：命令行工具，可在终端、iPipe CI/CD 流水线中运行 Comate Agent
- **Jinx Code**：Web 端 Vibe Coding，云端沙盒执行，网址 `https://web-agent-next.baidu-int.com/`
- **Copet**：MacOS 桌面宠物应用（v1.1+），任务执行时动画展示工作状态，多角色可选

## Mission Mode（仅 Comate AI IDE）

以任务为中心的研发模式，理念：让任务成为工程活动的基本单元，AI 围绕任务推进而非围着代码转。

| 特性 | Code Mode（传统） | Mission Mode |
|------|----------------|--------------|
| 关注点 | 代码写了什么 | 任务完成到哪了 |
| AI 角色 | 帮你补几行代码 | 围绕任务自主推进全流程 |
| 基本单元 | 文件/分支/PR | 任务 |

### 三大核心能力

1. **多任务并行**：同一工作区同时跑多个任务，每个任务独立上下文互不干扰
2. **多代码库联动**：一个 Workspace 绑定多个代码仓库，AI 自动感知跨库依赖
3. **工作流全程串联**：任务完成自动生成 commit message 并绑卡提交、发起 iCode CR

**入口页面**：`https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/jyGhbHUQQG/TboTJTD5shkc7p`
**完整手册**：`https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/mcV1ZM02Cz/laPtUbdW5yJsbo`

## 性能数据（4.0，2026年3月）

- SWE-Bench 评分稳定在 70 分以上
  - GLM-5：Comate（76.4）> Claude Code（72.5）
  - GLM-4.7：Comate（71.3）> Claude Code（70.7）
- 周活跃用户 > 1万，人均 Query 次数 > 38
- 线上任务采纳率 94.06%
