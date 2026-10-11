---
title: "resource"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\depend\\resource.md"
---
### 数据操作对象定义代码，文件路径：`library/resource/resource.go`
* 此文件生成追加内容即可，不要导包，示例如下：
```go
// 默认DB操作对象`UGGameCenterDB`已定义，若指定其他DB操作对象，则需要在此处定义，示例如下：
var TestNewDB *gorm_adapter.GormDB
// 默认Redis操作对象`RedisComClient`已定义，若指定其他Redis操作对象，则需要在此处定义，示例如下：
var TestNewRedis redis.Client
// 默认GCP操作对象`GcpCommonCf`已定义，若指定其他GCP操作对象，则需要在此处定义，示例如下：
var TestNewGcpConf *gcp.AppConfig
```