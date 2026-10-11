---
title: "HFW9oCPh-ipJu5"
description: "\"actTaskType\": 0,// 活动任务类型，0： 普通，1：搜索 \"wordList\": { \"word\":\"xxxx\", \"wordType\":0 // 0 普通，1热词，2商业词 } ,"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\lib\\req_agent\\ku\\HFW9oCPh-ipJu5.md"
---
获取任务列表

### 1.1请求方式
GET

### 2.1 PATH
/api/task/:actId/tasks

##### 2.2 路径参数
actID:活动方id



### 3.1 请求参数
|字段|是否必须|类型|备注|
|-|-|-|-|
|token|Y|string|任务平台分配的活动方token|
|uid|N|uint64|用户id|
|cuid|N|string|用户设备id|
|source|Y|string|区分来源分端标签，具体详见附录|
|platform|Y|int|区分来源的平台，Android-2，IOS-1，3-Harmony 默认0（按照Android处理）|
|version|Y|string|app版本|
|sid|N|string|用户命中的所有实验号|
|utsParams|N|string|活动需要接入策略时需要传入的参数，uts额外需要透传的参数(参数类型JSON字符串)，会跟默认参数进行merge|
|utsConfig|N|string|自定义请求策略地址， (类型：json字符串,包含三个参数appid,strategy,token,三个字段全是string类型)|
|incentiveParams|N|string|需要请求奖励策略时有额外的参数需要透传放在该字段下，常用场景：激励视频|
##### 3.2 调试参数
注意以下参数不要带到线上

|字段|是否必须|类型|备注|
|-|-|-|-|
|uts_test||int|获取任务需要请求策略&需要使用线下的策略环境，1:开启,0:不开启，默认0（不开启）|
|nouts||int|请求任务列表开启了策略，需要临时跳过调试使用，1:跳过，0:不跳过，0或者不传此参数会过uts策略（前提必须开启精细化策略过滤）|
|debug||int|调试模式任务列表会同时返回未展示的任务的被过滤情况，以及未展示原因，1:开启，0:不开启|
##### 3.3 utsParams参数
默认会透传：uid、cuid、sid

###### 3.3.1 常用字段
|字段|是否必须|类型|备注|
|-|-|-|-|
|pv|Y|string|系统版本|
|brand|Y|string|机型|
|ip|Y|string|用户ip|
|al|N|string|用户应用安装列表|
|version|Y|string|app版本|
|os|Y|string|操作系统1ios 2android 3harmony|
|is_widget|N|string|用户是否安装了某个widget，需要任务列表中有widget任务0未安装，1安装|
|is_push|N|string |用户是否打开了push, 如果任务列表中有push相关的任务需要下发|
|incentiveUserType|N|string|是否任务系统目标用户，1目标用户，0 | 2非目标用户|
|itemIncentiveUserType|N|string|是否实物目标用户，1目标用户，0 | 2 非目标用户|
还可以和策略约定透传其他额外参数。任务平台会做merge

### 4.1 返回数据
```
{
    "errno": 0,
    "errmsg": "",
    "data": {
        "act": {
            "actId": 158,
            "actName": "任务系统V1.3",
            "startTime": "2021-06-20 23:00:00",
            "endTime": "2024-07-03 00:00:00"
        },
        "expInfo": null,
        "list": [
            {
                "id": 3011, // 任务ID
                "taskId": 3011, // 任务ID
                "taskName": "Lite端时长任务", // 任务名称
                "actId": 158, // 活动ID
                "typeId": 596, //  任务方ID
                "tags": [ // 下发端
                    2 
                ],
                "type": 1,// 任务类型，0：默认，1：外部
                
                "actTaskType": 0,// 活动任务类型，0： 普通，1：搜索
                "wordList":[
                    {
                        "word":"xxxx",
                        "wordType":0 // 0 普通，1热词，2商业词
                    }
                ],
                
                "appId": 2, // 该任务导流的目标端，即任务方所在端
                "token": "8963eda54bc7b973be59bee08148e727edb2d55171c279b193f83e24e23f63c6", // 任务完成所需要的token
                "taskTimes": 0, // 任务总次数，0在任务平台标识无限次完成
                "utsScore": "", // 策略返回改任务的价值，可以根据该价值发放奖励
                "utsExt": null,
                "actionType": 7, // 任务方类型 动作计时，动作计次，普通任务等
                "extData": "",
                "taskNo": "202305310000", // 任务期号
                "taskStatus": 1, // 任务状态 0：未完成，1：已激活，2：已完成
                "source": 2, // 所在端
                "activeTime": "2023-05-29 16:49:25", // 激活时间
                "taskDoneTimes": 0, // 完成的次数
                "doneTime": "1970-01-01 08:00:00", // 首次完成时间
                "actionConf": { // 任务方配置
                    "apk": "",
                    "appId": 2,
                    "cbToken": "",
                    "custom_times": 0,
                    "inside": true,
                    "jumpType": 1, // 跳转类型
                    "options": "{\n    \"authority\": \"eopatask\",\n    \"path\": \"/registerTask\",\n    \"parameters\": {\n        \"taskInfo\": \"92999f8160285ac3c077c48e103c946ce31a824dcc6787a166b19f3f5e8fad473873f009b5b0a718b86222a425fa6439fe8e3ca88aa2ce1d3f017056478faff281d195a3c7141547e5e945285a5ffcfbdb7ea80a88f5004f96dfe4dd0b03d72377ce393f310bcd153ffb688ca3b5d04dffa94678d39ffa0e41b7915091fb2d7ca92f011e9f1b58a50b41babfa28f2f01749aebc838651778702f8c2b06f07b06703a3b935618dba5ce8ef250f09c30a5c44b2592ec39da2281e14dabbda3e5e347df8c4824a9a6c3ed522bd609b02951fada3105a450033cc72bf27af65716940924f5c791308b8e1f66b26d064ae428c0613d8d8c97083fab43fd686432cad26327ad343538e53612c2b52c45f4bc51c6889e977285c24955fb56e5e23b5becfcd145b799f95b17ba12bfe295ad1c2e97d670038cfe003639ad3d82a14d6b2c5e47e9637b06732e88b1a133a2f5665f67da5219e8be34215db32dc904c27f8df90d2860930709a5a868f3b35034417421444b25a2c182a934efffe04f3ad0aaf1095719507330ffcdede74fe55d61d883cf6aec53e10b500686cf9d690f2721a0fe038af5dae271426fde4524f14e547be77103a1b39dfd61108fd8734b7606a86344dc879f6199ede6a8a92d44539c60c1ef68bd896b6aa1d120cb3bb43b7ebe790aa36557a088429657a430a8769270fd5ec535207a5f3fe60d269fb93322f5eb5c8bf404f0931015caee807ec2bb4c627c221ed2914649e83ba5d836cd36ee8a653da94fc37820d72e5babbc39b59cc20e745941b6b1b3471d012751fb1049c1e7b7a643ccda91d8d42fe26663a5\"\n    }\n}",
                    "pkgName": "com.baidu.searchbox.lite",
                    "scheme": "baiduboxlite://eopatask/registerTask?taskInfo=92999f8160285ac3c077c48e103c946ce31a824dcc6787a166b19f3f5e8fad473873f009b5b0a718b86222a425fa6439fe8e3ca88aa2ce1d3f017056478faff281d195a3c7141547e5e945285a5ffcfbdb7ea80a88f5004f96dfe4dd0b03d72377ce393f310bcd153ffb688ca3b5d04dffa94678d39ffa0e41b7915091fb2d7ca92f011e9f1b58a50b41babfa28f2f01749aebc838651778702f8c2b06f07b06703a3b935618dba5ce8ef250f09c30a5c44b2592ec39da2281e14dabbda3e5e347df8c4824a9a6c3ed522bd609b02951fada3105a450033cc72bf27af65716940924f5c791308b8e1f66b26d064ae428c0613d8d8c97083fab43fd686432cad26327ad343538e53612c2b52c45f4bc51c6889e977285c24955fb56e5e23b5becfcd145b799f95b17ba12bfe295ad1c2e97d670038cfe003639ad3d82a14d6b2c5e47e9637b06732e88b1a133a2f5665f67da5219e8be34215db32dc904c27f8df90d2860930709a5a868f3b35034417421444b25a2c182a934efffe04f3ad0aaf1095719507330ffcdede74fe55d61d883cf6aec53e10b500686cf9d690f2721a0fe038af5dae271426fde4524f14e547be77103a1b39dfd61108fd8734b7606a86344dc879f6199ede6a8a92d44539c60c1ef68bd896b6aa1d120cb3bb43b7ebe790aa36557a088429657a430a8769270fd5ec535207a5f3fe60d269fb93322f5eb5c8bf404f0931015caee807ec2bb4c627c221ed2914649e83ba5d836cd36ee8a653da94fc37820d72e5babbc39b59cc20e745941b6b1b3471d012751fb1049c1e7b7a643ccda91d8d42fe26663a5",  // 跳转地址，激活完成后也会返回该字段，任务跳转用激活返回的任务
                    "tkey": "",
                    "url": "", // 下载页地址
                    "version": "5.9.0"
                }
            },
            {
                "id": 3149,
                "taskId": 3149,
                "taskName": "任务系统V1.4-30天签到弹窗",
                "actId": 158,
                "typeId": 6,
                "tags": [
                    27,
                    2,
                    10,
                    1,
                    46
                ],
                "type": 0,
                "appId": 0,
                "taskTimes": 1,
                "utsScore": "",
                "utsExt": null,
                "actionType": 3,
                "extData": "",
                "taskNo": "202305310000",
                "taskStatus": 0,
                "source": 0,
                "taskDoneTimes": 0,
                "actionConf": {
                    "appId": 0,
                    "inside": false,
                    "options": "none",
                    "pkgName": "com.baidu.searchbox.lite",
                    "scheme": "baiduboxlite://v11/appTab/select?item=home&upgrade=1",
                    "tkey": "",
                    "url": "https://downpack.baidu.com/litebaiduboxapp_AndroidPhone_1022608r.apk"
                }
            },
            {
                "id": 3125,
                "taskId": 3125,
                "taskName": "邀好友测试任务",
                "actId": 158,
                "typeId": 6,
                "tags": [
                    2,
                    27,
                    10,
                    46
                ],
                "type": 0,
                "appId": 0,
                "taskTimes": 1,
                "utsScore": "",
                "utsExt": null,
                "actionType": 3,
                "extData": "",
                "taskNo": "202305310000",
                "taskStatus": 0,
                "source": 0,
                "taskDoneTimes": 0,
                "actionConf": {
                    "appId": 0,
                    "custom_times": 0,
                    "inside": false,
                    "options": "{\n    \"authority\": \"v1\",\n    \"path\": \"/easybrowse/open\",\n    \"parameters\": {\n        \"url\": \"https://activity.baidu.com/invite/inviteHome?productid=2&productid=2&position=inv_task&idfrom=rwlb&append_di=1\",\n        \"newbrowser\": 1,\n        \"forbidautorotate\": 1,\n        \"type\": \"immerse\",\n        \"backlocation\": 1,\n        \"bannerswitch\": 1,\n        \"append\": 1,\n        \"zoomswitch\": 0,\n        \"append_di\": 1\n    }\n}",
                    "pkgName": "com.baidu.searchbox.lite",
                    "scheme": "baiduboxlite://v1/easybrowse/open?url=https%3A%2F%2Factivity.baidu.com%2Finvite%2FinviteHome%3Fproductid%3D2%26productid%3D2%26position%3Dinv_task%26idfrom%3Drwlb%26append_di%3D1&newbrowser=1&forbidautorotate=1&type=immerse&backlocation=1&bannerswitch=1&append=1&zoomswitch=0&append_di=1",
                    "tkey": "",
                    "url": "https://downpack.baidu.com/litebaiduboxapp_AndroidPhone_1022608r.apk"
                },
                "uiConf": {
                    "iconUrl": "这是iconUrl",
                    "lowestAppVersion": "",
                    "os": "all",
                    "subTitle": "邀好友副标题--",
                    "title": "邀好友"
                }
            }
            
        ]
    }
}
```