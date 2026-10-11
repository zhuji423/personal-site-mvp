---
title: "BWEwmdF9ED3EQ6"
description: "流畅播-新增激励广告变现方式"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\lib\\req_agent\\ku\\BWEwmdF9ED3EQ6.md"
---
流畅播-新增激励广告变现方式

父需求[[ailite-27822] 【6.43】流畅播路径优化二期](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-27822/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk)

子需求[[ailite-27832] 【6.43】【P0】新增激励广告变现方式](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-27832/show?source=drawer-header?t=mention&mt=doc&dt=sdk)

任务地址 [https://gt.baidu-int.com/#/consumer/362](https://gt.baidu-int.com/#/consumer/362)

## 项目背景
搜索第三方免费资源存在播放卡顿、站点不稳定问题，希望结合流畅播能力，优化整体播放链路，提升用户免费资源视频观看体验。

## 需求描述
![父需求图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a6dd224622c540ce9da9bb5551c9f343&docGuid=BWEwmdF9ED3EQ6 "父需求图")
用户满足触发条件，可通过完成激励广告获得流畅播权益

~~自行计数端成本较高，本期是否可以直接消耗不计数--pm~~

~~会员侧待反馈，若评估不通过，需求可能hold--pm下午给反馈~~

~~极速版&主版免费次数和广告免费次数需要分别计数，涉及到免费次数计算的地方，需要端从两个资源池获取，分别消耗，~~~~消耗优先级待定--pm~~

简化做，任务成功端上直接调网盘流畅播能力，当场消耗，无需技术--pm已确认

~~端是怎么消耗免费次数，吊起流畅播能力的呢，会员侧没有次数校验吗---pm和网盘侧具体了解一下次数限制，非会员可能一天只有5次，uid唯独，是否区分产品线未知--pm回复无限制~~

### 2.1 触发条件
|条件|判断方|备注|
|-|-|-|
|用户点击流畅播 |端||
|当前不是会员|端||
|无免费次数|端|由于要拆分计数，此处的免费次数要从两个数据源获取，以及从两个数据源消耗 server新增广告奖励查询和消耗接口，端合并判断|
|符合看广告任务条件|server|sid开关为true，可以灵活下线广告功能 登录 广告任务剩余次数>0 query非色情判断--pm待定|
|实验开关|端|端上针对流畅播整体需求有一个开关|
||server|server针对广告需求有一个子开关，方便单独下线子功能 子开关关闭，查询接口均返回0/false，即端上不会再请求任务相关逻辑|
### 2.2 任务奖励
完成看广告任务，增加1次流畅播权益，当场消费，~~x可配，~~

btn文案由端写死吗--云控

任务中台次数配置不为0

~~完成任务server会自动增加用户权益(中台回调)，之后端需要再刷新获取一下当前权益次数吗？目前线上消耗逻辑是什么~~

|场景|文案|下发方|备注|
|-|-|-|-|
|完成任务|恭喜获得一次流畅播权益|端|和yiyao沟通过，任务完成进度均由端取巧判断，server不介入|
|未完成任务|第一行：“视频未看完”，第二行“时长领取失败”|端||
|未请求到广告|第一行：“视频走丢了”，第二行：“送你一次流畅播权益”|端|和pm讨论过，不建议直接送权益，icafe待明确；以及任务完成失败的情况，是否也收拢到该场景，toast类似完成失败--pm 不送权益--pm确定，不申请反作弊，文案待改|
### 2.3 流程图
[流程图]
## 方案设计
### ~~3.1 【废弃】任务完成权益查询接口--对端~~
[流程图]
#### ~~3.1.1 流程图~~
#### ~~3.1.2 协议~~
~~req~~

|PATH|/baiduboxapp/basic/liuchangbo/vipsearch|
|-|-|
|METHOD|Get|
|Content-Type|application/x-www-form-urlencoded|
|Get参数|客户端公参|
~~rsp~~

```
{
  "errno": "0",
  "timestamp": "1727163750",
  "logid": "3349410503",
  "data": {
      "remainTimes": 3 // 剩余次数
  }
}
```
### ~~3.2 【废弃】任务完成权益消耗接口--对端~~
#### ~~3.2.1 流程图~~
[流程图]
#### ~~3.2.2 协议~~
~~req~~

|PATH|/baiduboxapp/basic/liuchangbo/vipconsume|
|-|-|
|METHOD|Post|
|Content-Type|application/x-www-form-urlencoded|
|Get参数|客户端公参|
|Post参数|{
"consumeTimes": 1 // 默认用1即可
} 端控制consumeTimes <=remainTimes且consumeTimes >0|
~~rsp~~

```
{
  "errno": "0",
  "timestamp": "1727163750",
  "logid": "3349410503",
  "data": {
      "remainTimes": 3 // 消耗后剩余次数
  }
}
```
### 3.3 任务查询接口--对端
任务中台查询接口[获取任务列表](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/6A-UXrf3Ha/qnvCs34rxl/HFW9oCPh-ipJu5?t=mention&mt=doc&dt=doc)

#### 3.3.1 流程图
[流程图]
#### 3.3.2 协议
req

|PATH|/baiduboxapp/basic/smoothplay/tasklist|
|-|-|
|METHOD|Get|
|Content-Type|application/x-www-form-urlencoded|
|Get参数|客户端公参|
uid cuid appversion强校验

rsp

* data list形式为了后续扩展 本次只有广告任务
* 是否展示任务的判断
  * 1-isvalid=false -- 不展示广告，展示会员卡
  * 2-isvalid=true 
    * 2-1 len(task)==0 -- 不展示广告，展示会员卡
    * 2-2 len(task)>0
      * 2-2-1 遍历task list 找到一个task.isvalid=true的任务 --展示广告，~~根据videotype调整btn顺序~~
      * 2-2-2 遍历task list也没有task.isvalid=true的任务 --不展示广告，展示会员卡
* ~~ todo： btn还是复用失败toast文案？如果复用toast，可以减掉这个接口~~
* ~~todo：端看下刷新页面时机~~
* ！！！任务中台配置无限次数的话，返回的值是0，考虑此时给端-1表示无限
```
{
  "errno": "0",
  "timestamp": "1727163750",
  "logid": "3349410503",
  "data": {
    "isValid": true, // 命中sid(server开关)允许下发任务
    // videoType 控制激励广告和会员付费优先级(btn上下顺序) 成人色情资源优先采用会员付费 其他资源优先采用激励视频广告
    "videoType": 0, // 资源类型 0-普通 1-色情 1.9record: 本次不做，字段保留
    "task": [ // list形式为了后续扩展
        { // 不同任务id和type不同
          "actID": 362, // 活动方id
          "taskID": 123, // 任务id 同任务中台
          "type": "ads", // 广告
          "isValid": false, // 有无剩余次数
          "remainTimes": 1, // 剩余次数 为-1的时候表示无限
          "btnText": "看视频领免费次数" // btn文案
       }
    ]
  }
}
```
### 3.4 任务激活接口--对端
#### 3.4.1 流程图
[流程图]
#### 3.4.2 协议
req

|PATH|/baiduboxapp/basic/smoothplay/taskregister|
|-|-|
|METHOD|Post|
|Content-Type|application/x-www-form-urlencoded|
|Get参数|客户端公参|
|Post参数|{
"actID": 362, // 活动方id
"taskID": 123 // 任务id
}|
uid cuid appversion强校验

rsp

~~todo：任务scheme处理 参考游戏 贵龙~~

scheme处理(参考游戏)： 拼接

{

    "ext_policy": "{\"complete_info\":\"{\\\"callback_id\\\":\\\"f347749bf59209a05299111af6ed74f5\\\"}\"}"

}

```
{
  "errno": "0",
  "timestamp": "1727163750",
  "logid": "3349410503",
  "data": {
      "success": true, // 是否激活成功
      "scheme": "xxxx", // 任务激活scheme
      "callbackID": "xxxx" // uuid，和scheme拼接的进行校验
  }
}
```
### ~~3.5 【废弃】任务完成回调接口--任务中台callback配置~~
#### 3.5.1 流程图
[流程图]
### 3.6 数据存储
#### 3.6.1 gcp
|key|地址|描述|
|-|-|-|
|lite_smoothplay_task_conf|http://ccs-offline.bcc-bdbl.baidu.com:8080/gcp-platform/index#/app/10/config/8961|server针对流畅播任务功能的配置|
## 测试场景
### 4.0 环境说明
#### 4.0.1 sid
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d79dd3e34bfd45c08883e13b4c592e38&docGuid=BWEwmdF9ED3EQ6 "")
已icafe为准 [[ailite-27822] 【6.43】流畅播路径优化二期](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-27822/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk)

#### 4.0.2 server环境
|server环境|host|分支|备注|
|-|-|-|-|
|sbox-basic 本次两个新接口|liyunqing03.bcc-bddx.baidu.com:8009|ailite-27984|任务中台回调callbackaddr需要在gcp里改成qa的环境 所有都要改 http://ccs-offline.bcc-bdbl.baidu.com:8080/gcp-platform/index#/app/10/config/8961 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dcbdef3d88bc4a7491ea69f726469945&docGuid=BWEwmdF9ED3EQ6 "")|
|searchbox(bdapp_core集群) 原有vipsearch vipconsume接口|bjhw-ps-beehive-agent131534.bjhw.baidu.com:8041|master 代码无改动 只是联调/测试下游map到联调环境|ral conf的vip_service.conf改成如下配置，ral-worker.log能看到remoteip是10.9.228.180 [CamelConfig]
[.ServiceConfig]
[..Local]

[...@Service]
Name : vip_service
DefaultPort : 8982
DefaultRetry : 0
DefaultConnectType : SHORT
DefaultConnectTimeOut : 500
DefaultReadTimeOut : 1500
DefaultWriteTimeOut : 2000

[....@Server]
Hostname : lym07.bcc-gzhxy.baidu.com
[....SuperStrategy]
Balance : Random
CrossRoom : Off
[....Protocol]
Name : http
[....Converter]
Name : form|
#### 4.0.3 其他
* 任务中台配置为无次数上限，任务的remaintimes会按照约定下发-1；如果要测试达上限情况，需要改任务中台配置
* 原有的免费流畅播次数(searchbox的vipserarch和vipconsume接口)，如需给uid增加，联系[@刘一鸣](https://ku.baidu-int.com?t=mention&mt=contact&id=96effaf0-ce50-11ef-8d1a-29e1d626e07d)
### 4.1 任务查询tasklist接口


|场景|子场景|期待表现|server表现|端表现|
|-|-|-|-|-|
|任务开关关闭 对照组sid|--|server下发isvalid=false，空tasklist 端走展示会员弹窗逻辑|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b4dddedb16c44762bf0271b244808b8a&docGuid=BWEwmdF9ED3EQ6 "") done| ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f6ccf28ccb2740028142e22bfb5bbee8&docGuid=BWEwmdF9ED3EQ6 "") done|
|任务开关打开 实验1sid|任务完成未达上限(无限次)|server下发isvalid=true，tasklist不为空，广告task.isvalid=true，videotype=0，剩余次数-1，下发btn文案 端展示广告弹窗|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=539d733bad004489905e2f894e258e4d&docGuid=BWEwmdF9ED3EQ6 "") -1表示无限 done| ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e78e53bcf23840e1bd7996d3a1c2e21f&docGuid=BWEwmdF9ED3EQ6 "") done|
||任务完成未达上限(有限次)|server下发isvalid=true，tasklist不为空，广告task.isvalid=true，videotype=0，剩余次数>0，下发btn文案 端展示广告弹窗|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a20f42579f68435da72743afd2f920d1&docGuid=BWEwmdF9ED3EQ6 "") 配置上限4 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=529766f46abc4778aa05b16171d0ef09&docGuid=BWEwmdF9ED3EQ6 "") 返回上限4，已完成2 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=edeef58c89dc486880b0469ad3ef38f1&docGuid=BWEwmdF9ED3EQ6 "") 剩余2 done|--|
||任务完成达上限 (有限次)|server下发isvalid=true，tasklist不为空，广告task.isvalid=false，没有剩余次数，下发btn文案 端展示会员弹窗|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a20f42579f68435da72743afd2f920d1&docGuid=BWEwmdF9ED3EQ6 "") 配置上限4 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=57560ffca5e04621b7e37071fc71d133&docGuid=BWEwmdF9ED3EQ6 "") 任务已完成 status=2 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fd6fdeb749d9486da35463c19922e295&docGuid=BWEwmdF9ED3EQ6 "") 下发false和0 done|--|
||任务列表长度为0 (人工mock长度为0)|server下发isvalid=true，tasklist为空， 端展示会员弹窗|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b758688824a94c2b89c71a8cc6c812fb&docGuid=BWEwmdF9ED3EQ6 "") mock长度0 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a3880b38dd224a8c957f7b47eb4b34a3&docGuid=BWEwmdF9ED3EQ6 "") done|--|
### 4.2 任务激活taskregister接口
|场景|子场景|期待表现|server表现|端表现|
|-|-|-|-|-|
|激活|--|下发拼接好的scheme，带callbackid|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8221f5327f824f9a9ad4fb77e28efa4b&docGuid=BWEwmdF9ED3EQ6 "") 下发拼接scheme baiduboxapp://v7/vendor/ad/rewardVideo?params=%7B%22android_pid%22%3A%221631797735150%22%2C%22ios_pid%22%3A%221631797735191%22%2C%22task_id%22%3A%22602%22%2C%22task_type%22%3A%222%22%2C%22task_from%22%3A%22taskCenterWalk%22%2C%22token%22%3A%229c4d5b811073613afa5f3b91461156b2a8701e62ef0b5b8bf21008fc88bfda73%22%2C%22unique_id%22%3A%22taskCenterWalkLogId%22%2C%22ext_policy%22%3A%22%7B%5C%22complete_info%5C%22%3A%5C%22%7B%5C%5C%5C%22callback_id%5C%5C%5C%22%3A%5C%5C%5C%22642720315%5C%5C%5C%22%7D%5C%22%7D%22%7D urldecode baiduboxapp://v7/vendor/ad/rewardVideo?params={"android_pid":"1631797735150","ios_pid":"1631797735191","task_id":"602","task_type":"2","task_from":"taskCenterWalk","token":"9c4d5b811073613afa5f3b91461156b2a8701e62ef0b5b8bf21008fc88bfda73","unique_id":"taskCenterWalkLogId","ext_policy":"{\"complete_info\":\"{\\\"callback_id\\\":\\\"642720315\\\"}\"}"} callbackid一致 done| ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=75395f1c0c1c4ed7850bde779d0fb74e&docGuid=BWEwmdF9ED3EQ6 "") done|
|完成回调|--|正常收到中台的回调|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0ce30790692144999b260bf581ea41a4&docGuid=BWEwmdF9ED3EQ6 "") 回调正常收到  端上扫码做任务，完成一个只后点x不会继续做任务 done| done|


## 上线checklist
|事项|子事项|完成情况|备注|
|-|-|-|-|
|sboxlib|写changelog|done||
||打tag，合master|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f974f9c36df844a48e8c3774318c2c87&docGuid=BWEwmdF9ED3EQ6 "") done||
|sbox-basic|sboxlib用tag 合master|done||
|gcp|上线 lite_smoothplay_task_conf，根据sid配置|done|http://ccs.baidu-int.com/gcp-platform/index#/app/10/config/7864|
|任务中台|预览配回调|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8e08f4a6883b4fa49d863981b48f4a06&docGuid=BWEwmdF9ED3EQ6 "") done||
||推全配bns回调|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=217417700b154bc58d938ea492f5025f&docGuid=BWEwmdF9ED3EQ6 "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=01daef004a284766a3b786dc61639d4d&docGuid=BWEwmdF9ED3EQ6 "") done||
### 5.1 预览回归
sqa预览文档：[流畅播新增激励广告变现方式测试记录](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/nCQpnMXGR4/o94aKKKRJtkeVy?t=mention&mt=doc&dt=doc)

#### 5.1.1 tasklist
|场景|子场景|期待表现|server表现|端表现|
|-|-|-|-|-|
|任务开关关闭 对照组sid|--|server下发isvalid=false，空tasklist 端走展示会员弹窗逻辑|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f69b0ea338f548fb8098d9e8b9055be8&docGuid=BWEwmdF9ED3EQ6 "") done|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=562f4d93786946a99cae96dbe8d1ec28&docGuid=BWEwmdF9ED3EQ6 "")  done|
|任务开关打开 实验1sid|任务完成未达上限(无限次)|server下发isvalid=true，tasklist不为空，广告task.isvalid=true，videotype=0，剩余次数-1，下发btn文案 端展示广告弹窗|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1a06489ad3b54ee7a8fdbe6e0c41abd7&docGuid=BWEwmdF9ED3EQ6 "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1f6bb943cf254aedbde92cfd536d1854&docGuid=BWEwmdF9ED3EQ6 "") done|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=acbec471fc9545cf89cc071d78f021bb&docGuid=BWEwmdF9ED3EQ6 "")  done|
||任务完成未达上限(有限次)|server下发isvalid=true，tasklist不为空，广告task.isvalid=true，videotype=0，剩余次数>0，下发btn文案 端展示广告弹窗|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7ee2a357eef24e25b4a63ff8d8f5f3b1&docGuid=BWEwmdF9ED3EQ6 "") done|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=60fb598aac5b4c5ca77ab88fc15ff393&docGuid=BWEwmdF9ED3EQ6 "")  done|
||任务完成达上限 (有限次)|server下发isvalid=true，tasklist不为空，广告task.isvalid=false，没有剩余次数，下发btn文案 端展示会员弹窗|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e4aba9ecfc0946239e6ce729724aba08&docGuid=BWEwmdF9ED3EQ6 "") done|  done|
#### 5.1.2 taskregister
|场景|子场景|期待表现|server表现|端表现|
|-|-|-|-|-|
|激活|--|下发拼接好的scheme，带callbackid|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b206d3abf4374e888a620cc193968731&docGuid=BWEwmdF9ED3EQ6 "") baiduboxapp://v7/vendor/ad/rewardVideo?params=%7B%22android_pid%22%3A%221631797735150%22%2C%22ios_pid%22%3A%221631797735191%22%2C%22task_id%22%3A%22602%22%2C%22task_type%22%3A%222%22%2C%22task_from%22%3A%22taskCenterWalk%22%2C%22token%22%3A%229c4d5b811073613afa5f3b91461156b2a8701e62ef0b5b8bf21008f888bfda73%22%2C%22unique_id%22%3A%22taskCenterWalkLogId%22%2C%22ext_policy%22%3A%22%7B%5C%22complete_info%5C%22%3A%5C%22%7B%5C%5C%5C%22callback_id%5C%5C%5C%22%3A%5C%5C%5C%224135593730%5C%5C%5C%22%7D%5C%22%7D%22%7D baiduboxapp://v7/vendor/ad/rewardVideo?params={"android_pid":"1631797735150","ios_pid":"1631797735191","task_id":"602","task_type":"2","task_from":"taskCenterWalk","token":"9c4d5b811073613afa5f3b91461156b2a8701e62ef0b5b8bf21008f888bfda73","unique_id":"taskCenterWalkLogId","ext_policy":"{\"complete_info\":\"{\\\"callback_id\\\":\\\"4135593730\\\"}\"}"} done|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3a095d04e4284af7844486eb1bd13535&docGuid=BWEwmdF9ED3EQ6 "")  done|
|完成回调|--|正常收到中台的回调|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=549f6c0fad3b46448ad24d1cfd5b72ff&docGuid=BWEwmdF9ED3EQ6 "") done|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fee7246a1393436493aa0b6127a9be51&docGuid=BWEwmdF9ED3EQ6 "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=df963c632d394c179fb76ccd7ee67e9d&docGuid=BWEwmdF9ED3EQ6 "") done|


## 排期
1.6-1.10开发联调

1.13测试

1.14上线

|server|@李云清|
|-|-|
|端rd|@龚丹@袁祎凯|
|sqa|@邹立凯@v_郭浩|
|端qa|@宁彦林|
|pm|@刘朋硕@李麓含之|