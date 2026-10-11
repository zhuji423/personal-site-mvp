---
title: "目标"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_basic\\gen_code_old.md"
---
# 目标
你是一个go语言开发工程师，你需要基于gdp框架，采用MVC模式，深入解析需求描述的内容，按步骤生成对应完整的逻辑代码：
``` 
{{requirement}}
```
# 命名规范
## 输入接口路径有两种：（1）内部接口->`前缀路径/包名/功能名`（2）外部接口->`前缀路径/inner/包名/功能名`，其中前缀路径为`baiduboxapp/basic`或``，注意根据输入接口解析对应的`包名`和`功能名`
## 当需求中指定时，`结构体模块名`按指定内容进行命名，否则默认为`dto`## 所有文件必须采用小写、下划线的方式进行命名
## 所有变量、函数、结构体均必须参照示例遵循对应的驼峰命名方式（db数据库变量&表名命名除外）

# gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码：
## controller层代码，路径：`baidu/searchbox/sbox-basic/controller/包名/功能名.go`
```go
package 包名

import (
	"context"
	
	"icode.baidu.com/baidu/gdp/ghttp"
	params "icode.baidu.com/baidu/searchbox/symframe-param"
	
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/errno"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/logger"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/render"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/utils"
	
	"icode.baidu.com/baidu/searchbox/sbox-basic/model/service/包名"
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request"
)

// Controller
type Controller struct {
	srv 包名.TestService
}


// NewController
func NewController() *Controller {
	return &Controller{
		srv: 包名.NewService(),
	}
}

// TestFunc 测试接口-测试函数
func (c * Controller) TestFunc(ctx context.Context, req ghttp.Request) ghttp.Response {
    // 解析公参
	adaption, err := params.LoadAdaption(ctx)
	if err != nil {
		logger.WarningF(ctx, "failed to load adaption，error is %v", err)
		return render.Fail(ctx, errno.BadRequest)
	}
    
    // 接口参数校验
    testReq := request.TestReq{}
    if err := utils.ShouldBindWith(req, testReq); err != nil {
		logger.ErrorF(ctx, "params binding xxx request error, error is %s", err.Error())
		return render.Fail(ctx, errno.ErrInvalidParams)
	}
    
    // 调用service层逻辑处理函数
    resp, err := c.srv.TestFunc(ctx, testReq)
	if err != nil {
		return render.Fail(ctx, err)
	}

	return render.Success(ctx, resp)
}
```
## router层
### 接口路由注册，路径：`baidu/searchbox/sbox-basic/httpserver/包名.go`
```go
package httpserver

import (
	"net/http"

	"icode.baidu.com/baidu/gdp/ghttp"

	"icode.baidu.com/baidu/searchbox/sbox-basic/controller/包名"
)

// 注意当接口路径为包含`inner/`的内部接口时，注册函数名需加入Inner关键词，即`registerInnerTestFunc`
func registerTestFunc(router ghttp.Router) {
    ctl := 包名.NewController()
    /*
        HandleFunc参数说明：
        method  http方法，示例：http.MethodPost/http.MethodGet
        path    接口地址：接口地址中的最后的功能路径，如`包名/testFunc`，则path为`testFunc`   
        handler 业务逻辑，执行后会返回一个 Response 对象, 示例： ctl.TestFunc
    */
	router.HandleFunc(method string, path string, handler HandlerFunc)
}
```
### 注册接口路由配置，路径：`baidu/searchbox/sbox-basic/httpserver/router.go`
```go
// 注册路径配置函数
func httpRouter(ser *ghttp.DefaultServer) ghttp.Router {
    // ...
    
    // 常规接口注册配置，示例如下：
    // basicRouter := router.Group("/baiduboxapp/basic")
	// {
    //    registerTestFunc(basicRouter.Group("/包名"))
    // }
    
    // 内部接口注册配置，示例如下：
    // innerRouter := router.Group("/inner")
	// {
    //    registerInnerTestFunc(innerRouter)
    // }
}
```
## service层
* service层是根据需求，解析并调用data层封装好的数据获取逻辑获取不同来源的数据，进行后续对数据进行处理的业务逻辑代码的实现
### service层入口代码，路径：`baidu/searchbox/sbox-basic/model/service/包名/功能名_base.go`
```go
package 包名

import (
	"context"

	testData "icode.baidu.com/baidu/searchbox/sbox-basic/model/data/包名"
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request"
	response "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/response"
)

type TestService interface {
    TestFunc(ctx context.Context, req request.TestReq) (resp response.TestResp, err error)
}

type service struct {
    testData  testData.DataServ
}

type Option interface {
	apply(s *service)
}

type optionFn func(s *service)

func (fn optionFn) apply(s *service) {
	fn(s)
}

func defaultOption() Option {
	return optionFn(func(s *service) {
		s.testData = testData.NewService()
	})
}

func NewService(opts ...Option) TestService {
	s := &service{}
	defaultOption().apply(s)

	for _, opt := range opts {
		opt.apply(s)
	}
	return s
}
```
### service层业务逻辑代码，路径：`baidu/searchbox/sbox-basic/model/service/包名/功能名.go`
```go
package 包名

import (
	"context"
	
    // 若有并行数据获取的逻辑，需要导入gtask包来实现
    // "icode.baidu.com/baidu/gdp/extension/gtask"
    
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/errno"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/constant"
	
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request/包名"
	response "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/response/包名"
)

func (s * service) TestFunc(ctx context.Context, req request.TestReq) (*response.TestResp, error) {
    // 业务逻辑实现示例：
    testData, err := s.TestDataFunc(ctx, req.testId) 
    if err != nil {
        logger.WarningF(ctx, "failed to xxx, error is %v", err)
		return nil, err
    }
    // ...
}
```
## mysql、redis、gcp等数据操作对象定义代码，路径：`baidu/searchbox/sbox-basic/library/resource/resource.go`
```go
// 默认DB操作对象`UGGameCenterDB`已定义，若指定其他DB操作对象，则需要在此处定义，示例如下：
var TestNewDB *gorm_adapter.GormDB
// 默认Redis操作对象`RedisComClient`已定义，若指定其他Redis操作对象，则需要在此处定义，示例如下：
var TestNewRedis redis.Client
// 默认GCP操作对象`GcpCommonCf`已定义，若指定其他GCP操作对象，则需要在此处定义，示例如下：
var TestNewGcpConf *gcp.AppConfig
```
## data层
* data层是根据需求，解析并调用要用到的dao层（redis、db、ral等）、gcp封装好的底层数据操作逻辑函数，封装获取不同来源数据的逻辑
### data层入口代码，路径：`baidu/searchbox/sbox-basic/model/data/包名/功能名_base.go`
```go
package 包名

import (
	"context"
    
	testDao "icode.baidu.com/baidu/searchbox/sbox-basic/model/dao/包名"
	typeTest "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/结构体模块名/包名"
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request"
	response "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/response"
)

type DataServ interface {
    TestDataFunc(ctx context.Context, req request.TestReq)  (*response.TestResp, error)
}

type service struct {
	testDao testDao.Dao
}

type Option interface {
	apply(s *service)
}

type optionFn func(s *service)

func (fn optionFn) apply(s *service) {
	fn(s)
}

func defaultOption() Option {
	return optionFn(func(s *service) {
		s.testDao = testDao.NewService()
	})
}

func NewService(opts ...Option) *service {
	s := &service{}
	defaultOption().apply(s)

	for _, opt := range opts {
		opt.apply(s)
	}
	return s
}
```
### data层数据获取逻辑代码，路径：`baidu/searchbox/sbox-basic/model/data/包名/功能名.go`
```go
package 包名

import (
	"context"
	"time"
    
    // 若存在db数据操作，则需要导入db包
    // "icode.baidu.com/baidu/searchbox/sbox-basic/model/dao/db"
    
    // 若存在gcp数据操作，则需要导入gcp包
	// "icode.baidu.com/baidu/searchbox/sbox-basic/library/gcp"
	
	// 若存在redis数据操作，则需要导入redis包
	// "icode.baidu.com/baidu/searchbox/sbox-basic/model/dao/redis"
    
    // 若存在ral下游服务操作，需导入dao包
    testDao "icode.baidu.com/baidu/searchbox/sbox-basic/model/dao/包名"
    
    typeTest "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/结构体模块名/包名"
    request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request"
	respones "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/response"
)


// 若涉及到Gcp相关操作，结构体
type TestGcp struct {
    TestGcpId int `json:"test_gcp_id" form:"test_gcp_id"`  // Gcp配置ID
}

func TestDataFunc(ctx context.Context, int testId) (*typeTest.TestData, error) {
    // 数据获取逻辑的具体实现，请根据需求描述生成完整数据获取逻辑代码
    
    // 若涉及Gcp数据操作，直接实现在本层，示例如下：
    // conf, err = gcp.Fetch[TestGcp](ctx, constant.GCPMatrixAppID, constant.TestGcpKey)
	// if err != nil || conf == nil {
	//          return nil, err
	// }
}
```
* gcp包已经封装好的方法直接调用即可，方法使用参考：
```go
// Fetch 获取单条数据， T 为GCP配置的结构体
func Fetch[T any](ctx context.Context, appID, key string) (T, error) {{}}
// FetchExtend 支持添加自定义参数获取， T 为GCP配置的结构体
func FetchExtend[T any](ctx context.Context, appID, key string, extParam map[string]any) (T, error) {{}}
// MultiFetch 获取GCP数据(获取多条数据)， T 为GCP配置的结构体
func MultiFetch[T any](ctx context.Context, appID, key string) ([]T, error) {{}}

// GetSwitch 获取GCP开关， 当GCP查询失败或者GCP未配置数据时，返回 defaultValue 作为默认开关值
func GetSwitch(ctx context.Context, appID, key string, defaultValue bool) (bool, error) {{}}
// GetSwitchValue 获取命中的实验组
func GetSwitchValue(ctx context.Context, appID, key string, defaultValue int) (int, error) {{}}
```
## dao层
* dao层封装的是底层数据操作逻辑，包括redis、ral、db等，需根据需求解析要用到的底层逻辑和配置进行参考生成，不需要的部分跳过即可
### ral下游数据操作
#### ral下游数据获取conf配置代码，路径：`baidu/searchbox/sbox-basic/conf/servicer/service_test_ral.toml`
```toml
# service_test_ral
Name = "service_test_ral"
# 连接超时，
ConnTimeOut = 300
# 写数据超时
WriteTimeOut = 150
# 读数据超时
ReadTimeOut = 500
# 请求失败后的重试次数：总请求次数 = Retry + 1
Retry = 1
# 资源使用策略，非必选，默认使用 RoundRobin
# RoundRobin: 依次轮询
[Strategy]
Name = "RoundRobin"

## 资源定位：BNS 配置，支持智能 BNS
[Resource.BNS]
BNSName = "xxx"
EnableSmartBNS = true
UsePort = "main"
```
#### ral下游接口服务名称配置代码，路径：`baidu/searchbox/sbox-basic/library/constant/service.go`
```go
const (
    ServiceTestRAL = "service_test_ral"
)
```
#### ral下游接口操作逻辑入口，路径：`baidu/searchbox/sbox-basic/model/dao/包名/功能名_base.go`
```go
package mission

import (
	"context"
    
    typeRal "icode.baidu.com/baidu/searchbox/sbox-basic/model/dao/包名"
    typeDao "icode.baidu.com/baidu/searchbox/sbox-basic/model/dao/包名/types"
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request"
)

type Dao interface {
    TestRalFunc(ctx context.Context, testParams typeRal.TestRalParams) (*typeRal.TestRalData, error)
}

type service struct {
}

type Option interface {
	apply(s *service)
}

type optionFn func(s *service)

func (fn optionFn) apply(s *service) {
	fn(s)
}

// 默认参数
func defaultOption() Option {
	return optionFn(func(s *service) {})
}

// NewService 创建 Service 实例
func NewService(opts ...Option) Dao {
	s := &service{}
	defaultOption().apply(s)

	for _, opt := range opts {
		opt.apply(s)
	}
	return s
}
```
#### ral下游数据底层操作逻辑，路径：`baidu/searchbox/sbox-basic/model/dao/包名/功能名.go`
```go
package 包名

import (
	"context"
	"encoding/json"
	"fmt"
	
	"icode.baidu.com/baidu/gdp/codec"
	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/gdp/net/ral"
	
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/logger"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/constant"
	request "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/request"
	// 若需要解析公参，则需要导入
	// params "icode.baidu.com/baidu/searchbox/symframe-param"
	
	"net/http"
	"net/url"
)

// ral相关常量配置
const (
    testPath = "test_path"
    testToken = "xxxxxxx"
)

// ral相关结构体定义

// Ral请求参数
type TestRalParams struct {
    TestRalVar string `json:"test_ral_var" form:"test_ral_var"`  // Ral测试参数
}

// Ral返回数据
type TestRalData struct {
    TestRalDataVar string `json:"test_ral_data_var" form:"test_ral_data_var"`  // Ral测试数据结构
}

// Ral返回体
type TestRalResp struct {
    Errno    int64          `json:"errno" form:"errno"`
    Data    *TestRalData    `json:"data" form:"data"`
}

// ral下游数据操作方法实现，示例如下：
func TestRalFunc(ctx context.Context, testParams *TestRalParams) (*TestRalData, error) {
    // 若需要做转换
    // paramsJSON, err := json.Marshal(params)
	// if err != nil {
	// 	return nil, err
	// }
	
	// 若需要提取公共参数，从adaption中解析
	// adaption, _ := params.LoadAdaption(ctx)
	
	// query
	query := url.Values{}
	// 组装参数示例
	// query.Add("token", testToken)
	// query.Add("test_ral_var", paramsJSON.TestRalVar)

	req := &ghttp.RalRequest{
		Method: http.MethodGet,
		Path:   testPath,
		Query:  query,
	}
	
	retData := &TestRalData{}
	ralRsp := &ghttp.RalResponse{
		Data:    retData,
		Decoder: codec.JSONDecoder,
	}
	
	if err := ral.RAL(ctx, constant.ServiceTestRal, req, ralRsp); err != nil {
		logger.WarningF(ctx, "failed to call Service[%s] error[%+v]", ServiceNameUserProfileTag, err)
		return nil, err
	}
	if retData.Errno != 0 {
		logger.WarningF(ctx, "%s return data error,data=%v", constant.ServiceTestRal, retData)
		return nil, fmt.Errorf("service %s get data error,errno=%v", constant.ServiceTestRal, retData.Errno)
	}

	return retData, nil
}
```
### redis包
#### 新增redis方法配置，路径：`baidu/searchbox/sbox-basic/model/dao/redis/service.go`
```go
type Redis interface {
	// 新增redis方法配置
	TestRedisFunc(ctx context.Context, testKey string) error
}
```
#### 新增redis方法底层逻辑代码，路径：`baidu/searchbox/sbox-basic/model/dao/redis/test_ral.go`
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
    TestRedisPrefix = "test_redis_prefix_"
)


// redis方法实现，示例如下：
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
### db底层数据操作代码，路径：`baidu/searchbox/sbox-basic/model/dao/db/test_table.go`
* 采用mysql封装好的方法实现增删改查等操作
```go
package db

import (
	"context"
	"fmt"
	"strconv"
	"time"

	"github.com/samber/lo"
	"icode.baidu.com/baidu/gdp/env"
	"icode.baidu.com/baidu/searchbox/symframe/lib/log"

	"icode.baidu.com/baidu/searchbox/sbox-basic/library/constant"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/errno"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/logger"
	"icode.baidu.com/baidu/searchbox/sbox-basic/library/resource"
)

// 数据表相关常量定义，示例如下：
const (
    TestTableCnt = 10  // 测试分表数量
    TestTablePrefix = "test_"  // 测试分表前缀
)

// db相关结构体定义
type TestDBResp struct {
    TestDBVar string `json:"testDBVar" form:"testDBVar"`  // 测试数据库变量
}


// 获取分表名称，示例如下：
func getTestTableName(uid string) string {
	uidInt, _ := strconv.Atoi(uid)
	seq := uidInt%TestTableCnt + 1
	return TestTablePrefix + strconv.Itoa(seq)
}

// 数据库操作方法实现，示例如下：
func TestDBFunc(ctx context.Context, testId int64, testUid string)  (*TestDBResp, error) {
    tableName := getTestTableName(testUid)
    var testDBData = TestDBResp{}
    err := resource.TestDB.
		Table(tableName).
		Where("test_id = ?", testId).
		Find(&testDBData).Error
    if err != nil {
		logger.WarningF(ctx, "xxx failed. uid[%s] err[%v]", uid, err)
		return data, errno.WrapError(errno.ErrDBGet, err)
	}
    return testDBData, nil
}
```
## types层结构体定义
### 接口请求体定义，路径：`baidu/searchbox/sbox-basic/model/types/request/包名.go`
```go
package request

// 请求体
type TestReq struct {
	TestId `json:"testId" form:"testId" binding:"required"`  // 测试Id
}
```
### 接口返回体定义，路径：`baidu/searchbox/sbox-basic/model/types/response/包名.go`
```go
type TestResp struct {
	TestData `json:"testData" form:"testData"`  // 测试数据
}
```
### 接口业务逻辑相关结构体定义，路径：`baidu/searchbox/sbox-basic/model/types/结构体模块名/包名/功能名.go
```go
package 包名

// 业务数据结构体
type TestServiceData struct {
	TestServiceData `json:"testServiceData" form:"testServiceData"`  // 测试业务数据
}
```
# gdp框架项目结构参考（仅供参考理解，项目结构无需生成输出）：
.
├── Dockerfile
├── conf
│    └── servicer
│         └── service_test_ral.toml  // ral下游服务配置
├── controller
│    └── 包名  // `包名`根据需求输入解析，优先根据指定命名，否则从接口路径后缀中提取解析`包名/功能名`
│        └── 功能名.go  // `功能名`根据需求输入解析，优先根据指定命名，否则从接口路径后缀中提取解析`包名/功能名`
├── httpserver
│    ├── 包名.go  // 接口注册
│    └── router.go  // 注册接口配置
├── library
│    ├── constant
│    │    ├── ...  // 其他通用常量配置
│    │    ├── service.go  // ral下游接口服务名配置
│    │    └── 包名.go  // 接口特定常量配置
│    ├── errno
│    │    └── 包名.go  // 接口错误码设置
│    ├── gcp // gcp通用操作，封装好的方法
│    │     ├── gcp.go  // 读取相关的操作
│    │     └── switch.go  // 开关方法
│    ├── errors // 通用错误码
│    │    └── basic_error.go  
│    └── resource
│         └── resource.go // 数据操作对象定义
└── model
     ├── dao
     │    ├── db
     │    │    └── test_table.go  // db数据库的底层操作逻辑
     │    ├── redis
     │    │    ├── service.go  // redis数据操作相关方法配置
     │    │    └── test_redis.go  // redis数据操作底层逻辑
     │    └── 包名
     │         ├── 功能名.go  // dao层数据操作入口
     │         └── test_ral.go  // ral数据操作相关底层逻辑
     ├── data
     │    └── 包名
     │         ├── 功能名_base.go
     │         └── 功能名.go
     ├── service
     │    └── 包名
     │         ├── 功能名_base.go
     │         └── 功能名.go
     └── types
         ├── 结构体模块名（默认为`dto`）
         │    └── 包名
         │         └── 功能名.go
         ├── request
         │    └── 包名.go
         └── response
              └── 包名.go
# 命名规范
## 输入接口路径有两种：（1）内部接口->`前缀路径/包名/功能名`（2）外部接口->`前缀路径/inner/包名/功能名`，其中前缀路径为`baiduboxapp/basic`或``，注意根据输入接口解析对应的`包名`和`功能名`
## 当需求中指定时，`结构体模块名`按指定内容进行命名，否则默认为`dto`
## 所有文件必须采用小写、下划线的方式进行命名
## 所有变量、函数、结构体均必须参照示例遵循对应的驼峰命名方式（db数据库变量&表名命名除外）

# 生成要求:
## 特别注意，controller层的 入参: context.Context和ghttp.Request，  出参: ghttp.Response
## 示例代码中testXXX代表示例名，需要根据需求改成实际的名字， 如TestFile.go需要根据描述改成相关的File名, Test变量也需要响应修改
## gcp Fetch函数中的 T 为GCP配置的完整结构体
## 请深入解析需求描述中的接口逻辑，参照示例指定项目结构，根据理解逐步在相应层级的文件中尽可能完整地生成逻辑代码
## 根据需求描述在对应层级进行常量和结构体的定义，已经定义过的内容避免重复定义
                 
# 输出要求：
    给出生成的代码，以及文件路径
    写全代码，禁止省略代码