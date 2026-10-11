---
title: "mis"
description: "// TestRegularConf 新增常规页面结构体定义 type TestRegularConf struct { TestPageId string json:\"testPageId\" // 测试页面ID } 新增常规mis页面配置"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\mis.md"
---
### mis相关底层逻辑代码&配置（关键词：mis、amis、爱速搭）
1. 根据需求描述解析mis页面类型哪种属于：（1）常规页面；（2）实验页面
2. 根据解析出的页面类型，生成页面类型对应的mis配置文件、逻辑代码
#### 若解析为新增mis实验页面，则配置&逻辑代码示例如下：
##### 新增mis实验页面配置，文件路径：`library/mis/struct_smaple.go`
* 本文件生成追加内容即可，示例如下：
```go
type SampleConf struct {
    // 需要在SampleConf结构体中新增对应的实验配置项，示例如下：
    TestExperiment  *SampleData   `json:"newTestExperiment"`  // 新增实验页面
}
```
##### 新增mis实验数据加载逻辑代码，文件路径：`model/data/sample/sample.go`
* 本文件生成追加内容即可，示例如下：
```go
// 需要在当前文件中新增实验逻辑函数的实现，示例如下：
// IsHitTestExperiment ...
func (usd *UserSampleData) IsHitTestExperiment() bool {
	config, err := usd.cache.GetSampleByApp(usd.productID)
	if err != nil || config == nil || config.TestExperiment == nil {
		logit.AddNotice(usd.ctx, logit.String("t_e-isValid", "0"))
		return false
	}
	if config.TestExperiment.Switch != "1" {
		logit.AddNotice(usd.ctx, logit.String("t_e-switch", "0"))
		return false
	}
	// 判断反转实验是否命中
	sidCommon := common.NewSIDCommon(usd.ctx)
	isHit := sidCommon.IsShowTaskBySID(config.TestExperiment.Sids, "")
	//命中反转
	if !isHit {
		logit.AddNotice(usd.ctx, logit.String("t_e-hit", "1"))
		return false
	}
	logit.AddNotice(usd.ctx, logit.String("t_e-un-hit", "1"))
	return true
}
```
#### 若解析为新增mis常规页面配置，则配置&逻辑代码示例如下：
##### 新增常规mis页面结构体定义，文件路径：`library/mis/struct_test_mis.go`
```go
package mis

// TestRegularConf 新增常规页面结构体定义
type TestRegularConf struct {
    TestPageId string `json:"testPageId"`  // 测试页面ID
}
```
##### 新增常规mis页面配置，路径：`library/mis/struct.go`
* 本文件生成追加内容即可，示例如下：
```go
type DuoDuoConfContent struct {
    TestRegularConf *TestRegularConf `json:"testRegularConf"`  // 新增常规页面
}
```
##### 新增常规mis页面脚手架逻辑代码，文件路径：`components/miscache/loader.go`
* 本文件生成追加内容即可，示例如下：
```go
func loadDuoDuoConf(ctx context.Context, confID int) (cache.Storage, error) {
    // 需要在loadDuoDuoConf中添加对应的配置项，示例如下：
    testRegularConf := loadTestRegularConf(ctx, content.TestRegularConf)
	if testRegularConf != nil {
		_ = storage.Set(mis.TestGroupRegularConf+strconv.Itoa(confID), testRegularConf)
	}
}

// 需要完成load函数方法的实现，示例如下：
func loadTestRegularConf(ctx context.Context, testRegularConf *mis.TestRegularConf) *mis.TestRegularConf {
    return testRegularConf
}
```
##### 新增常规页面mis相关常量配置，文件路径：`library/mis/consts.go`
* 本文件生成追加内容即可，示例如下：
```go
const (
    TestGroupRegularConf = "regular_conf_"  // 新增常规页面分组前缀
)
```
##### 新增mis常规页面封装好的逻辑代码参考，存放路径：`model/data/common/mis_ltcache.go`（仅供参考，无需生成）
```go
func (lt *LTCacheData) GetDuoDuoBannerByApp(productID int) (map[string][]*mis.Banner, error)
func (lt *LTCacheData) GetAllTaskConfByApp(productID int) (map[int]*mis.TaskInfo, error)
func (lt *LTCacheData) GetKeepSigninByApp(productID int) (*mis.KeepSignin, error)
func (lt *LTCacheData) GetSingleTaskConfByApp(productID int, taskID int) (*mis.TaskInfo, error)
func (lt *LTCacheData) GetWithdrawByApp(productID int) (*mis.WithdrawConf, error)
func (lt *LTCacheData) GetPaymentTaskByApp(productID int) (*mis.PaymentTask, error)
// ...
```