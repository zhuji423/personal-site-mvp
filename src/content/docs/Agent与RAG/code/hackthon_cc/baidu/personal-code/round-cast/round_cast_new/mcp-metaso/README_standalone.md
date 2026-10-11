---
title: "Metaso 独立搜索工具"
description: "这是一个独立的Metaso搜索工具，去除了MCP相关依赖，可以直接通过Python脚本使用。"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\hackthon_cc\\baidu\\personal-code\\round-cast\\round_cast_new\\mcp-metaso\\README_standalone.md"
---
# Metaso 独立搜索工具

这是一个独立的Metaso搜索工具，去除了MCP相关依赖，可以直接通过Python脚本使用。

## 功能特性

- 🔍 支持6种搜索类型：网页、文库、学术、图片、视频、播客
- 📖 网页内容解析和提取
- 🎛️ 命令行界面和交互式模式
- 🐍 支持异步和同步调用
- 📦 可作为模块导入到其他Python项目

## 安装依赖

```bash
pip install httpx asyncio
```

## 配置

设置Metaso API密钥环境变量：

```bash
export METASO_API_KEY="your_api_key_here"
```

## 使用方法

### 1. 命令行使用

#### 基本搜索

```bash
# 网页搜索
python3 standalone_metaso.py -q "Python编程"

# 学术搜索
python3 standalone_metaso.py -q "机器学习" -s scholar --summary

# 图片搜索
python3 standalone_metaso.py -q "风景" -s image --size 5
```

#### 网页解析

```bash
# 解析网页内容
python3 standalone_metaso.py -r "https://www.python.org"

# 以JSON格式输出
python3 standalone_metaso.py -r "https://example.com" --format json
```

#### 交互式模式

```bash
python3 standalone_metaso.py -i
# 或者直接运行
python3 standalone_metaso.py
```

### 2. 作为Python模块使用

#### 异步调用

```python
import asyncio
from standalone_metaso import metaso_search, metaso_reader

async def main():
    # 搜索
    result = await metaso_search("人工智能", "webpage", size=5)
    print(result)
  
    # 网页解析
    content = await metaso_reader("https://example.com")
    print(content)

asyncio.run(main())
```

#### 同步调用

```python
from standalone_metaso import search_sync, reader_sync

# 搜索
result = search_sync("Python教程", "webpage", include_summary=True, size=3)
print(result)

# 网页解析
content = reader_sync("https://docs.python.org")
print(content)
```

## 搜索类型

| 类型     | 说明         | scope参数    |
| -------- | ------------ | ------------ |
| 网页搜索 | 搜索网页内容 | `webpage`  |
| 文库搜索 | 搜索文档资料 | `document` |
| 学术搜索 | 搜索学术论文 | `scholar`  |
| 图片搜索 | 搜索图片资源 | `image`    |
| 视频搜索 | 搜索视频内容 | `video`    |
| 播客搜索 | 搜索播客节目 | `podcast`  |

## 参数说明

### metaso_search()参数

- `query`: 搜索关键词（必需）
- `scope`: 搜索类型（默认: "webpage"）
- `include_summary`: 是否包含搜索摘要（默认: False）
- `size`: 结果数量，1-20（默认: 10）

### metaso_reader()参数

- `url`: 要解析的网页URL（必需）
- `output_format`: 输出格式，"markdown"或"json"（默认: "markdown"）

## 命令行选项

```
-q, --query          搜索查询词
-s, --scope          搜索范围 (webpage/document/scholar/image/video/podcast)
--summary            包含搜索摘要
--size              结果数量 (1-20)
-r, --reader         解析指定URL的网页内容
--format            网页解析输出格式 (markdown/json)
-i, --interactive    启动交互式模式
-h, --help           显示帮助信息
```

## 示例输出

### 网页搜索结果

```
# 网页搜索结果：Python编程

## 结果 1
**标题**: Python官方教程
**URL**: https://docs.python.org/zh-cn/3/tutorial/
**摘要**: Python是一种易于学习又功能强大的编程语言...
**发布时间**: 2024-01-15

## 结果 2
...

---
**共找到 10 条网页结果**
```

### 学术搜索结果

```
# 学术搜索结果：机器学习

## 搜索摘要
机器学习是人工智能的一个重要分支，通过算法让计算机从数据中学习...

## 学术结果 1
**标题**: Deep Learning
**作者**: Ian Goodfellow, Yoshua Bengio, Aaron Courville
**URL**: https://www.deeplearningbook.org/
**摘要**: 深度学习是机器学习的一个子领域...
**发表年份**: 2016
**引用次数**: 50000+

---
**共找到 10 条学术结果**
```

## 错误处理

工具包含完善的错误处理机制：

- API密钥验证
- 网络请求超时处理
- 参数验证
- 异常捕获和友好错误提示

## 文件结构

```
├── standalone_metaso.py    # 主程序文件
├── example_usage.py        # 使用示例
├── config.py              # 配置文件
└── README_standalone.md   # 本说明文件
```

## 注意事项

1. 确保已设置有效的METASO_API_KEY环境变量
2. 网络连接正常，能访问Metaso API
3. 搜索结果数量限制在1-20之间
4. 某些搜索类型可能需要特定的API权限

## 故障排除

### API密钥问题

```bash
# 检查环境变量是否设置
echo $METASO_API_KEY

# 临时设置（当前会话有效）
export METASO_API_KEY="your_key_here"

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export METASO_API_KEY="your_key_here"' >> ~/.bashrc
```

### 网络连接问题

- 检查网络连接
- 确认能正常访问 https://metaso.cn
- 检查防火墙设置

### 依赖问题

```bash
# 安装所需依赖
pip install httpx

# 或使用requirements.txt
pip install -r requirements.txt
```
