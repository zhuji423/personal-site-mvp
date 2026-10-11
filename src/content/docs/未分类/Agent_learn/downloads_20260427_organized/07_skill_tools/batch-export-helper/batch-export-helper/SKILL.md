---
title: "批量导出助手 (Batch Export Helper)"
description: "批量导出知识库文档、整理邮件分类、重命名文件并打包交付的一站式工具。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\07_skill_tools\\batch-export-helper\\batch-export-helper\\SKILL.md"
---
# 批量导出助手 (Batch Export Helper)

批量导出知识库文档、整理邮件分类、重命名文件并打包交付的一站式工具。

## 使用场景

当用户需要以下任一操作时触发：
- 批量导出知识库文档为 Markdown 格式
- 按主题分类整理邮件（案例分享、会议分享、技术分享等）
- 使用文档标题批量重命名文件
- 打包导出结果并提供下载链接

## 核心功能

### 1. 知识库批量导出
- 支持递归查询子文件夹
- 自动下载图片和附件
- 生成带标题的 Markdown 文件

### 2. 邮件分类整理
- 按主题关键词分类（案例分享、会议分享、技术分享、公开课、培训）
- 支持自定义分类规则
- 生成结构化 Markdown 报告

### 3. 文件重命名
- 解析 Markdown 第一行标题作为文件名
- 自动清理非法字符
- 处理重名冲突（自动添加序号）

### 4. 打包交付
- 支持 tar.gz 和 zip 格式
- 自动上传到 BOS 生成短链接

## 使用方法

### 方式一：Python 脚本调用

```python
from scripts import BatchExportHelper

# 创建助手实例
helper = BatchExportHelper()

# 导出知识库
helper.export_ku_docs(
    repo_guid="WjGjiS_SK_",
    parent_doc_guid="_U6EhhLx7F5_DI",
    output_dir="/path/to/output"
)

# 整理邮件分类
helper.classify_emails(
    output_dir="/path/to/output",
    categories=["案例分享", "会议分享", "技术分享", "公开课", "培训"]
)

# 重命名文件
helper.rename_files_with_titles("/path/to/output")

# 打包上传
helper.package_and_upload(
    output_dir="/path/to/output",
    package_name="export_20260427",
    format="zip"
)
```

### 方式二：命令行调用

```bash
# 导出知识库
python3 scripts/export_ku.py --repo-guid="WjGjiS_SK_" --parent-doc-guid="_U6EhhLx7F5_DI" --output-dir="./output"

# 整理邮件分类
python3 scripts/classify_emails.py --output-dir="./output"

# 重命名文件
python3 scripts/rename_files.py --input-dir="./output"

# 打包上传
python3 scripts/package_upload.py --input-dir="./output" --name="export_20260427" --format="zip"
```

## 参数说明

### export_ku.py
| 参数 | 说明 | 必填 |
|------|------|------|
| --repo-guid | 知识库 ID | 是 |
| --parent-doc-guid | 父文档 ID（可选，用于导出子文件夹） | 否 |
| --output-dir | 输出目录 | 是 |
| --page-size | 每页数量（默认 100） | 否 |

### classify_emails.py
| 参数 | 说明 | 必填 |
|------|------|------|
| --output-dir | 输出目录 | 是 |
| --categories | 分类关键词（逗号分隔） | 否 |
| --folder | 邮件文件夹（默认 all） | 否 |

### rename_files.py
| 参数 | 说明 | 必填 |
|------|------|------|
| --input-dir | 输入目录 | 是 |
| --pattern | 文件匹配模式（默认 *.md） | 否 |

### package_upload.py
| 参数 | 说明 | 必填 |
|------|------|------|
| --input-dir | 输入目录 | 是 |
| --name | 包名称 | 是 |
| --format | 格式（zip 或 tar.gz，默认 zip） | 是 |

## 输出结构

```
output/
├── ku-export-{name}/          # 知识库导出
│   ├── 文档标题.md
│   └── assets/               # 图片和附件
├── email-export-{name}/       # 邮件分类
│   └── email_classification.md
└── {name}.zip                # 打包文件
```

## 依赖

- ku-operator skill（知识库操作）
- baidu-exchange-skill（邮件操作）
- dodo_cli（BOS 上传）

## 注意事项

1. 知识库导出需要 ugate token 授权
2. 邮件操作需要百度企业邮箱权限
3. 大量文件导出可能需要较长时间
4. 文件重命名会跳过无法解析标题的文件