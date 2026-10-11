---
title: "redis"
description: "import \"context\" \"errors\" \"fmt\" \"time\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_game\\depend\\redis.md"
---
#### redis缓存数据底层操代码，文件路径：`model/dao/redis/模块包占位/接口路径占位/功能名_test_redis.go`
```go
package 包名or子包名

import (
    "context"
	"errors"
	"fmt"
	"time"

	"icode.baidu.com/baidu/gdp/redis"
	params "icode.baidu.com/baidu/searchbox/symframe-param"
	
    "icode.baidu.com/baidu/searchbox/ug-game/library/errno"
	"icode.baidu.com/baidu/searchbox/ug-game/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-game/library/resource"
	redisConsts "icode.baidu.com/baidu/searchbox/ug-game/model/consts/redis/模块包占位"
)

// TestRedis ...
type TestRedis struct {
	TestRedisData string `json:"test_redis_data" form:"test_redis_data"`  // 测试数据
}

// 获取key
func (t *TestRedis) getKey() string {
    adapt, _ := symframe.LoadAdaption(ctx)
	return fmt.Sprintf(redisConsts.TestRedisKey, adapt.AppName())
}

// redis数据操作，示例如下：
// TestRedisFunc ...
func (t *TestRedis) TestRedisFunc(ctx context.Context) (*TestRedis, error) {
    key := m.key()
    info, err := resource.RedisComClient.Get(ctx, key).Result()
	   if err != nil {
		   logger.ErrWF(ctx, errno.RedisExecuteError, "xxx get err=%v", err)
		   return nil, err
	   }
    data := &TestRedis{}
    err = utils.JSONDecompressZLibB64(info, data)
	   if err != nil {
		   logger.ErrWF(ctx, errno.DecompressDataError,
			   "xxx JSONDecompressZLibB64 error, key=%s, val=%v, err=%v", key, info, err)
		   return nil, err
	   }
    
    return data, nil
}
```