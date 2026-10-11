---
title: "edit-go-piggybank-receive-middle"
description: "你是一个 go 服务端开发工程师，你正在开发一个存钱罐业务，下面是一个上滑红包领取接口的全部代码："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\eval\\code_gen\\prompt\\edit-go-piggybank-receive-middle.md"
---
你是一个 go 服务端开发工程师，你正在开发一个存钱罐业务，下面是一个上滑红包领取接口的全部代码：

## 文件： `model/service/redpacket/receive.go`

```go
package redpacket

import (
    "encoding/json"
    "fmt"
    "strings"
    "time"

    "github.com/spf13/cast"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/common"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/logpoint"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/task"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/userdata"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/withdraw"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/ugauth"

    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/gdp/logit"
    libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ierrno"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/pblog"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/resource"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/store/redis"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ua"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
    dataConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/types"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/service"
    thirdUAnti "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uanti"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uts"
)
type SlideRedPacket struct {
    RewardType   string `json:"rewardType"`
    Reward       string `json:"reward"`
    RemainReward string `json:"remainReward"`
    PayType      int    `json:"payType"`
}

func (rs *ReceiveService) receiveSmallFPacket(ctx *ibase.APIContext, userInfo *userdata.UserInfo, receiveNum int, userRedPacket *types.UserRedPacket, receiveRedPacket *types.RedPacket, res *ReceiveResponse) (err error) {
    uid := rs.params.UID
    productID := rs.params.ProductID
    //反作弊
    openid := ""
    if receiveRedPacket.PayType == dataConsts.PayTypeStatusWeChat {
        openid, _ = ugauth.GetUgAuthInfo(ctx, productID, uid, dataConsts.UgChannelWeChat)
    }
    extMap := map[string]interface{}{
        "task_type":     thirdUAnti.TypeRedEnvelope,
        "envelope_type": "account",
        "openid":        openid,
    }
    if !rs.IsSafeReceive(ctx, receiveRedPacket.Reward, extMap) {
        return ierrno.ErrorUAnti
    }

    moneyOperation, err := common.InitMoneyOperation(ctx, userInfo.UID, productID)
    if err != nil {
        return ierrno.ErrorServerError
    }
    addRes, err := moneyOperation.AddMoneyRecord(userInfo.Period, receiveRedPacket.Reward, dataConsts.MoneyTypePayRedPacket, receiveRedPacket.PayType, true, time.Now(), nil, nil)
    if !addRes {
        logit.AddNotice(ctx, logit.String("AddMoneyRecord-error", "1"))
        return ierrno.ErrorServerError
    }
    if err != nil {
        logit.AddNotice(ctx, logit.String("AddMoneyRecord-fail", err.Error()))
        return ierrno.ErrorServerError
    }

    //清理缓存
    err = rs.newPerson.DelRedPacketsCache(userInfo.Period)
    if err != nil {
        logit.AddNotice(ctx, logit.Error("DelRedPacketsCache", err))
        return ierrno.ErrorServerError
    }

    //处理提现逻辑
    withdrawData := withdraw.NewWithdrawData(ctx, productID)
    firstRes := &FRedPacket{
        Number:     receiveNum,
        RewardType: receiveRedPacket.RewardType,
        Reward:     util.FenToYuanNew(receiveRedPacket.Reward, 2, false),
        Type:       dataConsts.MoneyMapToRedPacketType[receiveRedPacket.MoneyType],
        LeftNum:    len(userRedPacket.FirstRedPacket) - receiveNum,
    }

    assetInfo, _ := rs.userData.GetUserAssetInfo(uid, productID)
    if assetInfo == nil {
        assetInfo = &common.UserAssetAPP{}
    }
    res.Asset = util.FenToYuanNew(assetInfo.DisplayMoneyInt, 2, false)
    res.AssetType = "money"
    firstRes.PayType = dataConsts.PayTypeStatusUCenter
    logit.AddNotice(ctx, logit.String("redPacket_reward", fmt.Sprintf("scene:%s,pay_type:%v", rs.params.Scene, receiveRedPacket.PayType)))

    //...
    //微信打款
    // 或者存钱罐新用户首日且绑定过微信的情况下  也直接打款的微信
    if receiveRedPacket.PayType == dataConsts.PayTypeStatusWeChat {
        // 针对用户首日创建，兜底判断打款金额是否满足最少0.1元
        if receiveRedPacket.Reward < 10 {
            receiveRedPacket.Reward = 10
        }
        res.IsWechatpay = true
        withdrawRes, withdrawErr := withdrawData.WeChatRealTimeWithdraw(userInfo, rs.params.CUID, receiveRedPacket.Reward, dataConsts.MoneyTypePayRedPacket)
        logit.AddNotice(ctx, logit.String("realTime_withdraw_res", fmt.Sprintf("res:%v,err:%v", withdrawRes, withdrawErr)))
        // 新手红包微信打款的原因日志埋点
        logpoint.UserWechatRedpacketReason(ctx, userInfo)
        if withdrawErr == nil && withdrawRes == dataConsts.RealTimeWithdrawSuccess {
            firstRes.PayType = dataConsts.PayTypeStatusWeChat
            res.First = firstRes
            logit.AddNotice(ctx, logit.String("payType", fmt.Sprintf("type_%d_aftet_%d", receiveRedPacket.PayType, firstRes.PayType)))
            userLevel := rs.userData.GetUserLevelByUtsCache(rs.params.UID)
            pblog.Prize(ctx, rs.params.UID, rs.params.CUID, rs.params.ProductID, userInfo.IsFirstDayUser(), receiveRedPacket.Reward, receiveRedPacket.RewardType, receiveRedPacket.MoneyType, dataConsts.PayTypeStatusWeChat, assetInfo.DisplayMoneyInt, assetInfo.DisplayCoin, userLevel)
            return
        }
    }

    //资产中心打款
    assetInfo.DisplayMoneyInt = assetInfo.DisplayMoneyInt + receiveRedPacket.Reward
    logit.AddNotice(ctx, logit.String("SmallWithdrawPrize", "1"))
    //走资产中心
    //兜底和其他情况下
    var isSend bool
    isSend, err = withdrawData.SmallWithdrawPrize(userInfo.UID, receiveRedPacket.Reward, dataConsts.MoneyTypePayRedPacket)
    if err != nil || !isSend {
        logit.AddNotice(ctx, logit.String("rewardType", "error"))
        return ierrno.ErrorServerError
    }
    res.First = firstRes
    userLevel := rs.userData.GetUserLevelByUtsCache(rs.params.UID)
    pblog.Prize(ctx, rs.params.UID, rs.params.CUID, rs.params.ProductID, userInfo.IsFirstDayUser(), receiveRedPacket.Reward, receiveRedPacket.RewardType, receiveRedPacket.MoneyType, dataConsts.PayTypeStatusUCenter, assetInfo.DisplayMoneyInt, assetInfo.DisplayCoin, userLevel)
    return
}

```

## 文件： `hirdparty/uanti/type.go`

```go
package uanti

const (
    //TypeRedEnvelope 领红包场景
    TypeRedEnvelope = "red_envelope"

    // TypeSign 7天签到
    TypeSign = "sign"

    // TypeExchange 兑换
    TypeExchange = "exchange"

    // TypeWithdraw 提现
    TypeWithdraw = "withdraw"

    //TypePageEnter 首页反作弊
    TypePageEnter = "page_enter"

    // TypeSynchronize 同步数据
    TypeSynchronize = "duoduosynchronize"

    // TypeVideoTaskCard 视频任务卡片
    TypeVideoTaskCard = "videoTaskCard"

    // TypeWealthDuration 时长
    TypeWealthDuration = "wealthDuration"
)

```


## 文件： `library/util/util.go`

```go

// FenToYuanNew 分转换为元,removeZeor 是否去除小数点后面的0  true 去除， false不去除
func FenToYuanNew(money int64, position int, removeZeor bool) string {

	res := "0"
	fMoney := float64(money)
	if money > 9999999 {
		// 返回万元，默认展示
		res = FloatFormatToString(fMoney/10000000.0, position, true)
		if removeZeor {
			res = strings.TrimRight(res, "0")
			res = strings.TrimRight(res, ".")
		}
		res = res + "万"
	} else {

		res = FloatFormatToString(fMoney/100.0, position, true)
		if removeZeor {
			res = strings.TrimRight(res, "0")
			res = strings.TrimRight(res, ".")
		}
	}
	return res
}

```

## 文件：'model/data/task/task_payment.go'


```go
package task

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"

	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/smaple"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/taskguide"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/userdata"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/withdraw"

	"github.com/spf13/cast"
	"icode.baidu.com/baidu/gdp/env"
	"icode.baidu.com/baidu/gdp/logit"
	libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/ierrno"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/mis"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/pblog"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/resource"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/store/redis"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/ua"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/common"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
	dataConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/types"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/task"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/ugauth"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uts"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uts/utsresponses"
)

// PaymentTask 微信组件任务
type PaymentTask struct {
	*baseTask
	info      *consts.TaskInfoResp
	gTaskInfo *task.Info
	IRedis    *redis.IRedis
	utsID     string
	sidCommon *common.SIDCommon
	cache     *common.LTCacheData
}

// PaymentTaskRecord 任务记录
type PaymentTaskRecord struct {
	*consts.BaseTaskRecord
	RewardList []*types.PaymentRewardNode `json:"node_list"` // 刷视频到钱包奖励列表，当天所有需要出的奖励
}

// taskGuide 上下滑挂件新增任务引导
type taskGuide struct {
	IsHit   string `json:"isHit"`    // 1： 命中实验；0：未命中实验
	Type    string `json:"type"`     // 挂件类型：签到：sigin、喝水：drinkWater、跳转任务面板：taskPanel
	Text    string `json:"text"`     // 挂件文案
	IconURL string `json:"icon_url"` // 挂件图标
	Scheme  string `json:"scheme"`   // 跳转scheme地址
	TaskID  string `json:"taskId"`   // 跳转任务面板的任务ID
}

// NewPaymentTaskObj new func for TasRegistryData
func NewPaymentTaskObj(ctx *ibase.APIContext, uid uint64, cuid string, productID int) *PaymentTask {
	cache := common.NewLTCacheData(ctx)
	taskListConf, err := cache.GetAllTaskConfByApp(productID)
	if err != nil || taskListConf == nil {
		return nil
	}
	//目前只有lite
	taskConf, ok := taskListConf[dataConsts.LitePaymentTaskID]
	if !ok {
		return nil
	}
	obj := &PaymentTask{
		baseTask:  newBaseTask(ctx, taskConf, uid, cuid, productID),
		info:      new(consts.TaskInfoResp),
		sidCommon: common.NewSIDCommon(ctx),
		IRedis:    redis.InitIRedis(ctx, resource.RedisClient),
		cache:     common.NewLTCacheData(ctx),
	}
	obj.utsID = strconv.Itoa(taskConf.TaskID)
	if taskConf.TaskInfo.SceneID != "" && taskConf.TaskInfo.SceneID != "0" {
		obj.utsID = taskConf.TaskInfo.SceneID
	}
	return obj
}

// NewPaymentTask new func for TaskRedPacket
func NewPaymentTask(ctx *ibase.APIContext, conf *mis.TaskInfo, uid uint64, cuid string, productID int) ITaskType {
	obj := &PaymentTask{
		baseTask:  newBaseTask(ctx, conf, uid, cuid, productID),
		info:      new(consts.TaskInfoResp),
		sidCommon: common.NewSIDCommon(ctx),
		IRedis:    redis.InitIRedis(ctx, resource.RedisClient),
		cache:     common.NewLTCacheData(ctx),
	}
	obj.utsID = strconv.Itoa(conf.TaskID)
	if conf.TaskInfo.SceneID != "" && conf.TaskInfo.SceneID != "0" {
		obj.utsID = conf.TaskInfo.SceneID
	}
	return obj
}

// GetListTaskInfo ...  任务面板里面的任务列表
func (pt *PaymentTask) GetListTaskInfo(taskInfoData *consts.TaskInfoData, gtInfo *task.Info, data2 *uts.ResData) (*consts.TaskInfoResp, error) {
	taskStatus, err := pt.GetTaskStatus(taskInfoData.UTSParams)
	if err != nil {
		return nil, err
	}
	if taskStatus.TotalTimes == 0 {
		return nil, nil
	}
	record, err := pt.GetTaskRecord()
	if err != nil || record == nil {
		return nil, err
	}
	if record.TaskStatus == consts.TaskStatusReceived {
		taskStatus.TaskStatus = consts.TaskStatusReceived
	}
	info := pt.GetBaseTaskInfo(gtInfo, taskStatus, taskInfoData.Platform, taskInfoData.DdScene)
	info.SubTitle = util.ReplaceTpl(info.SubTitle, map[string]interface{}{
		"totalTimes":     taskStatus.TotalTimes,
		"completedTimes": taskStatus.CompletedTimes,
	})
	info.SubTitleReplace = pt.GetReplceText()
	return info, nil
}

// TaskReceive 领取任务奖励 任务面板里面的任务领取奖励
func (pt *PaymentTask) TaskReceive(utsParams *uts.RequestUTS) (interface{}, error) {
	taskStatus, err := pt.GetTaskStatus(utsParams)
	if err != nil {
		return nil, ierrno.ErrorTaskReceiveFail
	}
	if taskStatus.TotalTimes == 0 {
		return nil, ierrno.ErrorTaskReceiveFail
	}
	if taskStatus.TaskStatus != consts.TaskStatusCompleted {
		return nil, ierrno.ErrorTaskNotComplete
	}

	// 初始化用户信息
	userData := userdata.NewUserInfoData(pt.Ctx, pt.ProductID)
	userInfo, err := userData.GetUserInfo(pt.UID)
	if err != nil || userInfo == nil { //初始化失败，不展示多多视频
		return nil, ierrno.ErrorTaskReceiveFail
	}

	record, err := pt.GetTaskRecord()
	if err != nil {
		return nil, err
	}
	if record == nil {
		record = &PaymentTaskRecord{
			BaseTaskRecord: consts.NewBaseTaskRecord(),
		}
	}
	if record.TaskStatus == consts.TaskStatusReceived {
		return nil, ierrno.ErrorTaskNotComplete
	}

	rewardInfo := &consts.TaskReward{
		RewardNum:  int64(pt.Conf.TaskInfo.RewardNum),
		RewardType: pt.Conf.TaskInfo.RewardType,
	}
	//	需要添加特定参数，改成调用本对象方法（从BaseTask的公共方法GetRewardForUTS copy改造）
	utsRewardInfo, err := pt.GetRewardFromUTS(utsParams, pt.utsID, userInfo)
	if err == nil && utsRewardInfo != nil {
		rewardInfo = utsRewardInfo
	}
	record.TaskStatus = consts.TaskStatusReceived
	_ = pt.SetTaskRecordForUIDByTaskID(record)
	err = pt.AddRewards(userInfo.Period, rewardInfo)
	if err != nil {
		return nil, errors.New("receive reward fail")
	}
	coin := rewardInfo.RewardNum
	money := int64(0)
	if rewardInfo.RewardType == libConsts.RewardTypeMoney {
		coin = 0
		money = rewardInfo.RewardNum
	}
	return map[string]any{
		"coin":  coin,
		"money": money,
	}, nil
}

// GetRewardFromUTS ...
func (pt *PaymentTask) GetRewardFromUTS(utsParams *uts.RequestUTS, sceneID string, userInfo *userdata.UserInfo) (*consts.TaskReward, error) {
	if pt.Conf.TaskInfo.IsUTS {

		//	获取当前签到周期的资产提现阈值
		expireThresholdFen, err := TryGetThreshold(pt.Ctx, pt.ProductID, pt.UID)
		if err != nil {
			logit.AddNotice(pt.Ctx, logit.Error("DoExpireMoney-TryGetThreshold-failed", err))
			return nil, err
		}

		if utsParams.SenceInfo == nil {
			utsParams.SenceInfo = make(map[string]*uts.TypeInfo)
		}
		utsParams.SenceInfo[sceneID] = &uts.TypeInfo{
			VActDay:           userInfo.VActDay,
			VActDayV2:         userInfo.VActDayV2,
			VActSignThreshold: int(expireThresholdFen),
		}
		// 领取奖励，请求策略
		u := uts.NewUTS(pt.Ctx, pt.ProductID)
		utsResp, err := u.RequestUTS(pt.UID, pt.CUID, utsParams)
		if err != nil || utsResp == nil {
			// 请求策略失败，下发兜底奖励
			logit.AddNotice(pt.Ctx, logit.Error("requestUTS-failed", err))
			return nil, err
		}
		utsReward, ok := utsResp.SceneRewardList[sceneID]
		if ok && utsReward.VideoActivityExt != nil && len(utsReward.VideoActivityExt.RewardList) > 0 && utsReward.VideoActivityExt.RewardList[0] != nil {
			utsRewardInfo := utsReward.VideoActivityExt.RewardList[0]

			rewardNum := utsRewardInfo.Value
			if err == nil && rewardNum > 0 {
				rewardType := libConsts.RewardTypeCoin
				if utsRewardInfo.ValueType == utsresponses.UTSRewardTypeMoney {
					rewardType = libConsts.RewardTypeMoney
				}
				return &consts.TaskReward{
					RewardNum:  rewardNum,
					RewardType: rewardType,
				}, nil
			}
		}
	}
	return nil, nil
}

// DoRegister ... 冷启app 外部激活
func (pt *PaymentTask) DoRegister(data *consts.TaskRegisterData, requestUTS *uts.RequestUTS) (interface{}, error) {
	res := &types.PaymentDuration{
		Status: consts.PaymentStatusDefault,
		IsDone: consts.PaymentDoneStatusIng,
	}
	//check版本
	if !pt.Check(requestUTS) {
		return res, nil
	}
	userData := userdata.NewUserInfoData(pt.Ctx, pt.ProductID)
	//请求策略判断是否为目标用户
	targetUserInfo, err := userData.GetTargetUser(pt.UID)
	if !targetUserInfo.IsTargetUser() || err != nil { //非目标用户
		logit.AddNotice(pt.Ctx, logit.String("isTargetUser", "0"))
		return res, nil
	}

	res.Status = consts.PaymentStatusHit
	if pt.UID <= 0 {
		res.IsDone = consts.PaymentDoneStatusEnd //不能使用需求功能
		return res, nil
	}
	// 初始化用户信息
	userInfo, err := userData.GetUserInfo(pt.UID)
	if err != nil || userInfo == nil { //初始化失败，不展示多多视频
		logit.AddNotice(pt.Ctx, logit.Error("userInfo-empty", err))
		res.Status = consts.PaymentStatusDefault
		return res, nil
	}

	register := data.Register
	taskID := data.TaskID
	sys := data.Sys
	utsRewardList, _ := pt.GetPaymentList(requestUTS)
	if utsRewardList == nil || len(utsRewardList.RewardList) == 0 {
		logit.AddNotice(pt.Ctx, logit.String("utsRewardList", "empty"))
		res.Status = consts.PaymentStatusDefault
		res.IsDone = consts.PaymentDoneStatusEnd
		return res, nil
	}

	//抽离公共处理逻辑
	pt.processRegisterRepsData(utsRewardList, requestUTS, userInfo, res)

	// res.NextAuto = pt.processNextAuto(utsRewardList)
	// res.WidgetToast = pt.processWidgetToast(utsRewardList)
	// 实验已经下线，去掉相关逻辑
	res.NextAuto = false
	res.WidgetToast = nil

	if res.IsDone == consts.PaymentDoneStatusEnd || res.Status == consts.PaymentStatusDefault {
		logit.AddNotice(pt.Ctx, logit.String("done", res.IsDone))
		return res, nil
	}
	if util.Interface2Int(register) != 1 {
		return res, nil
	}
	callbackID := 2057
	if env.RunModeDebug == env.RunMode() || env.RunModeTest == env.RunMode() {
		callbackID = 2059
	}
	obj, _ := task.NewTask(pt.ProductID)
	ext := map[string]interface{}{
		"productid":   pt.ProductID,
		"id":          taskID,
		"source":      libConsts.ProductID2Source[pt.ProductID],
		"device_type": sys,
		"pv":          requestUTS.Pv,
		"ip":          requestUTS.IP,
		"version":     requestUTS.Version,
		"platform":    ua.Platform2Int(requestUTS.Platform),
		"callbackId":  callbackID, //微信小额打款计时器
	}
	// 测试环境回调，配置超时时间为5秒
	ext = pt.callbackConf(ext)

	r, err := obj.Register(pt.Ctx, taskID, pt.UID, pt.CUID, ext, nil, nil, nil)
	if err != nil {
		logit.AddNotice(pt.Ctx, logit.String("TaskRegisterErr", fmt.Sprintf("err:%s", err.Error())))
		return nil, errors.New("register failed")
	}
	if r.Errno == 11006 {
		logit.AddNotice(pt.Ctx, logit.String("TaskRegisterErr", r.Errmsg))
		return nil, errors.New("register failed")
	}
	if r.Errno != 0 {
		return nil, errors.New(strconv.Itoa(r.Errno) + ":" + r.Errmsg)
	}

	res.ActID = util.Interface2String(taskID)
	res.IsDone = util.Interface2String(res.IsDone)
	res.ActionConf = r.Data["actionConf"]
	res.Scheme = r.Data["scheme"]
	res.Tkey = r.Data["tkey"]
	res.URL = r.Data["url"]
	res.ActionType = r.Data["actionType"]
	res.Ext = r.Data["ext"]
	res.Token = r.Data["token"]
	pblog.TaskClkPBLog(pt.Ctx, pt.ProductID, pt.UID, pt.CUID, userInfo.IsFirstDayUser(), taskID, pt.Conf.Title, "other", userData.GetUserLevelByUtsCache(pt.UID))
	return res, nil
}

func (pt *PaymentTask) processWidgetToast(utsRewardList *PaymentTaskRecord) *types.WidgetClickToast {
	if utsRewardList == nil || len(utsRewardList.RewardList) <= 0 {
		return nil
	}

	// 判断实验命中
	expHit := smaple.
		NewUserSampleData(pt.Ctx, &smaple.UserSampleDataParams{ProductID: pt.ProductID}).
		HitPaymentCoinProgressOpt()
	if !expHit {
		return nil
	}

	// 判断场景命中：下一个奖励为金豆并且后续存在现金奖励
	nextCoin, err1 := pt.RewardNextCoin(utsRewardList)
	moneyExists, nextSlide, err2 := pt.UCRewardExistsByRecord(utsRewardList)
	moneyExistedCnts, err3 := pt.UCRewardExistedCnt(utsRewardList)
	if err1 == nil && err2 == nil && err3 == nil && nextCoin && moneyExists {
		return pt.genWidgetToast(true, nextSlide, moneyExistedCnts)
	}

	// 命中实验但未生效的场景，保持线上一致表现
	return pt.genWidgetToast(false, 0, 0)
}

func (pt *PaymentTask) genWidgetToast(hitScene bool, nextMoneyStep, moneyTimesLeft int) *types.WidgetClickToast {
	toast := &types.WidgetClickToast{
		HitToastOptExp: true, // 命中实验

		// 线上默认值
		Title:            "看视频赚现金",
		ContentIcon:      "https://b.bdstatic.com/searchbox/file/cmsuploader/20230216/1676519956360442.png",
		Subtitle:         "今天还有!(left)笔奖励",
		ButtonText:       "继续看视频赚钱",
		ContentLeftText:  "上滑!(text)次",
		ContentRightText: "再上滑!(text)次",
	}

	toast.HitToastOptScene = hitScene
	toast.NextMoneyStep = nextMoneyStep
	toast.MoneyTimesLeft = moneyTimesLeft
	if hitScene {
		toast.SubtitleNew = "今天还有!(left)笔奖励，!(moneyTimesLeft)笔现金可领取"
	}

	return toast
}

func (pt *PaymentTask) processNextAuto(utsRewardList *PaymentTaskRecord) bool {
	autoRewardNodeNum := []int{1}

	//判断用户是否命中实验
	expHit := smaple.
		NewUserSampleData(pt.Ctx, &smaple.UserSampleDataParams{ProductID: pt.ProductID}).
		IsPaymentAutoReward()
	if !expHit {
		return false
	}

	_, competedTimes, _ := pt.calcProgress(utsRewardList)
	nextNodeNum := competedTimes + 1

	for _, num := range autoRewardNodeNum {
		if num == nextNodeNum {
			return true
		}
	}

	return false
}

func (pt *PaymentTask) callbackConf(ext map[string]any) map[string]any {
	// 测试环境回调，配置超时时间为5秒
	if env.RunModeDebug == env.RunMode() || env.RunModeTest == env.RunMode() {
		delete(ext, "callbackId")
		hostname := "http://" + util.GetLocalhostNameAndPort()
		callback := map[string]any{
			"method":       "GET",
			"server":       hostname,
			"path":         "/video/external/task/paymentComplete",
			"connTimeOut":  5000,
			"writeTimeOut": 5000,
			"readTimeOut":  5000,
		}
		cbStr, _ := json.Marshal(callback)
		ext["callbackConf"] = string(cbStr)
	}
	return ext
}

// DoComplete 计时器完成流程
func (pt *PaymentTask) DoComplete(data *consts.TaskCompleteData, requestUTS *uts.RequestUTS) (interface{}, error) {
	userData := userdata.NewUserInfoData(pt.Ctx, pt.ProductID)
	if pt.UID <= 0 {
		logit.AddNotice(pt.Ctx, logit.String("isUnLoginTargetUser", "0"))
		return nil, ierrno.ErrorServerError
	}

	userInfo, err := userData.GetExitUserInfo(pt.UID) //初始化用户信息
	if err != nil || userInfo == nil {
		logit.AddNotice(pt.Ctx, logit.Error("getUserInfo", err))
		return nil, ierrno.ErrorServerError
	}

	utsRewardList, _ := pt.GetPaymentList(requestUTS)
	if utsRewardList == nil || len(utsRewardList.RewardList) <= 0 {
		logit.AddNotice(pt.Ctx, logit.String("utsRewardList", "empty"))
		return nil, ierrno.ErrorTaskCompleteFail
	}

	userAssetInfo, err := userData.GetUserAssetInfo(pt.UID, pt.ProductID)
	if err != nil || userAssetInfo == nil {
		logit.AddNotice(pt.Ctx, logit.Error("GetUserAssetInfo-Error", err))
		return nil, ierrno.ErrorServerError
	}
	displayMoneyInt := userAssetInfo.DisplayMoneyInt
	paymentRewardNode, err := pt.getRewardInfo(utsRewardList)
	if err != nil || paymentRewardNode == nil {
		logit.AddNotice(pt.Ctx, logit.Error("getRewardInfo-Error", err))
		return nil, ierrno.ErrorIntranetTaskComplete
	}
	competedTimes := utsRewardList.TaskCompetedTimes
	totalTimes := len(utsRewardList.RewardList)
	if competedTimes > totalTimes { //再次校验
		logit.AddNotice(pt.Ctx, logit.String("intranetTaskComplete", "1"))
		return nil, ierrno.ErrorIntranetTaskComplete
	}
	tplData, err := pt.processTplData(data, requestUTS, utsRewardList, userInfo, userAssetInfo)
	if err != nil {
		return nil, ierrno.ErrorTaskCompleteFail
	}
	payType := paymentRewardNode.PayType
	var sceneType int
	sceneType, err = pt.ReceiveReward(userInfo, utsRewardList)
	if err != nil {
		logit.AddNotice(pt.Ctx, logit.Error("receiveReward-failed", err))
		return nil, ierrno.ErrorServerError
	}

	//	在奖励领取之后计算后续奖励情况（因为此时cache中的times已经+1）
	widgetToast := pt.processWidgetToast(utsRewardList)
	if widgetToast != nil && widgetToast.HitToastOptExp {
		tplData["hitToastOptExp"] = cast.ToString(widgetToast.HitToastOptExp)
		tplData["hitToastOptScene"] = cast.ToString(widgetToast.HitToastOptScene)

		tplData["subtitleNew"] = widgetToast.SubtitleNew
		tplData["nextMoneyStep"] = cast.ToString(widgetToast.NextMoneyStep)
		tplData["moneyTimesLeft"] = cast.ToString(widgetToast.MoneyTimesLeft)
	}

	res := map[string]string{"tplData": util.ToString(tplData)}
	coin := int64(0)
	num := int64(0)
	if tplData["reward_type"] == libConsts.RewardTypeCoin {
		coin = cast.ToInt64(tplData["reward"])
	} else {
		num = cast.ToInt64(tplData["reward"])
	}
	userLevel := userData.GetUserLevelByUtsCache(pt.UID)
	pblog.Prize(pt.Ctx, pt.UID, pt.CUID, pt.ProductID, userInfo.IsFirstDayUser(), cast.ToInt64(tplData["reward"]), tplData["reward_type"], sceneType, payType, displayMoneyInt, userAssetInfo.DisplayCoin, userLevel)
	pblog.TaskDonePBLog(pt.Ctx, pt.ProductID, pt.UID, pt.CUID, userInfo.IsFirstDayUser(), pt.Conf.TaskID, pt.Conf.Title, "other", coin, num, userLevel)
	logit.AddNotice(pt.Ctx, logit.String("complete-suc", "1"))
	return res, nil
}

// GetPaymentList 获取策略数据
func (pt *PaymentTask) GetPaymentList(utsParams *uts.RequestUTS) (utsRewardList *PaymentTaskRecord, err error) {
	if pt.UID <= 0 {
		return nil, err
	}
	utsRewardList, err = pt.GetPaymentListFromCache()
	if err != nil {
		return nil, err
	}
	if utsRewardList != nil {
		return utsRewardList, nil
	}

	utsRewardList = pt.GetRewardByUts(utsParams)

	if utsRewardList != nil {
		err = pt.SetTaskRecordForUIDByTaskID(utsRewardList)
	}
	return
}

// GetPaymentListFromCache ...
func (pt *PaymentTask) GetPaymentListFromCache() (utsRewardList *PaymentTaskRecord, err error) {
	utsRewardList, err = pt.GetTaskRecord()
	if err != nil {
		logit.AddNotice(pt.Ctx, logit.Error("getRewardData-err", err))
		return nil, err
	}
	return utsRewardList, nil
}

// GetTaskRecord 获取任务记录
func (pt *PaymentTask) GetTaskRecord() (record *PaymentTaskRecord, err error) {
	//登录情况下数据
	record = &PaymentTaskRecord{
		BaseTaskRecord: consts.NewBaseTaskRecord(),
	}
	err = pt.GetTaskRecordForUIDByTaskID(record)
	if err != nil && err != consts.ErrNotfoundTaskRecordByUID {
		logit.AddNotice(pt.Ctx, logit.Error("GetTaskRecord", err))
		return nil, nil
	}
	if len(record.RewardList) <= 0 {
		return nil, nil
	}
	return record, nil
}

// GetTaskStatus ...
func (pt *PaymentTask) GetTaskStatus(utsParams *uts.RequestUTS) (*consts.TaskStatus, error) {
	if !pt.Conf.IsValid { //任务开关关闭
		logit.AddNotice(pt.Ctx, logit.String("IsValid", "0"))
		return nil, nil
	}
	utsRewardList, err := pt.GetTaskRecord()
	if utsRewardList == nil || err != nil {
		logit.AddNotice(pt.Ctx, logit.String("rewardData", "empty"))
		return nil, err
	}
	taskStatus := consts.TaskStatusRegistered //未完成
	if utsRewardList.TaskTotalTimes <= utsRewardList.TaskCompetedTimes {
		taskStatus = consts.TaskStatusCompleted //已完成
	}
	return &consts.TaskStatus{
		TotalTimes:     utsRewardList.TaskTotalTimes,
		CompletedTimes: utsRewardList.TaskCompetedTimes,
		TaskStatus:     taskStatus,
	}, nil
}

// NoteListIsLastReceive 节点进度 下一个阶段索引
func (pt *PaymentTask) noteListIsLastReceive(utsRewardList *PaymentTaskRecord) (competedTimes int, isLast bool) {
	competedTimes = -1
	if utsRewardList.TaskCompetedTimes == 0 {
		competedTimes = 0
		return
	}
	if utsRewardList.TaskCompetedTimes != 0 && len(utsRewardList.RewardList) <= utsRewardList.TaskCompetedTimes {
		isLast = true
	}
	competedTimes = utsRewardList.TaskCompetedTimes
	return
}

// GetRewardByUts 请求uts
func (pt *PaymentTask) GetRewardByUts(utsParams *uts.RequestUTS) (res *PaymentTaskRecord) {
	utsParams = utsParams.Clone()
	if utsParams.SenceInfo == nil {
		utsParams.SenceInfo = map[string]*uts.TypeInfo{}
	}
	userData := userdata.NewUserInfoData(pt.Ctx, pt.ProductID)
	userAssetInfo, err := userData.GetUserAssetInfo(pt.UID, pt.ProductID)
	if err != nil {
		logit.AddNotice(pt.Ctx, logit.Error("GetUserAssetInfo-Error", err))
		return
	}
	//	获取当前签到周期的资产提现阈值
	expireThresholdFen, err := TryGetThreshold(pt.Ctx, pt.ProductID, pt.UID)
	if err != nil {
		logit.AddNotice(pt.Ctx, logit.Error("TryGetThreshold-failed", err))
		return nil
	}
	if userAssetInfo == nil {
		userAssetInfo = &common.UserAssetAPP{}
	}
	uCenterSumInt, _ := common.InitUserOperation(pt.Ctx, pt.UID).GetUCenterMoneySum(pt.ProductID)
	userInfo, _ := userdata.NewUserInfoData(pt.Ctx, pt.ProductID).GetUserInfo(pt.UID)
	if _, ok := utsParams.SenceInfo[uts.PaymentUTSType]; !ok && userInfo != nil {

		utsParams.SenceInfo[uts.PaymentUTSType] = &uts.TypeInfo{
			CacheUserLevel:    strconv.FormatInt(userInfo.Level, 10),
			VActDay:           userInfo.VActDay,
			VActDayV2:         userInfo.VActDayV2,
			VActCycle:         userInfo.GetPeriod(),
			FirstRedBagCash:   userInfo.FirstRedBagCash,
			UpSlideRedBagCash: userInfo.UpSlideRedBagCash,
			AcctCash:          userAssetInfo.DisplayMoneyInt,
			AcctGoldBean:      userAssetInfo.DisplayCoin,
			VActAsset90:       uCenterSumInt,
			VActIsBindWeChat: func() int {
				if ugauth.IsBindedWechatPayWithCtx(pt.Ctx, pt.ProductID, pt.UID) {
					return 1
				}
				return 0
			}(),
			VActSignThreshold: int(expireThresholdFen),
		}
	}
	res = pt.processUtsRepsData(utsParams)
	if res == nil {
		return
	}

	// str, _ := json.Marshal(res)
	// logit.AddNotice(pt.Ctx, logit.String("rewardByUts-resp", string(str)))
	return res
}

// ReceiveReward 领取视频额外奖励
func (pt *PaymentTask) ReceiveReward(userInfo *userdata.UserInfo, utsRewardList *PaymentTaskRecord) (sceneType int, err error) {
	noteList := utsRewardList.RewardList
	nextIndex, _ := pt.noteListIsLastReceive(utsRewardList)
	if nextIndex < 0 {
		logit.AddNotice(pt.Ctx, logit.Int("nextIndex", nextIndex))
		return
	}
	noteList[nextIndex].Status = 1
	noteList[nextIndex].ReceiveTime = time.Now().Unix()
	if utsRewardList.TaskCompetedTimes == utsRewardList.TaskTotalTimes { //如果完成，变为已完成
		utsRewardList.TaskStatus = consts.TaskStatusCompleted
	}
	utsRewardList.TaskCompetedTimes++
	err = pt.SetTaskRecordForUIDByTaskID(utsRewardList)
	if err != nil {
		logit.AddNotice(pt.Ctx, logit.Error("setTaskRecordForUIDByTaskID-err", err))
		return
	}
	sceneType, err = pt.AddReward(userInfo, noteList[nextIndex])
	if err != nil {
		return 0, ierrno.ErrorServerError
	}
	return sceneType, nil
}

// UCRewardExists ...
func (pt *PaymentTask) UCRewardExists(utsParams *uts.RequestUTS) (bool, int, error) {
	utsRewardList, _ := pt.GetPaymentList(utsParams)
	if utsRewardList == nil || len(utsRewardList.RewardList) <= 0 {
		logit.AddNotice(pt.Ctx, logit.String("utsRewardList", "empty"))
		return false, -1, ierrno.ErrorServerError
	}

	return pt.UCRewardExistsByRecord(utsRewardList)
}

// UCRewardExistsByRecord ...
func (pt *PaymentTask) UCRewardExistsByRecord(utsRewardList *PaymentTaskRecord) (bool, int, error) {
	noteList := utsRewardList.RewardList
	nextIndex, noNext := pt.noteListIsLastReceive(utsRewardList)
	if nextIndex < 0 {
		logit.AddNotice(pt.Ctx, logit.Int("nextIndexErr", nextIndex))
		return false, -1, ierrno.ErrorServerError
	}

	//	都已完成
	if noNext {
		return false, -1, nil
	}

	// nextIndex一定是未领取过的奖励
	for i := nextIndex; i < len(noteList); i++ {
		reward := noteList[i]

		if reward.PayType == dataConsts.PayTypeStatusUCenter && reward.RewardType == libConsts.RewardTypeMoney {
			return true, (i - nextIndex + 1), nil
		}
	}

	return false, -1, nil
}

// UCRewardRecevable ...
func (pt *PaymentTask) UCRewardRecevable(utsParams *uts.RequestUTS) (int64, error) {
	utsRewardList, _ := pt.GetPaymentList(utsParams)
	if utsRewardList == nil || len(utsRewardList.RewardList) <= 0 {
		logit.AddNotice(pt.Ctx, logit.String("utsRewardList", "empty"))
		return -1, ierrno.ErrorServerError
	}

	noteList := utsRewardList.RewardList
	nextIndex, noNext := pt.noteListIsLastReceive(utsRewardList)
	if nextIndex < 0 {
		logit.AddNotice(pt.Ctx, logit.Int("nextIndexErr", nextIndex))
		return -1, ierrno.ErrorServerError
	}

	//	都已完成
	if noNext {
		return 0, nil
	}

	// nextIndex一定是未领取过的奖励
	moneyFen := int64(0)
	for i := nextIndex; i < len(noteList); i++ {
		reward := noteList[i]

		if reward.PayType == dataConsts.PayTypeStatusUCenter && reward.RewardType == libConsts.RewardTypeMoney {
			moneyFen += reward.Reward
		}
	}

	return moneyFen, nil
}

// UCRewardExistedCnt ...
func (pt *PaymentTask) UCRewardExistedCnt(utsRewardList *PaymentTaskRecord) (int, error) {
	noteList := utsRewardList.RewardList
	nextIndex, noNext := pt.noteListIsLastReceive(utsRewardList)
	if nextIndex < 0 {
		logit.AddNotice(pt.Ctx, logit.Int("nextIndexErr", nextIndex))
		return 0, ierrno.ErrorServerError
	}

	//	都已完成
	if noNext {
		return 0, nil
	}

	// nextIndex一定是未领取过的奖励
	cnt := 0
	for i := nextIndex; i < len(noteList); i++ {
		reward := noteList[i]

		if reward.PayType == dataConsts.PayTypeStatusUCenter && reward.RewardType == libConsts.RewardTypeMoney {
			cnt++
		}
	}

	return cnt, nil
}

// RewardNextCoin ...
func (pt *PaymentTask) RewardNextCoin(utsRewardList *PaymentTaskRecord) (bool, error) {
	noteList := utsRewardList.RewardList
	nextIndex, noNext := pt.noteListIsLastReceive(utsRewardList)
	if nextIndex < 0 {
		logit.AddNotice(pt.Ctx, logit.Int("nextIndexErr", nextIndex))
		return false, ierrno.ErrorServerError
	}

	//	都已完成
	if noNext {
		return false, nil
	}

	// 下一个不是金豆
	if len(noteList) >= (nextIndex+1) && noteList[nextIndex] != nil {
		nextReward := noteList[nextIndex]
		return nextReward.RewardType == libConsts.RewardTypeCoin, nil
	}

	//	默认不是
	return false, nil
}

// getPaymentRewardRedisKey 业务key
func (pt *PaymentTask) getPaymentRewardRedisKey() string {
	rewardKey := consts.GetRedisKey(consts.PaymentReward, pt.ProductID, pt.Conf.TaskID, pt.UID)
	return rewardKey
}

// GetStrategyParams ...
func (pt *PaymentTask) GetStrategyParams(m map[string]*uts.TypeInfo) (map[string]*uts.TypeInfo, error) {
	return nil, nil
}

// GetUTSRespAndIsCache ...
func (pt *PaymentTask) GetUTSRespAndIsCache(data *uts.ResData) (*consts.BaseTaskRecord, error) {
	return nil, nil
}

// Process ...
func (pt *PaymentTask) Process(data *consts.TaskProcessData, requestUTS *uts.RequestUTS) (interface{}, error) {
	return nil, nil
}

// GetSign 获取签到信息
func (pt *PaymentTask) GetSign(ctx *ibase.APIContext, period int64, requestUTS *uts.RequestUTS) string {
	isSign := "0"
	wData := NewWelfareData(ctx, pt.ProductID)
	isCheckIn := true
	var err error
	if pt.UID <= 0 {
		return isSign
	}
	isCheckIn, _, err = wData.GetWelfareForNoCache(pt.UID, pt.CUID, period, requestUTS)
	if isCheckIn || err != nil {
		isSign = "1"
	}
	return isSign
}

// AddReward 领取视频额外奖励
func (pt *PaymentTask) AddReward(userInfo *userdata.UserInfo, rewardInfo *types.PaymentRewardNode) (sceneType int, err error) {
	reward := rewardInfo.Reward
	rewardType := rewardInfo.RewardType
	payType := rewardInfo.PayType
	period := userInfo.GetPeriod()
	//打款到账户余额-金币
	if rewardType == libConsts.RewardTypeCoin {
		sceneType = consts.TypeCoinPayment //账号金币-金币奖励
		o, coinErr := common.InitCoinOperation(pt.Ctx, pt.UID, pt.ProductID)
		if coinErr != nil {
			return sceneType, coinErr
		}
		addRes, err := o.AddCoin(period, reward, consts.TypeCoinPayment, true, time.Now(), "", nil, nil)
		if !addRes || err != nil {
			logit.AddNotice(pt.Ctx, logit.String("AddCoin-error", "1"))
		}
		return sceneType, err
	}

	//打款到余额账号余额
	if payType == dataConsts.PayTypeStatusAsset && rewardType == libConsts.RewardTypeMoney { //现金奖励-余额账号
		sceneType = dataConsts.MoneyTypePaymentAsset
		moneyRes, moneyErr := common.InitMoneyOperation(pt.Ctx, pt.UID, pt.ProductID)
		if moneyErr != nil {
			return sceneType, moneyErr
		}
		addRes, err := moneyRes.AddMoney(period, reward, dataConsts.MoneyTypePaymentAsset, payType, true, time.Now(), "", nil, nil)
		logit.AddNotice(pt.Ctx, logit.Bool("addRes", addRes))
		return sceneType, err
	}

	sceneType = consts.MoneyTypePayment
	//打款到资产中心余额
	if payType == dataConsts.PayTypeStatusUCenter && rewardType == libConsts.RewardTypeMoney {
		moneyOperation, err := common.InitMoneyOperation(pt.Ctx, pt.UID, pt.ProductID)
		if err != nil {
			return sceneType, err
		}
		addRes, err := moneyOperation.AddMoneyRecord(period, reward, consts.MoneyTypePayment, payType, true, time.Now(), nil, nil)
		if !addRes || err != nil {
			logit.AddNotice(pt.Ctx, logit.String("AddMoneyRecord-error", "1"))
			return sceneType, err
		}
		//打款到资产中心
		withdrawData := withdraw.NewWithdrawData(pt.Ctx, pt.ProductID)
		isSend, err := withdrawData.SmallWithdrawPrize(pt.UID, reward, sceneType)
		if err != nil || !isSend {
			logit.AddNotice(pt.Ctx, logit.String("rewardType", "error"))
		}
	}
	//打款到微信
	if payType == dataConsts.PayTypeWeChat && rewardType == libConsts.RewardTypeMoney { //现金奖励-余额账号
		sceneType = dataConsts.MoneyTypePaymentCountAsset
		moneyRes, moneyErr := common.InitMoneyOperation(pt.Ctx, pt.UID, pt.ProductID)
		if moneyErr != nil {
			return sceneType, moneyErr
		}
		var addRes bool
		addRes, err = moneyRes.AddMoneyRecord(period, reward, consts.MoneyTypePayment, consts.PayTypeWeChat, true, time.Now(), nil, nil)
		logit.AddNotice(pt.Ctx, logit.Bool("addRes", addRes))
		if err != nil {
			return
		}
		withdraw := withdraw.NewWithdrawData(pt.Ctx, pt.ProductID)
		_, err = withdraw.WeChatRealTimeWithdraw(userInfo, userInfo.GetCUID(pt.Ctx), reward, consts.MoneyTypePayment)
		return sceneType, err
	}
	return sceneType, err
}

// UnLoginGetListTaskInfo ...  任务面板里面的任务列表
func (pt *PaymentTask) UnLoginGetListTaskInfo(taskInfoData *consts.TaskInfoData, gtInfo *task.Info, data2 *uts.ResData) (*consts.TaskInfoResp, error) {
	taskStatus, err := pt.GetTaskStatus(taskInfoData.UTSParams)
	if err != nil {
		return nil, err
	}
	if taskStatus.TotalTimes == 0 {
		return nil, nil
	}
	record, err := pt.GetTaskRecord()
	if err != nil || record == nil {
		return nil, err
	}
	if record.TaskStatus == consts.TaskStatusReceived {
		taskStatus.TaskStatus = consts.TaskStatusReceived
	}
	info := pt.GetBaseTaskInfo(gtInfo, taskStatus, taskInfoData.Platform, taskInfoData.DdScene)
	info.SubTitleReplace = pt.GetReplceText()
	return info, nil
}

// processTplData 处理面板数据
func (pt *PaymentTask) processTplData(data *consts.TaskCompleteData, requestUTS *uts.RequestUTS, utsRewardList *PaymentTaskRecord, userInfo *userdata.UserInfo, userAssetInfo *common.UserAssetAPP) (tplData map[string]string, err error) {
	nodeList := utsRewardList.RewardList
	competedTimes := utsRewardList.TaskCompetedTimes
	totalTimes := len(nodeList)
	left := totalTimes - competedTimes - 1
	paymentRewardNode := nodeList[competedTimes]
	isLast := false
	if left <= 0 {
		isLast = true
	}
	//渲染模版
	tplData = map[string]string{
		"is_done":             "0",
		"reward":              "",
		"reward_type":         "",
		"pay_type":            "",
		"showSign":            "0",
		"left":                "",
		"icon_url":            "",
		"next_reward":         "",
		"next_reward_type":    "",
		"next_pay_type":       "",
		"asset_type":          "",
		"asset":               "",
		"home_guide_hit":      "0",
		"home_guide_type":     "",
		"home_guide_text":     "",
		"home_guide_icon_url": "",
		"home_guide_scheme":   "",
		"home_guide_taskId":   "",
	}
	if left > 0 && competedTimes <= totalTimes-1 {
		tplData["next_reward_type"] = nodeList[competedTimes+1].RewardType
		tplData["next_pay_type"] = strconv.Itoa(nodeList[competedTimes+1].PayType)
		tplData["next_reward"] = strconv.FormatInt(nodeList[competedTimes+1].Reward, 10)
		if tplData["next_reward_type"] == libConsts.RewardTypeMoney {
			tplData["next_reward"] = util.FenToYuanNew(nodeList[competedTimes+1].Reward, 2, false)
		}
	}

	rewardType := paymentRewardNode.RewardType
	payType := paymentRewardNode.PayType
	reward := paymentRewardNode.Reward
	if rewardType == libConsts.RewardTypeCoin {
		userAssetInfo.DisplayCoin = userAssetInfo.DisplayCoin + reward
		tplData["asset_type"] = libConsts.RewardTypeCoin
		tplData["asset"] = strconv.FormatInt(userAssetInfo.DisplayCoin, 10)
	} else if rewardType == libConsts.RewardTypeMoney {
		if payType == dataConsts.PayTypeStatusAsset { //到余额
			userAssetInfo.DisplayMoneyInt = userAssetInfo.DisplayMoneyInt + reward
		}
		tplData["asset_type"] = libConsts.RewardTypeMoney
		tplData["asset"] = util.FenToYuanNew(userAssetInfo.DisplayMoneyInt, 2, false)
	}

	logit.AddNotice(pt.Ctx, logit.String("curr-data", fmt.Sprintf("index:%d,left:%d,len:%d, reward:%v, type:%s,isLast:%v", competedTimes, left, totalTimes, reward, rewardType, isLast)))
	if left <= 0 && userInfo.IsFirstDayUser() {
		var showSign string
		showSign = pt.GetSign(pt.Ctx, userInfo.Period, requestUTS)
		isCondition := showSign == "0"
		if isCondition {
			tplData["showSign"] = "1"
		}
	}

	tplData["reward_type"] = rewardType
	tplData["left"] = strconv.Itoa(left)
	tplData["index"] = strconv.Itoa(competedTimes)
	tplData["pay_type"] = strconv.Itoa(payType)
	tplData["reward"] = cast.ToString(reward)

	platformStr := ua.Platform2Str(data.Platform)
	tplData = pt.processTopNotify(tplData, reward, payType, rewardType, platformStr, nodeList, competedTimes)

	if rewardType == libConsts.RewardTypeMoney {
		tplData["reward"] = util.FenToYuanNew(reward, 2, false)
	}

	if left <= 0 {
		tplData["is_done"] = "1"
		// 任务导流任务
		taskGuideData := pt.taskGuide(requestUTS)
		tplData["home_guide_hit"] = taskGuideData.IsHit
		tplData["home_guide_type"] = taskGuideData.Type
		tplData["home_guide_text"] = taskGuideData.Text
		tplData["home_guide_icon_url"] = taskGuideData.IconURL
		tplData["home_guide_scheme"] = taskGuideData.Scheme
		tplData["home_guide_taskId"] = taskGuideData.TaskID
	}

	return
}

func (pt *PaymentTask) processTopNotify(tplData map[string]string, reward int64, payType int, rewardType, platformStr string, rewardList []*types.PaymentRewardNode, formerCompetedTimes int) map[string]string {
	if tplData == nil {
		tplData = make(map[string]string)
	}

	if payType == dataConsts.PayTypeStatusUCenter && rewardType == libConsts.RewardTypeMoney {
		return pt.moneyUCenterNotify(tplData, reward, platformStr)
	}
	if payType == dataConsts.PayTypeStatusWeChat && rewardType == libConsts.RewardTypeMoney {
		return pt.moneyWechatNotify(tplData, reward, platformStr)
	}
	// 金豆顶部通知
	if rewardType == libConsts.RewardTypeCoin {
		return pt.coinNotify(tplData, reward, rewardList, formerCompetedTimes)
	}

	return tplData
}

func (pt *PaymentTask) coinNotify(tplData map[string]string, reward int64, rewardList []*types.PaymentRewardNode, formerCompetedTimes int) map[string]string {
	hitExp1, hitExp2, exp3NotifyCnt, hitExpReverse := smaple.
		NewUserSampleData(pt.Ctx, &smaple.UserSampleDataParams{ProductID: pt.ProductID}).
		IsPaymentCoinNotify()

	if hitExpReverse {
		// 反转组，do nothing，保持原线上不下发顶部通知的效果
		return tplData
	}

	if hitExp1 {
		// 每个金币都通知
		return pt.coinNotifyData(tplData, reward)
	}

	if hitExp2 {
		//	前3笔金豆通知
		notifyCnt := 3
		return pt.coinNotifyDataByCnt(tplData, reward, rewardList, formerCompetedTimes, notifyCnt)
	}
	if exp3NotifyCnt > 0 {
		//	前n笔金豆通知
		return pt.coinNotifyDataByCnt(tplData, reward, rewardList, formerCompetedTimes, exp3NotifyCnt)
	}

	// do nothing
	return tplData
}

func (pt *PaymentTask) coinNotifyDataByCnt(tplData map[string]string, reward int64, rewardList []*types.PaymentRewardNode, formerCompetedTimes, allowedNotifyCnt int) map[string]string {
	//	前n笔金豆通知
	for i := 0; i < formerCompetedTimes; i++ {
		if rewardList[i].RewardType == libConsts.RewardTypeCoin {
			allowedNotifyCnt--
		}
		if allowedNotifyCnt <= 0 {
			// 没有剩余次数，遍历结束
			break
		}
	}
	if allowedNotifyCnt > 0 {
		tplData = pt.coinNotifyData(tplData, reward)
	}

	return tplData
}

func (pt *PaymentTask) coinNotifyData(tplData map[string]string, reward int64) map[string]string {
	tplData["reward"] = cast.ToString(reward)
	tplData["title"] = "金豆到账"
	tplData["text"] = tplData["reward"] + "金豆已发放，加速提现20元"
	tplData["scheme"] = "baiduboxapp://growthsystem/invokeWealthVideoTalosPage?params=%7B%22startparams%22%3A%20%7B%22mainBizName%22%3A%20%22box.rnplugin.piggyBankTask%22%2C%22moduleName%22%3A%20%22piggyBankTask%22%2C%22subBizName%22%3A%20%22piggyBankTask%22%2C%22bundleName%22%3A%20%22piggyBankTask%22%7D%7D"
	tplData["icon_url"] = "https://efe-h2.cdn.bcebos.com/ceug/resource/res/2024-09/1726802597981/yntzx0h0mozk.png"
	return tplData
}

func (pt *PaymentTask) moneyWechatNotify(tplData map[string]string, reward int64, platformStr string) map[string]string {
	tplData["reward"] = util.FenToYuanNew(reward, 2, false)
	tplData["title"] = "现金到账"
	tplData["text"] = tplData["reward"] + "元已打款，请在微信查看"
	tplData["scheme"] = pt.withdrawRecordsScheme(platformStr)
	tplData["icon_url"] = "https://b.bdstatic.com/searchbox/file/cmsuploader/20230218/1676690363777027.png"
	return tplData
}

func (pt *PaymentTask) moneyUCenterNotify(tplData map[string]string, reward int64, platformStr string) map[string]string {
	// 默认IOS
	scheme := "baiduboxlite://v30/immerseBrowser/open?params=%7B%22url%22%3A%22https%3A%2F%2Factivity.baidu.com%2Fvideo%2Fwithdraw%2FwithdrawHome%3Fproductid%3D2%26idfrom%3Dtaskenter%26ddScene%3Dbar_flow_video%22%2C%22newbrowser%22%3A%221%22%2C%22forbidautorotate%22%3A%221%22%2C%22toolbarposition%22%3A%220%22%2C%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1&mediaPlayNeedUserAction=0"
	if platformStr == libConsts.PlatformAndroidStr {
		scheme = "baiduboxlite://v1/easybrowse/open?url=https%3A%2F%2Factivity.baidu.com%2Fvideo%2Fwithdraw%2FwithdrawHome%3Fproductid%3D2%26idfrom%3Dtaskenter%26ddScene%3Dbar_flow_video&newbrowser=1&forbidautorotate=1&type=immerse&backlocation=1&bannerswitch=1&params=%7B%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1"
	}
	// 未登录处理
	if pt.UID <= 0 {
		scheme = "baiduboxlite://v30/immerseBrowser/open?params=%7B%22url%22%3A%22https%3A%2F%2Factivity.baidu.com%2Fvideo%2Fwithdraw%2FassetCenter%3Fproductid%3D2%22%2C%22newbrowser%22%3A%221%22%2C%22forbidautorotate%22%3A%221%22%2C%22toolbarposition%22%3A%220%22%2C%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1&mediaPlayNeedUserAction=0"
		if platformStr == libConsts.PlatformAndroidStr {
			scheme = "baiduboxlite://v1/easybrowse/open?url=https%3A%2F%2Factivity.baidu.com%2Fvideo%2Fwithdraw%2FassetCenter%3Fproductid%3D2&newbrowser=1&forbidautorotate=1&type=immerse&backlocation=1&bannerswitch=1&params=%7B%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1"
		}
		if env.RunModeDebug == env.RunMode() || env.RunModeTest == env.RunMode() {
			scheme = "baiduboxlite://v30/immerseBrowser/open?params=%7B%22url%22%3A%22http%3A%2F%2Fmegqa-liumeng02.bcc-bdbl.baidu.com%3A8881%2Fvideo%2Fwithdraw%2FassetCenter%3Fproductid%3D2%22%2C%22newbrowser%22%3A%221%22%2C%22forbidautorotate%22%3A%221%22%2C%22toolbarposition%22%3A%220%22%2C%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1&mediaPlayNeedUserAction=0"
			if platformStr == libConsts.PlatformAndroidStr {
				scheme = "baiduboxlite://v1/easybrowse/open?url=http%3A%2F%2Fmegqa-liumeng02.bcc-bdbl.baidu.com%3A8881%2Fvideo%2Fwithdraw%2FassetCenter%3Fproductid%3D2&newbrowser=1&forbidautorotate=1&type=immerse&backlocation=1&bannerswitch=1&params=%7B%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1"
			}
		}
	}

	tplData["reward"] = util.FenToYuanNew(reward, 2, false)
	tplData["title"] = "现金到账"
	tplData["text"] = tplData["reward"] + "元收款成功，可提现至微信"
	tplData["scheme"] = scheme
	tplData["icon_url"] = "https://b.bdstatic.com/searchbox/file/cmsuploader/20230218/1676690363777027.png"
	return tplData
}

func (pt *PaymentTask) withdrawRecordsScheme(platformStr string) string {
	scheme := "baiduboxlite://v30/immerseBrowser/open?params=%7B%22url%22%3A%22https%3A%2F%2Factivity.baidu.com%2Fvideo%2Fwithdraw%2FwithdrawRecord%3Fproductid%3D2%22%2C%22newbrowser%22%3A%221%22%2C%22forbidautorotate%22%3A%221%22%2C%22toolbarposition%22%3A%220%22%2C%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1&mediaPlayNeedUserAction=0"
	if platformStr == libConsts.PlatformAndroidStr {
		scheme = "baiduboxlite://v1/easybrowse/open?url=https%3A%2F%2Factivity.baidu.com%2Fvideo%2Fwithdraw%2FwithdrawRecord%3Fproductid%3D2&newbrowser=1&forbidautorotate=1&type=immerse&backlocation=1&bannerswitch=1&params=%7B%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1"
	}
	if env.RunModeDebug == env.RunMode() || env.RunModeTest == env.RunMode() {
		scheme = "baiduboxlite://v30/immerseBrowser/open?params=%7B%22url%22%3A%22http%3A%2F%2F!(hostname)%3A!(port)%2Fvideo%2Fwithdraw%2FwithdrawRecord%3Fproductid%3D2%22%2C%22newbrowser%22%3A%221%22%2C%22forbidautorotate%22%3A%221%22%2C%22toolbarposition%22%3A%220%22%2C%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1&mediaPlayNeedUserAction=0"
		if platformStr == libConsts.PlatformAndroidStr {
			scheme = "baiduboxlite://v1/easybrowse/open?url=http%3A%2F%2F!(hostname)%3A!(port)%2Fvideo%2Fwithdraw%2FwithdrawRecord%3Fproductid%3D2&newbrowser=1&forbidautorotate=1&type=immerse&backlocation=1&bannerswitch=1&params=%7B%22showtoolbar%22%3A%221%22%7D&append=1&zoomswitch=0&append_di=1"
		}
		host, _ := os.Hostname()
		port := os.Getenv("LISTEN_PORT")
		scheme = strings.Replace(scheme, "!(hostname)", host, -1)
		scheme = strings.Replace(scheme, "!(port)", port, -1)
	}
	return scheme
}

// processTplData 处理面板数据
func (pt *PaymentTask) getRewardInfo(utsRewardList *PaymentTaskRecord) (paymentRewardNode *types.PaymentRewardNode, err error) {
	//节点状态计算
	nodeList := utsRewardList.RewardList
	competedTimes := utsRewardList.TaskCompetedTimes
	totalTimes := len(nodeList)
	//最大限制
	conf, err := pt.cache.GetPaymentTaskByApp(pt.ProductID)
	if conf != nil || err == nil && conf.Default.Limit > 0 {
		if totalTimes >= conf.Default.Limit {
			totalTimes = conf.Default.Limit
		}
	}
	left := totalTimes - competedTimes - 1
	if left < 0 {
		logit.AddNotice(pt.Ctx, logit.Int("noteListIsLastReceive", competedTimes))
		return nil, ierrno.ErrorIntranetTaskComplete
	}
	//已完成
	if nodeList[competedTimes].Status == consts.PaymentRedPacketStatusEnd {
		logit.AddNotice(pt.Ctx, logit.String("Status", "1"))
		return nil, ierrno.ErrorIntranetTaskComplete
	}
	paymentRewardNode = nodeList[competedTimes]
	return
}

// processUtsRepsData ...
func (pt *PaymentTask) processUtsRepsData(utsParams *uts.RequestUTS) (res *PaymentTaskRecord) {
	utsData := uts.NewUTS(pt.Ctx, pt.ProductID)
	taskRewardInfo, err := utsData.GetUtsActivityDataByUtsID(pt.UID, pt.CUID, utsParams, uts.PaymentUTSType)
	if err != nil || taskRewardInfo == nil {
		logit.AddNotice(pt.Ctx, logit.Error("requestUTS-fail", err))
		return
	}
	if len(taskRewardInfo.VideoWalletRewardList) == 0 {
		logit.AddNotice(pt.Ctx, logit.String("rewardList", "empty"))
		return
	}
	res = &PaymentTaskRecord{
		BaseTaskRecord: consts.NewBaseTaskRecord(),
	}
	nodeList := taskRewardInfo.VideoWalletRewardList
	moneyTypeCount := 0
	for _, item := range nodeList {
		rewardType := libConsts.RewardTypeCoin
		if item.ValueType == 1 {
			rewardType = libConsts.RewardTypeMoney
		}
		//错误配置数据, 资产中心的只能是现金
		if item.PayType == dataConsts.PayTypeStatusUCenter && rewardType != libConsts.RewardTypeMoney {
			continue
		}
		if rewardType == libConsts.RewardTypeMoney {
			moneyTypeCount++
		}
		rewardNode := &types.PaymentRewardNode{
			RewardType: rewardType,
			Reward:     item.Value,
			PayType:    item.PayType,
		}
		res.RewardList = append(res.RewardList, rewardNode)
	}
	res.MoneyTypeCount = moneyTypeCount
	res.TaskTotalTimes = len(res.RewardList)
	return
}

func (pt *PaymentTask) calcProgress(utsRewardList *PaymentTaskRecord) (int, int, int) {
	//节点状态计算
	noteList := utsRewardList.RewardList
	competedTimes := utsRewardList.TaskCompetedTimes
	totalTimes := len(noteList)
	//最大限制
	conf, err := pt.cache.GetPaymentTaskByApp(pt.ProductID)
	if conf != nil || err == nil && conf.Default.Limit > 0 {
		if totalTimes >= conf.Default.Limit {
			totalTimes = conf.Default.Limit
		}
	}
	left := totalTimes - competedTimes
	if left < 0 {
		left = 0
	}

	return totalTimes, competedTimes, left
}

// processUtsRepsData ...
func (pt *PaymentTask) processRegisterRepsData(utsRewardList *PaymentTaskRecord, requestUTS *uts.RequestUTS, userInfo *userdata.UserInfo, res *types.PaymentDuration) {
	totalTimes, competedTimes, left := pt.calcProgress(utsRewardList)
	res.TotalLeftTimes = left
	res.Total = totalTimes
	noteList := utsRewardList.RewardList

	//签到信息
	res.ShowSign = 0
	res.IsFirstDay = 0
	if left <= 0 && userInfo.IsFirstDayUser() {
		res.IsFirstDay = 1
		showSign := pt.GetSign(pt.Ctx, userInfo.Period, requestUTS)
		isCondition := showSign == "0"
		if isCondition {
			res.ShowSign = 1
		}
	}
	logit.AddNotice(pt.Ctx, logit.String("noteInfo", fmt.Sprintf("len:%d,left:%d,ShowSign:%d:", totalTimes, left, res.ShowSign)))
	//查询资产信息
	userData := userdata.NewUserInfoData(pt.Ctx, pt.ProductID)
	assetInfo, _ := userData.GetUserAssetInfo(pt.UID, pt.ProductID, pt.CUID)
	res.IsDone = consts.PaymentDoneStatusEnd
	if assetInfo != nil && assetInfo.DisplayMoneyInt > 0 {
		res.Asset = util.FenToYuanNew(assetInfo.DisplayMoneyInt, 2, false)
		res.AssetType = libConsts.RewardTypeMoney
	}
	if left > 0 { //未结束
		res.IsDone = consts.PaymentDoneStatusIng
		res.CurrentReward.PayType = noteList[competedTimes].PayType
		res.CurrentReward.RewardType = noteList[competedTimes].RewardType
		res.CurrentReward.PayType = noteList[competedTimes].PayType
		res.CurrentReward.Reward = cast.ToString(noteList[competedTimes].Reward)
		if res.CurrentReward.RewardType == libConsts.RewardTypeMoney {
			res.CurrentReward.Reward = util.FenToYuanNew(noteList[competedTimes].Reward, 2, false)
		}
		if res.CurrentReward.RewardType == libConsts.RewardTypeCoin && assetInfo != nil && assetInfo.DisplayCoin > 0 {
			res.Asset = cast.ToString(assetInfo.DisplayCoin)
			res.AssetType = libConsts.RewardTypeCoin
		}
	}

	// 新增任务引导
	if res.IsDone == consts.PaymentDoneStatusEnd {
		res.TaskGuide = pt.taskGuide(requestUTS)
	}

	return
}

// TaskGuidableNow ... 非面板任务，不引导
func (pt *PaymentTask) TaskGuidableNow(params *ListParamsV20) (bool, error) { return false, nil }

// TaskStepsToday ...
func (pt *PaymentTask) TaskStepsToday(params *ListParamsV20) (int, error) {
	return taskguide.GuideTaskStepsTotalZero, nil
}

// taskGuide 任务引导
func (pt *PaymentTask) taskGuide(requestUTS *uts.RequestUTS) (tg *taskGuide) {

	tg = &taskGuide{
		IsHit: "0", // 默认
	}
	sampleData := smaple.NewUserSampleData(pt.Ctx, &smaple.UserSampleDataParams{ProductID: pt.ProductID})
	// 引导命中任务面板导流实验
	if sampleData.IsPaymentTaskGuideToPanel() {
		tg.IsHit = "1"
		tg.Type = "taskPanel"
		tg.IconURL = "https://b.bdstatic.com/searchbox/image/gcp/20241008/1360464377.png"
		tg.Scheme = "baiduboxlite://growthsystem/invokeWealthVideoTalosPage?params=%7B%22startparams%22%3A%7B%22mainBizName%22%3A%22box.rnplugin.piggyBankTask%22%2C%22moduleName%22%3A%22piggyBankTask%22%2C%22subBizName%22%3A%22piggyBankTask%22%2C%22bundleName%22%3A%22piggyBankTask%22%7D%2C%22bizparams%22%3A%7B%22routerInfo%22%3A%7B%22url%22%3A%22%2F%22%2C%22data%22%3A%7B%22anchorTaskId%22%3A%226367%22%7D%7D%7D%7D"
		tg.Text = "2000"
		tg.TaskID = "6367"
		return
	}

	// 命中签到：sigin、喝水：drinkWater 导流实验  签到用户第一天不导流
	if sampleData.IsPaymentTaskGuideToDrinkSign() {
		// 签到
		siginStatus, _ := pt.taskGuideToSigin(pt.Ctx, requestUTS)
		if siginStatus {
			tg.IsHit = "1"
			tg.TaskID = strconv.Itoa(consts.LiteWelfareTaskID)
			tg.Type = "sigin"
			_ = pt.SetGuideFlag(pt.Ctx)
			return
		}
		// 喝水
		drinkeStatus, _ := pt.taskGuideTodrinkWater(pt.Ctx, requestUTS)
		flag := pt.CheckGuideFlag(pt.Ctx)
		if !flag && drinkeStatus {
			tg.IsHit = "1"
			tg.TaskID = strconv.Itoa(consts.LiteDrinkWaterTaskID)
			tg.IconURL = "https://b.bdstatic.com/searchbox/image/gcp/20241008/1038015768.png"
			tg.Scheme = "baiduboxlite://growthsystem/invokeWealthVideoTalosPage?params=%7B%22startparams%22%3A%7B%22mainBizName%22%3A%22box.rnplugin.piggyBankTask%22%2C%22moduleName%22%3A%22piggyBankTask%22%2C%22subBizName%22%3A%22piggyBankTask%22%2C%22bundleName%22%3A%22piggyBankTask%22%7D%2C%22bizparams%22%3A%7B%22routerInfo%22%3A%7B%22url%22%3A%22%2F%22%2C%22data%22%3A%7B%22videoCard%22%3A%7B%22cardType%22%3A%22invalid%22%2C%22clickType%22%3A%22drinkWater%22%7D%7D%7D%7D%7D"
			tg.Text = "200"
			tg.Type = "drinkWater"
			return
		}

	}

	return

}

// taskGuideTodrinkWater 喝水任务
func (pt *PaymentTask) taskGuideTodrinkWater(ctx *ibase.APIContext, requestUTS *uts.RequestUTS) (bool, error) {

	// 如果今日从未喝水，则推送卡片
	drinkObj := NewDrinkWaterTaskRecordObj(ctx, consts.LiteDrinkWaterTaskID,
		pt.UID, pt.CUID, pt.ProductID)
	rewardData, err := drinkObj.GetRewardData(requestUTS)

	if err != nil || rewardData == nil {
		logit.AddNotice(ctx, logit.Error("getCardDataFromDrinkErr", err))
		return false, err
	}
	if rewardData == nil || len(rewardData.RewardList) <= 0 {
		logit.AddNotice(ctx, logit.String("getCardDataFromDrink", "empty"))
		return false, nil
	}
	// 判断今日是否已喝水
	for _, item := range rewardData.RewardList {
		if item.Status == consts.DrinkWaterReceived { // 第一杯水已领取
			return false, nil
		}
		return true, nil
	}

	return false, nil

}

// taskGuideToSigin 签到信息
func (pt *PaymentTask) taskGuideToSigin(ctx *ibase.APIContext, requestUTS *uts.RequestUTS) (bool, error) {

	welfare := NewWelfareData(ctx, pt.ProductID)
	userData := userdata.NewUserInfoData(ctx, pt.ProductID)
	userInfo, err := userData.GetUserInfo(pt.UID)
	if userInfo == nil || err != nil {
		return false, err
	}
	// 首日不展示签到弹窗
	if userInfo.IsFirstDayUser() {
		return false, nil
	}

	welfareData, _, err := welfare.GetWelfare(pt.UID, pt.CUID, userInfo.Period, requestUTS)
	if err != nil || welfareData == nil {
		return false, err
	}
	if welfareData.IsCheckin {
		return false, nil
	}
	dayIndex := welfareData.Day - 1

	for idx := range welfareData.RewardList {
		if dayIndex > idx {
			continue
		}
		// 未签到的奖励
		return true, nil
	}

	return true, nil
}

// CheckGuideFlag 检测是否已经展示过弹窗
func (pt *PaymentTask) CheckGuideFlag(ctx *ibase.APIContext) bool {

	redisKey := consts.RedisKey(consts.TaskPaymentGuideFlag, pt.ProductID, pt.UID, time.Now().Format("20060102"))
	num, err := pt.IRedis.Exists(redisKey)
	if num > 0 || err != nil {
		return true
	}

	return false
}

// SetGuideFlag 设置已经展示过弹窗
func (pt *PaymentTask) SetGuideFlag(ctx *ibase.APIContext) error {

	redisKey := consts.RedisKey(consts.TaskPaymentGuideFlag, pt.ProductID, pt.UID, time.Now().Format("20060102"))
	restOfToday := time.Duration(util.GetRestOfToday())
	_, err := pt.IRedis.Set(redisKey, 1, time.Second*restOfToday)

	return err
}

// GetUpSlideMoneyToday 获取今日已领取的现金奖励
func (pt *PaymentTask) GetUpSlideMoneyToday() (upSlideMoneyToday int) {
	utsRewardList, err := pt.GetPaymentListFromCache()
	if err != nil || utsRewardList == nil || len(utsRewardList.RewardList) <= 0 {
		return
	}
	// 今天已获得现金奖励总和
	for idx, reward := range utsRewardList.RewardList {
		if idx < utsRewardList.TaskCompetedTimes && reward != nil && reward.RewardType == libConsts.RewardTypeMoney {
			upSlideMoneyToday += cast.ToInt(reward.Reward)
		}
	}

	return
}



```

请根据上面的接口代码内容，并参考当前项目代码风格，进行接下来的开发任务。当前代码库为sbox-baisc模块的上游调用方，当前接口为上滑红包领取相关接口，主要变更如下：
1. 新增实现上滑红包为小额资产奖励的领取逻辑。反作弊检查、增加领取记录、清理红包缓存、给用户加资产奖励、组装资产领取信息返回；
2. 增加反作弊参数类型值，小额资产，用于反作弊侧区分上滑红包领取场景下，奖励的不同类型，方便做监控和作弊识别；
3. 提取 model/data/task/task_payment.go 的资产奖励信息提取成公共方法：
        - 新增通用方法，统一收敛，和提供给前端的小额资产信息是类似的。将工具函数开发到如下路径：library/util/notify.go文件
        - 如果在以上需求中使用到了该文件需要额外表明。

请输出你修改后的完整代码并标出修改的部分：