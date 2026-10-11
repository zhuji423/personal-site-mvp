---
title: "service_test_ral"
description: "import \"context\" \"fmt\" \"net/http\" \"net/url\" \"time\" \"strconv\" \"string\" \"errors\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\ral.md"
---
### thirdparty第三方下游底层数据操作
#### ral下游数据获取conf配置代码，文件路径：`conf/servicer/service_test_ral.toml`
* 此文件必须生成一对一对应注释
```toml
# service_test_ral
Name = "service_test_ral"
# 连接超时，
ConnTimeOut = 300
# 写数据超时
WriteTimeOut = 150
# 读数据超时
ReadTimeOut = 500
# 请求失败后的重试次数：总请求次数 = Retry + 1
Retry = 1
# 资源使用策略，非必选，默认使用 RoundRobin
# RoundRobin: 依次轮询
[Strategy]
Name = "RoundRobin"

## 资源定位：BNS 配置，支持智能 BNS
[Resource.BNS]
BNSName = "xxx"
EnableSmartBNS = true
UsePort = "main"
```
#### ral下游接口服务名称配置代码，文件路径：`library/consts/service_name.go`
* 此文件必须生成一对一对应注释
* 此文件仅需生成追加内容即可，不要导包，示例如下：
```go
// ServiceRalTest ...
ServiceRalTest = "service_test_ral"  
```
#### ral下游数据获取逻辑代码，文件路径：`thirdparty/下游接口包名/test_ral.go`
* 所有结构体命名前缀要用`Ral`作为前缀，不能包含`下游接口包名`，例如：当路径中`下游接口包名`为`test_pkg`时，则逻辑结构体命名为：`test_pkg.RalTestPkg`
* 根据需求正确解析下游接口的请求方式是POST还是GET，然后根据请求方式组装参数，调用对应请求方法
```go
package 包名

import (
    "context"
	"fmt"
	"net/http"
	"net/url"
	"time"
	"strconv"
	"string"
	"errors"
	
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
	libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/gdp/net/ral"
)

// 结构体以`Ral`为前缀进行命名，示例如下：
// RalTest ...
type RalTest struct {
	Ctx       context.Context
    RalName   string
	TestProductID int
}

// NewRalTest ...
func NewRalTest(ctx *ibase.APIContext, testProductID int) (*RalTest, error) {
    ralName := libConsts.ServiceRalTest
    serv := servicer.DefaultMapper.Servicer(ralName)
	if serv == nil {
		return nil, errors.New("task ral conf not found")
	}
	return &RalTest{
		Ctx:           ctx,
        RalName:       ralName
		TestProductID: testProductID,
	}
}

// RalTestFunc ...
func (tr *RalTest) RalTestFunc(testCUID string) (*RalTestRespData, error) {
    // ...
    
    // 参数组装，示例如下：
    params := make(map[string]interface{})
	params = tr.getReqParams(testCUID, utsParams)
	paramsStrTmp, err := json.Marshal(params)
	if err != nil {
		return nil, err
	}
	nowTime := strconv.FormatInt(time.Now().Unix(), 10)
	paramsStr := string(paramsStrTmp)
	data := url.Values{
		"params": {paramsStr},
		"time":   {nowTime},
		"sign":   {util.MD5Encode(paramsStr+nowTime, TestToken)},
	}
	header := url.Values{
		"Content-Type": {"application/x-www-form-urlencoded"},
	}
	/*
    （1）根据需求解析第三方下游接口的请求方式是Get还是Post请求
    （2）调用解析出请求类型对应的方法进行数据获取
    */
    // 调用请求方法，示例如下：
	respData, err := tr.Get或Post请求方法(TestPath, data, header)
	if err != nil {
		logit.AddNotice(tr.ctx, logit.Error("requestxxx-fail", err))
		return nil, err
	}
	rsp := &RalTestResp{}
	err = json.Unmarshal(respData, rsp)
	if err != nil {
		logit.AddNotice(tr.ctx, logit.String("requestxxx-Unmarshal-fail", fmt.Sprintf("err:%v, res:%v", err.Error(), string(respData))))
		return nil, err
	}
	if rsp.ErrNo != 0 {
		logit.AddNotice(tr.ctx, logit.String("requestxxx-fail", strconv.Itoa(rsp.ErrNo)+","+rsp.ErrMsg))
	}
	return rsp.Data, err
}

// getReqParams 组装请求参数
// getReqParams ...
func (tr *RalTest) getReqParams(testCUID string, RalTestParams *RalTestParams) map[string]interface{} {
    params := make(map[string]interface{})
    
    // 传入参数，组装示例：
    // param["testCUID"] = testCUID
    
    // 从对象解析参数，组装示例：
    // params["productId"] = tr.TestProductId
    
    // 从参数结构体解析参数，组装示例：
    // params["testVersion"] = RalTestParams.TestVersion
    
    // ...
	return params
}

// sendGet/PostRequest，GET或POST请求，示例如下：
// sendGet/PostRequest ...
func (tr *RalTest) sendGet/PostRequest(uri string, params interface{}, header map[string][]string) ([]byte, error) {
    // 若为get、Get、GET请求，参数示例如下：
    // request := &ghttp.RalRequest{
    //  Method:   "GET",
	// 	Path:     uri,
	// 	Header:   header,
	// 	Query: param,
    // }
    // resp := &RalTestResp{}

    // 若为post、Post、POST请求，参数示例如下：
    // query := url.Values{}
    // query参数组装示例
    // query.Add("xxx", xxx)
    // request := &ghttp.RalPostRequest{
    //    RalRequest: ghttp.RalRequest{
    //        Method: http.MethodPost,
    //        Query: query,
    //        Path: uri,
    //        Header: header,
    //    }
    //    PostData: params,
	//    Encoder:  codec.JSONEncoder,
    // } 
   	// resp := &RalTestResp{}
	// ralResp := &ghttp.RalResponse{
	// 	Data:    resp,
	// 	Decoder: codec.JSONDecoder,
	// }
    
    // 结果获取与返回，格式示例如下：
	err := ral.RAL(ctx, t.RalName, request, ralResp)
	if err != nil {
		return nil, err
	}

	rawResp := ralResp.Response()
	defer rawResp.Body.Close()
	return ioutil.ReadAll(rawResp.Body)
}
```
#### ral下游数据获取相关常量定义，文件路径：`thirdparty/下游接口包名/consts.go`
* 此文件必须生成一对一对应注释
```go
package 包名

const (
    TestPath = "/xxx/xxx"  // 请求路径
    TestToken = "xxxxxx"   // 签名token
)
```
#### ral下游数据获取相关请求、响应等结构体定义，文件路径：`thirdparty/下游接口包名/type.go`
* 所有结构体命名前缀要用`Ral`作为前缀，不能包含`下游接口包名`，例如：当路径中`下游接口包名`为`test_pkg`时，则返回结构体命名为：`test_pkg.RalTestPkgResp`
* 此文件定义结构体及其变量必须一一对应生成注释
```go
package 包名

// 结构体以`Ral`为前缀进行命名，示例如下：

// RalTestParams ...
type RalTestParams struct {
	TestVersion string `json:"testVersion" form:"testVersion`  // 测试版本号
}

// RalTestResp ...
type RalTestResp struct {
    ErrNo  int                 `json:"errno" form:"errno`  // 错误码
    ErrMsg string              `json:"errmsg" form:"errmsg`  // 错误信息
    Data                       *RalTestRespData `json:"data" form:"data`  // 响应体数据
}

// RalTestRespData ...
type RalTestRespData struct {
    TestCUID string `json:"testCUID" form:"testCUID`  // 测试用户ID
}
```