---
title: "KAMI AIRD 请求回调处理"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\baidu\\qamate-server\\core\\.kami\\knowledge\\requirements\\kami-aird_【KAMI】aird请求回调处理_20260414.md"
---
# KAMI AIRD 请求回调处理

## 卡片信息
- 日期：2026-04-14
- 需求描述：针对 kamixgmt 创建接口新增 platform 字段，保存到 source；在 UserAgentQuery Callback 中，如果 source 为 aird，触发 AIRD 回调（成功 status=2，失败 status=4）

## 涉及文件

### 新增
- `manager/feign/AirdClientConfig.java`
- `manager/feign/client/AirdClient.java`
- `entity/req/feign/AirdUpdateTaskStatusReq.java`
- `entity/resp/feign/AirdUpdateTaskStatusResp.java`

### 修改
- `common/enums/PlatformEnum.java` — 新增 AIRD 枚举值
- `entity/req/SessionCreateReq.java` — 新增 platform 字段
- `service/impl/SessionServiceImpl.java` — createSession 中将 platform 映射到 source；handleRunningCallback 和 handleCompletedCallback 中触发 AIRD 回调

## 实现方案

### AIRD 回调逻辑
- `handleRunningCallback`：source=aird → 调用 AIRD API，status=2
- `handleCompletedCallback` success：source=aird → status=2
- `handleCompletedCallback` failure：source=aird → status=4，remark=errorMsg

### AIRD Feign 接口
- 测试环境：http://qerag-test.baidu-int.com（复用 ${qerag.baseUrl}）
- 线上环境：http://qerag.baidu-int.com
- PUT /api/kami/task/status
- Body: { sessionUUID, status, remark }
