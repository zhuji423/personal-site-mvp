---
title: "系统文档化与架构分析 - Claude Code Prompt"
description: "您是一位拥有20年经验的资深Java架构师。需要对一个大型微服务系统进行从全局到细节的深度架构评审与文档化。"
date: "2026-05-06"
category: "项目架构文档"
source: "D:\\mac_m4\\code\\baidu\\qamate-strategy\\apismart-code\\wiki\\CLAUDE_CODE_PROMPT.md"
---
# 系统文档化与架构分析 - Claude Code Prompt

## 🎯 核心任务

您是一位拥有20年经验的资深Java架构师。需要对一个大型微服务系统进行**从全局到细节的深度架构评审与文档化**。

**面向受众**：只对Python有比较多了解、对Java仅有语法水平的开发者

**输出质量标准**：无删减、全细节、架构级别深度，所有分析都要**结合具体代码文件和行数**进行论证

---

## 📦 系统背景

项目根目录：`/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code`

核心由两部分组成：
1. **现行系统（qamate-server）**：3个独立微服务
   - `core`：业务编排与调度中枢（JDK21 + Spring Boot 3.2）
   - `apiExecutor`：任务执行器引擎（JDK17 + Spring Boot 3.5）
   - `api-smart-dispatch`：分布式调度中心，基于XXL-JOB二次开发（JDK17）
2. **遗留系统（inner-os/itp）**：长期支持的老版本（JDK8，已隔离）

通讯方式：HTTP/REST（Feign代理） + 异步回调

---

## 📋 需要完成的任务

### 1️⃣ 架构深度解析报告

使用**思考过程 (Thinking Process)** 的方式，分析以下5个维度，输出为长篇幅Markdown文档：

**维度A：全局架构图景**
- 识别项目采用的架构模式（微服务、DDD、管道-过滤器等）
- 用Mermaid语法绘制核心模块的依赖关系图
- 类比Python生态（FastAPI + Celery）帮助理解

**维度B：核心业务流向**
- 追踪最关键的业务路径：从用户请求输入到数据库持久化的完整生命周期
- 解释各层级之间的交互逻辑
- 标注关键类名和代码行数

**维度C：隐性依赖与副作用**
- 分析模块间的深层耦合
- 找出通过全局变量、事件总线或数据库表共享产生的隐性依赖
- 具体举例（如ThreadLocal绑定、Metrics基数爆炸等）

**维度D：设计模式与代码风格**
- 识别代码中大量使用的设计模式
- 评价其实现的优劣
- 找出Clean Code违背的地方

**维度E：潜在风险评估**
- 从4个维度列出最危险的5个漏洞/技术债：
  1. 并发安全（ThreadLocal、线程池、MDC跨异步丢失）
  2. 内存管理（OOM风险）
  3. 安全性（SQL注入、越权、硬编码后门）
  4. 可扩展性（包冲突、版本兼容性）

---

### 2️⃣ 开发者维护手册

撰写极其详尽的手册，包含：

**部分A：全库知识索引**
- 每个模块（core、apiExecutor、api-smart-dispatch）的完整职责说明
- 目录结构与子模块的作用
- 关键类定义表（类名、所在模块、核心职责）
- 全局配置项释义字典（各配置项的用途、风险点、改动影响）

**部分B：代码逻辑补完**
- 针对代码库中**最复杂的3个函数**，分别撰写**极其详尽的逐行注释**
- 指出每个函数中违背Clean Code原则的地方，包括：
  - 单一职责原则(SRP)
  - 命令查询分离(CQS)
  - 隐藏状态依赖
  - 性能问题
  - 安全问题
- 给出具体的重构建议

---

### 3️⃣ 系统全景拓扑与生命周期文档

完成以下4大分析任务：

**任务1：全景拓扑**
- 绘制Mermaid图表展示3大模块的依赖关系
- 标注通讯协议（HTTP/Feign、异步回调等）
- 包含数据流和调用方向

**任务2：核心技术栈**
- 列出每个模块使用的关键框架（版本号、用途）
  - Core: Spring Boot 3.2、Feign 13.1、JetCache 2.7.7、Prometheus等
  - Executor: XXL-Job Core、Spring Boot 3.5、Transmittable ThreadLocal等
  - Dispatcher: XXL-Job Admin、Netty 4.2.6、Groovy 5.0.1等
- 列成表格形式便于查阅

**任务3：目录地图**
- 精确定位3大模块对应的源代码路径
- 标明每个模块的启动类Entry Points（如App.java、Application.java等）
- 列出关键业务类的位置（Controller、Service、Manager、Mapper等）

**任务4：启动生命周期**
- 描述系统启动顺序（Dispatcher → Executor → Core）
- 每个模块的初始化步骤（Spring容器、Feign代理、连接池、定时线程等）
- 三个模块的握手逻辑（Executor如何注册到Dispatcher，Core如何调用Dispatch等）
- 绘制完整的时序图（Mermaid）

---

## 🎓 特殊要求

1. **面向Python开发者**
   - 大量使用Python生态的类比（Flask vs Spring Boot、requests vs Feign、Celery vs XXL-Job等）
   - python 后端的内容也不熟悉，也需要详细的介绍python的框架然后再介绍java的对应框架
   - 解释Java概念对应的Python实现方式
   - ### 术语与概念回答风格（术语 101 / 原理内化）

- 对于重要的术语和概念（并扩展到其相关概念、对偶概念或相反概念），要进行必要的解释，并尽量多使用类比与联想来帮助理解。
- 对这些内容应当主动、直观，同时保持准确与严谨地阐述。
- 如果涉及计算相关的概念，可以补充相应的数学 LaTeX 表达；也可以适当补充一些我可能“还不知道自己不知道”的背景点。
- 始终以第三人称进行回答：表达要精准、有深度，既不失真实而有洞见的观点（truth insights），也要生动。
- 在输出答案之前，优先通过在线搜索对关键事实进行复核（可用 Web 搜索替代 Google）。

2. **不要精简**
   - "请尽可能详尽"、"我需要最完整的细节来辅助决策"
   - 所有分析都要**结合具体的代码文件和行数进行论证**
   - 逐行代码注释务必详尽

3. **一切为了决策**
   - TOP 5风险要明确优先级和修复方案
   - Clean Code诊断要给出重构建议
   - 配置释义要标注改动的风险点

4. **输出格式**
   - Markdown长篇幅文档
   - 包含Mermaid图表
   - 使用表格、列表等结构化形式
   - 文档间要有导航和索引

---


## 🎯 输出清单

请为我生成以下产出物：

✅ **4份详尽的Markdown Wiki文档**
1. `ARCHITECTURE_DEEP_DIVE.md` - 架构全景与风险评估
2. `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` - 维护手册与代码诊断
3. `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md` - 拓扑图与生命周期
4. `DOCUMENTATION_INDEX.md` - 文档导航与快速索引

✅ **每份文档应包含**
- 思考过程（Thinking Process）的开篇说明
- 详尽的分析，不做任何精简
- 具体的代码文件路径和行数
- Mermaid图表（拓扑、时序图等）
- 结构化的表格和列表

✅ **输出位置**
- 全部存储在 `/wiki_claude/` 目录下

---

## 🚀 优先级

1. 首先完成架构全景分析 (维度A-E)
2. 其次完成3个复杂函数的代码诊断
3. 然后完成系统拓扑与生命周期分析
4. 最后生成导航与快速索引文档

---

**这是一个完整系统的架构评审与文档化项目。请确保所有细节都包含在内，这份文档将用于关键的技术决策。**

