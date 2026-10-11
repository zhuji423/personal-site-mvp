---
title: "plus会员+pro会员店铺"
description: "CPD-278079 plus会员+pro会员店铺页mrdhttps://console.cloud.baidu-int.com/devops/icafe/issue/CPD-278079/show?t=mention&mt=doc&dt="
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\scripts\\business\\mrd\\plus会员+pro会员店铺.md"
---
MRD

[[CPD-278079] plus会员+pro会员店铺页mrd](https://console.cloud.baidu-int.com/devops/icafe/issue/CPD-278079/show?t=mention&mt=doc&dt=sdk)

|修改日期|修改内容|修改人|
|-|-|-|
|20250320|创建需求文档并完成V1.0 调研+C端权益输出|武惠韬|
|20250408|创建B端、O端需求详情|杨格|

### 一、需求背景&收益
#### **背景：**[会员plus设计](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/8CmleX0Skc/k4X3VvK4Qrz_1Q?t=mention&mt=doc&dt=doc)
|版本|标准版|品牌高级版（PLUS）|品牌旗舰版（PRO）|
|-|-|-|-|
|起售门槛|单店可售|单店可售|单店可售|
|单店刊例价|1499元|3499元|5499元|
|投流充值门槛|单店：500元首充捆绑 连锁：不强制捆绑|单店：500元首充捆绑 连锁：不强制捆绑|单店-49家店铺：500元首充捆绑 50家店铺及以上：不强制捆绑|
|定价逻辑|店铺会员单店刊例|店铺会员单店刊例+品牌通定制版底价 （PS.考虑本地销售政策及整合后竞争力提升，以合计定价为基础，增加20%溢价系数后向上微调美化售价）|店铺会员单店刊例+品牌通定制版底价 （PS.考虑品牌馆资源赠送，智享版为基数，增加100%溢价系数向下微调美化售价5999元）|

#### **收益**：按照25年20w会员目标预估，增加plus版+选购方案后，会员整体收入+3184w，粗估详情为：高级版（plus） 1w单 3499，1w单连锁均价999；旗舰版1w单 均价2399；
### 二、方案设计
#### 现状调研summary：地图类产品以地理位置为中心，以店铺视角展开品牌的权益分布；搜索/内容/电商产品以检索词为中心，分商品、店铺场景展开品牌馆的权益分布。
对比非品牌旗舰会员，主要权益差异体现为支持品牌个性化配置的程度高，如官网外跳、皮肤分级、品牌特色服务、品牌活动、热卖商品等。

* 详情参考：[权益配置](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/PhWJPFLUSm/gMU57F1tJHQX8E?t=mention&mt=doc&dt=doc)

|权益模块|店铺会员现状|百度地图|高德地图|美团|抖音|
|-|-|-|-|-|-|
|商家相册|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ccaa4a0a6e2741fc825843c32f2bfbf2&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=512672dc35c84d9f99cc3f556a1cf63a&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=515eedac24214cf49f19c6e1094e835b&docGuid=gMU57F1tJHQX8E "")|- (以品牌官网主页代替）|- (以品牌官网主页代替）|
|地址|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6c97e1c3a180458087249af7d9a7ddff&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=78a5167cdc3e41b0b372568bc3b17010&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a8e423c6bb784b599744cd2afe339eae&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c1acb0cb62cf44b0abb24229c30cfe9c&docGuid=gMU57F1tJHQX8E "") 仅名称体现店铺区域|- （注重电商平台）|
|特色服务|-|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e7501762243a4d8a99513793beaf0ded&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e7352b78ca7a4c3c8e5a769c01844367&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=87c5695a4f2141c893f65757484320f6&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=67951a81418647588b3712fe3d954134&docGuid=gMU57F1tJHQX8E "") (嵌入品牌官网主页代替）|
|咨询组件|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4406d6c3aac74867892b56c870de4e1c&docGuid=gMU57F1tJHQX8E "")||![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=12a04dc85d3b4cb088dc521de137d137&docGuid=gMU57F1tJHQX8E "") 以智能体提供店铺咨询服务 |![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fdd06280bcac46c2b177723604e7d5e6&docGuid=gMU57F1tJHQX8E "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=064d816f0a1a4444ab4a4129b11100a2&docGuid=gMU57F1tJHQX8E "") 以商品客服入口代替咨询组件|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=618b0c800e7b407d812bb4191005d909&docGuid=gMU57F1tJHQX8E "") 以商品客服入口代替咨询组件|
|风控相关|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=be68647ad8064aa7a607041e3fab000e&docGuid=gMU57F1tJHQX8E "")||-|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5afb239bf6e74d0d8d986efaa71bb63e&docGuid=gMU57F1tJHQX8E "") 商品假一赔四、官方认证等保障|-|
|Banner位|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8648c75e4a2e400a93f5ca0c8f6f1b53&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=772e0172557a4e168faf56b567208593&docGuid=gMU57F1tJHQX8E "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e5806ffc242a448e9e582aa251b62eb1&docGuid=gMU57F1tJHQX8E "")|- （主流活动嵌入商品列表及框架）|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ef91c50e8b4648dea62e67b441e8119f&docGuid=gMU57F1tJHQX8E "")|

* 百度会员Pro权益列表

|权益类型|品牌店铺类型|高德|美团|抖音|快手|淘宝|京东/微信|拼多多|百度双端融合会员Pro版最终权益||
|-|-|-|-|-|-|-|-|-|-|-|
||||||||||搜索|地图|
|C端流量入口权益|特殊样式sug|✅|✅|✅|❌|❌|❌|❌|✅|✅|
||定向活动资源入口|✅|✅|✅|✅|✅|❌|✅|✅|✅|
|列表页权益|列表页特殊标签|✅|✅|✅|✅|✅|✅|✅|✅|✅|
| 店铺主页权益|官网外跳页入口|❌|❌|✅|❌|❌|❌|❌|✅|❌|
||品牌详情页顶部banner|✅|✅|✅|✅|✅|✅|✅|✅|✅|
||品牌特色服务|✅|✅|✅|✅|✅|✅|✅|✅|✅|
||品牌热卖商品|✅|✅|✅|✅|✅|✅|✅|✅|✅|
||品牌活动信息|✅|✅|✅|✅|✅|✅|✅|✅|✅|
||品牌详情页底部banner|✅|✅|✅|❌|✅|❌|❌|✅|✅|
||SUG入口/检索入口/品牌馆头卡|✅|❌|❌ （以官方号替代）|❌|❌|❌|❌|pending|✅|
||品牌馆顶部banner|✅|✅|❌ （以官方号替代）|❌|❌|❌|❌|pending|✅|

#### 迭代节奏：
    * 一期：cover地图已有基础，在搜索端同步升级会员旗舰店铺页& B端店铺装修页
    * 二期：结合AI转化组件等功能，全面扩展店铺页形态及效果

#### 权益导览
[流程图]
### 三、需求详情
#### 需求列表
|序号|开发节奏|需求名称|权益生效/配置范围|开发周期|
|-|-|-|-|-|
|1|I期|店铺详情页-Plus版权益|双端|I期|
|2||中水滴标识权益|地图|I期|
|4||会员首页|B端|I期|
|5||创建会员|B端|I期|
|5||会员皮肤|B端|I期|
|6|II期|列表页V标|双端|II期|
|7||店铺详情页-Pro版权益|双端|II期|
|8||品牌详情页顶部/底部Banner|B端|II期|
|9||品牌特色服务|B端|II期|
|10||热卖商品信息|B端|II期|
|11||品牌活动信息|B端|II期|
|12||O端管理平台|O端|II期|
|13|III期|品牌馆|双端|III期|

#### 搜索UI: [https://www.figma.com/design/C3tdTTDiQc75k5HqdYQTPa/%E6%9C%AC%E5%9C%B0%E9%9C%80%E6%B1%82%E6%B1%87%E6%80%BB-2024%E6%96%B0?node-id=11906-139696&t=wAOSk3KQgUEil4AC-1](https://www.figma.com/design/C3tdTTDiQc75k5HqdYQTPa/%E6%9C%AC%E5%9C%B0%E9%9C%80%E6%B1%82%E6%B1%87%E6%80%BB-2024%E6%96%B0?node-id=11906-139696&t=wAOSk3KQgUEil4AC-1)
#### 地图UI：待更新（V1已于4.9输出，V2预计4.16输出）
* 流程图

[流程图]
#### 权益列表
|等级|基础会员|plus会员|pro会员|
|-|-|-|-|
|主要权益 |标识权益：双端『V』标 流量： 搜索：店铺寻址、品牌寻址、服务推荐、搜索POI 地图：精搜直达 装修：标准皮肤、基础组件 营销：礼包、优惠券 经营：商产品、基础线索转化 经营分析：商品诊断、店铺诊断、线索管理|沉浸皮肤  / 基础皮肤 二选一 水滴logo 免保|标识：V-品牌 /  V-官方 /  V-连锁  选一 皮肤：质感皮肤 / 沉浸皮肤  / 基础皮肤 三选一 会员Pro定制组件主视觉，支持品牌特色服务、热卖产品、活动信息组件配置 品牌馆 水滴logo 免保 外跳|

#### 需求详情：
##### 1.1 C端
|周期：场域|位置|需求原型|需求详情|
|-|-|-|-|
|I期：双端|品牌高级版（PLUS）|![I期彩虹色阶](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bebd09509cae40748f8a8e07d6d4adc6&docGuid=-yJnZITNJR3_5s "I期彩虹色阶") ![沉浸头卡+通用店铺组件](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fa6472f0048146b7ba915f72424d1858&docGuid=-yJnZITNJR3_5s "沉浸头卡+通用店铺组件") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b1d83fc0a7c44af1ab4378da1c2ebc4d&docGuid=-yJnZITNJR3_5s "")|PLUS版关键变更点： 1、店铺结构：基础结构维持与基础会员一致， 店铺现状结构： 店铺头卡：商家相册、基础皮肤、店铺名称、店铺登记、店铺评分、评价人数、城市、标签、营业时间、一级店铺行业、二级店铺行业、详细地址、距离xxkm、电话、百度保障标志、店铺banner 优惠活动：卡券、礼包、精选商品、服务流程、产品服务、真实案例 精选评价：评价组件 商家信息：品牌介绍、服务人员、热门问答 底部banner 智能转化组件 2、店铺皮肤： 皮肤选择逻辑： 1、默认选中店铺头图与9色固定图谱计算色差，默认选中最相近颜色 2、调试店铺皮肤效果，支持品牌高级皮肤及标准皮肤
a、用户可根据预览效果，确认是否更换其他色阶，并根据彩虹配色选择最终效果；
b、支持选配基础皮肤模式 默认色详情：主视觉色在原有8个色彩基础上，增加『黑蓝色』主题，以应对品牌色接近黑白灰或偏好中性色的客户，即总共9色 基础色阶：首期提供plus基础彩虹色共计8个，分为红、浅棕、深棕、墨绿、亮绿、亮蓝、紫色、紫红, 色阶 HSB值如下 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9f99979fa9f24b72b21ad834e73992c0&docGuid=-yJnZITNJR3_5s "") ![黑蓝色最终hsb值待提供](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f5ce30c132f541c487fa91f4cc37c4ae&docGuid=-yJnZITNJR3_5s "黑蓝色最终hsb值待提供")|
|I期：地图端|中水滴标识权益|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3fd54b9cfbae4670bf4c4dbb0b138f6c&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=65950bdd5cf44cc196aa3c35fb933cc7&docGuid=-yJnZITNJR3_5s "")|水滴展示 针对有logo客户：支持地图中水滴权益，场景为泛搜场景，客户需提供完成商标注册的logo物料 展示规范： 水滴内展示商标logo V标展示在水滴右上角 logo物料规范：参考：图像商业化-中水滴规范 尺寸：60px* 68px；分辨率72*72； 提供白天、暗夜两种模式的logo ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b7da6567246e4cff9b7c1b12e95620ba&docGuid=-yJnZITNJR3_5s "") 针对无logo客户：支持地图中水滴权益，场景为泛搜场景，提供默认图集 + v标体系权益 展示规范： 水滴内展示商标logo V标展示在水滴右上角 行业底图素材： 支持黑夜、白天两种模式； 素材行业以地图showtag为基础，枚举如下： ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=16233d74c5134b5598b81edfbc139bb8&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a4f0ff25651a4f3281f2e64d4737f88c&docGuid=-yJnZITNJR3_5s "")  水滴交互 场景及交互：中水滴V标，在泛搜戳点中变为大水滴且隐藏，大水滴权益拆分售卖（全部中水滴场景：精搜、泛搜、泛搜戳点） V标素材（UI稿updating）： 样式：三版高级感递增的样式 标准版：图区&面板展示相同v标，颜色为线上的浅金色 品牌高级版：图区&面板展示相同v标，颜色为黑金色交叠 品牌旗舰版：图区&面板展示相同v标，颜色待设计（更高级） 联动展示效果 水滴右上角的V标展示样式，同步影响头卡的V标、检索列表的等需展示V标位置，保持一致 召回逻辑 召回结果Top10的高阶会员，展示水滴权益 如水滴存在堆叠，需要露出部分V边角|
|I期：搜索端|阿拉丁卡V标|![阿拉丁卡](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ff61bbf4ef4c40b4963ae5a4b276e538&docGuid=-yJnZITNJR3_5s "阿拉丁卡") ![查看更多列表](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=29fab7ae54a24776a758279a03bc005f&docGuid=-yJnZITNJR3_5s "查看更多列表") ![新版V标示意图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=16dca96406b4438586afa0e135f02949&docGuid=-yJnZITNJR3_5s "新版V标示意图") https://www.figma.com/design/ik546FtqN5hUgIlk9bpVDM/%E6%83%A0%E7%94%9F%E6%B4%BB-2025%E8%A7%86%E8%A7%89%E6%96%87%E4%BB%B6?node-id=52-9623&p=f&t=2BZiJOOMegeNmll5-0|阿拉丁卡店铺展示V标 需求范围： 店铺页 所有阿拉丁卡片（涵教育，健康） 查看更多列表页内 展示形式： 根据基木鱼后台会员的身份类型不同展示不同的V标 仅在会员生效期间展示 三版高级感递增的样式 去掉商户等级的V标 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ccd1c125506649138d3a379e9fdedc29&docGuid=-yJnZITNJR3_5s "") 店铺页内点击V标后，文字提醒： 根据商户经营投入力度，当前店铺被判定为优选店铺/甄选店铺/奢选店铺 ![参考样式](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=06cb9896884849c2a4997b31771ecf43&docGuid=-yJnZITNJR3_5s "参考样式")|
|II期：双端|品牌旗舰版（Pro）|线上店铺页现状（before） ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=33aab4e83c2744bfa63236427aa4444d&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=596b1e856623461fb9a01dc2b180e1c1&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5f1549eae9f946aa949437c9d30ef0ff&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b7518c9042984637a60c91bb774391ac&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=197c3c97393b4cb0ad41b225b3efe18e&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8cea9229645d4aa595696d30443f9fb6&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=657301b397d041dcb75b20b49fb82a45&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=beaa74ee7a2d494287e7c48ad9084b38&docGuid=-yJnZITNJR3_5s "") 品牌旗舰店铺页原型（after） ![店铺页头图+ 顶部banner+ 特色服务](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b8cbeeb20fd544abb4e920b9034dfbda&docGuid=-yJnZITNJR3_5s "店铺页头图+ 顶部banner+ 特色服务") ![热卖商品+活动信息](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cc1b90e2ccc7496b9d079aca45537456&docGuid=-yJnZITNJR3_5s "热卖商品+活动信息") ![店铺页基础锚点结构](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8bc01ec3e3e84334ac25f3b58b386042&docGuid=-yJnZITNJR3_5s "店铺页基础锚点结构")  搜索端UI定稿： pro会员-质感皮肤 ![黑金封带+ 渐变头卡](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=53bf8f2a10434e89a828d7ca833c0a66&docGuid=-yJnZITNJR3_5s "黑金封带+ 渐变头卡") ![定制化模块](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ab8f35a9bd444d74b72105810dc86b16&docGuid=-yJnZITNJR3_5s "定制化模块") ![特色底栏](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=292ca68c67e54e57a2da0512bfc073f2&docGuid=-yJnZITNJR3_5s "特色底栏") pro会员-沉浸皮肤 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6eb08c2114d54fdf8e807330afc65dd6&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=59b5464d95494b71aa7eb51156be1f17&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4e073fe76f0e47acba3d2fc52b538bdd&docGuid=-yJnZITNJR3_5s "") pro会员-基础皮肤 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a742349df15b43a6993e60bea5c84f97&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=232adbb709d84d51995fd83f307681f8&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=275278826d264e04a43696d8d52add92&docGuid=-yJnZITNJR3_5s "")|PRO关键变更点： 店铺页关键结构新增： 店铺现状结构： 店铺头卡：商家相册、基础皮肤、店铺名称、店铺登记、店铺评分、评价人数、城市、标签、营业时间、一级店铺行业、二级店铺行业、详细地址、距离xxkm、电话、百度保障标志、店铺banner 优惠活动：卡券、礼包、精选商品、服务流程、产品服务、真实案例 精选评价：评价组件 商家信息：品牌介绍、服务人员、热门问答 底部banner 智能转化组件 品牌旗舰店铺页结构更新： #关键权益差异点1：基础版仅支持默认；plus会员可选择行业皮肤底色（共8种）/基础版皮肤；旗舰会员pro可选择 旗舰皮肤/ 行业皮肤底色（共9种）/基础版皮肤 #关键权益差异点2：基础版&plus版结构fit现状，旗舰会员在B端新增会员pro配置专区，模块a-e均可配置开关，开店侧配置『开』后前端展示；顺序为头卡、a-d、优惠活动、精选评价、商家信息、底部banner 品牌旗舰皮肤（变更）：品牌旗舰皮肤、品牌高级皮肤及标准皮肤；  1、默认选中旗舰版皮肤，主色调为根据头图推荐8色之一； 2、调试店铺皮肤效果，可选配其他颜色
a、用户可根据预览效果，确认是否更换其他模式皮肤（支持使用沉浸皮肤/基础皮肤模式）
b、沉浸皮肤模式及基础皮肤模式仍存在品牌黑标与v标；v标按照b端配置3选1进行展示； ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4de578b384574a6992ec2a5d64062f07&docGuid=-yJnZITNJR3_5s "") a、品牌详情页顶部banner（新增）: 上限设置为8帧；点击后进入banner详情页，详情页名称为『活动详情页』 b、品牌特色服务（新增）:单行排列，下限设置为4个，上限设置为8个，横滑查看更多，点击后进入详情页，详情页名称为『特色服务详情页』 c、品牌热卖商品（新增）: 分类：分tab展示商品，tab依次为品类1、品类2、品类3，品类限制上限10个； 样式：双行排列，单屏4个，上限12个，横滑查看更多，点击后进入详情页，详情页名称为『热卖商品详情页』； d、品牌活动信息（新增）：竖排，上限5个，点击后进入详情页，详情页名称为『品牌活动信息详情页』； e、品牌详情页底部banner（新增）： #关键权益差异点3：新增品牌馆权益，是否新增待定 a、SUG入口/检索入口/品牌馆头卡（新增） logo：统一要求 品牌馆名称：10字内 品牌slogan：第二行副标题，限制12字内 标签：金色“V品牌馆”，无法更改 b、品牌馆顶部banner（新增）、特色服务、热卖产品、活动信息、底部banner 以下结构不发生变更 优惠活动：卡券、礼包、精选商品、服务流程、产品服务、真实案例 精选评价：评价组件 商家信息：品牌介绍、服务人员、热门问答、 底部banner 智能转化组件|
||阿拉丁前卡列表页|![地图精搜列表页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8e12efcec484456096eea9bae435a515&docGuid=-yJnZITNJR3_5s "地图精搜列表页") ![搜索端经手列表页原型](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=db7496d8b8844daa86029f366e5a8072&docGuid=-yJnZITNJR3_5s "搜索端经手列表页原型")|店铺标志：阿拉丁前卡增加『品牌』v标；双端标志与权益对齐 标志值域： 官方、连锁、旗舰 3选1； 搜索端样式： ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=84346fc7d4b9400aaa7368827867105e&docGuid=-yJnZITNJR3_5s "") 地图端样式：（待更新）|
||8、SUG入口/检索入口/品牌馆头卡|-|logo：统一要求 第一行标题，限定10字内 列表页统一使用第一行标题文案 第二行副标题，限制12字内 金色“V品牌馆”，无法更改|
||9、品牌馆顶部banner|-|图片尺寸：尺寸710*220，小于150KB 落地页图片：图片尺寸750*x，小于1MB|

##### 1.2 B端
|场域|位置|需求原型|需求详情|
|-|-|-|-|
|B端I期|会员列表|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=15fef09312ae4b3ba0b6d725c36bc35c&docGuid=-yJnZITNJR3_5s "")|店铺会员页面 会员列表页：新增会员类型字段 店铺会员 品牌高级会员 会员类型加提醒：当前生效会员类型|
||会员购买|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cbb4f5b3c6b84a488405f4853d74da94&docGuid=-yJnZITNJR3_5s "")|会员下单界面新增字段：【会员类型】 枚举值【百度店铺会员】【品牌高级会员】 仅可单选 会员类型新增【 ? 】角标，跳转会员类型介绍文档 流量倾斜类目：保持线上逻辑不变 店铺选择组件： 店铺筛选框：【会员生效状态】枚举值 店铺会员生效中、 品牌高级会员生效中、 店铺会员待生效、 品牌高级会员待生效、 未开通 其他逻辑不变 商品描述： 0-49家 当选中会员类型为【店铺会员】，页面提醒【店铺会员¥1499+流量宝¥500   注：系统将自动为您创建流量宝计划，可在流量宝模块查看管理】 当选中会员类型为【品牌高级版】，页面提醒【品牌会员¥1999+流量宝¥500   注：系统将自动为您创建流量宝计划，可在流量宝模块查看管理】 50家及以上 当选中会员类型为【店铺会员】，页面提醒【百度店铺会员服务】 当选中会员类型为【品牌高级版】，页面提醒【品牌高级版xxxx元】 后端逻辑：绑定下单自动创建流量宝计划 会员权益时长累加，若当前生效中店铺会员有效期至2026-01-01，此时购买品牌高级会员，品牌高级会员从2026-01-02开始计收，生效，有效期为2026-01-02 至 2027-01-01|
||店铺基础信息|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=327732d419fd4be5b2fa792a540611ac&docGuid=-yJnZITNJR3_5s "")|场景：新建单店铺、批量新建店铺、修改店铺、批量修改店铺均需支持水滴logo上传 展示【店铺基础信息】页面新增 水滴logo： 字段需区别展示，vip专属样式等 选项：a. 行业logo b. 自定义logo 默认选中行业logo，悬浮提醒【行业logo根据店铺所属行业信息展示，不可变更】， 当选中：自定义logo， 出现图片上传框：点击图片上传框出现弹窗上传物料信息 上传框下方提醒：仅支持60px* 68px；分辨率72*72 上传校验图片尺寸，不符合尺寸不可上传 出现背景色选择：「透明」「不透明」单选，默认选中「透明」 出现【商标许可证】+【品牌授权】+【商标持有人营业执照】三个信息上传+有效期 店铺信息点击提交后，送审 当鼠标悬浮水滴logo模块，页面右侧【填写提醒模块】： 水滴logo仅针对百度品牌会员生效，仅在百度地图app端展示，出一张地图展示的样式demo 行业logo根据店铺所属行业信息展示，不可变更 如需展示自定义logo，需提供对应【商标许可证】+【品牌授权】+【商标持有人营业执照】，经审核后生效|
||店铺装修|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7a0a35e9120745208862e18e465238dd&docGuid=-yJnZITNJR3_5s "")|进入店铺装修界面，当选择的店铺会员身份为【品牌高级版】，且会员状态为待生效、生效中，展示【品牌高级版装修界面】 装修界面展示2个模块：行业皮肤、预览 行业皮肤：可选「沉浸皮肤模式」「经典皮肤模式」，仅支持单选，默认选中「沉浸皮肤模式」 当选中为「沉浸皮肤模式」 颜色选择框，可供选择9个选择【红、浅棕、深棕、墨绿、亮绿、亮蓝、紫色、紫红、黑篮】，给个颜色的框 默认选中店铺头图/视频首帧封面与9色固定图谱计算色差，默认选中最相近颜色 预览：右方预览界面展示店铺页+皮肤样式，颜色+模块渲染同用户配置 点击提交，或选择使用店铺  当选择的店铺会员【品牌高级版】非生效中，展示【品牌高级版装修界面】，页面弹窗或其他样式提醒【品牌高级版装修仅针对 「品牌高级版会员」生效】+一个有效期|
|会员|会员权益||当ucid下有一个生效中、待生效的【品牌高级会员】，账户免保 只要账号下有购买1个品牌会员，即可免保，品牌会员购买待生效场景也免保|
|B端II期|3、会员皮肤|![旗舰模式](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ce4d3a9c638e40c8a38883f10c3765bc&docGuid=-yJnZITNJR3_5s "旗舰模式") ![会员模式](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4cffbbbf29814af5813cc6fa416d3da1&docGuid=-yJnZITNJR3_5s "会员模式") ![预览](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=683a0d6d41f84196b79e5d6bd63f0609&docGuid=-yJnZITNJR3_5s "预览")|可选旗舰皮肤模式（会员pro）、会员皮肤模式（会员plus）；每种模式提供1-3套皮肤（详细数量待定）；选择后右侧预览适配效果；效果自动适配至 商家相册交互、品牌边框、底bar颜色、字体主色|
||4、品牌详情页顶部/底部Banner|![预览](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2f71e7bffa8642a2bcdf6c13aac6fde1&docGuid=-yJnZITNJR3_5s "预览") ![顶/底部Banner列表页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4fd8db28552e4acfbc443f69f4b603f4&docGuid=-yJnZITNJR3_5s "顶/底部Banner列表页") ![顶/底部Banner编辑项](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5b3a35e604d54be8b4ce86dae200af72&docGuid=-yJnZITNJR3_5s "顶/底部Banner编辑项")|列表页： Banner数量：上限设置为8帧 字段：banner头图、banner名称、id、审核标签 操作：添加banner、批量操作（II期）、编辑、适用门店、解除绑定 详情编辑页： 字段：行业（不可更改）、banner名称、banner头图、banner详情页 图片要求： banner头图尺寸要求：尺寸710*170，小于150KB banner详情页图片要求：图片尺寸750*x，小于1MB|
||5、品牌特色服务|![预览](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=49746c0852c1420a8d8418e321adddc9&docGuid=-yJnZITNJR3_5s "预览") ![特色服务列表页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c28ea4eb6e1f4f9493c50496ed776c4d&docGuid=-yJnZITNJR3_5s "特色服务列表页") ![特色服务编辑页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=80176a3ed8384c60bbc86ba169817e48&docGuid=-yJnZITNJR3_5s "特色服务编辑页")|1、列表页字段： 数量：上限设置为8个 字段：logo、服务名称、id、审核标签 操作：添加服务、批量操作（II期）、编辑、适用门店、解除绑定 2、新增/编辑可编辑字段按钮： 图片icon：尺寸68*68，小于150KB 文案：不超过4字 特色服务详情页：图片尺寸750*x，小于1MB 数量：小于等于8个  |
||6、热卖商品信息|![预览](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5099efdc4181408fa3447ba94e0901aa&docGuid=-yJnZITNJR3_5s "预览") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c7c0dc7a9b2a49ebbce7f73182b6ec37&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3795bc41091b457ab5b2e95738e0f132&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=39fb2a2b931442a7863136fb4d4bbd9d&docGuid=-yJnZITNJR3_5s "")|列表页： 字段： 品类名称、品类头图（I期不展示，II期升级后展示） 数量限制：种类数量：10个以内（建议5个） 操作：编辑、使用门店、解除绑定 详情页编辑： 1、种类图：尺寸780*780，小于150KB，建议透明底 2、商品选择来源： 在已通过审核的『店铺装修-产品服务』中选择； 3、图片要求： 为适配热卖商品尺寸，需在创建商品时按照以下要求完成对应商品创建： 商品图要求：尺寸780*780，小于150KB，建议透明底，每个种类商品数量不限制 商品详情页头图：尺寸780*780，小于150KB，建议透明底，6张以内 商品详情页详情图：尺寸750*x，小于1MB，支持3张图拼接|
||7、品牌活动信息|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=534b133e19fa4683b8a68d443ef3fea6&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2f5be40e97f34ae793f2355043d1a9e6&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2504653df4914dde9342024fbe107c42&docGuid=-yJnZITNJR3_5s "")|1、列表页字段： 数量：活动最多5个 字段：头图、主标题、活动描述、落地页图片  2、新增/编辑可编辑字段按钮： 图片icon：尺寸124*124，小于150KB 主标题：10字以内 活动描述：25字以内 落地页图片：图片尺寸750*x，小于1MB|

##### 1.3 O端
|场域|位置|需求原型|需求详情|
|-|-|-|-|
|O|会员商品管理|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=abf99e8a91734030b3e5cce8e9483abe&docGuid=-yJnZITNJR3_5s "")|创建会员商品 商品类型：选择，必选，枚举值：【健康搜索会员】【健康地图会员】【店铺会员】【品牌高级会员】 测试商品：选择，必选，枚举值：【是】【否】 商品价格：填写价格分|
||会员权益管理|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3d3c2cbcac454ebfb1bf119fde7b770b&docGuid=-yJnZITNJR3_5s "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7b9f32e2d6624323baaec1ca3b866e4d&docGuid=-yJnZITNJR3_5s "")|会员权益管理拆分两部分：会员权益创建、会员权益查看 会员权益创建 点击创建后出现【创建弹窗】 选择会员商品：必选，单选，【品牌高级会员】【品牌旗舰会员】 选择会员权益：必选，多选，选项包括 水滴权益【水滴logo】 皮肤权益【标准皮肤】【品牌高级皮肤】【品牌旗舰皮肤】 V标识权益 品牌馆 免保 外跳权益 权益的单独配置 6个权益项支持byucid白名单配置|

### 四、数据需求
|端|打点详情|
|-|-|
|C端|PLUS店铺页展现pv、uv；|
||店铺头卡点击pv、uv|
||店铺页流量时长|
||店铺页转化组件点击pv、uv|

### 五、小流量实验方案
* 对照组：线上皮肤方案
* 实验组：plus会员皮肤方案
* 实验方案：10%流量，监测实验组皮肤转化效率，正向置信后推全

### 六、排期&沟通地图
|端|类目|沟通地图|
|-|-|-|
|搜索|会员Plus/Pro产品负责人|马海娜|
||会员Plus/Pro C端店铺页|PM: 武惠韬&郭翀亦 FE：黄诗铭 & 曾昊林|
||会员Plus/Pro  B端配置|PM: 杨格 RD：梁东& 王丹凤|
||会员Plus/Pro 运营接口人|王成业|
|地图|||

参考文档：

1、地图品牌通物料上传内容：[品牌通物料格式说明文档（可下载）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/HwaWZj7TWb/92PXd1OOqT/7nPR209e6z1OAP?t=mention&mt=doc&dt=doc)

2、品牌会员：[品牌会员](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/PhWJPFLUSm/TP1Sj78x_irP4A?t=mention&mt=doc&dt=doc)