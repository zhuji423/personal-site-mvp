---
title: "service"
description: "import \"context\" \"icode.baidu.com/baidu/gdp/ghttp\" \"icode.baidu.com/baidu/searchbox/ugact/library/errno\" \"icode.baidu.co"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\service.md"
---
### service层根目录路径：`baidu/searchbox/ugact/service/包名/`
#### service构造函数定义，文件路径：`service/包名/constructor.go`
* 注意此文件无需生成注释
```go
package 包名

import (
    "context"
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/searchbox/ugact/library/errno"
    "icode.baidu.com/baidu/searchbox/sboxlib/extension/httputil"
    "icode.baidu.com/baidu/searchbox/ugact/library/render"
    "icode.baidu.com/baidu/searchbox/ugact/service/包名"
    "icode.baidu.com/baidu/searchbox/ugact/service/包名/types"
)

// Controller ...
type Controller struct {
    // 引用相关service层
    srv *包名.Service
}

// NewController ...
func NewController() *Controller {
    return &Controller{
        // service层初始化
        srv: 包名.NewService(),
    }
}

// TestFunc 入口函数
func (ctl *Controller) TestFunc(ctx context.Context, request ghttp.Request) ghttp.Response {
    // 从types包获取对应的请求变量
    TestReq := new(types.TestReq)
    // 校验参数的合法性
    if err := httputil.ShouldBindWith(request, TestReq); err != nil {
        return render.Fail(ctx, errno.RewriteMsg(errno.ErrInvalidParams, err.Error()))
    }
    // 调用service层的逻辑处理函数
    resp, err := ctl.srv.TestFunc(ctx, TestReq)
    if err != nil {
        return render.Fail(ctx, err)
    }

    return render.Success(ctx, resp)
}
```
#### service接口定义，文件路径：`service/包名/contract.go`
* 注意此文件无需生成注释
```go
package 包名

import (
    "context"
    "icode.baidu.com/baidu/searchbox/ugact/service/包名/types"
)

type IService interface {
    TestFunc(ctx context.Context, req *TestReq) (res *TestRes, err error) 
}
```
#### service接口逻辑实现，文件路径：`service/包名/功能名.go`
* 注意参考需求描述中的入参、出参的类型和结构，保证接口输入、输出数据格式和需求描述保持一致
* 涉及gcp相关的数据获取操作，直接在service层中实现
* service层调用data层封装好的数据获取方法获取数据，实现后续数据处理逻辑
```go
import (
    "context"
    "fmt"
    
    "icode.baidu.com/baidu/searchbox/ugact/library/errno"
    "icode.baidu.com/baidu/searchbox/ugact/library/logger"
    "icode.baidu.com/baidu/searchbox/ugact/library/constant"
    
    "icode.baidu.com/baidu/searchbox/ugact/service/包名/data/功能名"
    "icode.baidu.com/baidu/searchbox/ugact/service/包名/types"
    
    // 若涉及到数据并行获取，需导入GDP的gtask包
    "icode.baidu.com/baidu/gdp/extension/gtask"
    
    // 若需要解析接口传入cookie参数，需引用对应包
    params "icode.baidu.com/baidu/searchbox/symframe-param"

    // 若涉及到gcp，导入gcp包
    "icode.baidu.com/baidu/searchbox/ugact/library/gcp"
)

// 示例
// TestFunc ...
func (s *Service) TestFunc(ctx context.Context, req *types.TestReq) (*types.TestRsp, error) {
    // 若需要解析传入公共参数，示例如下：
    // adaption, _ := params.LoadAdaption(ctx)

    // 若存在数据并行获取，逻辑框架示例如下：
    // wg := gtask.Group{AllowSomeFail: true}
    // testTaskData := &types.TestTaskData{}
    // wg.Go(func() error {
    //     res, err := s.testData.方法名(ctx, req)
    //     if err != nil {
    //         logger.WarningF(ctx, "error message err: +%v", err)
    //         return err
    //     }
    //     if res != nil {
    //         testTaskData = res
    //     }
    //     return nil
    // } 
    // ...
    // _, err := wg.Wait()
    // if err != nil {
    //     return nil, fmt.Errorf("error message err: +%v", errno.ErrTest)
    // }
    
    // 若涉及gcp数据获取，示例如下：
    // testGcpConf, err := gcp.Fetch[[]int](ctx, constant.testGcpAppId, constant.testGcpKey)
    // if err != nil {
    //     logger.WarningF(ctx, "error message err: +%v", err)
    //     return nil, err
    // }
    
    // 若涉及mysql，采用data层封装好的方法mysql数据获取方法获取数据，示例如下：
    // testSqlData, err := s.testData.TestSqlData(ctx, req)
    // if err != nil {
    //     logger.WarningF(ctx, "error message err: +%v", err)
    //     return nil, err
    // }
        
    // ...
}
```