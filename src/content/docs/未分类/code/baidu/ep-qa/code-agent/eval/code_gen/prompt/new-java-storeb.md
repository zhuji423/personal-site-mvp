---
title: "new-java-storeb"
description: "你是一名JAVA web开发工程师，你需要基于java SpringBoot以及商业代码库框架，生成满足下列要求的接口代码： 要求： 接口地址：StoreCommonFlowPlanService/queryFlowPlanList 接口入"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\eval\\code_gen\\prompt\\new-java-storeb.md"
---
你是一名JAVA web开发工程师，你需要基于java SpringBoot以及商业代码库框架，生成满足下列要求的接口代码：
## 要求：
```
接口地址：StoreCommonFlowPlanService/queryFlowPlanList
接口入参：
{
     "source": 40
}
返回结构：
{
    "data": {
        "totalNum": 96,
        "list": [
            {
                "id": 100515,
                "mapUcId": "521583830067585024",
                "shopIds": "31383001",
                "name": "梁东新计划-1",
                "planPrice": 10000,
                "shopName": "海底捞(凯德茂分店)",
                "status": 1,
                "usePrice": 0,
                "clickNum": 0,
                "createTime": "2025-03-01 17:23:06",
                "payType": 5,
                "closeType": 9,
                "source": 36,
                "createMode":1, // 计划创建方式 0:用户手动创建, 1:捆绑下单自动生成
            }
        ]
    },
    "expand": {

    },
    "status": 0,
    "errors": [

    ]
}
业务逻辑：
1、从tb_flow_plan_bo中获取没删除的这个userId用户和渠道source的流量宝计划总数，得到的总数赋值给totalNum，若为0则可以直接返回
2、再从tb_flow_plan_bo中获取没删除的此ucid和渠道source的流量宝计划详情
3、计划详情里的shop_ids是以逗号连接的店铺id列表，用逗号分隔后提取出所有shopId，再用shopId列表从tb_shop_info表中查询所有店铺信息
4、将返回结构体所需的字段，从计划详情中提取出来并返回。其中ShopName需要获取该计划的店铺id列表，再从查询大盘的所有店铺信息中获取店铺名称，将店铺名称用（）括起来，如（店铺名称），然后并将所有的店铺名称用"、"组装在一起赋值给ShopName
5、注意校验入参不能为空


表结构：
CREATE TABLE `tb_flow_plan_bo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `uc_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '账号UCID',
  `map_uc_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '地图账号ID',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '名称',
  `shop_ids` text COMMENT '店铺的list，使用逗号分隔',
  `plan_price` bigint(20) NOT NULL DEFAULT '0' COMMENT '计划价格 单位分',
  `pay_type` int(11) NOT NULL DEFAULT '1' COMMENT '支付方式1：资金池支付， 2：免费额度',
  `source` int(11) NOT NULL DEFAULT '-1' COMMENT '流量宝类型 17 教育流量宝； 37 本地流量宝， 36 地图流量宝 40 通投流量宝，用来区分是老的数据刷过来的',
  `old_plan_id` bigint(255) NOT NULL DEFAULT '-1' COMMENT '历史计划id，地图和本地教育通过source区分',
  `status` int(11) NOT NULL DEFAULT '0' COMMENT '流量宝状态 0:开启,1:关闭, 2:待生效',
  `click` bigint(20) NOT NULL DEFAULT '0' COMMENT '点击数',
  `old_click` bigint(20) NOT NULL DEFAULT '0' COMMENT 'old点击数',
  `use_price` bigint(20) NOT NULL DEFAULT '0' COMMENT '消费金额， 单位分',
  `use_price_li` bigint(20) NOT NULL COMMENT '消费金额， 单位厘',
  `old_use_price` bigint(20) NOT NULL DEFAULT '0' COMMENT 'old消费(原计划消费金额)',
  `plan_json` text COMMENT '流量宝信息json',
  `scene_close` int(4) NOT NULL DEFAULT '0' COMMENT '投放端停止信号，0，不停止 1 地图停止， 2 搜索停止',
  `close_type` int(4) NOT NULL DEFAULT '-1' COMMENT '关闭类型：1、消费到达计划金额，2、用户手动关闭 3、资金池余额消耗完',
  `version` bigint(20) NOT NULL DEFAULT '1' COMMENT '乐观锁',
  `is_delete` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否删除 0-未删除,1-已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `scene` int(10) NOT NULL DEFAULT '0' COMMENT '投放端,通投时有效 0:双端 1:搜索 2:地图',
  `new_plan_scene` varchar(20) NOT NULL DEFAULT '0' COMMENT '投放端,逗号分隔 1,2  1:搜索 2:地图, 3:凤巢',
  `plan_type` int(4) NOT NULL DEFAULT '0' COMMENT '计划类型：0：旧计划，1：新通投计划',
  `match_code` bigint(20) NOT NULL DEFAULT '0' COMMENT '冻结资金包'
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idx_uc_id` (`uc_id`),
  KEY `idx_map_uc_id` (`map_uc_id`),
  KEY `idx_old_plan_id` (`old_plan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100085 DEFAULT CHARSET=utf8 COMMENT='流量宝计划表';

CREATE TABLE `tb_shop_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '店铺id',
  `uc_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '商家id',
  `app_id` int(11) NOT NULL DEFAULT '0' COMMENT '垂类id',
  `subapp_id` int(11) NOT NULL DEFAULT '0' COMMENT '分产品id',
  `name` varchar(128) NOT NULL DEFAULT '' COMMENT '店铺名字',
  `logo` varchar(1024) NOT NULL DEFAULT '' COMMENT '店铺logo',
  `backgroud` varchar(1024) NOT NULL DEFAULT '' COMMENT '店铺背景',
  `description` varchar(1024) NOT NULL DEFAULT '' COMMENT '店铺描述',
  `images` varchar(4096) NOT NULL DEFAULT '' COMMENT '店铺轮播图',
  `page_url` varchar(1024) NOT NULL DEFAULT '' COMMENT '线上url',
  `sort_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '排序类型0:按更新时间排序 1销量排序',
  `phone_number` varchar(20) NOT NULL DEFAULT '' COMMENT '电话号',
  `service_phone_number` varchar(20) NOT NULL DEFAULT '' COMMENT '客服电话号',
  `after_sale_phone_number` varchar(20) NOT NULL DEFAULT '' COMMENT '售后电话号',
  `consult_url` varchar(1024) NOT NULL DEFAULT '' COMMENT '在线咨询url',
  `trans_bottom_bar` text COMMENT '底部转化组件',
  `status` int(11) NOT NULL DEFAULT '2' COMMENT '店铺状态 1-已开启 2-未开启 3-豁免 4-整改 5-闭店中 6-已闭店',
  `is_del` int(11) NOT NULL DEFAULT '0' COMMENT '是否删除',
  `reason` varchar(2048) NOT NULL DEFAULT '' COMMENT '拒绝理由',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `is_note_verify` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否开启短信验证，0:关闭 1:开启',
  `is_auth` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否企业认证，0:无认证 1:已认证',
  `evaluate_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '评价类型，0:展示全网评价 1:隐藏全网评价 2:隐藏全网评价及关闭买家评价',
  `extra` mediumtext COMMENT '扩展字段',
  `auth_image` varchar(4096) NOT NULL DEFAULT '' COMMENT '认证图片',
  `auth_time` datetime NOT NULL DEFAULT '2019-01-01 00:00:00' COMMENT '认证时间',
  `open_shop_time` datetime DEFAULT NULL COMMENT '开店时间',
  `program_key` varchar(128) NOT NULL DEFAULT '' COMMENT '小程序key',
  `bulletin` text COMMENT '公告，逗号分割',
  `program_id` varchar(128) NOT NULL DEFAULT '' COMMENT '小程序Id',
  `pass_id` bigint(20) DEFAULT NULL COMMENT 'passId',
  `biz_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '业务id',
  `kv_json` mediumtext COMMENT 'kv_json数据可供检索建立索引',
  `short_name` varchar(20) NOT NULL DEFAULT '' COMMENT '店铺简称',
  `city_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '城市id',
  `province_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '省份id',
  `company_name` varchar(255) NOT NULL DEFAULT '' COMMENT '商户UC账户的公司名称',
  `is_master` int(11) NOT NULL DEFAULT '1' COMMENT '是否主门店 1:是 0:否',
  `relation_biz_id` bigint(20) NOT NULL DEFAULT '-1' COMMENT '父门店id',
  `is_commission` int(11) NOT NULL DEFAULT '0' COMMENT '店铺是否开启分佣',
  `commission_rate` int(11) NOT NULL DEFAULT '0' COMMENT '佣金比例',
  `program_status` int(11) NOT NULL DEFAULT '1' COMMENT '小程序状态: 1 发布, 2 下架',
  `evaluation_switch` int(10) NOT NULL DEFAULT '1' COMMENT '评价开关：1 展示，0 不展示',
  `private_json` mediumtext COMMENT '中台内部字段',
  `commission_rules` text,
  `evaluate_data` text COMMENT '店铺评价json',
  `cop_id` bigint(20) NOT NULL DEFAULT '-1' COMMENT '熊掌id',
  `site_shop_id` bigint(20) NOT NULL DEFAULT '-1' COMMENT '建站店铺id',
  `name_qualify` text COMMENT '店铺名称资质图片，多长用逗号分隔',
  `category_json` text COMMENT '店铺类目json',
  `refuse_field` varchar(128) NOT NULL DEFAULT '' COMMENT '拒绝字段list 1-名称 2-简介 3-logo 4-类目',
  `program_basic_status` int(11) NOT NULL DEFAULT '3' COMMENT '小程序基础信息状态 3-草稿 4-审核中 5-审核失败 6-审核通过 7-强制下线',
  `quality_tag` int(11) NOT NULL DEFAULT '0' COMMENT '品牌店铺标识,1:品牌店铺,0:非品牌店铺',
  `version` int(11) NOT NULL DEFAULT '1' COMMENT '物料版本',
  `logo_qualify` text COMMENT 'logo资质',
  `audit_status` int(10) NOT NULL DEFAULT '3' COMMENT '审核状态 3-草稿 4-审核失败 5-审核中 6-审核通过',
  `rectify_reason` varchar(1024) NOT NULL DEFAULT '' COMMENT '店铺整改原因',
  `page_h5_url` varchar(1024) NOT NULL DEFAULT '' COMMENT '店铺首页h5',
  `source` int(11) NOT NULL DEFAULT '0' COMMENT '来源渠道',
  `sub_name` varchar(255) NOT NULL DEFAULT '' COMMENT '分店名称',
  `door_logo` varchar(1024) NOT NULL DEFAULT '' COMMENT '门脸图片',
  `poi_flag` int(10) NOT NULL DEFAULT '0' COMMENT '是否为poi店铺 0-不是 1-是',
  `member_status` int(10) NOT NULL DEFAULT '0' COMMENT '会员状态 0-未开通 1-已开通',
  `business_check_status` int(10) NOT NULL DEFAULT '0' COMMENT '经营核验状态 0-未核验 1-已核验',
  `opt_id` bigint(10) NOT NULL DEFAULT '0' COMMENT '操作人id',
  `brand` varchar(255) NOT NULL DEFAULT '' COMMENT '品牌',
  `exempt_type` int(10) NOT NULL DEFAULT '-1' COMMENT '免审类型 -1-未接入审核 0-不免审 1-在风控免审白名单内 2-字段无diff',
  `brand_qualify` text COMMENT '品牌资质',
  `test_member_status` int(10) NOT NULL DEFAULT '0' COMMENT '会员状态 0-未开通 1-已开通',
  `tp_id` varchar(255) DEFAULT NULL COMMENT 'tpid',
  `migrate` int(11) DEFAULT NULL COMMENT '是否从线上导下来的数据',
  `flow_shield_flag` tinyint(4) NOT NULL DEFAULT '1' COMMENT '0-流量屏蔽，1-不屏蔽',
  `first_open_time` datetime DEFAULT NULL COMMENT '店铺状态首次变为已开启时间',
  `shop_brand_type` int(11) DEFAULT '0' COMMENT '品牌店铺类型：0-个体工商户 1-普通店 企业店 2-旗舰店 3-专卖店 4-专营店',
  `name_json` varchar(256) DEFAULT '' COMMENT '店铺名称分段存储json',
  `sub_shop_type` int(11) DEFAULT '-1' COMMENT '子店铺类型 1-直营店铺  2-加盟店铺  3-合作店铺',
  `last_modify_time` datetime DEFAULT NULL COMMENT '最后编辑时间',
  `close_source` int(11) DEFAULT '0' COMMENT '闭店来源 0-系统闭店 1-资质巡查闭店',
  `suspend_end_time` datetime DEFAULT NULL COMMENT '店铺歇业截止时间',
  `new_shop_flag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '新店标识,0-非新店,1-新店',
  `online_status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '门店上下架 0 上架  1下架',
  `state_label` varchar(255) NOT NULL DEFAULT '0000000000000000' COMMENT '1-整改 2-保障限制 3-置休 4-释放',
  `sleep_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00' COMMENT '置休时间',
  `mod_flag` smallint(6) NOT NULL DEFAULT '0' COMMENT '修改类型标识，0-单店铺修改，1-批量修改',
  `fission_id` bigint(20) DEFAULT NULL COMMENT '服务商id',
  `audit_type` int(11) NOT NULL DEFAULT '0' COMMENT '0-治理审核 1-风控审核',
  `flag_ship_urls` text COMMENT '旗舰店竞对开店证明材料',
  PRIMARY KEY (`id`),
  KEY `ind_shop_uc` (`uc_id`),
  KEY `ind_shop_passid` (`pass_id`) USING BTREE,
  KEY `idx_appid_bizid` (`app_id`,`biz_id`) COMMENT '业务线biz索引',
  KEY `idx_app_name_master` (`app_id`,`name`,`is_master`),
  KEY `idx_update_time` (`update_time`),
  KEY `idx_flow_shiled` (`flow_shield_flag`,`is_del`,`app_id`,`suspend_end_time`),
  KEY `idx_name` (`app_id`,`subapp_id`,`is_del`,`is_master`,`name`,`sub_name`),
  KEY `index_new_first_del` (`new_shop_flag`,`first_open_time`,`is_del`)
) ENGINE=InnoDB AUTO_INCREMENT=162305360745156 DEFAULT CHARSET=utf8 COMMENT='店铺信息表''
```


## 商业代码库框架
### store-b-api层代码如下：
#### api层使用海若依赖包的类来声明海若接口，接口具体实现在store-b-biz层
api层目录：`store-b-api/src/main/java/com/baidu/pa/storeb/api/${业务场景}/XxxService.java`
示例代码如下：
```java
package com.baidu.pa.storeb.api.${业务场景};

import com.baidu.fengchao.hairuo.meta.annotation.APIMethod;
import com.baidu.fengchao.hairuo.meta.annotation.APIService;
import com.baidu.fengchao.hairuo.meta.model.CommonSingleResponse;
import com.baidu.pa.storeb.PagingResponse;
import com.baidu.pa.storeb.vo.${业务场景}.XxxRequest;
import com.baidu.pa.storeb.vo.${业务场景}.XxxVo;

@APIService(desc = "服务描述")  //@APIService注解定义海若接口服务
public interface XxxService {

    // 普通返回结构体
    @APIMethod(read = true, desc = "接口描述")  //@APIMethod注解定义海若接口，read参数：true表示GET读接口，false表示POST写接口
    CommonSingleResponse<XxxVo> queryCapitalpoolBySource(Long userId, Long optId, XxxRequest request); //userId和optId为必要的默认参数(userId=ucId, optId=代理userid) , XxxRequest为本次请求参数

    // 分页返回结构体, 使用CommonSingleResponse<PagingResponse<T>>进行封装, 返回结构满足{"data": {{"totalNum": 1, "list": []}}}格式的，使用此结构体
    @APIMethod(read = true, desc = "接口描述")
    CommonSingleResponse<PagingResponse<CommonFlowPlanVo>> queryFlowPlanList(Long userId, Long optId, XxxRequest request);
}
```
#### vo层定义海若接口请求类型结构Request、接口返回类型结构VO
vo层目录：`store-b-api/src/main/java/com/baidu/pa/storeb/vo/${业务场景}/`
注意默认需使用@AllArgsConstructor, @NoArgsConstructor, @Builder注解
注意需要先识别本次请求为普通请求还是分页请求，如果返回结构满足{"data": {{"totalNum": 1, "list": []}}}格式的则为分页请求，必须使用分页请求结构体
请求类型结构示例代码如下：XxxRequest.java
```java
package com.baidu.pa.storeb.vo.${业务场景};

import com.baidu.fengchao.hairuo.meta.annotation.APIParam;
import com.baidu.pa.storeb.api.common.PageRequest;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

// 分页请求结构体
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class XxxRequest extends PageRequest {

    @APIParam(desc = "接口入参描述")
    private Long ucId;

}
```
返回类型结构示例代码如下：XxxVo.java
```java
package com.baidu.pa.storeb.vo.${业务场景};

import com.baidu.fengchao.hairuo.meta.annotation.APIParam;
import lombok.Data;

@Data

public class XxxVo {

    @APIParam(desc = "资金池总金额")
    private Long amount;
}
```
### store-b-biz层代码如下：
#### platservice层为store-b-api层接口的具体实现，并会调用handle层方法实现具体业务逻辑。调用链路为store-b-api->store-b-biz下的platservice层->store-b-biz下的handle层
platservice层目录：`store-b-biz/src/main/java/com/baidu/pa/storeb/biz/platservice/${业务场景}/XxxServiceImpl.java`
示例代码如下：
```java
package com.baidu.pa.storeb.biz.platservice.${业务场景};

import com.baidu.cloud.starlight.springcloud.server.annotation.RpcService;
import com.baidu.fengchao.hairuo.meta.model.CommonSingleResponse;
import com.baidu.fengchao.hairuo.meta.model.CommonResponse;
import com.baidu.pa.storeb.biz.service.AbstractRpcService;
import com.baidu.pa.storeb.biz.validator.platservice.${业务场景}.XxxRequestValidator;
import com.baidu.pa.storeb.vo.${业务场景}.XxxRequest;
import com.baidu.pa.storeb.vo.${业务场景}.XxxVo;
import jakarta.annotation.Resource;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RpcService
public class XxxServiceImpl extends AbstractRpcService implements XxxService {

    @Resource
    private XxxHandle xxxHandle;
    // 返回单个对象
    @Override
    public CommonSingleResponse<XxxVo> queryCapitalpoolBySource(
            Long userId, Long optId, XxxRequest request) {
        return super.executeCommonSingle("XxxService", "queryCapitalpool", request,
                new XxxRequestValidator(),
                () -> xxxHandle.queryCapitalpoolBySource(userId, optId, request));
    }
    // 没有返回值
    @Override
    public CommonSingleResponse<Void> syncMidPlatCapitalpool(
            Long userId, Long optId, MidPlatCapitalpoolRequest request) {
        return super.executeCommonSingleNoReturn("XxxService",
                "syncMidPlatCapitalpool", request,
                null,
                (none) -> xxxHandle.syncMidPlatCapitalpool(userId, optId, request));
    }
    // 返回对象数组
     @Override
    public CommonResponse<SiteRegionInfo> getAllRegionInfo(Long userId, Long optId, SitiRegionStoreReq request) {
        return super.executeCommon("XxxService", "getShopIdsByUcId",
                request, null, () -> xxxHandle.getAllRegionInfo(request));
    }
}
```
#### handle层负责实现具体的业务逻辑，包含声明接口、接口实现两部分
##### 声明handle接口
目录：`store-b-biz/src/main/java/com/baidu/pa/storeb/biz/handle/${业务场景}/XxxHandle.java`
示例代码如下：
```java
package com.baidu.pa.storeb.biz.handle.${功能场景};

import com.baidu.pa.storeb.vo.${功能场景}.XxxRequest;
import com.baidu.pa.storeb.vo.${功能场景}.XxxVo;
import java.util.List;

public interface XxxHandle {

    XxxVo queryCapitalpoolBySource(Long ucId, Long optId, XxxRequest request);

}
```
服务返回类型若为复杂结构体，则定义在vo层，禁止使用Object类型
##### HandleImpl接口实现
HandleImpl层目录：`store-b-biz/src/main/java/com/baidu/pa/storeb/biz/handle/${业务场景}/impl/`中放置服务实现XxxHandleImpl.java文件，是对应XxxHandle.java中方法声明的具体实现
示例代码如下：
```java
package com.baidu.pa.storeb.biz.handle.${功能场景}.impl;

import com.baidu.pa.storeb.dal.dao.${功能场景}.XxxDao;
import com.baidu.pa.storeb.dal.dto.XxxDto;
import com.baidu.pa.storeb.sal.${第三方服务}.XxxThirdService;
import com.baidu.pa.storeb.sal.${第三方服务}.model.XxxReq;
import com.baidu.pa.storeb.sal.${第三方服务}.model.xxxResp;

@Service
@Slf4j
public class XxxHandleImpl implements XxxHandle {
    @Resource
    private XxxDao xxxDao;
    @Resource
    private XxxThirdService xxxThirdService;
    
    @Override
    public XxxVo queryCapitalpoolBySource(Long ucId, Long optId, XxxRequest request) {
        log.info("CapitalPoolHandleImpl.queryCapitalPool request = {}", JsonUtils.toJson(request));

        // 与数据库交互需要调用Dao层代码, 禁止在biz层直接与db进行交互
        XxxDto xxxDto = xxxDao.queryFlowCapitalPoolByUcId(ucId);

        // 第三方服务交互需要调用sal层代码, 禁止在biz层直接调用第三方服务
        XxxReq req = new XxxReq();
        XxxResp xxxResponse = xxxThirdService.addAlbum(req)
        XxxVo xxxVo = queryCapitalpool(xxxDto, xxxResponse)
        log.info("CapitalPoolHandleImpl.queryCapitalPool end, ucId = {}",  request.getUcId());
        return vo;
    }
 }
```
#### vo层定义业务逻辑处理中涉及到的各种类型定义
vo层目录：`store-b-biz/src/main/java/com/baidu/pa/storeb/biz/vo/${功能场景}/XxxVo.java`
示例代码如下：
```java
package com.baidu.pa.storeb.biz.vo.${功能场景};
import lombok.Data;

@Data
public class XxxVo {

    private Integer msgType;
  }
```
#### utils层存放业务逻辑处理过程中的工具方法
utils层目录：`store-b-biz/src/main/java/com/baidu/pa/storeb/biz/utils/XxxUtils.java`

#### validator层为校验层，存放入参、权限、数据校验等方法
validator层目录：`store-b-biz/src/main/java/com/baidu/pa/storeb/biz/validator/${功能场景}/XxxValidator.java`

#### enums层存放业务逻辑处理中涉及到的枚举值
enums层目录：`store-b-biz/src/main/java/com/baidu/pa/storeb/biz/enums/XxxEnum.java`

#### config层定义业务逻辑处理中涉及到的配置类
config层目录：`store-b-biz/src/main/java/com/baidu/pa/storeb/biz/config/XxxConfig.java`
示例代码如下：
```java
package com.baidu.pa.storeb.biz.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Data
@Component
@ConfigurationProperties(prefix = "businesscheck")
public class BusinesscheckConfiguration {
    private Integer closeOrderDelayDays;
    private Integer creditVerifyActiveDay;
}
```
### store-b-common层代码如下：
store-b-common层存放公共方法（包含项目中通用的工具类、异常处理方法、枚举值、常量等），可被各层级调用
目录：`store-b-common/src/main/java/com/baidu/pa/storeb/common/`，除了constants、enums、utils，其他的可直接放到此路径下
#### constants层存放通用的常量
constants层目录：`store-b-common/src/main/java/com/baidu/pa/storeb/common/constants/`
#### enums层存放通用的枚举
enums层目录：`store-b-common/src/main/java/com/baidu/pa/storeb/common/enums/`
#### utils层存放通用的工具类
utils层目录：`store-b-common/src/main/java/com/baidu/pa/storeb/common/utils/`
### store-b-dal层代码如下：
store-b-dal层为数据访问层，负责与数据库交互。实现上分为三步：dao-> Mapper-> Mapper XML文件, 数据库操作需使用mybatis xml配置方式实现。数据库表对应的实体类、Mapper 接口以及XML文件的写法需要才用MyBatis Generator生成的代码格式来实现
#### dao层
层目录：`store-b-dal/src/main/java/com/baidu/pa/storeb/dal/dao/${业务场景}/XxxDao.java`
示例代码如下：
```java

package com.baidu.pa.storeb.dal.dao.${业务场景};

import com.baidu.pa.storeb.common.Constants;
import com.baidu.pa.storeb.dal.model.${业务场景}.TableName;
import com.baidu.pa.storeb.dal.model.${业务场景}.TableNameExample;
import jakarta.annotation.Resource;
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.compress.utils.Lists;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class XxxDao {
    @Resource
    private XxxMapper xxxMapper;

    public List<TableName> queryFlowCapitalPoolByUcId(Long ucId) {
        TableNameExample example = new TableNameExample();
        example.createCriteria().andUcIdEqualTo(ucId)
                .andIsDeleteEqualTo(Constants.DELETE_NO);
        List<TableName> xxxList = xxxMapper.selectByExample(example);
        return CollectionUtils.isEmpty(xxxList) ? Lists.newArrayList() : xxxList;
    }
 }
```

#### Mapper接口层
层目录：`store-b-dal/src/main/java/com/baidu/pa/storeb/dal/dao/${业务场景}/XxxMapper.java`
示例代码如下：
```java
package com.baidu.pa.storeb.dal.dao.${业务场景};
import com.baidu.pa.storeb.dal.model.${业务场景}.TableName;
import com.baidu.pa.storeb.dal.model.${业务场景}.TableNameExample;
import java.util.List;

public interface XxxMapper {
    List<TableName> selectByExample(TableNameExample example);
}

```

#### Mapper XML
Mapper XML层目录：`store-b-dal/src/main/resources/mapper/XxxMapper.xml`
示例代码如下：
```java
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.baidu.pa.storeb.dal.dao.${业务场景}.XxxMapper">
  <resultMap id="BaseResultMap" type="com.baidu.pa.storeb.dal.model.${业务场景}.TableName">
    <id column="id" jdbcType="BIGINT" property="id" />
    <result column="uc_id" jdbcType="BIGINT" property="ucId" />
  </resultMap>
  <select id="selectByExample" parameterType="com.baidu.pa.storeb.dal.model.${业务场景}.TableNameExample" resultMap="BaseResultMap">
    select
    <if test="distinct">
      distinct
    </if>
    <include refid="Base_Column_List" />
    from tb_flow_capital_pool
    <if test="_parameter != null">
      <include refid="Example_Where_Clause" />
    </if>
    <if test="orderByClause != null">
      order by ${orderByClause}
    </if>
  </select>
</mapper>

```

#### model层
##### TableName类
存放mysql数据库表结构，TableName的成员变量与数据表的字段一一对应
目录：`store-b-dal/src/main/java/com/baidu/pa/storeb/dal/model/${业务场景}/TableName.java`
示例代码如下：
```java
package com.baidu.pa.storeb.dal.model.${业务场景};

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;

public class TableName implements Serializable {

    /**
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column tb_flow_capital_pool.id
     *
     * @mbg.generated
     */
    private Long id;

    private Long ucId;
    
    private Integer isDelete;

}
```

##### TableNameExample类
遵循MyBatis Generator生成格式，用于构建动态 SQL 查询条件，提供了一种面向对象的方式来生成复杂的查询条件。
注意：一定要完整生成TableNameExample，不要忽略这部分的代码
目录：`store-b-dal/src/main/java/com/baidu/pa/storeb/dal/model/${业务场景}/TableNameExample.java`
示例代码如下：
```java
package com.baidu.pa.storeb.dal.model.${业务场景};

import java.util.ArrayList;
import java.util.List;

public class TableNameExample {

    /**
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database table tb_flow_capital_pool
     *
     * @mbg.generated
     */
    protected List<Criteria> oredCriteria;

    public TableNameExample() {
        oredCriteria = new ArrayList<Criteria>();
    }

    public Criteria createCriteria() {
        Criteria criteria = createCriteriaInternal();
        if (oredCriteria.size() == 0) {
            oredCriteria.add(criteria);
        }
        return criteria;
    }

    protected Criteria createCriteriaInternal() {
        Criteria criteria = new Criteria();
        return criteria;
    }
    

    protected abstract static class GeneratedCriteria {
        protected List<Criterion> criteria;

        protected void addCriterion(String condition) {
            if (condition == null) {
                throw new RuntimeException("Value for condition cannot be null");
            }
            criteria.add(new Criterion(condition));
        }

        protected void addCriterion(String condition, Object value, String property) {
            if (value == null) {
                throw new RuntimeException("Value for " + property + " cannot be null");
            }
            criteria.add(new Criterion(condition, value));
        }
        protected void addCriterion(String condition, Object value1, Object value2, String property) {
            if (value1 == null || value2 == null) {
                throw new RuntimeException("Between values for " + property + " cannot be null");
            }
            criteria.add(new Criterion(condition, value1, value2));
        }
        public Criteria andUcIdEqualTo(Long value) {
            addCriterion("uc_id =", value, "ucId");
            return (Criteria) this;
        }
        public Criteria andUcIdNotEqualTo(Long value) {
            addCriterion("uc_id <>", value, "ucId");
            return (Criteria) this;
        }
        public Criteria andIsDeleteEqualTo(Integer value) {
            addCriterion("is_delete =", value, "isDelete");
            return (Criteria) this;
        }
    }
    
    public static class Criteria extends GeneratedCriteria {

        protected Criteria() {
            super();
        }
    }

    public static class Criterion {
        private String condition;

        private Object value;

        private Object secondValue;

        private boolean noValue;

        private boolean singleValue;

        private boolean betweenValue;

        private boolean listValue;

        private String typeHandler;

        public String getCondition() {
            return condition;
        }

        public Object getValue() {
            return value;
        }

        public Object getSecondValue() {
            return secondValue;
        }

        public boolean isNoValue() {
            return noValue;
        }

        public boolean isSingleValue() {
            return singleValue;
        }

        public boolean isBetweenValue() {
            return betweenValue;
        }

        public boolean isListValue() {
            return listValue;
        }

        public String getTypeHandler() {
            return typeHandler;
        }

        protected Criterion(String condition) {
            super();
            this.condition = condition;
            this.typeHandler = null;
            this.noValue = true;
        }

        protected Criterion(String condition, Object value, String typeHandler) {
            super();
            this.condition = condition;
            this.value = value;
            this.typeHandler = typeHandler;
            if (value instanceof List<?>) {
                this.listValue = true;
            } else {
                this.singleValue = true;
            }
        }

        protected Criterion(String condition, Object value) {
            this(condition, value, null);
        }

        protected Criterion(String condition, Object value, Object secondValue, String typeHandler) {
            super();
            this.condition = condition;
            this.value = value;
            this.secondValue = secondValue;
            this.typeHandler = typeHandler;
            this.betweenValue = true;
        }

        protected Criterion(String condition, Object value, Object secondValue) {
            this(condition, value, secondValue, null);
        }
    }
}
```

#### dto层
存放*DTO数据，将获取到数据库表的数据进行处理与封装，然后传递给业务逻辑层
层目录：`store-b-dal/src/main/java/com/baidu/pa/storeb/dal/dto/XxxDto.java`
示例代码如下：
```java
package com.baidu.pa.storeb.dal.dto;

import lombok.Data;

@Data
public class AdLogCheatDto {
    private Integer source;
    private String baiduid;
    private String ip;
}
```

当前代码库路径：`icode.baidu.com/baidu/pa/store-b`

gdp框架的项目结构：
|-- pom.xml
|-- store-b-api  //定义海若接口,海若接口入口层
|   |-- pom.xml
|   |-- src
|   |   |-- main
|   |       |-- java
|   |           |-- com
|   |               |-- baidu
|   |                   |-- pa
|   |                       |-- storeb
|   |                           |-- api  //定义海若接口
|   |                           |   |-- ${业务场景}           //业务场景
|   |                           |   |   |-- XxxService.java
|   |                           |-- vo   //VO层,定义海若接口请求参数Request、返回结构
|   |                               |-- platapi             
|   |                               |   |-- ${业务场景}        //地址
|   |                               |   |   |-- XxxRequest.java  //接口请求参数
|   |                               |   |   |-- XxxVo.java       //接口返回结构
|-- store-b-biz  //业务逻辑处理层
|   |-- pom.xml
|   |-- src
|   |   |-- main
|   |       |-- java
|   |       |   |-- com
|   |       |       |-- baidu
|   |       |           |-- pa
|   |       |               |-- storeb
|   |       |                   |-- biz
|   |       |                       |-- platservice   //store-b-api和store-b-app层接口的实现层
|   |       |                       |   |-- ${业务场景}
|   |       |                       |   |   |-- XxxServiceImpl.java //api和app层接口的实现,会调用handle层方法实现具体业务逻辑
|   |       |                       |-- handle     //业务逻辑实际处理层
|   |       |                       |   |-- ${功能场景}
|   |       |                       |   |   |-- XxxHandle.java  //handle层接口定义
|   |       |                       |   |   |-- impl            //handle层接口的实现层
|   |       |                       |   |   |   |-- XxxHandleImpl.java
|   |       |                       |-- utils     //工具方法
|   |       |                       |   |-- XxxUtils.java
|   |       |                       |-- validator //校验方法，如权限校验、数据校验
|   |       |                       |-- enums    //业务逻辑处理中涉及到的枚举值
|   |       |                       |-- vo        //VO层
|   |       |                       |   |-- ${功能场景}
|   |       |                       |   |   |-- XxxVo.java  //定义业务逻辑处理中涉及到的实体
|   |       |-- resources
|   |           |-- file   //存放静态文件,如txt/xlsx
|-- store-b-common  //公共方法层，可被各层级调用
|   |-- pom.xml
|   |-- src
|   |   |-- main
|   |       |-- java
|   |       |   |-- com
|   |       |       |-- baidu
|   |       |           |-- pa
|   |       |               |-- storeb
|   |       |                   |-- common //包含项目中通用的工具类、常量、通用配置、异常处理等
|   |       |                       |-- constants  //常量
|   |       |                       |-- enums      //枚举
|   |       |                       |-- utils      //工具方法
|-- store-b-dal     //数据访问层，与数据库交互
|   |-- pom.xml
|   |-- src
|   |   |-- main
|   |       |-- java
|   |       |   |-- com
|   |       |       |-- baidu
|   |       |           |-- pa
|   |       |               |-- storeb
|   |       |                   |-- dal
|   |       |                       |-- dao     //数据访问对象层
|   |       |                       |   |-- ${功能场景} 
|   |       |                       |   |   |-- XxxDao.java      //Dao负责业务逻辑和数据访问逻辑的封装，调用Mapper层完成数据库操作
|   |       |                       |   |   |-- XxxMapper.java   //定义Mapper层接口
|   |       |                       |-- dto      //DTO层,定义与业务逻辑处理层相互进行数据传输的对象
|   |       |                       |   |-- XxxDto.java
|   |       |                       |-- model    //Model层,存放MySQL数据库表结构，类的成员变量一一映射到数据库表的列
|   |       |                       |   |-- ${功能场景}    
|   |       |                       |   |   |-- TableName.java   //数据表名命名
|   |       |-- resources
|   |           |-- mapper
|   |               |-- XxxMapper.xml    //Mapper XML文件,与Mapper层接口相对应,Sql的具体实现
|-- store-b-sal     //SAO层,调用第三方服务
|   |-- pom.xml
|   |-- src
|   |   |-- main
|   |       |-- java
|   |       |   |-- com
|   |       |       |-- baidu
|   |       |           |-- pa
|   |       |               |-- storeb
|   |       |                   |-- sal
|   |       |                       |-- AbstractHttpService.java
|   |       |                       |-- AbstractStarlightService.java
|   |       |                       |-- ${第三方服务}
|   |       |                       |   |-- XxxService.java    //定义与第三方服务交互的接口方法
|   |       |                       |   |-- impl
|   |       |                       |   |   |-- XxxServiceImpl.java   //与第三方服务交互接口的具体实现
|   |       |                       |   |-- model  //定义请求第三方服务时的数据传输对象
|   |       |                       |   |   |-- XxxRequest.java   //定义请求参数
|   |       |                       |   |   |-- XxxVo.java        //定义响应结构/其他数据传输对象
|   |       |                       |   |-- enums  //定义请求第三方服务时的枚举值
|   |       |                       |   |   |-- Enum.java
|   |       |                       |-- config        //请求第三方服务配置类
|   |       |                       |   |-- ${第三方服务} 
|   |       |                       |   |   |-- XxxConfiguration.java  //配置类,用于加载和管理与第三方服务的配置信息
|   |       |                       |   |   |-- XxxRestConfiguration.java  //配置类,用于创建和配置与第三方服务交互的RestTemplate实例
|   |       |                       |   |-- CommonConfiguration.java
|   |       |                       |   |-- CommonHttpRequestRetryStrategy.java
|   |       |                       |   |-- CommonRestConfiguration.java
|   |       |                       |   |-- CommonRestTemplate.java

## 生成步骤：
1、 分析需求,并输出该需求对应的业务场景
### 业务场景列表：
activity            //活动相关接口
amis                //amis
bce                 //bos服务
billingsystem       //计费系统
callback            //回调服务
capitalpool         //资金池
commission          //佣金
crawl               //爬虫抓取
decorate            //装修
flow                //流量宝
gd                  //高德
leads               //线索
member              //会员
order               //订单
product             //商品
score               //分数服务（店铺、商品分）
shop                //店铺
other               //未识别出以上业务场景

2、用上一步骤中分析出来的业务场景替换${业务场景}，用于确定文件路径
3、分析需求,并输出该需求对应的功能场景
### 功能场景列表：
ai               //ai
account         //账户
activity        //活动
ad              //广告
address         //地址
article         //内容
audit           //审核
bce             //bos
billingsystem   //计费系统
capitalpool     //资金池
check           //经营核验
compile         //产品/商品/店铺编译
content         //内容
crawl           //爬虫抓取
decorate        //装修
dowload         //下载
flow            //流量宝
gd              //高德
guarantee       //保障服务
leads           //线索
member          //会员
order           //订单
pass            //pass账户相关
product         //商品
score           //分数
sendmessage     //发送短信
settlement      //入驻
shop            //店铺
stock           //库存
tablecontent    //表格内容
tp              //tp代理商
vcr             //vcr
quoteprice      //报价
prompt          //prompt
other           //未识别出以上业务功能

4、用上一步骤中分析出来的业务场景替换${功能场景}，用于确定文件路径
5、分析需求,并输出该需求对应的功能场景
6、生成代码
7、注意校验入参是否为空

## 生成要求：
1、严格按照上述需求生成，请勿自由发挥
2、给出生成的代码，以及文件路径
3、必须写全所有代码，确保生成的代码是完整的、可运行的。禁止省略代码，也禁止生成包含假设方法或未实现的逻辑，禁止生成有遗留TODO的代码
4、除api层和app层之外的每个函数均需要完整函数注释（注释包括函数功能，参数类型含义，返回值类型含义），如：
/**
* 功能描述（一句话概括，采用中文）
*
* @param 变量名 类型 含义
* @return 返回类型 含义
*/

### 输出格式：每个文件给出完整路径与代码
文件名：`具体文件路径`
```java
// todo
```
文件名：`具体文件路径`
```java
// todo
```
其中todo和具体文件路径需要替换成自己的, 具体文件路径只需给出相对路径。除代码与文件路径外，无需给出其他说明。
