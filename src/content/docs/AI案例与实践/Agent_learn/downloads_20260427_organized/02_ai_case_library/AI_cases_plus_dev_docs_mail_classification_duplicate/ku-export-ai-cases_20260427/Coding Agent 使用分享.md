---
title: "一、背景介绍"
description: "Coding Agent 使用分享"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Coding Agent 使用分享.md"
---
Coding Agent 使用分享

#### 🧑‍🏫 案例作者：[@张爱欣](https://ku.baidu-int.com?t=mention&mt=contact&id=de87a520-fce4-11f0-96a7-69d0b2508639)
#### 🎬 案例场景：全流程
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了智能营销产品部张爱欣引入Claude Code提升研发效率的实践。通过对比使用Claude Code前后的预估人天和实际人天，展示了该工具在前端脚手架生成、代码规范符合度、单元测试生成等方面的显著提效。前端开发效率平均提升2-3倍，后端简单需求效率提升3倍，复杂需求效率提升50%，内部工具平台开发效率提升5-7倍，同时提升了代码质量和团队协作优化。
[文档目录]
# 一、背景介绍
### **团队面临的研发效率挑战**
    * 在公私有化项目和产品迭代并行（私有化-兴业/浦发银行、SaaS-九号电动车），新老平台同时维护（旧平台：客服云端版/专业版，老的外呼平台，新平台：客悦·ONE），前后端技术重构升级（后端：专业版和企业版核心组件能力打平重构，前端基础技术栈major版本升级）的背景下，团队整体产品竞争力迭代速度有所下降，需要持续优化研发效率，提升迭代速度，保障产品竞争力领先，为商业化成功提供有力支撑

### **Claude Code 介绍和引入**
    * Claude Code是Anthropic 开发的可在本地运行的coding助手，他基于Claude 4系列模型拥有迄今为止最出色的编程能力，为了提升团队的研发效能，第一时间引入到团队做小范围试点做验证

### **评估方法和指标设定**
    * 基于不同角色（前端、后端、算法）和不同的需求难度，对比使用Claude Code**之前的预估人天和使用之后的实际人天**，客观展示该工具对研发效能的提升情况

# 二、研发提效实践
## 2.1 前端开发场景
* **场景1：脚手架生成**
    * 传统方式：需要配置Kit构建、业务代码构建等多个步骤
    * Claude Code：一键生成符合百度编码规范的脚手架，支持项目初始化和重构
    * 效果：显著提升在灵活性上的表现，远胜传统工具

* **场景2：代码规范符合度**
    * 传统方式：配置eslint校验工具约需0.5天
    * Claude Code：支持hook commands配置，自动生成符合百度规范的代码
    * 效果：节省至少0.5天人力，无需人工干预

* **场景3：单元测试代码生成**
    * 优势：自动识别代码结构与逻辑路径，生成的测试用例覆盖比较全面，corner case也可以覆盖到
    * 效果：降低人工遗漏风险，**从天级别优化到分钟级**

* **场景4：E2E端到端测试集代码生成**
    * 传统方式：基于社区工具（如 Midscene）
    * Claude Code优势：结合MCP playwright和项目代码结构与逻辑路径的识别双重校准
    * 效果：相比社区类似工具，在测试用例生成的准确性与覆盖率上均有显著提升

* **场景5：前端技术栈升级**
    * 场景：基础技术栈的major版本升级（包含大量breaking change内容）
    * 效果：**从周级别优化到小时级**

* **场景6：设计稿转代码**
    *  预期：Figma设计稿直接转Page Code，符合团队编码规范且生成准确率95%
    * 现状：目前前端还在探索基于多模态输入的生成效果或基于Figma中间态数据格式，预期Q3落地




## 2.2 后端开发场景
* **后端简单需求**
    * 代码库理解问答场景：从1天缩短到半天
    * 测试驱动开发完成小需求：从1小时缩短到15分钟
    * Bug修复：从1小时缩短到15分钟
    * 代码优化：从半人天缩短到15分钟

* **后端复杂业务需求**
    * 传统方式：要先经过阅读业务对象源代码、技术方案设计，最后手动写代码，其中阅读源代码到技术方案设计预估要5人天，coding部分由于case较多预估5人天；
    * Claude Code：前期梳理背景信息和上下文3天，实际coding 2天
    * 提效：方案设计+Coding共节约5人天




## 2.3 使用案例
### 2.3.1 案例1：算法工程师端到端完成一个线下运营工具平台开发
* 需求描述：基于客悦的对话仿真系统，完成自动化的Prompt压缩优化和效果评估，提升数字员工&外呼的Agent上线效率和效果
* 原预估开发时间：7天，涉及文件上传、异步机制、前端动态渲染、页面布局开发等
* 基于Claude Code的开发&调优上线时间：1天
* 效果对比：相比原来预想开发的一些静态页面，最终基于Claude Code实现了动态的页面渲染，实时进度展示，页面美观度也不错，效果超出预期

[附件]
* 使用Claude Code之后，**研发体验极大提升**：

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 2.3.2 案例2：利用coding Agent 进行code review
* cluade可以以无头模式运行。将claude注册为git commit的钩子，在commit前对代码进行「主观检查」
* 主观检查：识别诸如拼写错误、过时的注释、误导性的函数、变量名称、甚至代码逻辑等问题

```
#!/bin/bash

# 生成 Git staged diff 并传入 Claude Code
diff=$(git diff --cached)

# 如果没有 diff，不运行 Claude
if [ -z "$diff" ]; then
  exit 0
fi

# 将 diff 作为输入用 echo 传入 Claude
echo "$diff" | claude \
  -p "请你作为一名主观代码审查专家，分析这段 Git 改动，指出命名不清、注释风格不一致、拼写
错误、逻辑混乱等主观问题。" \
  --input-format text \
  --output-format text
```
效果：

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 三、效果总结
###  3.1 量化提效
  - 前端开发效率：平均提升2-3倍

  - 后端简单需求：效率提升3倍

  - 后端复杂需求：效率提升50%

  - 内部工具平台开发：算法工程师可独立完成全栈开发，运营内部提效工具开发效率提升5-7倍



###   3.2 质量提升
  - 代码规范：自动符合百度编码规范，减少代码review时间

  - 测试覆盖：corner case覆盖更全面，降低线上风险

  - 技术债务：major版本升级等技术债务处理效率大幅提升



###   3.3 团队协作优化
  - 技能互补：算法工程师具备全栈开发能力

  - 人员配置：更灵活的人员配置和任务分配

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
