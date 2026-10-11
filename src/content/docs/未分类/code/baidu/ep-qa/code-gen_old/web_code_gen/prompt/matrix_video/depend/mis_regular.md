---
title: "mis_regular"
description: "// TestRegularConf 新增常规页面结构体定义 type TestRegularConf struct { TestPageId string json:\"testPageId\" // 测试页面ID } 新增常规amis页面配"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\mis_regular.md"
---
### amis相关底层逻辑代码&配置（关键词：`mis`、`amis`、`爱速搭`）
* 新增amis常规页面封装好的逻辑代码参考，文件路径：`model/data/common/mis_ltcache.go`（仅供参考，无需生成）
```go
func (lt *LTCacheData) GetDuoDuoBannerByApp(productID int) (map[string][]*mis.Banner, error)
func (lt *LTCacheData) GetAllTaskConfByApp(productID int) (map[int]*mis.TaskInfo, error)
func (lt *LTCacheData) GetKeepSigninByApp(productID int) (*mis.KeepSignin, error)
func (lt *LTCacheData) GetSingleTaskConfByApp(productID int, taskID int) (*mis.TaskInfo, error)
func (lt *LTCacheData) GetWithdrawByApp(productID int) (*mis.WithdrawConf, error)
func (lt *LTCacheData) GetPaymentTaskByApp(productID int) (*mis.PaymentTask, error)
// ...
```
#### 新增常规amis页面结构体定义，文件路径：`library/mis/struct_test_mis.go`
* 此文件必须生成一对一的注释
```go
package mis

// TestRegularConf 新增常规页面结构体定义
type TestRegularConf struct {
    TestPageId string `json:"testPageId"`  // 测试页面ID
}
```
#### 新增常规amis页面配置，文件路径：`library/mis/struct.go`
* 此文件必须生成一对一的注释
* 此文件仅需追加生成内容即可，不要导包，示例如下：
```go
type DuoDuoConfContent struct {
    TestRegularConf *TestRegularConf `json:"testRegularConf"`  // 新增常规页面
}
```
#### 新增常规amis页面脚手架逻辑代码，文件路径：`components/miscache/loader.go`
* 此文件仅需追加生成内容即可，不要导包，示例如下：
```go
func loadDuoDuoConf(ctx context.Context, confID int) (cache.Storage, error) {
    // 需要在loadDuoDuoConf中添加对应的配置项，示例如下：
    testRegularConf := loadTestRegularConf(ctx, content.TestRegularConf)
	if testRegularConf != nil {
		_ = storage.Set(mis.TestGroupRegularConf+strconv.Itoa(confID), testRegularConf)
	}
}

// 需要完成load函数方法的实现，示例如下：
// loadTestRegularConf ...
func loadTestRegularConf(ctx context.Context, testRegularConf *mis.TestRegularConf) *mis.TestRegularConf {
    return testRegularConf
}
```
#### 新增常规页面amis相关常量配置，文件路径：`library/mis/consts.go`
* 此文件必须生成一对一的注释
* 此文件仅需追加生成内容即可，不要导包，示例如下：
```go
TestGroupRegularConf = "regular_conf_"  // 新增常规页面分组前缀
```