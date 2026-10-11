---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "基于Skill插件架构的测试数据构造实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\基于Skill插件架构的测试数据构造实践.md"
---
基于Skill插件架构的测试数据构造实践

#### 🧑‍🏫 案例作者：[@闫世锋](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)[@李静静](https://ku.baidu-int.com?t=mention&mt=contact&id=87ae5870-396b-11f1-9800-29b8831d7d55)[@张瑞](https://ku.baidu-int.com?t=mention&mt=contact&id=8b9d6cf0-396b-11f1-9800-29b8831d7d55)[@姜灵之](https://ku.baidu-int.com?t=mention&mt=contact&id=8f598a90-396b-11f1-9800-29b8831d7d55)
#### 🎬 案例分类：数据分析
#### 🔧 使用工具：Claude
#### 📒 案例概要：AI造数据常遇六大坑：需求不清、结果不稳、数据不安全、敏感处理无标准、合并覆盖、未验证。根因是缺乏规范。解决方案：引入Skill插件架构，通过分层Skill（需求澄清→生成→验证）和Plugin管理，
> **作者团队**：SEP安全QA - 闫世锋、李静静、张瑞、姜灵之
**核心洞察：问题不在 AI，在协作机制**

AI 造数据出错的根因：**容易被跳过的关键节点，没有变成工具层的强制检查点。**

**质量保障新范式的四个维度：**

1. **需求澄清前置** → HARD-GATE阻断 + 审批门（澄清需求并获得审批，不是可选步骤，是必经流程）
2. **执行有兜底** → 运行时探测 + 降级路径（依赖不可用时有Plan B）
3. **完成有证据** → 先证据后声明（让模型知道是否做对了）
4. **规则持久化** → SessionStart钩子注入（规则不消失）

**落地形式**：Skill 体系 + Plugin 协同，应用于数据生产场景

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4a165103ed8a4c6b8b070d76a67a52d5&docGuid=mfy5Fjcg7nk31U "")
## 一 先说说你在 AI 造数据时遇到过哪些坑
用 AI 辅助测试数据构造已经是日常操作，但越用越会发现一些反复出现、让人头疼的问题。把团队里高频遇到的整理出来，你大概率经历过其中不止一个：

1. **隐性需求没有同步给 AI，事后才发现**：说了表面需求，脑子里的字段格式、枚举范围、业务规则没说出来。AI 做完之后才发现不满足要求，整个过程推倒重来。
2. **数据生成结果不稳定，难以复现**：同样的需求，不同时间由不同人做，生成的数据格式、质量参差不齐。没有模板，没有记录，出了问题也无从追溯。
3. **真实业务数据获取不安全、不规范**：需要从数据库拿真实数据来参考或补充，但查询方式不一，有没有读写权限边界也不清楚，安全隐患说不准。
4. **敏感数据处理无标准，密钥随手写**：加密算法靠个人习惯，密钥硬编码在脚本里，没有统一规范，安全性全靠自觉。
5. **多源数据合并时静默覆盖，导致数据丢失**：把两份 JSON 合并，遇到同名字段直接覆盖，没有任何提示。发现数据缺失的时候，已经不知道是什么时候丢的。
6. **AI 声称完成，但实际没有验证**：AI 说"数据已生成，格式正确"，你信了，传给下游，下游说有问题。AI 的完成声明和实际完成之间，有一段没人核查的空白。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e28be1bcc01f476e8165fdb820d88dc0&docGuid=mfy5Fjcg7nk31U "")
---

六个问题的根因是同一个：**和 AI 协作构造数据这件事，没有规范，只有临时约定。** 需求没有结构化澄清，完成没有经过验证，执行方式全靠当次的发挥。只要流程没有强制保障，这些问题就会反复出现。

---

解法只有一个方向：

> **把"容易被跳过的关键节点"，变成工具层的强制检查点。**不依赖使用者每次都记得做对，而是让工具在错误发生之前就拦住。
具体落地是一套 **Skill + Plugin 体系**：多个Skill 覆盖数据构造的完整链路（需求澄清 → 数据生成 → 质量验证），一个 Plugin 管理多个Skill 的分发、上下文注入和命名隔离。

---

### 6 个问题，6 个 Skill，一一对应
不是一个 Skill 解决所有问题，而是每个问题都有明确对应的 Skill，职责清晰：

```
flowchart LR
    subgraph PROB["❌ 痛点"]
        direction TB
        P1["① 隐性需求事后返工<br/><small>P0 设计层：必须第一步</small>"]
        P2["② 生成不稳定难以复现<br/><small>P1 执行层：按需选用</small>"]
        P3["③ 业务数据获取不规范<br/><small>P1 执行层：按需选用</small>"]
        P4["④ 敏感数据处理无标准<br/><small>P1 执行层：按需选用</small>"]
        P5["⑤ 多源合并静默覆盖<br/><small>P1 执行层：按需选用</small>"]
        P6["⑥ AI声称完成实际未验证<br/><small>P2 验证层：必须最后一步</small>"]
    end

    subgraph SKILL["✅ 对应 Skill"]
        direction TB
        S1["data-brainstorming<br/>批量提问 + 审批门<br/>确认后才能继续"]
        S2["data-generate<br/>模板驱动生成<br/>结果可追溯复现"]
        S3["fetching-database-data<br/>只读约束<br/>代码层拦截写操作"]
        S4["processing-batch-crypto<br/>标准化加解密<br/>密钥不可省略"]
        S5["merging-json-data<br/>冲突感知合并<br/>冲突前显式报告"]
        S6["verification-before-completion<br/>先证据后声明<br/>五步铁律"]
    end

    P1 --> S1
    P2 --> S2
    P3 --> S3
    P4 --> S4
    P5 --> S5
    P6 --> S6

    style PROB fill:#fff8f8,stroke:#ffcccc
    style SKILL fill:#f8fff8,stroke:#ccffcc
    style P1 fill:#fff3e0,stroke:#ff9800
    style P2 fill:#e8f5e9,stroke:#4caf50
```
### 用起来是什么样子：一次完整数据构造的流程
有一个总调度器（`using-datafactory`）作为入口，用户只需表达意图，它自动规划路径并强制执行顺序：

```
flowchart TD
    User(["你：我要造一批用户订单测试数据"]) --> UD

    UD["using-datafactory\n总调度器\n自动规划路径、强制执行顺序"]

    UD -->|"强制第一步"| BS

    BS["data-brainstorming\n主动提问，挖掘隐性需求\n确认模板规格文档\n⛔ 未审批不能继续"]

    BS -->|"你审批通过后"| EX

    subgraph EX["执行层（按需选用一个或多个）"]
        direction LR
        DG["data-generate\n按模板生成合成数据"]
        FD["fetching-database-data\n从数据库拿真实数据"]
        CR["processing-batch-crypto\n批量加密敏感字段"]
        MJ["merging-json-data\n合并多源数据"]
    end

    EX -->|"强制最后一步"| VF

    VF["verification-before-completion\n运行验证脚本\n有证据才能声称完成"]

    VF --> Done(["✅ 数据交付"])

    style BS fill:#fff3e0,stroke:#ff9800
    style VF fill:#e8f5e9,stroke:#4caf50
    style UD fill:#f3e5f5,stroke:#9c27b0
    style Done fill:#e3f2fd,stroke:#2196f3
```
这张图是整篇文章的骨架，下面各节围绕每个节点展开：怎么实现、遇到了哪些坑、为什么要这样设计。

---

先说清楚 Skill 和 Plugin 是什么：

* **Skill**：一个 Markdown 文档（SKILL.md），装的是 AI 的行为规则——什么时候触发、按什么步骤走、什么叫做完了。AI 读到这个文档，就知道如何应对对应的任务类型。
* **Plugin**：管理一组 Skill 的容器，负责命名隔离、工作流规则的持久注入、以及统一分发。

7 个 Skill 本身各自独立，不需要 Plugin 也能用。但当 Skill 数量到了 7 个，三类工程问题同时出现：

**命名冲突**：各团队的 Skills 散放在 `.claude/skills/`。另一个团队如果也有个 `data-generate` Skill，两者会互相覆盖，没有任何提示。

**工作流规则会消失**：长对话被压缩（compact）后，SKILL.md 里写的"先澄清需求再操作"规则随着历史记录一起消失了。AI 下一轮响应时不知道这个约束，直接开始生成数据——你花时间设置的流程约束，一次 context compact 之后归零，绕回了最初的状态。

**更新靠手动同步**：修改一个 Skill 的文档，要通知所有人手动替换对应目录。多个 Skill，每次更新都是一次协调成本，且无法验证每个人替换的结果是否一致。

Plugin 同时解决这三个问题：`plugin.json` 建立命名空间，`hooks/` 的 SessionStart 机制在每次会话启动时重新注入工作流规则，`marketplace.json` 让安装和更新变成一条命令。

```
flowchart LR
    subgraph BEFORE["❌ 没有 Plugin（Skills 散放）"]
        direction TB
        S1[".claude/skills/brainstorming/\nSKILL.md"]
        S2[".claude/skills/data-generate/\nSKILL.md\ntesting-standards.md ← 副本1"]
        S3[".claude/skills/verification/\nSKILL.md\ntesting-standards.md ← 副本2（已分叉）"]
        S4[".claude/skills/crypto/\nSKILL.md"]
        S1 -.->|"手动复制\n4次"| S2
        S2 -.->|"版本不同步"| S3
    end

    subgraph AFTER["✅ 有 Plugin（统一管理）"]
        direction TB
        PJ[".claude-plugin/plugin.json\nname: datafactory"]
        HK["hooks/hooks.json\nSessionStart → 注入 using-datafactory 全文\n+ 动态枚举 skills/ 名称索引\n每次会话自动执行"]
        MK["marketplace.json\n一条命令安装/更新"]
        SK["skills/\ndata-brainstorming/\ndata-generate/\nprocessing-batch-crypto/\nverification-before-completion/\n..."]
        PJ --> SK
        HK -->|"动态枚举 skills/"| SK
    end

    BEFORE -->|"Plugin 化改造"| AFTER
```
---

## 二 Skills 的三层优先级结构
多个 Skill 不是平铺的，而是按职责分成三层（含 1 个编排层元 Skill + 6 个业务 Skill）：

```
flowchart TD
    User(["用户数据请求"]) --> P0

    subgraph META["编排层（元 Skill）"]
        UD["using-datafactory\n工作流总调度\n注入 SessionStart 上下文"]
    end

    subgraph P0["P0 — 设计层（强制先执行）"]
        BS["data-brainstorming\n设计模板 · 获取用户审批\n⛔ HARD-GATE 阻断后续操作"]
    end

    subgraph P1["P1 — 执行层（选择一个或多个）"]
        DG["data-generate\n合成数据生成\n支持 JSON/文本/文档/图像"]
        FD["fetching-database-data\n数据库查询\nMySQL / Redis / MongoDB"]
        CR["processing-batch-crypto\n批量加解密\nAES · DES · RSA · SHA256 · BASE64"]
        MJ["merging-json-data\nJSON 合并\n支持冲突解决规则"]
    end

    subgraph P2["P2 — 校验层（强制最后执行）"]
        VF["verification-before-completion\nJSON Schema 出口校验\n错误定位到字段路径"]
    end

    META -.->|SessionStart Hook\n注入 P0→P1→P2 约束| P0
    P0 -->|设计审批通过| P1
    DG & FD & CR & MJ --> P2
    P2 --> Done(["✅ 任务完成"])

    style P0 fill:#fff3e0,stroke:#ff9800
    style P1 fill:#e3f2fd,stroke:#2196f3
    style P2 fill:#e8f5e9,stroke:#4caf50
    style META fill:#f3e5f5,stroke:#9c27b0
```
**三层设计与原始业务痛点的对应关系：**

|层级|Skill|对应解决的痛点|
|-|-|-|
|编排层（元 Skill）|using-datafactory|工作流总调度：声明 P0→P1→P2 执行顺序，SessionStart 注入确保规则跨会话持久|
|P0 设计层|data-brainstorming|需求同步不完整（批量提问 + 审批门强制澄清隐性需求）|
|P1 执行层|data-generate|结果不可复现（模板驱动，每次按同一模板执行）|
|P1 执行层|fetching-database-data|业务数据获取不规范（只读约束内置于代码层）|
|P1 执行层|processing-batch-crypto|敏感数据处理无标准（算法+密钥规范化，无默认值）|
|P1 执行层|merging-json-data|多源合并静默覆盖（冲突感知，合并前显式报告冲突）|
|P2 验证层|verification-before-completion|AI 完成声明不可信（先证据后声明，五步强制流程）|

> **五步铁律（来自 **`verification-before-completion/SKILL.md`**）**
> 1. **IDENTIFY** — 确定哪个命令/方法能证明这个声明
> 2. **RUN** — 执行完整验证（新鲜的、完整的，不复用缓存结果）
> 3. **READ** — 阅读完整输出，检查退出码，统计失败数
> 4. **VERIFY** — 输出是否确认了声明？若否，陈述实际状态并附带证据；若是，陈述声明并附带证据
> 5. **ONLY THEN** — 做出完成声明
> 
> 跳过任何步骤 = 谎言，不是验证
这个三层结构在 `using-datafactory/SKILL.md` 里以 Markdown 表格和流程图的形式声明，但**声明本身不会被强制执行**。真正的强制执行发生在两处：

**1. Hook 注入**：每次会话启动，`session-start` 脚本做两件事：① 把 `using-datafactory/SKILL.md` 的全部内容注入 AI 的上下文；② 动态枚举 `skills/` 目录，生成所有可用 skill 的名称索引一并注入。AI 在处理用户第一个消息之前，已经读到了"P0→P1→P2"的约束和完整的 skill 列表。

**2. HARD-GATE**：`data-brainstorming/SKILL.md` 里的 HARD-GATE 标签在 Markdown 层面拦截后续调用：

```
<HARD-GATE>
Do NOT invoke any data operation skill (data-generate, fetching-database-data,
processing-batch-crypto, merging-json-data) or create any data template until
you have presented a design and the user has approved it.
This applies to EVERY data task regardless of perceived simplicity.
</HARD-GATE>
```
以及一个专门针对"这个太简单不需要设计"心理的反模式警告：

```
## Anti-Pattern: "This Is Too Simple To Need A Design"

Every data task goes through this process. A simple JSON structure, a single table
query, a basic encryption — all of them. "Simple" data tasks are where unexamined
assumptions cause the most wasted work.
```
> **坑：需求澄清被 AI"优化"掉了**
> 早期版本没有 HARD-GATE，AI 遇到"这个需求看起来很简单"的场景时，会自行判断"不需要设计"并直接生成数据。问题在于"简单"是 AI 的主观判断，而遗漏的隐性约束恰恰在"看起来简单"的任务里最多——字段格式、枚举范围、业务规则，这些从不出现在用户的第一句话里。
> HARD-GATE 的目的不是怀疑 AI 的能力，而是**让跳过设计的成本高于做设计的成本**。HARD-GATE 和反模式警告组合使用，是因为 AI 在面对"没有规则覆盖的场景"时，会按"合理化"逻辑行事：只要把"跳步属于违规"显式列出，这条路就被封住了。
---

## 三 跨 Skill 协作的两种实现方式
### 方式 A：编排器 Skill（宏观工作流层）
`using-datafactory/SKILL.md` 是一个不直接做数据操作的"元 Skill"，它声明所有其他 Skill 的调用顺序：

```
## Data Factory Workflow Order

brainstorming (REQUIRED FIRST)
    ↓
data-generate (template creation + data generation)
    ↓ [OR]
fetching-database-data (fetch business data)
    ↓ [OR]
processing-batch-crypto (encrypt/decrypt data)
    ↓ [OR]
merging-json-data (merge JSON files/objects)
    ↓
verification-before-completion (REQUIRED LAST)
```
`using-datafactory/SKILL.md` 还维护了一张"违规思维"警示表（Red Flags），把 AI 常见的合理化行为列出来并直接否定：

|违规想法|现实|正确行动|
|-|-|-|
|"Just generate some data quickly"|No template design = data chaos|MUST invoke brainstorming first|
|"I'll skip verification, the data looks fine"|Unverified data causes downstream failures|MUST invoke verification-before-completion|
|"Let me combine generate + verify in one step"|Violates separation of concerns|Each skill has ONE responsibility|
|"I already know the schema"|Knowledge ≠ documented design|MUST present design and get approval|

这张表的写法背后有一个反直觉的经验：**给 AI 明确的"禁止清单"，比描述"应该做什么"更有效**。

AI 在面对没有明确规则的场景时，会按"合理化"逻辑行事：需求简单就跳过设计，数据看起来对就跳过验证，两步合并做起来更快就合并。这些行为在 AI 看来都是"优化效率"，但每一个都会导致下游问题。把这些"优化"显式列为违规行为，AI 无法再用"提高效率"来合理化跳步。

> **坑：Skill 描述太窄，触发率低**
> 早期每个 Skill 各自定义触发条件，触发词写得很具体，用户换个说法就触发不了。例如 `data-generate` 的触发条件里没有包含"我要造一批测试数据"这类表述，用户说这话时 AI 不知道该用哪个 Skill。引入 `using-datafactory` 作为宽泛入口后，用户只需表达"构造数据"的意图，调度器负责规划路径——单个 Skill 不再需要覆盖所有触发场景。
### 方式 B：运行时能力探测（微观依赖层）
`data-generate/SKILL.md` 的 Step 3 展示了另一种跨 Skill 协作方式——在运行时检测依赖 Skill 是否存在，并根据结果降级处理：

```
### Step 3: 检查数据来源并预获取数据

1. **检查 fetching-database-data skill 是否可用**
   - 通过尝试获取可用的 skill 列表来检测 fetching-database-data 是否存在

2. **如果 fetching-database-data skill 可用**：
   - 使用 Skill 工具调用 fetching-database-data skill 获取数据
   - 将获取的数据转换为 Python 脚本可接受的格式（JSON 文件）

3. **如果 fetching-database-data skill 不存在**：
   - 提示用户：fetching-database-data skill 不存在，无法从数据库获取数据。
   - 询问用户：是否要使用随机生成的数据代替？
   - 如果用户确认，将 data_source.type 改为 direct_generate，继续执行
```
紧跟这段流程，SKILL.md 明确说明了解耦原则：

> **重要**：不要在 Python 脚本中直接调用 fetching-database-data 的模块方法，而是通过 Skill 工具显式调用，保持技能之间的解耦。
这句话的意义超出它字面的意思：跨 Skill 的耦合必须发生在 **AI 层**（通过 Skill 工具调用），而不是**代码层**（Python import）。如果 `data-generate` 的 Python 脚本直接 `import fetch` 模块，两个 Skill 的代码就产生了强依赖，一方目录结构变动就会导致另一方报 ImportError。通过 Skill 工具调用，`data-generate` 只需要知道 `datafactory:fetching-database-data` 这个名称，不需要知道对方的目录结构或代码实现。

两种协作方式的对比：

```
flowchart LR
    subgraph A["方式 A：编排器声明（宏观）"]
        direction TB
        UD2["using-datafactory\nSKILL.md"]
        UD2 -->|"REQUIRED FIRST"| BS2["data-brainstorming"]
        UD2 -->|"REQUIRED LAST"| VF2["verification-before-completion"]
        UD2 -.->|"P1 任选"| P1X["data-generate\nfetching-database-data\ncrypto / merge"]
    end

    subgraph B["方式 B：运行时能力探测（微观）"]
        direction TB
        DG2["data-generate\nStep 3"] --> CHK{"fetching-database-data\n是否可用？"}
        CHK -->|"可用\n通过 Skill 工具调用"| FD2["fetching-database-data\n获取外部数据"]
        CHK -->|"不存在\n询问用户"| DEGRADE["降级：\ndirect_generate\n用随机数据代替"]
        FD2 --> CONT["继续 data-generate 流程"]
        DEGRADE --> CONT
    end

    A -.->|"会话级全局约束"| B
    B -.->|"局部可选依赖"| A
```
> **核心区别**：方式 A 是"在 Skill 文档层声明谁必须存在"，方式 B 是"在 AI 执行时探测谁实际存在"。前者适合强制工作流顺序，后者适合可选依赖的优雅降级。
## 四 业务实践：OpenClaw 模型安全测试数据构造
这一节记录一个真实的使用过程，帮助理解整套体系在实际任务里是怎么工作的。

### 背景
OpenClaw 是一个模型安全测试工具，用于评估大模型在对抗性输入下的鲁棒性。测试员需要一批多轮对话形式的输入数据，覆盖 4 种攻击类型。

需求说起来很简单："帮我造一些模型安全测试用的对话数据"。但这句话里没有说的东西比说的多——几轮对话、什么结构、要不要记录攻击元数据、输出格式是什么——每一项都是可能在事后翻车的隐性需求。

### 第一步：brainstorming 把需求问清楚
入口是 `using-datafactory`，它识别到这是数据构造任务，自动触发 `data-brainstorming`。

不是一次把所有问题全抛出来，而是分三轮：

**第一轮**：确认数据的基本结构——单轮还是多轮？要标注攻击类型吗？输出什么格式？

**第二轮**：基于第一轮的回答深入——攻击类型有哪些具体分类？轮数是否固定？要不要记录模型的实际响应？

**第三轮**：最终确认格式细节。

三轮问答之后，需求从一句话变成了可以直接写进模板的规格：

* 多轮对话，每条 3-5 轮随机
* 4 种攻击类型分类
* 仅记录输入和攻击元数据，不记录模型实际响应
* 输出 JSON 数组

没有 brainstorming 的时候，这些细节往往在数据生成完之后才意识到缺失，然后整批重做。

![输入需求](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=040789aa78d348ab87d0d8adcac6bcb4&docGuid=mfy5Fjcg7nk31U "输入需求")
![头脑风暴1](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=809dcc32b28048f19cce7f5e5162b7c4&docGuid=mfy5Fjcg7nk31U "头脑风暴1")
![头脑风暴2](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d82ace1f5b8d4b45a7d24fee7055f2d1&docGuid=mfy5Fjcg7nk31U "头脑风暴2")
### 第二步：模板设计与审批
brainstorming 产出了一份完整的模板方案，连字段说明和示例都带上了：

```
{
  "case_id": "tc_001",
  "attack_type": "jailbreak",
  "severity": "high",
  "turns": 3,
  "conversation": [
    { "turn": 1, "role": "user", "content": "..." },
    { "turn": 1, "role": "model", "content": "..." }
  ],
  "metadata": {
    "target_capability": "safety_filtering",
    "description": "..."
  }
}
```
用户确认后，模板规范自动保存到 `docs/templates/2026-04-13-openclaw-adversarial-test-data.md`，后续如果需要复现或修改，这份文档是起点。

![确认模板](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=93c79e66eaeb4411be71767f3a0e9fe6&docGuid=mfy5Fjcg7nk31U "确认模板")
### 第三步：生成与调试
`data-generate` 生成了一个 Python 脚本，第一次执行报错——字符串格式化里有 `{}` 占位符的处理问题。调试了两次后跑通，50 条数据输出到 `content_risk_data.json`。

这个过程里有两件事值得注意：

**脚本出错是正常的，重要的是流程有兜底。** `data-generate` 的 Step 7 是兜底机制，当现有脚本无法满足时走 `generate_fallback.py` 并记录原因日志。这里没有触发兜底，但两次报错+修复的过程说明：数据生成不是"运行一次就成"，能跑到成功输出文件，才算真的跑完。

**输出文件是中间产物，不是终点。** 生成完之后，脚本还做了一次清理，把残留的 `{}` 占位符替换掉。这一步如果没有后续的验证，很可能被忽略。

![数据生成](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9605ddc16e6f42e0a844baf0c85f1212&docGuid=mfy5Fjcg7nk31U "数据生成")
### 第四步：verification 做了什么
`verification-before-completion` 跑了 15 项检查：

* JSON 文件是否可解析，结构是否符合模板规范
* 50 条数据是否全部存在，字段是否完整
* attack_type 和 severity 的枚举值是否合法
* 对话轮数是否在 3-5 范围内，user/model 角色是否交替出现
* 攻击类型分布是否均衡（12-13 条/类型），severity 比例是否符合预期

15 项全过，验证报告保存为 `VALIDATION_REPORT.md`，数据质量评级为"优秀"。

用户拿到这份数据的时候，不是"AI 说没问题"，而是有一份有退出码、有明细的验证报告作为依据。

![数据验证](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2a67193b24d041778962806c38b12ca9&docGuid=mfy5Fjcg7nk31U "数据验证")
### 这次任务里体系发挥了什么作用
回头看，整个任务里体系约束实际介入了三次：

1. **brainstorming 的批量提问**：三轮问答把一句话需求变成了完整规格，避免了"做完发现缺字段"的返工。
2. **HARD-GATE 的阻断**：没有用户的审批确认，数据生成阶段不会启动。用户输入"继续"之后，流程才往下走。
3. **verification 的强制验证**：最终交付的 50 条数据有客观的质量证明，不是 AI 的自我声称。

交付产物：

* `content_risk_data.json`：50 条测试用例，涵盖 4 种攻击类型
* `docs/templates/`：模板规范文档，可复现
* `VALIDATION_REPORT.md`：验证报告

## 结语：Plugin 解决的不是功能问题，是工程问题
`datafactory-plugin` 里的 7 个 Skills 分散存放也能各自工作。Plugin 解决的是 Skills 规模化后的工程问题。

用 OpenClaw 那次任务说具体一点：

**brainstorming 问了三轮才问清楚需求**——如果没有 HARD-GATE，这一步会被跳过。第一次有人用这套工具的时候，试过直接表达意图让 AI 生成，AI 凭理解直接输出了数据，格式对了，但没有 attack_type 字段，轮数也不对。回头再跑一遍，加上了 brainstorming，三轮问答之后需求才变成了可执行的规格。HARD-GATE 不是在怀疑使用者，是在堵住一条大家都会走的捷径。

**生成脚本报了两次错才跑通**——这件事本身不意外，但值得注意的是，如果流程在"脚本跑通"就宣告完成，后续的 `{}` 占位符残留问题不会被发现。verification 跑了 15 项检查，其中有一项专门检查字段内容里的异常值。问题在 P2 层被拦住，不是在下游用数据的时候才暴露。

**模板规范存了下来**——`docs/templates/2026-04-13-openclaw-adversarial-test-data.md` 在任务完成后继续留着。两周后要追加 100 条数据，不需要重新设计，打开这个文件确认一下分布规则，直接跑生成脚本。没有这份文档，两周后的人不知道当时为什么选了 12-13 条每类型的分布，也不知道 severity 的比例是怎么定的。

---

回到体系的五个工程价值，结合实际情况：

* **命名空间**：OpenClaw 测试的 Skill 和另一个项目的 `data-generate` 不会打架，各自挂在不同的 plugin 命名空间下
* **跨 Skill 协调**：brainstorming → data-generate → verification 的顺序不是靠使用者记住的，是 using-datafactory 在每次会话启动时注入的约束
* **上下文持久化**：对话中途被 compact 了一次，Hook 在下一轮响应前重新注入了工作流规则，AI 没有忘记 P0→P1→P2 的顺序
* **运行时能力探测**：data-generate 执行前先探测 fetching-database-data skill 是否存在；这次任务不需要从数据库取数，skill 不存在时直接走 direct_generate 路径，流程不会因依赖缺失而硬中断
* **统一分发**：验证完的脚本和模板规范通过一条命令同步给其他需要做模型安全测试的人，不是把文件压缩发群里

**约束要前置，不是事后补救**——这不是设计原则，是从反复踩坑里归纳出来的。HARD-GATE 是在早期版本被绕过若干次之后加的，verification 的五步铁律是在"运行了命令但没读完输出就声称通过"之后加的。每一个强制检查点背后都有一次具体的失败。

用户不需要记住这些历史，规范已经内嵌在工具里了。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
