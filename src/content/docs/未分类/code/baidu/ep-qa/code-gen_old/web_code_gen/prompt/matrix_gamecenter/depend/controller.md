---
title: "controller"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\depend\\controller.md"
---
## controller层代码，文件路径：`servers/httpserver/controller/接口路径占位/功能名.go`
* 解释相关的注释不要生成
```go
package 包名or子包名

import (
    "context"

    "icode.baidu.com/baidu/gdp/ghttp"
    symframe "icode.baidu.com/baidu/searchbox/symframe-param"
    
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/parse"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/render"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/utils"
    
    typesTest "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/游戏模块名/接口路径占位"
    typesReq "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/request/接口路径占位"
    testSrv "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/service/接口路径占位"
)

// 解释：`TestFunc`对应`功能名`进行命名
// TestFunc ...
func TestFunc(ctx context.Context, req ghttp.Request) ghttp.Response {
	
	// req
	reqParams := &typesReq.TestReq{}
    if err = parse.ShouldBind(req, reqParams); err != nil {
		logger.WarningF(ctx, "bind params error, err[%+v]", err)
		return render.Fail(ctx, errno.BadRequest)
	}
	
	// main
    params := &typesTest.TestParams{
        TestUID: int64(adaption.PUID()),
        TestType: reqParams.TestType,
    }
    resp, err := testSrv.NewTestBase().TestFunc(ctx, params)
    if err != nil {
		return render.Fail(ctx, err)
	}
    return render.Success(ctx, resp)
}
```