---
title: "CNAP CLI 登录认证"
description: "适用于 AI Agent 和自动化脚本场景，无需人工交互。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\cnap-comate\\references\\login.md"
---
# CNAP CLI 登录认证

## 登录命令概览

| 命令 | 用途 | 推荐场景 |
|------|------|----------|
| `cnap login status` | 查看当前登录状态 | 登录前后检查 |
| `cnap login ugate` | UGate Token 登录 | AI Agent、自动化脚本 |
| `cnap login qrcode` | 扫码登录 | 人工操作 |
| `cnap login totp` | TOTP 登录 | 自动化脚本 |
| `cnap logout` | 退出登录 | 清理登录凭证 |

## 登录方式详解

### 1. UGate Token 登录（推荐 Agent）

适用于 AI Agent 和自动化脚本场景，无需人工交互。

```bash
# 交互式：提示输入 Token
cnap login ugate

# 非交互式：直接传入 Token
cnap login ugate --token <ugate-token>
```

**获取 Token**：访问 https://uuap.baidu.com/agent/token

**参数说明**：

| 参数 | 简写 | 必填 | 说明 |
|------|------|------|------|
| `--token` | `-t` | 否 | UGate Token，直接传入则非交互式 |
| `--username` | `-u` | 否 | 期望的用户名，用于校验 Token 是否属于该用户 |

**username 校验示例**：

```bash
# 指定期望用户名，Token 必须属于该用户，否则报错
cnap login ugate --username dongshuzhao --token <token>

# 输出示例：
# UGate logged in successfully as: dongshuzhao
```

### 2. 扫码登录

适用于人工操作，需要使用如流手机 App 扫描二维码确认登录。

```bash
# 交互式扫码登录
cnap login qrcode
```

扫码后在如流手机 App 中确认授权。

### 3. TOTP 登录

适用于自动化脚本，需要先申请 TOTP Secret。

```bash
# 使用 TOTP Secret 登录
cnap login totp --secret <your-secret>
```

**参数说明**：

| 参数 | 简写 | 必填 | 说明 |
|------|------|------|------|
| `--secret` | `-s` | 是 | TOTP Secret |

### 4. 查看登录状态

```bash
cnap login status
```

输出示例：

```
Logged in as: dongshuzhao
Login method: ugate
Token expires: 2026-04-03 12:00:00
```

### 5. 退出登录

```bash
cnap logout
```

退出后清除本地保存的登录凭证。

## 常见问题

### Token 过期

Token 有有效期限制，过期后需要重新登录：

```bash
cnap login ugate --token <new-token>
```

### 权限不足

如果遇到权限报错，联系账号管理员获取相应权限。

### 登录状态异常

如果遇到登录状态异常，可以尝试：

```bash
# 退出登录后重新登录
cnap logout
cnap login ugate --token <token>
```

## 登录凭证存储

登录成功后，凭证会保存在配置文件中：

- **UGate**：保存用户名到 `~/.cnap/config.yaml` 的 `auth.ugate.username`
- Token 信息由 oneauth 库管理

切换登录方式时，凭证会自动保存。