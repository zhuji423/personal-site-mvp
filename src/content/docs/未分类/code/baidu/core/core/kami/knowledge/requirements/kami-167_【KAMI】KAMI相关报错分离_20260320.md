---
title: "kami-167 [Story] 【KAMI】KAMI 相关报错分离"
description: "- 卡片 ID：kami-167 - 类型：Story - 状态：开发中 - 负责人：maxiaolong01 - 日期：2026-03-20"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\core\\.kami\\knowledge\\requirements\\kami-167_【KAMI】KAMI相关报错分离_20260320.md"
---
# kami-167 [Story] 【KAMI】KAMI 相关报错分离

## 卡片信息

- **卡片 ID**：kami-167
- **类型**：Story
- **状态**：开发中
- **负责人**：maxiaolong01
- **日期**：2026-03-20

## 需求描述

代码中会对 CoreException 做统一处理，并推送到如流群。现在，针对 http uri 包含 kami，请推送到 12292840 如流群；包含 lumos 请推送到 12453896 如流群。其余 URI 继续推送到原群 10839781。

## 涉及文件

- `src/main/java/com/baidu/qamate/core/prometheusmgt/dto/SendRuliuNotifyDto.java`

## 实现方案

在 `SendRuliuNotifyDto` 中：

1. 新增两个群常量：
   - `KAMI_ALERT_GROUP_LIST = List.of(12292840)` — KAMI 相关报错群
   - `LUMOS_ALERT_GROUP_LIST = List.of(12453896)` — Lumos 相关报错群

2. 在 `sendExceptionAsync` 方法中，根据 `request.getRequestURI()` 判断目标群：
   - URI 含 `kami` → `KAMI_ALERT_GROUP_LIST`
   - URI 含 `lumos` → `LUMOS_ALERT_GROUP_LIST`
   - 其他 → 原 `ALERT_GROUP_LIST`（10839781）

## 提交信息

- **分支**：dev_kami-167
- **Commit**：`kami-167 [Story] 【KAMI】KAMI 相关报错分离`
- **推送目标**：`preview_kami_20260320`
- **Review 链接**：http://icode.baidu.com/myreview/changes/c/baidu/qamate-server/core/+/120178081
