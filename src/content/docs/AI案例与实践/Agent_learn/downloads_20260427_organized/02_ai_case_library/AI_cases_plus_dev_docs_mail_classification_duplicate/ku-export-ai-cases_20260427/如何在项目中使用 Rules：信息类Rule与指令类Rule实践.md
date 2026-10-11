---
title: "一、信息类rule实践"
description: "如何在项目中使用 Rules：信息类Rule与指令类Rule实践"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\如何在项目中使用 Rules：信息类Rule与指令类Rule实践.md"
---
如何在项目中使用 Rules：信息类Rule与指令类Rule实践

#### 🧑‍🏫 案例作者：[@高赛](https://ku.baidu-int.com?t=mention&mt=contact&id=bea470c0-fcea-11f0-a9fd-13fc83432d39)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文探讨了如何在项目中使用信息类与指令类Rules，通过具体案例展示了Rules在统一任务理解、规范编码、减少沟通成本及提升效率方面的显著成效，同时详细阐述了项目架构、工作流、智能体系统、工具及编码规范等内容，为项目开发提供了标准化、自动化的解决方案。
# 一、信息类rule实践
### 目标
为 Agent 提供结构化的任务背景、规则和约束，确保模型对项目的理解一致、行为稳定、输出可控。

####  引入 Rules 之前的问题
Conexis Wiki 项目依赖多个智能体协同进行代码库探查和文档生成。在未使用 `rules` 文件时，由于缺乏统一的约束和上下文定义，在使用coding agent的过程中遇到了以下问题：

1. **agent对流程逻辑的把握不够清晰**

* 各 Agent 间的输入输出依赖关系模糊，人需要在 Chat 过程中反复向模型描述各agent职责与 data flow。



2. **编码规范不统一，CR 过程反复卡点**

* 模型生成代码时常缺少模块级 docstring、函数注释等，评审阶段规范问题导致合入阻塞。



3. **生成无关内容，产出噪声多**

* 模型在提交代码后经常附带说明文档、变更文档或示例 demo，这些文件与实际任务无关，增加了仓库冗余与维护负担。



4. **注释风格随意，输出质量难控**

* 模型倾向添加非正式语气或颜文字注释



### 引入 Rules 之后的成效
###### 1. 流程统一与上下文可复现
* 所有智能体执行顺序、输入输出依赖均在 rules 中显式定义，Agent 间的数据流转被规则约束，任务边界清晰；
* 无需反复解释流程逻辑，与agent沟通成本降低，完整工作流模型基本能复现；

###### 2. 规范自动落地，减少cr阻塞
* 编码规范（PEP8、注释格式）在生成阶段基本生效，减少cr阻塞

###### 3. 禁止项（README、demo、example、说明文档）强制执行
* 模型输出仅保留必要功能代码与轻量注释，代码结构清爽

###### 4. 模型通过读取rule，可以更好理解任务，迅速锚定修改点，减少模型检索和推理频次。


```
---
alwaysApply: true
description: 项目基础结构规则
---

## 项目概述

Conexis Wiki 是一个基于 Python 的文档生成系统，使用 LangGraph 和 LLM 智能体自动生成代码仓库的 wiki 文档。该系统集成了 MCP（模型上下文协议）进行代码分析，并使用多智能体工作流创建全面的文档。

## 运行命令
```bash
# 运行主应用程序
python -m conexis_wiki --work_dir /path/to/repo --repo_name name --db_dir /path/to/db --server_base_url url --request_id id
```

## 架构概述

### 核心工作流（基于 LangGraph）
系统在 `conexis_wiki/graph/builder.py` 中定义了顺序智能体工作流：

1. **prepare** → 2. **wiki_catalog_think** → 3. **wiki_parent_catalog_generate** → 4. **wiki_child_catalog_generate** → 5. **wiki_page_generate** → 6. **report**

**各工作流之间的data flow:**

1. **prepare** (准备阶段)
   - **职责**: 初始化运行环境和数据库
   - **输入**: WikiContext（包含 repo_path, repo_id, repo_name 等）
   - **输出**: 
     - `repo_tree`: 仓库目录树结构（字符串）
     - `catalog_service`, `repo_service`, `item_service`: 数据库服务实例
     - `persist_dir`: 持久化目录路径
     - `repo_index_ready`: 仓库索引就绪标志

2. **wiki_catalog_think** (目录结构分析)
   - **职责**: 使用 LLM 分析代码库整体结构，生成目录分析报告
   - **输入**: 
     - `repo_tree`: 从 prepare 阶段获取
     - `catalog_service`, `repo_service`: 服务实例
   - **输出**: 
     - `wiki_catalog_analysis`: 代码库分析结果（字符串，包含项目类型、架构、功能模块等）
     - `wiki_catalog_think_agent_tool_stats`: 工具调用统计

3. **wiki_parent_catalog_generate** (父目录生成)
   - **职责**: 基于分析结果生成一级 wiki 目录结构
   - **输入**: 
     - `wiki_catalog_analysis`: 从 wiki_catalog_think 阶段获取
     - `repo_tree`: 仓库目录树
     - `catalog_service`: 目录服务
   - **输出**: 
     - `parent_catalog_success`: 生成是否成功
     - `wiki_parent_catalog_generate_agent_tool_stats`: 工具调用统计

4. **wiki_child_catalog_generate** (子目录生成)
   - **职责**: 为每个父目录生成子目录结构
   - **输入**: 
     - `catalog_service`: 目录服务（用于查询已生成的父目录）
     - `repo_tree`: 仓库目录树
   - **输出**: 
     - `wiki_child_catalog_agent_tool_stats`: 工具调用统计

5. **wiki_page_generate** (页面内容生成)
   - **职责**: 为每个叶子目录生成对应的 wiki 页面内容
   - **输入**: 
     - `catalog_service`: 目录服务（用于查询叶子目录）
     - `repo_tree`: 仓库目录树
     - `item_service`: 页面项服务
   - **输出**: 
     - `wiki_page_agent_tool_stats`: 工具调用统计

6. **report** (报告阶段)
   - **职责**: 汇总统计信息并上报最终结果
   - **输入**: 
     - 所有 agent 的工具调用统计（wiki_catalog_think_agent_tool_stats, wiki_parent_catalog_generate_agent_tool_stats, wiki_child_catalog_agent_tool_stats, wiki_page_agent_tool_stats）
   - **输出**: 无（最终节点）

### 关键组件

**入口点：**
- `conexis_wiki/cmdline.py`: 主 CLI 入口点
- `conexis_wiki/run.py`: 核心执行逻辑，包含 WikiGenerateGraph

**智能体系统（`conexis_wiki/graph/agents/`）：**
- `prepare_agent.py`: 初始设置和准备
- `wiki_catalog_think_agent.py`: 目录结构分析
- `wiki_parent_catalog_generate_agent.py`: 父目录生成
- `wiki_child_catalog_generate_agent.py`: 子目录生成
- `wiki_page_agent.py`: wiki 页面内容生成
- `report_agent.py`: 最终报告和统计

**Tools（`conexis_wiki/tools/`）：**
提供grep_code、list_dir、read_file、search_file、search_codebase五种工具，但是注意search_codebase当前不在agent中使用。

**Prompt 管理（`conexis_wiki/prompts/`）：**
当前项目中处于使用状态的prompt如下：
- system_prompt_zh.md 系统提示词
- wiki_catalog_think_zh.md 服务于wiki_catalog_think智能体，用于代码库目录结构分析
- wiki_parent_catalog_generate_zh.md 服务于wiki_parent_catalog_generate智能体，用于父目录生成
- wiki_child_catalog_generate_zh.md 服务于wiki_child_catalog_generate智能体，用于子目录生成
- wiki_page_zh.md 服务于wiki_page智能体，用于wiki页面内容生成

## Agent接入指南
1. 在conexis_wiki/prompts/目录下新增任务prompt文件
2. 如果需要新增tools，参考其他tool的实现方式，在conexis_wiki/tools/新增tool
3. 参考其他agent的实现，在conexis_wiki/graph/agents/中新增任务agent。
4. 新增agent需要增加工具调用情况统计，并将统计结果在report_agent中输出

## 编码规范
遵循PEP 8编码规范，特别强调：
- 函数与函数之间保留两个空行
- 类的方法与方法之间保留一个空行
- 类与类之间保留三个空行
- 需要有模块注释、类注释、方法注释、函数注释，使用docstring方式来添加注释

## 重要约束（必须严格遵守）
**禁止创建文档和示例文件：**
- **禁止**在完成代码修改后创建任何"使用说明"、"README"、"使用文档"等markdown文档
- **禁止**创建任何example、demo、sample等示例文件
- **禁止**在代码注释中添加长篇的使用示例或使用说明
- **只修改代码本身**，完成功能实现即可，不需要额外的文档说明
- 代码注释应该简洁明了，只说明"是什么"和"为什么"，不需要说明"如何使用"
- 生成的文本描述中**禁止**添加任何颜文字、图标等。

```
# 二、指令类rule实践
### 目标
目标是把重复性的操作步骤流程化，让 Agent 能按规范自动完成一个明确的任务，而不需要人手动指导或反复解释，以此提高效率，并保持功能实现的统一性、准确性和整洁性。

### **编写思路**
在本案例中需要完成的任务是：新增一个Prometheus指标。

根据实际完成指标的过程进行整理，作为Agent执行任务时的操作指导。主要步骤如下：

1. 检查现有指标的实现与使用方式，明确Agent应复用的逻辑与位置；
2. 定义新的指标；
3. 在合适的业务逻辑中实现埋点。

### **成效**
通过规则化的指导，Agent可在3分钟内完成一个Prometheus业务指标的新增，且编码风格与打点方式保持一致。



```
.cursor/rules/metrics.mdc
---
alwaysApply: false
description: 增加自定义prometheus指标
---

增加一个自定义Prometheus指标，请按照如下步骤

1. 检查已有的指标实现与使用方式，避免和已有的指标冲突
- 当前的指标定义在`internal/request/metric.go`中
- 参考`internal/request/httpclient.go`的使用方式


2. 定义指标，复用现有桶配置和命名风格
- 不同的统计需要，对应不同的prometheus，请选择合适的指标
- 在`internal/request/metric.go`中增加新的指标

3. 在对应的业务逻辑位置，增加合适的观察点
- 统计操作可以在defer中增加，确保不影响主线业务逻辑
```
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
