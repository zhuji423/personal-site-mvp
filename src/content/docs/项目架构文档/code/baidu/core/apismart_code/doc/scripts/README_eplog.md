---
title: "EPLog 日志查询工具"
description: "通过 WebSocket 连接 neweplog.baidu-int.com 查询日志。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\apismart_code\\doc\\scripts\\README_eplog.md"
---
# EPLog 日志查询工具

通过 WebSocket 连接 neweplog.baidu-int.com 查询日志。

## 安装依赖

```bash
pip install aiohttp
```

## 使用方法

### 基本查询

```bash
python query_eplog_shrink.py --type byTraceId --traceId <trace_id>
```

### 参数说明

| 参数 | 简写 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| --type | | ✅ | | 查询类型，目前支持 `byTraceId` |
| --traceId | | ✅ | | 日志追踪 ID |
| --owner | | | itp | 日志归属 |
| --timeout | | | 30 | 超时时间（秒） |
| --maxEmpty | | | 3 | 最大连续空消息次数 |
| --output | -o | | | 输出 JSON 文件 |
| --txt | -t | | | 输出 TXT 文件 |
| --summary | -s | | | 显示日志摘要 |

## 示例

### 1. 简单查询日志

```bash
python query_eplog_shrink.py --type byTraceId --traceId P872756_1769597615000
```

### 2. 查询并保存为 JSON 文件

```bash
python query_eplog_shrink.py --type byTraceId --traceId P872756_1769597615000 -o
```

文件自动保存为：`20260129_P872756_1769597615000.json`（日期为日志中的日期）

### 3. 查询并保存为 TXT 文件

```bash
python query_eplog_shrink.py --type byTraceId --traceId P872756_1769597615000 -t
```

文件自动保存为：`20260129_P872756_1769597615000.txt`

### 4. 完整示例：查询 + 保存 JSON/TXT + 显示摘要

```bash
python query_eplog_shrink.py --type byTraceId --traceId P872756_1769597615000 -o -t -s
```

### 5. 自定义超时时间和空消息阈值

```bash
python query_eplog_shrink.py --type byTraceId --traceId P872756_1769597615000 --timeout 60 --maxEmpty 5
```

### 6. 指定日志归属

```bash
python query_eplog_shrink.py --type byTraceId --traceId P872756_1769597615000 --owner itp
```

## 输出文件说明

### 文件命名规则

文件名格式：`{日志日期}_{traceId}.{后缀}`

- 日期从日志内容中自动提取
- 例如：`20260128_P872756_1769597615000.json`

### JSON 文件

保存原始的日志消息数据，包含完整的日志结构。

### TXT 文件

保存格式化后的日志内容，每行一条日志：

```
[logid] [timestamp] [level] message
```

## 对应 Web 页面

查询时会输出对应的 Web 页面 URL，可直接在浏览器中打开查看：

```
https://neweplog.baidu-int.com/index.html?owner=itp&logId=<trace_id>
```

