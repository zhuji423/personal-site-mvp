---
title: "redis"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\redis.md"
---
### redis相关逻辑&配置
#### redis常用的封装好方法使用参考，存放路径：`library/store/redis/redis.go`（无需生成，仅供参考）
```go
func (r *IRedis) Get(key string) (string, error)
func (r *IRedis) Del(key string) redis.IntCmder
func (r *IRedis) Set(key string, val interface{}, ttl ...time.Duration) (string, error)
func (r *IRedis) Exists(keys ...string) (num int64, err error)
func (r *IRedis) Expire(key string, ttl time.Duration) redis.BoolCmder
func (r *IRedis) SetNX(key string, val interface{}, ttl ...time.Duration) redis.BoolCmder 
func (r *IRedis) HSet(key, field string, value interface{}) (int64, error)
func (r *IRedis) HDel(key string, fields ...string) redis.IntCmder 
func (r *IRedis) HGetAll(key string) redis.StringStringMapCmder
// ...
```
#### redis常量key配置文件，文件路径：`model/data/consts/duoduo_redis_key.go`
* 此文件必须生成一对一对应注释
* 此文件仅需生成追加内容即可，不要导包，示例如下：
```go
RedisKeyTestFunc = "ddv:test:func:%v:%v" // 测试接口redis key
```