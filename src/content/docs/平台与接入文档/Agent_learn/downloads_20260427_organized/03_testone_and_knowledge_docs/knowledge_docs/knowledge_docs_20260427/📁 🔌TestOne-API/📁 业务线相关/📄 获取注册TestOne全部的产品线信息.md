---
title: "📄 获取注册TestOne全部的产品线信息"
description: "获取注册TestOne全部的产品线信息"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 业务线相关\\📄 获取注册TestOne全部的产品线信息.md"
---
获取注册TestOne全部的产品线信息

**功能**

> 获取注册TestOne全部的产品线信息


**接口信息**

> 地址：https://testone.baidu-int.com/api/department/getAllDept
> 方法：GET


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|Content-Type|string||application/json|
|username|string|用户名|xxxxxx|
|token|string|Token |xxxxxx|



**参数**

无



**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20250829-server-01-a6f4-95989afeb81e",
    "owner": "wushaoshan",
    "data": [
        {
            "id": 222,
            "name": "百度APP",
            "subDirections": [
                "基础",
                "搜索",
                "内核",
                "基础技术&性能",
                "服务端",
                "发版团队"
            ],
            "owner": "wangzhongyang,huoxinyue,zhangkaili05,zhaokairui",
            "creator": "gaolizhe",
            "operator": "gaolizhe",
            "createdTime": "2023-08-31 11:17:43",
            "updateTime": "2023-08-31 11:17:59",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 232,
            "name": "小程序",
            "subDirections": [
                "客户端",
                "服务端",
                "前端Web",
                "前端Swan",
                "开发者工具"
            ],
            "owner": "lihao61",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-01-11 12:31:45",
            "updateTime": "2024-01-11 12:31:45",
            "manager": "zhaohuijie",
            "isDeleted": 0
        },
        {
            "id": 239,
            "name": "贴吧",
            "subDirections": [
                "客户端",
                "服务端"
            ],
            "owner": "zengqiong,yuanshuang01",
            "creator": "wangshitao",
            "operator": "wangshitao",
            "createdTime": "2023-11-24 15:29:10",
            "updateTime": "2023-11-24 15:29:10",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 271,
            "name": "直播",
            "subDirections": [
                "直播",
                "直播架构"
            ],
            "owner": "weijingjing01",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2023-11-23 20:42:48",
            "updateTime": "2023-11-23 20:42:48",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 272,
            "name": "直播推荐",
            "subDirections": [
                "电商推荐"
            ],
            "owner": "binxuemei",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-10-25 14:47:19",
            "updateTime": "2024-10-25 14:47:19",
            "manager": "liulanying01",
            "isDeleted": 0
        },
        {
            "id": 310,
            "name": "小说",
            "subDirections": [
                "客户端",
                "服务端"
            ],
            "owner": "liurui14",
            "creator": "gaolizhe",
            "operator": "gaolizhe",
            "createdTime": "2023-11-20 15:32:14",
            "updateTime": "2023-11-20 15:32:14",
            "manager": "dingyalin01",
            "isDeleted": 0
        },
        {
            "id": 395,
            "name": "知识创新",
            "subDirections": [
                "客户端",
                "服务端"
            ],
            "owner": "fengxiaomiao",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-05-14 20:44:10",
            "updateTime": "2024-05-14 20:44:10",
            "manager": "zhaohuijie",
            "isDeleted": 0
        },
        {
            "id": 410,
            "name": "好看视频",
            "subDirections": [
                "好看视频",
                "服务端",
                "短剧版APP"
            ],
            "owner": "wangjing87",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2023-11-27 15:33:17",
            "updateTime": "2023-11-27 15:33:17",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 550,
            "name": "大FEED",
            "subDirections": [
                "Feed",
                "视频",
                "Talos",
                "Feed前端",
                "服务端",
                "荣耀白牌",
                "鸿蒙适配",
                "视频-xapp",
                "feed-xapp"
            ],
            "owner": "lixue24",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2023-11-23 16:35:38",
            "updateTime": "2023-11-23 16:35:38",
            "manager": "lisi02",
            "isDeleted": 0
        },
        {
            "id": 551,
            "name": "搜索产研",
            "subDirections": [
                "搜索前端",
                "产研服务端",
                "阿拉丁",
                "阿拉丁架构&策略",
                "知识创新客户端",
                "知识创新服务端",
                "百科",
                "Feature一体化"
            ],
            "owner": "wangchenxue,liaoxin02,zhangjin02,zhangsi01,fengxia",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-03-20 16:46:14",
            "updateTime": "2024-03-20 16:46:14",
            "manager": "zhaohuijie",
            "isDeleted": 0
        },
        {
            "id": 567,
            "name": "百度百科",
            "subDirections": [
                "百科"
            ],
            "owner": "zhangmengmeng04",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-05-08 16:00:55",
            "updateTime": "2024-05-08 16:00:55",
            "manager": "zhaohuijie",
            "isDeleted": 0
        },
        {
            "id": 773,
            "name": "百度教育",
            "subDirections": [
                "百度教育"
            ],
            "owner": "chenqiehao",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-03-19 14:12:09",
            "updateTime": "2024-03-19 14:12:09",
            "manager": "zhaohuijie",
            "isDeleted": 0
        },
        {
            "id": 1469,
            "name": "商业原生广告",
            "subDirections": [
                "商业原生广告",
                "原生广告检索端",
                "原生广告流量中台"
            ],
            "owner": "tifeifei",
            "creator": "guyouda",
            "operator": "guyouda",
            "createdTime": "2023-09-19 14:28:07",
            "updateTime": "2023-09-19 14:28:07",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 1583,
            "name": "商业ToB垂类",
            "subDirections": [
                "爱采购",
                "爱番番",
                "企信",
                "行业创新",
                "汽车",
                "泛娱乐",
                "月匣",
                "问一问"
            ],
            "owner": "lizhixuan03",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-03-13 09:37:41",
            "updateTime": "2024-03-13 09:37:41",
            "manager": "dingyalin01",
            "isDeleted": 0
        },
        {
            "id": 1584,
            "name": "商业智能交付测试",
            "subDirections": [
                "测试产品线A"
            ],
            "owner": "renxuejian",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-08-19 17:19:07",
            "updateTime": "2024-08-19 17:19:07",
            "manager": "dingyalin01",
            "isDeleted": 0
        },
        {
            "id": 1996,
            "name": "电商直播",
            "subDirections": [
                "电商sdk",
                "直播sdk",
                "鸿蒙sdk",
                "服务端",
                "前端",
                "大事件"
            ],
            "owner": "caoxue01,yeyuqi",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2023-10-24 19:09:46",
            "updateTime": "2023-10-24 19:09:46",
            "manager": "liulanying01",
            "isDeleted": 0
        },
        {
            "id": 1997,
            "name": "电商数字人",
            "subDirections": [
                "服务端",
                "前端"
            ],
            "owner": "caoxue01",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-04-07 17:14:39",
            "updateTime": "2024-04-07 17:14:39",
            "manager": "liulanying01",
            "isDeleted": 0
        },
        {
            "id": 1998,
            "name": "搜索电商",
            "subDirections": [
                "电商产研",
                "电商前端",
                "baise策略",
                "搜索策略"
            ],
            "owner": "dairongrong",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-06-21 18:53:32",
            "updateTime": "2024-06-21 18:53:32",
            "manager": "liulanying01",
            "isDeleted": 0
        },
        {
            "id": 1999,
            "name": "电商商家B端",
            "subDirections": [
                "电商投放",
                "小店B端",
                "商家治理"
            ],
            "owner": "dujiayu02,wangshuang03",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-07-18 15:19:50",
            "updateTime": "2024-07-18 15:19:50",
            "manager": "liulanying01",
            "isDeleted": 0
        },
        {
            "id": 2000,
            "name": "电商小店C端",
            "subDirections": [
                "随版-服务端",
                "非随"
            ],
            "owner": "wangshuang03",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-08-29 18:36:03",
            "updateTime": "2024-08-29 18:36:03",
            "manager": "liulanying01",
            "isDeleted": 0
        },
        {
            "id": 2001,
            "name": "电商",
            "subDirections": [
                "营销"
            ],
            "owner": "sangzhan",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2025-05-14 10:29:19",
            "updateTime": "2025-05-14 10:29:19",
            "manager": "liulanying01",
            "isDeleted": 0
        },
        {
            "id": 2086,
            "name": "政务",
            "subDirections": [
                "政务"
            ],
            "owner": "yulei15",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-01-17 10:37:34",
            "updateTime": "2024-01-17 10:37:34",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 4041,
            "name": "百度文库",
            "subDirections": [
                "客户端",
                "服务端",
                "橙篇APP",
                "文库策略",
                "创新增长"
            ],
            "owner": "jiangchan",
            "creator": "gaolizhe",
            "operator": "gaolizhe",
            "createdTime": "2023-11-21 15:39:33",
            "updateTime": "2023-11-21 15:39:33",
            "manager": "chenmeina01",
            "isDeleted": 0
        },
        {
            "id": 4385,
            "name": "PUSH中台",
            "subDirections": [
                "客户端",
                "服务端",
                "配置类需求"
            ],
            "owner": "wunan10",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-04-19 14:06:11",
            "updateTime": "2024-04-19 14:06:11",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 4386,
            "name": "用户增长",
            "subDirections": [
                "策略&投放增长",
                "长线活动",
                "运营中台",
                "大事件",
                "技术类需求",
                "配置类需求"
            ],
            "owner": "guoningning",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-04-19 14:06:54",
            "updateTime": "2024-04-19 14:06:54",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 11457,
            "name": "问一问",
            "subDirections": [
                "问一问"
            ],
            "owner": "shangyanan",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-04-26 17:31:17",
            "updateTime": "2024-04-26 17:31:17",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 25219,
            "name": "中台服务",
            "subDirections": [
                "IM-SDK",
                "交易",
                "Pass-SDK",
                "IM服务端",
                "Pass服务端&前端",
                "大用户",
                "收藏SDK"
            ],
            "owner": "yueyuanbo",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2023-11-22 16:31:41",
            "updateTime": "2023-11-22 16:31:41",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 25274,
            "name": "简搜APP",
            "subDirections": [
                "简搜APP"
            ],
            "owner": "zhaokairui",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2023-11-23 15:36:45",
            "updateTime": "2023-11-23 15:36:45",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 26127,
            "name": "百度APP矩阵",
            "subDirections": [
                "极速版",
                "大字版"
            ],
            "owner": "maojinyu",
            "creator": "gaolizhe",
            "operator": "gaolizhe",
            "createdTime": "2023-11-20 10:41:29",
            "updateTime": "2023-11-20 10:41:29",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 26674,
            "name": "TestOne",
            "subDirections": [
                "智能交付",
                "工作台",
                "精准推荐",
                "众测"
            ],
            "owner": "guyouda",
            "creator": "guyouda",
            "operator": "guyouda",
            "createdTime": "2023-08-31 11:17:43",
            "updateTime": "2023-08-31 11:17:59",
            "manager": "weichenhui",
            "isDeleted": 0
        },
        {
            "id": 26675,
            "name": "品牌",
            "subDirections": [
                "品专前端",
                "GD前端",
                "开屏前端",
                "品专-检索",
                "GD-检索端",
                "开屏-检索端",
                "知识营销-检索",
                "品牌智能体-检索"
            ],
            "owner": "lichengcheng04",
            "creator": "gaolizhe",
            "operator": "gaolizhe",
            "createdTime": "2023-11-22 14:26:56",
            "updateTime": "2023-11-22 14:26:56",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 26676,
            "name": "网盟",
            "subDirections": [
                "网盟-SDK",
                "网盟-FE",
                "网盟-AIGC",
                "LU前端",
                "LU检索",
                "AFD检索",
                "BES检索",
                "内容联盟",
                "聚屏",
                "业务端",
                "联盟-Union",
                "AIGC-服务端",
                "联盟-UCRM",
                "联盟聚屏业务端",
                "分润",
                "广告联盟-BES业务端",
                "商机联盟",
                "百青藤-流量中台"
            ],
            "owner": "lijianxin02",
            "creator": "gaolizhe",
            "operator": "gaolizhe",
            "createdTime": "2023-11-22 14:27:48",
            "updateTime": "2024-09-23 14:27:48",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 26677,
            "name": "NewAPP",
            "subDirections": [
                "newapp",
                "newapp服务端",
                "万话",
                "万话服务端"
            ],
            "owner": "mahailiang01",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2023-11-29 17:24:31",
            "updateTime": "2023-11-29 17:24:31",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 26678,
            "name": "度豆",
            "subDirections": [
                "客户端",
                "服务端"
            ],
            "owner": "weijingjing01",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-06-19 13:02:30",
            "updateTime": "2024-06-19 13:02:30",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 26679,
            "name": "文心智能体",
            "subDirections": [
                "文心智能体平台",
                "文心智能体-分发",
                "文心智能体-策略",
                "行业-情感"
            ],
            "owner": "yulei15,lihao61",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-07-26 11:00:15",
            "updateTime": "2024-07-26 11:00:15",
            "manager": "zhaohuijie",
            "isDeleted": 0
        },
        {
            "id": 27084,
            "name": "内容生态中心",
            "subDirections": [
                "百家号",
                "黄油相机",
                "度咔",
                "手百发布器",
                "AIGC服务端",
                "内容风控",
                "日志中台&OPS"
            ],
            "owner": "liuyanting01",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2023-12-21 15:05:27",
            "updateTime": "2023-12-21 15:05:27",
            "manager": "lisi02",
            "isDeleted": 0
        },
        {
            "id": 27090,
            "name": "商业凤巢",
            "subDirections": [
                "前端",
                "流量中台",
                "主搜检索",
                "健康垂类",
                "知识垂类",
                "RFQ检索",
                "点击转化模型",
                "相关性模型",
                "内容模型",
                "流量模型",
                "行业模型",
                "扬辑"
            ],
            "owner": "zhenyunao,chenhao46,wangchenhui01",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-04-23 15:50:44",
            "updateTime": "2024-04-23 15:50:44",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27091,
            "name": "商业风控",
            "subDirections": [
                "物料风控",
                "客户风控",
                "AIGC风控",
                "其他风控"
            ],
            "owner": "fengmeixue",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-06-17 11:25:45",
            "updateTime": "2024-06-17 11:25:45",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27092,
            "name": "搜索内容技术",
            "subDirections": [
                "搜索内容技术-视频环",
                "搜索内容技术-解析",
                "搜索内容技术-内容关系",
                "搜索内容技术-调度",
                "搜索内容技术-渲染",
                "搜索内容技术-搜索平台",
                "搜索内容技术-抓取",
                "搜索内容技术-小环",
                "搜索内容技术-千仞",
                "搜索内容技术-分发",
                "搜索内容技术-接入",
                "搜索内容技术-图片创作",
                "搜索内容技术-搜索出图",
                "搜索内容技术-搜索指纹",
                "搜索内容技术-AI妙笔",
                "搜索内容技术-知识库"
            ],
            "owner": "dingyalin01",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-06-20 14:40:05",
            "updateTime": "2024-06-20 14:40:05",
            "manager": "zhaohuijie",
            "isDeleted": 0
        },
        {
            "id": 27093,
            "name": "搜索架构&策略",
            "subDirections": [
                "搜索消费",
                "搜索整页",
                "搜索召回",
                "搜索离线",
                "搜索展现",
                "搜索排序",
                "搜索笔记",
                "搜索时效性",
                "生态安全",
                "搜索基础技术",
                "搜索推荐",
                "搜索数据流",
                "搜索多模"
            ],
            "owner": "liqianqian08,huangziyue",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-06-27 10:38:55",
            "updateTime": "2024-06-27 10:38:55",
            "manager": "zhaohuijie",
            "isDeleted": 0
        },
        {
            "id": 27094,
            "name": "CRM",
            "subDirections": [
                "自用CRM"
            ],
            "owner": "zhangqian49,chenhua09",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-07-18 13:24:46",
            "updateTime": "2024-07-18 13:24:46",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27095,
            "name": "百度地图",
            "subDirections": [
                "产品运营"
            ],
            "owner": "huangyan09",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-09-19 18:25:18",
            "updateTime": "2024-09-19 18:25:18",
            "manager": "luoqin03",
            "isDeleted": 0
        },
        {
            "id": 27096,
            "name": "广告投放",
            "subDirections": [
                "凤巢投放",
                "信息流投放",
                "Editor",
                "报表中心",
                "营销解决方案",
                "客户服务",
                "一站式平台",
                "O端",
                "商业开发者中心",
                "百度营销手机版",
                "优化中心",
                "客户中心",
                "排查兔",
                "线索直播",
                "智能工具"
            ],
            "owner": "zhengyunao",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-10-23 17:23:18",
            "updateTime": "2024-10-23 17:23:18",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27097,
            "name": "轻舸",
            "subDirections": [
                "轻舸",
                "B端智能体"
            ],
            "owner": "lijiacheng07",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-10-25 16:42:53",
            "updateTime": "2024-10-25 16:42:53",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27098,
            "name": "托管",
            "subDirections": [
                "梧桐建站",
                "建站中台",
                "行业托管",
                "营销通",
                "转化中心",
                "商家智能体",
                "本地生活",
                "爱番番",
                "教育垂类",
                "旅游垂类"
            ],
            "owner": "lijiacheng07",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-10-25 16:45:04",
            "updateTime": "2024-10-25 16:45:04",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27099,
            "name": "品牌投放端",
            "subDirections": [
                "品专-投放端",
                "开屏-投放端",
                "GD-投放端",
                "聚屏-投放端",
                "展示广告业务中台",
                "知识营销"
            ],
            "owner": "lipingping04",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-11-06 19:53:17",
            "updateTime": "2024-11-06 19:53:17",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27100,
            "name": "商业阿拉丁",
            "subDirections": [
                "星河数据产品",
                "IDMP",
                "百度指数",
                "百度统计"
            ],
            "owner": "lipingping04",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-11-06 19:53:17",
            "updateTime": "2024-11-06 19:53:17",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27101,
            "name": "内容营销",
            "subDirections": [
                "内容营销"
            ],
            "owner": "lipingping04",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-11-06 19:53:17",
            "updateTime": "2024-11-06 19:53:17",
            "manager": "mazhe",
            "isDeleted": 0
        },
        {
            "id": 27102,
            "name": "小度云平台",
            "subDirections": [
                "垂类",
                "教育"
            ],
            "owner": "yangrui23",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-12-17 16:45:45",
            "updateTime": "2024-12-17 16:45:45",
            "manager": "linxiaolan",
            "isDeleted": 0
        },
        {
            "id": 27103,
            "name": "百度健康",
            "subDirections": [
                "健康商城",
                "在线医疗",
                "医生医院智能体",
                "健康中台",
                "健康内容",
                "基础库",
                "度小医"
            ],
            "owner": "yangmin01",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2025-01-07 14:01:32",
            "updateTime": "2025-01-07 14:01:32",
            "manager": "sunxiaojie",
            "isDeleted": 0
        },
        {
            "id": 27104,
            "name": "商业AIGC",
            "subDirections": [
                "AIGC产品化"
            ],
            "owner": "zhengyunao",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2025-02-20 10:38:30",
            "updateTime": "2025-02-20 10:38:30",
            "manager": "wangchenhui01",
            "isDeleted": 0
        },
        {
            "id": 27105,
            "name": "心响",
            "subDirections": [
                "客户端",
                "服务端"
            ],
            "owner": "shangyanan",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2025-03-21 16:37:22",
            "updateTime": "2025-03-21 16:37:22",
            "manager": "dingyalin01",
            "isDeleted": 0
        },
        {
            "id": 27106,
            "name": "XAPP",
            "subDirections": [
                "基础功能"
            ],
            "owner": "zhangkaili05",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2025-03-27 19:40:35",
            "updateTime": "2025-03-27 19:40:35",
            "manager": "hongyuyang",
            "isDeleted": 0
        },
        {
            "id": 27107,
            "name": "百度网盘",
            "subDirections": [
                "一刻相册"
            ],
            "owner": "dengxurui",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2025-04-21 20:30:56",
            "updateTime": "2025-04-21 20:30:56",
            "manager": "gongweiwei",
            "isDeleted": 0
        },
        {
            "id": 27108,
            "name": "生花",
            "subDirections": [
                "生花平台"
            ],
            "owner": "yulei15",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2025-06-12 14:27:10",
            "updateTime": "2025-06-12 14:27:10",
            "manager": "dingyalin01",
            "isDeleted": 0
        },
        {
            "id": 27109,
            "name": "Feed内容技术",
            "subDirections": [
                "Feed内容技术-terrace",
                "Feed内容技术-指纹系统（B端）",
                "Feed内容技术-指纹系统（C端）",
                "Feed内容技术-内容库（B端）",
                "Feed内容技术-内容库（C端）",
                "Feed内容技术-后验"
            ],
            "owner": "zhuxinbo",
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2025-08-12 14:35:01",
            "updateTime": "2025-08-12 14:35:01",
            "manager": "dingyalin01",
            "isDeleted": 0
        },
        {
            "id": 27110,
            "name": "商业AIGC",
            "subDirections": [
                "AIGC模型"
            ],
            "owner": "",
            "creator": "",
            "operator": "",
            "createdTime": "2025-08-15 18:25:08",
            "updateTime": "2025-08-15 18:25:08",
            "manager": "",
            "isDeleted": 0
        }
    ]
}
```







