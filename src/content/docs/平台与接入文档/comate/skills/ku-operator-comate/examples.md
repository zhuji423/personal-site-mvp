---
title: "ku-operator 参考示例"
description: "以下示例展示了各子命令的典型用法，供 agent 调用时参考。 所有命令在 ku-operator/ 目录下运行。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\examples.md"
---
# ku-operator 参考示例

> 以下示例展示了各子命令的典型用法，供 agent 调用时参考。
> 所有命令在 `ku-operator/` 目录下运行。

---

## 一、query-content（查询文档内容）

### 通过 doc-id 查询

```bash
python3 scripts/ku_operator.py query-content --doc-id OQAehZAod_HVHC
```

输出 Markdown 格式的文档正文，可直接阅读。

### 通过完整 URL 查询

```bash
python3 scripts/ku_operator.py query-content \
  --url "https://ku.baidu-int.com/knowledge/HFVrC2hT9H/pKzYIZbmZx/B8wSneaLSC/OQAehZAod_HVHC"
```

效果同上，适用于用户直接给出链接的场景。

### 通过短链接查询

```bash
python3 scripts/ku_operator.py query-content \
  --url "https://ku.baidu-int.com/d/bLKhnZmWDDm7JH"
```

短链接格式为 `https://ku.baidu-int.com/d/{docId}`，`/d/` 后面即文档 ID。也可以直接提取 doc-id 使用：

```bash
python3 scripts/ku_operator.py query-content --doc-id bLKhnZmWDDm7JH
```

---

## 二、query-repo（查询知识库目录）

### 查询根目录

```bash
python3 scripts/ku_operator.py query-repo --repo-guid Xw0t0FBvVy
```

示例输出：

```
知识库 Xw0t0FBvVy 根目录（共 3 项）：

📄 欢迎使用 (GgD6PTVjSmZEC3)
📁 浏览器相关 (gsrJkBZ6XlyGRl) [2 子文档]
📄 接口说明 (vtUh01DEnyYDA6)
```

### 展开子目录

看到 📁 图标表示该文档下有子文档，用其 docGuid 作为 `--parent-doc-guid` 继续展开：

```bash
python3 scripts/ku_operator.py query-repo \
  --repo-guid Xw0t0FBvVy \
  --parent-doc-guid gsrJkBZ6XlyGRl
```

### 大目录翻页

当目录内容超过 100 项时，末尾会提示翻页：

```bash
python3 scripts/ku_operator.py query-repo --repo-guid Xw0t0FBvVy --page 2
```

---

## 三、create-doc（新建文档）

### 创建空文档

```bash
python3 scripts/ku_operator.py create-doc \
  --repo-guid B8wSneaLSC \
  --title "会议纪要-2026-02-09"
```

返回新文档的 `docGuid` 和 `url`。

### 从本地文件创建带内容的文档

先将内容写入本地 `.md` 文件，再通过 `--content-file` 传入：

```bash
python3 scripts/ku_operator.py create-doc \
  --repo-guid B8wSneaLSC \
  --title "接口说明" \
  --content-file ./接口说明.md
```

### 在指定目录下创建文档

```bash
python3 scripts/ku_operator.py create-doc \
  --repo-guid B8wSneaLSC \
  --title "子文档" \
  --parent-doc-guid OQAehZAod_HVHC
```

---

## 四、move-doc（移动文档）

### 移动到知识库根目录

```bash
python3 scripts/ku_operator.py move-doc \
  --doc-id ABC123 \
  --to-repo-guid B8wSneaLSC
```

### 移动到指定目录下

```bash
python3 scripts/ku_operator.py move-doc \
  --doc-id ABC123 \
  --to-repo-guid B8wSneaLSC \
  --to-parent-guid XYZ789
```

---

## 五、delete-doc（删除文档）

### 删除指定文档

```bash
python3 scripts/ku_operator.py delete-doc --doc-id ABC123
```

> 删除操作不可恢复，执行前请确认目标文档无误。

---

## 六、典型组合流程

### 流程1：用户给了一个文档 URL，要求分析内容

```bash
# 1. 读取文档内容
python3 scripts/ku_operator.py query-content \
  --url "https://ku.baidu-int.com/knowledge/HFVrC2hT9H/pKzYIZbmZx/B8wSneaLSC/OQAehZAod_HVHC"

# 2. 检查该文档是否有子文档（文档即目录）
#    从 URL 解析：repoGuid=B8wSneaLSC，docGuid=OQAehZAod_HVHC
python3 scripts/ku_operator.py query-repo \
  --repo-guid B8wSneaLSC \
  --parent-doc-guid OQAehZAod_HVHC

# 3. 如果有子文档，按需读取子文档内容进行分析
python3 scripts/ku_operator.py query-content --doc-id <子文档docGuid>
```

### 流程2：用户给了一个知识库 URL（3 段路径），要求了解结构

```bash
# URL 只有 3 段：https://ku.baidu-int.com/knowledge/HFVrC2hT9H/pKzYIZbmZx/B8wSneaLSC
# 这是一个知识库链接，repoGuid=B8wSneaLSC

# 1. 查看根目录结构
python3 scripts/ku_operator.py query-repo --repo-guid B8wSneaLSC

# 2. 对感兴趣的目录（📁）逐层展开
python3 scripts/ku_operator.py query-repo \
  --repo-guid B8wSneaLSC \
  --parent-doc-guid <目标目录docGuid>
```

### 流程3：创建文档 → 验证 → 移动

```bash
# 1. 在根目录创建文档
python3 scripts/ku_operator.py create-doc \
  --repo-guid B8wSneaLSC \
  --title "待归档文档"
# 记录返回的 docGuid

# 2. 确认文档已创建
python3 scripts/ku_operator.py query-repo --repo-guid B8wSneaLSC

# 3. 移动到目标目录
python3 scripts/ku_operator.py move-doc \
  --doc-id <步骤1返回的docGuid> \
  --to-repo-guid B8wSneaLSC \
  --to-parent-guid <目标目录ID>

# 4. 确认文档已移动到位
python3 scripts/ku_operator.py query-repo \
  --repo-guid B8wSneaLSC \
  --parent-doc-guid <目标目录ID>
```
