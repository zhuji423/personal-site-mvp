---
title: "Service的名字，必选"
description: "gdp2框架使用&接口开发"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\gdp2框架使用&接口开发.md"
---
gdp2框架使用&接口开发

## 一、GDP2 介绍
GDP2（ Go Develop Platform ）是一个对厂内的 Go 开发框架。具备完善的 RPC Client 和 RPC Server 能力，以及配套的通用基础库，可以用来开发 API、Web 及后端服务等各种应用。

![](/personal-site-mvp/img/doc-placeholder.svg "")
文档：[http://gdp.baidu-int.com/gdp2/docs/readme/](http://gdp.baidu-int.com/gdp2/docs/readme/)

## 二、GDP 接口服务构成
### 1、环境
go环境安装：[go环境安装与配置](./gdp2框架使用&接口开发_引用文档/go环境安装与配置.md)

icoding安装：[icoding安装与comate插件使用](./gdp2框架使用&接口开发_引用文档/icoding安装与comate插件使用.md)

### 2、安装gdp2
```
go install icode.baidu.com/baidu/gdp/gps/gdp@master
```
`go install`会将命令安装到 `$GOBIN` 目录下。如果报错connect: connection refused，配置 Go Proxy（参考[go环境安装与配置](./gdp2框架使用&接口开发_引用文档/go环境安装与配置.md)第三部分）后再次执行

![](/personal-site-mvp/img/doc-placeholder.svg "")
查看是否安装成功： gdp help

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 3、项目构成
#### 初始化项目
```
gdp new baidu/personal/myapp
```
创建完成后，项目结构如：[1.项目组织结构](./gdp2框架使用&接口开发_引用文档/1.项目组织结构.md)

```
.
├── bin            // 存放启动脚本，编译输出的二进制文件
├── bootstrap      // 应用初始化相关代码
├── cmd            // 其他 Go CLI 程序代码，如定时任务程序、临时处理数据的程序
├── conf           // 配置文件，线下测试开发
├── conf_online    // 配置文件，线上
├── data           // 数据目录
├── document       // 设计文档存放目录，可选
├── library        // 模块自己的公共基础库，没有 RPC 调用的可以放在这里
├── log            // 日志输出目录，不同类型的日志分别放在不同的子目录
├── model          // 业务模型层代码，一般会有子目录
│   └── service    // 存放service相关代码的目录，一般与controller下的文件一一对应
├── script         // 其他相关脚本，如 php、python、shell 脚本
├── servers        // 将一个应用的所有的 server 都放在此目录下
│   ├── adminserver  // 管理类功能的 server，也是一个 HTTP Server，监控指标等信息也是通过这个 server 对外输出
│   ├── httpserver   // HTTP Server   的相关代码(Server创建、路由注册、协议专属的控制器代码)
│   │   └── controller   // 存放controller相关代码的目录，一般与service下的文件一一对应
│   ├── router.go        // 路由注册
│   └── server.go        // Server 初始化
├── webroot        // 当对外提供 HTTP 服务时，此目录存放 css、js 等资源文件
├── ci.yml
├── Dockerfile
├── go.env
├── go.mod         // module 描述文件，包括依赖的版本信息
├── go.sum         // 依赖模块的签名信息，不可缺少
├── main.go        // 当前应用的主入口文件
├── Makefile
└── README.md
```
#### 构建运行项目
启动服务

```
go run main.go
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
默认显示端口是 8080

#### 路由
在myapp/servers/httpserver 目录中

![](/personal-site-mvp/img/doc-placeholder.svg "")
路由注册在router.go中

![](/personal-site-mvp/img/doc-placeholder.svg "")
controller中有2个接口的实现

```
package controller

import (
	"context"

	"icode.baidu.com/baidu/gdp/ghttp"
)

func Hello(ctx context.Context, req ghttp.Request) ghttp.Response {
	return ghttp.NewHTMLResponse(200, []byte("Hello"))
}
```
```
package controller

import (
	"context"
	"strconv"
	"strings"

	"icode.baidu.com/baidu/gdp/ghttp"

	"icode.baidu.com/baidu/personal/myapp/library/types"
	"icode.baidu.com/baidu/personal/myapp/model/service/calculator"
)

func Sum(ctx context.Context, req ghttp.Request) ghttp.Response {
	tmp := strings.Split(req.QueryDefault("ids", "0"), ",")
	var ids calculator.SumRequest
	for _, v := range tmp {
		id, err := strconv.Atoi(v)
		if err != nil {
			resp := &types.Response{
				ErrNo: 400,
				Msg:   err.Error(),
				Data:  nil,
			}
			return ghttp.NewJSONResponse(400, resp)
		}
		ids = append(ids, id)
	}

	ret, err := calculator.Sum(ctx, ids)
	if err != nil {
		resp := &types.Response{
			ErrNo: 500,
			Msg:   err.Error(),
			Data:  nil,
		}
		return ghttp.NewJSONResponse(400, resp)
	}

	resp := &types.Response{
		ErrNo: 0,
		Msg:   "success",
		Data:  ret,
	}
	return ghttp.NewJSONResponse(200, resp)
}
```
加法具体的实现在model/service/calculator/sum.go中

```
package calculator

import (
	"context"
	"time"
)

type SumRequest []int

type SumResult struct {
	Total int
}

// Sum 加法
func Sum(ctx context.Context, param SumRequest) (*SumResult, error) {
	// 模拟耗时
	time.Sleep(10 * time.Millisecond)

	// 检查 ctx 是否已被取消
	if err := ctx.Err(); err != nil {
		return nil, err
	}

	var total int
	for _, v := range param {
		total += v
	}
	return &SumResult{Total: total}, nil
}
```
测试2个接口

1、[http://localhost:8080/hello](http://localhost:8080/hello)

![](/personal-site-mvp/img/doc-placeholder.svg "")
2、[http://localhost:8080/cal/sum?ids=124,2](http://localhost:8080/cal/sum?ids=124,2)

正确格式

![](/personal-site-mvp/img/doc-placeholder.svg "")
错误格式

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 三、创建接口服务
### 1、结合mysql开发接口
#### 配置与初始化mysql
配置：

```
# Service的名字，必选
Name = "mysql_myapp"

## 各种自定义的参数，会以 Option 的方式放到 Servicer 中，全部非必选
# 连接超时
ConnTimeOut = 145
# 写数据超时
WriteTimeOut = 750
# 读数据超时
ReadTimeOut = 750
# 请求失败后的重试次数：总请求次数 = Retry + 1
Retry = 2

# 资源使用策略，非必选，默认使用 RoundRobin
# RoundRobin: 依次轮询
# Random 随机
[Strategy] 
Name="Random"
# 资源定位配置必须有且只有一项
# 资源定位：使用 BNS
[Resource.Manual]
[[Resource.Manual.default]]
Host = ""                     # 修改host
Port =                        # 修改port


[MySQL]
Username     = ""             # 修改user
Password     = ""             # 修改password
DBName       = ""             # 修改batabase
DBDriver     = "mysql"
MaxOpenPerIP = 5
MaxIdlePerIP = 5
ConnMaxLifeTime = 5000 # 单位 ms
SQLLogLen      =-1    # 打印sql内容，为0不打印，-1 为全部
SQLArgsLogLen  =-1    # 打印sql参数内容，为0不打印，-1 为全部
LogIDTransport = true # 是否sql注释传递logid
DSNParams ="charset=utf8&timeout=90s&collation=utf8mb4_unicode_ci&parseTime=true&loc=Asia%2FShanghai"
```
注：这里DSNParams的collation需要和数据表的排序规则一致，建议使用collation=utf8_unicode_ci

![](/personal-site-mvp/img/doc-placeholder.svg "")
初始化：

MustInit函数新增initMySQL初始化：

```
func MustInit(ctx context.Context) {
    // 其他初始化
    initMySQL(ctx) 
}

func initMySQL(_ context.Context) {
	// client 初始化为单例，放到 resource 里去
	resource.MySQLClientUser = mustInitOneMySQL("mysql_myapp")   // 与配置文件名一致
}
```
表信息:

```
CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '账户ID',
  `email` varchar(30) NOT NULL DEFAULT '' COMMENT '账户电子邮箱',
  `name` varchar(30) NOT NULL DEFAULT '' COMMENT '账户名称',
  `sex` tinyint(1) NOT NULL DEFAULT '0' COMMENT '性别 0.为止 1.男 2.女',
  `register_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '注册时间',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '账户状态 1.审核中 2.通过 3.未通过 4.失效',
  `created_at` datetime DEFAULT NULL COMMENT '创建时间',
  `updated_at` datetime DEFAULT NULL COMMENT '更新时间',
  `deleted_at` datetime DEFAULT NULL COMMENT '删除时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COMMENT='账户表';
```
#### **base 方式**
也是gdp官方默认的方式。

##### 接口开发
###### 注册路由
在httpRouter函数中新增initRouter(router)，新建initRouter函数并注册user业务 handler

```
import "icode.baidu.com/baidu/personal/myapp/servers/httpserver/controller/user"

func httpRouter(ser *ghttp.DefaultServer) ghttp.Router {
    // 省略
	initRouter(router)  // 新增
	return route
 }

// 新增
func initRouter(router ghttp.Router) {
	userController := user.NewUserController()
	router.HandleFunc("GET", "/api/getUser", userController.GetUser)
}
```
###### controller
```

package user

import (
	"context"
	"strconv"

	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/personal/myapp/library/types"
	"icode.baidu.com/baidu/personal/myapp/model/service/user"
)

type UserController struct {
	UserService *user.UserService
}

func NewUserController() *UserController {
	return &UserController{
		UserService: user.NewUserService(),
	}
}

func (c *UserController) GetUser(ctx context.Context, req ghttp.Request) ghttp.Response {
	idStr, _ := req.Query("id")
	id, err := strconv.ParseInt(idStr, 10, 64)
	if err != nil || id == 0 {
		return ghttp.NewJSONResponse(200, types.Response{
			ErrNo: 200,
			Msg:   "id参数错误",
			Data:  nil,
		})
	}
	res, err := c.UserService.GetInfoByID(ctx, id)
	if err != nil {
		return ghttp.NewJSONResponse(400, types.Response{
			ErrNo: 400,
			Msg:   "获取失败",
			Data:  nil,
		})
	}
	return ghttp.NewJSONResponse(200, types.Response{
		ErrNo: 0,
		Msg:   "success",
		Data:  res,
	})
}
```
###### service
```
package user

import (
	"context"

	"icode.baidu.com/baidu/personal/myapp/model/dao"
)

type UserService struct {
	UserDao *dao.UserDao
}

func NewUserService() *UserService {
	return &UserService{
		UserDao: dao.NewUserDao(),
	}
}

func (s *UserService) GetInfoByID(ctx context.Context, id int64) ([]dao.User, error) {
	return dao.NewUserDao().GetInfoByID(ctx, id)
}
```
###### dao
先复制官方提供的：[base.go](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/gdp/demo/blob/master/model/dao/base.go) 到model/dao/base.go作为依赖

创建user.go：

```
package dao

import (
	"context"
	"time"

	"icode.baidu.com/baidu/gdp/mysql"
	"icode.baidu.com/baidu/personal/myapp/library/resource"
)

type UserDao struct {
	BaseDBDao
}

func NewUserDao() *UserDao {
	return &UserDao{
		BaseDBDao{
			Table:  "users",
			Client: resource.MySQLClientUser,
		},
	}
}

type User struct {
	ID        int64     `ddb:"id" json:"id"`
	Email     string    `ddb:"email" json:"email"`
	Name      string    `ddb:"name" json:"name"`
	Sex       int       `ddb:"sex" json:"sex"`
	Status    int       `ddb:"status" json:"status"`
	CreatedAt time.Time `ddb:"created_at" json:"created_at"`
	UpdatedAt time.Time `ddb:"updated_at" json:"updated_at"`
	DeletedAt time.Time `ddb:"deleted_at" json:"deleted_at"`
}

func (dao *UserDao) GetInfoByID(ctx context.Context, id int64) ([]User, error) {
	where := map[string]any{
		"id":       id,
		"_orderby": "id desc",
	}
	condition := []string{"*"}
	data := []User{}
	err := dao.BaseSelectConvert(ctx, where, condition, &data)
	if err == nil && len(data) != 0 {
		return data, nil
	}
	return nil, err
}
```
##### 改动文件
```
.
├── bootstrap
│   └── bootstrap.go              // 初始化mysql
├── conf
│   └── servicer
│       └── mysql_myapp.toml      // mysql配置
├── model
│   ├── dao
│   │   ├── base.go              // 官方base
│   │   └── user.go              // dao
│   └── service
│       └── user
│           └── user.go          // service  大部分情况会直接将与mysql的交互写在用controller或者dao，不要service部分
├── servers
│   ├── httpserver
│   │   ├── controller
│   │   │   └── user
│   │   │       └── user.go      // controller
│   │   └── router.go            // router
```
##### 效果
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### **gorm 方式**
gorm_adapter 库提供了 gdp mysql 库对 Gorm 的适配封装。

##### 初始化gorm
MustInit函数新增initGorm初始化：

```
import "icode.baidu.com/baidu/gdp/gorm_adapter"

func MustInit(ctx context.Context) {
    // 其他初始化
    initMySQL(ctx)  // 与第一部分配置与初始化mysql相同
	initGorm(ctx)
}

func initGorm(_ context.Context) {
    var err error
    // 打印对应执行的 sql 语句
    cfg := &gorm.Config{
        SkipDefaultTransaction: true,
    }
    // 封装的 mysql client 已打印日志 如用户无自定义 logger 默认不输出 gorm 操作日志
    logger := logit.NewSimple(os.Stderr)
    // 初始化 gorm.Config
    opts := []gorm_adapter.Option{
        gorm_adapter.OptConfig(cfg),
        gorm_adapter.OptLogger(logger),
    }
    resource.OrmClientUser, err = gorm_adapter.NewGorm(resource.MySQLClientUser, opts...)
    if err != nil {
        panic(err.Error())
    }
}
```
library/resource/resource.go 新增 gorm 单例：

```
import "icode.baidu.com/baidu/gdp/gorm_adapter"

var OrmClientUser *gorm_adapter.GormDB
```
##### 接口开发
这次简洁一些，不要service部分，将与mysql的交互写dao，controller直接调用dao。

###### dao
默认结构名与表名一致，这里type Users对应users表，如果是mysql表名usr_info结构体就为UsrInfo

```
package dao

import (
	"context"
	"time"

	"icode.baidu.com/baidu/personal/myapp/library/resource"
)

type Users struct {
	ID        int64     `ddb:"id" json:"id"`
	Email     string    `ddb:"email" json:"email"`
	Name      string    `ddb:"name" json:"name"`
	Sex       int       `ddb:"sex" json:"sex"`
	Status    int       `ddb:"status" json:"status"`
	CreatedAt time.Time `ddb:"created_at" json:"created_at"`
	UpdatedAt time.Time `ddb:"updated_at" json:"updated_at"`
	DeletedAt time.Time `ddb:"deleted_at" json:"deleted_at"`
}

func GetUserByID(ctx context.Context, id int64) ([]Users, error) {
	var user []Users
	db := resource.OrmClientUser.WithContext(ctx)
	result := db.Where("id = ?", id).First(&user)
	if result.Error != nil {
		return nil, result.Error
	}
	return user, nil
}
```
###### controller
```
package user

import (
	"context"
	"strconv"

	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/personal/myapp/library/types"
	"icode.baidu.com/baidu/personal/myapp/model/dao"
)

func GetUserGorm(ctx context.Context, req ghttp.Request) ghttp.Response {
	idStr, _ := req.Query("id")
	id, err := strconv.ParseInt(idStr, 10, 64)
	if err != nil || id == 0 {
		return ghttp.NewJSONResponse(200, types.Response{
			ErrNo: 200,
			Msg:   "id参数错误",
			Data:  nil,
		})
	}
	res, err := dao.GetUserByID(ctx, id)
	if err != nil {
		return ghttp.NewJSONResponse(400, types.Response{
			ErrNo: 400,
			Msg:   err.Error(),
			Data:  nil,
		})
	}
	return ghttp.NewJSONResponse(200, types.Response{
		ErrNo: 0,
		Msg:   "success",
		Data:  res,
	})
}
```
###### 注册路由
这里有2种注册方式：直接注册与子路由注册，后者更符合模块化设计。

1、直接注册：

对应 get  /api/getUserGorm

```
import "icode.baidu.com/baidu/personal/myapp/servers/httpserver/controller/user"

func initRouter(router ghttp.Router) {
	// 其他路由
    
	// 1、直接注册
	router.HandleFunc("GET", "/api/getUserGorm", user.GetUserGorm)
	// 2、注册到user.Router
	// user.Router(router.Group("/api/user"))
}
```
2、注册到user.Router

对应 get  /api/user/getUserGorm

新建路由：

```
package user

import (
	"icode.baidu.com/baidu/gdp/ghttp"
)

func Router(router ghttp.Router) {
	router.HandleFunc("GET", "/getUserGorm", GetUserGorm)
}
```
注册：

```
import "icode.baidu.com/baidu/personal/myapp/servers/httpserver/controller/user"

func initRouter(router ghttp.Router) {
	// 其他路由
    
	// 1、直接注册
	// router.HandleFunc("GET", "/api/getUserGorm", user.GetUserGorm)
	// 2、注册到user.Router
	user.Router(router.Group("/api/user"))
}
```
##### 改动文件
```
.
├── bootstrap
│   └── bootstrap.go                  // 初始化mysql gorm
├── library
│   ├── resource
│   │   └── resource.go               // gorm单例
├── model
│   ├── dao
│   │   └── user_gorm.go              // dao
├── servers
│   ├── httpserver
│   │   ├── controller
│   │   │   └── user
│   │   │       ├── router.go         // user.Router   
│   │   │       └── user_gorm.go      // controller
│   │   └── router.go                 // router
```
##### 效果
![直接注册](/personal-site-mvp/img/doc-placeholder.svg "直接注册")
![注册到user.Router](/personal-site-mvp/img/doc-placeholder.svg "注册到user.Router")
### 2、结合redis开发接口
#### 配置与初始化redis
配置：

```
Name = "redis_my"

# ConnTimeOut = 1000
# WriteTimeOut = 1000
# ReadTimeOut = 1000
# Retry = 2

[Strategy] 
Name="RoundRobin"

[Resource.BNS]
BNSName = "group.bdrp-bdrp-common-test-v308-2-proxy.redis.all"

[Redis]
DB = 0
PoolSizePerIP = 10
MinIdleConnsPerIP = 5
```
初始化：

MustInit函数新增 initRedis 初始化：

```
func MustInit(ctx context.Context) {
    // 其他初始化
    initRedis(ctx) 
}

func initRedis(_ context.Context) {
	// client 初始化为单例，放到 resource 里去
	resource.RedisClient = mustInitOneRedis("redis_my")
}
```
library/resource/resource.go 新增 redis client 单例：

```
import "icode.baidu.com/baidu/gdp/redis"

// RedisClient  redis client 单例
var RedisClient redis.Client
```
#### 接口开发
只有一个控制器，包括功能设置值与取值

##### controller
```
package usercache

import (
	"context"
	"net/http"
	"time"

	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/gdp/redis"

	"icode.baidu.com/baidu/personal/myapp/library/resource"
	"icode.baidu.com/baidu/personal/myapp/library/types"
)

// SetInfo  设置redis 中的user 信息
func SetInfo(ctx context.Context, req ghttp.Request) ghttp.Response {
	response := &types.Response{
		ErrNo: 0,
		Msg:   "success",
	}
	data := map[string]any{}

	key := "test"
	val := "123"
	_, err := resource.RedisClient.Set(ctx, key, val, time.Minute).Result()
	if err != nil {
		response.ErrNo = 500
		response.Msg = err.Error()
		return ghttp.NewJSONResponse(http.StatusOK, response)
	}

	data["setResult"] = "success"
	response.Data = data

	return ghttp.NewJSONResponse(http.StatusOK, response)
}

// GetInfo 获取redis 中的user 信息
func GetInfo(ctx context.Context, req ghttp.Request) ghttp.Response {
	response := &types.Response{
		ErrNo: 0,
		Msg:   "success",
	}
	data := map[string]any{}

	key := "test"
	val, err := resource.RedisClient.Get(ctx, key).Result()
	if err != nil && err != redis.ErrNil {
		response.ErrNo = 500
		response.Msg = err.Error()
		return ghttp.NewJSONResponse(http.StatusOK, response)
	}

	data["key"] = key
	data["val"] = val
	response.Data = data
	return ghttp.NewJSONResponse(http.StatusOK, response)
}
```
##### 注册路由
```
router.HandleFunc("GET,POST", "/setinfo", usercache.SetInfo)
router.HandleFunc("GET", "/getinfo", usercache.GetInfo)
```
### 3、结合RAL开发接口
#### http接口开发
```
# Service的名字，必选
Name = "self_main"

ConnTimeOut = 100
WriteTimeOut = 200
ReadTimeOut = 750

Retry = 2

[Strategy]
Name="RoundRobin"

# 资源定位：手动配置 - 使用IP、端口
[Resource.Manual]
[[Resource.Manual.default]]
Host = "127.0.0.1"
Port = 8080
```
##### controller
调用已有的接口127.0.0.1:8080/chengfa、127.0.0.1:8080/sort 来实现功能

```
package controller

import (
	"context"
	"encoding/json"
	"net/http"
	"net/url"

	"icode.baidu.com/baidu/gdp/codec"
	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/gdp/net/ral"

	"icode.baidu.com/baidu/personal/myapp/library/types"
)

func HttpChengfa(ctx context.Context, req ghttp.Request) ghttp.Response {

	idsStr, has := req.Query("ids")
	if !has {
		response := &types.Response{
			ErrNo: 10001,
			Msg:   "ids is required",
		}
		return ghttp.NewJSONResponse(http.StatusOK, response)
	}
	query := url.Values{}
	query.Set("ids", idsStr)

	reqdata := &ghttp.RalRequest{
		Query:   query,
		Path:    "/chengfa",
		Method:  http.MethodGet,
		APIName: "self_main",
	}

	ret := &ChengfaResponse{}
	respdata := &ghttp.RalResponse{
		Data:    ret,
		Decoder: codec.JSONDecoder,
	}

	err := ral.RAL(ctx, "self_main", reqdata, respdata)

	if err != nil {
		response := &types.Response{
			ErrNo: 10002,
			Msg:   err.Error(),
		}
		return ghttp.NewJSONResponse(http.StatusOK, response)
	}

	return ghttp.NewJSONResponse(http.StatusOK, ret)
}

func HttpSort(ctx context.Context, req ghttp.Request) ghttp.Response {
	var sortReq SortReq
	decoder := json.NewDecoder(req.Body())
	if err := decoder.Decode(&sortReq); err != nil {
		response := &types.Response{
			ErrNo: 20001,
			Msg:   err.Error(),
		}
		return ghttp.NewJSONResponse(http.StatusOK, response)
	}

	reqdata := &ghttp.RalRequest{
		Path:    "/sort",
		Method:  http.MethodPost,
		APIName: "self_main",
	}

	if err := reqdata.WithBody(sortReq, codec.JSONEncoder); err != nil {
		response := &types.Response{
			ErrNo: 20002,
			Msg:   err.Error(),
		}
		return ghttp.NewJSONResponse(http.StatusOK, response)
	}

	ret := &SortResponse{}
	respdata := &ghttp.RalResponse{
		Data:    ret,
		Decoder: codec.JSONDecoder,
	}

	err := ral.RAL(ctx, "self_main", reqdata, respdata)
	if err != nil {
		response := &types.Response{
			ErrNo: 20003,
			Msg:   err.Error(),
		}
		return ghttp.NewJSONResponse(http.StatusOK, response)
	}

	return ghttp.NewJSONResponse(http.StatusOK, ret)
}

type ChengfaResponse struct {
	Msg   string
	ErrNo int
	Data  struct {
		Total int
	}
}

type SortReq struct {
	Mode  string `json:"mode"`
	Datas []int  `json:"datas"`
}

type SortResponse struct {
	Msg   string
	ErrNo int
	Data  []int
}
```
##### 注册路由
```
router.HandleFunc("GET", "/ral/http_chengfa", controller.HttpChengfa)
router.HandleFunc("POST", "/ral/http_sort", controller.HttpSort)
```
##### 效果
![ral_http_get](/personal-site-mvp/img/doc-placeholder.svg "ral_http_get")
![ral_http_post](/personal-site-mvp/img/doc-placeholder.svg "ral_http_post")
## 四、大模型生成gdp接口代码
接口生成：[大模型生成gdp接口代码](./gdp2框架使用&接口开发_引用文档/大模型生成gdp接口代码.md)

应用实践：[0808 商业团队 迁go产品交互](./gdp2框架使用&接口开发_引用文档/0808 商业团队 迁go产品交互.md)

|需求描述|模型生成|修改|
|-|-|-|
|生成以下接口：
[
    {
        "desc": "查询代码迁移信息列表",
        "api": "api/code_trans_info/list",
        "method": "get",
        "param": {
            "module_name": "string, 模块名, 可选",
            "url": "string, URL地址, 可选",
            "pn": "string, 页码, 可选, 默认为1",
            "perPage": "string, 每页数据量, 可选, 默认为10"
        },
        "response": {
            "status": "int, 状态码, 0表示成功",
            "msg": "string, 消息提示",
            "data": {
                "items": [
                    {
                        "id": "int, 自增ID",
                        "module_name": "string, 模块名",
                        "url": "string, URL地址",
                        "demand_desc": "string, 生成的需求描述",
                        "operator": "string, 操作人",
                        "update_time": "string, 更新时间",
                        "demand_status": "int, 需求状态(0待审核 1已审核)",
                        "is_deleted": "int, 是否删除(0未删除 1已删除)"
                    }
                ],
                "total": "int, 数据库中总数据量"
            }
        }
    },
    {
        "desc": "编辑代码迁移信息的需求描述",
        "api": "api/code_trans_info/edit",
        "method": "post",
        "param": {
            "id": "string, 自增ID, 必填",
            "demand_desc": "string, 生成的需求描述, 必填"
        },
        "response": {
            "status": "int, 状态码, 0表示成功",
            "msg": "string, 消息提示"
        }
    },
    {
        "desc": "删除代码迁移信息",
        "api": "api/code_trans_info/delete",
        "method": "post",
        "param": {
            "id": "string, 自增ID, 必填"
        },
        "response": {
            "status": "int, 状态码, 0表示成功",
            "msg": "string, 消息提示"
        }
    },
    {
        "desc": "获取模块名列表",
        "api": "api/code_trans_info/getModuleList",
        "method": "get",
        "param": {},
        "response": {
            "status": "int, 状态码, 0表示成功",
            "msg": "string, 消息提示",
            "data": [
                {
                    "module_name": "string, 模块名"
                }
            ]
        }
    },
    {
        "desc": "根据模块名获取URL列表",
        "api": "api/code_trans_info/getUrlListByModuleName",
        "method": "get",
        "param": {
            "module_name": "string, 模块名, 必填"
        },
        "response": {
            "status": "int, 状态码, 0表示成功",
            "msg": "string, 消息提示",
            "data": [
                {
                    "url": "string, URL地址"
                }
            ]
        }
    },
    {
        "desc": "获取提取的PHP代码",
        "api": "api/code_trans_info/getPhpCode",
        "method": "get",
        "param": {
            "id": "string, 自增ID, 必填"
        },
        "response": {
            "status": "int, 状态码, 0表示成功",
            "msg": "string, 消息提示",
            "data": "string, 提取的PHP代码"
        }
    },
    {
        "desc": "获取实际的Go代码",
        "api": "api/code_trans_info/getGoCode",
        "method": "get",
        "param": {
            "id": "string, 自增ID, 必填"
        },
        "response": {
            "status": "int, 状态码, 0表示成功",
            "msg": "string, 消息提示",
            "data": "string, 实际的Go代码"
        }
    }
]
CREATE TABLE `code_trans_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `module_name` varchar(100) NOT NULL DEFAULT '' COMMENT '模块名',
  `url` varchar(255) NOT NULL DEFAULT '' COMMENT 'URL地址',
  `php_code` text COMMENT '提取的PHP代码',
  `demand_desc` text COMMENT '生成的需求描述',
  `go_code` text COMMENT '实际的Go代码',
  `operator` varchar(50) NOT NULL DEFAULT '' COMMENT '操作人',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `demand_status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '需求状态(0待审核 1已审核)',
  `is_deleted` tinyint(1) DEFAULT '0' COMMENT '是否删除(0未删除 1已删除)',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='代码迁移信息表';
![](/personal-site-mvp/img/doc-placeholder.svg "")|1、文件路径├── model
│   ├── dao
│   │   └── code_trans_info.go  // dao层文件
└── servers
    └── httpserver
        ├── controller
        │   └── code_trans_info.go  // controller层文件
        └── router.go   // 注册路由2、路由注册代码 servers/httpserver/router.gopackage httpserver

import (
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/personal/myapp/servers/httpserver/controller"
)

func registerDemoAPI(router ghttp.Router) {
    // 路由注册代码
    router.HandleFunc("GET", "/api/code_trans_info/list", controller.ListCodeTransInfo)
    router.HandleFunc("POST", "/api/code_trans_info/edit", controller.EditCodeTransInfo)
    router.HandleFunc("POST", "/api/code_trans_info/delete", controller.DeleteCodeTransInfo)
    router.HandleFunc("GET", "/api/code_trans_info/getModuleList", controller.GetModuleList)
    router.HandleFunc("GET", "/api/code_trans_info/getUrlListByModuleName", controller.GetUrlListByModuleName)
    router.HandleFunc("GET", "/api/code_trans_info/getPhpCode", controller.GetPhpCode)
    router.HandleFunc("GET", "/api/code_trans_info/getGoCode", controller.GetGoCode)
}3、Controller层代码 servers/httpserver/controller/code_trans_info.gopackage controller

import (
    "context"
    "encoding/json"
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/personal/myapp/library/types"
    "icode.baidu.com/baidu/personal/myapp/model/dao"
)

// ListCodeTransInfo 查询代码迁移信息列表
func ListCodeTransInfo(ctx context.Context, req ghttp.Request) ghttp.Response {
    var params struct {
        ModuleName string `json:"module_name"`
        URL        string `json:"url"`
        Pn         string `json:"pn"`
        PerPage    string `json:"perPage"`
    }
    json.NewDecoder(req.Body()).Decode(&params)

    items, total, err := dao.ListCodeTransInfo(ctx, params.ModuleName, params.URL, params.Pn, params.PerPage)
    if err != nil {
        return ghttp.NewJSONResponse(500, types.Response{
            ErrNo: 500,
            Msg:   "Internal Server Error",
            Data:  nil,
        })
    }

    return ghttp.NewJSONResponse(200, types.Response{
        ErrNo: 200,
        Msg:   "success",
        Data: map[string]interface{}{
            "items": items,
            "total": total,
        },
    })
}

// EditCodeTransInfo 编辑代码迁移信息的需求描述
func EditCodeTransInfo(ctx context.Context, req ghttp.Request) ghttp.Response {
    var params struct {
        ID          string `json:"id"`
        DemandDesc  string `json:"demand_desc"`
    }
    json.NewDecoder(req.Body()).Decode(&params)

    err := dao.EditCodeTransInfo(ctx, params.ID, params.DemandDesc)
    if err != nil {
        return ghttp.NewJSONResponse(500, types.Response{
            ErrNo: 500,
            Msg:   "Internal Server Error",
            Data:  nil,
        })
    }

    return ghttp.NewJSONResponse(200, types.Response{
        ErrNo: 200,
        Msg:   "success",
        Data:  nil,
    })
}

// DeleteCodeTransInfo 删除代码迁移信息
func DeleteCodeTransInfo(ctx context.Context, req ghttp.Request) ghttp.Response {
    var params struct {
        ID string `json:"id"`
    }
    json.NewDecoder(req.Body()).Decode(&params)

    err := dao.DeleteCodeTransInfo(ctx, params.ID)
    if err != nil {
        return ghttp.NewJSONResponse(500, types.Response{
            ErrNo: 500,
            Msg:   "Internal Server Error",
            Data:  nil,
        })
    }

    return ghttp.NewJSONResponse(200, types.Response{
        ErrNo: 200,
        Msg:   "success",
        Data:  nil,
    })
}

// GetModuleList 获取模块名列表
func GetModuleList(ctx context.Context, req ghttp.Request) ghttp.Response {
    modules, err := dao.GetModuleList(ctx)
    if err != nil {
        return ghttp.NewJSONResponse(500, types.Response{
            ErrNo: 500,
            Msg:   "Internal Server Error",
            Data:  nil,
        })
    }

    return ghttp.NewJSONResponse(200, types.Response{
        ErrNo: 200,
        Msg:   "success",
        Data:  modules,
    })
}

// GetUrlListByModuleName 根据模块名获取URL列表
func GetUrlListByModuleName(ctx context.Context, req ghttp.Request) ghttp.Response {
    moduleName := req.QueryDefault("module_name", "")

    urls, err := dao.GetUrlListByModuleName(ctx, moduleName)
    if err != nil {
        return ghttp.NewJSONResponse(500, types.Response{
            ErrNo: 500,
            Msg:   "Internal Server Error",
            Data:  nil,
        })
    }

    return ghttp.NewJSONResponse(200, types.Response{
        ErrNo: 200,
        Msg:   "success",
        Data:  urls,
    })
}

// GetPhpCode 获取提取的PHP代码
func GetPhpCode(ctx context.Context, req ghttp.Request) ghttp.Response {
    id := req.QueryDefault("id", "")

    phpCode, err := dao.GetPhpCode(ctx, id)
    if err != nil {
        return ghttp.NewJSONResponse(500, types.Response{
            ErrNo: 500,
            Msg:   "Internal Server Error",
            Data:  nil,
        })
    }

    return ghttp.NewJSONResponse(200, types.Response{
        ErrNo: 200,
        Msg:   "success",
        Data:  phpCode,
    })
}

// GetGoCode 获取实际的Go代码
func GetGoCode(ctx context.Context, req ghttp.Request) ghttp.Response {
    id := req.QueryDefault("id", "")

    goCode, err := dao.GetGoCode(ctx, id)
    if err != nil {
        return ghttp.NewJSONResponse(500, types.Response{
            ErrNo: 500,
            Msg:   "Internal Server Error",
            Data:  nil,
        })
    }

    return ghttp.NewJSONResponse(200, types.Response{
        ErrNo: 200,
        Msg:   "success",
        Data:  goCode,
    })
}4、DAO层代码 model/dao/code_trans_info.gopackage dao

import (
    "context"
    "strconv"
    "icode.baidu.com/baidu/personal/myapp/library/resource"
    "gorm.io/gorm"
)

type CodeTransInfo struct {
    ID          int    `gorm:"column:id"`
    ModuleName  string `gorm:"column:module_name"`
    URL         string `gorm:"column:url"`
    PhpCode     string `gorm:"column:php_code"`
    DemandDesc  string `gorm:"column:demand_desc"`
    GoCode      string `gorm:"column:go_code"`
    Operator    string `gorm:"column:operator"`
    UpdateTime  string `gorm:"column:update_time"`
    DemandStatus int    `gorm:"column:demand_status"`
    IsDeleted   int    `gorm:"column:is_deleted"`
}

func (u *CodeTransInfo) TableName() string {
    return "code_trans_info"
}

// ListCodeTransInfo 查询代码迁移信息列表
func ListCodeTransInfo(ctx context.Context, moduleName, url, pn, perPage string) ([]CodeTransInfo, int, error) {
    db := resource.OrmClientUser.WithContext(ctx)

    var items []CodeTransInfo
    query := db.Model(&CodeTransInfo{})

    if moduleName != "" {
        query = query.Where("module_name = ?", moduleName)
    }
    if url != "" {
        query = query.Where("url = ?", url)
    }

    page, _ := strconv.Atoi(pn)
    if page == 0 {
        page = 1
    }
    pageSize, _ := strconv.Atoi(perPage)
    if pageSize == 0 {
        pageSize = 10
    }

    var total int64
    if err := query.Count(&total).Error; err != nil {
        return nil, 0, err
    }

    if err := query.Offset((page - 1) * pageSize).Limit(pageSize).Find(&items).Error; err != nil {
        return nil, 0, err
    }

    return items, int(total), nil
}

// EditCodeTransInfo 编辑代码迁移信息的需求描述
func EditCodeTransInfo(ctx context.Context, id, demandDesc string) error {
    db := resource.OrmClientUser.WithContext(ctx)

    intID, err := strconv.Atoi(id)
    if err != nil {
        return err
    }

    return db.Model(&CodeTransInfo{}).Where("id = ?", intID).Update("demand_desc", demandDesc).Error
}

// DeleteCodeTransInfo 删除代码迁移信息
func DeleteCodeTransInfo(ctx context.Context, id string) error {
    db := resource.OrmClientUser.WithContext(ctx)

    intID, err := strconv.Atoi(id)
    if err != nil {
        return err
    }

    return db.Model(&CodeTransInfo{}).Where("id = ?", intID).Update("is_deleted", 1).Error
}

// GetModuleList 获取模块名列表
func GetModuleList(ctx context.Context) ([]string, error) {
    db := resource.OrmClientUser.WithContext(ctx)

    var modules []string
    if err := db.Model(&CodeTransInfo{}).Distinct("module_name").Pluck("module_name", &modules).Error; err != nil {
        return nil, err
    }

    return modules, nil
}

// GetUrlListByModuleName 根据模块名获取URL列表
func GetUrlListByModuleName(ctx context.Context, moduleName string) ([]string, error) {
    db := resource.OrmClientUser.WithContext(ctx)

    var urls []string
    if err := db.Model(&CodeTransInfo{}).Where("module_name = ?", moduleName).Pluck("url", &urls).Error; err != nil {
        return nil, err
    }

    return urls, nil
}

// GetPhpCode 获取提取的PHP代码
func GetPhpCode(ctx context.Context, id string) (string, error) {
    db := resource.OrmClientUser.WithContext(ctx)

    var codeTransInfo CodeTransInfo
    intID, err := strconv.Atoi(id)
    if err != nil {
        return "", err
    }

    if err := db.Where("id = ?", intID).First(&codeTransInfo).Error; err != nil {
        return "", err
    }

    return codeTransInfo.PhpCode, nil
}

// GetGoCode 获取实际的Go代码
func GetGoCode(ctx context.Context, id string) (string, error) {
    db := resource.OrmClientUser.WithContext(ctx)

    var codeTransInfo CodeTransInfo
    intID, err := strconv.Atoi(id)
    if err != nil {
        return "", err
    }

    if err := db.Where("id = ?", intID).First(&codeTransInfo).Error; err != nil {
        return "", err
    }

    return codeTransInfo.GoCode, nil
}|编码规范：未使用的库在粘贴保存后，icoding会自动删去未使用库功能：查询条件中忽略了已删除模块和空模块|




