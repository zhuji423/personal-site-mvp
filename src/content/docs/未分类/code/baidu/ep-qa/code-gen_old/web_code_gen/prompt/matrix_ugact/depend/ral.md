---
title: "service_test_func"
description: "import \"context\" \"fmt\" \"net/http\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\ral.md"
---
#### 下游http接口数据获取
##### conf层下游http接口ral配置（若已完成配置，则跳过此配置步骤），文件路径：`conf/servicer/service_test_func.toml`
* 注意配置信息等生成时需要生成一对一对应注释
```go
# service_test_func
Name = "service_test_func"
# 连接超时，
ConnTimeOut = 200
# 写数据超时
WriteTimeOut = 250
# 读数据超时
ReadTimeOut = 1000
# 请求失败后的重试次数：总请求次数 = Retry + 1
Retry = 1
# 资源使用策略，非必选，默认使用 RoundRobin
# RoundRobin: 依次轮询
[Strategy]
Name = "RoundRobin"

## 资源定位：BNS 配置，支持智能 BNS
[Resource.BNS]
BNSName = ""
EnableSmartBNS = true
UsePort = "main"
```
##### 下游http接口名配置，文件路径：`library/constant/service.go`
* 注意配置信息等生成时需要生成对应注释
* 此文件生成追加内容即可，不要导包，示例如下：
```go
// ServiceTestFunc接口服务
ServiceTestFunc = "service_test_func"
```
##### repository层
###### 下游http接口获取数据逻辑代码，文件路径：`repository/test_pkg/test_file.go`
* 文件夹`test_pkg`根据下游接口名进行命名，如：从需求解析的下游接口名为`feed_video`，则文件夹命名为`feed_video`
* 文件`test_file.go`根据要获取的数据描述进行命名，如：从需求解析从下游接口获取的数据是`历史记录列表数据`，那么文件可以命名为`history_list.go`
* 注意数据获取、处理等逻辑根据需求生成注释
```go
package test_pkg

import (
    "context"
    "fmt"
    "net/http"
    
    "icode.baidu.com/baidu/gdp/codec"
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/gdp/net/ral"
    "icode.baidu.com/baidu/searchbox/ugact/library/constant"
)

// TestGetHttpData ...
func TestGetHttpData(ctx context.Context, testReq *TestHttpReq) ([]TestHttpData, error) {
    // 下游http接口获取数据底层逻辑，示例如下：
    header := http.Header{}
    header.Set("Content-Type", "application/x-www-form-urlencoded")
    
    // 若解析为Get/get/GET请求，示例如下：
    // ralReq := &ghttp.RalRequest{
	// 	    Method: http.MethodGet,
	//    	Path:   testPath,
	//      Header: header,
	// 	    Query:  testReq,
	// }
    // ralResp := new(TestHttpRsp)
    
    // 若解析为Post/post/POST请求，示例如下：
    // postData := map[string]string {
    //     "testKey": "testValue",
    // }
    // ralReq := &ghttp.RalPostRequest{
    //     RalRequest: ghttp.RalRequest{
    //         Method: "POST",
    //         Path: testPath,
    //         Header: header,
    //         Query: testReq,
    //     }
    //     PostData: postData,
    //     Encoder:  codec.FORMEncoder,
    // }
    // resp := new(TestHttpRsp)
    // ralResp := &ghttp.RalResponse{
    //     Data: resp,
    //     Decoder: codec.JSONDecoder,
    // }
    
    // 请求结果处理
    err = ral.RAL(ctx, constant.ServiceTestFunc, ralReq, ralResp)
    if err != nil {
        return nil, err
    }
    if resp.Errno != "0" {
        return nil, fmt.Errorf("error messsage  resp errno: %s", resp.Errno)
    }
    return resp.Data, nil
}
```
###### 下游http接口数据获取涉及到的常量、结构体定义，文件路径：`repository/test_pkg/types.go`
* 注意常量、结构体等生成时需要生成对应注释
```go
package test_pkg

// 常量定义
const (
    testPath = "/test/path"  // 下游接口路径
)

// TestHttpReq ...
type TestHttpReq struct {
    TestID int64  `json:"test_id"` // 测试ID
}

// TestHttpRsp ...
type TestHttpRsp struct {
    Errno string          `json:"errno"`  // 错误码
    Data []TestHttpData  `json:"data"` // 返回数据列表
}

// TestHttpData ...
type TestHttpData struct {
    TestID int64  `json:"test_id"`  // 测试ID
    TestName string `json:"test_name"` // 测试名称
}
```