---
title: "service"
description: "import \"strings\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\service.md"
---
## service层代码，文件路径：`model/service/包名/功能名.go`
* 此文件中结构体根据功能进行命名
* 注意service层`BeforeExec`方法中的参数校验、常用参数校验步骤必须按照给出示例内容完整生成
```go
package 包名


import (
	"strings"
	
    "icode.baidu.com/baidu/gdp/logit"
	libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/ierrno"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/ua"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/service"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uts"
)

// TestFuncParams 参数结构体
type TestFuncParams struct {
    TestId int64 `json:"testId" form:"testId"`  // 测试ID
    TestCUID string `json:"testCuid" form:"testCuid"`  // 测试CUID
    TestVersion int64 `json:"testVersion" form:"testVersion"`  // 测试版本号
    UtsParams uts.RequestUTS 
}

// TestResp 返回结构体
type TestResp struct {
    TestKey string `form:"testKey" json:"testKey"` // 测试Key
}

// TestFuncService ...
type TestFuncService struct {
	*service.BaseService
	Params    *TestFuncParams
}

// NewTestFuncService ...
func NewTestFuncService() ibase.ExecLogicInterface {
	instance := new(TestFuncService)
	return instance
}

// 业务逻辑入口函数，示例如下：
// Exec _
func (tfs *TestFuncService) Exec(ctx *ibase.APIContext) interface{} {
    // 调用data层对应定义的方法获取数据，示例如下：
    testFuncData := 包名.NewTestFuncData(ctx, tfs.params.TestId, tfs.params.TestCUID)
    testFunc, err := testFuncData.GetTestFunc(tfs.params.TestVersion)
    if testFunc == nil || err != nil {
        // service执行方法出错时，错误码为ierrno.ErrorServerError
		return ierrno.ErrorServerError
	}
	
    // 后续数据处理逻辑的完整实现
    // ...
}


// BeforeExec方法，包含参数校验等步骤的完整实现，示例如下：
// BeforeExec ...
func (tfs *TestFuncService) BeforeExec(ctx *ibase.APIContext) error {
    // 1. 参数校验
    params := &TestFuncParams{}
	if err := util.ShoudBind(ctx.HTTPRequest(), params); err != nil {
		return ierrno.ErrorParam
	}
	
    // 2. 常用参数校验步骤，按照以下参数校验内容完整生成：
    params.CUID = tfs.GetCUID(ctx)
	if tfs.Params.CUID == "" {
		logit.AddNotice(ctx, logit.String("cuid-params-invalid", strl.Params.CUID))
		return ierrno.ErrorParam
	}
    params.ProductID = tfs.GetProductID(ctx)
	if _, ok := libConsts.DuoduoProductMap[params.ProductID]; !ok {
		return ierrno.ErrorParam
	}
    passport := tfs.GetUserInfo(ctx)
	if passport != nil && passport.UID != 0 {
		params.UID = passport.UID
	}
	uaStr := tfs.GetUA(ctx)
	version := ua.GetAppVersion(params.ProductID, uaStr)
	if len(version) > 0 {
		params.Version = version
	}
	
	// 3. 参数绑定：
    tfs.Params.utsParams = &uts.RequestUTS{
		// ...根据需求描述生成需要用到的参数绑定逻辑
	}
    tfs.params = params
    return nil
}
```
* 一些已经封装的方法参考如下（参考方法无需生成，调用即可，注意方法名要保持一致）
1. util文件中的方法
```go
func ShoudBind(r *http.Request, obj interface{}) error
```
2. ua文件中的常用方法
```go
func IsAndroid(uaStr string) bool
func GetAppVersion(productID int, uaStr string) string
// ...
```
3. service文件中基类的常用方法
```go
func (bs *BaseService) GetAllParams(ctx *ibase.APIContext) map[string]interface{}
func (bs *BaseService) GetProductID(ctx *ibase.APIContext) int
func (bs *BaseService) GetProductAppName(ctx *ibase.APIContext) string
func (bs *BaseService) GetUserInfo(ctx *ibase.APIContext) *passport.SessionUserInfo
func (bs *BaseService) GetCUID(ctx *ibase.APIContext, findQuery ...bool) string
func (bs *BaseService) GetSID(ctx *ibase.APIContext) string
func (bs *BaseService) GetUA(ctx *ibase.APIContext) string
// ...
```