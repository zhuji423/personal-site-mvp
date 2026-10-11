---
title: "用户需要显式引用"
description: "从 Rules 到 Skill：AI 单元测试生成的工程化演进"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\从 Rules 到 Skill：AI 单元测试生成的工程化演进.md"
---
从 Rules 到 Skill：AI 单元测试生成的工程化演进

#### 🧑‍🏫 案例作者：[@柴延晨](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发、测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：阐述了从Rules到Skill的AI单元测试生成工程化演进过程，通过实践进一步了解Skill的优点及应用场景

## 一、前文回顾
在上一篇文章[AI 生成 TalosPro 项目单元测试：规则驱动的实践方法](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/XmAoToL5vCkUKG?t=mention&mt=doc&dt=doc)，我使用了一套 **规则驱动（Rules-driven）** 的 AI 单测生产流程：

1. 人工编写初版 rules（mock 配置、测试模板、覆盖率策略）
2. AI 在 rules 约束下批量生成测试并自我修复
3. 基于踩坑记录反向迭代 rules

这套方法验证了一个核心结论：

> **AI 写单测的上限，取决于 rules 的质量，而不是 prompt 的花哨程度。**
但在实际项目推广中，我发现 **rules 本身存在工程化瓶颈**。本文将介绍我们如何把测试 rules 升级为 **skill**，以及这次演进解决了哪些问题。

---

## 二、Rules 的瓶颈：能用，但不够好
### 2.1 被动触发，依赖人工指引
Rules（`.mdr` 文件）是被动的。AI 不会主动读取它，必须依赖以下方式触发：

```
# 用户需要显式引用
按照 #test.mdr 给该项目补充单元测试
```
或在 `always-apply-rules` 中编写复杂的场景匹配逻辑，强制 AI 在特定场景下执行 `read_file` 读取对应 rules。这意味着：

* **新人不知道规则存在** → 无法触发
* **AI 也不知道规则存在** → 除非被告知

### 2.2 单文件膨胀，上下文浪费
随着迭代，[test.mdr](/Users/chaiyanchen/Documents/code/baidu/newx-comic/talospro-comic/.comate/rules/test.mdr) 从最初的简单配置膨胀到 **800+ 行**，包含：

|内容|行数占比|
|-|-|
|核心配置（vitest.config.ts, setup.ts）|~30%|
|测试模板（组件、页面、工具函数）|~25%|
|常见问题与解决方案|~25%|
|覆盖率策略与检查清单|~20%|

但每次触发时，**全部内容一次性加载到上下文**。写一个简单的工具函数测试，也要消耗 800 行 token 去加载 Worklet mock 模板和 DOM API 问题排查。

### 2.3 踩坑记录与规则脱节
在 rules 方案中，AI 遇到的问题被记录到独立的 `test-trouble.mdr`，然后由人工合并回 rules。这个流程存在两个问题：

1. **手动合并容易遗忘** — 问题记录了但没回流到规则
2. **缺乏去重判断** — 同一个问题可能被反复记录

### 2.4 缺乏标准化工作流
Rules 只告诉 AI "规范是什么"，但不告诉它 "工作流程是什么"。AI 读完 800 行规则后的行为是不确定的：

* 有时先写测试再运行
* 有时运行了但不检查覆盖率
* 有时漏掉了环境配置检查

---

## 三、Skill 的设计：从"文档"到"工作流"
### 3.1 核心设计理念
Skill 不是把 rules 换个格式存放，而是一次 **从静态文档到主动工作流** 的架构升级：

```
Rules 模式:  规则文档 → 人工引用 → AI 读取 → 自由发挥
Skill 模式:  触发条件 → 自动加载 → 标准流程 → 按需引用 → 知识回流
```


附上具体的skill描述

```
---
name: talospro-test
description: TalosPro 项目单元测试生成与维护。使用场景：(1) 为 TalosPro 组件或页面生成单元测试 (2) 配置测试环境（vitest.config.ts, setup.ts）(3) 解决测试运行错误 (4) 提高测试覆盖率 (5) 用户提及"单测"、"单元测试"、"test"、"vitest"、"覆盖率"
---

# TalosPro 单元测试

## 核心原则

1. **全面覆盖**: 行覆盖率目标 80%+，分支覆盖率 70%+
2. **独立性**: 每个测试用例独立运行，不依赖其他测试状态
3. **模拟依赖**: 所有外部依赖应被正确模拟
4. **快速反馈**: 测试应快速运行（单文件<2秒）

## 测试文件结构

```
__test__/
├── components/           # 组件测试
│   └── component-name/
│       └── index.test.ts
├── pages/               # 页面测试
│   └── page-name/
│       ├── index.test.ts
│       └── root.test.ts
├── src/                 # 源码目录测试
│   └── index.test.ts
└── setup.ts             # 测试环境配置
```

## 工作流程

### 1. 环境配置

首次配置时，参考以下模板：
- **vitest.config.ts**: 参考 [references/vitest-config-template.ts](references/vitest-config-template.ts)
- **__test__/setup.ts**: 参考 [references/setup-template.ts](references/setup-template.ts)

### 2. 编写测试

参考 [references/test-patterns.md](references/test-patterns.md) 获取：
- 组件测试模板
- 页面测试模板
- 异步操作测试
- 模拟技术

### 3. 运行与验证

```bash
# 运行所有测试
pnpm test

# 运行特定文件
pnpm test path/to/test/file.test.ts

# 生成覆盖率报告
pnpm test:coverage
```

### 4. 覆盖率目标

| 层级 | 目标 | 包含内容 |
|------|------|---------|
| 核心层 | 90%+ | utils/, const.ts, storage.ts |
| 业务层 | 80%+ | computed, 数据处理方法 |
| 视图层 | 60%+ | 生命周期, 事件处理 |

### 5. 问题排查

遇到测试错误时，参考 [references/troubleshooting.md](references/troubleshooting.md)

## 自测验证检查清单

完成测试编写后必须执行：

- [ ] 运行 `pnpm test` 确认全部通过
- [ ] 运行 `pnpm test:coverage` 检查覆盖率达标
- [ ] 失败用例已修复或有明确说明
- [ ] 测试运行稳定（多次运行结果一致）
- [ ] 没有 console.log 等调试代码
- [ ] 没有被跳过的测试（.skip）

---

## Reflector 机制

当修复测试错误后，**必须执行** Reflector 流程，将有价值的问题记录到知识库中。

### 触发条件

满足以下**任一条件**时触发 Reflector：
1. 错误信息具有通用性（不依赖特定业务逻辑）
2. 解决方案涉及框架/工具的特定用法
3. 错误可能在其他组件/页面中重复出现
4. 调试耗时超过 5 分钟

### 排除条件

满足以下条件时**不触发** Reflector：
- 简单的拼写错误或语法错误
- 业务逻辑相关的断言失败
- 一次性的测试数据问题

### Reflector 执行流程

1. **检查重复**: 在 [references/troubleshooting.md](references/troubleshooting.md) 的快速查找表中搜索错误关键词
2. **判断价值**: 评估是否符合触发条件
3. **记录问题**: 如果是新问题，按以下格式追加到 troubleshooting.md：

```markdown
## 问题N: [简短描述]

**症状**: `[错误信息]`

**原因**: [根本原因分析]

**解决方案**: [具体修复方法]

\`\`\`typescript
// 代码示例
\`\`\`

---
```

4. **更新快速查找表**: 在文件顶部的表格中添加新条目

### 示例

修复了一个 `TypeError: xxx.map is not a function` 错误后：

1. 检查快速查找表 → 未找到类似问题
2. 判断价值 → 数组类型检查是通用问题，符合条件
3. 追加到 troubleshooting.md 末尾（测试失败排查流程之前）
4. 在快速查找表添加：`xxx.map is not a function | 数据未初始化为数组 | 添加默认值或类型检查`

```


### 3.2 目录结构对比
**之前（Rules）**：

```
.comate/rules/
├── test.mdr                  # 800+ 行，一个文件包含所有内容
└── test-troubleshooting.mdr  # 独立的问题记录，需手动合并
```
**之后（Skill）**：

```
.comate/skills/talospro-test/
├── SKILL.md                          # ~80 行，核心工作流
└── references/
    ├── setup-template.ts             # setup.ts 配置模板
    ├── vitest-config-template.ts     # vitest 配置模板
    ├── test-patterns.md              # 测试模式参考
    └── troubleshooting.md            # 常见问题（含 Reflector 插入点）
```
**关键变化：从 1 个 800 行文件 → 1 个 80 行入口 + 4 个按需加载的参考文件。**

---

## 四、Skill 解决的四个核心问题
### 4.1 主动触发：AI 自己知道该用什么
Skill 的 `description` 字段是主动触发机制：

```
description: TalosPro 项目单元测试生成与维护。使用场景：
  (1) 为 TalosPro 组件或页面生成单元测试
  (2) 配置测试环境
  (3) 解决测试运行错误
  (4) 提高测试覆盖率
  (5) 用户提及"单测"、"单元测试"、"test"、"vitest"、"覆盖率"
```
当用户说"补充单元测试"时，AI **自动匹配并加载** 这个 skill，无需用户知道规则文件的存在。

|对比项|Rules|Skill|
|-|-|-|
|触发方式|用户手动引用 `#test.mdr`|关键词自动匹配|
|新人上手|需要先知道规则文件存在|直接说需求即可|
|AI 感知|被动等待 `read_file`|主动识别场景|

### 4.2 渐进式加载：只读需要的内容
Skill 采用三级加载策略：

```
Level 1: description（~50 词）     → 始终在上下文中，用于触发判断
Level 2: SKILL.md body（~80 行）   → 触发后加载，提供核心工作流
Level 3: references/（按需）        → 仅在具体步骤需要时加载
```
**实际效果对比：**

|场景|Rules 加载量|Skill 加载量|
|-|-|-|
|写一个工具函数测试|800 行全部|80 行 SKILL.md + test-patterns.md|
|排查一个测试错误|800 行全部|80 行 SKILL.md + troubleshooting.md|
|首次配置测试环境|800 行全部|80 行 SKILL.md + 两个模板文件|

上下文窗口是公共资源。Skill 的渐进式加载让 AI 有更多空间去理解业务代码，而不是被规则文档挤占。

### 4.3 标准化工作流：AI 每次都走同样的路
SKILL.md 定义了一个确定性的工作流程：

```
1. 环境配置 → 检查 vitest.config.ts / setup.ts 是否就绪
2. 编写测试 → 参考 test-patterns.md 中的模板
3. 运行验证 → pnpm test / pnpm test:coverage
4. 覆盖率检查 → 核心层 90%+ / 业务层 80%+ / 视图层 60%+
5. 问题排查 → 参考 troubleshooting.md
6. Reflector → 将新问题回流到知识库（如触发条件满足）
```
相比 rules 的"读完自由发挥"，skill 确保 AI 每次执行的步骤一致、可预期。

### 4.4 Reflector 机制：知识自动回流
这是 skill 方案中最关键的创新。在 rules 模式下，问题记录和规则迭代是分离的：

```
Rules 模式:
  AI 遇到错误 → 记录到 test-trouble.mdr → 人工审阅 → 手动合并回 rules
  （断裂点：人工合并经常遗忘）
```
Skill 内置了 Reflector 机制，让问题记录自动闭环：

```
Skill 模式:
  AI 修复错误 → 评估是否通用 → 检查 troubleshooting.md 是否已有
                                     ↓ 是新问题
                              按格式追加到 troubleshooting.md
                              同步更新快速查找表
```
**触发条件**（满足任一即触发）：

* 错误信息具有通用性（不依赖特定业务逻辑）
* 解决方案涉及框架/工具的特定用法
* 错误可能在其他组件/页面中重复出现

**排除条件**（避免噪音）：

* 简单拼写错误
* 业务逻辑断言失败
* 一次性测试数据问题

这意味着 **troubleshooting.md 会随着使用不断积累**，形成项目专属的测试知识库。下次 AI 遇到类似问题时，直接从中查找已有方案，而不是重新摸索。

---

## 五、实践效果
在 TalosPro 漫画频道项目中，我们完成了 rules → skill 的转换并验证：

|指标|Rules 模式|Skill 模式|
|-|-|-|
|触发方式|手动引用 `#test.mdr`|说"补充单元测试"自动触发|
|上下文消耗|~800 行/次|~80 行 + 按需加载|
|工作流一致性|不确定|标准 6 步流程|
|问题回流|手动合并|Reflector 自动回流|
|最终覆盖率|100%|100%|
|测试通过率|128/128|128/128|

---

## 六、从这个案例看 Skill 的本质
Rules 和 Skill 的关系，不是"旧版本"和"新版本"的关系，而是两种不同的抽象层级：

||Rules|Skill|
|-|-|-|
|本质|静态文档|可执行的工作流|
|职责|告诉 AI "规范是什么"|告诉 AI "怎么做、何时做、做完后干什么"|
|触发|被动（需人工引用）|主动（关键词匹配）|
|加载|全量|渐进式|
|演进|人工合并|内置反馈闭环|

一个直觉性的类比：

> **Rules 是操作手册，Skill 是带导航的工作台。**
> 操作手册需要你先翻到正确的页码，再逐条对照执行。
> 工作台在你坐下时就知道你要做什么，按顺序递给你需要的工具，做完后还帮你记录经验。
---

## 七、适用场景
这套 rules → skill 的演进方法适用于以下场景：

1. **规则文件已膨胀到 300+ 行** — 拆分为 SKILL.md + references
2. **多人协作项目** — 新人不需要知道规则文件的存在
3. **规则需要持续演进** — Reflector 机制减少人工维护成本
4. **AI 执行一致性要求高** — 标准化工作流消除行为不确定性

---

## 八、结语
上一篇文章的结论是：**把 AI 变成可被工程化管理的测试生产力**。

这篇文章进一步回答了：**用什么载体来承载这个工程化管理？**

答案是 Skill — 它不只是规则的容器，而是：

* 一个 **主动感知场景** 的触发器
* 一个 **按需加载知识** 的调度器
* 一个 **标准化执行流程** 的编排器
* 一个 **自动积累经验** 的学习器

当规则升级为 Skill，AI 不再是"读了手册的实习生"，而是"带着工具箱和经验手册的熟练工"。



> 备注：本文AI含量约80%😄
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
