---
title: "data"
description: "import \"context\" \"fmt\" \"strings\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_personal\\depend\\data.md"
---
## data层代码，文件路径：`model/data/包名/功能名.go`
```go
package 包名

import (
	"context"
	"fmt"
	"strings"

	"icode.baidu.com/baidu/searchbox/personal-go/library/logger"
	"icode.baidu.com/baidu/searchbox/personal-go/library/utils"
	"icode.baidu.com/baidu/searchbox/personal-go/library/constant"
	// 若涉及gcp数据获取，需导入gcp底层数据操作包
	gcpPersonal "icode.baidu.com/baidu/searchbox/personal-go/model/dao/gcp/personal"
	// 若涉及redis数据获取，需导入redis底层数据操作包
	redisPersonal "icode.baidu.com/baidu/searchbox/personal-go/model/dao/redis/personal"
	// 若涉及ral第三方下游数据获取，需导入ral底层数据操作包
	"icode.baidu.com/baidu/searchbox/personal-go/model/dao/包名"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/dto"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/request"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/response"
)

// data层导出方法，示例如下：
// TestGetData ...
func TestGetData(ctx context.Context, r *request.TestReq) (*dto.TestData, error) {
    // 调用dao层底层数据操作方法实现完整数据获取逻辑代码
}

// data层内部方法，格式为：`func testDataFunc(...) (...) {...}`  
```
