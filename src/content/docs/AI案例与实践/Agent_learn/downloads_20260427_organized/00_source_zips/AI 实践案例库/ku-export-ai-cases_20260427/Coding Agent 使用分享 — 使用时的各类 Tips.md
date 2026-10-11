---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "Coding Agent 使用分享 — 使用时的各类 Tips"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Coding Agent 使用分享 — 使用时的各类 Tips.md"
---
Coding Agent 使用分享 — 使用时的各类 Tips

#### 🧑‍🏫 案例作者：[@华彬闳](https://ku.baidu-int.com?t=mention&mt=contact&id=7696ccb0-fce5-11f0-b478-356db5cf5e79)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Claude Code
#### 📒 案例概要：本文分享了在开发场景下使用Claude Code的Prompt具体实操经验，强调了选择Claude Code的三大理由：可控性、智能性和自动化。详细介绍了Commands、Agents和Hooks三大核心功能，并提供了实操时的核心原则，包括目标明确性、分步骤执行和小上下文策略。通过具体案例展示了如何利用Claude Code工具提升开发效率，实现自动化工作流和无缝集成开发工具链。
### 一. 开发场景下 Prompt 具体使用实操 - Claude Code
#### 1.1 为什么选择Claude Code？
* **可控性：**通过Commands精确指导AI行为
* **智能性：**Agents提供专业化的编程协助
* **自动化：**Hooks实现工作流程无缝衔接
* **结果导向：**交付可运行的解决方案，而不仅仅是代码片段

**（1）Commands**

* 结构化的指令接口，精确控制AI行为
* 标准化操作：/tdd、/commit、/add-test、/fix
* 避免模糊交互，确保执行结果可预期

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=611fc407c809490b83d92be6db16168f&docGuid=NIm502_xkNnNBV "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=166bab0db4424d4097cafe2e2960d385&docGuid=NIm502_xkNnNBV "")
**（2）****Agents（智能代理）**

* 专业化AI代理处理不同编程任务
* 上下文感知：理解项目结构和代码关系
* 持续学习：在项目进展中积累领域知识

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9029589270a24183b4a4eda6a147e01c&docGuid=NIm502_xkNnNBV "")
**（3）****Hooks（钩子机制）**

* 事件驱动的自动化工作流
* 代码变更触发自动测试和检查
* 无缝集成开发工具链和CI/CD流程
* 自动完成编码最耗时部分：配置文件生成、测试用例编写、文档生成、部署脚本

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=675ffb2d8fa74933a98410f5cc337e10&docGuid=NIm502_xkNnNBV "")
#### 1.2 实操时的核心原则
**（1）目标明确性原则**

项目类型区分：新建Demo项目 vs 大型现有项目

* **新建Demo**："创建支持邮箱/密码登录、JWT token认证、包含注册/登录/找回密码功能的用户认证系统"
* **大型项目**："在UserController.py的login方法中添加登录失败3次锁定账户30分钟的逻辑"
* **上下文完整：**提供业务背景、技术栈、约束条件
* **期望明确：**说明预期的输出格式、性能要求、安全标准

**【举例说明】**

* **新项目**
    * **目标：**为电商网站开发商品搜索功能
    * **技术栈：**Python + FastAPI + Elasticsearch
    * **需求：**支持关键词、分类、价格区间过滤，响应时间<200ms
    * **输出：**完整的API端点代码 + 单元测试

* **大型项目（指令要小，改动要小）**
    * **目标：**在现有用户系统中添加邮箱验证功能
    * **需求：**发送验证邮件，验证码6位数字，5分钟有效期
    * **输出**：单个方法实现 + 对应测试用例


**【需要避免的指令类型】**

* ❌ "帮我写个搜索功能"
* ❌ "优化这段代码"
* ❌ "做个网站"
* ❌大型项目中的大范围修改："重构整个用户模块"
* ❌跨多个文件的复杂变更："统一所有API的错误处理"



**（2）****Comnand Step by Step**

* **为什么要分步骤？**
    * **降低复杂度：**将大任务分解为可管理的小步骤
    * **提高准确性：**每步都可以验证和调整
    * **便于调试：**问题定位更精确
    * **支持迭代：**可以随时调整方向

* **Step-by-Step 最佳实践**
    * 第一步：架构设计和文件结构规划
    * 第二步：核心功能模块实现
    * 第三步：测试用例编写
    * 第四步：集成测试和优化
    * 第五步：文档和部署准备

* **实际应用示例**
    * Step 1: 设计数据库schema和API接口
    * Step 2: 实现用户模型和数据访问层
    * Step 3: 开发认证中间件
    * Step 4: 创建路由和控制器
    * Step 5: 编写测试和错误处理




**（3）小上下问+配合工具**

* **小上下文策略**
    * 主动清理上下文：完成模块后立即clear，保持AI专注力
    * 单任务聚焦：每次交互只关注一个具体问题
    * 依赖CLAUDE.md：通过文档而非对话历史提供项目背景
    * 模块化思维：将大项目拆分为独立可测试的模块
    * 清晰边界：明确每个步骤的输入输出

* **充分利用Claude Code工具**
    * /tdd: 测试驱动开发，先写测试后写实现
    * /commit: 提交代码变更，自动生成提交信息
    * /add-test: 为现有代码添加测试用例
    * /fix: 修复代码问题和bug

* **代码库上下文管理秘诀：CLAUDE.md**
    * 项目概览：在根目录创建CLAUDE.md文件
    * 架构说明：记录系统架构、技术栈、设计决策
    * 编码规范：统一的代码风格和最佳实践
    * 业务逻辑：核心业务规则和数据流向
    * 开发约定：文件组织、命名规范、测试策略
    * 上下文传承：让AI快速理解整个项目的来龙去脉


![CLAUDE.md](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c49edbe59bf04666902fc65b9275e448&docGuid=NIm502_xkNnNBV "CLAUDE.md")
* **Hooks（钩子机制）**
    * 在关键节点设置检查点
    * 自动触发代码质量检查
    * 集成测试自动化执行
    * 自动化最耗时任务：通过hooks配合，自动完成配置管理、环境搭建、依赖安装、测试执行、部署发布等繁琐工作

* **Notify（通知系统）**
    * 任务完成状态实时反馈错误和警告及时提醒
    * 进度跟踪和里程碑通知


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=33518a6ab87d4b9c910cd8a843802aca&docGuid=NIm502_xkNnNBV "")
* **Check（检查验证）**
    * 代码规范自动检查
    * 安全漏洞扫描
    * 性能基准测试
    * 单元测试覆盖率验证


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
