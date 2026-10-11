---
title: "create-doc — 新建文档"
description: "在知识库中新建文档或目录。支持从本地 Markdown 文件读取内容，自动上传本地图片/附件到 BOS。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\create_doc.md"
---
# create-doc — 新建文档

在知识库中新建文档或目录。支持从本地 Markdown 文件读取内容，自动上传本地图片/附件到 BOS。

## CLI 用法

```bash
python3 scripts/ku_operator.py create-doc --repo-guid <知识库ID> --title "文档标题"
python3 scripts/ku_operator.py create-doc --repo-guid <知识库ID> --title "文档标题" --content-file ./doc.md
python3 scripts/ku_operator.py create-doc --repo-guid <知识库ID> --title "子文档" --parent-doc-guid <父文档ID>
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--repo-guid` | 是 | 知识库 ID |
| `--title` | 否 | 文档标题 |
| `--content-file` | 否 | 从本地文件读取文档内容（Markdown 格式）；不传则创建空文档 |
| `--parent-doc-guid` | 否 | 父文档 ID，不传则创建在根目录 |

## 输出说明

返回 JSON 格式结果，关键字段：
- `docGuid` — 新建文档的 ID
- `url` — 新建文档的访问 URL（可直接提供给用户）

## 注意事项

- 创建者用户名自动从环境变量 `COMATE_USERNAME` 读取，无需手动传入
- 如需创建带内容的文档，先将内容写入本地 `.md` 文件，再通过 `--content-file` 传入
- **自动资源上传**：使用 `--content-file` 时，脚本会自动扫描 Markdown 中引用的本地图片和附件，通过 `bos` 工具上传到 BOS 并替换为远程 URL
- **重要：撰写 Markdown 时，图片和附件引用必须使用绝对路径**（如 `![图片](/home/user/ku_assets/doc_id/image.png)`），不要使用相对路径

## 使用示例

### 创建空文档

```bash
python3 scripts/ku_operator.py create-doc \
  --repo-guid B8wSneaLSC \
  --title "会议纪要-2026-02-09"
```

### 从本地文件创建带内容的文档

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
