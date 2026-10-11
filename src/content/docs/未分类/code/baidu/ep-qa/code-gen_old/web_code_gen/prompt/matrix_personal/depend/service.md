---
title: "service"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_personal\\depend\\service.md"
---
## service层代码，文件路径：`model/service/personal/包名.go`
```go
package personal

import (
    "context"

	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/searchbox/personal-go/library/constant"
	"icode.baidu.com/baidu/searchbox/personal-go/library/errno"
    "icode.baidu.com/baidu/searchbox/personal-go/model/data/包名"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/dto"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/request"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/response"
)


// service层导出方法，示例如下：
// TestSrvFunc ...
func (p *PersonalSrv) TestSrvFunc(ctx context.Context, r *request.TestReq) (*response.TestSrvResp, error) {
    // 调用data层数据获取方法实现完整的业务逻辑代码
}

// service层内部方法，格式为：`func (p *PersonalSrv) testSrvFunc(...) (...) {...}`  
```
