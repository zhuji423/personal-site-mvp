---
title: "edit-go-gamecenter"
description: "你是一个 go 服务端开发工程师，你正在开发一个游戏中心业务，下面是一个上报游戏数据接口的全部代码："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\eval\\code_gen\\prompt\\edit-go-gamecenter.md"
---
你是一个 go 服务端开发工程师，你正在开发一个游戏中心业务，下面是一个上报游戏数据接口的全部代码：

## 文件： `servers/httpserver/router/service.go`
```go
package router

import (
	"net/http"

	"icode.baidu.com/baidu/gdp/ghttp"

	pubUser "icode.baidu.com/baidu/searchbox/ug-gamecenter/servers/httpserver/controller/pub/user"
)

// 外部业务
func RegisterPubAPI(router ghttp.Router) {
	// 用户部分
	userRouter := router.Group("/user")
	userRouter.HandleFunc(http.MethodPost, "/gameReport", pubUser.GameReport) // 上报用户游戏数据
}
```

## 文件：`servers/httpserver/controller/pub/user/game_report.go`
```go
package user

import (
    "context"
    "net/url"
    "strconv"
    "time"

    "icode.baidu.com/baidu/gdp/conf"
    "icode.baidu.com/baidu/gdp/extension/gtask"
    "icode.baidu.com/baidu/gdp/extension/safely"
    "icode.baidu.com/baidu/gdp/ghttp"

    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/config"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/parse"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/render"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/tools"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/tools/gks"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/utils"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts"
    srvConsts "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts/srv"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/service/task"
    userSrv "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/service/user"
    taskDTO "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/dto/task"
    userDTO "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/dto/user"
    typesReq "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/request/pub/user"
)

// GameReport 游戏上报
// 当前暂未验证ak与gk关系，后期如果需要应补充
func GameReport(ctx context.Context, req ghttp.Request) ghttp.Response {
    // check params
    params, err := gameReportParams(ctx, req)
    if err != nil {
        return render.Fail(ctx, err)
    }
    // appname
    if params.AppName != "" && utils.IsAllowApp(params.AppName) {
        // 公参设置。注意此处因为仅有宿主信息，所以固定了端信息，都会是安卓
        tools.SetAppName(ctx, params.AppName)
    }
    // main
    err = userSrv.NewPlatformGame().Report(ctx, req, params)

    // 异步处理任务
    go safely.RunVoid(func() {
        gameReportHandleTask(utils.NewCtx(ctx), req, params)
    })

    if err != nil {
        return render.Fail(ctx, err)
    }

    return render.Success(ctx, nil)
}

// gameReportParams 游戏信息上报，校验并获取参数
func gameReportParams(ctx context.Context, req ghttp.Request) (*userDTO.GameReportParams, error) {
    // validate
    reqParams, err := gameReportParamsValidate(ctx, req)
    if err != nil {
        return nil, err
    }

    return gameReportParamsConvert(reqParams), nil
}

// gameReportParamsValidate 请求参数校验&获取
func gameReportParamsValidate(ctx context.Context, req ghttp.Request) (*typesReq.GameReportReq, error) {
    // req
    reqParams := &typesReq.GameReportReq{}
    if err := parse.ShouldBind(req, reqParams); err != nil {
        logger.WarningF(ctx, "bind params error, err=%v", err)
        return nil, errno.UserPlatformGameReportReqParamsErr
    }
    if reqParams.AppName != nil && utils.IsDenyApp(*reqParams.AppName) {
        logger.WarningF(ctx, "bind params error, appname not allow, appname=%v", *reqParams.AppName)
        return nil, errno.UserPlatformGameReportReqParamsErr
    }

    // sk
    var pConf config.Platform
    if err := conf.Parse(config.TomlPlatform, &pConf); err != nil {
        logger.WarningF(ctx, "conf parse error, err=%v", err)
        return nil, errno.UserPlatformGameReportErr
    }
    sk := pConf.Keys.SecretKey(reqParams.AppKey)
    if sk == "" {
        logger.WarningF(ctx, "ak invalid, sk not exists")
        return nil, errno.UserPlatformGameReportAppKeyInvalid
    }
    // ts offset
    timeOffset := time.Now().Unix() - reqParams.Timestamp
    if timeOffset > consts.RequestSignTimestampExpire || timeOffset < 0 {
        logger.WarningF(ctx, "timestamp invalid, not in allow range")
        return nil, errno.UserPlatformGameReportTimestampInvalid
    }
    // sign
    signData := url.Values{}
    signData.Add(srvConsts.PlatformGameReportFieldAppKey, reqParams.AppKey)
    signData.Add(srvConsts.PlatformGameReportFieldTimestamp, strconv.FormatInt(reqParams.Timestamp, 10))
    signData.Add(srvConsts.PlatformGameReportFieldGameKey, reqParams.GameKey)
    signData.Add(srvConsts.PlatformGameReportFieldUserKey, reqParams.UserKey)
    signData.Add(srvConsts.PlatformGameReportFieldAction, reqParams.Action)
    signData.Add(srvConsts.PlatformGameReportFieldData, utils.JSONStr(reqParams.Data))
    signData.Add(srvConsts.PlatformGameReportFieldSecretKey, sk)
    if reqParams.Test != nil {
        signData.Add(srvConsts.PlatformGameReportFieldTest, strconv.Itoa(*reqParams.Test))
    }
    if reqParams.AppName != nil {
        signData.Add(srvConsts.PlatformGameReportFieldAppName, *reqParams.AppName)
    }
    if !tools.ValidatePlatformSign(signData, reqParams.Sign) {
        logger.WarningF(ctx, "sign invalid, not match, signData=%v reqParams=%v", signData, utils.JSONStr(reqParams))
        return nil, errno.UserPlatformGameReportSignInvalid
    }
    // gk
    gid := gks.GK2ID(reqParams.GameKey)
    if gid == 0 {
        logger.WarningF(ctx, "params error, gid invalid, gk=%v", reqParams.GameKey)
        return nil, errno.UserPlatformGameReportGameKeyInvalid
    }
    tools.LogSetGame(ctx, gid)

    return reqParams, nil
}

// gameReportParamsConvert 转换为处理用的参数
func gameReportParamsConvert(reqParams *typesReq.GameReportReq) *userDTO.GameReportParams {
    params := &userDTO.GameReportParams{
        AppKey:    reqParams.AppKey,
        Timestamp: reqParams.Timestamp,
        Sign:      reqParams.Sign,
        GameKey:   reqParams.GameKey,
        GID:       gks.GK2ID(reqParams.GameKey),
        UserKey:   reqParams.UserKey,
        Action:    reqParams.Action,
        Data: &userDTO.GameReportParamsData{
            User: reqParams.Data.User,
        },
    }
    if reqParams.Test != nil {
        params.Test = *reqParams.Test
    }
    if reqParams.AppName != nil {
        params.AppName = *reqParams.AppName
    }
    if reqParams.Data.Level != nil {
        params.Data.Level = reqParams.Data.Level
    }
    if reqParams.Data.VIPLevel != nil {
        params.Data.VIPLevel = reqParams.Data.VIPLevel
    }
    if reqParams.Data.Score != nil {
        params.Data.Score = reqParams.Data.Score
    }

    return params
}

// gameReportHandleTask 游戏信息上报处理任务
func gameReportHandleTask(ctx context.Context, req ghttp.Request, params *userDTO.GameReportParams) {
    gt := gtask.Group{
        AllowSomeFail: true,
    }

    gt.Go(func() error {
        if err := gameReportHandleGameActTask(ctx, req, params); err != nil {
            logger.WarningF(ctx, "GameReport.gameReportHandleGameActTask error, err=%v", err)
        }
        return nil
    })

    gt.Go(func() error {
        if err := gameReportHandleGameExciteTask(ctx, req, params); err != nil {
            logger.WarningF(ctx, "GameReport.gameReportHandleGameExciteTask error, err=%v", err)
        }
        return nil
    })

    _ = gt.WaitErr()
}

// gameReportHandleGameActTask 处理游戏行为上报
func gameReportHandleGameActTask(ctx context.Context, req ghttp.Request, params *userDTO.GameReportParams) error {
    taskSrv, err := task.NewTaskSrv(srvConsts.TaskIDGameAct)
    if err != nil {
        // 任务不存在，返回
        return nil
    }
    _, err = taskSrv.Complete(ctx, &taskDTO.TaskCompleteParam{GameReportParams: params}, req)
    return err
}

// gameReportHandleGameExciteTask 处理游戏激励任务
func gameReportHandleGameExciteTask(ctx context.Context, req ghttp.Request, params *userDTO.GameReportParams) error {
    taskSrv, err := task.NewTaskSrv(srvConsts.TaskIDGameExcite)
    if err != nil {
        // 任务不存在，返回
        return nil
    }
    _, err = taskSrv.Complete(ctx, &taskDTO.TaskCompleteParam{GameReportParams: params}, req)
    return err
}

// gameReportParams 游戏信息上报，校验并获取参数
func gameReportParams(ctx context.Context, req ghttp.Request) (*userDTO.GameReportParams, error) {
    // validate
    reqParams, err := gameReportParamsValidate(ctx, req)
    if err != nil {
        return nil, err
    }

    return gameReportParamsConvert(reqParams), nil
}

// gameReportParamsValidate 请求参数校验&获取
func gameReportParamsValidate(ctx context.Context, req ghttp.Request) (*typesReq.GameReportReq, error) {
    // req
    reqParams := &typesReq.GameReportReq{}
    if err := parse.ShouldBind(req, reqParams); err != nil {
        logger.WarningF(ctx, "bind params error, err=%v", err)
        return nil, errno.UserPlatformGameReportReqParamsErr
    }
    if reqParams.AppName != nil && utils.IsDenyApp(*reqParams.AppName) {
        logger.WarningF(ctx, "bind params error, appname not allow, appname=%v", *reqParams.AppName)
        return nil, errno.UserPlatformGameReportReqParamsErr
    }

    // sk
    var pConf config.Platform
    if err := conf.Parse(config.TomlPlatform, &pConf); err != nil {
        logger.WarningF(ctx, "conf parse error, err=%v", err)
        return nil, errno.UserPlatformGameReportErr
    }
    sk := pConf.Keys.SecretKey(reqParams.AppKey)
    if sk == "" {
        logger.WarningF(ctx, "ak invalid, sk not exists")
        return nil, errno.UserPlatformGameReportAppKeyInvalid
    }
    // ts offset
    timeOffset := time.Now().Unix() - reqParams.Timestamp
    if timeOffset > consts.RequestSignTimestampExpire || timeOffset < 0 {
        logger.WarningF(ctx, "timestamp invalid, not in allow range")
        return nil, errno.UserPlatformGameReportTimestampInvalid
    }
    // sign
    signData := url.Values{}
    signData.Add(srvConsts.PlatformGameReportFieldAppKey, reqParams.AppKey)
    signData.Add(srvConsts.PlatformGameReportFieldTimestamp, strconv.FormatInt(reqParams.Timestamp, 10))
    signData.Add(srvConsts.PlatformGameReportFieldGameKey, reqParams.GameKey)
    signData.Add(srvConsts.PlatformGameReportFieldUserKey, reqParams.UserKey)
    signData.Add(srvConsts.PlatformGameReportFieldAction, reqParams.Action)
    signData.Add(srvConsts.PlatformGameReportFieldData, utils.JSONStr(reqParams.Data))
    signData.Add(srvConsts.PlatformGameReportFieldSecretKey, sk)
    if reqParams.Test != nil {
        signData.Add(srvConsts.PlatformGameReportFieldTest, strconv.Itoa(*reqParams.Test))
    }
    if reqParams.AppName != nil {
        signData.Add(srvConsts.PlatformGameReportFieldAppName, *reqParams.AppName)
    }
    if !tools.ValidatePlatformSign(signData, reqParams.Sign) {
        logger.WarningF(ctx, "sign invalid, not match, signData=%v reqParams=%v", signData, utils.JSONStr(reqParams))
        return nil, errno.UserPlatformGameReportSignInvalid
    }
    // gk
    gid := gks.GK2ID(reqParams.GameKey)
    if gid == 0 {
        logger.WarningF(ctx, "params error, gid invalid, gk=%v", reqParams.GameKey)
        return nil, errno.UserPlatformGameReportGameKeyInvalid
    }
    tools.LogSetGame(ctx, gid)

    return reqParams, nil
}

// gameReportParamsConvert 转换为处理用的参数
func gameReportParamsConvert(reqParams *typesReq.GameReportReq) *userDTO.GameReportParams {
    params := &userDTO.GameReportParams{
        AppKey:    reqParams.AppKey,
        Timestamp: reqParams.Timestamp,
        Sign:      reqParams.Sign,
        GameKey:   reqParams.GameKey,
        GID:       gks.GK2ID(reqParams.GameKey),
        UserKey:   reqParams.UserKey,
        Action:    reqParams.Action,
        Data: &userDTO.GameReportParamsData{
            User: reqParams.Data.User,
        },
    }
    if reqParams.Test != nil {
        params.Test = *reqParams.Test
    }
    if reqParams.AppName != nil {
        params.AppName = *reqParams.AppName
    }
    if reqParams.Data.Level != nil {
        params.Data.Level = reqParams.Data.Level
    }
    if reqParams.Data.VIPLevel != nil {
        params.Data.VIPLevel = reqParams.Data.VIPLevel
    }
    if reqParams.Data.Score != nil {
        params.Data.Score = reqParams.Data.Score
    }

    return params
}
```

## 文件：`model/service/user/platform_game.go`
```go
package user

import (
    "context"
    "errors"
    "strconv"

    "icode.baidu.com/baidu/gdp/ghttp"

    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/errno"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/logger/extlog"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/tools"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/tools/guks"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/library/utils"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts"
    srvConsts "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/consts/srv"
    gameData "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/data/game"
    userDTO "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/dto/user"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/pb"
)

// PlatformGame 厂商游戏信息
type PlatformGame interface {
    // Report 上报信息
    Report(ctx context.Context, req ghttp.Request, params *userDTO.GameReportParams) error
}

// platformGame impl
type platformGame struct{}

// NewPlatformGame .
func NewPlatformGame() PlatformGame {
    return &platformGame{}
}

// Report 上报信息
// 后续可本地缓存游戏数据，减少redis查询
// 后续有稳定性保障可入队列&重试处理
func (p *platformGame) Report(ctx context.Context, req ghttp.Request, params *userDTO.GameReportParams) error {
    // validation
    if params == nil {
        // 请求参数错误
        logger.ErrWF(ctx, errno.UserPlatformGameReportHandleParamsErr, "platformGame.Report error, params is nil")
        return errno.UserPlatformGameReportHandleParamsErr
    }

    // 测试请求，后续执行直接忽略
    if params.Test == 1 {
        extlog.InfoF(ctx, "req is test ignore")
        return nil
    }

    // 游戏信息查询
    gi := gameData.NewGameInfo()
    gInfo, err := gi.One(ctx, params.GID)
    if err != nil || gInfo == nil {
        if !errors.Is(err, errno.DataNotFound) {
            logger.ErrWF(ctx, errno.UserPlatformGameReportGameInfoGetErr, "platformGame.Report error, game get error, params=%v err=%v", params, err)
            return errno.UserPlatformGameReportGameInfoGetErr
        }
        // 游戏查询错误
        return errno.UserPlatformGameReportGameInvalid
    }

    if gInfo.State != srvConsts.GameStateOnline {
        // 游戏状态错误，当前失效无法处理
        logger.ErrWF(ctx, errno.UserPlatformGameReportGameInvalid, "platformGame.Report error, game invalid, state not online, params=%v", params)
        return errno.UserPlatformGameReportGameInvalid
    }

    uid := guks.NewGUIDUK(uint64(gInfo.Platform)).UK2UID(params.UserKey)
    if uid < 1 {
        // 用户信息错误，无法正确解析用户
        logger.ErrWF(ctx, errno.UserPlatformGameReportUserInvalid, "platformGame.Report error, user invalid, params=%v", params)
        return errno.UserPlatformGameReportUserInvalid
    }
    params.UID = int64(uid)

    // 上报后业务处理
    _ = p.reportHandle(ctx, req, params)

    return nil
}

// reportHandle 上报后业务处理
func (p *platformGame) reportHandle(ctx context.Context, req ghttp.Request, params *userDTO.GameReportParams) error {
    extlog.InfoF(ctx, "platformGame.reportHandle, params=%v", utils.JSONStr(params))

    // PB 打点，内部有错误记录
    p.reportPB(ctx, params)

    return nil
}

// reportPB 上报数据到PB
func (p *platformGame) reportPB(ctx context.Context, params *userDTO.GameReportParams) {
    extPlatformGame := &pb.ExtPlatformGame{
        UID:        params.UID,
        GameKey:    params.GameKey,
        GID:        params.GID,
        GameUser:   params.Data.User,
        GameAction: params.Action,
    }
    if params.Data.Level != nil {
        gameLevel := strconv.Itoa(*params.Data.Level)
        extPlatformGame.GameLevel = &gameLevel
    }
    if params.Data.VIPLevel != nil {
        gameVIPLevel := strconv.Itoa(*params.Data.VIPLevel)
        extPlatformGame.GameVIPLevel = &gameVIPLevel
    }
    if params.Data.Score != nil {
        gameScore := strconv.FormatInt(*params.Data.Score, 10)
        extPlatformGame.GameScore = &gameScore
    }

    pbInfo := &pb.LogParams{
        ID:   consts.PBID,
        Page: consts.PbPagePlatformGame,
        Ext:  extPlatformGame,
    }
    err := tools.AppendActionData(ctx, pbInfo)
    if err != nil {
        logger.ErrWF(ctx, errno.PBRecordErr, "completeCertifyPB err, pbInfo=%v err=%v", utils.JSONStr(pbInfo), err)
    }
}
```

## 文件：`model/types/dto/user/platform_game_report.go`
```go
package user

// GameReportParams 用户游戏请求
type GameReportParams struct {
    AppKey    string                // 产品标识
    Timestamp int64                 // 时间戳（秒）
    Sign      string                // 签名
    Test      int                   // 是否为测试数据，测试数据则会丢弃处理&不记录。
    GameKey   string                // 游戏标识
    GID       int64                 // 游戏ID
    UserKey   string                // 用户标识
    Action    string                // 事件类型
    AppName   string                // 端信息 baiduboxlite baiduboxapp
    Data      *GameReportParamsData // 数据详情

    UID int64 // uid
}

// GameReportParamsData 用户游戏请求数据详情
type GameReportParamsData struct {
    User     string   // 游戏角色标识，可能会是uk
    Level    *int     // 当前等级/关卡
    VIPLevel *int     // VIP等级
    Score    *int64   // 战力、综合评分等
}
```

## 文件：`model/types/request/pub/user/platform_game_report.go`
```go
package user

// GameReportReq 用户游戏请求
type GameReportReq struct {
	AppKey    string             `json:"ak" binding:"required"`     // 产品标识
	Timestamp int64              `json:"ts" binding:"required"`     // 时间戳（秒）
	Sign      string             `json:"sign" binding:"required"`   // 签名
	Test      *int               `json:"test,omitempty"`            // 是否为测试数据，测试数据则会丢弃处理&不记录。
	UserKey   string             `json:"uk" binding:"required"`     // 用户标识
	GameKey   string             `json:"gk" binding:"required"`     // 游戏标识
	Action    string             `json:"action" binding:"required"` // 事件类型
	AppName   *string            `json:"appname,omitempty"`         // 端信息
	Data      *GameReportReqData `json:"data" binding:"required"`   // 数据详情
}

// GameReportReqData 用户游戏请求数据详情
type GameReportReqData struct {
	User     string  `json:"user" binding:"required"` // 游戏角色标识，可能会是uk
	Level    *int    `json:"level,omitempty"`         // 当前等级/关卡
	VIPLevel *int    `json:"vipLevel,omitempty"`      // VIP等级-关卡等级
	Score    *int64  `json:"score,omitempty"`         // 战力、综合评分等
}
```

请根据上面的接口代码内容，并参考当前项目代码风格，进行接下来的开发任务，要求：
1. 请求参数的Data字段中新增可选字段rules，是由逗号连接的多个规则组成的字符串
2. 将传入的rules字符串解析为规则列表(字符串数组)，按照分隔符分割字符串，并且进行去重、删空处理，
3. 日志记录转换后的参数
请输出你修改的代码：