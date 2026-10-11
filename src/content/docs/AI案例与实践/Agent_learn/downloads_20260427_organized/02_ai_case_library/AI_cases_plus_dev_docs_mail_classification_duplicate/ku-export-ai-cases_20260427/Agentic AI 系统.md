---
title: "复制配置模板"
description: "Agentic AI 系统"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Agentic AI 系统.md"
---
Agentic AI 系统

#### 🧑‍🏫 案例作者：[@徐梁攀](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：全流程、开发、模型
#### 🔧 使用工具：Deepseek、其他
#### 📒 案例概要：一个 边做边学（Learn by Building） 的本地 AI Agent 项目，使用 Go 从零实现一个可持续进化的 Agentic AI 系统。
项目地址：[https://console.cloud.baidu-int.com/devops/icode/repos/baidu/personal-code/Agentic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/personal-code/Agentic)

一个 **边做边学（Learn by Building）** 的本地 AI Agent 项目，使用 **Go** 从零实现一个可持续进化的 Agentic AI 系统。

本项目的核心目标不是"调用一个大模型聊天"，而是：

> **通过亲手构建 Agent，系统性学习 AI / LLM / Agentic AI 的核心原理与工程实践。**
---

## ✨ 项目特性
* 🧠 **Agent 而非 ChatBot**：具备状态、规划与执行能力
* 📚 **学习驱动**：以"学习目标"为输入，自动拆解并执行
* 📝 **长期记忆（Memory）**：本地持久化 + 向量检索（RAG）
* 🔧 **Tool Calling**：LLM 自主决策调用工具
* 🎯 **Skills 系统**：可扩展的高阶能力单元，支持复杂工作流编排
* 🔌 **MCP 集成**：支持 Model Context Protocol，可扩展外部工具
* 📊 **结构化日志**：完整的日志系统，可追踪执行流程
* 🧱 **工程化结构**：模块清晰，可持续扩展
* 💻 **本地运行**：CLI 形式，无依赖复杂平台

---

## 🎯 项目愿景
随着 Agentic AI 成为 AI 系统的重要形态，本项目希望解决一个真实问题：

> **工程师如何高效、可验证、可沉淀地学习 AI？**
答案是：

* 不先“学完再做”
* 而是 **让 Agent 成为学习过程本身的一部分**

最终获得的不是笔记，而是：

* 一个真实可运行的 Agent
* 一套 AI 工程方法论
* 可复用、可展示的技术资产

---

## 🏗️ 系统架构
```
User (CLI)
   ↓
Agent Orchestrator
   ├── Skills Registry (高阶能力路由)
   │     ├── DeepLearning Skill (系统化学习)
   │     ├── GitReport Skill    (Git日报生成)
   │     └── Configurable Skill (配置驱动)
   ├── Planner        (学习任务拆解)
   ├── Memory         (长期记忆 + RAG)
   ├── Tool Registry  (本地工具 + MCP 工具)
   │     ├── Memory Tools (write_memory, list_memory)
   │     └── MCP Tools    (filesystem, etc.)
   ├── MCP Manager    (外部工具协议)
   └── LLM Client     (模型调用 + 工具调用循环)
```
---

## 📁 项目结构
```
Agentic/
├── cmd/agentic/main.go              # CLI 入口点
├── internal/
│   ├── agent/
│   │   ├── orchestrator.go          # Agent 编排器（核心调度中心）
│   │   └── planner.go               # 学习任务规划
│   ├── llm/
│   │   ├── client.go                # LLM 客户端（支持工具调用循环）
│   │   ├── embedding.go             # 嵌入服务
│   │   └── models.go                # 数据模型
│   ├── memory/
│   │   ├── manager.go               # 记忆管理器
│   │   ├── storage.go               # 存储抽象
│   │   └── vector_db.go             # 向量检索
│   ├── skills/
│   │   ├── skill.go                 # Skill 接口定义
│   │   ├── base.go                  # BaseSkill（默认实现）
│   │   ├── registry.go              # Skill 注册中心
│   │   ├── configurable.go          # 配置驱动的 Skill
│   │   ├── deeplearning.go          # 深度学习 Skill
│   │   └── gitreport.go             # Git 日报 Skill
│   ├── tools/
│   │   ├── registry.go              # 工具注册中心
│   │   ├── memory_tools.go          # 记忆工具
│   │   └── mcp_adapter.go           # MCP 工具适配器
│   ├── mcp/
│   │   ├── client.go                # MCP 客户端
│   │   ├── manager.go               # MCP 服务器管理
│   │   ├── protocol/
│   │   │   ├── jsonrpc.go           # JSON-RPC 2.0 协议
│   │   │   └── tools.go             # MCP 工具定义
│   │   └── transport/
│   │       ├── transport.go         # 传输接口
│   │       └── stdio.go             # Stdio 传输实现
│   ├── logger/                      # 日志系统
│   │   └── logger.go                # 结构化日志（支持组件级日志）
│   └── config/
│       ├── config.go                # 配置管理（TOML 解析）
│       └── validation.go            # 配置验证
├── pkg/
│   ├── types/                       # 公共类型定义
│   └── utils/
│       └── similarity.go            # 余弦相似度计算
├── test/                            # 测试文件
│   ├── config_test.go
│   ├── llm_test.go
│   ├── mcp_integration_test.go
│   └── skills_test.go               # Skills 系统测试
├── config/
│   ├── config.toml                  # 配置文件
│   └── config.toml.example          # 配置模板
├── scripts/
│   ├── setup.sh                     # 环境设置
│   └── check_structure.sh           # 结构检查
└── data/
    └── memory.json                  # Agent 的"第二大脑"
```
---

## 🚀 快速开始
### 1️⃣ 环境准备
* Go 1.25
* LLM API Key（支持 OpenAI / DeepSeek 等）
* Node.js（可选，用于 MCP 服务器）
* Ollama（可选，用于本地 Embedding）

### 2️⃣ 配置
```
# 复制配置模板
cp config/config.toml.example config/config.toml

# 编辑配置文件
vim config/config.toml
```
**配置示例：**

```
# LLM 设置
[llm]
model = "deepseek-chat"
base_url = "https://api.deepseek.com"
api_key = "your_api_key"

# Embedding 设置（本地 Ollama）
[embedding]
model = "bge-m3"
base_url = "http://localhost:11434/v1"
api_key = "ollama"

# Agent 设置
[agent]
system_prompt = "你是一个有用的 AI 学习助手。请使用中文回答所有问题。"
max_tool_call_round = 10

# 记忆设置
[memory]
file_path = "data/memory.json"
top_k = 5

# MCP 配置
[mcp]
enabled = true

# 文件系统 MCP 服务器
[[mcp.servers]]
name = "filesystem"
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/your/workspace/path"]
```
也可以通过环境变量覆盖配置：

```
export LLM_API_KEY=your_api_key
export LLM_BASE_URL=https://api.deepseek.com
```
**Skills 配置：**

```
# Skills 系统配置
[skills]
enabled = true

# 配置驱动的 Skill 示例
[[skills.configurable]]
name = "code_review"
description = "代码审查助手"
keywords = ["审查", "review", "检查代码"]
system_prompt = "你是一个严谨的代码审查专家..."
tools = ["mcp_filesystem_read_file", "mcp_filesystem_list_directory"]
```
**日志配置：**

```
# 日志设置
[log]
level = "info"              # debug/info/warn/error
format = "text"             # text/json
output = "both"             # stdout/file/both
file_path = "logs/agent.log"
```
### 3️⃣ 启动 Agent
```
go run ./cmd/agentic
```
启动后你会看到类似输出：

```
🤖 学习助手已启动
模型: deepseek-chat
API地址: https://api.deepseek.com
MCP: 正在连接服务器...
Connected to MCP server: filesystem
MCP: 已连接 1 个服务器
  - filesystem: 11 个工具
  注册 MCP 工具: mcp_filesystem_read_file
  注册 MCP 工具: mcp_filesystem_write_file
  ...
(输入 'exit' 退出)
```
### 4️⃣ 示例输入
**学习型输入（触发 DeepLearning Skill）：**

```
我想学习 Transformer 架构
帮我搞懂 Go 的并发模型
```
**文件操作（MCP）：**

```
帮我读取 README.md 文件的内容
列出项目根目录下有哪些文件
```
**记忆操作：**

```
记住：Go 的 interface 是隐式实现的
列出我已经学过的内容
```
**Git 日报（触发 GitReport Skill）：**

```
生成今天的 git 提交日报
```
---

## 🧠 Agent 工作流程
### 主流程（带 Skills 路由）
```
User Input
   ↓
Orchestrator
   ├─ Skills Registry 路由
   │   ├─ 匹配到 Skill？ → 执行 Skill 工作流
   │   └─ 未匹配        → 走默认对话
   ↓
返回结果
```
### 学习型输入（DeepLearning Skill）
```
User Input: "我想学习 XXX"
   ↓
匹配到 DeepLearning Skill
   ↓
1️⃣ Plan   - Planner 拆解为 3~5 个可执行步骤
   ↓
2️⃣ Execute - 逐步执行
   │   ├─ 从 Memory 检索相关知识（RAG）
   │   ├─ LLM 推理（可调用 Tool）
   │   └─ 保存步骤结果
   ↓
3️⃣ Review  - 自我反思与总结
   ↓
4️⃣ Memory  - 沉淀到长期记忆
```
### 工具调用流程
```
User Input → LLM 决策 → Tool Call → 执行结果 → LLM 继续推理 → Reply
                ↑                              ↓
                └──────── 工具调用循环 ─────────┘
```
---

## 🎯 Skills 系统
Skills 是 Tool 之上的高阶能力单元，封装多步骤、有编排逻辑的复杂工作流。

### 核心概念
**Skill vs Tool：**

* **Tool**：单步原子操作（如 read_file、write_memory）
* **Skill**：多步编排的工作流（如系统化学习、生成报告）

### 内置 Skills
|Skill 名称|触发关键词|功能描述|
|-|-|-|
|**DeepLearning Skill**|学习、搞懂、理解、掌握|系统化学习技术主题（Plan → Execute → Review）|
|**GitReport Skill**|git、日报、提交记录|生成 Git 提交日报|

### Skills 执行流程
```
用户输入："我想学习 Transformer 架构"
   ↓
Skills Registry 路由 → 匹配 DeepLearning Skill
   ↓
Skill 工作流：
   1️⃣ Plan   - 拆解学习步骤（3-5步）
   2️⃣ Execute - 逐步执行（可调用 Tool）
   3️⃣ Review  - 自我反思与总结
   4️⃣ Memory  - 沉淀到长期记忆
   ↓
返回最终结果
```
### 扩展 Skills
**方式一：代码定义**

```
type MySkill struct {
    skills.BaseSkill
}

func (s *MySkill) Execute(ctx SkillContext) (SkillResult, error) {
    // 实现你的工作流逻辑
    return SkillResult{Content: "..."}, nil
}

// 在 Orchestrator 中注册
skillsRegistry.Register(NewMySkill(toolRegistry))
```
**方式二：配置驱动**

在 `config.toml` 中添加：

```
[[skills.configurable]]
name = "code_review"
description = "代码审查助手"
keywords = ["审查", "review", "检查代码"]
system_prompt = "你是一个严谨的代码审查专家，擅长发现代码中的问题..."
tools = ["mcp_filesystem_read_file"]
max_rounds = 5
```
### Skills 隔离机制
每个 Skill 可以声明 `RequiredTools()`，限制其可用的工具子集，实现能力隔离。

```
func (s *DeepLearningSkill) RequiredTools() []string {
    return []string{"write_memory", "list_memory"}
}
```
---

## 🔌 MCP（Model Context Protocol）
本项目实现了完整的 MCP 客户端，支持连接任何符合 MCP 协议的服务器。

### 支持的 MCP 服务器
|服务器|安装命令|提供的工具|
|-|-|-|
|filesystem|`npx @modelcontextprotocol/server-filesystem`|read_file, write_file, list_directory, etc.|
|其他...|参考 [MCP Servers](https://github.com/modelcontextprotocol/servers)|-|

### MCP 架构
```
Agent
  ↓
Tool Registry
  ├── 本地工具 (write_memory, list_memory)
  └── MCP 工具适配器
        ↓
    MCP Manager
        ├── MCP Client (filesystem)
        ├── MCP Client (other...)
        └── ...
              ↓
          MCP Server (外部进程)
```
### 添加新的 MCP 服务器
在 `config/config.toml` 中添加：

```
[[mcp.servers]]
name = "your-server"
command = "your-command"
args = ["arg1", "arg2"]
env = { KEY = "value" }
```
---

## 项目阶段规划
本项目采用 **阶段式演进**，每一阶段都在前一阶段基础上做最小增量升级。

### ✅ 阶段一：Agent 最小闭环
* CLI 交互式 Agent
* LLM 调用封装
* 本地长期 Memory（JSON）

### ✅ 阶段二：Plan → Execute 学习 Agent
* Planner：将学习目标拆解为可执行步骤
* Executor：逐步执行每个步骤
* 执行过程与结果自动沉淀为 Memory

### ✅ 阶段三：检索式 Memory（RAG）
* 引入 Embedding（支持 OpenAI / Ollama）
* 基于余弦相似度的 Top-K 相似记忆检索
* Prompt 仅注入与当前问题最相关的历史知识

### ✅ 阶段四：Tool Calling
* 定义 Tool Schema（Function Calling）
* LLM 自主决策是否调用工具
* 工具执行结果回传给 LLM 继续推理
* 已实现工具：`write_memory`、`list_memory`

### ✅ 阶段五：Reflection / Review Agent
* Plan → Execute 完成后自动触发 Review
* 总结关键结论、识别不清晰点、生成下一步建议
* Reflection 结果写入长期 Memory

### ✅ 阶段六：MCP 集成
* 实现 MCP 客户端（JSON-RPC 2.0 over stdio）
* MCP Manager 管理多服务器连接
* MCP 工具自动注册到 Tool Registry
* 支持文件系统等外部工具

### ✅ 阶段七：Skills 系统
* 定义 Skill 接口（高阶能力单元）
* 实现 Skills Registry（智能路由）
* 内置 DeepLearning Skill（系统化学习）
* 内置 GitReport Skill（代码日报）
* 支持配置驱动的 Skill
* 快速接入外部 Skills
* Skills 隔离机制（Tool 子集控制）

---

## 🧩 技术选型
|组件|选型|说明|
|-|-|-|
|语言|Go 1.25|高性能、工程化|
|LLM|DeepSeek / OpenAI|可配置切换|
|Embedding|Ollama (bge-m3)|本地运行，隐私安全|
|Memory|JSON + 向量检索|简单有效|
|外部工具|MCP|标准化工具协议|

---

## 🏁 当前进度
- [x] Agent 最小闭环
- [x] Plan → Execute 学习模式
- [x] Embedding + 检索式 Memory（RAG）
- [x] Tool Calling（Agent 行为能力）
- [x] Reflection / Review Agent（自我进化）
- [x] MCP 集成（外部工具扩展）
- [x] Skills 系统（高阶能力编排）
- [x] 结构化日志系统

---

## 🌟 未来演进方向
* **Skills 市场**：外部 Skills 的发现、安装、版本管理
* **多 Agent 协作**：Planner / Executor / Reviewer 独立 Agent
* **任务队列**：支持异步任务、长期目标追踪
* **评估系统**：学习效果评估 / 打分机制
* **产品化**：Web UI / REST API
* **更多 MCP 服务器**：数据库、搜索引擎、代码执行等
* **Skills 自动生成**：根据用户需求自动创建新 Skill

---

## 📝 最近更新
* **2026-03 feat：快速接入外部 Skills** - 支持通过配置快速接入外部 Skills
* **2026-03 feat：实现具体 Skill** - 实现 DeepLearning Skill 和 GitReport Skill
* **2026-03 test：Skills 测试** - 完善 Skills 系统的测试覆盖
* **2026-03 feat：重构 Orchestrator** - 优化编排器架构，支持 Skills 路由
* **2026-03 chore：替换模型** - 更新 LLM 模型配置，支持更多模型选择

---

> **这是一个完整的 Agentic AI 学习与实践项目，而不是 Demo。**
> 项目仍将持续演进，核心 Agentic Loop + Skills 系统 + MCP 扩展能力已经完成。
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
