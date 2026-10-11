---
title: "/engine/proxy/{id} 接口使用文档"
description: "/engine/proxy/{id} 接口使用文档"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📄 _engine_proxy_{id} 接口使用文档.md"
---
/engine/proxy/{id} 接口使用文档

# /engine/proxy/{id} 接口使用文档
## 接口概述
`/engine/proxy/{id}` 接口用于通过预配置的 API 代理配置发起代理请求。该接口支持两种请求格式：JSON 格式和 Multipart/Form-Data 格式（用于文件上传）。

**接口路径：** `/engine/proxy/{id}`
**请求方式：** POST
**Content-Type：** `application/json` 或 `multipart/form-data`

## 功能说明
该接口通过配置 ID (`id`) 查询预配置的 API 代理配置，然后使用配置中的 URI、Method、Headers 发起代理请求。请求的 Body 参数可以在调用时动态传入。

### 主要特点
1. **配置驱动**：通过配置 ID 关联预配置的 API 代理信息
2. **安全性**：Headers 配置在数据库中加密存储
3. **灵活性**：支持 JSON 和文件上传两种请求格式
4. **便捷性**：调用时只需提供配置 ID 和 Body 参数，无需重复配置 URI、Method、Headers

## 请求参数
### 路径参数
|参数名|类型|必填|说明|
|-|-|-|-|
|id|Long|是|API 代理配置 ID|

### 请求体（JSON 格式）
**Content-Type：** `application/json`

|参数名|类型|必填|说明|
|-|-|-|-|
|body|Object|否|请求参数，JSON 格式|

**请求示例：**

```
{
  "body": {
    "param1": "value1",
    "param2": "value2"
  }
}
```
### 请求体（Multipart/Form-Data 格式）
**Content-Type：** `multipart/form-data`

|参数名|类型|必填|说明|
|-|-|-|-|
|body|String|否|请求体，JSON 格式|
|file|File|否|上传的文件|
|fileParamName|String|否|文件参数名，默认为 "file"|

**请求示例（cURL）：**

```
curl -X POST "http://your-domain/engine/proxy/123" \
  -H "Content-Type: multipart/form-data" \
  -F 'body={"param1":"value1"}' \
  -F "file=@/path/to/file.jpg" \
  -F "fileParamName=uploadFile"
```
## 返回结果
### 成功响应
**Content-Type：** `application/json`

返回目标 API 的原始响应结果，格式为 JSON。

**返回示例：**

```
{
  "code": 0,
  "message": "success",
  "data": {
    "result": "data from target api"
  }
}
```
### 错误响应
|错误码|说明|
|-|-|
|PARAM_VALIDATE_ERROR|配置不存在或参数验证失败|
|BUSINESS_EXCEPTION|业务处理异常|

**错误响应示例：**

```
{
  "code": 400,
  "message": "配置不存在",
  "data": null
}
```
## 配置说明
API 代理配置存储在 `api_proxy_conf` 表中，包含以下字段：

|字段名|类型|说明|
|-|-|-|
|id|Long|配置 ID（主键）|
|uri|String|目标 API 地址|
|method|String|请求方法（GET、POST、PUT、DELETE、PATCH 等）|
|headers|String|请求头（JSON 格式，加密存储）|
|description|String|简介描述|
|owners|List|负责人列表|
|createUser|String|创建人|
|createTime|Timestamp|创建时间|
|updateUser|String|更新人|
|updateTime|Timestamp|更新时间|
|isDeleted|Integer|是否删除（0：否，1：是）|

## 使用场景
### 场景 1：调用第三方 API（JSON 格式）
**需求：** 调用第三方 API 获取用户信息

**步骤：**

1. **创建 API 代理配置**

    * URI：`https://api.example.com/user/info`
    * Method：`POST`
    * Headers：`{"Authorization": "Bearer token123"}`
    * 记录配置 ID，假设为 `123`

2. **调用接口**

```
curl -X POST "http://your-domain/engine/proxy/123" \
  -H "Content-Type: application/json" \
  -H "username: your-username" \
  -H "token: your-token" \
  -d '{
    "body": {
      "userId": "user001"
    }
  }'
```
### 场景 2：文件上传（Multipart 格式）
**需求：** 上传文件到第三方 API

**步骤：**

1. **创建 API 代理配置**

    * URI：`https://api.example.com/file/upload`
    * Method：`POST`
    * Headers：`{"Authorization": "Bearer token123"}`
    * 记录配置 ID，假设为 `456`

2. **调用接口**

```
curl -X POST "http://your-domain/engine/proxy/456" \
  -H "username: your-username" \
  -H "token: your-token" \
  -F 'body={"description":"test upload"}' \
  -F "file=@/path/to/file.jpg"
```
## 注意事项
1. **配置必须存在**：调用前需要确保配置 ID 对应的 API 代理配置已创建且未删除
2. **Headers 加密**：配置中的 Headers 会被加密存储，调用时会自动解密
3. **权限控制**：接口需要通过 TestOne 平台的认证（username 和 token）
4. **文件参数名**：上传文件时，`fileParamName` 参数用于指定文件在请求中的参数名，默认为 "file"
5. **错误处理**：如果配置不存在或参数验证失败，会返回相应的错误信息

## 相关接口
|接口路径|说明|
|-|-|
|`/engine/proxy`|直接发起代理请求（不使用配置）|
|`/engine/apiProxyConf`|API 代理配置管理接口|

## 常见问题
### Q1：如何获取 API 代理配置 ID？
A：通过 `/engine/apiProxyConf` 接口创建或查询 API 代理配置，获取配置 ID。

### Q2：Headers 中的敏感信息如何处理？
A：Headers 配置在数据库中会自动加密存储，调用时会自动解密，无需手动处理。

### Q3：支持哪些 HTTP 方法？
A：支持 GET、POST、PUT、DELETE、PATCH 等 HTTP 方法，具体取决于配置中的 method 字段。

### Q4：文件上传有大小限制吗？
A：文件上传大小限制取决于 TestOne 平台的配置，通常为 10MB。

---

**文档版本：** v1.0
**最后更新时间：** 2026-03-23
**维护人员：** TestOne 平台团队

# /engine/proxy/{id} 接口使用文档
## 接口概述
`/engine/proxy/{id}` 接口用于通过预配置的 API 代理配置发起代理请求。该接口支持两种请求格式：JSON 格式和 Multipart/Form-Data 格式（用于文件上传）。

**接口路径：** `/engine/proxy/{id}`
**请求方式：** POST
**Content-Type：** `application/json` 或 `multipart/form-data`

## 功能说明
该接口通过配置 ID (`id`) 查询预配置的 API 代理配置，然后使用配置中的 URI、Method、Headers 发起代理请求。请求的 Body 参数可以在调用时动态传入。

### 主要特点
1. **配置驱动**：通过配置 ID 关联预配置的 API 代理信息
2. **安全性**：Headers 配置在数据库中加密存储
3. **灵活性**：支持 JSON 和文件上传两种请求格式
4. **便捷性**：调用时只需提供配置 ID 和 Body 参数，无需重复配置 URI、Method、Headers

## 请求参数
### 路径参数
|参数名|类型|必填|说明|
|-|-|-|-|
|id|Long|是|API 代理配置 ID|

### 请求体（JSON 格式）
**Content-Type：** `application/json`

|参数名|类型|必填|说明|
|-|-|-|-|
|body|Object|否|请求参数，JSON 格式|

**请求示例：**

```
{
  "body": {
    "param1": "value1",
    "param2": "value2"
  }
}
```
### 请求体（Multipart/Form-Data 格式）
**Content-Type：** `multipart/form-data`

|参数名|类型|必填|说明|
|-|-|-|-|
|body|String|否|请求体，JSON 格式|
|file|File|否|上传的文件|
|fileParamName|String|否|文件参数名，默认为 "file"|

**请求示例（cURL）：**

```
curl -X POST "http://your-domain/engine/proxy/123" \
  -H "Content-Type: multipart/form-data" \
  -F 'body={"param1":"value1"}' \
  -F "file=@/path/to/file.jpg" \
  -F "fileParamName=uploadFile"
```
## 返回结果
### 成功响应
**Content-Type：** `application/json`

返回目标 API 的原始响应结果，格式为 JSON。

**返回示例：**

```
{
  "code": 0,
  "message": "success",
  "data": {
    "result": "data from target api"
  }
}
```
### 错误响应
|错误码|说明|
|-|-|
|PARAM_VALIDATE_ERROR|配置不存在或参数验证失败|
|BUSINESS_EXCEPTION|业务处理异常|

**错误响应示例：**

```
{
  "code": 400,
  "message": "配置不存在",
  "data": null
}
```
## 配置说明
API 代理配置存储在 `api_proxy_conf` 表中，包含以下字段：

|字段名|类型|说明|
|-|-|-|
|id|Long|配置 ID（主键）|
|uri|String|目标 API 地址|
|method|String|请求方法（GET、POST、PUT、DELETE、PATCH 等）|
|headers|String|请求头（JSON 格式，加密存储）|
|description|String|简介描述|
|owners|List|负责人列表|
|createUser|String|创建人|
|createTime|Timestamp|创建时间|
|updateUser|String|更新人|
|updateTime|Timestamp|更新时间|
|isDeleted|Integer|是否删除（0：否，1：是）|

## 使用场景
### 场景 1：调用第三方 API（JSON 格式）
**需求：** 调用第三方 API 获取用户信息

**步骤：**

1. **创建 API 代理配置**

    * URI：`https://api.example.com/user/info`
    * Method：`POST`
    * Headers：`{"Authorization": "Bearer token123"}`
    * 记录配置 ID，假设为 `123`

2. **调用接口**

```
curl -X POST "http://your-domain/engine/proxy/123" \
  -H "Content-Type: application/json" \
  -H "username: your-username" \
  -H "token: your-token" \
  -d '{
    "body": {
      "userId": "user001"
    }
  }'
```
### 场景 2：文件上传（Multipart 格式）
**需求：** 上传文件到第三方 API

**步骤：**

1. **创建 API 代理配置**

    * URI：`https://api.example.com/file/upload`
    * Method：`POST`
    * Headers：`{"Authorization": "Bearer token123"}`
    * 记录配置 ID，假设为 `456`

2. **调用接口**

```
curl -X POST "http://your-domain/engine/proxy/456" \
  -H "username: your-username" \
  -H "token: your-token" \
  -F 'body={"description":"test upload"}' \
  -F "file=@/path/to/file.jpg"
```
## 注意事项
1. **配置必须存在**：调用前需要确保配置 ID 对应的 API 代理配置已创建且未删除
2. **Headers 加密**：配置中的 Headers 会被加密存储，调用时会自动解密
3. **权限控制**：接口需要通过 TestOne 平台的认证（username 和 token）
4. **文件参数名**：上传文件时，`fileParamName` 参数用于指定文件在请求中的参数名，默认为 "file"
5. **错误处理**：如果配置不存在或参数验证失败，会返回相应的错误信息

## 相关接口
|接口路径|说明|
|-|-|
|`/engine/proxy`|直接发起代理请求（不使用配置）|
|`/engine/apiProxyConf`|API 代理配置管理接口|

## 常见问题
### Q1：如何获取 API 代理配置 ID？
A：通过 `/engine/apiProxyConf` 接口创建或查询 API 代理配置，获取配置 ID。

### Q2：Headers 中的敏感信息如何处理？
A：Headers 配置在数据库中会自动加密存储，调用时会自动解密，无需手动处理。

### Q3：支持哪些 HTTP 方法？
A：支持 GET、POST、PUT、DELETE、PATCH 等 HTTP 方法，具体取决于配置中的 method 字段。

### Q4：文件上传有大小限制吗？
A：文件上传大小限制取决于 TestOne 平台的配置，通常为 10MB。

---

**文档版本：** v1.0
**最后更新时间：** 2026-03-23
**维护人员：** TestOne 平台团队
