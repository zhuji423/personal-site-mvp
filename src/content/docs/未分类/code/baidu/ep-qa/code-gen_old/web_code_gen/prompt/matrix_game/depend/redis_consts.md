---
title: "redis_consts"
description: "const // TestRedisKey ... TestRedisKey = testPrefix + \"rediskey\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_game\\depend\\redis_consts.md"
---
### redis常量定义
* redis常量定义分为两部分，第一部分为前缀常量定义，第二部分为逻辑相关常量定义
#### redis前缀常量定义，文件路径：`model/consts/redis/模块包占位/base.go`
* 此文件仅生成以下追加内容即可，不要导包，示例如下：
```go
testPrefix = basePrefix + "test_"  // 新接口前缀，`test`对应包名
```
#### redis逻辑相关常量定义，文件路径：`model/consts/redis/模块包占位/包名.go`
* 此文件必须生成注释
```go
package redis

const (
    // TestRedisKey ...
    TestRedisKey = testPrefix + "redis_key"
)
```