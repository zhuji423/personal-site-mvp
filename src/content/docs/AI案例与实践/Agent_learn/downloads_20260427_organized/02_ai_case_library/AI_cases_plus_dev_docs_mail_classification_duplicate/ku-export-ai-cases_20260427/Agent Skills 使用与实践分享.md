---
title: "一、Agent 技术进展"
description: "Agent Skills 使用与实践分享"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Agent Skills 使用与实践分享.md"
---
Agent Skills 使用与实践分享

#### 🧑‍🏫 案例作者：[@靖声险](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：iCode、Comate
#### 📒 案例概要：Agent Skills标准化封装，渐进式披露破解上下文困境，实现能力模块化复用与确定性执行。
# 一、Agent 技术进展
**2023**

**~**

**2024**

**基础搭建**

**工具调用落地 & 单任务适配实现从****「****文本生成****」****到****「****实际行动****」**

* 标志性技术为工具使用**（Tool Use）**与函数调用**（Function Calling）**的初步落地
* API接口将**大模型与外部系统连接**，打破了大模型仅能进行文本生成的局限，使智能体具备了获取实时数据*（如天气查询、股票行情）*、调用基础服务*（如数据库检索、邮件发送）*的原子化操作能力
* 提示词工程**（Prompt Engineering）**开始兴起，通过优化指令描述提升模型对任务意图的识别准确率，成为当时智能体开发的核心技术手段

**2024**

**~**

**2025**

**能力优化**

**多任务规划 & 状态记忆能力升级使得复杂任务的****「****长周期交互的稳定性****」****提升**

* 任务规划**（Planner）**技术的初步成熟，智能体可通过简单的逻辑推理将复杂任务拆分为多个原子化步骤
* 状态记忆**（Memory）**技术从无状态向简单有序演进，智能体可短暂记忆上一轮交互结果，支持多轮对话场景下的上下文衔接
* **工具调用的多样化升级**，支持同时调用多个不同类型的工具，实现多工具协同完成复杂任务

**2025**

**~**

**2026**

**架构升级**

**从「提示词工程（Prompt Engineering）」迈入「技能工程（Skill Engineering）」的全新阶段**

* 跨平台兼容性提升，基于**MCP协议**（Model Context Protocol）的数据链接有助于实现“一次开发，多平台共用”
* **Agent Skill的标准化封装机制**，将提示词、逻辑代码、知识库、工具调用接口封装为独立的标准化模块*（如：Anthropic的SKILL.md架构）*，实现了能力的模块化复用
* **“渐进式披露（Progressive Disclosure）”架构**的创新，模型仅根据任务意图动态加载必要的技能资源，无需全量加载所有规则，大幅优化了上下文效率

# 二、背景
**       传统模式的弊端开始显现**：在大模型爆发初期，开发者控制模型行为主要依赖于“提示词工程”（Prompt Engineering），即将复杂的业务规则、知识库和操作指令全部写入系统提示（System Prompt）或对话上下文中。然而，随着企业级应用向工作流（Agentic Workflow）演进，这种模式的瓶颈日益凸显：

* **上下文污染与指令漂移**：为了覆盖所有边界情况，提示词往往长达数万Token，导致模型注意力分散，产生“指令漂移”，即在长对话中遗忘或混淆初始指令
* **复用性与维护性极差**：复杂的业务逻辑被硬编码在对话历史中，难以实现跨项目货跨团队的迁移，同时版本控制成本较高。任何细微的流程修改都需要重新测试整个庞大的提示词系统，成本高昂



     与此同时，旨在连接外部工具和数据的**模型上下文协议（Model Context Protocol,MCP）** 虽然解决了“连接性”问题，但暴露了新的挑战：当MCP服务器暴露数十上百个工具的完整JSON Schema时，会造成**上下文爆炸**，占用大量Token窗口, 从而出现上下文爆炸、成本飙升、推理能力下降；并且，**拥有工具连接能力并不等于智能体“知道如何正确使用”这些工具**，存在显著的**能力鸿沟**。



**     新模式的诞生**：Anthropic于2025年10月推出了Agent Skill，旨在解决编码场景的工具调用问题，并于2025年12月18日被确立为**开放标准**，这标志着AI智能体开发从“提示词工程”迈入了 **“技能工程”** 的新阶段。其核心设计理念是**将连接性与能力分离**：**MCP专注于提供标准化的工具访问接口，而Skills则专注于封装领域专业知识和工作流程，****教导智能体“如何组合使用这些工具”**、

## 三、Agent Skills定位
###    3.1、渐进式披露：破解上下文困境
           Agent Skills 最核心的创新是渐进式披露(Progressive Disclosure) 机制。这种机制将技能信息分为三个层次, 智能体按需逐步加载, 既确保必要时不遗漏细节, 又避免一次性将过多内容塞入上下文窗口。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**第一层:  元数据Metadata - ****认知索引的建立**

    Skills设计中, 核心是一个Markdown格式的SKILL.md文件, 文件开头的YAML Frontmatter（前置元数据）定义了**Skills的****技能名称（Name）和描述（Description）**, 而Agent启动时, 会扫描所有安装的Skills文件夹, 但仅读取每个SKILL.md的Frontmatter部分。



**第二层: 技能主体Instructions - ****程序性知识的激活**

    只有判断某个skills与当前任务高度相关时, Agent才会读取Skills的SKILL.md文件内容, 将详细的指令、注意事项、示例等加载到上下文中。



**第三层: 附加资源 Script & Reference**

    对于更复杂的技能，`SKILL.md` 可以引用同一文件夹下的其他文件：脚本、配置文件、参考文档等。智能体仅在需要时才加载这些资源。



###    3.2、沙箱与代码执行器（Code Execution Tool）：提升确定性
    Agent Skills 的强大之处在于其与 Code Execution Tool 的无缝集成。模型不再试图通过概率最大的文本生成来解决复杂的数学运算或数据处理问题*（这是 LLM 的弱点）*，而是通过编写或者执行 Python 代码来获得**确定性的结果**。

       例如: 一个 PDF 处理技能的文件结构可能是：

```
skills/pdf-processing/
├── SKILL.md              # 主技能文件
├── references/
    ├── api_reference.md  # PDF处理 API参考文档和代码示例
└── scripts/              # PDF 处理脚本
    ├── extract_text.py     # PDF 提取文本
    ├── rotate_pdf.py       # PDF 旋转页面
    ├── merge_pdf.py        # PDF 合并
    ├── extract_tables.py   # PDF 提取表格
    ├── extract_images.py   # PDF 图片处理能力
    └── split_pdf.py        # PDF 拆分
```
 在 `SKILL.md` 中，可以这样引用附加资源：

* 当需要执行 PDF 解析时，智能体会运行 scripts下面的 脚本
* 例如: 当遇到表格，才会加载  extract_tables.py并执行
* 例如: 当遇到图片，才会加载 extract_images.py并执行
* 模板文件只在需要生成特定(markdown、JSON、CSV)三种格式文档时访问

这种设计有两个关键优势：

1. **无限的知识容量**：通过脚本和外部文件，技能可以"携带"远超上下文限制的知识。例如，一个数据分析技能可以附带一个 1GB 的数据文件和一个查询脚本，智能体通过执行脚本来访问数据，而无需将整个数据集加载到上下文中。
2. **确定性执行**：复杂的计算、数据转换、格式解析等任务交给代码执行，避免了 LLM 生成过程中的不确定性和幻觉问题。

###    3.3、Agent Skills vs MCP
       Agent Skills 是一种标准化的程序性知识封装格式。可以简单理解: MCP 为智能体提供了"手"来操作工具，而Skills 提供了"操作手册"或"SOP（标准作业程序）"，也能换句话说: Skills是一种新的AI任务执行范式,  教导智能体如何正确使用这些工具,  而不是新的模型能力, 也不是简单的功能拓展, 它是将原本隐含在Prompt中的「如何工作」, 从模型内部拆解出来,  显式化、结构话、可复用、可组合, 形成一套标准化的执行协议。核心要点如下:

*      Skill能力模块与多功能连接平台（MCP）互为补充。通过能力模块实现知识共享，借助多功能连接平台（MCP）完成功能扩展，二者协同使用能发挥最佳效果！
* **     Skills 更像“把 SOP 打包”**：流程、清单、产物格式这些东西，装上就能用。
* **     MCP 更像“统一接口”**：把 GitHub、Notion、浏览器、数据库这类外部系统能力接进来。



![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


###   3.4、MAPS框架来审视Agent skills
## M mindest - 心智模式
    从写Prompt, 到把它资产化的一个过程, 相当于把隐性的知识, 显性化、模块化

这就不再是我知道该怎么做, 而是把它封装成了可以复用的模块。    

## A architecture - 架构阶段
    skills 可以作为中间层,它可以连接你的prompt 、Agent、智能体, 可以通过软编排把一项任务的声明过程(也就是它的流程过程) 和它的执行过程进行分离, 然后你的判断逻辑都变成可以版本化, 可以共享的数字资产。

## P prompt - 人机模式
   prompt 不再是临时的指令了, 这些prompt就会变成封装在Skills里面的规范, 而Skills的特点: 渐进式披露, 只在需要的时候加载, 从而节省大量的Token。同样, 每一个Skills, 我们可以进行独立的迭代和优化, 从而具有很好的可测试性。

## S system - 系统化
    skills 不是一个孤立的功能, 它是可以和MCP工具调用, 多Agent进行协作的一个功能, 它相当于是从一个单点的工具到完整的工作, 同样还有一个可组合性,sub-agents可以被多个Skills复用, Skills之间也是可以相互调用, 互相可以协同。



## 四、Agent skills创建
###    4.1 **Skills 的文件结构**
```
├── SKILL.md              # 必备核心
    元数据 + 核心指令, 控制在500行以内
├── assets                # 模版静态文件
    Agent 直接复制到结构模板
├── references            # 渐进式加载        
    补充资料, 用指令按需加载
└── scripts/              # 确定性脚本
    单一功能CLI, 输出清晰
```
###    4.2 编写规范
####        4.2.1 Frontmatter规范
  Agent 只看 name  + description 决定是否加载

#####             **指令名称name**
                 **目录一致性**: name 与 根目录(文件夹名称) 保持一致 

**                 名称格式:** 只能用小写字母(a-z), 数字, 连字符(-), 且最长64个字符

**                 命名语义:  **推荐采用“功能类型+具体操作”的格式, 例如: pdf-processing

#####             **指令说明description**
**                 功能概述**: 简洁明了地描述该技能的主要作用, 例如: 用于从网页中提取结构化数据

**                 输入参数说明**: 列出所有必需和可选的输入参数及类型、含义和示例值

                 **输出结果说明:** 描述技能执行后返回的数据格式、结构和可能的异常情况

**                 适用场景: **指出该技能最适合的应用领域，如“适用于内容爬取、数据清洗等任务”

**                 注意事项: **提醒用户在使用时需注意的限制条件或潜在风险，如“仅支持英文网页解析”

####        4.2.2  指令编写规范
 面向LLM 而非人类的文档

            **渐进式披露**  

                skills.md 写主流程, 细节用 see reference/xxx.md

            **编号步骤 + 决策树 **

                严格编号、分支清晰、消除歧义

           **第三人称祈使句**

                 “Extract the text ..." 而非 “I will extract……”

           **术语 100%一致** 

                 采用领域原生最精确词汇, 全文统一 

####        4.2.3 确定性脚本
 解析、查询等确定性操作, 不让Agent 猜测执行

           **清晰 stdout / stderr  **

                便于 Agent 自判成功并自动修复

           **不含通用库代码**

                只放Skill专用脚本, 库代码走标准仓库目录

           **禁止嵌套子目录**

                 禁止 README、CHANGELOG等人类文档

####        4.2.4 LLM 四步验证
             **Discovery:  **仅用frontmatter 测试触发准确性

             **Logic: **模拟执行、标记幻觉/猜测点

            **Edge Case: **扮演无情QA, 提3~5个破坏性问题

          **  Refinement: **重构为渐进披露 + 增加错误处理

###    4.3 十大原则
         知道skills的文件结构和编写的一些基本规范, 基本知道怎么写一个 SKILL.md, 但怎么把它**「写好」**才是关键. 最后根据看一些优秀的Skill案例, 也在自己的反复试错,  大概归纳下面10个核心原则:

####       **原则一:  精简为王 - 只写 Agent 不知道的事**
            Agent 已经是一个训练有素的"高级开发" ——它知道 React 怎么写、TypeScript 怎么用、怎么发起 HTTP 请求。你不需要教它这些。

            你真正需要写的，是那些**「只存在于你团队脑子里」**的知识：我们的状态管理用 zustand 不用 redux、接口请求统一走 `src/api/request.ts` 里封装的方法、日期用 dayjs 不用 moment...这些"潜规则"Agent 没法从公开知识里推断出来。

```
# ❌ 浪费：Agent 自己就知道怎么用 fetch
 
When making HTTP requests, you can use the fetch API. The fetch 
 
function takes a URL and an options object containing method, 
 
headers, and body...
 
# ✅ 有价值：这是你们团队的私有约定
 
All API calls MUST use the project's request wrapper:
\```ts
import { request } from '@/api/request'
// GET
const users = await request.getUser('/api/users')
// POST
await request.post('/api/users', { name: 'Winty' })
\```
Do NOT use raw fetch or axios directly.
```
     

####       **原则二:  设置合适的自由度 - 按风险等级调“管控力度”**
            写 Skill 指令就像设计道路——在高速公路上你需要严格的车道线和护栏，在公园小路上随意走走就好。不同任务的风险不同，给 Agent 的"自由空间"也应该不同。我把它分成三档：            

|**管控力度**|**什么时候用**|**实际场景**|
|-|-|-|
|**「松」 **— 只给方向|方案灵活、不会出大问题|"帮我 Review 这段代码"|
|**「中」 **— 给模板|有推荐做法、但允许调整|"按团队规范写一个组件"|
|**「严」 **— 给精确步骤|操作敏感、一步都不能错|"执行数据库迁移"|

**越危险的操作越要"收紧"，越创造性的任务越要"放手"。**

       写一个新的 React 组件, 我会给"中"——提供模板和规范，但具体 JSX 怎么写 Agent 自己判断就好。但如果是修改 Nginx 配置、执行数据库迁移这种，我会给"严"——精确到每一条命令，不留任何发挥空间。



        



####       原则三:  渐进式披露 - 内容分层加载, 别一股脑全塞
           Agent 的上下文窗口就像你的电脑内存——容量有限。如果你把所有规范、文档、示例一股脑全写进 SKILL.md，就像同时开了 200 个浏览器标签页，系统肯定卡死。

           更聪明的做法是**「分层」**：

* **「第一层」**（始终加载）：SKILL.md 里只放最核心的指令和规则，控制在 500 行以内
* **「第二层」**（按需加载）：详细的规范文档、API 参考拆到 `references/` 目录

```
 # React Component Skill
 
## Core Rules
 
1. Named exports only
 
2. CSS Modules for styling
 
3. Co-locate tests
 
 
## Need More Detail?
 
- Naming conventions → see [naming.md](references/naming.md)
 
- State management patterns → see [state.md](references/state.md)
 
- Accessibility checklist → see [a11y.md](references/a11y.md)
```
          当用户只是让 Agent 写个简单组件时，它看 Core Rules 就够了。只有涉及无障碍适配时，Agent 才会去读 `a11y.md`。这样每次执行任务时，上下文窗口里只有"用得着"的内容。

  **注意一个坑：引用文件只支持一层深度。**不要让 `naming.md` 里面再引用 `naming-detail.md`，Agent 大概率不会读到那么深。

####       原则四:  代码示例 > 文字 
           这是我自己写 Skill 最深的一个体会：**「当你发现自己在写第三段"解释"的时候，停下来，换一个代码示例就够了。」**

           Agent 理解代码的能力远强于理解自然语言描述。你用文字写"组件的 Props 要用 interface 定义，命名为组件名 + Props 后缀，放在组件函数的上面"——Agent 可能理解出好几种写法。但你直接贴一个代码示例，它就100%照着来：

```
 ## Custom Hook 规范

\```ts
// ✅ 标准写法 — 直接照这个格式来
export function useUserList(params: UseUserListParams) {
  const [users, setUsers] = useStateUser([])
  const [loading, setLoading] = useState(false)
  const fetch = useCallback(async () => {
    setLoading(true)
    try {
      const data = await request.getUser('/api/users', { params })
      setUsers(data)
    } finally {
      setLoading(false)
    }
  }, [params])
  useEffect(() => { fetch() }, [fetch])
  return { users, loading, refresh: fetch }
}
\```
 
 
 
Naming: `use` + resource name, e.g. `useOrderDetail`, `useCartItems`
 
Return: always return an object (not array), include a `refresh` method
      
```


####       原则五:  设定清晰边界 - 能做、要问、别碰
            Agent 没有"职场常识"。你不告诉它什么不能动，它真可能顺手帮你重构了 `webpack.config.js`，或者把 `.env` 里的密钥提交到仓库里。

```
## 操作边界
 
✅ **放手做：**
 
- 在 `src/components/` 下新建文件
 
- 在 `src/hooks/` 下新建 custom hook
 
- 修改当前任务相关的组件和样式
 
 
 
⚠️ **先问我：**
 
- 要改 `src/shared/` 或 `src/utils/` 里的公共代码
 
- 要新加一个 npm 依赖
 
- 要改路由配置或全局状态
 
 
 
🚫 **绝对不要：**
 
- 动任何 config 文件（webpack/vite/tsconfig/eslint）
 
- 删除或修改已有的测试用例
 
- 在代码里硬编码环境变量或密钥
      
```
####       原则六:  工作流清单模式 - 多步任务用编号清单“锁死”顺序
            让 Agent 写一段代码、一个函数，它很擅长。但让它**「按特定顺序做一连串操作」**，就容易出乱子——跳步、漏步、颠倒顺序都有可能。

```
## 新页面开发流程
 
 
按照以下顺序执行，不要跳步：
 
 
1. 在 `src/pages/` 下创建页面目录和 `index.tsx`
 
2. 在 `src/router/config.ts` 中注册路由
 
3. 编写页面基础结构和布局
 
4. 接入 API 数据，完成主要交互逻辑
 
5. 编写单元测试 `__tests__/index.test.tsx`
 
6. 运行 `npm run test` 确认通过
 
7. 运行 `npm run build` 确认构建无报错
```
          为什么编号清单管用？因为它给了 Agent 两样东西：**「明确的先后顺序」**和**「可追踪的进度」**。Agent 做完第 3 步，它知道下一步该做什么，不需要自己判断。

     

####       原则七:  脚本封装操作
            有一类操作是"不管谁来做，结果都应该一模一样"的——建目录结构、生成模板文件、注册路由、格式化代码。这种操作你用文字描述 10 行，不如包成一个脚本一行搞定。

```
## 创建新组件
 
不要手动创建文件。运行脚手架脚本：
 
\```bash
node scripts/create-component.js UserCard
\```
 
 
脚本会自动完成：
 
- 创建 `src/components/UserCard/` 目录
 
- 生成 index.tsx（含 Props interface 模板）
 
- 生成 UserCard.module.css（含基础类名）
 
- 生成 UserCard.test.tsx（含 render 基础用例）
 
- 在 `src/components/index.ts` 中追加 export
 
 
查看所有选项：`node scripts/create-component.js --help`
```
            **why?**

               **省上下文空间**: 脚本细节不需要出现在 Skill 里，Agent 只要知道"调哪个命令"就行

               **结果 100% 一致: **Agent 手写可能漏掉 export 注册或者文件名大小写写错，但脚本不会

####       原则八:  确认节点 - 交付前设一道"质检门"
            遇到过这种场景：Agent 信心满满地说"搞定了"，你一看——TypeScript 编译报错、甚至 console.log 还留着三四处。 问题不是 Agent 能力不行，而是你没告诉它「交活之前该检查什么」。加一个 Pre-Delivery Checklist，效果立竿见影：

```
## 交付检查（每次完成任务后必须执行）
 
确认以下每一项都通过后，再告诉用户"已完成"：
 
- [ ] 运行 `npx tsc --noEmit` 无报错
 
- [ ] 运行 `npm run test` 全部通过
 
- [ ] 代码中没有 console.log / debugger / TODO 注释
 
- [ ] 新增的 Props 都有 JSDoc 注释
 
- [ ] 可交互元素有 aria-label 或 role 属性
 
- [ ] 组件在不传任何 props 时不会崩溃（有合理默认值）
 
- [ ] 新增文件已在 barrel file 中 export
```
####       原则九:  用参数让 Skill "一鱼多吃"
           不太可能为 `UserCard`、`ProductCard`、`OrderCard` 各写一个 Skill 吧？用参数化设计，一个 Skill 就能通吃所有组件的生成。

       核心思路是：把可变的部分抽成参数，固定的部分写成规则。

```
## 输入参数
 
 
 
| 参数 | 必填 | 默认值 | 说明 |
 
|-----|------|-------|------|
 
| 组件名称 | 是 | - | PascalCase，如 UserCard |
 
| 样式方案 | 否 | css-modules | 可选 css-modules / tailwind |
 
| 是否生成测试 | 否 | 是 | 设为"否"可跳过测试文件 |
 
| 是否生成 Story | 否 | 否 | Storybook 文件 |
 

 
## 输出文件
 
 
根据参数生成以下文件：
 
-`src/components/{组件名称}/index.tsx` ← 始终生成
 
-`src/components/{组件名称}/{组件名称}.module.css` ← 样式方案为 css-modules 时
 
-`src/components/{组件名称}/{组件名称}.test.tsx` ← 开启测试时
 
-`src/components/{组件名称}/{组件名称}.stories.tsx` ← 开启 Story 时
```


####       原则十：告诉 Agent 你的项目有哪些"趁手工具"
            大多数成熟项目都有一堆好用的 npm scripts 和 CLI 工具，但 Agent 完全不知道它们的存在。你不说，它就会自己"手搓"一个本该一行命令搞定的操作。

       在 Skill 里**「列出项目已有的工具清单」**，相当于给 Agent 发了一套"装备"：

```
## 项目工具箱
 
本项目提供了以下开发工具，请优先使用：
 
| 命令 | 用途 | 什么时候用 |
 
|-----|------|-----------|
 
| `npx plop component` | 创建组件脚手架 | 新建任何 React 组件时 |
 
| `npm run codegen` | 从 OpenAPI 生成 API 类型 | 后端接口有更新时 |
 
| `npm run analyze` | 分析打包体积 | 添加新依赖或大改动后 |
 
| `npm run lint:fix` | 自动修复 lint 问题 | 代码写完后 |
 
| `npm run test:visual` | 跑视觉回归测试 | 改了 UI 样式后 |
 
 
## 什么时候用工具 vs 手写
 
-**用工具**：脚手架搭建、代码生成、构建部署、格式化
 
-**手写**：业务逻辑、自定义 Hook、复杂交互组件
 
创建新组件时，**始终**优先用 `npx plop component` 而不是手动建文件。
```
## 五、实践解析
### 5.1 接口模块Actions 封装
### **未使用Skill**
### **使用Skill**
**处理流程:**

   初版版本:

      1、人工编写接口封装公共信息

      2、人工统计接口路由

      3、人工整理接口文档, 手动输出接口出入参数类型定义

      4、人工根据接口路由与接口出入参数类型定义, 进行手动出入接口封装

  联调阶段:

      1、前后端沟通对齐,  再人工更新接口封装信息



耗时:  预估20分钟/每个接口

**处理流程:**

   初版版本:

     1、人工编写接口封装公共信息

     2、获取iapi授权信息、ID等信息, 并放入指定目录中

     3、使用xxx技能, 生成接口路由文件、接口出入参数类型定义、接口封装文件

   联调阶段:

       1、前后端沟通对齐,  再使用xxx技能直接更新接口封装信息





耗时: 预估2分钟/每个接口



   

* **fetch.ts 公共信息编写**

```
import {createFactory, Options} from 'axios-interface';
import {toast} from 'acud';
import {get} from 'lodash';

const CODE_MESSAGE: any = {
    400: '400：发出的请求有错误，服务器没有进行新建或修改数据的操作。',
    401: '401：用户没有权限（令牌、用户名、密码错误）。',
    403: '403：用户得到授权，但是访问是被禁止的。',
    404: '404：发出的请求针对的是不存在的记录，服务器没有进行操作。',
    406: '406：请求的格式不可得。',
    410: '410：请求的资源被永久删除，且不会再得到的。',
    422: '422：当创建一个对象时，发生一个验证错误。',
    500: '500：服务器发生错误，请检查服务器。',
    502: '502：网关错误。',
    503: '503：服务不可用，服务器暂时过载或维护。',
    504: '504：网关超时。'
};

const DEFAULT_CONFIG = {
    timeout: 1000 * 60
};

export const apiBaseUrl = '/api/agent/version';

export const options: Options = {
    baseURL: apiBaseUrl,
    ...DEFAULT_CONFIG,
    validateStatus: () => true,
    onResolve(response) {
        const {status, statusText, config, data} = response;
        if (status > 400 || status < 200) {
            const error = new Error(
                `API ${config.url} status is ${status} (${statusText})`
            );
            return Promise.reject(error);
        }
        
        if (data.code && data.code !== 0) {
            return Promise.reject(new Error(
                typeof data?.message === 'object' ? (data.message?.global || '请求出错')
                    : (data?.message || '请求出错！')
            ));
        }

        if (response.status >= 300) {
            throw new Error(String(response.status));
        }

        return data;
    },
    onReject(error) {
        const errorCode = get(error, 'response.status');
        const errorMessage = (errorCode && CODE_MESSAGE[errorCode]) ? CODE_MESSAGE[errorCode] : error.message;
        toast.error({
            message: '报错提示',
            description: errorMessage,
            duration: 5
        });
    }
};

export const createInterface = createFactory(options).createInterface;
```


* **接口路由统计 - api.ts 生成**

![](/personal-site-mvp/img/doc-placeholder.svg "")


* **接口出入参数类型定义 - index.model.ts生成**

![](/personal-site-mvp/img/doc-placeholder.svg "")


* **接口封装 - index.api.ts生成**

![](/personal-site-mvp/img/doc-placeholder.svg "")


* **联调阶段- 接口文档更新**

    如: 文件上传从单文件到多文件

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 5.2 蓝图前端版本查询以及流水线分支确认
### **未使用Skill**
### **使用Skill**
**处理流程:**

  查询蓝图平台客户环境前端版本链路：

     进入蓝图平台=>点击客户项目=>点击软件服务=>点击前端包=>找到对应的前端服务的版本号

  查询产品对应版本号的流水线链路：

     进入蓝图平台=>点击包管理=>点击组件CI发布记录=>查询对应的产品版本号信息=>跳转版本号对应的流水线

  查询流水线对应的分支以及commit

     找到流水线=>找到对应的分支以及提交记录



弊端：

   繁琐：整个链路需要各个平台跳转查询，操作很繁琐。

   耗时：查询过程链路比较长，也很耗时。

   学习成本高：学习前端查询链路还是有一定成本的，需要梳理文档供大家学习。





耗时:  预估5分钟

**处理流程:**

   初版版本:

       1、封装查询蓝图版本的skill+mcp

       2、查询完产品对应的版本号之后封装跳转到对应流水线的skill+mcp

       3、基于流水线查询对应分支以及commit的skill+mcp

     编排：

          基于这三个skill可以按照从上到下的链路获取到版本对应的完整信息。



优势：

    快速便捷：可以直接在comate平台就能完成整个链路的查询，便捷快速，查询准确，不需要各个平台来回跳转查询。

    学习成本较低：只需要通过自然语言的方式沟通就能获取到用户想要的信息。

     



耗时: 预估1分钟



* **查询蓝图产品版本号：**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


* **查询产品对应的流水线、分支以及commit**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


* **三个skill编排查询：**

![](/personal-site-mvp/img/doc-placeholder.svg "")
* **把当前产品自动切换到项目对应的分支进行问题或者需求的开发：**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


## 六、社区热门Skills排行榜 Top 20
  数据来源：SkillsMP · 2026年1月19日   [https://skillsmp.com/](https://skillsmp.com/)

|**方向**|**Skill名称**|**热度**|**功能介绍**|
|-|-|-|-|
|**开发工作流类**|create-pr|169.7k|自动创建GitHub PR，格式化标题，通过CI校验|
||skill-lookup|142.6k|技能查找与安装器，问什么Skills都能找到|
||frontend-code-review|126.3k|前端代码审查，支持tsx/ts/js文件检查清单|
||component-refactoring|126.3k|组件重构专家，安全拆分和优化React组件|
||github-code-review|48.2k|GitHub代码审查+AI协调，多Agent协同评审|
|**AI/LLM开发类**|cache-components-expert|137.2k|缓存组件专家，优化LLM应用的缓存策略|
||opus-4.5-migration|47.2k|Opus 4.5迁移指南，升级现有Claude应用|
||confidence-check|19.8k|置信度检查，让Claude评估自己的回答可靠性|
||context-engineering|5.5k|上下文工程基础，优化Prompt设计|
||multi-agent-patterns|5.5k|多Agent架构模式，设计协作式AI系统|
|**专项技术类**|dify-frontend-testing|124.9k|Dify前端测试，专为Dify平台优化|
||electron-chromium-upgrade|119.6k|Electron升级指南，Chromium版本迁移|
||zig-syscalls-bun|86k|Zig系统调用，Bun运行时底层开发|
||cloudflare-skill|2.8k|Cloudflare全平台开发，60+产品一站式指南|
|**技能创作与管理类**|skill-writer|96k|技能编写器，帮你创建高质量SKILL.md|
||skill-creator|38.5k|技能创建向导，从零开始设计Skills|
||llm-project-methodology|5.5k|LLM项目方法论，AI项目最佳实践|
|**综合框架类**|obra/superpowers|29.1k|超能力框架，TDD+YAGNI+DRY方法论全家桶|
||awesome-claude-skills|21.6k|社区精选合集，50+经过验证的Skills|
||skillport|229|跨Agent技能管理器，一处管理多处使用|

## 七、未来规划
  **1、逐步拓展接口模块Actions封装内容**

* 从最简单Iapi有哪些url & interferce  到 结合业务构建多个接口服务组合生成的某些具体服务
* 结合接口服务 - 作为中间层, 为列表页、详情页、创建页快速搭建页面的Agent skills 提供作为参数, 提供的业务模块信息

#####   2、**团队协作: 版本管理、文档规范、安全审查**
* **用项目级 **`.claude/skills/`** + Git 提交**实现团队共享；社区明确表示克隆仓库即可自动获得访问。
* **建立“Skill 评审门禁”**：部署前按验证清单检查 YAML、脚本、引用、长度、安全与环境变量。
* **最小权限原则**：敏感操作限制为只读工具或受控脚本，并通过 hooks 增加前置校验

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
