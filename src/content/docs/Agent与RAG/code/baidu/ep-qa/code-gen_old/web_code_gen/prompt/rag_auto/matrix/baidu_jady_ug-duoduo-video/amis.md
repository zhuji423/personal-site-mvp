---
title: "amis"
description: "// TestRegularConf 新增常规页面结构体定义 type TestRegularConf struct { TestPageId string json:\"testPageId\" // 测试页面ID } （2）新增常规amis"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\matrix\\baidu_jady_ug-duoduo-video\\amis.md"
---
## 涉及到amis爱速搭数据操作时，需按以下步骤实现：
1. 判断是`实验页面`还是`常规页面`;
2. 根据页面类型参考示例生成对应代码：
### 实验页面
（1） 新增amis实验页面配置，新增实验配置默认为`*SampleData`类型，带关键词`Test`的页面命名根据需求描述生成，**仅生成配置语句即可**，示例如下：
* 文件名：`library/mis/struct_smaple.go`
```go
TestExperiment  *SampleData   `json:"newTestExperiment"`  // 新增实验页面
```
（2）新增amis实验数据加载逻辑代码，带关键词`Test`的函数命名根据需求描述生成，**仅生成命中函数即可**，示例如下：
* 文件名：`model/data/sample/sample.go`
```go
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
	// 注意区分黑名单、白名单配置的参数传递顺序，从需求解析并参照对应示例进行配置，此处仅为示例说明：
	// 白名单配置（默认配置），示例如下：
	isHit := sidCommon.IsShowTaskBySID("", config.TestExperiment.Sids)
	// 黑名单配置，示例如下：
	// isHit := sidCommon.IsShowTaskBySID(config.TestExperiment.Sids, "")
	//命中反转
	if !isHit {
		logit.AddNotice(usd.ctx, logit.String("t_e-hit", "1"))
		return false
	}
	logit.AddNotice(usd.ctx, logit.String("t_e-un-hit", "1"))
	return true
}
```
### 常规页面
（1）新增常规amis页面结构体定义，带关键词`test`的命名根据需求描述生成，示例如下：
* 文件名：`library/mis/struct_test_mis.go`
```go
package mis

// TestRegularConf 新增常规页面结构体定义
type TestRegularConf struct {
    TestPageId string `json:"testPageId"`  // 测试页面ID
}
```
（2）新增常规amis页面配置，带关键词`test`的命名根据需求描述生成，**仅生成配置语句即可**，示例如下：
* 文件名：`library/mis/struct.go`
```go
TestRegularConf *TestRegularConf `json:"testRegularConf"`  // 新增常规页面
```
（3）新增常规amis页面脚手架逻辑代码，带关键词`test/Test`的命名根据需求描述生成，示例如下：
* 文件名：`components/miscache/loader.go`
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
（4）新增常规页面amis相关常量配置，带关键词`test`的命名根据需求描述生成，**仅生成配置语句即可**，示例如下：
* 文件名：`library/mis/consts.go`
```go
TestGroupRegularConf = "regular_conf_"  // 新增常规页面分组前缀
```