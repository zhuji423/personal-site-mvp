---
title: "controller"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_basic\\depend\\controller.md"
---
## controller层代码，注意参数解析、参数校验逻辑必须保留，文件路径：`controller/包名/功能名.go`
* controller层入口方法等已定义，此文件仅需生成追加内容即可，按照示例格式生成：
```go
package 包名

import (
	"context"
	
	"icode.baidu.com/baidu/gdp/ghttp"
	params "icode.baidu.com/baidu/searchbox/symframe-param"
	
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/errno"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/logger"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/render"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/utils"
	
	"icode.baidu.com/baidu/searchbox/sbox-basic/model/service/包名"
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request"
)

// TestFunc 测试接口-测试函数
func (c * Controller) TestFunc(ctx context.Context, req ghttp.Request) ghttp.Response {
    // 解析公参
	adaption, err := params.LoadAdaption(ctx)
	if err != nil {
		logger.WarningF(ctx, "failed to load adaption，error is %v", err)
		return render.Fail(ctx, errno.BadRequest)
	}
    
    // 接口参数校验
    testReq := request.TestReq{}
    if err := utils.ShouldBindWith(req, testReq); err != nil {
		logger.ErrorF(ctx, "params binding xxx request error, error is %s", err.Error())
		return render.Fail(ctx, errno.ErrInvalidParams)
	}
    
    // 通过对象调用service层逻辑处理函数，示例如下：
    resp, err := c.srv.TestFunc(ctx, testReq)
	if err != nil {
		return render.Fail(ctx, err)
	}

	return render.Success(ctx, resp)
}
```