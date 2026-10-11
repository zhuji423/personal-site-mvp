---
title: "errno"
description: "import \"icode.baidu.com/baidu/gdp/extension/gerror\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\depend\\errno.md"
---
## service层业务逻辑用到的错误码定义，文件路径：`library/errno/包名.go`
* 常规参数校验、基础配置校验等错误码已在当前文件夹下common.go文件中定义，无需生成，当前文件仅生成业务逻辑相关特定错误码
* 此文件必须生成注释
```go
package errno

import "icode.baidu.com/baidu/gdp/extension/gerror"

var (
    TestExistDataError = gerror.NewCodeError(10000, "test exist data error")  // 现有数据获取错误
    TestNewDataError   = gerror.NewCodeError(10001, "test new data error")  // 新数据获取错误
)
```