---
title: "baidu_wenku-go_tfapi"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\iapi\\api_code\\baidu_wenku-go_tfapi.md"
---
## router层代码，注意中间件的保留，文件名：`httpserver/routers/test_pkg.go`
```go
package routers

import (
    "context"

	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/wenku-go/golib/wkhttp/gmiddleware"

	"icode.baidu.com/baidu/wenku-go/tfapi/httpserver/controller/test_pkg"
	"icode.baidu.com/baidu/wenku-go/tfapi/library/resource"
)


// RegisterTest 注册测试路由
func RegisterTest(router ghttp.Router) {
    grTest := router.Group("/test_pkg")
    grTest.HandleFunc("POST", "/test_func", test_pkg.NewTestFunc(), gmiddleware.NewUserLoginWareFunc(resource.LoggerService()))
}
```
## controller层代码，注意保留参数校验，文件名：`httpserver/controller/test_pkg/test_func.go`
```go
package test_pkg

import (
	"context"
	"encoding/json"
	"strconv"

	"github.com/gin-gonic/gin"
	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/gdp/logit"
	"icode.baidu.com/baidu/wenku-go/golib/wkerror"
	"icode.baidu.com/baidu/wenku-go/golib/wkhttp/frame"

	"icode.baidu.com/baidu/wenku-go/tfapi/library/resource"
	"icode.baidu.com/baidu/wenku-go/tfapi/library/util"
	"icode.baidu.com/baidu/wenku-go/tfapi/model/service/test_pkg"
)

// testFunc ...
type testFunc struct {
    AIBase
    Params SetTestParams
}

// SetTestParams 参数
type SetTestParams struct {
    ShowPage  string `json:"showPage" form:"showPage"` // 显示页面
    TestId    int    `json:"testId" form:"testId"` // 测试ID
}

// TestFuncRsp 返回体
type TestFuncRsp struct {
    TestUserInfo string  `json:"testUserInfo"`  // 测试用户信息
}

// NewTestFunc 返回一个ghttp.HandlerFunc类型的函数
func NewTestFunc() ghttp.HandlerFunc {
	return frame.NewCommonHandle(
		func() (frame.Executor, []frame.MiddleWareFunc) {
			return &testFunc{}, nil
		},
	)
}

// OnInit 中间件函数
func (t *testFunc) OnInit(ctx context.Context, req ghttp.Request, next frame.MiddleWareQueue) (data interface{}, err error) {
    gctx := gin.Context{
		Request: req.HTTPRequest(),
	}
	if err := gctx.ShouldBind(&g.Params); err != nil {
		resource.LoggerService().Warning(ctx, "ShouldBind error", logit.AutoField("err", err))
		return nil, wkerror.New(wkerror.ErrorCodeParamsError)
	}
	
	// user
	if e := t.UserLoginCheck(ctx); e != nil {
		return nil, e
	}

	// get sula conf
	t.FeedSampleId(ctx) //获取小流量实验ID
	if e := t.SulaConfNewCheck(ctx, t.UID, "", t.SampleId, t.Params.ShowPage, entertrytf.HasAIDialogAbility); e != nil {
		return nil, e
	}
	
	// api frequency forbidden
	if e := t.ApiFrdCheck(ctx, t.UID, "xxx", t.Entry.SulaConf.AiDialog.ApiFrequency); e != nil {
		return nil, e
	}

	// checkparams
	if e := t.checkParams(ctx); e != nil {
		return nil, wkerror.New(wkerror.ErrorCodeParamsError, e.Error())
	}

	return next.Next(ctx, req)
}

// OnExecute 执行函数
func (t *testFunc) OnExecute(ctx context.Context, req ghttp.Request) (interface{}, error) {
	var testResp = &TestFuncRsp{}
	
    // 调用service层、data层等封装方法实现业务逻辑，示例如下：
    // testRes, err := test_pkg.TestSrvFunc(ctx, t.Params.TestId)
    // if err != nil {
    //     return nil, err
    // }
    
    return testRes, nil
}

// checkParam 参数检查
func (t *testFunc) checkParam(ctx context.Context) error {
    // 参数深入解析校验逻辑实现在此处
	return nil
}
```
## service层，文件名：`model/service/test_pkg/test_func.go`
```go
package test_pkg

import (
	"context"

	"icode.baidu.com/baidu/wenku-go/tfapi/model/data/test_pkg"
)

type TestSrvFunc struct {}

// TestSrvResp 返回体
type TestSrvRsp struct {
    TestName string  `json:"testName"`  // 测试名称
}

// TestSrvFunc 测试服务函数
func (t *TestSrvFunc) TestSrvFunc(ctx context.Context, testId int) (testSrvRes *TestSrvResp, err error) {
     // 业务逻辑的具体实现
}
```