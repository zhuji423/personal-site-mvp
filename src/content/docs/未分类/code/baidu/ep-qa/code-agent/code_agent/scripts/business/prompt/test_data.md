---
title: "test_data"
description: "你是一个接口文档结构抽取专家，请你根据以下【研发详设文档】，严格提取所有“对外接口说明”中的接口信息，转换为统一的结构化 JSON 格式，供后续自动化评估系统使用。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\scripts\\business\\prompt\\test_data.md"
---
你是一个接口文档结构抽取专家，请你根据以下【研发详设文档】，严格提取所有“对外接口说明”中的接口信息，转换为统一的结构化 JSON 格式，供后续自动化评估系统使用。

## 输出格式
请返回如下 JSON 结构：
```json
{
  "code_base": ["涉及的icode模块路径，如有"],
  "apis": [
    {
      "name": "接口名, 参考小节标题，不错改写",
      "desc": "接口功能描述，必须保留原文内容，不做改写",
      "uri": "接口地址字段原文",
      "req_params": {
        "字段名": "字段类型 // 字段含义（完全保留原文注释）"
      },
      "resp_params": {
        "字段名": "字段类型 // 字段含义（完全保留原文注释）"
      },
      "change_type": "NEW|MODIFIED"
    }
  ]
}
```


## 字段提取规则说明

1. 提取“详细设计”部分出现的接口，通常每一小节对应一个接口；
2. `name` 接口名称参照子标题；
3. `uri` 为表格中“接口地址”的值；
4. `desc` 字段务必保留接口描述的原文表述，不可改写；
5. `req_params` 与 `resp_params` 字段，请从接口示例 JSON 中提取字段名与结构，并尽可能识别字段类型（如为数字则为 int，字符串则为 string，布尔值为 bool，嵌套结构请保持原结构）；
6. 所有字段注释必须保留，使用 `字段类型 // 原文注释` 形式；
7. 只处理 JSON 格式的参数结构（忽略流程图、URL 说明等非结构化信息）；
9. 新增的接口 change_type 标记为 `NEW`，修改的接口 change_type 标记为 `MODIFIED`，如果文档中没有说明按照新增处理；
10. 严禁主观推测、扩展或改写内容，必须严格根据原文提取。

---

## 研发详设文档内容如下：

详设

## 1. 项目背景
    * 项目MRD链接：*

*     项目主要需求说明：*搭建初版服务商平台，实现服务商开户；其他复用开店原有的开店下单能力、财务平台的开票退款能力。



## 2. 总体设计（可选）
###     2.1 升级icode模块名称list
|模块名|升级功能描述|
|-|-|
|baidu/pa/store-b|商户创建、删除、账户查询等功能|

###     2.2 整体流程图
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f765f6fcd91b4491a4748150cc547aa0&docGuid=6_4Kky8iC8Mx3A "")
## 3. 详细设计
###  3.1 密保手机号校验
####     3.1.1 功能逻辑&流程图说明
调用CRM接口，CRM接口说明：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ed9f8c2e064e416f95b65c43d2f4495a&docGuid=6_4Kky8iC8Mx3A "")
####     3.1.2 对外接口说明 
|接口地址|StoreShopAgentService/checkSecretPhone|备注 后端封装： 密保手机号验证： UserSecureInfoService.findBindCountByMobile()|
|-|-|-|
|参数|{
        "secretPhone":13110001000 // 密保手机
}| |
|返回|{
    "data": {
        "count": 2,
        "isBlock": 0,
        "allowLogin": 1,
        "allowBind": 1,
        "canBindCount": 10
    },
    "expand": {},
    "status": 0,
    "errors": []
}||

###  3.2 商户创建
####     3.2.1 功能逻辑&流程图说明
[流程图]


####     3.2.2 对外接口说明 
|接口地址|StoreShopAgentService/saveOrUpdateMerchant|备注 后端封装： 注册UC账号： UcBaseService.ucRegist() uc暗绑pass： UcBindApiService.acquireBindInfo()|
|-|-|-|
|参数|{
    "id": 111, // 更新时必填
    "appId": 269,
    "subAppId": 669,
    "saveFlag": 1, //1 保存 2保存并送审
    "companyVo": {
        "licenseUrl": "https://jmy-pic.baidu.com/0/pic/657810310_135311176_-374519386.jpg",
        "companyName": "保山市隆阳至乐汽车配件经营部",
        "businessLicense": "92530502MA7JWN3702",
        "licenseStartTime": "2024-11-20 00:00:00",
        "licenseEndTime": "9999-01-01 00:00:00",
        "businessProvince": "云南省",
        "businessCity": "保山市",
        "businessDetailAddress": "保山市隆阳区九隆街道办事处泰龙社区居民委员会建设路兴和苑5号",
        "businessScope": "一般项目：汽车零配件批发；汽车零配件零售；润滑油销售；轮胎销售；机动车修理和维护(除依法须经批准的项目外，凭营业执照依法自主开展经营活动)。",
        "businessArea": "隆阳区",
        "supplierType": 2, // 2 个体工商户
        "qualifySource": 2 //  2为手动填写 4 非营业执照
    },
    "shopId": 247559003,
    "ucId": 247559003,
    "contact": "客户联系人",
    "contactPhone": "客户联系人电话", // 质名称
    "ucName": "账号名称", //
    "secretPhone":13110001000 // 密保手机
}|1、草稿态只保存信息，不进行送审， 不提交CRM创建账  商户相关的数据添加到表 tb_shop_info 字段：tp_id 记录TP代理商的ucid 草稿：复用 audit_status   SHOP_STATUS_DRAFT(3, "店铺-草稿"), SHOP_STATUS_REFUSE(4, "店铺-拒绝"), SHOP_STATUS_AUDIT(5, "店铺-审核中"), SHOP_STATUS_PASSED(6, "店铺-审核通过"), 商户资质相关数据添加到表 tb_shop_trade_qualification 地址信息 tb_shop_map  账户相关的数据添加到表 tb_tp_user_info   账户名称不能重复 |
|返回|{
    "data": {
        "id": ""
    },
    "expand": {},
    "status": 0,
    "errors": []
}||
|调用CRM创建账号接口|服务商用户创建推广账号 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f4a80255f0904adc9ef5d38bd349d0d1&docGuid=6_4Kky8iC8Mx3A "")|custName: 公司资质名称|
|创建完UC账号后默认创建passId|获取唯一关系  acquireBindInfo||

#### 3.2.3 数据结构说明
```

CREATE TABLE `tb_tp_user_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键自增',
  `tp_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'tp用户id',
  `uc_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '用户id',
  `pass_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'passid',
  `uc_name` varchar(64) NOT NULL DEFAULT '' COMMENT '账号名称',
  `shop_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '店铺id',
  `contact` varchar(64) NOT NULL DEFAULT '' COMMENT '客户联系人',
  `contact_phone` varchar(256) NOT NULL DEFAULT '' COMMENT '客户联系人电话',
  `secret_phone` varchar(256) NOT NULL DEFAULT '' COMMENT '密保手机',
  `is_delete` int(4) NOT NULL DEFAULT '0' COMMENT '是否删除 0-未删除,1-已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_tp_id` (`tp_id`),
  KEY `idx_uc_id` (`uc_id`),
  KEY `idx_uc_name` (`uc_name`),
  KEY `idx_shop_id` (`shop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='tp客户表';
```
### 3.3 商户信息修改
|接口地址|复用添加接口|备注 封装后台调用UC接口 更新公司名称：UcUserService.updateSfInfo()|
|-|-|-|
|参数||1、修改信息也是可以保存草稿态 2、修改信息这可以修改商户相关的数据|
|调用CRM修改账号接口|推广账号信息更新通用接口 {"ucId":10000,  "company":"公司名称"}|  |

### 3.4 商户删除- 只有草稿数据支持删除
####     3.4.1 对外接口说明 
|接口地址|StoreShopAgentService/deleteMerchant|备注|
|-|-|-|
|参数|{
        "id":1001
}|ucId不为0时可以删除|
|返回|{
    "data": {},
    "expand": {},
    "status": 0,
    "errors": []
}||

### 3.5 查看商户详情
####     3.5.1 对外接口说明 
|接口地址|StoreShopAgentService/queryMerchantDetail|备注|
|-|-|-|
|参数|{
    id:10001
}||
|返回|{
    "data": {
        "id": 100001,
        "shopId": 123456, // 商户id
        "companyVo": {
            "licenseUrl": "https://jmy-pic.baidu.com/0/pic/657810310_135311176_-374519386.jpg",
            "companyName": "保山市隆阳至乐汽车配件经营部",
            "businessLicense": "92530502MA7JWN3702",
            "licenseStartTime": "2024-11-20 00:00:00",
            "licenseEndTime": "9999-01-01 00:00:00",
            "businessProvince": "云南省",
            "businessCity": "保山市",
            "businessDetailAddress": "保山市隆阳区九隆街道办事处泰龙社区居民委员会建设路兴和苑5号",
            "businessScope": "一般项目：汽车零配件批发；汽车零配件零售；润滑油销售；轮胎销售；机动车修理和维护(除依法须经批准的项目外，凭营业执照依法自主开展经营活动)。",
            "businessArea": "隆阳区",
            "supplierType": 2,
            "qualifySource": 2
        },
        "shopStatus": 6, // 商户状态 
        "memberStatus": 1, // 会员状态 1是有会员 0是无会员
        "ucId": 10001,
        "ucName": "账号名称",
        "contact": "客户联系人",
        "contactPhone": "客户联系人电话", // 质名称
        "ucName": "账号名称", //
        "secretPhone": 13110001000 // 密保手机
    },
    "expand": {},
    "status": 0,
    "errors": []
}| 商户状态：码值复用现有码值 草稿【账号仅保存草稿态，未提交】 审核中【已创建账号，本地商户审核中】 已生效【账号已创建，本地商户审核通过】 拒绝状态【审核未通过】 会员状态： 未生效【商户下全部店铺未购买会员、会员过期】 待生效【商户下有待生效的会员】 已生效【商户下有一条或多条生效中的会员】|
||||

### 3.6 查询对公打款账号
####     3.6.1 功能逻辑&流程图说明
调用财务接口：

[获取用户对公转账账号接口](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/DDWA7rKjDG/ctFiYDJ-YO/wGYEXOXzhTIYyk?t=mention&mt=doc&dt=doc)

####     3.6.2 对外接口说明 
|接口地址|FinanceService/queryUcBankInfo|备注 后端接口封装：UcFinancePayService.getAutoBankInfo()|
|-|-|-|
|参数|{
    ucId:10001 // 商户的账号的uc
}||
|返回|{
    "data": {
        "acctName": "百度在线网络技术（北京）有限公司上海软件技术分公司",
        "acctBank": "招商银行股份有限公司上海曹家渡支行",
        "acctNo": "2150813928100019000000682"
    },
    "expand": {},
    "status": 0,
    "errors": []
}||

### 3.7 查询TP信息概览接口
####     3.7.1 对外接口说明 
|接口地址|StoreShopAgentService/queryTpOverview|备注|
|-|-|-|
|参数|{
}||
|返回|{
    "data": {
        "merchantsNum": 10, // 商户数量
        "merchantsValidNum": 5, // 商户生效数量
        "shopMemberNum": 5, // 会员生效数
        "merchantsShopMemberNum": 5, // 会员生效商户数
    },
    "expand": {},
    "status": 0,
    "errors": []
}|商户状态：码值复用现有码值 草稿【账号仅保存草稿态，未提交】 待生效【已创建账号，本地商户审核中、未审核通过】 已生效【账号已创建，本地商户审核通过】 拒接状态 会员状态： 未生效【商户下全部店铺未购买会员、会员过期】 待生效【商户下有待生效的会员】 已生效【商户下有一条或多条生效中的会员】|



### 3.8 查询商户列表
####     3.8.1 对外接口说明 
|接口地址|StoreShopAgentService/queryMerchantList|备注|
|-|-|-|
|参数|{
    "auditStatus":1 // 商户状态
    "ucId":1000 账号名称
    "companyName":商户主体名称
    "pageNum":1
    "pageSize":20
}||
|返回|{
    "data": {
        "totalNum": 71,
        "list": [
            {
                "id": 100001,
                "shopId": 1111,
                "companyVo": {
                    "licenseUrl": "https://jmy-pic.baidu.com/0/pic/657810310_135311176_-374519386.jpg",
                    "companyName": "保山市隆阳至乐汽车配件经营部",
                    "businessLicense": "92530502MA7JWN3702",
                    "licenseStartTime": "2024-11-20 00:00:00",
                    "licenseEndTime": "9999-01-01 00:00:00",
                    "businessProvince": "云南省",
                    "businessCity": "保山市",
                    "businessDetailAddress": "保山市隆阳区九隆街道办事处泰龙社区居民委员会建设路兴和苑5号",
                    "businessScope": "一般项目：汽车零配件批发；汽车零配件零售；润滑油销售；轮胎销售；机动车修理和维护(除依法须经批准的项目外，凭营业执照依法自主开展经营活动)。",
                    "businessArea": "隆阳区",
                    "supplierType": 2,
                    "qualifySource": 2
                },
                "shopStatus": 6, // 商户状态
                "memberStatus": 1, // 会员状态
                "ucId": 10001,
                "ucName": "账号名称",
                "contact": "客户联系人",
                "contactPhone": "客户联系人电话", // 质名称
                "secretPhone": 13110001000 // 密保手机
            }
        ]
    },
    "expand": {},
    "status": 0,
    "errors": []
}|1、查询逻辑 ，下面3个表联查， 带着（tp_id 去查询） tb_shop_info tb_shop_trade_qualification tb_tp_user_info 2、后置处理 查询tb_shop_member_info 补充会员状态信息|

### 3.9 充值流水查询
####     3.9.1 功能逻辑&流程图说明
依赖财务接口

|财务接口|流水查询接口 支付方式码表 {
    "fundtype": 1, // 1=》直销（TP）用户现金流水
    "condition" : {
         "uid": 2008780, // ucid
         "paytime": {            // 可选，付款时间范围
             "gte": "2025-03-01 00:00:00",  // paytime >= "2025-03-01 00:00:00"
             "lte": "2025-03-25 00:00:00"   // paytime <= "2025-03-25 00:00:00"
         },
         product": {          // 要查询的资金包列表
              "in": [1]    // 推广资金池
         },
    },
    "chunksize": 100, // 批量数据（最大）最小
    "offset": {                 // 结果数据集偏移值 
        "id": {
            "gt/lt": 0,
        }
    },
    "sort": {                   // 排序字段和排序方向列表
        "in": [
            "id asc",
        ]
    }
}   |查询充值的要加上这个字段筛选 "paymethod": {          // 可选，要查询的流水支付方式列表 *             "in": [1,2,3,4]    // paymethod in (1,2,3,4) *         },@徐敏蕾|
|-|-|-|

####     3.9.2 对外接口说明 
|接口地址|FinanceService.getPayRecord|备注 后端接口封装： 查询财务流水：UcDrfinanceService.PaymentRecordVo()|
|-|-|-|
|参数|{
       "ucId":1000, // uc账号
       "payStartTime":"2025-03-01 00:00:00"
       "payEndTime":"2025-03-25 00:00:00",
       "page":{
            "pageSize":10 // 当前显示页数
            "offset":10000 // 数据集偏移值, desc 列表返回的最后的一条数据的payRecordId， asc 列表返回的第一条数据的payRecordId
            "sort":desc // 默认desc（展示最近的充值记录） ，排序 asc/desc
        }
}||
|返回|{
    "data": {
        "totalNum":100,
        "list" [
            {
                "payRecordId": 流水号
                "pay": 100000, // 加款金额，单位分
                "refund": 1000, // 退款金额
                "paytime": "2017-04-24 16:25:43", // 充值时间
                "paymethodTitle": "支付方式", // 支付方式
             }
        }
    },
    "expand": {},
    "status": 0,
    "errors": []
}||

### 3.10 会员订单查询
####     3.10.1 对外接口说明 
|接口地址|StoreShopOrderService/queryMemberOrderListByCondition|备注|
|-|-|-|
|参数|{
       "ucId":1000, // uc账号
       "merchantId":123 // 商户id
       "createTimeStart":"2025-03-01 00:00:00"  // 下单时间起点时间
        "createTimeEnd":"2025-03-25 23:59"  //  下单时间终点时间
        "orderStatus":5 // 订单状态（父） 1待付款 2付款中 3已取消 4付款失败 5已付款 6退款中 7已退款
        "subOrderType": 1 // 子订单类型 1-会员 2-llb
        "page":1,  // 请求页码
        "pageSize":10 // 分页大小
        
}||
|返回|{
    "list": [
    {
        "shopId": 100001, // 店铺id
        "name": "批量到家", // 店铺名称
        "subName": "秋月路店", // 分店名
        "productSpuName": "商品名称",
        "parentOrderId": "100001", // 父订单id
        "subOrderId": "12349348", // 子订单id
        "payFinishedTime": "1970-01-01 00:00:00" // 支付完成时间
        "createTime":"2025-01-01 00:00:00"  // 下单时间
        "orderStatus":  5 // 订单状态
        "orderType" :  1   // 订单类型 1-捆绑订单 2-连锁订单 3-流量宝订单
        "subOrderType": 1  // 子订单类型 1-会员 2-流量宝
         
    },
    {
        "shopId": 100002, // 店铺id
        "name": "批量到家1", // 店铺名称
        "subName": "秋月路店1", // 分店名
        "productSpuName": "商品名称1",
        "parentOrderId": "100001", // 父订单id
        "subOrderId": "123244454", // 子订单id
        "payFinishedTime": "1970-01-01 00:00:00" // 支付完成时间
        "createTime":"2025-01-01 00:00:00"  // 下单时间
        "orderStatus":  5 // 订单状态
        "orderType" :  1   // 订单类型 1-捆绑订单 2-连锁订单 3-流量宝订单
        "subOrderType": 1  // 子订单类型 1-会员 2-流量宝
         
    }
    ],
    "totalNum" : 2000 // 数据总条数
    "expand": {},
    "status": 0,
    "errors": []
}|查询表 tb_shop_order tb_shop_sub_order tb_shop_info|



### 3.11 流量宝订单查询
####     3.11.1 对外接口说明 
|接口地址|StoreCommonFlowPlanService/queryFlowOrderList|备注|
|-|-|-|
|参数|{
       "ucId":1000, // uc账号
       startTime:"2025-03-01 00:00:00"
       endTime:"2025-03-25 00:00:00"，
           "page":1
    "pageSize":20
}||
|返回|{
    "data": {
        "totalNum": 100,
        "list": [
            {
                "planId": 100001, // 流量宝计划id
                "planName": "计划名称",
                "subOrderId": "子订单id", // 子订单id
                "payFinishedTime": "1970-01-01 00:00:00" // 下单时间，支付完成时间
            }
        ]
    },
    "expand": {},
    "status": 0,
    "errors": []
}|查询表 tb_shop_order tb_shop_sub_order tb_flow_plan_bo|

### 3.12 提交待支付订单（选择二维码支付）返回获取财务支付二维码接口
####     3.12.1 功能逻辑&流程图说明
依赖财务接口

|财务接口|移动端收银台接入接口  {
       "uuid":uuid, // uuid 注意点：订单id
       "uid":1001, // ucid
       "passId":1000001 // passId
       "platform":27 // 27：百度收银台一码付 【固定值】
       "product":1, // 充值包 1:推广资金池 【固定值】
       "amount":100 // 金额 = 订单总额， 单位为元，最多两位小数
       "appid": 584 // 固定值
       "appcode":""，
       "returnurl":"https://kaidian.baidu.com/localplat/localshop/member/memberService"， // 用户支付完成后调准url[固定值]https://kaidian.baidu.com/localplat/localshop/member/memberService       "returnurl":"https://kaidian.baidu.com/localplat/localshop/member/memberService"， // 用户支付完成后调准url[固定值]
       "returnData":"{"orderId":"100001"}" // B端订单id
       
} {
"pay_info_str":"" // url
"order_id"： // 财务平台生成的支付订单ID
} |appcode的规则：md5(uid_salt1_appid_salt2) uid：待充值的uid salt1：special-appid（固定值） appid：产线id salt2：ext-netpay（固定值） ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4940b7e513964234817675a4d2920b1f&docGuid=6_4Kky8iC8Mx3A "") 10001_special-appid_584_ext-netpay 然后md5加密|
|-|-|-|

####     3.12.2 对外接口说明 
|接口地址|StoreShopOrderService/createOrder|备注|
|-|-|-|
|参数|{
    "shopId": "商户id",
    "merchantsName": "商户名称", // 注意：：：：资质中的 公司名称
    "orderType": 1, // 订单类型 1-捆绑订单 2-会员订单 3-流量宝订单
    "orderScene": 1, // 订单场景 1-店铺会员订单 2- 大健康订单
    "rightsType": 1, // 会员类型 1-搜索会员 2-地图会员 3-店铺会员'
    "orderPlatform": 1, // 订单来源平台： 1-开店b端， 2-代理商后台（新的应该没有了），3-本地C端，4-地图APP
    "orderSource": 1, // 订单来源 1-非自入驻订单 2-自入驻订单
    "agreementIds": "1,2", // 协议id
    "totalAmount": 200000, // 订单总额 - 分
    "firstCategoryId": 123, // 一级类目
    "secondCategoryId": 456, // 二级类目
    "memberOrderParam": [
        {
            "shopId": 1000,
            "salePrice": 149900, // 商品原价 - 分
            "realPrice": 100000, // 实际售价 - 分
            "productSpuId": 10001, // 会员商品spuID
            "productSpuSkuId": 10001, // 会员商品skuID
            "productPromotionId": 10001, // 会员商品促销ID
            "productPromotionDetailId": 10001, // 会员商品促销详情ID
            "mapUid": "1234gse4",
            "uidType": 1 // 点位类型
        }
    ],
    "flowOrder": {
        "flowOrderNum": 123, // 流量宝订单总数
        "realPrice": 50000, // 真实价格 分
        "totalPrice": 100000 // 流量宝总价格 分
    },
    "payType": 2 // 支付类型 1-资金池支付,  2-现场支付(二维码) [新增]
}|tb_shop_order 表增加支付类型 pay_type:   1 资金池支付 2 现场支付(二维码)  如果用户选择了 2 现场支付，在返回参数中增加payUrl|
|返回 |{
    "data": {
        "shopOrderId": 10, // 订单id
        "payUrl": "" // // 支付url
    },
    "expand": {},
    "status": 0,
    "errors": []
}||





### 3.13 待支付订单详情查询（选择二维码支付）返回获取财务支付二维码接口
####     3.13.1 功能逻辑&流程图说明
依赖财务接口

####     3.13.2 对外接口说明 
|接口地址|StoreShopOrderService/queryOrderDetail|
|-|-|
|参数|{
     "orderId"﻿: "10001"
     "orderStatus":2  // 订单状态 ：2付款中 3已取消 4付款失败 5已付
}|
|返回|{
    "data": [
        {
            "orderId": "35412146",
            "createTime": "2025-02-19 16:28:36",
            "orderType": 1, // 订单类型 1-捆绑订单 2-会员订单 3-流量宝订单
            "totalPrice": 1000, // 订单总金额 
            "orderStatus": 2   // 1待付款 2付款中 3已取消 4付款失败 5已付款 6退款中 7已退款 8退款失败 9部分退款中 10部分已退款 11干预已退款 12订单关闭',
            "memberOrderList": [ // 会员订单
                {
                    "shopId": 1,
                    "shopName": "店铺名称",
                    "address": "店铺地址",
                    "subOrderId": 1,
                    "orderType": 1, // 订单类型，1：会员
                    "salePrice": 149900, // 原价
                    "realPrice": 149900 // 优惠后真实价钱
                },
                {
                    "shopId": 1,
                    "shopName": "店铺名称",
                    "address": "店铺地址",
                    "subOrderId": 1,
                    "orderType": 1, // 订单类型，1：会员
                    "salePrice": 149900, // 原价
                    "realPrice": 149900 // 优惠后真实价钱
                }
            ],
            "flowOrder": {
                "subOrderNum": 2,
                "realPrice": 500,
                "totalPrice": 1000
            },
            "payUrl": "http://baidu.com.skkks" // 二维码支付链接---新增参数，只有原订单是 二维码支付的时候 & 订单状态是支付中 返回
        }
    ],
    "expand": {},
    "status": 0,
    "errors": []
}|



### 3.14 财务支付完成后回调财B端接口
####     3.14.1 功能逻辑&流程图说明
[流程图]
####     3.14.2 对外接口说明 
|接口地址|外部域名（财务） 线上：http://bmp.baidu-int.com 线下：ip+port 线下环境：http://10.141.194.18:8027/store-b/callback/ucfinance/payOrderSuccessCallback 预上线环境：http://10.96.116.139:5858/store-b/callback/ucfinance/payOrderSuccessCallback 线上环境：http://bmp.baidu-int.com/store-b/callback/ucfinance/payOrderSuccessCallback|备注|
|-|-|-|
|参数|Header：
"appId": "20002"
"sign":"签名"

Data
{
       "uuid":uuid, // uuid
       "orderId":"1001"﻿, // 财务平台侧生成的订单id
       "payOrderId":"1000001" // 实际支付的订单id（百度收银台侧的订单ID）
       "payResultCode":0 // 0表示支付成功 非0 表示支付失败
       "uid":1﻿0001, // ucid
       "product":1 // 1:推广资金池 
       "amount":100 // 金额 = 订单总额， 单位为元，最多两位小数
       "payTime": 1743504804 // 支付时间-时间戳
       "appcode":""，
       "returnData":"{"orderId":"﻿100001﻿"}" // B端订单id       
}|在tb_shop_order 增加两个字段 crm_order_id :crm财务订单id crm_order_data: crm回调json|
|返回 |{
    "data": {
        "uuid": "12345" // uuid
    },
    "expand": {},
    "status": 200,
    "errors": []
}||



### 3.15 获取TP基本信息
####     3.15.1 对外接口说明 
|接口地址|StoreUcService/getBaseUserInfo|备注|
|-|-|-|
|参数|{
}||
|返回 |{
    "data": {
        "userInfo": {
            "userId": 39647483,
            "userName": "本地生活preonline"
        }
    },
    "expand": {},
    "status": 200,
    "errors": []
}||


