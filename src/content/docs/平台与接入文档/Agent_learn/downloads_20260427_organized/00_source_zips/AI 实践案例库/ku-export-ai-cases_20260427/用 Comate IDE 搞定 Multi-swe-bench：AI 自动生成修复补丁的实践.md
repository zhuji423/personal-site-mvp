---
title: "实践简介"
description: "用 Comate IDE 搞定 Multi-swe-bench：AI 自动生成修复补丁的实践"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\用 Comate IDE 搞定 Multi-swe-bench：AI 自动生成修复补丁的实践.md"
---
用 Comate IDE 搞定 Multi-swe-bench：AI 自动生成修复补丁的实践

#### 🧑‍🏫 案例作者：[@江宇琪](https://ku.baidu-int.com?t=mention&mt=contact&id=1e05d8f0-fce7-11f0-a8de-7954b8673f5c)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了使用Comate IDE补全Multi-swe-bench基准测试中缺失的AI模型自动生成修复补丁的实践。通过制定智能体规则、利用Agent实现多语言patch生成，并优化GitHub仓库读取逻辑，成功实现了AI自动生成并验证代码补丁，提升了研究可复现性。
# 实践简介
人工智能赋能软件开发是当前趋势，自动代码修复是提升研发效率的重要方向。

**Multi-swe-bench** 是评估 AI 模型代码修复能力的核心基准测试集，简单说就是一套标准化的 “测试工具”—— 它收集了大量真实软件开发中出现的代码缺陷，以及验证修复效果的标准，专门用来衡量 AI 模型修复代码的能力。其核心流程分为三步：

本文目标就是采用** Comate IDE** 来补全 Multi-swe-bench 缺失的 “**AI 模型自动生成修复补丁（Patch）**” 的代码实现！

1. **数据集准备**：整理代码缺陷的问题描述、错误代码及测试用例；
2. **Patch 生成**：由 AI 模型针对缺陷生成修复代码（即 “补丁”）；
3. **评估验证**：验证补丁的正确性与有效性。

[流程图]
但在复现该基准测试时发现，其开源代码中缺少「**AI 模型自动生成 patch**」这一关键环节的具体实现，影响了研究的可复现性。

# 关键词
Github项目复现、代码智能体评测、自定义规则、功能代码生成

# 具体实践
## 1.制定智能体规则——未经允许不修改代码
为避免频繁直接修改代码导致的逻辑混乱，我需要 Comate Agent 在执行任何代码修改前，严格遵循以下规则：

1. 先清晰列出「实现流程思路」（包括核心逻辑、涉及的代码模块 / 文件、预期效果）；
2. 再提供「拟修改的具体代码片段」（标注新增 / 删除 / 修改的内容，确保可追溯）；
3. 最后明确询问「是否同意按该方案执行修改」，仅在我确认后，方可实际操作代码。

### 具体规则实现
```

---description: |
description: |
globs: 
alwaysApply: true
---
Code Modification Protocol - Agent必须遵守的代码修改规则
  
  核心原则：
  1. 透明化修改流程：在修改代码前必须完整展示实现方案
  2. 用户确认机制：所有修改必须获得用户明确同意后才能执行
  3. 最小化风险：确保修改不会破坏现有功能
  
  具体执行流程：
  1. 需求分析阶段：
     - 明确用户需求的具体含义
     - 分析现有代码结构和依赖关系
     - 评估修改可能带来的影响
  
  2. 方案设计阶段：
     - 设计详细的实现思路和架构
     - 列出具体的修改步骤和顺序
     - 考虑边缘情况和错误处理
  
  3. 方案展示阶段：
     - 展示完整的实现代码（包括新增、修改、删除的部分）
     - 说明修改的工作流程和数据流向
     - 指出可能的风险和应对措施
   
  4. 确认执行阶段：
     - 等待用户明确确认（"确认"、"同意"、"执行"等）
     - 只有在获得确认后才执行实际修改
     - 修改后验证功能正常
  
  注意事项：
  - 对于复杂的修改，建议分步骤展示和确认
  - 如果修改涉及多个文件，需要展示完整的文件列表
  - 重大重构或架构调整需要更详细的说明
  - 保持代码风格与项目现有规范一致
  - 确保修改后的代码有适当的注释和文档
  
  例外情况：
  - 简单的语法修正或明显的拼写错误可以直接修复
  - 用户明确要求"直接修改"的情况可以跳过确认流程

```


实际使用后整体效果符合预期：Agent 会先梳理出清晰的待办任务清单（todos），接着输出详细的方案设计思路及对应的代码修改方案，最后会明确询问是否执行修改，且全程不会主动破坏现有代码。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9087c76babcf4cb4b218b078c234ad46&docGuid=_POCuGUzrMTKLa "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4972a24f08a143e3b9ed91722f200f57&docGuid=_POCuGUzrMTKLa "")
## 2.利用Agent实现生成多语言patch
```
prompt是我想实现的大致流程：
    读取本地数据集data，输入为data/编程语言文件/项目.jsonl，输出为输入的父目录文件，实现思路为读取输入的jsonl文件，jsonl文件的每一行对应一个补丁项目，使用zulu-cli 和 claude-cli的形式请求模型，zulu和claude的api-token为xxx，使用subprocess库，先创建函数生成command命令，再调用另一个函数执行，将std.out和std.err文件都存放在输出目录中，实现自动化批量请求。
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=60bc6c00abd04e1f8b1528dbd7edc93f&docGuid=_POCuGUzrMTKLa "")
从实际使用效果来看，核心功能虽已实现，但仍存在两处关键不足：一是未关联 GitHub 仓库，二是缺乏异常捕获机制，因此需要进一步推动模型优化。

本次优化重点聚焦**GitHub 仓库读取逻辑的实现**，为了让模型更精准理解我的需求，我通过「add to chat」功能，直接指定了需要修改的函数及代码行，并补充了三部分关键信息：

① 整体实现流程（ “先通过 GitHub API 拉取仓库元数据→解析文件结构→缓存核心代码”）；

② 核心逻辑说明（ “需支持私有仓库通过 Token 认证，公开仓库直接匿名拉取”）；

③ 伪代码示例（标注关键步骤的输入输出、异常处理节点），以此引导模型按明确路径完善功能。

```
对于生成patch，还需要关联github仓库，思路是准备代码仓库，如果不存在则克隆，存在则复用，然后重置仓库到指定的base commit，再根据这些信息读取项目文件生成patch，并且对每个过程要有足够的异常捕获机制。只修改这些代码行，其他功能不要更改。
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e17490c8dd6b489eb622ede2f5d8164b&docGuid=_POCuGUzrMTKLa "")
多次使用 Add to Chat 功能，精准定位并锁定需修改的功能函数代码，进行小幅度、有针对性的调整，最终生成最接近预期的版本后，再对部分细节进行手动微调。

最终手动测试运行，成功跑通并生成目标Patch。

# 复盘
## 模式：（好的经验）
    * 制定一个好的Rules十分重要，这能从根本上避免许多模型思考误区和不良体验。例如，本文强调的 “未经允许不修改代码” 规则，就能有效防止因模型生成结果有误而导致的代码混乱，减少不必要的反复修改。
    * 在使用Agent开发的过程中，最好保证逻辑清晰，思路细致，你向 Agent 阐述代码实现思路时越详尽（包括项目背景、业务逻辑、技术细节等），Agent 就越能理解你的意图，其输出结果也就越接近你的预期。
    * 灵活使用**“Add to chat”**功能，**精准控制修改范围。**使用 Agent 编写代码时，反复修改是常态。一个常见的痛点是模型可能会 “过度操作”，修改了你认为无需改动的部分。这时，“Add to chat” 功能就能派上用场。通过它，你可以精确指定需要修改的代码片段，让你的指令更具体，Agent 也能更清晰地理解你的需求，从而避免不必要的代码变动。

### 反模式：（不要这么做）
    * 不要过分相信Agent的理解能力，他确实可以实现一些常用功能，但由于不同项目的差异性，模型理解能力有限。很多人都会有这种经历：向模型描述一个需求后，模型会反复生成和修改代码，每次都看似接近目标，却始终无法达到 “符合项目真实场景” 的完美效果。这通常是因为模型对需求的理解过于泛化，未能精准捕捉项目的独特性。
    * **小步迭代，精准微调，** 当 Agent 输出的代码已经达到约 60% 符合预期时，建议优先使用 “Add to chat” 功能进行小范围、有针对性的修改，甚至可以精确到行级别。这种方式能最大限度地保留已有的正确代码结构，避免因模型的 “过度理解” 而导致不必要的改动

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
