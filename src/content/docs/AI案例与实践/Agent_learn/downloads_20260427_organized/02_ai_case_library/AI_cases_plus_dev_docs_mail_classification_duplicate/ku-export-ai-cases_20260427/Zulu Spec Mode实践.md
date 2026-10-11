---
title: "智能CR点击触发解读携带的参数，需在点击新建会话同样携带"
description: "Zulu Spec Mode实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Zulu Spec Mode实践.md"
---
Zulu Spec Mode实践

#### 🧑‍🏫 案例作者：[@连聪](https://ku.baidu-int.com?t=mention&mt=contact&id=5ab8b060-fcec-11f0-917b-717b0ec7fc48)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文详细记录了Zulu在Spec模式下的实践过程，包括智能CR点击触发解读、分析触发解读携带的参数、解决点击生成文件无响应问题，以及智能CR规则管理功能的实现。通过需求分析、界面设计、数据流设计和接口设计，成功实现了规则查看、管理、应用等功能，并探讨了Spec模式的适用场景与局限性，强调了其对于边界清晰、结构性强项目的优势。
# 智能CR点击触发解读携带的参数，需在点击新建会话同样携带
先让Zulu分析触发解读都做了什么

![](/personal-site-mvp/img/doc-placeholder.svg "")
发现在创建解读接口中有所需参数

接着分析新建会话时的流程

![](/personal-site-mvp/img/doc-placeholder.svg "")
不过他还是分析出了跟 apiGetAgentById 有关，确实每次新建回话都会请求该接口来返回 Agent信息

这正是需要携带meta信息的接口

![](/personal-site-mvp/img/doc-placeholder.svg "")
过程中遇到了一个问题，点击生成好的文件无法跳转至对应处，也就是点击无响应

![](/personal-site-mvp/img/doc-placeholder.svg "")
发现文档和任务列表和总结都没有正常工作

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
useAgentInfoWithMetadata文件中的hook并未被使用，实际并不需要

# 智能CR Rules
发送了一个有点模糊的需求

让 zulu 复用 StaffSetting，改成模态框，并且接口也都要改，携带了接口的基本信息

![](/personal-site-mvp/img/doc-placeholder.svg "")
zulu 列出的详细需求文档

```
# 智能CR规则管理功能需求文档

## 需求背景
在小码哥嵌入式对话框中，需要为智能CR（Code Review）功能提供规则管理能力，允许用户定制评审标准和行为规范，提升代码评审的质量和一致性。

## 用户故事
作为小码哥的用户，我希望能够在嵌入式对话框中管理智能CR规则，以便：
1. 查看当前仓库的评审规则
2. 添加、编辑、删除自定义评审规则
3. 在代码评审时应用这些规则

## 使用场景
1. **规则查看**：用户在小码哥嵌入式对话框中点击"查看所有委托任务"旁的规则图标，查看当前仓库的智能CR规则
2. **规则管理**：用户可以添加新规则、编辑现有规则或删除不需要的规则
3. **规则应用**：在进行代码评审时，用户可以选择要应用的规则，系统将根据这些规则进行智能评审

## 技术方案

### 1. 界面设计
- 在`Header.tsx`中添加规则管理按钮，位于"查看所有委托任务"按钮右侧
- 使用`Ruler.tsx`图标作为规则管理入口
- 弹窗采用左右布局，左侧为规则列表，右侧为规则详情或空状态

### 2. 数据实体设计
```typescript
interface CRRule {
  ruleId: number;
  repoName: string;
  ruleName: string;
  charCount: number;
  content: string;
  gmtCreate: Date;
  gmtModified: Date;
}

interface CRRuleParams {
  repoName: string;
  ruleName: string;
  content: string;
}
```

### 3. 数据流设计
1. **规则获取**：调用`GET /api/comatestack/rest/ai/cr/rules?repoName={repoName}`获取规则列表
2. **规则创建**：调用`POST /api/comatestack/rest/ai/cr/rules/addRule`创建新规则
3. **规则更新**：调用`POST /api/comatestack/rest/ai/cr/rules/updateRule`更新规则
4. **规则删除**：调用`POST /api/comatestack/rest/ai/cr/rules/deleteRule`删除规则
5. **规则应用**：在评审接口`POST /api/comatestack/rest/ai/cr/review/start`中传入`userRuleIds`数组

### 4. 逻辑时序设计
1. 用户点击规则图标 → 打开规则管理弹窗
2. 弹窗加载时获取当前仓库规则列表
3. 用户进行规则操作（增删改）→ 调用对应API → 刷新规则列表
4. 用户关闭弹窗 → 保存当前状态

### 5. 接口设计
- **获取规则列表**：`GET /api/comatestack/rest/ai/cr/rules?repoName={repoName}`
- **创建规则**：`POST /api/comatestack/rest/ai/cr/rules/addRule`
- **更新规则**：`POST /api/comatestack/rest/ai/cr/rules/updateRule`
- **删除规则**：`POST /api/comatestack/rest/ai/cr/rules/deleteRule`

## 实现细节

### 1. Header组件修改
在`src/comatestack/StaffInline/ChatPanel/Header.tsx`中：
- 判断是否为小码哥且是嵌入式对话框
- 在"查看所有委托任务"按钮右侧添加规则管理按钮
- 使用`Ruler.tsx`图标

### 2. 规则管理弹窗
基于`src/comatestack/StaffSettings`组件改造：
- 标题为"智能评审规则"
- 副标题："该规则作用于小码哥的评审，提供定制化的评审标准，或规范小码哥需要遵守的行为"
- 包含"新建规则"和"使用示例"按钮
- 左右布局：左侧规则列表，右侧规则详情

### 3. 规则列表组件
- 显示规则标题、启用状态、字符数、更新时间
- hover时显示编辑和删除图标
- 无规则时显示空状态，使用`Empty.tsx`图标

### 4. API集成
创建专用的CR规则API接口：
- 使用`createBaseInterface`创建API方法
- 统一的错误处理和响应格式

## 预期成果
1. 用户可以在小码哥嵌入式对话框中便捷管理智能CR规则
2. 规则管理界面直观易用，支持完整的CRUD操作
3. 规则能够正确应用到代码评审流程中
4. 提升代码评审的标准化和自动化水平
```
接口理解有点偏差，应该是icode前缀，人为修改

修改后点击 confirm 无响应

![](/personal-site-mvp/img/doc-placeholder.svg "")
人为继续

![](/personal-site-mvp/img/doc-placeholder.svg "")
后续点击仍然无响应

![](/personal-site-mvp/img/doc-placeholder.svg "")
创建/编辑规则不再弹窗，因为该场景已经是弹窗；

取消测试

confirm and continue 开始执行

修改完后启动项目

![](/personal-site-mvp/img/doc-placeholder.svg "")
zulu用了 useReducer管理状态

![](/personal-site-mvp/img/doc-placeholder.svg "")
将错误信息发送给他解决

![](/personal-site-mvp/img/doc-placeholder.svg "")
这一步执行了较长时间，仿佛陷入了死循环

![](/personal-site-mvp/img/doc-placeholder.svg "")
最后生成解决了错误语法，实际并未解决

![](/personal-site-mvp/img/doc-placeholder.svg "")
spec模式还会改动其他文件，实际上该文件并无关联

![](/personal-site-mvp/img/doc-placeholder.svg "")
执行速度有点慢

分析了好几次问题也没有解决

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 数字员工对话流式回复动画实现
![](/personal-site-mvp/img/doc-placeholder.svg "")
文档合理详细

![](/personal-site-mvp/img/doc-placeholder.svg "")
计划合理，还考虑到采用 context7

![](/personal-site-mvp/img/doc-placeholder.svg "")
生成过程中有几次失败，最终生成无报错

![](/personal-site-mvp/img/doc-placeholder.svg "")
突然又意识到和数字员工对话并非流式输出，需求只是在数字员工对话到一半 类似于卡住的情况 新增loading效果即可；

让zulu改变需求，事实上这已经违背了spec模式的本质

不过zulu还是正确修改了tasks文件和doc文件

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
对于非流式加 loading 的任务也完成了

此时我又想让 zulu 取消对于流式情况下的所有改动

![](/personal-site-mvp/img/doc-placeholder.svg "")
但 zulu 在这一步理解错了

它把所有的改动均回退了，只留下了一些文档，相当于直接回滚到对话未开始处

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 总结思考
我理解的 spec 模式就是先写规格文档 → 确认 → 写任务列表 → 确认 → 执行 → 汇总

首先非常适合边界清晰的功能开发，有明确的约束条件，强结构性的项目；

能以流程、分步骤形式表达的任务，在这种模式下 agent 执行也就更稳健



不太适合需求模糊，大概率不断变动的需求或大型项目；



spec应该最适合复杂度适中的需求

如果太小写文档和审阅任务列表的时间比直接写代码还长，效率极低；

如果太大复杂度指数级上升。AI 生成的 Spec 可能会因为太长而变得空泛，缺乏细节；



不过这种模式还是像一面镜子，它反逼着我把需求描述得更清晰。有时候在修改 Spec 的过程中，我自己就发现了原先逻辑的漏洞，可能有许多地方没有描述清楚，先一步防止 AI 有理解误差。



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
