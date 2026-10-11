---
title: "edit-go-piggybank-index-hard"
description: "你是一个 go 服务端开发工程师，你正在开发一个存钱罐业务，需要领取特定任务的奖励并返回领取信息。下面是一个上滑接受钱数额接口的全部代码："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\eval\\code_gen\\prompt\\edit-go-piggybank-index-hard.md"
---
你是一个 go 服务端开发工程师，你正在开发一个存钱罐业务，需要领取特定任务的奖励并返回领取信息。下面是一个上滑接受钱数额接口的全部代码：

## 文件：'library/mis/struct_smaple.go'

```
package mis

import (
    "errors"
    "strings"
    "time"

    libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
)

// SampleConf .
type SampleConf struct {
    GuideTask                    *SampleData                    `json:"guideTask"`
    NewUserWechatpay             *SampleData                    `json:"newUserWechatpay"`
    WealthPlaylet                *SampleData                    `json:"wealthPlaylet"`
    SigninViewvideoDone          *SampleData                    `json:"signinViewvideoDone"`
    AdVideoMoneyList             *SampleData                    `json:"adVideoMoneyList"`           //激励视频现金阶段任务发放实验
    SearchBrowseDuration         *SearchBrowseDuration          `json:"searchBrowseDuration"`       //搜索页时长实验
    SearchDirectRewards          *SampleData                    `json:"searchDirectRewards"`        //搜索任务直接下发实验
    AdVideoDirectRewards         *SampleData                    `json:"adVideoDirectRewards"`       //激励视频任务直接下发实验
    Expirered                    *SampleData                    `json:"expirered"`                  //失活用户清理资产中心余额实验
    AdVideoMultipleEntry         *AdVideoMultipleEntry          `json:"adVideoMultipleEntry"`       //多入口添加激励视频(换现金弹窗、三餐任务、喝水打卡)
    WealthProcessTips            *WealthProcessTips             `json:"wealthProcessTips"`          //小财神计时器新样式tips
    EatRecharge                  *SampleData                    `json:"eatRecharge"`                //三餐看视频补领
    RedpacketAdVideoMultiple     *SampleData                    `json:"redpacketAdVideoMultiple"`   //红包广场多个激励视频
    SearchQueryWord              *SampleData                    `json:"searchQueryWord"`            //搜索关键词
    UcMoneyExpire                *UcExpireInfo                  `json:"ucExpire"`                   //资产中心余额过期
    AdVideoSubScript             *SampleData                    `json:"adVideoSubScript"`           //激励视频角标
    WithdrawList                 *SampleData                    `json:"withdrawList"`               //提鲜氛围优化
    TaskPanelActivation          *TaskPanelActivationSampleData `json:"taskPanelActivationNew"`     //任务面板根据活跃度排序
    UcThreshold                  *SampleData                    `json:"ucThreshold"`                //资产中心提现阈值
    DurationNoToast              *SampleData                    `json:"durationNoToast"`            // 有倒计时 无弹窗有toast
    DurationToast                *SampleData                    `json:"durationToast"`              // 有倒计时 有倒计时有弹窗无toast
    PriorityPopup                *SampleData                    `json:"priorityPopup"`              // priorityPopup
    UCenterEntrance              *SampleData                    `json:"ucenterEntrance"`            // ucenterEntrance
    VideoTaskRemoveTop           *SampleData                    `json:"videoTaskRemoveTop"`         // 视频任务去顶部
    AdVideoTitle                 *AdVideoTitleSampleData        `json:"adVideoTitle"`               // 激励视频文案优化
    TaskPanelTile                *SampleData                    `json:"taskPanelTile"`              // 任务面板标题优化
    CheckInPersonalized          *SampleData                    `json:"checkInPersonalized"`        // 签到天数个性化
    TaskPanelVideoNumTitle       *SampleData                    `json:"taskPanelVideoNumTitle"`     // 任务面板非30日活动用户看视频任务任务标题优化
    TaskPanelViewVideoTitle      *SampleData                    `json:"taskPanelViewVideoTitle"`    // 任务面30日内看视频任务板标题优化
    HomeDialog                   *SampleData                    `json:"homeDialog"`                 // 首页弹窗优化
    SearchBackRoute              *SampleData                    `json:"searchBackRoute"`            // 搜索任务回流路径优化
    CheckInNeedOpenPanel         *SampleData                    `json:"checkInNeedOpenPanel"`       // 签到弹窗优化
    AdVideoGuideLimit            *SampleData                    `json:"adVideoGuideLimit"`          // 激励视频引导限制 三餐、喝水、换金豆弹窗上激励视频引导弹窗
    CheckInShowBigTips           *SampleData                    `json:"checkInShowBigTips"`         // 小额余额清理逻辑修改,签到弹窗角标修改
    CheckInBalanceClear          *SampleData                    `json:"checkInBalanceClear"`        // 小额余额清理逻辑修改
    TaskListAdVideoReardNum      *SampleData                    `json:"taskListAdVideoReardNum"`    // 激励视频奖励值实验 副标题修改为:看一次广告最高可得999金豆
    TaskListAdVideoFirstReward   *SampleData                    `json:"taskListAdVideoFirstReward"` // 每日首个激励视频奖励 副标题修改为:每日首次看广告金豆翻倍XXX *2
    UcenterAmountArea            *UcenterAmountAreaSampleData   `json:"ucenterAmountArea"`          // 激励视频引导限制 三餐、喝水、换金豆弹窗上激励视频引导弹窗
    TaskGuideCompress            *TaskGuideCompress             `json:"taskGuideCompress"`          // 引导任务压缩开关
    PushPrivateConf              *PushPrivateConf               `json:"pushPrivate"`
    PaymentAutoReward            *SampleData                    `json:"paymentAutoReward"`            // 上下滑首个奖励自动发放
    PaymentCoinNotify            *PaymentCoinNotifyConf         `json:"paymentCoinNotify"`            // 上下滑金豆奖励增加通知（顶部）
    VideoTaskGuideUTS            *SampleData                    `json:"videoTaskGuideUTS"`            // 激励视频弹窗引导次数控制开关
    UCenterAreaOptimize          *CommonSidConf                 `json:"ucenterAreaOptimize"`          // 资产挂件优化
    PaymentTaskGuideToPanel      *SampleData                    `json:"paymentTaskGuideToPanel"`      // 上线滑任务引导任务面板
    PaymentTaskGuideToDrinkSigin *SampleData                    `json:"paymentTaskGuideToDrinkSigin"` // 上线滑任务引导喝水签到
    TaskWeChatGroupWxToUID       *SampleData                    `json:"taskWeChatGroupWxToUID"`       // 任务面板微信绑定百度uid
    TaskWealthExtraTitle         *SampleData                    `json:"taskWealthExtraTitle"`         // 时长任务额外奖励标题实验
    TaskWealthExtraTitleNoRed    *SampleData                    `json:"taskWealthExtraTitleNoRed"`    // 时长任务额外奖励标题不飘红
    WelfareRewardAnimation       *WelfareRewardAnimationConf    `json:"welfareRewardAnimation"`       // 签到动效
    WelfareCoolingEndDate        *SampleData                    `json:"welfareCoolingEndDate"`        // 冷却期结束时间
    TaskListBubble               *SampleData                    `json:"taskListBubble"`               // 任务列表气泡提示
    CheckInfoBlack               *SampleData                    `json:"checkInfoBlack"`               // 签到信息黑名单
    UserWithdrawCash             *SampleData                    `json:"userWithdrawCash"`             // 提现氛围信息
    VideoBarNotifyOpt            *VideoBarNotifyOpt             `json:"videoBarNotifyOpt"`            // 视频底bar飘新优化
    ResetUcThreshold             *SampleData                    `json:"resetUcThreshold"`             // 重置资产中心提现阈值
    GameCenterSpecialTask        *SampleData                    `json:"gameCenterSpecialTask"`        // 游戏中心特殊游戏
    CaseCheckInUcThreshold       *SampleData                    `json:"caseCheckInUcThreshold"`       // 签到场景下资产中心提现阈值
    PaymentCoinProgressOpt       *SampleData                    `json:"paymentCoinProgressOpt"`       // 上下滑签到金豆进度优化
    VideoRealTimeReward          *SampleData                    `json:"videoRealTimeReward"`          // 激励视频实时奖励
    GeneralTaskBtnYellow         *SampleData                    `json:"generalTaskBtnYellow"`         // 导流任务按钮改为黄色
    CheckIn76WBlack              *SampleData                    `json:"checkIn76WBlack"`              // 签到76w黑名单
    VideoBarPauseTips            *SampleData                    `json:"videoBarPauseTips"`            // 视频底bar暂停出财神提示
    WithdrawHomeUnReceive        *SampleData                    `json:"withdrawHomeUnReceive"`        // 提现首页未领取提示
    CheckInRegressReward         *SampleData                    `json:"checkInRegressReward"`         // 签到奖励扩展
    QRCodeOptExp                 *OneCompareSidConf             `json:"qrCodeOptExp"`                 // 社群二维码过程优化
    SmartSwitchUcThreshold       *SmartSwitchInfo               `json:"smartSwitchUcThreshold"`       // 小额提现开关及门槛信息
    SmartSwitchUpSlide           *SmartSwitchInfo               `json:"smartSwitchUpSlide"`           // 上下滑减发开关信息
    SmartSwitchExchange          *SampleData                    `json:"smartSwitchExchange"`          // 换金豆汇率开关信息
    WithdrawHomeUnReceiveOneDay  *SampleData                    `json:"withdrawHomeUnReceiveOneDay"`  // 提现首页未领取提示 当日
    WeChatTaskSwitch             *SampleData                    `json:"weChatTaskSwitch"`             // 微信社群退场任务开关
}
```

## 文件：'model/data/smaple/sample.go'

```
package smaple

import (
    "errors"
    "fmt"
    "math/rand"
    "strconv"
    "time"

    "icode.baidu.com/baidu/gdp/logit"
    "icode.baidu.com/baidu/searchbox/sboxlib/extension/single"

    libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ierrno"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/mis"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/resource"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/store/redis"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/common"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    dataConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/types"
)



func (usd *UserSampleData) IsPaymentCoinNotify() (bool, bool, int, bool) {
    config, err := usd.cache.GetSampleByApp(usd.productID)
    if err != nil || config == nil || config.PaymentCoinNotify == nil {
        logit.AddNotice(usd.ctx, logit.String("pcn-isValid", "0"))
        return false, false, -1, false
    }
    if config.PaymentCoinNotify.Switch != "1" {
        return false, false, -1, false
    }

    // 判断实验是否命中
    sidCommon := common.NewSIDCommon(usd.ctx)
    isHit1 := sidCommon.IsShowTaskBySID("", config.PaymentCoinNotify.Sids1st)
    isHit2 := sidCommon.IsShowTaskBySID("", config.PaymentCoinNotify.Sids2nd)

    isHit3 := sidCommon.IsShowTaskBySID("", config.PaymentCoinNotify.Sids3rd)
    notifyCnt3 := -1
    if isHit3 {
        notifyCnt3 = config.PaymentCoinNotify.NotifyCnt3rd
    }

    isHitReverse := sidCommon.IsShowTaskBySID("", config.PaymentCoinNotify.SidsReverse)
    return isHit1, isHit2, notifyCnt3, isHitReverse
}

```

## 文件：'model/data/task/new_person.go'

```
package task

import (
    "encoding/json"
    "errors"
    "strconv"
    "time"

    "github.com/spf13/cast"
    "icode.baidu.com/baidu/gdp/logit"
    libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
    libCuid "icode.baidu.com/baidu/jady/ug-duoduo-video/library/cuid"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/resource"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/store/redis"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/dao"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/black"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/common"
    dataConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/smaple"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/types"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/userdata"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/withdraw"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/ugauth"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uts"
)

func (np *NewPerson) GetRedPacketsByUts(utsRequest uts.RequestUTS) (userRedPacket *types.UserRedPacket, err error) {
    if utsRequest.SenceInfo == nil {
        utsRequest.SenceInfo = map[string]*uts.TypeInfo{}
    }
    userData := userdata.NewUserInfoData(np.ctx, np.productID)
    userInfo, _ := userData.GetUserInfo(np.uid)
    if _, ok := utsRequest.SenceInfo[uts.RedPacketUTSType]; !ok && userInfo != nil {

        // 黑名单用户 && 命中实验 断签或完成一个周期后加标识，提现门槛不再拦截，恢复原有的门槛
        vActBlackUser := 0
        userSampleParams := &smaple.UserSampleDataParams{
            ProductID: np.productID,
            Platform:  utsRequest.Platform,
        }
        userSampleData := smaple.NewUserSampleData(np.ctx, userSampleParams)
        blackData := black.NewBlackData(np.ctx, np.productID)
        if userSampleData.IsCaseCheckInUcThreshold() && !blackData.Check76WBlackStatus(np.uid) && blackData.CheckBlackStatus(np.uid) {
            vActBlackUser = 1
            logit.AddNotice(np.ctx, logit.AutoField("GetCycleWelfareFromUTS-GetRedPacketsByUts", "1"))
        }
        utsRequest.SenceInfo[uts.RedPacketUTSType] = &uts.TypeInfo{
            CacheUserLevel:    cast.ToString(userInfo.Level),
            VActDay:           userInfo.VActDay,
            VActDayV2:         userInfo.VActDayV2,
            VActCycle:         userInfo.GetPeriod(),
            FirstRedBagCash:   userInfo.FirstRedBagCash,
            UpSlideRedBagCash: userInfo.UpSlideRedBagCash,
            VActIsBindWeChat: func() int {
                if ugauth.IsBindedWechatPayWithCtx(np.ctx, np.productID, np.uid) {
                    return 1
                }
                return 0
            }(),
            Scene:         utsRequest.Scene,
            VActBlackUser: vActBlackUser,
        }
        if np.uid > 0 {
            userAssetInfo, aErr := userData.GetUserAssetInfo(np.uid, np.productID)
            if aErr != nil {
                logit.AddNotice(np.ctx, logit.Error("GetUserAssetInfo-Error", aErr))
                err = aErr
                return
            }
            if userAssetInfo == nil {
                userAssetInfo = &common.UserAssetAPP{}
            }
            utsRequest.SenceInfo[uts.RedPacketUTSType].AcctCash = userAssetInfo.DisplayMoneyInt
            utsRequest.SenceInfo[uts.RedPacketUTSType].AcctGoldBean = userAssetInfo.DisplayCoin

            objWithdrawData := withdraw.NewWithdrawData(np.ctx, np.productID)
            withdrawSum := objWithdrawData.GetWithdrawSum(np.uid)
            withdrawSumInt := 0
            if len(withdrawSum) <= 0 {
                _, withdrawSumInt, _ = objWithdrawData.SetWithdrawSum(np.uid)
            } else {
                withdrawSumInt, _ = strconv.Atoi(withdrawSum)
            }
            uCenterSumInt, _ := common.InitUserOperation(np.ctx, np.uid).GetUCenterMoneySum(np.productID)
            utsRequest.SenceInfo[uts.RedPacketUTSType].VActWithdraw90 = withdrawSumInt
            utsRequest.SenceInfo[uts.RedPacketUTSType].VActAsset90 = uCenterSumInt
        }
    }
    utsData := uts.NewUTS(np.ctx, np.productID)
    cuid, _ := libCuid.GetFromRequest(np.ctx, np.productID, np.ctx.HTTPRequest())
    utsRewardRes, utsErr := utsData.GetUtsActivityDataByUtsID(np.uid, cuid, &utsRequest, uts.RedPacketUTSType)
    if utsErr != nil || utsRewardRes == nil {
        logit.AddNotice(np.ctx, logit.Error("RequestUTS-fail", err))
        return
    }
    if len(utsRewardRes.FirstRedBagList) == 0 || utsRewardRes.UpSlideRedBag == nil {
        logit.AddNotice(np.ctx, logit.String("redPacketList", "empty"))
        return
    }
    userRedPacket = &types.UserRedPacket{}
    for _, item := range utsRewardRes.FirstRedBagList {
        if item.Value == 0 { //数据不返回
            continue
        }
        rewardType := libConsts.RewardTypeCoin
        if item.ValueType == 1 {
            rewardType = libConsts.RewardTypeMoney
        }
        moneyType := dataConsts.MoneyTypePayRedPacket //小额打款
        //大额红包类型 对应 大额红包
        if item.BigType == dataConsts.BigType {
            moneyType = dataConsts.MoneyTypeBigRedPacket //大额打款
        }
        rewardNode := &types.RedPacket{
            RewardType: rewardType,
            Reward:     item.Value,
            BigType:    item.BigType,
            PayType:    item.PayType,
            MoneyType:  moneyType,
        }
        userRedPacket.FirstRedPacket = append(userRedPacket.FirstRedPacket, rewardNode)
    }

```

## 文件：'model/service/index/dialog.go'

```
package index

import (
    "fmt"
    "strconv"

    "icode.baidu.com/baidu/gdp/extension/gtask"
    "icode.baidu.com/baidu/gdp/logit"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ierrno"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/pblog"
    dataConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/smaple"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/task"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/types"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/userdata"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/wechatgroup"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uts"
)

func (dialog *DialogReq) GetDialog() (dialogRes *DialogRes) {
    dialogRes = new(DialogRes)

    g := &gtask.Group{
        Concurrent:    3,
        AllowSomeFail: true,
    }
    //新人红包弹窗
    g.Go(func() error {
        //非目标用户没有新手红包
        if !dialog.UserInfo.IsTargetUser(dialog.Ctx) {
            logit.AddNotice(dialog.Ctx, logit.String("IsTargetUser", "0"))
            return nil
        }
        newPersonData := task.NewNewPerson(dialog.Ctx, dialog.UID, dialog.ProductID)
        if dialog.userSampleData.IsWeChatWithdraw() {
            dialog.UtsParams.Scene = dataConsts.RedPackageSceneWxAuthorized //支持微信提现参数，默认登录情况下带上参数，实验由策略控制下发为准
        }
        userRedPacket, err := newPersonData.GetRedPackets(false, dialog.UserInfo, dialog.UtsParams)
        if err != nil {
            logit.AddNotice(dialog.Ctx, logit.Error("GetRedPackets", err))
            return err
        }
        if userRedPacket == nil {
            logit.AddNotice(dialog.Ctx, logit.String("getRedPackets", "empty"))
            return err
        }

        //上划红包
        if userRedPacket.SlideRedPacket != nil && userRedPacket.SlideRedPacket.Reward > 0 {
            dialogRes.SlideDialog = &RedPacketDialog{
                Type:    dataConsts.RedPacketTypeSlide,
                Status:  userRedPacket.SlideRedPacket.Status,
                PayType: userRedPacket.SlideRedPacket.PayType,
            }
        }
        //三个红包
        for _, item := range userRedPacket.FirstRedPacket {
            if item.Reward <= 0 {
                continue
            }
            dialogRes.FirstDialog = append(dialogRes.FirstDialog, &RedPacketDialog{
                Type:    dataConsts.MoneyMapToRedPacketType[item.MoneyType],
                Status:  item.Status,
                PayType: item.PayType,
            })
        }
        if len(userRedPacket.FirstRedPacket) >= 2 {
            logit.AddNotice(dialog.Ctx, logit.String("payType", fmt.Sprintf("%d_%d", userRedPacket.FirstRedPacket[0].PayType, userRedPacket.FirstRedPacket[1].PayType)))
        }

        dialog.DoRedPacketIssueLog(dialogRes.FirstDialog)
        return nil
    })

    g.Go(func() error {
        //非目标用户没有组件计时器
        if !dialog.UserInfo.IsTargetUser(dialog.Ctx) {
            logit.AddNotice(dialog.Ctx, logit.String("IsTargetUser", "0"))
            return nil
        }
        //微信组件打款弹窗
        paymentTaskObj := task.NewPaymentTaskObj(dialog.Ctx, dialog.UID, dialog.CUID, dialog.ProductID)
        if paymentTaskObj == nil {
            return nil
        }
        utsParams := dialog.UtsParams
        utsRewardList, _ := paymentTaskObj.GetPaymentList(&utsParams)
        if utsRewardList == nil || len(utsRewardList.RewardList) <= 0 {
            return nil
        }
        dialogRes.PaymentTask = &PaymentTask{
            MoneyNum: utsRewardList.MoneyTypeCount,
            TotalNum: utsRewardList.TaskTotalTimes,
        }
        return nil
    })

    //微信进群奖励弹窗
    g.Go(func() error {
        //有微信社群弹窗标识，才展示弹窗
        if dialog.DialogScene != DialogSceneWechatReward {
            return nil
        }
        if !dialog.UserInfo.IsTargetUser(dialog.Ctx) {
            logit.AddNotice(dialog.Ctx, logit.String("IsTargetUser", "0"))
            return nil
        }
        //调用进群奖励接口
        wechatGroupObj := task.NewTaskWechatGroupRecordObj(dialog.Ctx, dialog.UID, "", dialog.ProductID)
        wechatGroupPopupInfo := wechatGroupObj.NeedPopup()
        if wechatGroupPopupInfo != nil && wechatGroupPopupInfo.NeedPopup {
            dialogRes.WechatGroup = wechatGroupPopupInfo
        }
        drawData := wechatgroup.NewGroupDrawData(dialog.Ctx, dialog.UID, dialog.ProductID)
        //展示及领取(支持多次合并)
        drawInfo, err := drawData.ReceiveDraw(dialog.UserInfo.Period, &dialog.UtsParams)
        if err == nil && drawInfo != nil {
            dialogRes.GroupDrawInfo = drawInfo
        }

        //处理社群签到
        //签到弹窗包含抽奖的屏蔽抽奖弹窗
        var groupSignin *GroupCheckinDialog
        if dialog.userSampleData != nil && dialog.userSampleData.CheckTargetTVersion(DialogSceneWechatGroupCheckinTVersion) {
            checkinData := wechatgroup.NewGroupCheckinData(dialog.Ctx, dialog.UID, dialog.ProductID)
            checkinInfo, _ := checkinData.GetInfo(&dialog.UtsParams)
            if checkinInfo != nil {
                //今日签到未领奖才可弹窗
                if checkinInfo.TodayCheckinType != types.TodayCheckinTypeCheckedButUnReward {
                    return nil
                }
                if len(checkinInfo.GroupCheckinRewardInfoList) <= checkinInfo.CheckinTimes-1 || checkinInfo.CheckinTimes < 1 {
                    logit.AddNotice(dialog.Ctx, logit.AutoField("GroupCheckinRewardInfoList err", checkinInfo))
                    return ierrno.ErrorServerError
                }
                groupCheckinRewardInfo := checkinInfo.GroupCheckinRewardInfoList[checkinInfo.CheckinTimes-1]
                title := GroupCheckinTitle{
                    CommunityRewardType: CommunityRewardTypeCheckin,
                    Text:                "恭喜获得\n福利群签到奖励{x}",
                    Replace: map[string]interface{}{
                        "x": strconv.Itoa(int(groupCheckinRewardInfo.RewardNum)) + "金豆",
                    },
                }
                dialogRes.GroupDrawInfo = nil
                checkinDialog := GroupCheckinDialog{
                    RewardNum:  groupCheckinRewardInfo.RewardNum,
                    RewardType: groupCheckinRewardInfo.RewardType,
                }
                if drawInfo != nil {
                    title.CommunityRewardType = CommunityRewardTypeCheckinAndDraw
                    title.Text = "恭喜获得\n福利群奖励{x}"
                    title.Replace = map[string]interface{}{
                        "x": strconv.Itoa(int(groupCheckinRewardInfo.RewardNum+drawInfo.RewardNum)) + "金豆",
                    }
                    //奖励相同合并,如果奖励类型不同需要再处理
                    checkinDialog.RewardNum += drawInfo.RewardNum

                    //    置空，防止后续进群奖励合并干扰
                    drawInfo = nil
                }
                checkinDialog.Title = title
                dialogRes.GroupExtReward = checkinDialog
                err := checkinData.ReceiveCheckin(&dialog.UtsParams)
                if err != nil {
                    logit.AddNotice(dialog.Ctx, logit.Error("ReceiveCheckin", err))
                }

                groupSignin = &checkinDialog
            }
        }

        //    进群奖励合并
        if dialogRes.WechatGroup != nil && (dialogRes.GroupDrawInfo != nil || dialogRes.GroupExtReward != nil) {
            groupReward := wechatGroupPopupInfo
            drawReward := drawInfo
            signinReward := groupSignin

            //    社群奖励目前都是金豆，直接合并
            if drawReward != nil {
                groupReward.RewardNum += drawReward.RewardNum
                dialogRes.GroupDrawInfo = nil
            }
            if signinReward != nil {
                groupReward.RewardNum += signinReward.RewardNum
                dialogRes.GroupExtReward = nil
            }
            groupReward.Title = task.GenWechatGroupTitle("恭喜您获得\n福利群奖励{x}", groupReward.RewardNum, groupReward.RewardType)
            dialogRes.WechatGroup = groupReward
        }

        return nil
    })
    _, _ = g.Wait()
    logit.AddNotice(dialog.Ctx, logit.AutoField("dialogRes", dialogRes))
    return
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

## 文件：'model/service/index/index.go'

```
package index

import (
    "encoding/json"
    "fmt"
    "strings"
    "time"

    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/smaple"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/task"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/withdraw"

    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/types"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/ugauth"

    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/resource"
    dataConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    thirdUAnti "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uanti"

    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/pblog"

    "icode.baidu.com/baidu/gdp/extension/gtask"
    "icode.baidu.com/baidu/gdp/logit"
    libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ierrno"
    syncTask "icode.baidu.com/baidu/jady/ug-duoduo-video/library/task"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ua"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/userdata"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/service"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uts"
)
func (ddis *DuoDuoIndexService) Exec(ctx *ibase.APIContext) interface{} {
    resp := &Response{}
    resp.IsLogin = "0"
    uid := ddis.params.UID
    productID := ddis.params.ProductID

    // 入口打点
    pblog.StatisticsWelfareInfoPBLog(ctx, productID, uid, ddis.params.CUID, pblog.PbLogAPISrcIndex, pblog.PbLogAPIActionEnter, "no", "no")

    userData := userdata.NewUserInfoData(ctx, productID)
    userSampleParams := &smaple.UserSampleDataParams{
        Version:      ddis.params.UtsParams.Version,
        ProductID:    productID,
        Platform:     ddis.params.UtsParams.Platform,
        TalosVersion: ddis.params.UtsParams.TalosVersion,
    }
    userSample := smaple.NewUserSampleData(ctx, userSampleParams)
    dialogReq := &DialogReq{
        Ctx:            ctx,
        UID:            uid,
        CUID:           ddis.params.CUID,
        ProductID:      productID,
        UtsParams:      ddis.params.UtsParams,
        userSampleData: userSample,
        UserInfo:       &userdata.UserInfo{},
        DialogScene:    ddis.params.DialogScene,
    }
    resp.UserSample = userSample.GetUserSample()
    if ddis.params.UID <= 0 {
        resp.DiaLog = dialogReq.ULWeChatWithdrawGetDialog()
        //    迁移basic未登录红包兜底逻辑(未登录下发pay假红包，引导登录)
        if resp.DiaLog == nil {
            resp.DiaLog = &DialogRes{
                FirstDialog: []*RedPacketDialog{
                    {
                        Type:   consts.RedPacketTypePay,
                        Status: dataConsts.RedPacketCanReceived,
                    },
                },
            }
        }
        if len(resp.DiaLog.FirstDialog) == 0 {
            resp.DiaLog.FirstDialog = []*RedPacketDialog{
                {
                    Type:   consts.RedPacketTypePay,
                    Status: dataConsts.RedPacketCanReceived,
                },
            }
        }
        //    未登录红包打点
        dialogReq.DoRedPacketIssueLog(resp.DiaLog.FirstDialog)

        userLevel := userData.GetUserLevelByUtsCache(ddis.params.UID)
        pblog.WriteJoin(ctx, 0, ddis.params.CUID, ddis.params.ProductID, false, userLevel) //未登录不清楚是否首次
        return resp
    }
    //登录逻辑
    resp.IsLogin = "1"
    userInfo, err := userData.GetUserInfo(uid)
    if err != nil {
        return resp
    }
    dialogReq.UserInfo = userInfo
    resp.UserType = userInfo.GetUserType()
    resp.FirstTime = userInfo.FirstTime
    if userInfo.FirstTime == 0 {
        resp.FirstTime = time.Now().Unix()
    }
    resp.IsSign = "1"
    resp.Period = userInfo.Period
    resp.Day = userInfo.GetNewUserFirstDateDay()
    isFirstDay := false
    if userInfo.IsFirstDayUser() {
        isFirstDay = true
    }
    // 是否强制目标用户
    if userData.IsForceTargetUser(ctx, uid) {
        resp.Force = "1"
    }
    shareReq := &ShareReq{
        Ctx:       ctx,
        UID:       uid,
        CUID:      ddis.params.CUID,
        ProductID: productID,
    }

    g := &gtask.Group{
        Concurrent:    3,
        AllowSomeFail: true,
    }
    //新人红包弹窗
    g.Go(func() error {
        resp.DiaLog = dialogReq.GetDialog()
        return nil
    })

    //提现信息和签到信息和openid信息
    g.Go(func() error {
        isSign, infoCode := ddis.GetSign(ctx, userInfo)
        resp.IsSign = isSign
        resp.InfoCode = infoCode

        resp.WxBind, resp.WithdrawLeft = ddis.processWithdraw(ctx, userInfo)
        return nil
    })

    //反作弊信息
    g.Go(func() error {
        resp.HitAntiCheat = "0"
        //请求微信社群弹窗，不请求风控，直接返回
        if ddis.params.DialogScene == DialogSceneWechatReward {
            return nil
        }
        if !ddis.IsSafe(ctx) { //不安全
            resp.HitAntiCheat = "1"
        }
        return nil
    })

    g.Go(func() error { //处理分享回流
        if len(ddis.params.ShareToken) <= 0 {
            return nil
        }
        _ = shareReq.ProcessShare(ddis.params.ShareToken)
        return nil
    })

    _, err = g.Wait()
    if err != nil {
        logit.AddNotice(ctx, logit.Error("DuoDuoIndexService-fail", err))
        return ierrno.ErrorServerError
    }
    if userInfo.FirstTime <= 0 { //更新首次到访首页时间
        _ = resource.QueueClient.Produce(ctx, syncTask.Message{TaskType: dataConsts.UserService, DataType: dataConsts.UserServiceDataTypeJoin, UID: uid, ProductID: ddis.params.ProductID, Period: userInfo.Period})
    }
    userLevel := userData.GetUserLevelByUtsCache(ddis.params.UID)
    finalInfoCode := "nil"
    if resp != nil {
        finalInfoCode = fmt.Sprintf("%s-%s", resp.HitAntiCheat, resp.InfoCode)
    }
    pblog.StatisticsWelfareInfoPBLog(ctx, productID, uid, ddis.params.CUID, pblog.PbLogAPISrcIndex, pblog.PbLogAPIActionLeave, resp.IsSign, finalInfoCode)
    pblog.WriteJoin(ctx, uid, ddis.params.CUID, ddis.params.ProductID, isFirstDay, userLevel)
    return resp
}

```

## 文件接口router层定义

```go
func InitDuoDuo(r ghttp.Router) {
    r = r.Group("/video", middlewares.SetAppName(false)) //duoduo ==> video
    //端内请求
    {
        externalRouter := r.Group("/external", middlewares.InternalCUID(), middlewares.InternalUID(), middlewares.CheckLogin(false), middlewares.UserType(), middlewares.UcMoneyExpire())
        externalRouter.HandleFunc("GET,POST", "index", index.FuncIndexController, middlewares.CheckLogin(false), middlewares.UserInactive(), middlewares.MergeNoLoginReward())
}

```

## 文件controller 层定义

```
package index

import (
    "context"
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/controller"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/service/index"
)

// Controller _
type Controller struct {
    controller.Controller
}

// NewIndexController _
func NewIndexController() *Controller {
    instance := new(Controller)
    instance.BaseController = controller.NewBaseController()
    instance.ResponseType = "json"
    instance.ExecLogicInterface = index.NewDuoDuoIndexService()
    return instance
}

// FuncIndexController _
func FuncIndexController(ctx context.Context, req ghttp.Request) ghttp.Response {
    return NewIndexController().Execute(ctx, req)
}
```

## data层Execute具体实现

```go
package index

import (
    "encoding/json"
    "fmt"
    "strings"
    "time"

    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/smaple"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/task"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/withdraw"

    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/types"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/ugauth"

    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/resource"
    dataConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/consts"
    thirdUAnti "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uanti"

    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/pblog"

    "icode.baidu.com/baidu/gdp/extension/gtask"
    "icode.baidu.com/baidu/gdp/logit"
    libConsts "icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ibase"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ierrno"
    syncTask "icode.baidu.com/baidu/jady/ug-duoduo-video/library/task"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/ua"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/data/userdata"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/model/service"
    "icode.baidu.com/baidu/jady/ug-duoduo-video/thirdparty/uts"
)

// Request 参数
type Request struct {
    ProductID   int    `form:"productid" json:"productid"` // 产品线id
    Version     string `form:"version" json:"version"`
    CUID        string `form:"cuid" json:"cuid"`
    Zid         string `form:"zid" json:"zid"`
    Sid         string `form:"sid" json:"sid"`
    UID         uint64 `form:"uid" json:"uid"`
    Cua         string `form:"cua" json:"cua"`
    Cen         string `form:"cen" json:"cen"`
    Cfrom       string `form:"cfrom" json:"cfrom"`
    Network     string `form:"network" json:"network"`
    DialogScene string `form:"dialogScene" json:"dialogScene"` //弹窗场景
    Uname       string
    ShareToken  string `form:"shareToken" json:"shareToken"`
    UtsParams   uts.RequestUTS
}

// Response ...
type Response struct {
    Force        string            `json:"force"`
    Day          int64             `json:"day"`
    Period       int64             `json:"period"`
    WithdrawLeft int64             `json:"withdrawLeft"`
    FirstTime    int64             `json:"firstTime"`
    UserType     string            `json:"userType"`
    IsSign       string            `json:"isSign"`
    IsLogin      string            `json:"isLogin"`
    HitAntiCheat string            `json:"hitAntiCheat"` // 0-未命中反作弊（默认），1-命中反作弊；
    DiaLog       *DialogRes        `json:"dialog"`
    UserAsset    UserAssetAPP      `json:"user_asset"`
    UserSample   *types.UserSample `json:"userSample"`
    WxBind       int               `json:"wxBind"`
    InfoCode     string
}

// UserAssetAPP 用户信息结构体
type UserAssetAPP struct {
    DisplayMoneyInt int64 `mapstructure:"money,omitempty" json:"money"`
    DisplayCoin     int64 `mapstructure:"coin,omitempty" json:"coin"`
    Prize           int64 `mapstructure:"prize,omitempty" json:"prize"`
}

// DuoDuoIndexService _
type DuoDuoIndexService struct {
    *service.BaseService
    params *Request
}

// NewDuoDuoIndexService _
func NewDuoDuoIndexService() ibase.ExecLogicInterface {
    instance := new(DuoDuoIndexService)
    return instance
}

// Exec _
func (ddis *DuoDuoIndexService) Exec(ctx *ibase.APIContext) interface{} {
    resp := &Response{}
    resp.IsLogin = "0"
    uid := ddis.params.UID
    productID := ddis.params.ProductID

    // 入口打点
    pblog.StatisticsWelfareInfoPBLog(ctx, productID, uid, ddis.params.CUID, pblog.PbLogAPISrcIndex, pblog.PbLogAPIActionEnter, "no", "no")

    userData := userdata.NewUserInfoData(ctx, productID)
    userSampleParams := &smaple.UserSampleDataParams{
        Version:      ddis.params.UtsParams.Version,
        ProductID:    productID,
        Platform:     ddis.params.UtsParams.Platform,
        TalosVersion: ddis.params.UtsParams.TalosVersion,
    }
    userSample := smaple.NewUserSampleData(ctx, userSampleParams)
    dialogReq := &DialogReq{
        Ctx:            ctx,
        UID:            uid,
        CUID:           ddis.params.CUID,
        ProductID:      productID,
        UtsParams:      ddis.params.UtsParams,
        userSampleData: userSample,
        UserInfo:       &userdata.UserInfo{},
        DialogScene:    ddis.params.DialogScene,
    }
    resp.UserSample = userSample.GetUserSample()
    if ddis.params.UID <= 0 {
        resp.DiaLog = dialogReq.ULWeChatWithdrawGetDialog()
        //    迁移basic未登录红包兜底逻辑(未登录下发pay假红包，引导登录)
        if resp.DiaLog == nil {
            resp.DiaLog = &DialogRes{
                FirstDialog: []*RedPacketDialog{
                    {
                        Type:   consts.RedPacketTypePay,
                        Status: dataConsts.RedPacketCanReceived,
                    },
                },
            }
        }
        if len(resp.DiaLog.FirstDialog) == 0 {
            resp.DiaLog.FirstDialog = []*RedPacketDialog{
                {
                    Type:   consts.RedPacketTypePay,
                    Status: dataConsts.RedPacketCanReceived,
                },
            }
        }
        //    未登录红包打点
        dialogReq.DoRedPacketIssueLog(resp.DiaLog.FirstDialog)

        userLevel := userData.GetUserLevelByUtsCache(ddis.params.UID)
        pblog.WriteJoin(ctx, 0, ddis.params.CUID, ddis.params.ProductID, false, userLevel) //未登录不清楚是否首次
        return resp
    }
    //登录逻辑
    resp.IsLogin = "1"
    userInfo, err := userData.GetUserInfo(uid)
    if err != nil {
        return resp
    }
    dialogReq.UserInfo = userInfo
    resp.UserType = userInfo.GetUserType()
    resp.FirstTime = userInfo.FirstTime
    if userInfo.FirstTime == 0 {
        resp.FirstTime = time.Now().Unix()
    }
    resp.IsSign = "1"
    resp.Period = userInfo.Period
    resp.Day = userInfo.GetNewUserFirstDateDay()
    isFirstDay := false
    if userInfo.IsFirstDayUser() {
        isFirstDay = true
    }
    // 是否强制目标用户
    if userData.IsForceTargetUser(ctx, uid) {
        resp.Force = "1"
    }
    shareReq := &ShareReq{
        Ctx:       ctx,
        UID:       uid,
        CUID:      ddis.params.CUID,
        ProductID: productID,
    }

    g := &gtask.Group{
        Concurrent:    3,
        AllowSomeFail: true,
    }
    //新人红包弹窗
    g.Go(func() error {
        resp.DiaLog = dialogReq.GetDialog()
        return nil
    })

    //提现信息和签到信息和openid信息
    g.Go(func() error {
        isSign, infoCode := ddis.GetSign(ctx, userInfo)
        resp.IsSign = isSign
        resp.InfoCode = infoCode

        resp.WxBind, resp.WithdrawLeft = ddis.processWithdraw(ctx, userInfo)
        return nil
    })

    //反作弊信息
    g.Go(func() error {
        resp.HitAntiCheat = "0"
        //请求微信社群弹窗，不请求风控，直接返回
        if ddis.params.DialogScene == DialogSceneWechatReward {
            return nil
        }
        if !ddis.IsSafe(ctx) { //不安全
            resp.HitAntiCheat = "1"
        }
        return nil
    })

    g.Go(func() error { //处理分享回流
        if len(ddis.params.ShareToken) <= 0 {
            return nil
        }
        _ = shareReq.ProcessShare(ddis.params.ShareToken)
        return nil
    })

    _, err = g.Wait()
    if err != nil {
        logit.AddNotice(ctx, logit.Error("DuoDuoIndexService-fail", err))
        return ierrno.ErrorServerError
    }
    if userInfo.FirstTime <= 0 { //更新首次到访首页时间
        _ = resource.QueueClient.Produce(ctx, syncTask.Message{TaskType: dataConsts.UserService, DataType: dataConsts.UserServiceDataTypeJoin, UID: uid, ProductID: ddis.params.ProductID, Period: userInfo.Period})
    }
    userLevel := userData.GetUserLevelByUtsCache(ddis.params.UID)
    finalInfoCode := "nil"
    if resp != nil {
        finalInfoCode = fmt.Sprintf("%s-%s", resp.HitAntiCheat, resp.InfoCode)
    }
    pblog.StatisticsWelfareInfoPBLog(ctx, productID, uid, ddis.params.CUID, pblog.PbLogAPISrcIndex, pblog.PbLogAPIActionLeave, resp.IsSign, finalInfoCode)
    pblog.WriteJoin(ctx, uid, ddis.params.CUID, ddis.params.ProductID, isFirstDay, userLevel)
    return resp
}
```

请根据上面的接口代码内容，并参考当前项目代码风格，进行接下来的开发任务。当前代码库为sbox-baisc模块的上游调用方，当前接口为弹窗相关信息处理接口，主要变更如下：

1. 新增实验配置信息
   - 增加红包奖励实验配置
   - 增加上滑引导界面关闭实验配置
2. 小额奖励信息抽取方法提取
   - 将原资产奖励信息获取提取成公共方法，可用于小额奖励信息的提取
   - 返回体即定义为小额资产红包的返回（NotifyInfo）
3. 新增实验命中判断
   - 新增红包奖励优化实验命中判断
   - 新增上滑引导界面关闭命中判断
4. 实验执行
   a 红包奖励实验执行，判断是否命中红包实验：
   - 若命中，则执行：
   - 红包文案修改为“立得微信打款”
   - 进入新的红包逻辑（奖励类型、数量等更改）
   - 若未命中，保持原有逻辑执行
   b 上滑引导界面实验执行，判断是否命中引导优化实验：
   - 若命中：则进入新增引导优化逻辑（点击空白页面关闭引导弹窗）
   - 若未命中：则保持原有逻辑执行主要变更内容如下
   5.提取 model/data/task/task_payment.go 的资产奖励信息提取成公共方法：
   - 新增通用方法，统一收敛，和提供给前端的小额资产信息是类似的。将工具函数开发到如下路径：library/util/notify.go文件
   - 如果在以上需求中使用到了该文件需要额外表明。

请输出你修改后的完整代码并标出修改的部分：
