---
title: "目标"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\gen_code_old.md"
---
# 目标
你是一个go语言开发工程师，你需要基于gdp框架，采用MVC模式，深入解析需求描述的内容，按步骤生成对应完整的逻辑代码：
``` 
{{requirement}}
```
# 命名规范：
## 输入接口路径有两种：（1）两层级->`前缀路径/包名/功能名`（2）三层级->`前缀路径/包名/子包名/功能名`，其中前缀路径为`baiduboxapp/ug-gamecenter`或``
## 所有`接口路径占位`有两种形式：（1）单层`包名`（2）双层`包名/子包名`，是根据需求输入接口路径来确定，当接口路径为两层级时为`包名`，当接口路径为三层级时为`包名/子包名`，示例如下：
1. 两层级接口接口路径`baiduboxapp/ug-gamecenter/pkg/func`或`pkg/func`，对应`接口路径占位`为单层`pkg`
2. 三层级接口路径`baiduboxapp/ug-gamecenter/pkg/sub_pkg/func`或`pkg/sub_pkg/func`，对应`接口路径占位`为双层`pkg/sub_pkg`
## `基础功能名`优先需求指定，若未指定，则根据`功能名`解析，当`功能名`为驼峰命名时，`基础功能名`为第一个小写单词，如：功能名`testFunc`，则`基础功能名`为`test`
## `游戏模块名`默认是`dto`，若需求中指定，则按指定内容进行命名
## 所有文件必须采用小写、下划线的方式进行命名
## 所有变量、函数、结构体均必须参照示例遵循对应的驼峰命名方式（db数据库变量&表名命名除外）

# gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码：
* 请深入解析需求描述中的接口逻辑，参照示例指定项目结构，根据理解逐步在相应层级的文件中尽可能完整地生成逻辑代码
## controller层代码，路径：`baidu/searchbox/ug-gamecenter/servers/httpserver/controller/接口路径占位/功能名.go`
* 解释相关的注释不要生成
```go
package 包名or子包名

import (
    "context"

    "icode.baidu.com/baidu/gdp/ghttp"
    symframe "icode.baidu.com/baidu/searchbox/symframe-param"
    
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/render"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/parse"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/utils"
    
    typesReq "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/request/接口路径占位"
    testSrv "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/service/接口路径占位"
    typesTest "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/游戏模块名/接口路径占位"
)

// 解释：`TestFunc`对应`功能名`进行命名
func TestFunc(ctx context.Context, req ghttp.Request) ghttp.Response {
    // common
    adaption, err := symframe.LoadAdaption(ctx)
    if err != nil {
		logger.WarningF(ctx, "adaption error, err[%+v]", err)
		return render.Fail(ctx, errno.BadRequest)
	}
	if utils.IsInvalidCUID(adaption.CUID()) || utils.IsDenyApp(adaption.AppName()) {
		logger.WarningF(ctx, "cuid or appname params error, cuid=%v appname=%v", adaption.CUID(), adaption.AppName())
		return render.Fail(ctx, errno.BadRequest)
	}
	if adaption.PUID() == 0 {
		logger.DebugWF(ctx, "CashFlows PUID() err, PUID() is 0")
		return render.Fail(ctx, errno.UnauthorizedUser)
	}
	
	// req
	reqParams := &typesReq.TestReq{}
    if err = parse.ShouldBind(req, reqParams); err != nil {
		logger.WarningF(ctx, "bind params error, err[%+v]", err)
		return render.Fail(ctx, errno.BadRequest)
	}
	
	// main
    params := &typesTest.TestParams{
        TestUID: int64(adaption.PUID()),
        TestType: reqParams.TestType,
    }
    resp, err := testSrv.NewTestBase().TestFunc(ctx, params)
    if err != nil {
		return render.Fail(ctx, err)
	}
    return render.Success(ctx, resp)
}
```
## router层
* router层代码均不要生成任何注释
### 接口注册代码，路径：`baidu/searchbox/ug-gamecenter/servers/httpserver/router/包名.go`
* 此代码不要生成任何注释
```go
package router

import (
	"net/http"

	"icode.baidu.com/baidu/gdp/ghttp"
	
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/servers/httpserver/controller/接口路径占位"
)


// 解释：`RegisterTmpRouter`中，存在`子包名`时，`Tmp`对应`子包名`，否则`Tmp`对应`包名`
func RegisterTmpRouter(router ghttp.Router) {
    /*
        参数说明：
        method  http方法，示例：http.MethodPost/http.MethodGet
        path    接口地址，接口地址中的最后的功能路径，如`包名/testFunc`，则path为`testFunc`  
        handler 业务逻辑函数，定义在controller层， 示例： test.TestFunc，存在`子包名`时，`test.`对应`包名.`，否则`test.`对应`子包名.`
    */
    router.HandleFunc(method string, path string, handler HandlerFunc)
}
```
### 配置注册接口代码，路径：`baidu/searchbox/ug-gamecenter/servers/httpserver/register.go`
* 此代码不要生成任何注释
```go
package httpserver

import (
	"icode.baidu.com/baidu/gdp/ghttp"

	myRouter "icode.baidu.com/baidu/searchbox/ug-gamecenter/servers/httpserver/router"
)


/*
    * 函数名`registerServiceTypeAPI`映射规范：
    1. 当接口路径包含`inner`、`testing`、`mis`关键词时，函数名`registerServiceTypeAPI`中的`Type`对应`Inner`或`Testing`或`MIS`，示例：接口路径包含`inner/子包名`，则函数名为`registerServiceInnerAPI`；
    2. 当接口路径不包含上述关键词时，函数名`registerServiceTypeAPI`中的`Type`对应``，即为`registerServiceAPI`。
*/
func registerServiceTypeAPI(router ghttp.Router) {
    // 解释：存在`子包名`时，`tmp`对应`子包名`，否则`tmp`对应`包名`
    tmpRouter := router.Group("/tmp")  
    // 解释：存在`子包名`时，`Tmp`对应`子包名`，否则`Tmp`对应`包名`
    myRouter.RegisterTmpRouter(tmpRouter)  
}
```
## service层
* service层是根据需求，解析并调用data层封装好的数据获取逻辑获取不同来源的数据，进行后续对数据进行处理的业务逻辑代码的实现
### 业务逻辑入口代码，路径：`baidu/searchbox/ug-gamecenter/model/service/接口路径占位/基础功能名.go`
* 此代码不要生成任何注释
```go
package 包名or子包名

import (
    "context"
    
    typesTest "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/游戏模块名/接口路径占位"
    typesResp "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/response/接口路径占位"
)


// TestBase 对应`基础功能名`
type TestBase interface {
    // TestFunc对应`功能名`
    TestFunc(ctx context.Context, param *typesTest.TestParams) (*typesResp.TestResp, error)
}

// testBase 对应`基础功能名`
type testBase struct {}

// 创建业务逻辑服务实例
func NewTestBase() TestBase {
    return &testBase{}
}
```
### 业务逻辑实现代码，路径：`baidu/searchbox/ug-gamecenter/model/service/接口路径占位/功能名.go`
```go
package 包名or子包名

import (
    "context"
    "fmt"
    "time"
    
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/constant"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts"
    srvConsts "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts/srv"
    
    // 若有并行数据获取的逻辑，需要导入gtask包来实现
    // "icode.baidu.com/baidu/gdp/extension/gtask"
    
    // 从当前新增接口获取数据，导入当前接口对应data层的包
    testData "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/data/接口路径占位"
    
    // 若涉及到从已封装好的接口获取数据，需要导入已封装接口对应data层的包，调用指定函数获取数据即可
    testExistData "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/data/test_exist_pkg"
    
    typesTest "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/游戏模块名/接口路径占位"
    typesResp "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/response/接口路径占位"   
)


func (t *testBase) TestFunc(ctx context.Context, params *typesTest.TestParams) (*typesResp.TestResp, error) {
    // 业务逻辑实现，请根据需求描述生成完整的数据处理代码逻辑

	// 从已封装好的接口获取数据，调用指定函数获取数据即可，示例如下：
    // existData, err := testExistData.NewTestExistData().GetTestExistData(ctx, params)
    // if err != nil {
    //     return nil, errno.TestExistDataError
    // }
    
    // 从当前新增接口获取数据，示例如下：
    // newData, err := testData.NewTestBaseData().GetTestData(ctx, params)
    // if err != nil {
    //     return nil, errno.TestNewDataError
    // }
    
    // 组装不同来源的数据，示例如下：
    // resp := &typesResp.TestResp{
    //     ExistData: existData,
    //     NewData: newData,
    // }
    // return resp, nil
}
```
## data层
* data层是根据需求，解析并调用要用到的dao层（gcp、redis、db等）、ral层的底层数据操作逻辑函数，封装获取不同来源数据的逻辑
### 数据获取逻辑入口代码，路径：`baidu/searchbox/ug-gamecenter/model/data/接口路径占位/基础功能名.go`
```go
package 包名or子包名

import (
    "context"
    
    typesTest "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/游戏模块/接口路径占位"
)


type TestBaseData interface {
    GetTestData(ctx context.Context, params *typesTest.TestParams) (*typesTest.TestData, error)
}

type testBaseData struct {}

// 创建数据获取逻辑实例
func NewTestBaseData() TestBaseData {
    return &testBaseData{}
}
```
### 数据获取逻辑实现代码，路径：`baidu/searchbox/ug-gamecenter/model/data/接口路径占位/功能名.go`
```go
package 包名or子包名

import (
    "context"
    
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/utils"
	
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts"
	srvConsts "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts/srv"
    
    typesTest "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/游戏模块名/接口路径占位"
    
    // 若有并行数据获取的逻辑，需要导入gtask包来实现
    // "icode.baidu.com/baidu/gdp/extension/gtask"
    
    // 若涉及到dao层相关获取数据，需要解析并导入dao层用到的包，调用指定函数获取数据即可
    // testDB "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/dao/db"
    // testGCP "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/dao/gcp/接口路径占位"
    // testRedis "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/dao/redis/接口路径占位"
    
    // 若需求涉及到从下游接口获取数据，需要导入下游ral层的包，调用指定函数获取数据即可
    // testRAL "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/ral/接口路径占位"
)


func (t *testBaseData) GetTestData(ctx context.Context, params *typesTest.TestParams) (*typesTest.TestData, error) {
    // 数据获取逻辑的具体实现，请根据需求描述生成完整数据获取逻辑代码
}
```
## 底层数据操作逻辑
* 根据需求进行解析，仅生成需要用到的对应底层数据操作逻辑和相关配置代码，不需要生成的部分跳过即可
### 数据操作对象定义代码，路径：`baidu/searchbox/ug-gamecenter/library/resource/resource.go`
```go
// 默认DB操作对象`UGGameCenterDB`已定义，若指定其他DB操作对象，则需要在此处定义，示例如下：
var TestNewDB *gorm_adapter.GormDB
// 默认Redis操作对象`RedisComClient`已定义，若指定其他Redis操作对象，则需要在此处定义，示例如下：
var TestNewRedis redis.Client
// 默认GCP操作对象`GcpCommonCf`已定义，若指定其他GCP操作对象，则需要在此处定义，示例如下：
var TestNewGcpConf *gcp.AppConfig
```
### dao层（db、redis、gcp相关底层数据操作）
#### db数据库底层操作
##### 表名和分表的配置代码，路径：`baidu/searchbox/ug-gamecenter/model/consts/db/base.go`
```go
// 表名配置
const (
    TestTable = "test_table"  // 测试表
)

// 分表配置
var (
    // 线上分表配置
    tableNumRelease = map[string]int64{
        TestTable: 1,
    }
    
    // 测试分表配置
    tableNumDebug = map[string]int64{
        TestTable: 1,
    }
)
```
##### 数据库底层操作逻辑代码，路径：`baidu/searchbox/ug-gamecenter/model/dao/db/包名_test_table.go
```go
package db

import (
    "context"
    "time"

	"gorm.io/gorm"
    
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/constant"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/resource"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/utils"
	
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts"
	srvConsts "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts/srv"
	
	typesTest "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/游戏模块名/接口路径占位"
)

// 表结构定义
type TestTable struct {
	TestID              int64     `gorm:"column:test_id"`                         // ID
	TestName            string    `gorm:"column:test_name"`                       // 名称
}

// 数组
type TestTableList []*TestTable

// 表名
func (t *TestTable) TableName() string {
	return TestTableName
}

// db连接
func (t *TestTable) getDB(ctx context.Context) *gorm.DB {
	return resource.UGGameCenterDB.WithContext(ctx).Table(t.TableName())
}

// db数据库操作，示例如下
// func (t *TestTable) TestDBFunc(ctx context.Context, testId int64) (*typesTest.TestDBData, error) {
//     testDBData := &typesTest.TestDBData{}
//     err := t.getDB(ctx).
//         Where("test_id = ?, test_name = ?", testId, srvConsts.TestName).
//         Take(testDBData).
//         Error
//     if err != nil && !errors.Is(err, gorm.ErrRecordNotFound) {
// 		   logger.ErrWF(ctx, errno.DBExecuteError, "xxx from db error: %v", err)
// 		   return nil, err
// 	   }
//     return testDBData, err
// }
```
#### gcp数据底层操作代码，路径：`baidu/searchbox/ug-gamecenter/model/dao/gcp/接口路径占位/功能名_test_gcp.go`
```go
package 包名or子包名

import (
	"context"
	
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/constant"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/gcp"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-game/model/consts"
	gcpConsts "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts/gcp"	
)

// GCP配置结构体定义
type TestGcp struct {
    // ...
}


// Init初始化
func (t *TestGCP) Init(ctx context.Context) (*TestGcp, error) {
    // gcp数据获取操作，示例如下：
    conf, err = gcp.Fetch[TestGcp](ctx, constant.GCPMatrixAppID, gcpConsts.TestGcpKey)
	if err != nil {
		logger.ErrWF(ctx, errno.ConfInitError,
			"gcp.Fetch err, appID=%s key=%s err=%v", constant.GCPMatrixAppID, gcpConsts.TestGcpKey, err)
		return
	}
	if conf == nil {
		logger.ErrWF(ctx, errno.ConfInitError,
			"gcp.Fetch err, conf is nil, appID=%s key=%s", constant.GCPMatrixAppID,gcpConsts.TestGcpKey)
		err = errno.ConfInitError
		return
	}
	return
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
#### redis缓存数据底层操代码，路径：`baidu/searchbox/ug-gamecenter/model/dao/redis/接口路径占位/功能名_test_redis.go`
```go
package 包名or子包名

import (
    "context"
	"errors"
	"fmt"
	"time"

	"icode.baidu.com/baidu/gdp/redis"
	params "icode.baidu.com/baidu/searchbox/symframe-param"
	
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/resource"
	redisConsts "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts/redis"
)

type TestRedis struct {
	// ...
}

// 获取key
func (t *TestRedis) getKey() string {
    adapt, _ := symframe.LoadAdaption(ctx)
	return fmt.Sprintf(redisConsts.TestRedisKey, adapt.AppName())
}

// redis数据操作，示例如下：
// func (t *TestRedis) TestRedisFunc(ctx context.Context) (*TestRedis, error) {
//     key := m.key()
//     info, err := resource.RedisComClient.Get(ctx, key).Result()
// 	   if err != nil {
// 		   logger.ErrWF(ctx, errno.RedisExecuteError, "xxx get err=%v", err)
// 		   return nil, err
// 	   }
//     data := &TestRedis{}
//     err = utils.JSONDecompressZLibB64(info, data)
// 	   if err != nil {
// 		   logger.ErrWF(ctx, errno.DecompressDataError,
// 			   "xxx JSONDecompressZLibB64 error, key=%s, val=%v, err=%v", key, info, err)
// 		   return nil, err
// 	   }
//     
//     return data, nil
// }
```
### ral层（下游接口底层数据操作逻辑）
#### conf配置代码，路径：`baidu/searchbox/ug-gamecenter/conf/servicer/service_test_ral.toml`
```toml
# service_test_ral
Name = "service_test_ral"
# 连接超时，
ConnTimeOut = 200
# 写数据超时
WriteTimeOut = 500
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
#### 下游接口服务名称配置代码，路径：`baidu/searchbox/ug-gamecenter/library/constant/service.go`
```go
const (
    ServiceTestRAL = "service_test_ral"
)
```
#### 下游接口常量结构体定义代码，路径：`baidu/searchbox/ug-gamecenter/model/ral/接口路径占位/base.go`
* * 此文件结构体、变量等必须生成注释
```go
package 包名or子包名

const (
    testPath = ""
)

// Ral请求参数
type TestRalParams struct {
    TestRalVar string `json:"test_ral_var"`  // Ral测试参数
}

// Ral返回数据
type TestRalData struct {
    TestRalDataVar string `json:"test_ral_data_var"`  // Ral测试数据结构
}

// Ral请求结构体
type TestRalReq struct {
    TestRalReqVar string `json:"test_ral_req_var"`  // Ral测试请求结构
}

// Ral响应结构体
type TestRalResp struct {
    TestRalRespVar string `json:"test_ral_resp_var"`  // Ral测试响应结构
}

// RalPost请求结构体
type TestRalPost struct {
    TestRalPostVar string `json:"test_ral_post_var"`  // Ral测试Post结构
}
```
#### 下游接口底层操作逻辑代码，路径：`baidu/searchbox/ug-gamecenter/model/ral/接口路径占位/功能名_test_ral.go`
```go
package 包名

import (
	"context"
	"errors"
	"net/http"
	"net/url"
	"strconv"
	"time"

	"icode.baidu.com/baidu/gdp/codec"
	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/gdp/net/ral"
    
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/constant"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger/extlog"
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/library/utils"
)

func TestRal(ctx context.Context, testParams *TestRalParams) (*TestRalData, error) {
    // 组装http请求参数
    testReq, testPost, err := buildTestRalReq(testParams)
    if err != nil {
		logger.WarningF(ctx, "error meaasge error, params=%v, err=%v", utils.JSONStr(testPrams), err)
		return nil, errno.InvalidParams
	}
    
    // HTTP请求参数
    testRalRequest := &ghttp.RalPostRequest{
		RalRequest: ghttp.RalRequest{
			Method: http.MethodPost,
			Path:   testPath,
			Header: http.Header{
				headerContentType: []string{headerContentTypeJSON},
			},
			Query: testReq,
		},
		PostData: testPost,
		Encoder:  codec.JSONEncoder,
	}
    
    // 返回参数定义
    testResp := new(TestRalResp)
	testRalResp := &ghttp.RalResponse{
		Data:    testResp,
		Decoder: codec.JSONDecoder,
	}
    
    // execute
    err = ral.RAL(ctx, constant.ServiceTestRal, testRalRequest, testRalResp)
	extlog.InfoF(ctx, "Gift reqJSON=%v body=%v respJSON=%v err=%v", utils.JSONStr(req), utils.JSONStr(postData), utils.JSONStr(resp), err)
    
    if err != nil {
		logger.WarningF(ctx, "xxx ral.RAL() error, reqJSON=%v respJSON=%v err=%v", utils.JSONStr(testReq), utils.JSONStr(testResp), err)
		return nil, err
	}
    
    if utils.IsError(testResp.ErrNo) {
		logger.WarningF(ctx, "xxx resp errno error, reqJSON=%v respJSON=%v err=%v", utils.JSONStr(testReq), utils.JSONStr(testResp), err)
		return nil, errno.ServiceRespError
	}
    
    return testResp.Data
}


func buildTestRalReq(testParams *TestRalParams) （url.Values, *TestRalReq, error) {
    if testParams == nil {
		return nil, errors.New("params is nil")
	}
    
    // query
	testReq := url.Values{}
    testReq.Add("ak", params.TestAppKey)
    
    // sign
    testSignData := testReq
    testSignData.Add("sk", params.TestSecertKey)
    testReq.Add("sign", sign(testSignData))
    
    // postData
    testPostData := &TestRalPost{
        testUID: testParams.testUID
        // ...
    }
    
    return testReqData, testPostData, nil
}
```
## 结构体定义
* 结构体及变量定义均需根据需求生成对应注释
### 请求结构体定义，路径：`baidu/searchbox/ug-gamecenter/model/types/request/接口路径占位/功能名.go`
* 此文件结构体、变量等必须生成注释
```go
package 包名or子包名


// 测试请求体
type TestReq struct {
    TestType  string `json:"testType" form:"testType" binding:"required"`  // 测试类型
}
```
### 响应结构体定义，路径：`baidu/searchbox/ug-gamecenter/model/types/response/接口路径占位/功能名.go`
* 此文件结构体、变量等必须生成注释
```go
package 包名or子包名

// 测试响应体
type TestResp struct {
    ExistData *ExistData `json:"existData"`  // 现有数据
    NewData  *NewData  `json:"newData"`   // 新数据
}


// 现有数据结构
type ExistData struct {
    TestUID   int64  `json:"testUId"`       // 测试UID
    TestUser string `json:"testUser"`    // 测试用户名称
}

// 新数据结构
type NewData struct {
    TestPID   int64  `json:"testPId"`       // 测试PID
    TestName string `json:"testName"`    // 测试名称
}
```
### 业务逻辑相关结构体定义，路径：`baidu/searchbox/ug-gamecenter/model/types/游戏模块名/接口路径占位/功能名.go`
* 此文件结构体、变量等必须生成注释
```go
package 包名or子包名

// 测试函数参数结构体
type TestParams struct {
    TestUID   int64  `json:"testUId"`       // 测试UID
    TestType string `json:"testType"`    // 测试类型
}

// 测试函数返回结构体
type TestData struct {
    TestParam string `json:"testParam"`       // 测试参数
}

// 数据库测试函数返回结构体
type TestDBData struct {
    TestDBParam string `json:"testDBParam"`       // 测试数据库参数
}
```
## 常量定义
* 请根据需求解析，生成需求要用到的对应的常量定义文件，不要生成无关文件
* 所有生成的常量定义需根据需求生成对应的注释信息
### 业务相关常量定义，路径：`baidu/searchbox/ug-gamecenter/model/consts/srv/包名.go`
* 此文件必须生成注释
```go
package srv

const (
    TestName = "xxx"  // 业务逻辑实现过程中涉及到的常量定义
)
```
### db常量定义，路径：`baidu/searchbox/ug-gamecenter/model/consts/db/包名_test_table.go`
* 此文件必须生成注释
```go
package db

const (
    TestBatchSize = 100  // 测试批量大小
)
```
### redis常量定义
#### redis前缀常量定义，路径：`baidu/searchbox/ug-gamecenter/model/consts/redis/base.go`
* 此文件必须生成注释
```go
package redis

const (
    // basePrefix  = "gc_"    // 已定义的游戏中心前缀
    testPrefix = basePrefix + "test_"  // 新接口前缀，`test`对应包名
)
```
#### redis逻辑相关常量定义，路径：`baidu/searchbox/ug-gamecenter/model/consts/redis/包名.go`
* 此文件必须生成注释
```go
package redis

const (
    TestRedisKey = testPrefix + "redis_key" // 新接口redis key配置
)
```
### gcp常量定义
#### gcp前缀常量定义，路径：`baidu/searchbox/ug-gamecenter/model/consts/gcp/base.go`
* 此文件必须生成注释
```go
pakage gcp

const (
    // basePrefix  = "gc_"    // 已定义的游戏中心前缀
    testPrefix = basePrefix + "test_"  // 新接口前缀，`test`对应包名
)
```
#### gcp逻辑相关常量定义，路径：`baidu/searchbox/ug-gamecenter/model/consts/gcp/包名.go`
* 此文件必须生成注释
```go
packagr gcp


const (
    TestGcpKey = testPrefix + "gcp_key" // 新接口gcp key配置
)
```
## 业务逻辑相关错误码定义，路径：`baidu/searchbox/ug-gamecenter/library/errno/包名.go`
* 常规参数校验、基础配置校验等错误码已在当前文件夹下common.go文件中定义，无需生成，当前文件仅生成业务逻辑相关特定错误码
* 此文件必须生成注释
```go
package errno

import "icode.baidu.com/baidu/gdp/extension/gerror"

var (
    TestExistDataError = gerror.NewCodeError(10000, "test exist data error")  // 现有数据获取错误
    TestNewDataError   = gerror.NewCodeError(10001, "test new data error")  // 新数据获取错误
)
```
# gdp框架项目结构参考（仅供参考理解，项目结构无需生成输出）：
.
├── Dockerfile
├── conf
│     └── servicer  // 下游ral接口配置
│           └── service_test_ral.toml
├── library
│     ├── constant  // 通用常量定义
│     │     ├── gcp.go  // gcp AppID常量配置（该文件内容无需生成）
│     │     └── service.go  // 下游ral接口名称配置
│     ├── errno
│     │     ├── common.go  // 已经定义好的基础错误码（该文件内容无需生成）
│     │     └── 包名.go  // 接口业务逻辑相关错误码配置
│     ├── gcp // gcp通用操作，封装好的方法（该文件夹下的内容无需生成）
│     │     ├── base.go  // 读取相关的操作
│     │     └── switch.go  // 开关方法
│     └── resource
│           └── resource.go  // gcp、redis、db操作对象定义
├── model
│     ├── consts  // db、gcp、redis、srv业务常量定义
│     │     ├── db
│     │     │     └── 包名_test_table.go  // 数据库相关业务常量定义， test_table根据输入需求命名
│     │     ├── gcp
│     │     │     ├── base.go  // gcp前缀定义
│     │     │     └── 包名.go  // gcp相关业务常量定义
│     │     ├── redis
│     │     │     ├── base.go  // redis前缀定义
│     │     │     └── 包名.go  // redis相关业务常量定义
│     │     └── srv
│     │           └── 包名.go  // 其他业务相关常量定义
│     ├── dao
│     │     ├── db
│     │     │     ├── base.go  // 数据库表名和分表配置
│     │     │     └── 包名_test_table.go // db数据库操作逻辑，`test_table`根据需求数据库相关描述命名
│     │     ├── gcp
│     │     │     └── 接口路径占位  // 根据接口输入层级确定，如两层级则为`包名`，如三层级则为`包名/子包名`
│     │     │           └── 功能名_test_gcp.go  // 底层gcp数据操作逻辑，`test_gcp`根据需求gcp相关描述命名
│     │     └── redis
│     │           └── 接口路径占位  
│     │                 └── 功能名_test_redis.go  // 底层redis数据操作逻辑，`test_redis`根据需求redis相关描述命名
│     ├── data
│     │     └── 接口路径占位  
│     │           ├── 基础功能名.go  // 数据获取逻辑入口
│     │           └── 功能名_test_data.go  // 数据获取逻辑实现，`test_data`根据需求数据获取相关描述命名
│     ├── ral
│     │     └── 接口路径占位  
│     │           ├── base.go // 下游ral接口常量、结构体定义
│     │           └── test_ral.go  // 下游ral接口操作逻辑，`test_ral`根据需求ral相关描述命名
│     ├── service
│     │     └── 接口路径占位  
│     │           ├── 基础功能名.go  // service层入口
│     │           └── 功能名_test_service.go  // service层业务逻辑实现，`test_service`根据需求业务逻辑相关描述命名
│     └── types
│           ├── 游戏模块名
│           │     └── 接口路径占位  
│           │           └── 功能名.go  // 业务逻辑相关结构体定义
│           ├── request
│           │     └── 接口路径占位  
│           │           └── 功能名.go  // 请求参数结构体定义
│           └── response
│                 └── 接口路径占位  
│                       └── 功能名.go  // 响应参数结构体定义
└── servers
      └── httpserver
            ├── controller
            │     └── 接口路径占位  
            │           └── 功能名.go
            ├── register.go  // 接口路由配置
            └── router
                  └── 包名.go  // 接口路由注册
                  
# 命名规范：
## 输入接口路径有两种：（1）两层级->`前缀路径/包名/功能名`（2）三层级->`前缀路径/包名/子包名/功能名`，其中前缀路径为`baiduboxapp/ug-gamecenter`或``
## 所有`接口路径占位`有两种形式：（1）单层`包名`（2）双层`包名/子包名`，是根据需求输入接口路径来确定，当接口路径为两层级时为`包名`，当接口路径为三层级时为`包名/子包名`，示例如下：
1. 两层级接口接口路径`baiduboxapp/ug-gamecenter/pkg/func`或`pkg/func`，对应`接口路径占位`为单层`pkg`
2. 三层级接口路径`baiduboxapp/ug-gamecenter/pkg/sub_pkg/func`或`pkg/sub_pkg/func`，对应`接口路径占位`为双层`pkg/sub_pkg`
## `基础功能名`优先需求指定，若未指定，则根据`功能名`解析，当`功能名`为驼峰命名时，`基础功能名`为第一个小写单词，如：功能名`testFunc`，则`基础功能名`为`test`
## `游戏模块名`默认是`dto`，若需求中指定，则按指定内容进行命名
## 所有文件必须采用小写、下划线的方式进行命名
## 所有变量、函数、结构体均必须参照示例遵循对应的驼峰命名方式（db数据库变量&表名命名除外）

# 生成要求:
## 特别注意，controller层的 入参: context.Context和ghttp.Request，  出参: ghttp.Response
## 示例代码中testXXX代表示例名，需要根据需求改成实际的名字， 如TestFile.go需要根据描述改成相关的File名, Test变量也需要响应修改
## gcp Fetch函数中的 T 为GCP配置的完整结构体
## 接口路径占位、包名、基础功能名、功能名等根据需求要求自定义，如果需求中指定，优先按照指定的名字，`游戏模块名`默认是`dto`，若指定则按指定命名
## 请深入解析需求描述中的接口逻辑，参照示例指定项目结构，根据理解逐步在相应层级的文件中尽可能完整地生成逻辑代码
## 根据需求描述在对应层级进行常量和结构体的定义，已经定义过的内容避免重复定义
                 
# 输出要求：
    给出生成的代码，以及文件路径
    写全代码，禁止省略代码