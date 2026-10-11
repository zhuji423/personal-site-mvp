---
title: "redis"
description: "import \"context\" \"fmt\" \"icode.baidu.com/baidu/gdp/redis\" \"icode.baidu.com/baidu/searchbox/sbox-basic/library/errno\" \"ico"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_basic\\depend\\redis.md"
---
### redis包
#### 新增redis方法配置，文件路径：`model/dao/redis/service.go`
* 此文件仅需生成追加内容即可，不要导包，示例如下：
```go
type Redis interface {
	TestRedisFunc(ctx context.Context, testKey string) error 	// 新增redis方法配置
}
```
#### 新增redis方法底层逻辑代码，文件路径：`model/dao/redis/test_ral.go`
```go
package redis

import (
	"context"
	"fmt"
	"icode.baidu.com/baidu/gdp/redis"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/errno"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/resource"
)

// redis相关常量配置
const (
    // TestRedisKey ...
    TestRedisPrefix = "test_redis_prefix_"
)


// redis方法实现，示例如下：
// TestRedisFunc ...
func (s *service) TestRedisFunc(ctx context.Context, testKey string) error {
    key = s.getRedisKey(testKey)
    result, err := resource.RedisClient.Get(ctx, testKey).Result()
	if err != nil {
		if err == redis.ErrNil {
			return "", nil
		}
		logger.WarningF(ctx, "failed to xxx for [%s] ", err)
		return "", err
	}
	return result, nil   
}

// 获取redis key，示例如下：
func (s *service) getRedisKey(testKey string) string {
	return fmt.Sprintf("%s:%s", TestRedisKey, testKey)
}
```