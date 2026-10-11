---
title: "mis_experiment"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\mis_experiment.md"
---
### amis相关底层逻辑代码&配置（关键词：`mis`、`amis`、`爱速搭`）
* 方法、结构体、变量命名遇到缩写词时注意全大写，如：`QRCode`中`QR`为缩写词，则全大写为`QRCode`
#### 新增amis实验页面配置，文件路径：`library/mis/struct_smaple.go`
* 新增实验配置默认为`*SampleData`类型，页面命名优先需求描述解析命名
* 此文件仅需追加生成内容即可，不要导包，示例如下：
```go
type SampleConf struct {
    TestExperiment  *SampleData   `json:"newTestExperiment"`  // 新增实验页面
}
```
#### 新增amis实验数据加载逻辑代码，文件路径：`model/data/sample/sample.go`
* 此文件仅需追加生成内容即可，不要导包，示例如下：
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