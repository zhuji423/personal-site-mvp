---
title: "data"
description: "import \"icode.baidu.com/baidu/gdp/gormadapter\" \"icode.baidu.com/baidu/gdp/redis\" \"icode.baidu.com/baidu/searchbox/ugact/"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\data.md"
---
### data层根目录路径：`service/包名/data/功能名/`
#### data构造函数定义，文件路径：`service/包名/data/功能名/constructor.go`
* 注意此文件无需生成注释
```go
package 功能名

import (
    "icode.baidu.com/baidu/gdp/gorm_adapter"
    "icode.baidu.com/baidu/gdp/redis"
    "icode.baidu.com/baidu/searchbox/ugact/library/resource"
)

type (
    service struct {
        // 涉及mysql和redis，则定义对象
        redisClient redis.Client
        mysqlClient *gorm_adapter.GormDB
    }

    Option interface {
        apply(*service)
    }

    optionFn func(*service)
)

// apply 函数接受一个optionFn类型参数，并将其应用于指定的服务对象s。
func (fn optionFn) apply(s *service) {
    fn(s)
}

// defaultOpt 返回一个默认的 Option 对象，用于初始化服务对象
// 默认的 Option 使用 Redis 和 MySQL 的资源以及 进行初始化
func defaultOpt() Option {
    return optionFn(func(s *service) {
        // 涉及mysql和redis，需要根据resource层定义的对象进行初始化，其中`Test`对应指定包名
        s.redisClient = resource.RedisClientTest
        s.mysqlClient = resource.OrmClientTest
    })
}

// NewTestData 函数返回一个新的实例，可以设置一些选项
func NewTestData(opts ...Option) I包名Data {
    s := &service{}
    defaultOpt().apply(s)
    for _, opt := range opts {
        opt.apply(s)
    }
    return s
}
```
#### data接口定义，文件路径：`service/包名/data/功能名/contract.go`
* 注意此文件无需生成注释
```go
package 功能名

import "context"

type I包名Data interface {
    TestSqlData(ctx context.Context, req *TestReq) (res *TestSqlData, err error) 
    TestHttpData(ctx context.Context) (res []TestHttpData, err error)
}
```
#### data数据获取逻辑实现，文件路径：`service/包名/data/功能名/test_file.go`
* 注意数据获取、处理等逻辑根据需求生成注释
```go
package 功能名

import (
    "context"
    "fmt"
    
    "icode.baidu.com/baidu/searchbox/ugact/library/errno"
    "icode.baidu.com/baidu/searchbox/ugact/library/logger"
    "icode.baidu.com/baidu/searchbox/ugact/library/constant"
    "icode.baidu.com/baidu/searchbox/ugact/service/包名/types"
    "icode.baidu.com/baidu/baidu/searchbox/ugact/service/包名/data/功能名"
    
    // 若涉及到从新增的下游http接口获取数据，需要导入对应的包，test_pkg根据需求描述获取的数据类型进行命名
    "icode.baidu.com/baidu/searchbox/ugact/repository/test_pkg"
)
    

// 涉及mysql数据获取，根据需求解析sql语句，调用已经初始化的mysqlClient对象进行数据获取，示例如下：
// TestSqlData ...
func (s *service) TestSqlData(ctx context.Context, req *types.TestReq) (*TestSqlData, error) {
    testSqlData := new(TestSqlData) 
    if err := s.mysqlClient.WithContext(ctx).
        Where("test_id = ? ", req.testID).
       Find(&testSqlData).Error; err != nil {
        logger.WarningF(ctx, "error message err: +%v", err)
        return nil, err
    }
}
    
// 若涉及到redis数据获取，调用已经初始化的redisClient对象进行数据获取，示例如下：
// TestRedisData ...
func (s *service) TestRedisData(ctx context.Context, req *types.TestReq) (*TestRedisData, error) {
    testRedisData, err := s.redisClient.Get(ctx, testID).Result()
    if err == nil {
        logger.WarningF(ctx, "error message err: +%v", err)
        return testRedisData, nil 
    }
    return testRedisData, err
}

// 若涉及到从下游http接口获取数据，需要调用对应的下游接口方法获取数据，示例如下：
// TestHttpData ...
func (s *service) TestHttpData(ctx context.Context) ([]TestFmtHttpData, error) {
    testFmtHttpDataLst := make([]TestFmtHttpData, 0, 5)
    testHttpDataLst, err := test_pkg.TestGetHttpData(ctx)
    if err != nil {
        logger.WarningF(ctx, "error message: +%v", err)
        return nil, err
    }
    return testFmtHttpDataLst, nil
}
```