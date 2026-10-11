---
title: "Short_Mem Pipeline Bug Fixes & Principles"
description: "Opencode治好了我的FOMO"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Opencode治好了我的FOMO.md"
---
Opencode治好了我的FOMO

#### 🧑‍🏫 案例作者：[@宁英松](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：需求、设计、开发、测试、全流程、通用、办公
#### 🔧 使用工具：opencode
#### 📒 案例概要：Manus、Opencode、Cowork、Clawdbot（Openclaw）……工具层出不穷。 前脚 Remotion 干翻剪映，后脚 Pencil 打倒 Figma。 去年前端已死，今年 iOS 爆发。
上周还在嘲笑苹果，这周默默下单 Mac。 在这个每天都革昨天命、日日都是 AGI 的时代，大家不要 FOMO！

“Talk is cheap, show me your code”… is outdated
“Code is cheap, show me your prompt”
```
Manus、Opencode、Cowork、Clawdbot（Openclaw）……工具层出不穷。 前脚 Remotion 干翻剪映，后脚 Pencil 打倒 Figma。 去年前端已死，今年 iOS 爆发。
上周还在嘲笑苹果，这周默默下单 Mac。 在这个每天都革昨天命、日日都是 AGI 的时代，大家不要 FOMO！

“Talk is cheap, show me your code”… is outdated
“Code is cheap, show me your prompt”
```
## Opencode是什么：
* OpenCode 不仅仅是一款开源的 AI 智能体，它更是一个打破了编辑器与模型边界的全能数字工坊。无论你身处终端、IDE 还是桌面应用，它都能通过 LSP 深度集成理解代码上下文，利用多会话并行处理复杂任务，并支持[链接分享](https://opncd.ai/share/d6Mt1lH0)以便团队协作调试。
    * 它真正的杀手锏在于极致的自由与进化能力。
        * 你不再受限于单一模型，而是可以同时指挥全球顶尖模型协同作战：用 Gemini 写精美的 UI，让 GPT 修复刁钻的 Bug，派 Sonnet 研读晦涩的文档，遇到难题再请 Opus 出山。
        * 同时，它与 OpenAI 官宣合作，不仅完美支持 GPT 系列，还能直接复用你的 GitHub Copilot 和 ChatGPT 额度。
        * 在架构上，OpenCode 利用 CLI 在文件管理上的天然优势，以文件为单位定制 Skill 并卸载上下文，构建了独立的会话管理与共享记忆体系，这一点在体验深度上远超 Trae 等同类产品。



配置一下，你就得到：

    * 一个可以全自动调用所有sub agent的主智能体Sisyphus及规划智能体Prometheus
    * 一个可以循循善诱，通过苏格拉底式引导我们学习的全知老师（skill实现，skill名字叫：/mentor）
    * 一个开箱即用自带三个MCP支持联网搜索的百科全书，内置浏览器(也就是说，可以直接把paper链接，github链接发给opencode，她会忠诚的告诉用户她读了什么）
    * 一个可以记住用户的所有偏好，在使用过程中不断进化的Coding Agent (Supermem & skill实现)

![OMO系统架构](/personal-site-mvp/img/doc-placeholder.svg "OMO系统架构")
![](/personal-site-mvp/img/doc-placeholder.svg "")
在2月2日，opencode的插件又更新了，我的最新配置披露如下：

```
  "$schema": "https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/master/assets/oh-my-opencode.schema.json",
  "google_auth": false,
  "agents": {
    "sisyphus": {
      "model": "google/claude-opus-4-5-thinking"
    },
    "oracle": {
      "model": "openai/gpt-5.2",
      "variant": "high"
    },
    "librarian": {
      "model": "opencode/glm-4.7-free"
    },
    "explore": {
      "model": "google/gemini-3-flash"
    },
    "frontend-ui-ux-engineer": {
      "model": "google/gemini-3-pro",
      "variant": "high"
    },
    "document-writer": {
      "model": "google/gemini-3-pro",
      "variant": "high"
    },
    "multimodal-looker": {
      "model": "google/gemini-3-flash"
    },
    "atlas": {
      "model": "opencode/kimi-k2.5-free"
    },
    "hephaestus": {
      "model": "openai/gpt-5.2-codex",
      "variant": "medium"
    },
    "prometheus": {
      "model": "google/claude-opus-4-5-thinking",
      "variant": "max"
    },
    "metis": {
      "model": "google/claude-opus-4-5-thinking",
      "variant": "max"
    },
    "momus": {
      "model": "openai/gpt-5.2",
      "variant": "medium"
    }
  }
}
```


## Terminal install & Plugins
我的最佳解决方案，配合以下插件食用更佳：

### **官方入口：**[OPENCODE](https://opencode.ai/)
### **必备插件：**
tips:除了需要 npm i -g opencode-ai 安装opencode cli之外，其余的所有配置都可以让opencode自己完成，例如：把github链接发给opencode，她会自己读README来安装，把issue发给opencode，她会自己根据issue修bug，需要更新opencode了，把更新命令发给她就好！

    * [Opencode 插件支持](https://opencode.ai/docs/ecosystem/) & [API/SKILL管理（cc-switch）](https://github.com/farion1231/cc-switch)：基础环境搭建。
    * [Oh my opencode](https://github.com/code-yeongyu/oh-my-opencode)：提升交互体验。
    * [Antigravity auth login](https://github.com/NoeFabris/opencode-antigravity-auth)：神器，支持将 Google 模型引入 Opencode 环境。
    * [Antigravity Tools](https://github.com/lbjlaq/Antigravity-Manager/tree/main)：实时监控用量，心中有数（亦可以使用反代功能，在claude code ,cherry studio等框架中使用google的模型）。

![Antigravity Tools](/personal-site-mvp/img/doc-placeholder.svg "Antigravity Tools")
![CC-SWITCH管理OPENCODE API](/personal-site-mvp/img/doc-placeholder.svg "CC-SWITCH管理OPENCODE API")
### ** API 平台推荐:**
* **国外中转（稳定生产力）：**
    * [Openrouter](https://openrouter.ai/)：支持微信/支付宝支付。如果你对 Anthropic 原生模型有刚需，且追求稳定的生产环境，这是首选（虽然有点烧 Token）。

* **国内高性价比（量大管饱）：**
    * [云雾](https://yunwu.ai/console/topup): 价格实惠，[@杨范芃](https://ku.baidu-int.com?t=mention&mt=contact&id=8001f2c0-fcef-11f0-894f-1d9b1343dded)倾力推荐。
    * **其他 Coding Plan**：[KIMI-K2.5](https://platform.moonshot.cn/console/account)、[GLM4.7](https://bigmodel.cn/glm-coding)、[Minimax](https://www.minimaxi.com/)🌟
    * *注：以上平台均有官方文档支持接入 Opencode。*
    * 从使用的经验来看，安装plugin，配置url，key，opencode的更新，插件的更新等操作直接交给LLM来做就好。后期API和Skill可以用cc-switch自己手动管理。


![GLM等国内平台基本都支持opencode](/personal-site-mvp/img/doc-placeholder.svg "GLM等国内平台基本都支持opencode")
## Skills
### Skill是什么？
Skill 的本质，是**上下文工程 (Context Engineering)**。

* 在生产环境中使用 CLI ，有两大核心优势：**Offload 能力** 与 **文件读写能力**。
* 通过 [agent memory](https://skillsmp.com/zh/skills/yamadashy-repomix-claude-skills-agent-memory-skill-md) 和 [writing skills](https://skillsmp.com/zh/skills/obra-superpowers-skills-writing-skills-skill-md) ，辅以 [supermemory](https://supermemory.ai/)，我们可以将一个常见任务开发成完整的 Pipeline。

**愿景：** 显式地将任务背景、个人偏好、操作规范 Offload 到本地。遇到相似/重复工作内容的时候，用/skill命令调出对应的 memory/skill 给模型，让大模型越来越懂你，同时为团队沉淀资产（如 Rules Skills、复用代码、Bug 修复日志）。

```
---
summary: "Short_Mem Pipeline Bug Fixes: source_id mapping, high-confidence omission, sensitive info field, and confidence calculation"
created: 2026-01-28
updated: 2026-01-28
status: resolved
tags: [bugfix, pipeline, prompt-tuning, short-mem]
related: [/Volumes/508/NewApp/Short_Mem/run_pipeline.py, /Volumes/508/NewApp/Short_Mem/prompt.txt]
---

# Short_Mem Pipeline Bug Fixes & Principles

## 1. Source ID Mapping Error (Critical)

**Symptom:** 
二阶 Persona Traits 的 `source_id` 指向错误的一阶 Interested Content。例如，二阶显示"关注AI"，但引用的 ID 对应一阶的"关注医疗"。

**Cause:**
Pipeline 中对一阶内容进行了重排序（按 confidence 降序），但二阶引用的 `source_id` 仍然是排序前的序号（old index）。

**Fix:**
在排序前后建立映射关系，更新二阶的 `source_id`。

```python
# 1. Record old order
old_order = {id(item): i+1 for i, item in enumerate(interested)}

# 2. Sort interested content
interested.sort(key=lambda x: x.get('confidence', 0), reverse=True)

# 3. Create mapping (old_index -> new_index)
old_to_new = {old_order[id(item)]: i+1 for i, item in enumerate(interested)}

# 4. Update traits source_ids
for item in traits:
    old_src_ids = item.get('source_id', [])
    item['source_id'] = [old_to_new.get(sid, sid) for sid in old_src_ids]
```

**Principle:** 
**任何对列表顺序的改变（Sorting/Filtering），都必须同步更新所有引用该列表索引（Index）的外部数据。**

---

## 2. High Confidence Info Omission (The "Mutton/羊肉" Case)

**Symptom:**
高置信度（conf=40）的 info（如"用户关注羊肉..."）被完全遗漏，未出现在任何一阶记忆中。

**Cause:**
模型在归类时，受限于"强制合并同领域"规则，如果某条 info 与现有主要分类（如餐饮品牌、菜品做法）均有细微差异，模型可能选择丢弃它，而不是单独列出。

**Fix:**
在 Prompt 中添加强制检查步骤（Step 4）：

```markdown
- step4: **高置信度检查**：检查所有confidence≥30的原始info，确认每条都已被纳入某条一阶记忆的source_id中。若有遗漏，必须将其合并到最相关的一阶记忆中，或单独输出为一条新的一阶记忆。
```

**Principle:**
**Don't trust the LLM to cover everything implicitly.** Explicitly require a "coverage check" step for high-value inputs.

---

## 3. Confidence Calculation Reliability

**Symptom:**
模型输出的 confidence 数值经常错误（例如 20+10+10+20+10 = 90，实际应为 70）。

**Cause:**
LLM are bad at arithmetic.

**Fix:**
1. **Prompt**: 移除 confidence 输出要求，只输出 `source_id`。
2. **Code**: 在 Pipeline 中根据 `source_id` 自动计算 confidence。

```python
# 一阶 = Sum(source confs), max 90
total = sum(conf_map.get(sid, 0) for sid in src_ids)
item['confidence'] = min(total, 90)

# 二阶 = Avg(referenced interested confs) * 0.95, max 85
avg = sum(ref_confs) / len(ref_confs)
item['confidence'] = min(round(avg * 0.95, 1), 85)
```

**Principle:**
**Logic in Prompt, Math in Code.** Never ask LLM to do arithmetic if you can do it in code.

---

## 4. Sensitive Info Field

**Symptom:**
User requested to flag sensitive/negative content (e.g., adult content).

**Fix:**
1. **Prompt**: Define `hasSensitiveInfo` field and rules (true/false).
2. **Pipeline**: Ensure field exists in output (default to `False` if missing).
3. **Scope**: Apply to **EACH** item (interested_content item & persona_trait item), not top-level.

**Principle:**
Structured fields must have default fallbacks in code to handle LLM omission.

---

## 5. Prompt Tuning Principle

**Do not add specific cases to prompt.** (Already saved in `prompt-tuning-principles.md`).
Use generalized rules (e.g., "Domain > Action verb") instead of specific examples ("Sheep meat should merge with fish soup").

```
![supermem管理偏好](/personal-site-mvp/img/doc-placeholder.svg "supermem管理偏好")
![supermem管理偏好](/personal-site-mvp/img/doc-placeholder.svg "supermem管理偏好")


### Skill-Mem案例：
* 跨对话记忆召回

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### Skill安装:
****[Skill查找商店](https://skillsmp.com/zh)  [Skill查找商店2](https://awesome-skills.com/)** ** [自动帮我们找skill的skill](https://skills.sh/vercel-labs/skills/find-skills)**   **

通用skill与opencode全局提示：

[附件]
[附件]
### 个性化skill:
[黑客松冠军的claude skills](https://github.com/affaan-m/everything-claude-code?tab=readme-ov-file)

## **实战案例：**
* 在使用 Opencode 辅助设计/探索记忆召回模型的训练时：

    1. 通过上述 Skill，将整个开发过程（数据构建、训练参数选择等）Offload。
    2. 复用价值：下次遇到类似任务，直接调用整个 Pipeline，节省大量重复提示的时间。

### ****[Prompt Tuning Pipeline](https://skillsmp.com/zh/skills/wshobson-agents-plugins-llm-application-dev-skills-prompt-engineering-patterns-skill-md)
[【导入】dimensions_preview_v3_review](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/6WZ6KfmYUf/2de25d25d8a84d?t=mention&mt=doc&dt=sheet)

[【导入】multiturn_dimensions_review](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/6WZ6KfmYUf/4874ef9fa85445?t=mention&mt=doc&dt=sheet)

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
持续优化提示词。(大家可以根据自己的场景，创建一个专门属于自己的prompt tuning pipeline!)

```
---
name: prompt-tuning
description: Use when iteratively improving LLM prompts based on evaluation cases, expected/output comparisons, or quality feedback. Before making prompt changes.
---

# Prompt Tuning Workflow

## Overview

**把 prompt 调优固化成工程闭环**：定义输出契约 → 建基准集 → 跑评测 → 做误差归因 → 提炼可泛化规则 → 改 Prompt → 回归验证 → 版本化。

**核心价值**：把"禁止 case patching"和"可复现的验证门禁"写死，让每一轮迭代都能解释"为什么会更好"，并且不回退。

## When to Use

- 收到 expected/output 对比数据（case 文件、标注反馈）
- Prompt 输出不符合预期格式/风格/覆盖率/准确率
- 需要迭代优化 LLM 输出质量
- 新增约束或规则后需要验证效果

**When NOT to Use:**
- 一次性简单修改（如修错别字、调参数）
- 问题出在数据定义不清而非 prompt 表达

## Non-Negotiables (红线)

### 1. 禁止 Case Patching（最核心禁令）

**禁止**：为修复某个样本/某个ID/某段具体文本而加入特判句、专用例子、专用关键词表。

**允许**：把该失败抽象为"普遍规则"（可覆盖一类输入），并通过回归集证明不伤整体。

| 违规行为 | 正确做法 |
|---------|---------|
| "加个例子修掉这个 case" | 分析失败类型，写可泛化规则 |
| "把这个关键词加到禁止列表" | 定义禁止项的边界标准 |
| "针对 uid=123 加特判" | 找出该 case 代表的失败模式 |

### 2. 禁止一次改太多

每轮变更不超过 3-7 条规则，便于归因。写清每条规则对应的错误类型与预期改善指标。

### 3. 禁止跳过回归门禁

新版本必须：
- 不降低关键指标超过阈值（建议 2%）
- 不破坏 Golden 集中的 must-pass 样本
- 解析/格式错误率保持极低

### 4. 禁止混淆"规则"与"示例"

- 示例用于**解释规则边界**，不用于堆砌覆盖所有失败
- 示例应少、稳定、具代表性
- 优先用"对比示例（Bad vs Good）"而非单独示例

### 5. 禁止把 Dev 集调成"背答案"

反复看同一批失败样本直到"刚好过"，但 Test/新数据崩溃。

**约束**：每轮只在 Dev 看细节；定期用盲测 Test 验收。

## Workflow (8 Phases)

```
┌─────────────────────────────────────────────────────────────────┐
│  1. Contract    2. Baseline    3. Dataset    4. Evaluate        │
│     定义契约       固定基线       划分数据       跑评测          │
│        │             │             │             │               │
│        ▼             ▼             ▼             ▼               │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    5. Error Analysis                     │    │
│  │                       错误归因聚类                        │    │
│  └─────────────────────────────────────────────────────────┘    │
│                              │                                   │
│                              ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              6. Rule Induction (禁止 case patching!)     │    │
│  │                     提炼可泛化规则                        │    │
│  └─────────────────────────────────────────────────────────┘    │
│                              │                                   │
│                              ▼                                   │
│        7. Prompt Update         8. Regression Gate              │
│           更新 Prompt              回归门禁验证                  │
│               │                        │                         │
│               └────────────────────────┘                         │
│                              │                                   │
│                              ▼                                   │
│                    Version & Changelog                           │
│                       版本化发布                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Phase 1: Contract 定义（输出契约）

明确任务边界和输出规范：

- **任务类型**：分类 / 提取 / 生成
- **输入边界**：空输入、超长、噪声、冲突如何处理
- **输出格式**：JSON schema / 标签枚举 / 文本规范
- **硬约束**：必须满足的条件（格式、字段、禁止项）
- **软约束**：偏好但可容忍偏差（风格、长度、排序）

**产物**：`contract.md` 或 prompt 中的"输出规范"部分

### Phase 2: Baseline 固定（可复现基线）

锁定环境变量：

- 模型版本（如 `doubao-seed-1-8-251228`）
- 参数配置（temperature, top_p, max_tokens）
- Prompt 版本（建议用 hash 或版本号）
- 采样策略（单次 / 多次取最优）

**产物**：`prompt_v{n}.txt` + `config.yaml`

### Phase 3: Dataset 划分

| 数据集 | 用途 | 可见性 |
|-------|------|--------|
| **Dev** | 快速迭代调优 | 可看细节 |
| **Golden** | 回归保护（历史坑+边界） | 可看，不可调 |
| **Test** | 最终验收 | 盲测，调优过程禁止偷看 |

**关键**：按实体/用户/主题分组切分，避免泄露。

### Phase 4: Evaluate 评测

**自动检查**：
- 格式解析成功率
- Schema 字段覆盖率
- 约束遵循率（禁止项、必须项）
- 重复率、长度分布

**半自动/人工**：
- 事实性、幻觉率
- 抽象层级是否合适
- 风格是否符合要求

**产物**：`eval_report_v{n}.xlsx` 或 `.md`

### Phase 5: Error Analysis 错误归因

**不是挑几个坏 case 修掉**，而是把失败聚成"类型"，定位缺失的规则/定义。

**推荐错误分类**：

| 类型 | 描述 |
|------|------|
| Format/Schema | 无法解析、字段缺失、类型错误 |
| Constraint | 违反必须/禁止项 |
| Coverage | 漏提取/漏分类/漏要点 |
| Hallucination | 无来源内容 |
| Granularity | 太抽象/太细碎/混合多个域 |
| Ranking/Scoring | 排序不稳定、置信度漂移 |

**产物**：`error_taxonomy.md` + 每类示例

### Phase 6: Rule Induction 规则提炼

**只允许以"可泛化规则"的形式进入 prompt**：

- **定义类**：给出术语边界与判定标准
- **决策类**：何时输出/何时拒绝/何时截断
- **约束类**：格式、字段、风格、去重、排序
- **置信度类**：锚点与区间含义

**产物**：`rule_proposal.md`（见模板）

### Phase 7: Prompt Update 更新

**模块化 prompt 结构**：

```
┌─────────────────────┐
│  Role / Goal        │  ← 角色定位
├─────────────────────┤
│  Output Contract    │  ← schema + 硬约束
├─────────────────────┤
│  Decision Policy    │  ← 边界与拒绝策略
├─────────────────────┤
│  Style Guidelines   │  ← 语气/语言/格式化
├─────────────────────┤
│  Examples (可选)     │  ← 对比示例解释规则
└─────────────────────┘
```

**变更策略**：一次只引入少量规则，便于归因。

### Phase 8: Regression Gate 回归门禁

**硬门禁（不达标直接失败）**：
- 结构化输出：`parse_success_rate >= 99%`
- 禁止项：出现一次即失败
- Golden 集 must-pass 样本：100%

**核心质量指标**：
- 分类：Accuracy / Macro-F1
- 提取：Precision / Recall / F1 / 幻觉率
- 生成：事实错误率 / 必含要点覆盖率

**回归保护**：
- 总体指标下降 > 2% 触发阻断
- 版本对比报告自动生成

## Templates

### Rule Proposal 模板

```markdown
## Rule Proposal: [简短标题]

- **Rule ID**: R-{n}
- **Error type(s) 覆盖**: [Format/Constraint/Coverage/...]
- **一句话规则（可泛化）**: [规则描述]
- **适用范围**: [何时适用]
- **不适用范围**: [何时不适用]
- **对 prompt 的最小改动**: [写在哪个模块，改什么]
- **预期提升的指标**: [如 Coverage +5%, Hallucination -3%]
- **可能引入的副作用**: [以及如何用回归发现]
- **验收标准（门禁阈值）**: [如 Golden 集 must-pass 保持 100%]
```

### Eval Report 模板

```markdown
## Evaluation Report v{n}

**Prompt Version**: v{n} (hash: xxx)
**Model**: doubao-seed-1-8-251228
**Dataset**: Dev (N=xxx)
**Date**: YYYY-MM-DD

### Metrics Summary
| Metric | Value | vs v{n-1} |
|--------|-------|-----------|
| Parse Success Rate | 99.5% | +0.2% |
| Coverage | 85% | +3% |
| Hallucination Rate | 2% | -1% |

### Top Error Types
1. [Type A]: N cases (X%)
2. [Type B]: N cases (X%)

### Sample Failures
[每类 2-3 个代表性样本]
```

## Stop Criteria 停止条件

**何时停止调 prompt**：

1. 核心指标已达目标阈值（如 F1 > 0.9）
2. 连续 2-3 轮迭代指标无明显提升
3. 剩余错误集中在"确定性计算"类问题

## Escalation Triggers 升级触发器

**该换更复杂方案的信号**：

| 信号 | 升级方案 |
|------|---------|
| 错误集中在确定性计算/严格排序/归一化 | 模型输出中间结构，代码做后处理 |
| Prompt 过长导致成本/延迟不可接受 | 拆分任务 / 多轮调用 |
| 主要失败来自数据定义不清 | 先修 contract / 统一金标 |
| 模型稳定性差（同输入多次输出差异大） | 降 temperature / 多采样投票 |

## Task-Specific Adaptations

### Classification 分类任务

- **Contract**: 标签空间枚举、拒识策略、置信度定义
- **验证重点**: Accuracy / Macro-F1 / 边界样本一致性 / 置信度校准

### Extraction 提取任务

- **Contract**: JSON schema、字段必选/可选、去重排序规则、禁止幻觉
- **验证重点**: Parse rate / Schema pass rate / P/R/F1 / 幻觉率 / 覆盖率

### Generation 生成任务

- **Contract**: 必含信息点、风格语气、长度范围、事实性来源约束
- **验证重点**: 事实错误率 / 指令遵循度 / 稳定性 / 人工 rubric 打分

## Quick Reference

| Phase | 产物 | 门禁 |
|-------|------|------|
| Contract | contract.md | - |
| Baseline | prompt_v{n}.txt + config | - |
| Dataset | Dev/Golden/Test 划分 | 无泄露 |
| Evaluate | eval_report.md | - |
| Error Analysis | error_taxonomy.md | - |
| Rule Induction | rule_proposal.md | 禁止 case patching |
| Prompt Update | prompt_v{n+1}.txt | 最小变更 |
| Regression | 回归报告 | 硬门禁通过 |

## Red Flags - STOP and Reconsider

- 想为某个具体样本加特判 → **STOP**，找到可泛化规则
- 一次想改 10+ 条规则 → **STOP**，拆分成多轮
- Golden 集开始"调不动" → **STOP**，检查是否在背答案
- 连续 3 轮指标无提升 → **STOP**，考虑升级方案
- 想删掉失败的测试样本 → **STOP**，这是 case patching 变体

```


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
