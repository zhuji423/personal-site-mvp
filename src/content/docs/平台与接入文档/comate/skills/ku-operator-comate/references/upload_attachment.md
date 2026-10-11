---
title: "upload-attachment — 上传附件并插入文档正文"
description: "上传本地文件作为附件到指定文档，默认自动插入文档正文。使用 multipart/form-data 方式上传，超时时间 120 秒。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\upload_attachment.md"
---
# upload-attachment — 上传附件并插入文档正文

上传本地文件作为附件到指定文档，默认自动插入文档正文。使用 multipart/form-data 方式上传，超时时间 120 秒。

## CLI 用法

```bash
python3 scripts/ku_operator.py upload-attachment --doc-id <文档ID> --file <本地文件路径> [--no-insert] [--view-type attachment|preview]
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--file` | 是 | 本地文件路径 |
| `--no-insert` | 否 | 只上传不插入正文 |
| `--view-type` | 否 | 显示方式：`attachment`=附件卡片（默认）, `preview`=内嵌预览 |

## 输出说明

返回 JSON 格式结果，包含上传成功后的附件信息（attachId、name、extension、size 等）。上传成功后默认自动调用 edit-content 将附件 block 插入文档末尾。

> 上传超时时间为 120 秒，适合大文件上传。

## 使用示例

### 上传 PDF 并自动插入正文

```bash
python3 scripts/ku_operator.py upload-attachment \
  --doc-id OQAehZAod_HVHC \
  --file ./report.pdf
```

### 只上传不插入正文

```bash
python3 scripts/ku_operator.py upload-attachment \
  --doc-id OQAehZAod_HVHC \
  --file ./data.xlsx \
  --no-insert
```

### 以内嵌预览方式插入

```bash
python3 scripts/ku_operator.py upload-attachment \
  --doc-id OQAehZAod_HVHC \
  --file ./screenshot.png \
  --view-type preview
```
