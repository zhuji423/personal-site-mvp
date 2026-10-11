---
title: "Comate Docs"
description: "Use when the user asks how to use Comate (百度 AI 编程智能体), needs up-to-date documentation from the internal knowledge base, wants to understand Comate's Agent modes/Skills/Context system/MCP/CLI, or seeks guidance on models, billing, or troubleshooting. Load reference files only as supplementary context."
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\comate-docs-comate\\SKILL.md"
name: "comate-docs"
---

# Comate Docs

## Quick Start

## 前置依赖

- **Skill 依赖 `get-ugate-token`**：认证通过 get-ugate-token skill 自动获取个人身份 token
- **Skill 依赖 `ku-operator`**：通过 ku-operator 的 query-content 能力获取文档内容
- **当前用户名**: ${COMATE_USERNAME}，即`COMATE_USERNAME=${COMATE_USERNAME}`

## 质量原则

- 必须以知识库实时内容为准。
- 回答时引用具体页面 URL，用户通过 URL 连接可以直接进入页面

## Comate Product Snapshot

1. **Agent 模式（One Agent, Three Modes）**：Agent（直接生成实现，默认模式）、Ask（只读问答/解释）、Plan（复杂任务先规划再执行，含澄清和 Human-in-the-loop 审核）；Shift+Tab 快速切换
2. **Context 系统**：Skills（可移植技能包）、Subagents（并行子智能体，内置 Explore Agent）、Rules（项目/个人规范）、Commands（`/` 指令，内置 `/code-review`、`/debug`、`/unit-test`）、MCP（Model Context Protocol，渐进式加载）、`@` 关联上下文（File/Folder/Terminal/Doc/Rules）
3. **并行执行**：工具级 + Subagent 级并行；Explore Agent 作为 SubAgent 多步推理检索代码库
4. **Skills 市场**：内置 `/find-skills` 指令，从远端 Skills 中心搜索并安装 skill；内置 `/create-skill` 一键创建项目级或个人级 skill
5. **Zulu CLI**：命令行工具，可在终端、iPipe CI/CD 流水线中运行 Comate Agent
6. **Jinx Code**：Web 端 Vibe Coding 产品，云端沙盒执行，网址 `https://web-agent-next.baidu-int.com/`
7. **MCP 渐进式加载**：以 MCP Server 为粒度按需加载工具定义，大幅节省上下文 Tokens；支持 MCP 市场 UI 一键添加
8. **兼容性**：兼容 Claude Code、Codex、Cursor 等 20+ Agent 工具的 Skills 目录格式
9. **自动化**：Hooks 可插拔扩展能力
10. **模型管理**：支持在设置页面启用/禁用模型，过滤出你需要的模型列表
11. **新增功能**：Checkpoints（Agent 变更自动快照，随时回滚）、并行 Tab（多标签页并行任务）、代码审查界面（diff 格式逐块接受/撤销）
12. **Copet**：MacOS 桌面宠物应用，任务执行时可视化状态
13. **Mission Mode**：以任务为中心的研发模式（仅 Comate AI IDE）；支持多任务并行（独立上下文）、多代码库联动（一个 Workspace 绑定多个仓库）、工作流全程串联（自动绑卡/提交/发起 CR）

## Content retrieve

示例命令，只需替换对应文档的 url 即可
`
cd ${COMATE_SKILL_DIR}/../ku-operator-comate && COMATE_USERNAME=${COMATE_USERNAME} python3 scripts/ku_operator.py query-content --url "https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/jyGhbHUQQG/WBcj3KdE3ATpQR"
`


## Workflow

1. 明确用户问题属于哪个类别：功能使用、模型选择/计费、Skills/Context、CLI、故障排除、最新动态。
2. 按需加载 `references/` 中对应的参考文件（见下方 Reference Map）。
4. 综合文档内容和参考文件回答，并给出知识库页面链接作为引用。

## Doc Map

所有页面均在同一知识空间，基础路径：`https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/jyGhbHUQQG`

| 章节                        | URL 页面 ID | 说明                        |
|---------------------------|------------------|---------------------------|
| 知识库首页/目录                  | `WBcj3KdE3ATpQR` | 11 个顶级章节的总目录              |
| 开始使用                      | `CAu-Eo5qijd3xY` | 开始使用章节入口                  |
| 开始使用 > 快速开始               | `KhrgIWkjEkRdA3` | 安装、模型列表（含 Tokens 倍数）、快速上手 |
| 开始使用 > 概念                 | `SjueaOAs7omDOW` | Tab/Agent/Mode/Skills/Rules/Subagents/@ / 概念词汇 |
| 开始使用 > 功能使用手册             | `byA0I1Gd9YAt_t` | 功能使用详细说明                  |
| 开始使用 > 模型                 | `SRSExwbEp2FHVf` | 所有模型属性详情页                 |
| Mission Mode                | `TboTJTD5shkc7p` | 以任务为中心的研发模式（仅 Comate AI IDE）；多任务并行/多代码库联动/工作流全程串联 |
| Mission Mode 使用手册           | 独立路径 `https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/mcV1ZM02Cz/laPtUbdW5yJsbo` | 完整操作手册：5步快速上手、Workspace 配置、三大核心能力详解 |
| Agent                     | `rEVzf39R6KVKXM` | Agent 章节入口                |
| Agent > 概述                | `eOPhb1KxQEXmfl` | Agent 工作原理、工具列表、消息压缩、Checkpoints、并行 Tab |
| Agent > 模式（Mode）          | `NYGrqnNt_A8Y0g` | Agent/Ask/Plan 三种模式详解及切换方式 |
| Agent > 审查（Review）        | `x2I2B2sbqLPtSl` | diff 审查界面、逐块接受/撤销、/code-review 命令 |
| Agent > 安全性               | `90BNp3Z4eV4XuI` | 安全性说明                     |
| Model                     | `14-z1y4EdPxllF` | Model 章节入口（模型选择）          |
| Model > 查询可用模型列表          | `ZS3uu0XgQjLm31` | 输入代码库地址查询可用模型             |
| Model > 看不到外部模型怎么办        | `IhV9oBqa4VrEcR` | 6步排查：账号/资源账户/代码库密级/Workspace类型/版本/Reload |
| Context                   | `Pn9zCxdoUeQ-SC` | Context 章节入口              |
| Context > Skills          | `BAD2sU4Yqs1kCP` | Skills 完整说明：格式、目录、/create-skill、/find-skills |
| Context > Subagents       | `4HSaAXnNTSW1fX` | Subagents 说明：内置 Explore Agent、自定义 Subagent 格式 |
| Context > @关联上下文          | `9ZnJeejauIRvTk` | @ 快捷键：File/Folder/Terminal/Doc/Rules |
| Context > Semantic Search | `4QvLhmceIx4I9O` | 语义检索说明                    |
| Context > Commands        | `nLF-end9lwqeej` | / 命令说明：内置 /code-review、/debug、/unit-test |
| Context > MCP             | `t0diKSjnMyiFEG` | MCP 配置（个人/项目级）、MCP 市场 UI、手动配置 |
| Context > Rules           | `KmCRxSZy1wGkeh` | Rules 格式与配置说明             |
| 自动化                       | `TFK964x5GaGnOd`    | 自动化 章节入口                  |
| 自动化 > Hooks               | `SsPwYQyvQxdGeb`    | Hooks                     |
| 账户                        | `XOEDtioqXFa5zg` | 账户章节入口                    |
| 使用账单（账户子页）                | `cMPrc68gwEX1Hs` | 多模型列表、按 Token 计价、资源账户绑定   |
| 数据度量（账户子页）                | `iSLaMIFKeD7Pmy` | 个人/团队 Coding Agent 使用数据视图 |
| 故障排除                      | `sEQ16HgwkyDc_H` | 故障排除章节                    |
| 故障排除 > Comate常见问题         | `4goStF_n2tJpsB` | 常见问题                      |
| Changelog                 | `6Ft3QPJ87cXqek` | 版本更新历史                    |
| 周边生态                      | `XLL_Zhb2ruCp4l` | 周边生态章节入口                  |
| Zulu CLI（周边生态子页）          | `amicnOzxkkzxiQ` | CLI 安装、参数、iPipe 用法、Docker 镜像 |
| Jinx Code（周边生态子页）         | `jor-aKcmbLwRKv` | Web 端云沙盒 Vibe Coding 产品介绍 |
| Copet（周边生态子页）             | `z7z8_oXn5YP8rt` | MacOS 桌面宠物应用，任务执行状态可视化    |
| 团队动态                      | `9y6h0rTC3Bdg8V` | 团队动态章节入口                  |
| 【动态】Comate 4.0 升级情况       | `Hb6OQz5Jc7/mhBWPhoBv258Ve` | 4.0 架构详解、SWE-Bench 评分、使用数据分析 |
| 【动态】Comate上下文重磅升级         | `9k-K32PXRHIycf` | Explorer Agent 升级、CodebaseSearch 全链路升级 |
| 【动态】模型管理功能上线              | `Wxf9N2-pqP8GKf` | 新增模型管理页面，支持启用/禁用模型        |
| 【动态】Comate正在和将来的Feature   | `VFcMaO6en_p8jJ` | Comate 近期和规划中的功能动态        |
| 【实践】打通如流知识库               | `Nrj3-AWvt1DPt-` | 使用 ku-doc-manage Skill 直接读写知识库文档 |
| 【实践】内网资源大集合               | `Np0ZvForjkgRBz` | baidu-intranet-access Skill 安装和使用指南 |
| 【实践】拆卡提码一条龙               | `hbAL01OPSL9LMU` | create-cr Skill：从 PRD 建 iCafe 卡片到提交代码 |
| 【实践】让Comate做代码「尸检」        | `Z0TRY_G1wG2s2v` | 代码 post-mortem 实践         |
| 【研究】MCP 渐进式加载             | `EpzgIaNtaVAHf-` | MCP 上下文优化原理，对比 Claude Code、Cursor 方案 |

## Reference Map

按需读取，不要一次性全部加载：

- `references/product-overview.md` → 产品架构、模式说明、Context 系统、并行执行机制
- `references/models-and-billing.md` → 支持的模型列表、按密级的模型权限、计费规则
- `references/doc-map-extended.md` → 完整 URL 索引（含所有已知子页面）
