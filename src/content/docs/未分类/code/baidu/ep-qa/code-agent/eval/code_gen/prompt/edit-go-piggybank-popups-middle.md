---
title: "edit-go-piggybank-popups-middle"
description: "你是一个 go 服务端开发工程师，你正在开发一个存钱罐业务，其中弹窗展示信息接口，从下游ug-duoduo调用多个接口获取不同任务的弹窗展示信息。下面是一个上滑引导接口的全部代码："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\eval\\code_gen\\prompt\\edit-go-piggybank-popups-middle.md"
---
你是一个 go 服务端开发工程师，你正在开发一个存钱罐业务，其中弹窗展示信息接口，从下游ug-duoduo调用多个接口获取不同任务的弹窗展示信息。下面是一个上滑引导接口的全部代码：

## 文件：'model/data/ddmissionpopup/slideredpackage.go'

```go

package ddmissionpopup


import (

"context"

"encoding/json"

"strings"


"icode.baidu.com/baidu/gdp/logit"

    params "icode.baidu.com/baidu/searchbox/symframe-param"


"icode.baidu.com/baidu/searchbox/sbox-basic/library/logger"

    missionDao "icode.baidu.com/baidu/searchbox/sbox-basic/model/dao/mission"

    pdcmsDao "icode.baidu.com/baidu/searchbox/sbox-basic/model/dao/pdcms"

"icode.baidu.com/baidu/searchbox/sbox-basic/model/data/ddmissionpopup/types"

)



func (p *SlideRedPackage) RewardPopup(ctx context.Context) (*types.RewardPopup, bool) {

result := &types.RewardPopup{}

adapt, _ := params.LoadAdaption(ctx)

// 获取实验组信息

expType := GetExpType(ctx)

    result.SetExpType(expType)


// 未命中命中未登录领奖励用户的未登录用户直接返回

if !adapt.IsLogin() && expType == ExpTypeDefault {

returnnil, true

    }


mResp, err := p.daoMission.GetDDRedPackages(ctx, "")

if err != nil {

        logger.WarningF(ctx, "slide red package request mission GetDDRedPackages failed. %s", err.Error())

returnnil, true

    }

if mResp == nil {

        logger.WarningF(ctx, "slide red package request mission GetDDRedPackages is nil.")

returnnil, true

    }


// 新用户

userType := "1"

if mResp.Period > 1 {

// 连续20天没来 第22天回归

userType = "2"

    }


if mResp.Dialog.SlideRedPacket == nil {

returnnil, true

    }


// 已领红包则过滤

if mResp.Dialog.SlideRedPacket.Status == 1 {

return result, true

    }


pdcmsData, err := p.daoPdcms.GetDuoduoVideoRewardRedPackage(ctx, userType)

if err != nil {

        logger.WarningF(ctx, "slide pdcms userType:%s GetDuoduoVideoRewardRedPackage failed. %s", userType, err.Error())

returnnil, true

    }


if pdcmsData == nil {

        logger.WarningF(ctx, "slide pdcms userType:%s GetDuoduoVideoRewardRedPackage data is nil", userType)

returnnil, true

    }


material := pdcmsData.Slide


rData := map[string]interface{}{

"text":     material.Text,

"sub_text": material.SubText,

"icon":     material.Icon,

    }

    result.SetData(rData)

return result, false

}

```

## 文件：'model/data/ddmissionpopup/popup.go'

```

package ddmissionpopup


import (

    "context"


    "icode.baidu.com/baidu/searchbox/sbox-basic/library/logger"

    "icode.baidu.com/baidu/searchbox/sbox-basic/model/data/ddmissionpopup/types"

)


const (

    PopupKeyRedPackage         = "red_package"          // 新手红包

    PopupKeySlideRedPackage    = "slide_red_package"    // 滑动红包

    PopupKeyWithdraw           = "withdraw"             // 提现弹窗

    PopupKeyWelfare            = "welfare"              // 七天签到弹窗

    PopupKeyPayment            = "payment"              // 上滑打款弹窗

    PopupKeyUnloginClearRemind = "unlogin_clear_remind" // 未登录清理资产弹窗

    PopupKeyTurnLogin          = "guest_login_guide"    // 游客转正弹窗

    PopupKeyDrinkWater         = "drinkWater"           // 喝水打卡弹窗

    PopUpKeyWatchADVideo       = "watchADVideo"         // 观看广告赚翻倍金豆弹窗

    PopUpKeyCornucopia         = "cornucopia"           // 聚宝盆

    PopUpKeyThreeMeals         = "eat"                  // 三餐任务

    PopUpKeyEarnCash           = "6881"                 // 连续n天打卡赚现金

    PopUpKeyTakePat            = "takepat"              // 拍一拍

    PopupWechatReward          = "wechatReward"         // 微信进群奖励 && 抽奖弹窗

    PopupPlayletSigninDialog   = "playletSigninDialog"  // 短剧签到弹窗信息

    PopupKeyKeepSignIn         = "keepSignIn"           // 短剧签到弹窗信息

    PopupKeyVideoCallBack      = "videoCallback"        // 挂机用户挽回奖励弹窗

    PopupKeyImmersionUpgrade   = "immersionUpgrade"     // 沉浸式首页弹窗信息

)


//go:generate mockgen -destination mock/mock.go -package mock icode.baidu.com/baidu/searchbox/sbox-basic/model/data/ddmissionpopup Popup

type Popup interface {

    RewardPopup(ctx context.Context) (*types.RewardPopup, bool)

    ReceivePopup(ctx context.Context) *types.ReceivePopup

}


type Popups struct {

    popupKeys             []string            // 要处理的弹窗标识列表

    needRealTimePopupKeys map[string]struct{} // 需要实时请求的弹窗

    popupMap              map[string]Popup    // 弹窗处理实体

}


func NewPopups(popupKeyList ...string) *Popups {

    return &Popups{

        popupKeys:             popupKeyList,

        needRealTimePopupKeys: make(map[string]struct{}, len(popupKeyList)),

        popupMap: map[string]Popup{

            PopupKeyRedPackage:         NewRedPackage(),

            PopupKeySlideRedPackage:    NewSlideRedPackage(),

            PopupKeyWithdraw:           NewWithdraw(),

            PopupKeyWelfare:            NewWelfare(),

            PopupKeyPayment:            NewPayment(),

            PopupKeyUnloginClearRemind: NewClearUnloginRemind(),

            PopupKeyTurnLogin:          NewTurnLogin(),

            PopupKeyDrinkWater:         NewDrinkWater(),

            PopUpKeyWatchADVideo:       NewWatchAdsVideo(),

            PopUpKeyCornucopia:         NewCornucopia(),

            PopUpKeyThreeMeals:         NewThreeMeals(),

            PopUpKeyEarnCash:           NewEarnCash(),

            PopUpKeyTakePat:            NewTakePat(),

            PopupWechatReward:          NewWechatReward(),

            PopupPlayletSigninDialog:   NewWealthPlayletSigninDialog(),

            PopupKeyKeepSignIn:         NewKeepSignIn(),

            PopupKeyVideoCallBack:      NewVideoCallBack(),

            PopupKeyImmersionUpgrade:   NewImmersionUpgrade(),

        },

    }

}


func (p *Popups) SetNeedRealTimePopup(popupKey ...string) {

    for _, s := range popupKey {

        p.needRealTimePopupKeys[s] = struct{}{}

    }

}


// GetRewardPopups 获取奖励弹窗

func (p *Popups) GetRewardPopups(ctx context.Context) []*types.RewardPopupResp {

    result := make([]*types.RewardPopupResp, 0, len(p.popupKeys))

    for _, key := range p.popupKeys {

        if _, ok := p.needRealTimePopupKeys[key]; ok {

            result = append(result, &types.RewardPopupResp{

                Type:       key,

                IsRealtime: "1",

                Data:       struct{}{},

            })

            continue

        }


        if _, ok := p.popupMap[key]; !ok {

            logger.WarningF(ctx, "GetRewardPopups key:%s obj is null", key)

            continue

        }


        popupData, isFilter := p.popupMap[key].RewardPopup(ctx)

        if isFilter {

            continue

        }


        data := map[string]any{}

        if popupData != nil {

            data = popupData.GetData()

        }


        result = append(result, &types.RewardPopupResp{

            Type:       key,

            IsRealtime: "0",

            Data:       data,

        })

    }

    return result

}


func (p *Popups) GetReceivedPopups(ctx context.Context) map[string]any {

    result := make(map[string]any, 1)

    for _, key := range p.popupKeys {

        if _, ok := p.popupMap[key]; !ok {

            logger.WarningF(ctx, "GetReceivedPopups key:%s obj is null", key)

            continue

        }


        pr := p.popupMap[key].ReceivePopup(ctx)

        if pr == nil {

            result[key] = struct{}{}

            continue

        }

        pr.Data["status"] = pr.Status

        pr.Data["failed_type"] = pr.FailedType

        pr.Data["hit_anti_cheat"] = pr.HitAntiCheat

        result[key] = pr.Data

    }

    return result

}


```

## 文件：'model/service/ddmission/types.go'

```go


package ddmission


import (

    dto "icode.baidu.com/baidu/searchbox/sbox-basic/model/types/dto/mission"

)



// PopupResp 序列弹窗接口返回

typePopupRespstruct {

    IsTargetUser          string`json:"is_target_user"`

    WithdrawCountdown     int64`json:"withdraw_countdown"`

    ReActiveVersion       int64`json:"re_active_version"`

    HitAntiCheat          string`json:"hit_anti_cheat"`

    HitVideoDirectShowExp string`json:"hit_video_direct_show_exp"`

    Popup                 any    `json:"popup"`

}



```

## 文件：'model/types/dto/mission/ddmissionpopup.go'

```go

package mission


// DDRedPackageResp 多多视频新手红包、上划红包信息

typeDDRedPackageRespstruct {

    Day          int`json:"day"`

    Period       int`json:"period"`// 期数，值大于1 代表回归用户

    WithdrawLeft int64`json:"withdrawLeft"`

    FirstTime    int64`json:"firstTime"`

    IsSign       string`json:"isSign"`

    IsLogin      string`json:"isLogin"`

    HitAntiCheat string`json:"hitAntiCheat"`// 0-未命中反作弊（默认），1-命中反作弊

    WxBind       *int`json:"wxBind"`// 微信绑定, 0-未绑定 1-绑定

    IsForce      string`json:"isForce"`//是否强制命中,1-是强制命中 ""-字符串是非强制命中

    Dialog       struct {

        FirstRedPacket []DDRedPackageFirstRedPacket `json:"firstRedPacket"`

        SlideRedPacket *struct {

            Type   string`json:"type"`

            Status int`json:"status"`

        } `json:"slideRedPacket"`

        PaymentTask *struct {

            MoneyNum int`json:"moneyNum"`// 奖励次数，升级前

            TotalNum int`json:"totalNum"`// 奖励次数，升级后

        } `json:"paymentTask"`// 小额支付弹窗

        GroupDraw *struct {

            RewardNum  int`json:"rewardNum"`// 奖励数

            RewardType string`json:"rewardType"`// 奖励类型

            Status     int`json:"status"`// 状态，0-未领取 1-已领取

            Title      any    `json:"title"`// 标题

        } `json:"groupDraw,omitempty"`

        WechatGroup *struct {

            RewardNum  int`json:"rewardNum"`// 奖励数

            RewardType string`json:"rewardType"`// 奖励类型

            Title      any    `json:"title"`// 标题

        } `json:"wechatGroup,omitempty"`

        GroupExtReward *struct {

            RewardNum  int64`json:"rewardNum"`

            RewardType string`json:"rewardType"`

            Title      GroupCheckinTitle `json:"title"`

        } `json:"groupExtReward,omitempty"`

    } `json:"dialog"`

    UserAsset struct {

        Money int`json:"money"`

        Coin  int`json:"coin"`

        Prize int`json:"prize"`

    } `json:"user_asset"`

    UserSample *UserSample `json:"userSample"`

}

```

请根据上面的接口代码内容，并参考当前项目代码风格，进行接下来的开发任务，当前代码库为中转代码库，用于透传各种信息，为上游调用方提供信息解析能力&方便实验，当前接口是弹窗相关信息透传接口，主要变更逻辑如下：

1. 新增上滑引导页面字段透传
    - 增加pay_type字段，用来区分奖励类型，支持新增的小额资产奖励类；以前默认是大额现金奖励
- 新增引导文案透传：从上滑引导界面获取引导文案并解析至新增字段；
    - 原来的文案在pdcms配置中心配置，这次通过ugduoduo透传，在ugduoduo做实验控制
- 新增奖励类型透传：从上滑引导界面获取奖励类型并解析至新增字段；


2. 弹窗响应信息添加实验命中返回字段

- 新增奖励控制字段
- 新增关闭控制字段

3. 奖励响应信息添加实验命中+奖励类型字段
- 新增2个字段，代表2个实验命中情况，分别是：HitslideupGuideRewardExp ,HitSlideupGuideUeExp
- 新增实验字段定义结构：PopupResp

- 新增奖励控制字段
- 新增关闭控制字段
* 类型：DDRedPackageResp
* 结构：新增字段，实验标记+奖励类型

4. 红包字段中子字段新增类型字段PopupResp

请输出你修改后的完整代码并标出修改的部分,然后为每一个函数增加单元测试：
