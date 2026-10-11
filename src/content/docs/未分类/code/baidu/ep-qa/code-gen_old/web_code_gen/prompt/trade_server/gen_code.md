---
title: "gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码："
description: "你是一个go语言开发工程师，你需要基于gdp框架，采用MVC模式，深入解析需求描述的内容，按步骤生成对应完整的逻辑代码： {{requirement}}"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\trade_server\\gen_code.md"
---
你是一个go语言开发工程师，你需要基于gdp框架，采用MVC模式，深入解析需求描述的内容，按步骤生成对应完整的逻辑代码：
{{requirement}}

# gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码：
## router层的代码，文件路径：`httpserver/router.go`
* 此文件不生成任何注释
```go
import (
    "icode.baidu.com/baidu/searchbox/tradeserver/httpserver/controller/test_package"
    "icode.baidu.com/baidu/gdp/ghttp"
)

func registertest_package(router ghttp.Router) {
    // test_package为指定包名
    // - 若需求指定接口路径最后两个层级为`path1/path2`，则有router.Group("/path1")
    // - 如，需求指定接口路径为"api/check"，则有router.Group("/api")
    m := router.Group("/test_package")
    // - 若需求指定接口路径最后两个层级为`path1/path2`，指定函数名为TestFunc，则有router.HandleFunc("POST", "/path2", path1.TestFunc)
    // - 如，需求指定接口路径为"api/check"，指定函数名为CheckList，则有router.HandleFunc("POST", "/check", api.CheckList)
    m.HandleFunc("POST", "/test_file", test_package.TestFunc)
}
```
## controller层的代码，文件路径：`httpserver/controller/test_package/test_file.go`
* 该路径和router、service层均存在对应关系，需要根据需求描述来确定，示例如下：
- 若需求指定接口路径最后两个层级为`path1/path2`，则controller层代码存放路径为：`httpserver/controller/path1/path2.go`
- 如，需求指定接口路径为"api/check"，则controller层代码存放路径为：`httpserver/controller/api/check.go`
* 此文件不生成任何注释
* 示例代码如下：
```go
// test_package 需遵循上述对应关系
package test_package

import (
    "context"
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/searchbox/tradeserver/library/frame"
    "icode.baidu.com/baidu/searchbox/tradeserver/model/service/test_package"
)

func TestFunc(ctx context.Context, req ghttp.Request) ghttp.Response {
    // 注意：下述调用service层函数`&test_package.TestFunc`函数名需和当前controller层函数命名`TestFunc`需保持一致，不要重新命名！！！
    // 如，若需求指定接口路径为"api/check"，controller当前函数名为CheckList，则service层函数名也为CheckList，即：CheckList := &api.CheckList{}
    TestFunc := &test_package.TestFunc{}
    response := frame.NewDirector(ctx, req, TestFunc).BuildPage()
    return ghttp.NewJSONResponse(200, response)
}
```
## service层的代码
### 路径
* 代码存放，文件路径为`model/service/test_package/test_file.go`
该路径和router、controller层均存在对应关系，需要根据需求描述来确定，示例如下：
- 若需求指定接口路径最后两个层级为`path1/path2`，则service层代码存放路径为：`model/service/path1/path2.go`
- 如，需求指定接口路径为"api/check"，则service层代码存放路径为：`model/service/api/check.go`
### 逻辑实现
service层需要根据需求描述实现Execute()、PreCheck()函数
#### PreCheck()
根据需求，进行参数校验
#### Execute()
实现需求描述涉及的完整业务逻辑，要求如下：
* 若涉及redis数据获取，需要遵守以下规则：
1. 从需求描述中获取redis对象，默认对象名`RedisMsgLogic`
2. 对redis的操作，通过`.Result() (any, error)`获取结果
* 若涉及mysql数据获取，调用dao层表的定义的数据操作对象，实现数据库数据获取操作
### 示例
根据需求描述完整实现业务逻辑代码，不要简写省略，其中，关于参数校验的逻辑实现在PreCheck函数中即可
* 示例代码如下：
```go
import (
    "fmt"
    
    "icode.baidu.com/baidu/gdp/extension/gerror"
	"icode.baidu.com/baidu/searchbox/tradeserver/library/frame"
	"icode.baidu.com/baidu/searchbox/tradeserver/library/log"
	"icode.baidu.com/baidu/searchbox/tradeserver/library/pre"
	"icode.baidu.com/baidu/searchbox/tradeserver/library/resource"
	"icode.baidu.com/baidu/searchbox/tradeserver/library/types"
	"icode.baidu.com/baidu/searchbox/tradeserver/model/dao"
)

// 注意：service层函数`TestFunc`需和router、controller层关联函数命名保持一致，不要重新命名！！！
// 如，若指定函数名为CheckList，则service层函数名也为CheckList，和controller层函数名保持一致，也和router层调用函数名保持一致
type TestFunc struct {
    frame.SampleBuilder
    request *TestFuncReq
    TestInfo *dao.TestInfo
}

// 常量定义
const (
    TestRedisKey = "test_redis_key"  // redis key
)

// TestFuncReq 请求体
type TestFuncReq struct {
    TestID int `json:"testId" form:"testId" binding:"required"`  // 测试ID
    TestNames string `json:"testNames" form:"testNames"`  // 测试名称列表
}

// TestDBRsp 响应体
type TestDBRsp struct {
    TestList []*TestItem `json:"testList"`  // 测试列表
}

// TestItem ...
type TestItem struct {
    TestID int `json:"testId" form:"testId"`  // 测试ID
    TestName string `json:"testName" form:"testName"`  // 测试名称
}

// 若涉及redis数据获取，定义redis数据响应结构体，示例如下：
type TestRedisRsp struct {
    TestName string `json:"testName" form:"testName"`  // 测试名称
}

func (tf *TestFunc) Execute() (any, gerror.CodeError) {

    // 若涉及redis数据获取，调用封装的redis数据获取方法实现，示例如下：
    // testRedisResp, err := tf.TestRedisFunc(tf.Ctx, TestRedisKey)
    // if err != nil {
    //     log.SetWarning(rr.Ctx, resource.LoggerService, types.ErrRedisqueryFail, err.Error())
    //     return nil, gerror.NewCodeError(types.ErrRedisqueryFail, err.Error())
    // }
    
    // 若涉及mysql数据获取，调用数据库数据获取方法，实现数据库数据获取操作，示例如下：
    // testDBResp, err := tf.TestDBFunc(tf.Ctx)
	// if err != nil {
	// 	   log.SetWarning(rr.Ctx, resource.LoggerService, types.ErrRalCommonFail, err.Error())
	//     return nil, gerror.NewCodeError(types.ErrRalCommonFail, err.Error())
	// }
	
    // ...
}

func (tf *TestFunc) PreCheck() gerror.CodeError {
    // 所有基础参数校验通过Validator即可实现，参照以下方式实现：
    if _, tf.request = pre.Validator[TestFuncReq](tf.Ctx, tf.Req); tf.request == nil {
        return gerror.NewCodeError(types.ErrParam, "request params check failed")
    }
    
    // 涉及复杂的参数解析校验，示例如下：
    // 示例：需求要求对于参数TestNames，需采用";"进行分隔成数组TestName，分割后的数组长度不能大于8
    // TestName := strings.Split(tf.request.TestNames, ";")
    // if len(testSubParam1) > 8 {
    //     return gerror.NewCodeError(types.ErrParam, "request TestName check failed")
    // }
    return nil
}

// 若涉及redis数据获取，封装对应数据获取方法，示例如下：
TestRedisFunc ...
func (tf *TestFunc) TestRedisFunc(ctx context.Context, key string) (*TestRedisRsp, error) {

    // 用户指定redis对象 `TestRedis`，则采用 `resource.TestRedis` 进行操作，否则默认采用`resource.RedisMsgLogic`，获取数据，通过.Result() 获取结果
    result, err = resource.TestRedis.Get(ctx, key).Result()
    if err != nil {
        log.SetWarning(rr.Ctx, resource.LoggerService, types.ErrRedisqueryFail, err.Error())
        return nil, gerror.NewCodeError(types.ErrRedisqueryFail, err.Error())
	}
    // 设置数据，通过.Result() 获取结果，示例如下：
    _, err := resource.TestRedis.Set(ctx, "key-abc", "value-123", time.Minute).Result()
    // ...
}

// 若涉及mysql数据获取，需实现数据库数据获取方法，逻辑均实现在service层，示例如下：
// TestDBFunc ...
func (tf *TestFunc) TestDBFunc(ctx context.Context) ([]*TestDBRsp, error) {
    req := tf.request
    // 构建查询条件
	where := map[string]any{
		"test_id": req.TestId,
	}
	
	// 查询数据
	result := make([]TestItem, 0)
	err := dao.NewTestDBDao().WithContext(tf.Ctx).
        Select(dao.TestDefaultField).
		Where(where).Find(&result).Error
	if err != nil {
		log.SetWarning(rr.Ctx, resource.LoggerService, types.ErrRalCommonFail, err.Error())
		return nil, gerror.NewCodeError(types.ErrRalCommonFail, err.Error())
	}

	return &TestDBRsp{TestItem: result}, nil
}
```
### mysql数据库表、操作对象等定义文件，文件路径：`model/dao/test_info.go`
```go
package dao

import (
	"context"
	"strconv"

	jsoniter "github.com/json-iterator/go"
	"icode.baidu.com/baidu/searchbox/tradeserver/library/log"
	"icode.baidu.com/baidu/searchbox/tradeserver/library/resource"
	"icode.baidu.com/baidu/searchbox/tradeserver/library/types"
)

// 表名
const TestInfoTable = "test_info"

// TestInfo 表结构
type TestInfo struct {
    TestID   uint64 `ddb:"test_id" gorm:"column:test_id" json:"test_id"`  // 测试id
    TestNID  string `ddb:"test_nid" gorm:"column:test_nid" json:"test_nid"`  // 测试nid
    TestName string `ddb:"test_name" gorm:"column:test_name" json:"test_name"`  // 测试名称
}

var TestDefaultFields = []string{
	"test_id",
	"test_name",
}

// TestInfoDao dao层，依赖于参考基类DBDao
type TestInfoDao struct {
    DBDao
    GDB
}

// NewTestInfoDao 初始化表
func NewTestInfoDao() *TestInfoDao {
    return &TestInfoDao{
        DBDao: NewDBDao(TestInfoTable, resource.MysqlTrade),
        GDB:   NewGDB(TestInfoTable, resource.MysqlGorm),
    }
}
```
# gdp框架项目结构，用于对项目框架的理解，无需生成：
├── Dockerfile
├── httpserver
│   ├── controller
│   │   └── test_package // 包名，需根据需求指定命名，如：需求中指定路径最后两个层级为`path1/path2`，则包名为path1，否则根据需求内容自定义
│   │      └── test_xxx.go // controller层代码存放文件，需根据需求指定命名，如：需求中指定路径最后两个层级为`path1/path2`，则文件名为path2.go，否则根据需求自定义命名
│   └── router.go // router层代码存放文件
├── library
│   └── resource.go  // redis原生操作包
└── model
    ├── dao  // dao层代码存放路径
    │   └── test_xxx.go  // mysql数据表定义、初始化等代码存放文件
    └── service  
        └── test_package // 包名，需根据需求指定命名，如：需求中指定路径最后两个层级为`path1/path2`，则包名为path1，否则根据需求内容自定义
            └── test_xxx.go  // service层业务逻辑代码存放文件，需根据需求指定命名，如：需求中指定路径最后两个层级为`path1/path2`，则文件名为path2.go，否则根据需求自定义命名

# 要求
## 生成要求:
* 特别注意，controller层的 入参: context.Context和ghttp.Request，  出参: ghttp.Response
* 示例代码中TestXXX/testXXX等代表示例名，需要根据需求改成实际的名字， 如test_file.go需要根据描述改成相关的File名, Test变量也需要响应修改
* 注意代码生成过程中添加从需求中提炼的简洁注释，要导出的方法、结构体采用`// 方法名...`、`// 结构体名...`格式进行注释
* 注意异常处理时打印对应异常日志
* service层关于参数校验的逻辑代码必须都放在PreCheck函数中，不要在业务逻辑函数中实现

## 输出要求：
* 给出生成的代码，以及文件路径
* 按照指定层存放代码逻辑，不要重复实现函数
* 写全各个规定层的代码，禁止省略代码！！！

# 输出格式参考如下：
文件路径：`具体文件路径`
```go
```