---
title: "service"
description: "import \"context\" \"net/http\" \"net/url\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\haokan_ui\\haokan-ad\\service.md"
---
## ral写法示例
### 逻辑放在services层
```go
// 获取所有榜单
package services

import (
	"context"
	"net/http"
	"net/url"

	"icode.baidu.com/baidu/gdp/codec"
	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/go-hulk/hulk/component/ral"
	"icode.baidu.com/baidu/go-hulk/hulk/gdp_wrapper/logit"
	"icode.baidu.com/baidu/haokan-go/hklib/common/ctx_util"
	"icode.baidu.com/baidu/haokan-go/ui-video/bootstrap/hk_logger"
	"icode.baidu.com/baidu/haokan-go/ui-video/models/response"
)

func GetTestInfo(ctx context.Context) ([]*response.TestInfoData, error) {
	ralReq := &ghttp.RalRequest{
		Method: http.MethodGet,
		Path:   "test/info",
	}
	// 临时兼容
	var resp *response.TestInfoData
	ralResp := &ghttp.RalResponse{
		Data:    &resp,
		Decoder: codec.JSONDecoder,
	}
	err := ral.RAL(ctx, "baidu_test_info", ralReq, ralResp)
	if err != nil {
		hk_logger.Logger.Error(ctx, "GetTestInfo error", logit.String("err", err.Error()), logit.AutoField("resp", resp))
		return nil, ctx_util.ERR_NO_RAL_CALL_FAIL
	}
	if resp.ErrNo != 0 {
		hk_logger.Logger.Error(ctx, "GetTestInfo response error", logit.String("err", resp.Msg), logit.AutoField("resp", resp))
		return nil, ctx_util.ERR_NO_RAL_DATA_ERROR
	}
	hk_logger.Logger.Notice(ctx, "GetTestInfo response", logit.AutoField("resp", resp))

	return resp.Data, nil
}
```

### GetTestInfo对应的ral配置文件如下，文件路径：conf/ral/services/baidu_test_info.toml
```toml
Name = "baidu_test_info"
ConnTimeOut = 150
WriteTimeOut = 300
ReadTimeOut = 300
Retry = 1
Protocol = "http" # http / https / nshead
Reuse = true

[Strategy]
Name="LocalityAware"

[Resource.BNS]
BNSName        = "group.bdapp-feedhot-online.searchbox.all"
EnableSmartBNS = true # 可选参数
```

## mysql写法示例。逻辑放在services层
```go
package services

import (
	"golang.org/x/net/context"
	"gorm.io/gorm/clause"
	"icode.baidu.com/baidu/go-hulk/hulk/gdp_wrapper/logit"
	"icode.baidu.com/baidu/haokan-go/ui-video/bootstrap/dao"
	"icode.baidu.com/baidu/haokan-go/ui-video/bootstrap/hk_logger"
	"icode.baidu.com/baidu/haokan-go/ui-video/models/do"
	"icode.baidu.com/baidu/haokan-go/ui-video/models/request"
	"time"
)

// 新增短剧气泡数据
func AddPlayletBubble(ctx context.Context, param request.PlayletBubbleReq) error {

	var objInsert = do.PlayletBubbleInfo{
		VideoID:    param.VideoID,
		PlayletID:  param.PlayletID,
		Title:      param.Title,
		CreateTime: time.Now().Unix(),
		UpdateTime: time.Now().Unix(),
	}

	// 不存在则新增，存在则更新
	err := dao.MysqlPlaylet.Clauses(clause.OnConflict{
		Columns:   []clause.Column{{Name: "video_id"}},
		DoUpdates: clause.AssignmentColumns([]string{"title", "update_time"}),
	}).Create(&objInsert).Error

	if err != nil {
		hk_logger.Logger.Error(ctx, "add playlet bubble error", logit.Error("err", err))
		return err
	}

	return nil
}

func GetTitleByVid(ctx context.Context, vid string) string {
	var rsp do.PlayletBubbleInfo
	err := dao.MysqlPlaylet.Model(&do.PlayletBubbleInfo{}).Where("video_id = ?", vid).Take(&rsp).Error
	if err != nil {
		hk_logger.Logger.Error(ctx, "get playlet bubble error", logit.Error("err", err))
		return ""
	}

	return rsp.Title
}



```

### mysql客户端初始化，文件路径：bootstrap/dao/mysql.go
```go
package dao

import (
	"icode.baidu.com/baidu/go-hulk/hulk/component/client/mysql"
)

var MysqlHotPoint *mysql.GormDB
var MysqlPlaylet *mysql.GormDB
var MysqlSeries *mysql.GormDB

func InitDbClient() {
	MysqlPlaylet = mysql.InitGormMysqlClient("mysql_playlet")
	MysqlSeries = mysql.InitGormMysqlClient("mysql_series")
}

func InitTaskDbClient() {
	MysqlHotPoint = mysql.InitGormMysqlClient("mysql_hotpoint")
	MysqlPlaylet = mysql.InitGormMysqlClient("mysql_playlet")
}

```


## redis写法示例。逻辑放在services层

### redis客户端初始化，文件路径：bootstrap/dao/redis.go
``` go
package client

import (
	"context"

	"icode.baidu.com/baidu/go-hulk/hulk"
	"icode.baidu.com/baidu/go-hulk/hulk/gdp_wrapper/redis"
	"icode.baidu.com/baidu/haokan-go/hklib/client/redisha"
)

var (
	// redis db client
	RedisDB redis.Client
	// redis cache read write client
	RedisCacheReadWrite redis.Client
	// redis cache delete clients
	RedisCacheDeletes []redis.Client
	// redis cache IDCs
	RedisCacheIDCs = []string{"bj", "gz", "sz", "nj"}
)

// InitRedisClient
func InitRedisClient(ctx context.Context) {
	// 初始化 redis db(haokanapi) client
	RedisDB = redisha.InitDefaultClient(ctx)
	// 初始化 redis cache clients
	RedisCacheReadWrite = hulk.InitRedisClient("redis_haokancache")
	RedisCacheDeletes = make([]redis.Client, len(RedisCacheIDCs))
	for i, idc := range RedisCacheIDCs {
		RedisCacheDeletes[i] = hulk.InitRedisClient("redis_haokancache_" + idc)
	}
}
```

### redis读写示例，文件路径：services/collection_service.go
```go
func getLatestPlayLetFromRedis(ctx context.Context, key string) []string {
	playletIDList := []string{}
	now := time.Now().Unix()
	start := time.Now().AddDate(0, 0, -7).Unix()
	zs, err := dao.RedisHaokanPlayletSeries.ZRevRangeByScoreWithScores(ctx, key, &redis.ZRangeBy{
		Min: strconv.FormatInt(start, 10),
		Max: strconv.FormatInt(now, 10)}).Result()
	if err != nil {
		hk_logger.Logger.Warning(ctx, "get playlet collection from redis error",
			logit.AutoField("key", key), logit.AutoField("error", err))
		return playletIDList
	}
	for _, member := range zs {
		if playletID, ok := member.Member.(string); ok {
			playletIDList = append(playletIDList, playletID)
		}
	}
	return playletIDList
}
```

## iconf写法示例。逻辑放在services层
### iconf services逻辑示例，文件路径：
```go
import (
	"context"
	"encoding/json"
	"fmt"
	"strconv"
	"time"

	"icode.baidu.com/baidu/go-hulk/hulk/component/iconf_client"
	"icode.baidu.com/baidu/go-hulk/hulk/gdp_wrapper/logit"
	"icode.baidu.com/baidu/go-hulk/hulk/gdp_wrapper/redis"
	"icode.baidu.com/baidu/haokan-go/hklib/component"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils"
)
// 是否短剧货架活动期间
func IsPlayletShelfActivity(ctx context.Context) bool {
	var beginTime, endTime int64
	activityDateMap := map[string]int64{}
	activityDate := iconf_client.GetStringValueWithAppGroup("hklib_config", "playlet_activity_time", "{}")
	if err := json.Unmarshal([]byte(activityDate), &activityDateMap); err == nil {
		beginTime, _ = activityDateMap["begin_time"]
		endTime, _ = activityDateMap["end_time"]
	}
	nowUnix := time.Now().Unix()
	return nowUnix >= beginTime && nowUnix <= endTime
}
```