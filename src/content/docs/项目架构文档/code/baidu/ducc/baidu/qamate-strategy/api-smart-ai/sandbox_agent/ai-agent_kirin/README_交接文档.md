---
title: "AI-Agent_Kirin 项目交接文档"
description: "基于 Kirin 平台 + E2B 沙箱 + DuccClaude 的 ITP 智能问答 Agent"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\qamate-strategy\\api-smart-ai\\sandbox_agent\\ai-agent_kirin\\README_交接文档.md"
---
# AI-Agent_Kirin 项目交接文档

> 基于 Kirin 平台 + E2B 沙箱 + Ducc(Claude) 的 ITP 智能问答 Agent

---

## 1. 项目概述

### 1.1 项目定位

本项目是一个部署在 **Kirin 平台** 上的 AI Agent，主要服务于 **ITP（Interface Test Platform）平台**，提供：

- **用户答疑**：回答平台使用、接入、操作等问题
- **问题排查**：通过日志、数据库分析定位用户遇到的问题
- **数据统计**：协助用户进行数据库查询和统计分析

### 1.2 核心架构

```
┌─────────────────────────────────────────────────────────────────┐
│                        Kirin 平台                                │
│  ┌─────────────┐                                                │
│  │   main.py   │  ← 入口，接收 Kirin 任务参数                    │
│  └──────┬──────┘                                                │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────────┐                                           │
│  │ SandboxDemoAgent │  ← 管理沙箱生命周期、上传代码、执行任务     │
│  └────────┬─────────┘                                           │
│           │                                                      │
└───────────┼──────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     E2B 沙箱环境                                  │
│  ┌─────────────┐      ┌─────────────────────────┐               │
│  │   task.py   │ ───▶ │    Ducc (Claude CLI)    │               │
│  └─────────────┘      └───────────┬─────────────┘               │
│                                   │                              │
│                    ┌──────────────┼──────────────┐               │
│                    ▼              ▼              ▼               │
│              ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│              │database- │  │  log-    │  │ qerag-   │           │
│              │ helper   │  │ helper   │  │ helper   │           │
│              └──────────┘  └──────────┘  └──────────┘           │
│                          Skills 技能                             │
└─────────────────────────────────────────────────────────────────┘
```

### 1.3 技术栈

| 组件 | 说明 |
|------|------|
| Python 3.11+ | 主语言 |
| qep-ai-agent | 百度内部 AI Agent SDK |
| e2b | 沙箱环境 SDK（百度定制版） |
| claude-agent-sdk | Ducc/Claude CLI 的 Python SDK |
| qep-delivery-data | 百度内部数据工具 SDK |
| qep-delivery-component | 百度内部组件 SDK |

---

## 2. 目录结构

```
ai-agent_kirin/
├── main.py                      # 入口文件，Kirin 调用的主程序
├── workspace/                   # 本地工作目录（可忽略）
├── output/                      # 输出目录
└── agents/
    ├── __init__.py
    ├── requirements.txt         # 主依赖（Kirin 环境）
    ├── build_for_kirin.sh       # 打包部署脚本
    ├── sandbox_agent_demo.py    # 沙箱 Agent 核心实现
    ├── ducc_agent_demo.py       # Ducc Agent 示例
    ├── deepseek_agent_demo.py   # DeepSeek Agent 示例
    ├── infoflow_agent_demo.py   # 如流 Agent 示例
    ├── testone_agent_demo.py    # TestOne Agent 示例
    └── sbx_code/                # 【核心】部署到沙箱内的代码
        ├── task.py              # 沙箱内执行的主脚本
        ├── requirements.txt     # 沙箱内的依赖
        ├── claude-skills.zip    # Skills 打包文件（自动生成）
        └── .claude/             # Ducc 配置目录
            ├── CLAUDE.md        # Agent 人设 & 指令配置
            └── skills/          # 自定义技能
                ├── database-helper/  # 数据库查询技能
                ├── loger-helper/     # 日志查询技能
                ├── qerag-helper/     # RAG 知识库查询技能
                └── doc-helper/       # 文档处理技能
```

---

## 3. 核心文件说明

### 3.1 main.py - 入口文件

**作用**：Kirin 平台调用的入口，负责：
1. 解析 Kirin 传入的参数
2. 初始化 Agent 并执行
3. 将结果回调给 Kirin

**关键配置**（需要修改的地方）：

```python
# 运行模式：OFFLINE=本地调试，ONLINE=生产环境
RUN_MODE = 'OFFLINE'

# TestOne 账号（用于 SDK 调用）
TESTONE_USERNAME = 'yangdeqian'
TESTONE_TOKEN = 'xxxx'

# Kirin 账号
KIRIN_USERNAME = "yangdeqian"
KIRIN_TOKEN = "xxxx"

# 沙箱配置
os.environ["E2B_API_KEY"] = "xxxx"
os.environ["E2B_DOMAIN"] = "agent-sandbox.baidu-int.com"
SBX_TEMPLATE = "Amy数字员工"  # 沙箱镜像模板名称
```

### 3.2 sandbox_agent_demo.py - 沙箱 Agent

**作用**：管理沙箱的完整生命周期

**核心方法**：

| 方法 | 说明 |
|------|------|
| `execute()` | 执行入口，调用沙箱执行任务 |
| `before_execute_in_sandbox()` | 沙箱执行前准备：上传代码、安装依赖 |
| `after_execute_in_sandbox()` | 沙箱执行后清理 |

**工作流程**：
1. 获取或复用沙箱实例
2. 上传 `claude-skills.zip` 和 `task.py`
3. 安装依赖环境
4. 在沙箱内执行 `task.py`

### 3.3 task.py - 沙箱内任务脚本

**作用**：在沙箱内实际干活的脚本，负责：
1. 初始化环境变量
2. 调用 Ducc (Claude CLI) 执行用户查询
3. 处理消息流，区分推送到 TestOne 和如流的内容
4. 上传产出文件到 BOS

**关键类**：

```python
class MyDuccUtil(DuccUtil):
    """
    自定义消息处理
    - 通过 '----回复----' 分隔符区分中间过程和最终结论
    - 分隔符之前：只推送到 TestOne
    - 分隔符之后：推送到 TestOne + 如流
    """

class Processor:
    """
    任务处理器
    - 支持多轮对话（session 复用）
    - 产出文件自动上传 BOS
    """
```

### 3.4 CLAUDE.md - Agent 人设配置

定义了 Ducc 的角色和行为规范：
- Agent 身份：ITP 平台负责人
- 可用技能：database-helper、log-helper、qerag-helper、doc-helper
- 问题处理流程和输出规范

---

## 4. Skills 技能说明

| 技能 | 作用 | 使用场景 |
|------|------|----------|
| **database-helper** | 查询 ITP 数据库 | 根据链接查 trace_id、用例详情等 |
| **loger-helper** | 查询 EP 日志 | 根据 trace_id 查错误日志 |
| **qerag-helper** | 查询 RAG 知识库 | 常见问题解答、平台文档查询 |
| **doc-helper** | 文档处理 | 将分析结果写入在线文档 |

---

## 5. 使用指南

### 5.1 本地调试

1. **安装依赖**：
```bash
pip install -r agents/requirements.txt
```

2. **修改配置**：
   - 确保 `main.py` 中 `RUN_MODE = 'OFFLINE'`
   - 配置好 TestOne、Kirin、E2B 的账号信息

3. **修改测试问题**：
```python
# main.py 中的 main() 函数
question = r"你的测试问题"
```

4. **运行**：
```bash
python main.py
```

### 5.2 打包部署

```bash
cd ai-agent_kirin
sh agents/build_for_kirin.sh
```

**脚本执行的操作**：
1. 打包 `.claude/` 目录为 `claude-skills.zip`
2. 复制代码到 `output/ai-agent/`
3. 安装依赖 SDK 到 output 目录
4. 修改 `RUN_MODE` 为 `ONLINE`
5. 打包成 `ai-agent.zip`
6. 上传到 Kirin 平台

### 5.3 新增/修改 Skill

1. 在 `agents/sbx_code/.claude/skills/` 下创建新目录
2. 创建 `SKILL.md` 定义技能说明
3. 创建 `scripts/` 目录放置脚本
4. 在 `CLAUDE.md` 中添加技能说明
5. 重新打包部署

---

## 6. 环境变量清单

### 6.1 Kirin 环境（main.py）

| 变量 | 说明 |
|------|------|
| `E2B_API_KEY` | 沙箱 API Key |
| `E2B_DOMAIN` | 沙箱域名 |

### 6.2 沙箱环境（task.py init_env）

| 变量 | 说明 |
|------|------|
| `BAIDU_CC_PLATFORM_TOKEN` | Ducc 平台 Token |
| `BAIDU_CC_PLATFORM` | Ducc 平台名称 |
| `BAIDU_CC_USERNAME` | Ducc 用户名 |
| `ANTHROPIC_MODEL` | 使用的模型 |
| `ANTHROPIC_AUTH_TOKEN` | 模型 API Token |
| `DB_HELPER_*` | 数据库连接配置 |
| `TESTONE_*` | TestOne 账号配置 |
| `KIRIN_*` | Kirin 账号配置 |
| `APP_KEY` / `APP_SECRET` | 如流机器人配置 |

---

## 7. 常见问题

### Q1: 沙箱环境准备失败
- 检查 `E2B_API_KEY` 是否正确
- 检查沙箱模板 `SBX_TEMPLATE` 是否存在

### Q2: Ducc 执行报错
- 检查 `ANTHROPIC_AUTH_TOKEN` 是否有效
- 检查沙箱内网络是否能访问模型服务

### Q3: 消息没有推送到如流
- 确保最终回复前有 `----回复----` 分隔符
- 检查 `APP_KEY` 和 `APP_SECRET` 配置

### Q4: 产出文件没有上传
- 确保文件名格式为 `{USERNAME}#{TASK_ID}#{RECORD_ID}#{fileName}`
- 检查文件是否在 `/workspace/output` 目录下

---

## 8. 相关链接

| 资源 | 链接 |
|------|------|
| Kirin 平台 | http://kirin.baidu-int.com |
| TestOne 平台 | https://testone.baidu-int.com |
| ITP 平台 | https://console.cloud.baidu-int.com/itp |
| EP 日志平台 | https://neweplog.baidu-int.com |
| 在线文档 | https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/rXPeyrumXw/JS-fABpV_ikpYJ |

---

## 9. 维护者

- 原作者：yangdeqian
- 创建时间：2026/01

---

*最后更新：2026-03-27*
