---
title: "resource"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\resource.md"
---
#### data层数据操作对象需在对应文件新增配置，文件路径：`library/resource/resource.go`
* 此文件追加生成以下内容即可，不要导包，示例如下：
```go
// 定义数据库连接对象示例，其中`Test`对应指定包名
MySQLClientTest mysql.Client
OrmClientTest   *gorm_adapter.GormDB
RedisTest       redis.Client
```