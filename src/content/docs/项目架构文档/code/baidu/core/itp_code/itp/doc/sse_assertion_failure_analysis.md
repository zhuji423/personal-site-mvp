---
title: "SSE 断言替换失败问题分析"
description: "data: {\"errno\": 0, \"errmsg\": \"success\", \"result\": \" 国庆节的由来与历史意义\", \"needclearhistory\": false, \"isrunning\": true, \"title\":"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\sse_assertion_failure_analysis.md"
---
# SSE 断言替换失败问题分析

## 问题描述

### 错误现象
- **断言表达式**: `${&request[0].err_no}`
- **错误信息**: `[断言替换失败] can 't find ${&request[0].err_no} in response`
- **用户勾选选项**:
  1. "判断时，返回中String字段强制转化为Json对象"
  2. "判断时，sse返回内容格式化为Json对象"

### 原始响应内容
```
data: {"err_no": 0, "err_msg": "success", "result": "# 国庆节主题PPT", "need_clear_history": false, "is_running": true, "title": "国庆节主题PPT", "ai_id": "", "language": "zh", "ppt_scene": "html_instruct2ppt"}

data: {"err_no": 0, "err_msg": "success", "result": "## 国庆节的由来与历史意义", "need_clear_history": false, "is_running": true, "title": "国庆节主题PPT", "ai_id": "", "language": "zh", "ppt_scene": "html_instruct2ppt"}
...
```

## 代码分析

### 1. SSE 格式化逻辑

**文件位置**: `itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/executor/HttpRequestExecutor.java:1718-1745`

```java
private String formatSseResponse(String rawResponse) {
    if (Strings.isNullOrEmpty(rawResponse)) {
        return rawResponse;
    }
    try {
        return JSON.toJSONString(
                Arrays.stream(rawResponse.split("\\r?\\n"))
                        .map(String::trim)
                        .filter(s -> s.startsWith("data:"))
                        .map(s -> s.substring("data:".length()).trim())
                        .filter(StringUtils::isNotBlank)
                        .map(s -> {
                            if (JSON.isValid(s)) {
                                try {
                                    return JSON.parse(s);  // 关键：解析为JSON对象
                                } catch (Exception e) {
                                    // fall back to raw line text when JSON parsing fails
                                }
                            }
                            return s;
                        })
                        .collect(Collectors.toList())
        );
    } catch (Exception e) {
        LogUtil.info("sse返回结构化异常");
        return rawResponse;
    }
}
```

**格式化后的响应示例**:
```json
[
  {"err_no": 0, "err_msg": "success", "result": "# 国庆节主题PPT", ...},
  {"err_no": 0, "err_msg": "success", "result": "## 国庆节的由来与历史意义", ...}
]
```

### 2. SSE 格式化触发条件

**文件位置**: `HttpRequestExecutor.java:156-167`

```java
// SSE返回格式化逻辑
if (new Integer(1).equals(httpRequest.getUseSseFormat())) {
    if (null != envConfig
            && null != envConfig.getRespHeaderMap()
            && null != httpRequest.getRequestId()
            && null != envConfig.getRespHeaderMap().get(httpRequest.getRequestId())
    ) {
        Multimap<String, String> responseHeader = envConfig.getRespHeaderMap().get(httpRequest.getRequestId());
        if (isSseContentType(responseHeader)) {
            response = formatSseResponse(response);
        }
    }
}
```

**触发条件**:
1. `httpRequest.getUseSseFormat() == 1`
2. `envConfig` 不为空
3. `respHeaderMap` 存在且包含当前请求的 ID
4. `isSseContentType()` 返回 true（检查 `Content-Type` 包含 `text/event-stream`）

### 3. 断言替换逻辑

**文件位置**: `itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/utils/VariableUtils.java:667-685`

```java
} else if (matchedString.toLowerCase().startsWith("&request")) {
    // jsonPath 格式变量替换
    String[] keyArray = matchedString.split("&request");
    if (keyArray.length == 2) {
        keyArray[1] = "$" + keyArray[1];  // 转换为 JsonPath 格式
        try {
            LOG.info("[real_key]: " + keyArray[1]);
            realValue = JsonPath.read(response, keyArray[1]).toString();
            LOG.info("[actual_value]:" + realValue);
        } catch (Exception ex) {
            LOG.error("please check your variable !!" + keyArray[1]);
            throw new ItestException(0, "can't find key:" + keyArray[1], ex);
        }
    }
}
```

**断言解析流程**:
1. `${&request[0].err_no}` → `matchedString = "&request[0].err_no"`
2. `split("&request")` → `keyArray = ["", "[0].err_no"]`
3. 转换为 JsonPath → `$[0].err_no`
4. `JsonPath.read(response, "$[0].err_no")` 提取值

### 4. 断言验证调用链

**文件位置**: `HttpRequestExecutor.java:184-194`

```java
List<Verification> verifications = request.getVerifications();

if (!ListUtils.isNullOrEmpty(verifications)) {
    if (response != null) {
        response = response.trim();
    }
    VerifyFacade.verify(verifications, envConfig, response);  // 传递 response 给断言逻辑
    returnResp.setVerifications(verifications);
    returnResp.setPass(findAllVerificationResult(verifications));
}
```

## 问题根因分析

### 关键发现

从错误日志中的 `resp` 字段可以看到：
```
resp='data: {"err_no": 0, "err_msg": "success", ...}
data: {"err_no": 0, "err_msg": "success", ...}
...'
```

**响应仍然是原始 SSE 格式，没有被格式化为 JSON 数组！**

### 可能的原因

#### 1. `useSseFormat` 标志未生效
- 虽然用户勾选了 "判断时，sse返回内容格式化为Json对象"
- 但 `httpRequest.getUseSseFormat()` 可能返回的不是 `1`
- 需要确认配置是否正确传递到 `HTTPRequest` 对象

#### 2. `isSseContentType()` 检查失败
- `Content-Type` 响应头可能不包含 `text/event-stream`
- 或者响应头没有被正确存储到 `envConfig.getRespHeaderMap()`

#### 3. SSE 格式化逻辑未执行
- 某些代码路径可能绕过了 SSE 格式化
- 需要检查所有调用 `formatSseResponse` 的位置

#### 4. 响应传递问题
- SSE 格式化后的响应可能没有正确传递给 `VerifyFacade.verify()`
- 可能存在多个 response 变量，格式化的是其中一个，传递的是另一个

## 相关文件路径

| 文件路径 | 说明 |
|---------|------|
| `itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/executor/HttpRequestExecutor.java` | HTTP 请求执行器，包含 SSE 格式化逻辑 |
| `itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/utils/VariableUtils.java` | 变量替换工具类，包含断言解析逻辑 |
| `itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/framework/VerifyFacade.java` | 验证门面，处理断言验证 |
| `itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/dto/HTTPRequest.java` | HTTP 请求 DTO，包含 `useSseFormat` 字段 |

## 下一步排查方向

1. **确认 `useSseFormat` 的值**：检查配置是否正确传递
2. **检查响应头**：确认 `Content-Type` 是否为 `text/event-stream`
3. **跟踪 response 变量**：确认格式化后的响应是否正确传递
4. **检查 SSE 格式化调用点**：确认所有可能的执行路径