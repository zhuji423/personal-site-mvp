---
title: "Skill搜索器"
description: "当用户提出可能需要专业能力的问题，且本地已安装的skills都不适合时，从Skills中心（Comate内部平台或开源skills.sh生态）推荐并安装新skills。获取可用skills列表，分析用户意图，展示Top 3相关选项，并在安装前预览详细信息。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\find-skills-comate\\SKILL.md"
name: "find-skills"
version: "20260410"
---

# Skill搜索器

从Skills中心搜索并安装新skills，支持Comate内部平台和开源skills.sh生态，优先内部、自动降级。

## 触发条件

**自动触发：**

- 用户提出的问题或任务可能受益于专业skill
- 本地已安装的skills都不适合处理该问题
- 存在远端平台上的某个skill可能更好地处理该请求的可能性

**不触发：**

- 请求简单且不需要专业知识
- 本地已有skill可以处理（本地优先）
- 用户询问与工具使用无关的一般信息

## 来源策略

优先使用Comate内部平台，不可用时自动降级到开源生态：

| 来源               | 获取方式                                                                           | 适用场景               |
| ------------------ |--------------------------------------------------------------------------------| ---------------------- |
| Comate内部平台     | `python3 ${COMATE_SKILL_DIR}/scripts/fetch_skills.py --page 1 --page-size 200` | Comate用户，内网环境   |
| 开源生态（skills.sh） | `npx skills find [query]`                                                      | 通用场景，内网不可达时 |

> 若两个来源均不可用，告知用户并直接用现有能力处理请求。

## 安装位置规则

根据用户意图和skill来源确定安装位置：

| 意图            | 来源       | 安装路径                         | 说明                       |
| --------------- |------| -------------------------------- | -------------------------- |
| 安装到当前项目  | Comate     | `.comate/skills/<skill_name>/`   | 仅当前项目可用，随仓库共享 |
| 安装到全局/个人 | Comate     | `~/.comate/skills/<skill_name>/` | 所有项目可用，个人专属     |
| 安装到当前项目  | 开源生态 | `.agents/skills/<skill_name>/`   | 仅当前项目可用，随仓库共享 |
| 安装到全局/个人 | 开源生态 | `~/.agents/skills/<skill_name>/` | 所有项目可用，个人专属     |

**意图识别关键词：**

- **项目级**：用户提及"当前项目"、"这个仓库"、"项目里"、"团队共享"等
- **全局级**：用户提及"全局"、"个人"、"所有项目"、"通用"等

**无法识别时，主动询问：**

```
请问你希望将技能安装到哪里？

1. **当前项目** (.comate/skills/ 或 .agents/skills/ ) - 仅当前项目可用，会随代码仓库共享给团队
2. **全局个人** (~/.comate/skills/，~/.agents/skills/ 或 npm全局) - 所有项目通用，仅自己可用

请选择 1 或 2：
```

安装时若目标目录不存在，自动创建。

## 使用流程

### 步骤1：获取可用Skills

**优先尝试Comate内部平台：**

注意：如果第一页（page=1）没有找到，请继续遍历下一页，直到展示出Comate平台所有的skill之后再判断skill是否存在

```bash
python3 ${COMATE_SKILL_DIR}/scripts/fetch_skills.py --page 1 --page-size 200
```

脚本输出包含skill名称和描述的JSON。

**若Comate平台不可用（脚本失败），自动切换到开源生态：**

```bash
npx skills find [query]
```

其中 `[query]` 根据用户请求中的关键词自动生成（如 `react performance`、`pr review` 等）。

### 步骤2：分析和推荐

根据获取到的skill描述分析用户请求的相关性，考虑：

- 用户问题中的关键词和领域术语
- 请求的任务类型
- 用户意图与skill描述之间的语义相似度

选择Top 3最相关的skills，不足3个则只展示匹配度高的。

### 步骤3：向用户展示选项

```
发现以下技能可能对你有帮助:

1. **skill-name-1** - skill功能描述  （来源: Comate内部 / skills.sh）
2. **skill-name-2** - skill功能描述  （来源: Comate内部 / skills.sh）
3. **skill-name-3** - skill功能描述  （来源: Comate内部 / skills.sh）

需要我帮你安装哪个技能？（我会先展示详细信息供你确认）
```

### 步骤4：确定安装位置

用户选择skill后，根据上下文判断安装位置：

- 如果用户已明确表达安装位置意图，直接使用对应路径
- 如果无法判断，主动询问用户（参见"安装位置规则"）

### 步骤5：获取下载链接（仅Comate来源）

```bash
python3 ${COMATE_SKILL_DIR}/scripts/get_download_url.py <skill_name>
```

> 开源来源跳过此步骤，直接进入预览。

### 步骤6：预览Skill详细信息

**安装前必须先预览，获得用户确认。**

**Comate来源：**

```bash
python3 ${COMATE_SKILL_DIR}/scripts/preview_skill.py <skill_name> <download_url>
```

**开源来源：**

展示 `npx skills find` 返回的描述信息，并附上详情链接：

```
https://skills.sh/<owner>/<repo>/<skill-name>
```

向用户展示（使用Markdown格式，确保每个字段独占一行）：

```markdown
**Skill详细信息：**

- **名称**：<skill_name>
- **描述**：<description>
- **来源**：<Comate内部 / skills.sh>
- **安装位置**：<安装路径>
- **详情页**：<skills.sh链接（开源来源时展示）>

**功能概览：**

<overview前500字符，开源来源使用搜索结果描述>

确认安装这个技能吗？（输入"是"继续安装）
```

**等待用户明确确认后，再进行安装。**

### 步骤7：安装Skill

用户确认后，根据来源和安装位置执行安装：

**Comate来源：**

```bash
# 安装到当前项目
python3 ${COMATE_SKILL_DIR}/scripts/install_skill.py <skill_name> <download_url> --scope project

# 安装到全局个人目录
python3 ${COMATE_SKILL_DIR}/scripts/install_skill.py <skill_name> <download_url> --scope global
```

**开源来源（skills.sh）：**

```bash
# 安装到全局（推荐）
npx skills add <owner/repo@skill> -g -y -a universal

# 安装到当前项目（如用户明确要求）
npx skills add <owner/repo@skill> -y -a universal
```

### 步骤8：确认安装完成

```
技能 '<skill_name>' 已成功安装!

来源: <Comate内部 / skills.sh>
安装位置: <实际安装路径>

请重启 Comate 以加载新技能。

```

## 错误处理

**Comate API不可用，自动降级：**

```
Comate内部平台暂时不可用，正在切换到开源技能生态（skills.sh）...
```

**两个来源都无法访问：**

```
抱歉，暂时没有找到合适的技能来解决这个问题。你可以直接告诉我需要做什么，我会尽力帮助你。
```

**没有找到匹配的skill：**

```
当前技能生态中没有找到特别匹配的技能。
如果这是你经常需要做的事，可以创建自己的技能：npx skills init my-skill-name
我会用现有能力尽力帮你处理这个问题。
```

不要自动重试失败的API调用。
