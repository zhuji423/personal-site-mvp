---
title: "controller"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_personal\\depend\\controller.md"
---
## controller层代码，文件路径：`controller/personal/包名.go`
```go
package personal

import (
	"context"

	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/searchbox/personal-go/library/errno"
	"icode.baidu.com/baidu/searchbox/personal-go/library/render"
	"icode.baidu.com/baidu/searchbox/personal-go/library/utils"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/request"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/response"
)

// TestFunc 测试函数
func (ctl *Controller) TestFunc(ctx context.Context, req ghttp.Request) gthttp.Response {
    // 参数校验，按照以下格式生成：
    r := new(request.TestReq)
    if err := utils.ShouldBind(req, r); err != nil {
        return render.Fail(ctx, errno.MissingParameter)
    }
    
    // 调用service层的方法，示例如下：
    ret, err := ctl.srv.TestSrvFunc(ctx, r)
    if err != nil {
		return render.Fail(ctx, err)
	}

	res := response.TestResp{
		TestRet: ret,
	}
	return render.Success(ctx, res)
}
```
