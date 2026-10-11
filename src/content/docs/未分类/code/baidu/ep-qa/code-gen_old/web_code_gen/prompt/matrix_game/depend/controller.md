---
title: "controller"
description: "// 注意导包顺序需遵守规范 import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_game\\depend\\controller.md"
---
## controller层代码，文件路径：controller/path1/path2/功能名.go
* `path1`、`path2`命名根据输入接口路径层级来确定，要求如下：
1. 经解析接口路径为三层级时，路径中`path1`对应`包名`，`path2`对应`子包名`，如：接口路径为`testing/intervene/testFunc`时，路径中`path1`对应`testing`，`path2`对应`intervene`
2. 经解析接口路径为两层级时，路径中`path1`为`ddz`，`path2`对应`包名`，如：接口路径为`task/testFunc`时，路径中`path1`为`ddz`，`path2`对应`task`
```go
package path2


// 注意导包顺序需遵守规范
import (
    "context"

    "icode.baidu.com/baidu/gdp/ghttp"
    symframe "icode.baidu.com/baidu/searchbox/symframe-param"
    
    "icode.baidu.com/baidu/searchbox/ug-game/library/errno"
    "icode.baidu.com/baidu/searchbox/ug-game/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-game/library/render"
    "icode.baidu.com/baidu/searchbox/ug-game/library/parse"
    "icode.baidu.com/baidu/searchbox/ug-game/library/utils"
    
    typesReq "icode.baidu.com/baidu/searchbox/ug-game/model/types/模块包占位/request/接口路径占位"
    typesTest "icode.baidu.com/baidu/searchbox/ug-game/model/types/模块包占位/游戏模块名/接口路径占位"
    testSrv "icode.baidu.com/baidu/searchbox/ug-game/model/service/模块包占位/接口路径占位"
)

// 解释：`TestFunc`对应`功能名`进行命名
// TestFunc ...
func TestFunc(ctx context.Context, req ghttp.Request) ghttp.Response {
    // common
    adaption, err := symframe.LoadAdaption(ctx)
    if err != nil {
		logger.WarningF(ctx, "adaption error, err[%+v]", err)
		return render.Fail(ctx, errno.BadRequest)
	}
	if utils.IsInvalidCUID(adaption.CUID()) || utils.IsDenyApp(adaption.AppName()) {
		logger.WarningF(ctx, "cuid or appname params error, cuid=%v appname=%v", adaption.CUID(), adaption.AppName())
		return render.Fail(ctx, errno.BadRequest)
	}
	if adaption.PUID() == 0 {
		logger.WarningF(ctx, "CashFlows PUID() err, PUID() is 0")
		return render.Fail(ctx, errno.UnauthorizedUser)
	}
	
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