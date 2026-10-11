---
title: "EPLog 日志查询脚本"
description: "此脚本用于通过 WebSocket 连接 neweplog.baidu-int.com 查询日志，替代手动打开网页查看。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\apismart_code\\doc\\scripts\\README.md"
---
# EPLog 日志查询脚本

## 简介

此脚本用于通过 WebSocket 连接 `neweplog.baidu-int.com` 查询日志，替代手动打开网页查看。

## 安装依赖

```bash
pip install -r requirements.txt
# 或者直接安装
pip install websockets
```

## 使用方法

### 基本用法

```bash
python query_eplog.py <trace_id>
```

### 示例

```bash
# 查询指定 trace_id 的日志
python query_eplog.py P872756_1769597615000

# 指定 owner 和超时时间
python query_eplog.py P872756_1769597615000 --owner itp --timeout 60

# 将结果保存到 JSON 文件
python query_eplog.py P872756_1769597615000 -o result.json

# 将日志拼接保存到 TXT 文件
python query_eplog.py P872756_1769597615000 -t logs.txt

# 显示日志摘要信息
python query_eplog.py P872756_1769597615000 --summary

# 组合使用：保存txt文件并显示摘要
python query_eplog.py P872756_1769597615000 -t logs.txt --summary --timeout 30

# 设置连续空消息阈值（防止无限等待）
python query_eplog.py P872756_1769597615000 --max-empty 5 --timeout 60

# 快速断开：遇到2次连续空消息就断开
python query_eplog.py P872756_1769597615000 --max-empty 2
```

### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `trace_id` | 日志追踪 ID（必填） | - |
| `--owner` | 日志归属 | `itp` |
| `--timeout` | 等待消息超时时间（秒） | `10` |
| `--cookie-file` | Cookie 文件路径 | - |
| `-o, --output` | 输出 JSON 文件路径 | - |
| `-t, --txt` | 输出 TXT 文件路径 | - |
| `-s, --summary` | 显示日志摘要信息 | - |
| `--max-empty` | 连续空消息的最大次数 | `3` |

## 特殊功能

### 空消息自动断开

当 EPLog 服务端日志传输完成后，可能会发送空消息或无效消息，脚本具有智能检测功能：

- **检测逻辑**：自动识别空字符串、空列表、无内容的日志条目
- **阈值控制**：通过 `--max-empty` 参数设置连续空消息的最大次数
- **自动断开**：达到阈值后主动断开连接，避免无限等待

```bash
# 默认：连续3次空消息后断开
python query_eplog.py P872756_1769597615000

# 更敏感：连续2次空消息后断开  
python query_eplog.py P872756_1769597615000 --max-empty 2

# 更宽容：连续5次空消息后断开
python query_eplog.py P872756_1769597615000 --max-empty 5
```

### WebSocket 连接说明

EPLog 使用 WebSocket (WSS) 协议进行实时日志传输：

- **协议**：`wss://neweplog.baidu-int.com/websocket`
- **SSL验证**：脚本自动跳过内网证书验证
- **心跳保活**：每20秒发送心跳包维持连接
- **超时控制**：可通过 `--timeout` 参数控制无消息等待时间

## 认证配置

由于 EPLog 需要登录认证，你需要配置有效的 Cookie。

### 方式一：直接修改脚本

编辑 `query_eplog.py` 中的 `get_default_cookies()` 函数：

```python
def get_default_cookies() -> dict:
    return {
        "UUAP_P_TOKEN": "PT-xxx",
        "SECURE_UUAP_P_TOKEN": "PT-xxx",
        # ... 其他 Cookie
    }
```

### 方式二：使用 Cookie 文件

创建文件 `~/.eplog_cookies`，格式如下：

```
# EPLog 认证 Cookie
UUAP_P_TOKEN=PT-xxx
SECURE_UUAP_P_TOKEN=PT-xxx
ZT_GW_TOKEN=eyJxxx
```

然后使用：

```bash
python query_eplog.py P872756_1769597615000 --cookie-file ~/.eplog_cookies
```

### 如何获取 Cookie

1. 打开 Chrome 浏览器，访问 https://neweplog.baidu-int.com
2. 登录 UUAP
3. 按 F12 打开开发者工具
4. 切换到 Network 标签
5. 刷新页面，点击任意请求
6. 在 Headers 中找到 `Cookie` 字段，复制其值

## 对应 Web 页面

脚本查询的 trace_id 对应的 Web 页面 URL 格式为：

```
https://neweplog.baidu-int.com/index.html?owner=itp&logId=<trace_id>
```

例如：
- Trace ID: `P872756_1769597615000`
- Web URL: https://neweplog.baidu-int.com/index.html?owner=itp&logId=P872756_1769597615000

## 输出格式说明

### TXT 文件格式

当使用 `--txt` 参数时，日志会被拼接成易读的文本格式：

```
[LogID] [时间戳] [日志级别] 日志内容
```

示例：
```
[P872756_1769597615000] [2026-01-28 18:53:36] [INFO] async op[gettaskpptstatus] doing 1 time
[P872756_1769597615000] [2026-01-28 18:53:36] [ERROR] java.net.UnknownHostException: host: unknown error
[P872756_1769597615000] [2026-01-28 18:53:36] [INFO] httpclient end time:2026-01-28 18:53:36
```

### 摘要信息格式

使用 `--summary` 参数时，会显示日志统计信息：

```
📈 日志摘要:
   总消息数: 1650
   日志级别: {'info': 1645, 'error': 5}
   错误数量: 5
   唯一LogID数: 1
   时间范围: 2026-01-28 18:53:36 ~ 2026-01-28 19:17:57
```

## 输出示例

```
============================================================
🔍 EPLog 日志查询
   Trace ID: P872756_1769597615000
   Owner: itp
   Timeout: 10.0s
============================================================
📡 连接 WebSocket: wss://neweplog.baidu-int.com/websocket/owner=itp&logId=P872756_1769597615000
🌐 对应 Web 页面: https://neweplog.baidu-int.com/index.html?owner=itp&logId=P872756_1769597615000
------------------------------------------------------------
✅ WebSocket 连接成功
ℹ️ [2025-01-29 10:00:00] [INFO] 任务开始执行
ℹ️ [2025-01-29 10:00:01] [INFO] 加载测试用例
✅ [2025-01-29 10:00:05] [INFO] 执行完成

⏱️ 等待 10 秒无新消息，结束查询
============================================================
📊 共获取 3 条日志消息
```
