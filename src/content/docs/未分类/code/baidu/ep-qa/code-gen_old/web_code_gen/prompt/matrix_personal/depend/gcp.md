---
title: "gcp"
description: "import \"context\" \"fmt\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_personal\\depend\\gcp.md"
---
### gcp数据操作
#### gcp常量配置，文件路径：`library/constant/gcp.go`
* 仅当需求描述中涉及新增gcp常量定义时才需要在此文件中定义常量，否则无需生成此文件内容
* 此文件追加生成内容即可，不要导包，示例如下：
```go
GcpKeyTest = "test_gcp" // 测试gcpKey
```
#### gcp底层数据操作代码，文件路径：`model/dao/gcp/personal/test_gcp.go`
```go
package personal

import (
	"context"
	"fmt"

	params "icode.baidu.com/baidu/searchbox/symframe-param"

	"icode.baidu.com/baidu/searchbox/personal-go/library/logger"
	"icode.baidu.com/baidu/searchbox/personal-go/library/resource"
	"icode.baidu.com/baidu/searchbox/personal-go/model/types/dto"
)

// GCP底层数据操作方法，示例如下：
// TestGcp ...
func TestGcp(ctx context.Context, gcpKey string) ([]*dto.TestGcpData, error) {
    // Filter操作，示例如下：
    // adaption, _ := params.LoadAdaption(ctx)
	// filter := adaption.ExportSearchBoxParams()
	// result, ok, err := resource.GcpCommonCf.FilterOne(gcpKey, filter)
	// if err != nil {
	// 	return nil, fmt.Errorf("read gcp<%s> cofiguration failed", gcpKey)
	// }
	// if !ok {
	// 	return nil, fmt.Errorf("analysis gcp<%s> cofiguration failed", gcpKey)
	// }
	// testMap, ok := result.(*map[string]string)
	// if !ok || testMap == nil {
	// 	return nil, fmt.Errorf("analysis gcp<%s> cofiguration failed", gcpKey)
	// }
	
	// Fetch操作，示例如下：
	// result, err := gcp.Fetch[dto.TestGcpParam](ctx, constant.GcpCommonAppId, gcpKey)
	// if err != nil {
	// 	logger.WarningF(ctx, "function[TestGcp] read gcp[%s] cofiguration failed error[%+v]", gcpKey, err)
	// 	return nil, fmt.Errorf("fetch gcp config<%s> cofiguration failed", gcpKey)
	// }

	// ...
}
```
* gcp包已经封装好的方法直接调用即可，方法使用参考：
```go
func Fetch[T any](ctx context.Context, appID, key string) (T, error) // 获取单条数据
func GetSwitch(ctx context.Context, appID, key string, defaultValue bool) (bool, error) // 获取开关数据
func MultiFetchWithExtraParam[T any](ctx context.Context, appID, key string, m map[string]interface{}) ([]T, error) // 获取多条数据
func FetchWithExtraParam[T any](ctx context.Context, appID, key string, m map[string]interface{}) (T, error) // 带额外参数筛选获取单条数据
```
