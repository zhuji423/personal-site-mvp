---
title: "Redis 列表功能 Zulu 规则"
description: "一种基类抽取并业务发散的实践——redis列表服务实现"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\一种基类抽取并业务发散的实践——redis列表服务实现.md"
---
一种基类抽取并业务发散的实践——redis列表服务实现

#### 🧑‍🏫 案例作者：[@徐飞](https://ku.baidu-int.com?t=mention&mt=contact&id=bf5dc4c0-fce1-11f0-9112-bfb6f8aaa757)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了通过提炼基类并业务发散实现Redis列表服务的实践经验。首先总结实现Redis列表服务的步骤，抽象出通用列表服务基类，涵盖添加、查询、删除等核心功能。然后，基于基类制定rules，指导业务代码生成，确保业务实现遵循统一规范和最佳实践。此方法提高了代码复用性，降低了维护成本，展示了基类抽取与业务发散实践的价值。
### 背景与目标
业务场景中存在较多可以通用的基础数据结构或者代码流程（如代码重构、lib库建设等）

我们可以从中提取一种方法：提取基类并形成发散的业务实现



### 问题分析与解决流程
我们可以完全依赖模型能力，提炼基础服务，再以基础服务为基类，发散为各种业务实现

首先我们通过一个线上redis列表场景，让zulu帮我们总结实现一个列表服务需要的步骤

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bd118ff2fe3b4398bfadee993ad77d3b&docGuid=kShGHF9deaZDmV "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a44096a3e5964e2ebc847a5faf6d88c1&docGuid=kShGHF9deaZDmV "")


然后让zulu根据其总结出来的步骤，抽象出一个通用列表服务的实现

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=35e9062d3b7d4245a44ea3c5d0b3ef4a&docGuid=kShGHF9deaZDmV "")


```
// Package redis 提供通用的Redis列表服务实现
package redis

import (
    "context"
    "fmt"
    "time"

    "github.com/go-redis/redis/v8"
    "icode.baidu.com/baidu/wenku-go/ghome/library/resource"
    "icode.baidu.com/baidu/wenku-go/golib/wkerror"
)

// ListConfig 列表服务配置
type ListConfig struct {
    KeyPrefix   string        // Redis键前缀
    MaxSize     int64         // 列表最大容量
    DefaultSize uint          // 默认列表大小
    ExpireTime  time.Duration // 过期时间
}

// ListService Redis列表服务接口
type ListService interface {
    // Add 添加元素到列表
    Add(ctx context.Context, keySuffix interface{}, member interface{}) error
    // GetList 获取列表
    GetList(ctx context.Context, keySuffix interface{}, rn uint, offset int) ([]redis.Z, error)
    // GetListByRange 按范围获取列表
    GetListByRange(ctx context.Context, keySuffix interface{}, minScore, maxScore string) ([]redis.Z, error)
    // Remove 从列表中移除元素
    Remove(ctx context.Context, keySuffix interface{}, member interface{}) error
    // GetCount 获取列表元素数量
    GetCount(ctx context.Context, keySuffix interface{}) (int64, error)
    // Clear 清空列表
    Clear(ctx context.Context, keySuffix interface{}) (int64, error)
}

// GenericListService 通用的Redis列表服务实现
type GenericListService struct {
    config ListConfig
}

// NewGenericListService 创建新的通用列表服务
func NewGenericListService(config ListConfig) *GenericListService {
    return &GenericListService{
        config: config,
    }
}

// buildKey 构建Redis键
func (s *GenericListService) buildKey(keySuffix interface{}) string {
    switch v := keySuffix.(type) {
    case uint64:
        return fmt.Sprintf(s.config.KeyPrefix, v)
    case int:
        return fmt.Sprintf(s.config.KeyPrefix, v)
    case string:
        return fmt.Sprintf("%s%s", s.config.KeyPrefix, v)
    default:
        return s.config.KeyPrefix
    }
}

// Add 添加元素到列表
func (s *GenericListService) Add(ctx context.Context, keySuffix interface{}, member interface{}) error {
    key := s.buildKey(keySuffix)

    zc := resource.Redis().CacheTags.ZAdd(ctx, key, &redis.Z{
        Score:  float64(time.Now().Unix()),
        Member: member,
    })
    if zc.Err() != nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZAdd[%s] failed, err: %+v", key, zc.Err()))
        return wkerror.New(wkerror.ErrorCodeInternalError, "zadd redis error")
    }

    _, err := zc.Result()
    if err != nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZAdd[%s] failed, err: %+v", key, err))
        return wkerror.New(wkerror.ErrorCodeInternalError, "zadd redis error")
    }

    // 设置过期时间
    if s.config.ExpireTime > 0 {
        resource.Redis().CacheTags.Expire(ctx, key, s.config.ExpireTime*time.Second)
    }

    // 维护列表大小
    if s.config.MaxSize > 0 {
        s.maintainSize(ctx, key)
    }

    return nil
}

// maintainSize 维护列表大小
func (s *GenericListService) maintainSize(ctx context.Context, key string) {
    zc := resource.Redis().CacheTags.ZCard(ctx, key)
    zcnt, err := zc.Result()
    if err != nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZCard[%s] failed, err: %+v", key, err))
        return
    }

    if zcnt > s.config.MaxSize {
        resource.Redis().CacheTags.ZRemRangeByRank(ctx, key, 0, zcnt-s.config.MaxSize-1)
    }
}

// GetList 获取列表
func (s *GenericListService) GetList(ctx context.Context, keySuffix interface{}, rn uint, offset int) ([]redis.Z, error) {
    if rn == 0 {
        rn = uint(s.config.DefaultSize)
    }

    key := s.buildKey(keySuffix)
    param := &redis.ZRangeBy{
        Offset: int64(offset),
        Count:  int64(rn),
        Min:    "(1.1",
        Max:    "+INF",
    }

    zc := resource.Redis().CacheTags.ZRevRangeByScoreWithScores(ctx, key, param)
    if zc.Err() != nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZRevRangeByScoreWithScores[%s] failed, err: %+v", key, zc.Err()))
        return nil, wkerror.New(wkerror.ErrorCodeInternalError, "get redis error")
    }

    z, err := zc.Result()
    if err != nil || z == nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZRevRangeByScoreWithScores[%s] failed, err: %+v", key, err))
        return nil, wkerror.New(wkerror.ErrorCodeInternalError, "get redis error")
    }

    return z, nil
}

// GetListByRange 按范围获取列表
func (s *GenericListService) GetListByRange(ctx context.Context, keySuffix interface{}, minScore, maxScore string) ([]redis.Z, error) {
    key := s.buildKey(keySuffix)
    param := &redis.ZRangeBy{
        Offset: 0,
        Count:  int64(s.config.DefaultSize),
        Min:    minScore,
        Max:    maxScore,
    }

    zc := resource.Redis().CacheTags.ZRevRangeByScoreWithScores(ctx, key, param)
    if zc.Err() != nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZRevRangeByScoreWithScores[%s] failed, err: %+v", key, zc.Err()))
        return nil, wkerror.New(wkerror.ErrorCodeInternalError, "get redis error")
    }

    z, err := zc.Result()
    if err != nil || z == nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZRevRangeByScoreWithScores[%s] failed, err: %+v", key, err))
        return nil, wkerror.New(wkerror.ErrorCodeInternalError, "get redis error")
    }

    return z, nil
}

// Remove 从列表中移除元素
func (s *GenericListService) Remove(ctx context.Context, keySuffix interface{}, member interface{}) error {
    key := s.buildKey(keySuffix)
    _, err := resource.Redis().CacheTags.ZRem(ctx, key, member).Result()
    if err != nil {
        // 重试一次
        _, err = resource.Redis().CacheTags.ZRem(ctx, key, member).Result()
        if err != nil {
            resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZRem[%s] failed, err: %+v", key, err))
            return wkerror.New(wkerror.ErrorCodeInternalError, "remove redis error")
        }
    }
    return nil
}

// GetCount 获取列表元素数量
func (s *GenericListService) GetCount(ctx context.Context, keySuffix interface{}) (int64, error) {
    key := s.buildKey(keySuffix)
    zc := resource.Redis().CacheTags.ZCard(ctx, key)
    count, err := zc.Result()
    if err != nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis ZCard[%s] failed, err: %+v", key, err))
        return 0, err
    }
    return count, nil
}

// Clear 清空列表
func (s *GenericListService) Clear(ctx context.Context, keySuffix interface{}) (int64, error) {
    key := s.buildKey(keySuffix)
    zc := resource.Redis().CacheTags.Del(ctx, key)
    result, err := zc.Result()
    if err != nil {
        resource.LoggerService().Warning(ctx, fmt.Sprintf("redis Del[%s] failed, err: %+v", key, err))
        return 0, err
    }
    return result, nil
}

```


最后，让zulu根据其生成的基类，产出rules，用于业务代码生成

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e3c1e8caa87f4560bc16db764a3e7dc1&docGuid=kShGHF9deaZDmV "")


```
---
description: 
globs: 
alwaysApply: false
---

# Redis 列表功能 Zulu 规则

## 参考基类
1. 以`library/redis/list_service.go`为基类实现实际业务列表服务
2. 继承基类的ListConfig
3. 可以适当扩展业务字段

## 配置规则
1. **前缀配置**：所有 Redis 列表键必须使用统一前缀，通过 `ListConfig.KeyPrefix` 配置
2. **容量控制**：必须设置 `ListConfig.MaxSize` 防止列表无限增长
3. **默认大小**：必须设置 `ListConfig.DefaultSize` 作为默认查询大小
4. **过期时间**：必须设置 `ListConfig.ExpireTime` 防止数据堆积

## 接口规范
1. **接口定义**：必须实现 `ListService` 接口的 6 个方法：
   - `Add`
   - `GetList` 
   - `GetListByRange`
   - `Remove`
   - `GetCount`
   - `Clear`

2. **错误处理**：
   - 所有 Redis 操作错误必须记录日志
   - 必须返回 `wkerror` 类型的错误
   - 关键操作(如 Remove)应实现重试机制

## 实现规范
1. **键构建**：
   - 必须支持多种 keySuffix 类型(uint64/int/string)
   - 必须使用 `fmt.Sprintf` 构建完整键名

2. **添加元素**：
   ```go
   func (s *GenericListService) Add(ctx context.Context, keySuffix interface{}, member interface{}) error {
       // 必须包含以下步骤：
       // 1. 构建完整键名
       // 2. 使用 ZAdd 添加元素
       // 3. 设置过期时间(如果配置)
       // 4. 维护列表大小(如果配置MaxSize)
   }

3. **查询列表**
   ```go
   func (s *GenericListService) GetList(ctx context.Context, keySuffix interface{}, rn uint, offset int) ([]redis.Z, error) {
        // 必须：
        // 1. 处理默认大小
        // 2. 使用 ZRevRangeByScoreWithScores 获取有序列表
        // 3. 处理错误情况
    }
   ```

4. 实现 `maintainSize` 方法控制列表大小

5. 使用 `ZRemRangeByRank` 修剪超限列表

```


接下来（rules还是经过了些许测试和调整），基于规则，让zulu直接生成具体的代码

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=742827449d3c4f5b986febddacbb9d63&docGuid=kShGHF9deaZDmV "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
