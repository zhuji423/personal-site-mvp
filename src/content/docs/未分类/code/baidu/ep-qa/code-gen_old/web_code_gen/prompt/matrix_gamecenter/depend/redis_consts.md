---
title: "redis_consts"
description: "const // TestRedisKey 测试接口redis key配置 TestRedisKey = testPrefix + \"rediskey\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\depend\\redis_consts.md"
---
### redis常量定义
* redis常量需要生成两部分，第一部分是前缀关键词定义，第二部分是结合前缀常量的redis逻辑常量定义
#### redis常量前缀关键词定义，文件路径：`model/consts/redis/base.go`
* 此文件追加生成以下内容即可，不要导包，示例如下：
```go
testPrefix = basePrefix + "test_"  // 新接口前缀，`test`对应包名
```
#### 结合前缀常量的redis逻辑常量定义，文件路径：`model/consts/redis/包名.go`
```go
package redis

const (
    // TestRedisKey 测试接口redis key配置
    TestRedisKey = testPrefix + "redis_key" 
)
```