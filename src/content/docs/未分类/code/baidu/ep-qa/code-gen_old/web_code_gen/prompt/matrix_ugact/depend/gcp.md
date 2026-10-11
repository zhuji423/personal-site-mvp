---
title: "gcp"
description: "// GetSwitch 获取GCP开关， 当GCP查询失败或者GCP未配置数据时，返回 defaultValue 作为默认开关值 func GetSwitchctx context.Context, appID, key string, "
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\gcp.md"
---
#### gcp相关代码&逻辑
##### gcp常量配置，文件路径：`library/constant/gcp.go`
* 此文件生成追加内容即可，不要导包，示例如下：
```go
testGcpAppId  = "xxxxx"
testGcpKey    = "xxxxx"
```
##### gcp相关函数已经封装到 `library/gcp`包中，在service层直接调用相关函数即可，调用参考：
```go
// Fetch 获取单条数据， T 为GCP配置的结构体
func Fetch[T any](ctx context.Context, appID, key string) (T, error) {}
// FetchExtend 支持添加自定义参数获取， T 为GCP配置的结构体
func FetchExtend[T any](ctx context.Context, appID, key string, extParam map[string]any) (T, error) {}
// MultiFetch 获取GCP数据(获取多条数据)， T 为GCP配置的结构体
func MultiFetch[T any](ctx context.Context, appID, key string) ([]T, error) {}

// GetSwitch 获取GCP开关， 当GCP查询失败或者GCP未配置数据时，返回 defaultValue 作为默认开关值
func GetSwitch(ctx context.Context, appID, key string, defaultValue bool) (bool, error) {}
// GetSwitchValue 获取命中的实验组
func GetSwitchValue(ctx context.Context, appID, key string, defaultValue int) (int, error) {}
```