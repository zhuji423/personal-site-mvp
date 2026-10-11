---
title: "ral 编码规则"
description: "1.2 基础字段构造 - 所有请求必须显式构造： - Header - Query 参数（url.Values） - Body（POST 请求） - RALResponse 结构 2. GET 请求规则 GET 请求必须按照以下格式构造： "
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\ral.md"
---
# ral 编码规则
**ral主要是针对下游服务进行请求的封装，所有请求必须使用 RAL 请求结构体，并按照以下规则进行构造**
1. 通用请求构造规则   
1.1 请求类型 根据请求方式使用不同结构体：
   - GET请求 ：使用 ghttp.RalRequest
   - POST请求 ：使用 ghttp.RalPostRequest  

1.2 基础字段构造
  - 所有请求必须显式构造：
     - Header 
     - Query 参数（url.Values）
     - Body（POST 请求） 
     - RALResponse 结构
2. GET 请求规则  
GET 请求必须按照以下格式构造：
```go
queryParams := url.Values{}
queryParams.Add("key", value)

ralRequest := &ghttp.RalRequest{
    Method: http.MethodGet,
    Path:   path,
    Query:  queryParams,
    Header: map[string][]string{
        "Content-Type": {"application/json"},
        "hash_tag":     {tagValue},
    },
}
```  
2.1 Query 参数规则
  - 使用 url.Values{}
  - 统一 Add 方法添加参数

2.2 Header 规则
  - 必须使用 map[string][]string 格式
  - 内容示例：
```go
"Content-Type": {"application/json"}
```
3. POST 请求规则  
POST 请求必须使用：
```go
ralReq := &ghttp.RalPostRequest{
    RalRequest: ghttp.RalRequest{
        Method: "POST",
        Path:   path,
        Header: header,
        Query:  queryParams,
    },
    PostData: postData,
    Encoder:  codec.FORMEncoder 或 codec.JSONEncoder,
}
```
3.1 Header 规则  
POST 请求必须使用 http.Header：
```go
header := http.Header{}
header.Set("Content-Type", "application/x-www-form-urlencoded")
```
3.2 Body（PostData）规则
  - 必须使用 map 作为 PostData
  - 若 body 是结构体，需使用 jsoniter.MarshalToString 序列化
```go
dataStr, _ := jsoniter.MarshalToString(data)
postData := map[string]string{
    "data": dataStr,
}
```
4. 响应解析规则（GET/POST 通用）  
RAL 响应必须遵循固定模板：
```go
resp := new(RespStruct)
ralResp := &ghttp.RalResponse{
	Data:    resp,
	Decoder: codec.JSONDecoder,
}
```
此处 RespStruct 为接口返回的数据结构。

5.错误处理规则（核心一致性要求）   
5.1 RAL 执行错误
```go
err := ral.RAL(ctx, serviceName, ralRequest, ralResp)
if err != nil {
	logger.Warning(ctx,
	    fmt.Sprintf("failed to call %s: err[%+v]", serviceName, err))
	return nil, err
}
```
5.2 业务 errno 校验规则  
若 response 结构中存在 Errno 字段，必须校验：
```go
if resp.Errno != "0" {
    return nil, fmt.Errorf("ral resp errno: %s", resp.Errno)
}
```
6. 空值校验规则（若结构体以 Data 返回）   
若业务约定 resp.Data == nil 表示失败，需处理：
```go
if resp.Data == nil {
    return nil, fmt.Errorf("ral resp data is nil")
}
```
7. 函数返回规则  
最终必须返回业务数据，例如：
```go
return resp.Data, nil
```

可参考下面示例：  
ral 相关写法可以参考以下示例：
```go
func PlayLetFreeList(ctx context.Context) (infos []FreeData, err error) {
	header := http.Header{}
	header.Set("Content-Type", "application/x-www-form-urlencoded")

	queryParams := url.Values{}
	queryParams.Add("branchname", "baiduboxlite")

	dataInfo := map[string]any{
		"fe_page_type": "widget",
		"type":         "free_top",
	}
	dataStr, jsonErr := jsoniter.MarshalToString(dataInfo)
	if jsonErr != nil {
		return nil, jsonErr
	}
	postData := map[string]string{
		"data": dataStr,
	}
	ralReq := &ghttp.RalPostRequest{
		RalRequest: ghttp.RalRequest{
			Method: "POST",
			Path:   path,
			Header: header,
			Query:  queryParams,
		},
		PostData: postData,
		Encoder:  codec.FORMEncoder,
	}
	resp := new(HotListRsp)
	ralResp := &ghttp.RalResponse{
		Data:    resp,
		Decoder: codec.JSONDecoder,
	}
	err = ral.RAL(ctx, constant.ServiceFeedVideo, ralReq, ralResp)
	if err != nil {
		return nil, err
	}
	if resp.Errno != "0" {
		return nil, fmt.Errorf("feed video resp errno: %s", resp.Errno)
	}

	return resp.Data, nil
}
````