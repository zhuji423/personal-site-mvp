---
title: "百度内搜研究 (Baidu Neisou Research)"
description: "百度内网搜索深度研究工具。从 neisou.baidu.com（如流搜索）批量抓取文档并分析总结。使用本地 chromium-browser。"
date: "2026-02-25"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\baidu-neisou-research\\SKILL.md"
name: "baidu-neisou-research"
---

# 百度内搜研究 (Baidu Neisou Research)

> 版本：v1.9.0

基于百度内网搜索（neisou.baidu.com / 如流搜索）的深度研究工具。

## 前置条件

```bash
pip install playwright
# 注意：直接复用本地 chromium-browser，无需执行 playwright install chromium

# 首次使用需要登录（只需一次）
python scripts/search.py --login
```

登录后会保存在独立目录，不影响日常使用的浏览器。

## 步骤1: 搜索索引

```bash
python scripts/search.py --keyword "OpenClaw 实践" --dir ./task_openclaw --pages 5
```

输出: `{dir}/search_results.json`

## 步骤2: 筛选文档

```python
import json

DIR = './task_openclaw'
docs = json.load(open(f'{DIR}/search_results.json'))

# 按标题关键词排除
exclude = ['日报', '周报', '情报', '榜单']
docs = [d for d in docs if not any(kw in d['title'] for kw in exclude)]

# 按标题关键词保留
include = ['实践', '案例', '总结']
docs = [d for d in docs if any(kw in d['title'] for kw in include)]

# 保存筛选结果
json.dump(docs[:20], open(f'{DIR}/selected.json', 'w'), ensure_ascii=False, indent=2)
print(f"筛选后: {len(docs)} 篇")
```

输出: `{dir}/selected.json`

## 步骤3: 抓取内容

```bash
python scripts/fetch.py --dir ./task_openclaw
```

输出: `{dir}/docs/doc_*.md`, `{dir}/fetch_results.json`

---

## 步骤4: 合成报告

由 Agent 执行，**严格按以下流程，禁止跳过任何阶段**。

输出:
- `{dir}/summaries/*.json` - 逐篇摘要
- `{dir}/analysis.json` - 聚类分析
- `{dir}/report.md` - 最终报告

---

## ⚠️ 强制执行规则

```
┌─────────────────────────────────────────────────────────────┐
│  禁止跳过任何阶段！必须按顺序完成：                            │
│                                                             │
│  1. MAP    - 必须逐篇读取，逐篇输出 summary_*.json           │
│  2. REDUCE - 必须基于所有 summary 生成 analysis.json         │
│  3. PACKAGE - 必须基于 analysis.json 生成 report.md          │
│                                                             │
│  为什么必须全部读取？                                         │
│  文档包含公司内部特有的业务信息（术语、系统、流程、数据），     │
│  这些信息大模型不可能预先知道，必须逐篇阅读才能理解。          │
│  跳过任何一篇都可能遗漏关键信息。                              │
│                                                             │
│  违规行为：                                                   │
│  ✗ 只读几篇就生成报告                                        │
│  ✗ 跳过 MAP 直接写报告                                       │
│  ✗ 不输出中间文件                                            │
│  ✗ 编造未读过的内容                                          │
│                                                             │
│  ⚠️ 不接受任何借口：                                          │
│  ✗ "节省 token"                                              │
│  ✗ "高效分析策略"                                            │
│  ✗ "文档较长"                                                │
│  ✗ "已掌握核心信息"                                          │
│  ✗ "快速扫描即可"                                            │
│                                                             │
│  不要考虑成本，必须按要求执行。                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 执行流程详解

### 模式选择

| 模式 | 文档数 | 适用场景 | 流程 |
|------|--------|----------|------|
| **quick** | ≤5篇 | 快速了解、简单问题 | 直接合并→生成报告 |
| **standard** | 6-15篇 | 常规调研 | Map→Reduce→报告 |
| **deep** | 16-30篇 | 深度研究、重要决策 | Map→Reduce→审查→补充→报告 |

### 流程图

```
┌─────────────────────────────────────────────────────────────────┐
│                      合成报告流程                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Phase A: MAP（逐篇提取）                                        │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                           │
│  │ doc_001 │ │ doc_002 │ │ doc_003 │ ...                       │
│  └────┬────┘ └────┬────┘ └────┬────┘                           │
│       ▼           ▼           ▼                                 │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                           │
│  │summary_1│ │summary_2│ │summary_3│ → {dir}/summaries/*.json  │
│  └────┬────┘ └────┬────┘ └────┬────┘                           │
│       └───────────┼───────────┘                                 │
│                   ▼                                             │
│  Phase B: REDUCE（聚类归纳）                                     │
│  ┌─────────────────────────────┐                               │
│  │ 场景聚类 + 最佳实践提炼      │ → {dir}/analysis.json         │
│  └──────────────┬──────────────┘                               │
│                 ▼                                               │
│  Phase C: CRITIQUE（审查补充，deep模式）                         │
│  ┌─────────────────────────────┐                               │
│  │ 识别空白 + 补充调研          │                               │
│  └──────────────┬──────────────┘                               │
│                 ▼                                               │
│  Phase D: PACKAGE（生成报告）                                    │
│  ┌─────────────────────────────┐                               │
│  │ 套用模板 + 引用验证          │ → {dir}/report.md             │
│  └─────────────────────────────┘                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Prompt 模板参考

以下为 Agent 执行 Phase A/B 时参考的 Prompt 模板。

### Phase A: MAP（逐篇提取）

**触发条件**：文档 >5篇 或 总字数 >3万

**⚠️ 批量处理规则（提升效率）**：
```
┌─────────────────────────────────────────────────────────────┐
│  为加快处理速度，支持批量读取多篇文档一起生成 summary！       │
│                                                             │
│  规则：                                                      │
│  1. 每批读取 3-5 篇文档（根据文档长度调整）                  │
│  2. 短文档（<3000字）：每批 5 篇                             │
│  3. 中等文档（3000-8000字）：每批 3 篇                       │
│  4. 长文档（>8000字）：每批 1-2 篇                           │
│  5. 一次性为该批所有文档生成 summary，然后写入各自的文件     │
│                                                             │
│  示例（批量处理 doc_001 到 doc_003）：                       │
│  1. 同时读取 doc_001.md, doc_002.md, doc_003.md             │
│  2. 一次性生成 3 个 summary                                 │
│  3. 分别写入 summary_001.json, summary_002.json, ...        │
│                                                             │
│  注意：                                                      │
│  - 如果 context 不够，减少每批数量                          │
│  - 每个 summary 仍然独立保存为单独文件                      │
└─────────────────────────────────────────────────────────────┘
```

**⚠️ 引用编号规则（必须遵守）**：
```
┌─────────────────────────────────────────────────────────────┐
│  引用编号必须与 fetch_results.json 中的 idx 严格对应！        │
│                                                             │
│  规则：                                                      │
│  1. 先读取 fetch_results.json，获取文档列表和 idx            │
│  2. 按 idx 顺序处理，summary 文件名用 idx：summary_001.json   │
│  3. summary 中的 doc_id 必须是 "doc_001" 格式，和 idx 对应   │
│                                                             │
│  示例（fetch_results.json 中 idx=7 的文档）：                 │
│  - 读取：docs/doc_007_xxx.md                                │
│  - 输出：summaries/summary_007.json                         │
│  - doc_id 字段：{"doc_id": "doc_007", ...}                  │
│                                                             │
│  禁止：                                                      │
│  ✗ 自己编造文档编号                                          │
│  ✗ 使用和 fetch_results.json idx 不一致的编号               │
│  ✗ 跳号或重复编号                                            │
└─────────────────────────────────────────────────────────────┘
```

**System Prompt**:
```
你是技术文档分析专家。从文档中提取结构化要点，保留原文关键片段作为引用依据。

规则：
1. 每个要点必须有原文依据
2. 保留可量化的效果数据
3. 标注信息的置信度（高/中/低）
4. 必须用 Python json.dump 写入文件，禁止直接输出 JSON 字符串
```

**User Prompt**:
```
文档编号：{doc_id}
文档标题：{title}
文档来源：{url}
文档内容：
{content}

提取要点，返回 Python dict 格式（注意：不是 JSON 字符串）：
{
  "doc_id": "{doc_id}",
  "title": "{title}",
  "url": "{url}",
  "scenario": {
    "description": "应用场景描述",
    "evidence": "原文依据片段",
    "confidence": "high|medium|low"
  },
  "approach": {
    "description": "具体做法",
    "steps": ["步骤1", "步骤2"],
    "code_snippets": ["关键代码/配置"],
    "evidence": "原文依据"
  },
  "effect": {
    "description": "效果描述",
    "metrics": ["指标1: 数值", "指标2: 数值"],
    "evidence": "原文依据"
  },
  "problems": [
    {"problem": "问题", "solution": "解决方案", "evidence": "原文依据"}
  ],
  "key_quotes": [
    "最有价值的原文片段1",
    "最有价值的原文片段2"
  ]
}
```

**⚠️ 输出方式（必须用 Python 写入）**：
```python
import json

summary = {
    "doc_id": "doc_001",
    "title": "文档标题",
    "url": "文档URL",
    "scenario": {...},
    "approach": {...},
    "effect": {...},
    "problems": [...],
    "key_quotes": [...]
}

with open("{dir}/summaries/summary_001.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
```

**为什么必须用 json.dump？**
- LLM 直接输出 JSON 字符串时，中文引号 "" 不会被转义，导致 JSON 解析失败
- json.dump 会自动处理所有特殊字符的转义

**输出**：`{dir}/summaries/summary_{doc_id}.json`

---

### Phase B: REDUCE（聚类归纳）

**⚠️ 引用来源规则（必须遵守）**：
```
┌─────────────────────────────────────────────────────────────┐
│  所有引用必须来自 summary 文件中的 doc_id，禁止自己编造！     │
│                                                             │
│  规则：                                                      │
│  1. 读取 summaries/*.json，收集所有 doc_id                   │
│  2. analysis.json 中的 source 字段只能用这些 doc_id          │
│  3. 引用格式统一为 [doc_001]、[doc_002] 等                   │
│                                                             │
│  禁止：                                                      │
│  ✗ 使用 summary 文件中不存在的 doc_id                        │
│  ✗ 自己编造 [doc_xxx] 编号                                   │
└─────────────────────────────────────────────────────────────┘
```

**System Prompt**:
```
你是研究报告专家。将多篇文档要点归类整合，生成结构化分析。

规则：
1. 相似场景合并，保留差异点
2. 每个结论必须标注来源文档编号 [doc_001]
3. 冲突观点并列呈现，不要强行统一
4. 提炼可直接复用的最佳实践
```

**User Prompt**:
```
研究主题：{keyword}
文档要点汇总：
{all_summaries_json}

生成分析结果（JSON格式）：
{
  "theme": "{keyword}",
  "doc_count": {n},
  "categories": [
    {
      "name": "场景类别名",
      "description": "类别描述",
      "doc_refs": ["doc_001", "doc_003"],
      "approaches": [
        {"method": "做法", "source": "doc_001", "evidence": "原文"}
      ],
      "effects": [
        {"metric": "效果", "source": "doc_001", "evidence": "原文"}
      ]
    }
  ],
  "best_practices": [
    {
      "name": "实践名称",
      "scenario": "适用场景",
      "steps": ["步骤1", "步骤2"],
      "source": ["doc_001", "doc_002"],
      "confidence": "high|medium|low"
    }
  ],
  "common_problems": [
    {
      "problem": "问题",
      "cause": "原因",
      "solution": "解决方案",
      "source": "doc_005"
    }
  ],
  "gaps": ["未覆盖的方面1", "未覆盖的方面2"],
  "conflicts": [
    {"topic": "冲突点", "view_a": "观点A [doc_001]", "view_b": "观点B [doc_003]"}
  ]
}
```

**输出**：`{dir}/analysis.json`

---

### Phase C: CRITIQUE（审查补充，deep模式）

仅 **deep** 模式执行。

**检查清单**：
- [ ] 是否有重要场景未覆盖？
- [ ] 效果数据是否充分？
- [ ] 是否存在未解决的冲突观点？
- [ ] 最佳实践是否有足够案例支撑？

**如发现空白**：
1. 列出需要补充的方向
2. 返回步骤1-3补充搜索和抓取
3. 重新执行 Phase A-B

---

### Phase D: PACKAGE（生成报告）

**⚠️ 长报告分段写入（必须遵守）**：
```
┌─────────────────────────────────────────────────────────────┐
│  防止 output token 上限（8192）导致写入失败！                 │
│                                                             │
│  规则：                                                      │
│  1. 创建报告目录：{dir}/report/                              │
│  2. 分章节写入多个文件，每个文件不超过 3000 字                │
│  3. 文件命名：01_摘要.md, 02_场景.md, 03_实践.md, ...         │
│  4. 写完所有章节后，用 bash 合并：                            │
│     cat {dir}/report/*.md > {dir}/report.md                 │
│                                                             │
│  章节拆分建议：                                               │
│  - 01_摘要.md: 标题 + 摘要                                   │
│  - 02_场景.md: 场景分类                                      │
│  - 03_实践.md: 最佳实践                                      │
│  - 04_问题.md: 常见问题                                      │
│  - 05_冲突.md: 观点冲突 + 研究空白                           │
│  - 06_附录.md: 入门路径 + 文档索引                           │
│                                                             │
│  禁止：一次性生成完整报告（会触发 token 上限导致 JSON 截断）   │
└─────────────────────────────────────────────────────────────┘
```

**⚠️ 上下文连贯性（必须遵守）**：
```
┌─────────────────────────────────────────────────────────────┐
│  分段写入时，确保章节之间术语、数据、引用一致！               │
│                                                             │
│  规则：                                                      │
│  1. 生成第 N 章节时，将前面所有章节（1 到 N-1）完整内容放入   │
│  2. 不要用摘要代替原文，直接包含已生成章节的全部输出          │
│  3. 保持一致：术语命名、文档编号、数据引用、人名/系统名       │
│                                                             │
│  示例（生成 03_实践.md 时）：                                 │
│  ```                                                        │
│  [已生成章节内容]                                            │
│  {01_摘要.md 的完整内容}                                     │
│  {02_场景.md 的完整内容}                                     │
│                                                             │
│  [本章节任务]                                                │
│  现在请继续生成"最佳实践"章节...                             │
│  ```                                                        │
│                                                             │
│  为什么不用摘要？                                            │
│  - 摘要会丢失细节，导致术语不一致                            │
│  - 原文包含具体的 doc_xxx 引用，便于保持一致                 │
│  - 每章节 <3000 字，累计通常不会超出上下文限制               │
└─────────────────────────────────────────────────────────────┘
```

**防幻觉协议（必须遵守）**：
```
⚠️ 严格规则：
1. 每个事实陈述必须标注来源 [doc_001]
2. 区分"文档原文"和"分析推断"
3. 无来源的推断必须标注"[推断]"
4. 禁止编造引用、数据、案例
5. 不确定时写"文档未提及"而非猜测
```

**报告模板**：

```markdown
# {keyword} 百度内网研究报告

> 研究时间：{date} | 文档数量：{doc_count}篇 | 模式：{mode}

---

## 摘要

{3-5句话概括核心发现，每句标注来源}

---

## 一、场景分类

### 1.1 {场景名称}（{count}篇：{doc_refs}）

**场景描述**：
{description} [doc_001]

**典型做法**：
1. {approach_1} [doc_001]
2. {approach_2} [doc_003]

**效果数据**：
- {metric_1} [doc_001]
- {metric_2} [doc_003]

**代表案例**：
> "{原文引用}" — [doc_001]《{title}》

---

## 二、最佳实践

### 2.1 {实践名称}

| 维度 | 内容 | 来源 |
|------|------|------|
| 适用场景 | {scenario} | [doc_001] |
| 具体步骤 | 1. {step1}<br>2. {step2} | [doc_001, doc_002] |
| 注意事项 | {limitations} | [doc_003] |
| 置信度 | {high/medium/low} | 基于{n}篇文档 |

---

## 三、常见问题

| # | 问题 | 原因 | 解决方案 | 来源 |
|---|------|------|----------|------|
| 1 | {problem} | {cause} | {solution} | [doc_005] |

---

## 四、观点冲突 [如有]

| 议题 | 观点A | 观点B | 建议 |
|------|-------|-------|------|
| {topic} | {view_a} [doc_001] | {view_b} [doc_003] | {建议} |

---

## 五、研究空白 [如有]

以下方面文档未充分覆盖：
- {gap_1}
- {gap_2}

---

## 六、入门路径

基于文档分析，建议的学习路径：

1. **入门**：{step_1} [doc_002]
2. **进阶**：{step_2} [doc_005]
3. **深入**：{step_3} [doc_008]

---

## 附录A：文档索引

**⚠️ 必须从 fetch_results.json 生成，禁止自己编造！**

| ID | 标题 | 字数 | 链接 |
|----|------|------|------|
| doc_001 | {fetch_results[0].title} | {fetch_results[0].len} | [链接]({fetch_results[0].url}) |
| doc_002 | {fetch_results[1].title} | {fetch_results[1].len} | [链接]({fetch_results[1].url}) |
| ... | ... | ... | ... |

```python
# 生成附录A的参考代码
import json
results = json.load(open('{dir}/fetch_results.json'))
for r in results:
    print(f"| doc_{r['idx']:03d} | {r['title'][:30]} | {r['len']} | [链接]({r['url']}) |")
```

---

## 附录B：引用验证

报告中所有 `[doc_xxx]` 引用均可在附录A中查证原文。

**验证方法**：
1. 提取报告中所有 `[doc_xxx]` 引用
2. 检查每个引用是否存在于 fetch_results.json
3. 不存在的引用必须删除或修正

```python
# 验证脚本参考
import json, re
report = open('{dir}/report.md').read()
refs = set(re.findall(r'\[doc_(\d+)\]', report))
results = json.load(open('{dir}/fetch_results.json'))
valid_ids = {f"{r['idx']:03d}" for r in results}
invalid = refs - valid_ids
if invalid:
    print(f"⚠️ 无效引用: {invalid}")
else:
    print("✅ 所有引用已验证")
```

**验证状态**：✅ 所有引用已验证
```

---

### 验证清单

生成报告后执行：

```
□ 每个事实陈述都有 [doc_xxx] 标注
□ 所有 [doc_xxx] 在附录A中有对应条目
□ 无"可能"、"大概"等模糊表述（除非标注[推断]）
□ 效果数据有原文依据
□ 冲突观点已标注双方来源
□ 研究空白已明确列出
```

---

## 任务目录结构

```
task_openclaw/
├── search_results.json      # 步骤1: 搜索索引
├── selected.json            # 步骤2: 筛选结果
├── fetch_results.json       # 步骤3: 抓取元数据
├── docs/                    # 步骤3: 文档正文
│   ├── doc_001_xxx.md
│   └── ...
├── summaries/               # 步骤4 Phase A: 逐篇摘要
│   ├── summary_001.json
│   └── ...
├── analysis.json            # 步骤4 Phase B: 聚类分析
└── report.md                # 步骤4 Phase D: 最终报告
```
