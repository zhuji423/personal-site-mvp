---
title: "service"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_basic\\depend\\service.md"
---
## service层
* service层是根据需求，解析并调用data层封装好的数据获取逻辑获取不同来源的数据，进行后续对数据进行处理的业务逻辑代码的实现
### service层入口代码，文件路径：`model/service/包名/功能名_base.go`
```go
package 包名

import (
	"context"

	testData "icode.baidu.com/baidu/searchbox/sbox-basic/model/data/包名"
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request"
	response "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/response"
)

type TestService interface {
    TestFunc(ctx context.Context, req request.TestReq) (resp response.TestResp, err error)
}
```
### service层业务逻辑代码，文件路径：`model/service/包名/功能名.go`
* 交互入口方法已定义无需生成，按照示例格式生成即可
```go
package 包名

import (
	"context"
	
    // 若有并行数据获取的逻辑，需要导入gtask包来实现
    // "icode.baidu.com/baidu/gdp/extension/gtask"
    
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/errno"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/constant"
	
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request/包名"
	response "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/response/包名"
)

// TestFunc ...
func (s *service) TestFunc(ctx context.Context, req request.TestReq) (*response.TestResp, error) {
    // 业务逻辑实现，示例如下：
    testData, err := s.TestDataFunc(ctx, req.testId) 
    if err != nil {
        logger.WarningF(ctx, "failed to xxx, error is %v", err)
		return nil, err
    }
    // ...
}
```
#### service层导出方法入口，文件路径：`model/service/ddmission/service.go`
* 此文件仅需生成追加内容即可，不要导包，示例如下：
```go
// TestFunc ...
TestFunc(ctx context.Context, req request.TestReq) (*response.TestResp, error)
```