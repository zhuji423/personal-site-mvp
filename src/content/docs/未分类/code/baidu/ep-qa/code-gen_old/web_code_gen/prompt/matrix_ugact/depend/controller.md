---
title: "controller"
description: "import \"context\" \"icode.baidu.com/baidu/gdp/ghttp\" \"icode.baidu.com/baidu/searchbox/ugact/library/errno\" \"icode.baidu.co"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\controller.md"
---
## controller层代码，文件路径：`controller/包名/功能名.go`
### 入参: context.Context和ghttp.Request，  出参: ghttp.Response
* 注意此文件无需生成注释
```go
package 包名

import (
    "context"
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/searchbox/ugact/library/errno"
    "icode.baidu.com/baidu/searchbox/sboxlib/extension/httputil"
    "icode.baidu.com/baidu/searchbox/ugact/library/render"
    "icode.baidu.com/baidu/searchbox/ugact/service/包名"
    "icode.baidu.com/baidu/searchbox/ugact/service/包名/types"
)

// Controller ...
type Controller struct {
    srv *包名.Service
}

// NewController ...
func NewController() *Controller {
    return &Controller{
        srv: 包名.NewService(),
    }
}

// TestFunc ...
func (ctl *Controller) TestFunc(ctx context.Context, request ghttp.Request) ghttp.Response {
    // 从types包获取对应的请求变量
    TestReq := new(types.TestReq)
    // 使用封装好的方法校验参数的合法性
    if err := httputil.ShouldBindWith(request, TestReq); err != nil {
        return render.Fail(ctx, errno.RewriteMsg(errno.ErrInvalidParams, err.Error()))
    }
    // 调用service层的逻辑处理函数
    resp, err := ctl.srv.TestFunc(ctx, TestReq)
    if err != nil {
        return render.Fail(ctx, err)
    }

    return render.Success(ctx, resp)
}
```