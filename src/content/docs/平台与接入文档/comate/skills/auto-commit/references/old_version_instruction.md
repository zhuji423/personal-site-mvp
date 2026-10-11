---
title: "旧版本 IDE 交互指南"
description: "本文档适用于旧版本 IDE（IDE 名称占位符未替换、或插件版本 < 4.1.0）的交互方式。旧版本不支持 silent: 和 interactive: 前缀。"
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\auto-commit\\references\\old_version_instruction.md"
---
# 旧版本 IDE 交互指南

本文档适用于**旧版本 IDE**（IDE 名称占位符未替换、或插件版本 < 4.1.0）的交互方式。旧版本不支持 `__silent:` 和 `__interactive:` 前缀。

---

## 步骤 1：获取 iCafe 数据（旧版本命令）

使用 SKILL.md 步骤 1 中定义的命令模板，**不加 `__silent:` 前缀**直接执行。

---

## 步骤 2：获取 git diff（旧版本命令）

使用 SKILL.md 步骤 2 中定义的命令模板，**不加 `__silent:` 前缀**直接执行。

---

## 步骤 4：展示卡片选择（文本交互）

根据 `viewMode` 输出文本列表。

**当 `viewMode == "list"`（有高匹配卡片）时：**

先展示卡片列表（已按匹配度排序，标注匹配理由），再展示新建选项：

```
📋 根据代码变更，找到以下匹配的 iCafe 卡片：

1. ⭐ [${spacePrefix}-${card1.sequence}] ${card1.title}
   类型: ${card1.type} | 状态: ${card1.status}
   匹配理由: ${reason}

2. [${spacePrefix}-${card2.sequence}] ${card2.title}
   类型: ${card2.type} | 状态: ${card2.status}

（最多显示 10 张卡片，⭐ 标记匹配度较高的卡片）

---
🆕 如需新建卡片，为你推荐以下信息：
- 推荐标题：${result.defaults.title}
- 推荐空间：${spaceName} (${spacePrefix})
- 推荐类型：${推荐的类型名称}（类型 ID: ${result.defaults.type_id}）

---
请回复：
- 输入序号（如 "1"）选择对应卡片
- 输入卡片 ID（如 "DevOps-iScan-35835"）直接关联
- 输入 "new" 使用推荐信息直接新建卡片
- 输入 "new 自定义标题" 使用推荐空间和类型、但自定义标题新建
- 输入 "new?" 查看所有可选空间和类型枚举
```

**当 `viewMode == "create"`（无高匹配卡片）时：**

先展示新建卡片推荐（突出位置），再附上已有卡片作为备选：

```
💡 当前代码变更与已有卡片匹配度较低，建议新建卡片：

🆕 推荐新建卡片信息：
- 推荐标题：${result.defaults.title}
- 推荐空间：${spaceName} (${spacePrefix})
- 推荐类型：${推荐的类型名称}（类型 ID: ${result.defaults.type_id}）

---
📋 以下是你当前活跃的卡片（供参考）：

1. [${spacePrefix}-${card1.sequence}] ${card1.title}
   类型: ${card1.type} | 状态: ${card1.status}

（最多显示 10 张卡片）

---
请回复：
- 输入 "new" 使用推荐信息直接新建卡片
- 输入 "new 自定义标题" 使用推荐空间和类型、但自定义标题新建
- 输入序号（如 "1"）选择对应卡片
- 输入卡片 ID（如 "DevOps-iScan-35835"）直接关联
- 输入 "new?" 查看所有可选空间和类型枚举
```

如果没有找到卡片，输出：

```
📋 未找到可关联的 iCafe 卡片

🆕 为你推荐以下建卡信息：
- 推荐标题：${result.defaults.title}
- 推荐空间：${spaceName} (${spacePrefix})
- 推荐类型：${推荐的类型名称}

---
请回复：
- 输入卡片 ID（如 "DevOps-iScan-35835"）直接关联
- 输入 "new" 使用推荐信息直接新建卡片
- 输入 "new 自定义标题" 使用推荐空间和类型、但自定义标题新建
- 输入 "new?" 查看所有可选空间和类型枚举
```

**推荐类型名称的获取方式：** 从 `result.available_spaces` 中找到当前空间（匹配 `space_prefix`），取其 `types` 列表中 `id` 等于 `result.defaults.type_id` 的类型的 `name`。如果找不到，取该空间 `types` 列表第一个的 `name`。

---

## 步骤 5：处理用户操作（旧版本 IDE）

根据用户在对话中的文本回复：

**如果用户输入序号（如 "1"、"2"）：**
- 解析用户选择的卡片，保存 `selected_card` 信息，继续步骤 7

**如果用户输入卡片 ID（如 "DevOps-iScan-35835"）：**
- 调用 `recognize_card_cli.py` 获取卡片详情：
  ```
  cd <用户项目目录> && python3 <skill_directory>/scripts/recognize_card_cli.py --link "<卡片ID>"
  ```
- 保存 `selected_card` 信息，继续步骤 7

**如果用户输入 "new"（使用推荐信息直接新建）：**
- 使用 `result` 中的推荐信息调用 `create_card_cli.py` 创建卡片
- 标题 = `result.defaults.title`，空间 = `result.space_prefix`
- 类型 = 从 `result.available_spaces` 中匹配当前空间，取 `types` 中 `id` 等于 `result.defaults.type_id` 的类型名称

**如果用户输入 "new 自定义标题"：**
- 与 "new" 逻辑相同，但标题使用用户输入的自定义标题（去掉 "new " 前缀后的部分）

**如果用户输入 "new?"（查看空间和类型枚举）：**

从 `result.available_spaces` 输出完整枚举：

```
📋 可选空间和类型：

空间 1: ${space1.name} (${space1.prefix})
  可选类型：
  - ${type1.name} (ID: ${type1.id})
  - ${type2.name} (ID: ${type2.id})

---
请回复以下格式新建卡片：
  new [标题] | [空间前缀] | [类型名称]
  例如：new 修复登录问题 | dkx | Bug

也可以只指定部分：
  new 修复登录问题 | dkx       → 使用指定空间 + 该空间默认类型
  new 修复登录问题 | | Story   → 使用推荐空间 + 指定类型
```

**如果用户输入 "new 标题 | 空间 | 类型"（完整指定）：**
- 按 `|` 分割解析，第一段为标题，第二段（可选）为空间前缀，第三段（可选）为类型名称
- 为空的部分使用推荐值，调用 `create_card_cli.py` 创建卡片

---

## 步骤 8：展示提交确认（文本确认）

输出：

```
✅ 已关联卡片: ${spacePrefix}-${sequence}
   标题: ${title}
   类型: ${type} | 状态: ${status}

---
📝 建议的 commit message：

${spacePrefix}-${sequence} ${brief_description}

---
请确认：
- 回复 "ok" 或 "确认" 使用此 message 提交
- 回复 "edit: <新message>" 修改后提交（如 "edit: dkx-200 修复登录bug"）
- 回复 "no" 或 "取消" 放弃提交
```

---

## 步骤 9：执行提交（旧版本 IDE）

**如果用户确认提交（回复 "ok"、"确认"、"yes"）：**
- 执行 `git add . && git commit -m "${commit_message}"`

**如果用户修改后提交（回复 "edit: <新message>"）：**
- 使用用户提供的新 message 执行提交

**如果用户取消（回复 "no"、"取消"）：**
- 输出取消信息

旧版本 IDE 提交成功后额外提示：`如需推送到远程，请执行：git push`
