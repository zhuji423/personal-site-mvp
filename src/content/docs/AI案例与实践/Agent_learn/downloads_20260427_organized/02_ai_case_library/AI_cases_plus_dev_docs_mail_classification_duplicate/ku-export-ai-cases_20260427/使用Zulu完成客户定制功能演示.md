---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "使用Zulu完成客户定制功能演示"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\使用Zulu完成客户定制功能演示.md"
---
使用Zulu完成客户定制功能演示

#### 🧑‍🏫 案例作者：[@吴玮琦](https://ku.baidu-int.com?t=mention&mt=contact&id=9b3e7080-fceb-11f0-ba0c-19ee8a1ce495)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文展示了使用Zulu和AI完成客户定制需求的实践，包括支持自定义代码规范、配置编码检测规则、设置质量门禁等。通过MCP和容器化技术，提供API扫描和页面展示功能，满足客户对代码质量、统计和过滤的需求，实现高效的代码审查和管理。
## 客户需求
当前公司使用的是Sonar，但是不支持自定义规范，所以希望使用百度Comate能力进行替换。[https://rules.sonarsource.com/](https://rules.sonarsource.com/)

1. 支持用户自定义代码规范，后续可以自己修改规范。

    * **支持配置各语言的编码规范检测规则**
    * **支持配置当个方法复杂度**
    * **支持配置单个文件不能超过多少行**
    * **支持配置质量门禁，bug、异味、漏洞不能超过多少个，重复代码率不能超过多少，复杂度不能超过多少**
    * **支持配置仅校验新代码或全量校验，或新代码全量代码同时校验**

2. 提供API能力，用于客户侧流水线的扫描。扫描支持全量扫描和diff扫描（diff扫描用户给两个仓库地址，接口能明确出哪些是diff，针对diff进行代码审查）
3. **扫描结果需要用页面呈现**，给出具体代码的问题点，不需要修复，后续人工修复。
4. 支持过滤代码功能，一些白名单的文件等。
5. 扫描结果提供本次结果即可，可以不记录历史结果。
6. 需要有数据统计功能，包括所有历史扫描不符合规范的统计结果，例如漏洞、异位、复杂度数据。

百度可以提供的：

提供一个CLI，对接客户侧的mcp提供分配责任人的能力：

    * 提供一个容器，该容器内置所有云天化语言的规范，以文件形式存在。Agent会自动读取。
    * 集成环境，支持导入用户数据，产出报告html格式，需要客户提供一个mcp，报告+用户id传给mcp，通过mcp分配给具体的责任人。
    * 确认运行环境版本

## 客户希望的扫描结果页面
**1报告总览页面**

需要给出是否可以合并代码的建议，如果不能合并，需罗列出不满足要求的指标。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**2问题列表页**

![](/personal-site-mvp/img/doc-placeholder.svg "")
**3问题详情页**

问题详情页，需要定位到问题代码行号，并且给出修复建议。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**4重复代码定位**

重复代码，支持定位到具体哪个文件的哪一行代码重复。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**5复杂度定位**

复杂度不满足门禁的，需要给出详细的复杂度计算，具体是哪一行增加多少复杂度。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**6指标变化趋势**

![](/personal-site-mvp/img/doc-placeholder.svg "")


## 拆解任务
很明显，这个demo虽小，但是五脏俱全：有详情，有列表，有总览；有各种扫描规则，不同的规则可能展示内容不同。

在一个任务里完成所有需求有些困难，需要人工拆解。

在评审生成阶段通过rule约束模型输入

[流程图]
```
---
description: 
globs: 
alwaysApply: false
---

你是一个code-review助手，帮我检查当前文件是否有下述问题。你要检查最近的commit的所有修改的文件，先把所有修改的文件列举成一个文件，文件名为modified-files.txt。然后后面逻辑根据每个文件来进行，文件完成之后标记一下

* 检查当前文件的行数，可以使用wc -l命令。不要超过200行。
* 计算每个方法的圈复杂度，把复杂度算出来，不要超过10。
* 找出代码中的bug、异味、漏洞


注意，你要把遇到的问题用json结构的数据写到code-review目录下，文件名为issue.json
单个问题的 JSON 结构，一定要有文件路径，必须是相对路径。并且你找代码在哪里的时候，不要猜，用命令行来搜索具体的位置，注意，执行路径最多只能是当前目录
{
  "id": "issue-uuid-12345",
  "type": "bug|vulnerability|code_smell|complexity|duplication|security|maintainability|reliability",
  "severity": "blocker|critical|major|minor|info",
  "category": "accessibility|performance|security|best-practice",
  "rule": {
    "id": "typescript-S1082",
    "name": "Visible, non-interactive elements with click handlers must have at least one keyboard listener",
    "description": "Mouse events should have corresponding keyboard events"
  },
  "location": {
    "filePath": "apps/example/src/pages/Login/index.tsx",
    "startLine": 195,
    "endLine": 197,
    "startColumn": 1,
    "endColumn": 20,
    "codeSnippet": "  className={classNames(styles.eyes, passErr ? styles['validate-err'] : '')}\n  onClick={clickEye}\n>"
  },
  "message": "添加键盘事件处理器以确保可访问性",
  "description": "可交互元素需要同时支持鼠标和键盘操作，以满足无障碍访问要求",
  "suggestion": {
    "title": "添加 onKeyDown 或 onKeyPress 事件处理器",
    "content": "为该元素添加键盘事件监听器，例如：onKeyDown={(e) => e.key === 'Enter' && clickEye()}",
    "fixExample": "onClick={clickEye}\nonKeyDown={(e) => e.key === 'Enter' && clickEye()}"
  },
  "effort": "5min",
  "tags": ["accessibility", "react", "a11y"],
  "status": "open|confirmed|resolved|false_positive|wont_fix",
  "assignee": null,
  "createdAt": "2025-11-03T10:30:00Z",
  "metrics": {
    "complexity": null,
    "duplicatedLines": null,
    "duplicatedBlocks": null
  },
  "references": [
    {
      "type": "rule_documentation",
      "url": "https://rules.sonarsource.com/typescript/RSPEC-1082"
    }
  ],
  "relatedLocations": [],
  "isNewCode": true,
  "debt": "5min"
}
圈复杂度问题示例
{
  "id": "complexity-uuid-67890",
  "type": "complexity",
  "severity": "critical",
  "category": "maintainability",
  "rule": {
    "id": "java-S3776",
    "name": "Cognitive Complexity of methods should not be too high",
    "description": "方法的认知复杂度不应过高"
  },
  "location": {
    "filePath": "src/main/java/com/example/Service.java",
    "startLine": 56,
    "endLine": 82,
    "startColumn": 1,
    "endColumn": 1,
    "codeSnippet": "public void processData(String url) {\n  // method body\n}",
    "functionName": "processData",
    "functionSignature": "public void processData(String url)"
  },
  "message": "将此方法的认知复杂度从 26 降低到允许的 15",
  "description": "当前方法的圈复杂度为 26，超过了门禁要求的 15",
  "suggestion": {
    "title": "重构方法以降低复杂度",
    "content": "建议将复杂的逻辑拆分为多个小方法，每个方法只负责一个职责。可以考虑：\n1. 提取嵌套的 if 语句为独立方法\n2. 使用策略模式替代多个条件分支\n3. 将循环内的复杂逻辑提取为独立方法",
    "fixExample": null
  },
  "effort": "18min",
  "tags": ["brain-overload", "maintainability"],
  "status": "open",
  "assignee": null,
  "createdAt": "2025-11-03T10:30:00Z",
  "metrics": {
    "complexity": {
      "current": 26,
      "threshold": 15,
      "exceeded": 11,
      "details": [
        {
          "line": 57,
          "increment": 1,
          "reason": "for loop",
          "code": "for (int i = 0; i < 1000000; i++)"
        },
        {
          "line": 58,
          "increment": 2,
          "reason": "nested if statement",
          "code": "if (condition1 && condition2)"
        },
        {
          "line": 62,
          "increment": 1,
          "reason": "if statement",
          "code": "if (records.isEmpty())"
        },
        {
          "line": 64,
          "increment": 2,
          "reason": "nested for loop",
          "code": "for (Object record : records)"
        }
      ]
    },
    "duplicatedLines": null,
    "duplicatedBlocks": null
  },
  "references": [
    {
      "type": "rule_documentation",
      "url": "https://rules.sonarsource.com/java/RSPEC-3776"
    }
  ],
  "relatedLocations": [],
  "isNewCode": false,
  "debt": "18min"
}
重复代码问题示例
{
  "id": "duplication-uuid-11111",
  "type": "duplication",
  "severity": "major",
  "category": "maintainability",
  "rule": {
    "id": "common-duplication",
    "name": "Duplicated code blocks should be removed",
    "description": "重复的代码块应该被移除或提取为公共方法"
  },
  "location": {
    "filePath": "yth-platform/apps/src/utils/create.js",
    "startLine": 45,
    "endLine": 67,
    "startColumn": 1,
    "endColumn": 1,
    "codeSnippet": "export const createItem = () => {\n  const data = new Data();\n  data.process();\n  return data;\n}"
  },
  "message": "检测到重复代码块，重复率 25.6%",
  "description": "该代码块与其他文件中的代码存在 25.6% 的重复",
  "suggestion": {
    "title": "提取重复代码为公共方法",
    "content": "将重复的代码逻辑提取到一个公共的工具方法或基类中，避免代码重复",
    "fixExample": null
  },
  "effort": "10min",
  "tags": ["duplication", "refactoring"],
  "status": "open",
  "assignee": null,
  "createdAt": "2025-11-03T10:30:00Z",
  "metrics": {
    "complexity": null,
    "duplicatedLines": 23,
    "duplicatedBlocks": 1
  },
  "references": [],
  "relatedLocations": [
    {
      "filePath": "yth-platform/apps/src/utils/update.js",
      "startLine": 12,
      "endLine": 34,
      "message": "与此处代码重复",
      "codeSnippet": "export const updateItem = () => {\n  const data = new Data();\n  data.process();\n  return data;\n}"
    },
    {
      "filePath": "yth-platform/apps/src/utils/delete.js",
      "startLine": 8,
      "endLine": 30,
      "message": "与此处代码重复",
      "codeSnippet": "export const deleteItem = () => {\n  const data = new Data();\n  data.process();\n  return data;\n}"
    }
  ],
  "isNewCode": false,
  "debt": "10min"
}

```
### 将HTML页面和填充的数据拆分
拆解原则：将HTML页面结构与数据填充逻辑完全分离
具体做法：

1. 静态模板层：创建纯vue模板，使用占位符标记数据插入点 
2. 数据层：设计标准化的JSON数据结构，作为模板和扫描结果之间的桥梁 

一次开发，且能每次保证输出稳定

### 根据需求单出生成一个中间交互的json
拆解原则：定义一个标准化的中间交互JSON格式
数据结构层次：

```

├── 元数据（项目信息、扫描时间、配置参数）
├── 总览数据（质量门禁状态、各类问题统计）
├── 问题列表数据
│   ├── Bug列表
│   ├── 漏洞列表
│   ├── 异味列表
│   └── 其他问题分类
├── 重复代码数据（文件对比、行号映射）
├── 复杂度数据（方法级、文件级统计）
└── 趋势数据（历史对比、变化曲线）
```
 智能体任务分配：

1. 让智能体根据客户需求单，生成完整的JSON Schema定义 	
2. 要求智能体提供示例数据，覆盖各种边界情况（无问题、大量问题、部分门禁失败等） 	
3. 让智能体生成数据验证逻辑，确保扫描结果符合Schema规范

### 将应用拆成3个HTML页面
将用户的截图直接发给模型，让他按照图片和生成的json结构来写总览页、列表页、详情页等。

规定使用vue、tailwind css，所有依赖使用CDN，为了**用更少的上下文空间**

### 将需要CR的代码拆成逐个文件读取
拆解原则：将批量代码审查拆解为逐个文件的顺序处理
处理流程设计：

```
代码仓库
↓
文件列表提取（过滤白名单）
↓
逐个文件读取
↓ (循环处理)
单文件扫描 → 应用规则集 → 收集问题
↓
汇总结果
↓
生成中间JSON
↓
渲染HTML报告
```
## 验证
基本满足需求，有些地方甚至超出预期。比如使用本地存储来跨页面传输数据，并且对问题、漏洞进行了分级。

[附件]


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
