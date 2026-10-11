---
title: "拆分初始样本数据"
description: "sparse特征： 特点：数据集中，大部分值为零的特征，特征值分布稀疏，如用户的性别（男/女），商品的品牌和类目，以及其他id类特征； 举例：用户历史点击过的商品（特征：商品id）对当前搜索结果排序的影响。"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\奇怪的知识增加了_引用文档\\ctr流程串讲.md"
---
ctr流程串讲

## 场景
|**搜索结果页（1*4）**|**比价详情页**|**搜索结果页（3*2）**|**搜索结果页（1*3）**|
|-|-|-|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|

## 流程图
[流程图]
## 特征
[特征梳理和规划 20241210](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/iTTERk-uXa/WGwrTOcfH88DMG?t=mention&mt=doc&dt=doc)

### 特征列表
**特征类别：**

* **sparse特征：**
    * **特点**：数据集中，大部分值为零的特征，特征值分布稀疏，如用户的性别（男/女），商品的品牌和类目，以及其他id类特征；
    * **举例：**用户历史点击过的商品（特征：商品id）对当前搜索结果排序的影响。

* **dense特征：**
    * **特点：**数据集中，特征值分布一般均匀连续，如商品价格，商品销量等
    * **举例：**价格（特征：商品价格）对搜索结果排序的影响。


#### 用户特征（user feature）
* **sparse特征：**local_city（城市编码）、local_province（省份）、hometown_city（故乡城市编码）、marriage（婚姻状态）、income（收入状态）、device（设备信息）、app_list（应用列表）、age（年龄）、gender（性别）、last7d_clk_spu（最近7天点击的商品）、last7d_clk_keyword（最近7天点击的关键词）、last7d_clk_spu_cate1（最近7天点击的一级类目）、last7d_clk_spu_cate2（最近7天点击的耳机类目）、last7d_clk_spu_brand（最近7天点击的品牌）等
* **dense特征：**avg_price（平均消费价格）、clk_max_price（点击最高价格）、clk_min_price（点击最低价格）等

#### 搜索词特征（query feature）
* **sparse特征：**norm_query（搜索词）、query_prd_cate_1_name（query对应商品一级类目名称）、query_prd_cate_2_name（query对应商品二级类目名称）、query_prd_brand_name（搜索词品牌名）、query_prd_name（搜索词指向的产品词）、query_gender（搜索词性别）等
* **dense特征：**click_avg_price（query平均点击的价格）、expose_avg_price（query平均曝光价格）、gender_weight（query性别权重）等

#### 商品特征（item feature）
* **sparse特征：**id（商品id）、title（商品标题）、brand_name（商品品牌名）、cate_1_name（一级品类名）、cate_1_id（一级品类id）、keywords（商品关键词）、params（商品参数）、sku_id（默认sku_id）、pic_embed（首图向量）等
* **dense特征：**price（商品价格）、sales_volume（销量）、imp\clk\ctr_3\7\30d（3\7\30天曝光数\点击数\点击率）、price_diff_1\3\7\30d（1\3\7\30价格变化）、hot_ratio_1\3\7\30d（1\3\7\30d热度变化）

#### 交叉特征（cross feature）
* **sparse特征：**
    * query*spu：cross_query_product_spu_title、cross_query_brand_spu_brand、cross_query_cate_spu_cate_1、cross_query_cate_spu_cate_2
    * user*spu：cross_user_gender_spu_spuid、cross_user_age_spu_spuid、cross_user_local_province_spu_spuid、cross_user_hometown_province_spu_spuid、cross_user_perfession_spu_spuid、cross_user_consumption_level_spu_spuid、cross_user_lifestage_spu_spuid、cross_user_educational_spu_spuid、cross_user_assets_spu_spuid、cross_user_marriage_spu_spuid、、cross_user_economic_class_spu_spuid、cross_user_industry_spu_spuid

* **dense特征**：暂无

#### 交叉特征（context feature）
* **卡片位置、展示样式**

### 特征获取
#### offline（离线特征计算）
[流程图]
**代码库：**[文件页：baidu/good-search/good-search-offline-new  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/good-search/good-search-offline-new/tree/master/price_compare/goods_rank_model/mrjob?t=mention&mt=doc&dt=sdk)

##### 流程介绍：
**目前bijia模型所有的离线特征产出任务都是基于mr**

*这里以用户的统计特征为例，介绍从如何从初始样本生成的用户唯独的统计特征并存入undb，并部署例行化任务*



* **初始样本：**由数据同学产出，主要任务是将线上的**dump**日志和客户端所记录的真实用户行为的**打点**日志进行join，产出带有label的初始样本数据
    * **dump：**一次请求中对真实送入模型的各个特征值进行记录
    * **打点：**记录结果页展示的卡片信息和商品信息同时也记录用户对卡片和商品所进行的各类行为

* **初始样本结构：**通过"\t"将下述字段按顺序进行连接

**is_clk,search_id,uid,cuid,baiduid,normalized_query,spuid,usr_attr,usr_group,usr_consume_intent,usr_asset,usr_age,usr_consume_level,usr_gender,usr_profession,usr_interest,usr_cate_consume_level,usr_app_list,usr_lifestage,usr_hometown_province,usr_local_province,usr_hometown_city,usr_industry,usr_local_city,us_ebtiny_input,usr_edu,usr_marriage,usr_economic_class,qry_ebtiny_input,qry_qp,spu_title,spu_brand_name,spu_brand_id,spu_sh_cate_1_name,spu_sh_cate_1_id,spu_sh_cate_2_name,spu_sh_cate_2_id,spu_price,spu_hot,spu_sh_appraise_num,spu_sales_volume,spu_sh_category_tag_list,spu_sh_keywords,spu_sh_params,spu_imp_3d,spu_imp_7d,spu_imp_30d,spu_clk_3d,spu_clk_7d,spu_clk_30d,spu_ctr_3d,spu_ctr_7d,spu_ctr_30d,is_expo,ctr_score,final_score,sid_list,clk_area,clk_type,is_baiduapp,mobile_browser_id,spu_satisfaction_score**

**用户统计特征计算任务**

* **mr任务路径：**good-search-offline-new/price_compare/goods_rank_model/mrjob/**mr_fea_step1_usr_stat_v1.sh**
* **任务输入路径：**afs://wuge.afs.baidu.com:9902/user/ec_user_alg_data/warehouse/esearch/dwd/search_dwd_price_disp_clk_dump_di/event_day={event_day}/
* **任务输出路径：**afs://wuge.afs.baidu.com:9902/user/sasd-goods/goods-search/wanghe25/bijia/train_data/20241231/step1_usr_stat_v1
* **任务目标：**获取usr_avg_price，usr_min_price，usr_max_price，usr_last7d_clk_spu，usr_last7d_clk_keywords，usr_last7d_clk_brand，usr_last7d_clk_cate1，usr_last7d_clk_cate2
* **任务流程：**
    * **map：**对数据进行解析，提取需要的部分，用于reduce计算


```
def parser(line, date_type):
    """
    line:      一条初始样本数据
    date_type: 样本产出的时间和任务时间相隔的天数
    """
    # 拆分初始样本数据
    line = line.strip("\n").split("\t")
    # 校验数据格式
    if len(line) != 62:
        return
   
    is_click = line[0]
    
    # 统计值都依赖用户点击后的信息，无点击行为的样本过滤
    if is_click == "0":
        return

    # 基于初始样本结果获取所需值
    uid = line[2]
    spu_id = line[6]
    price = line[37]
    spu_keywords = line[42]
    spu_brand_id = line[32]
    spu_cate_1_id = line[34]
    spu_cate_2_id = line[36]
    
    # 输出给reduce
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(uid, spu_id, price, spu_keywords, spu_brand_id, spu_cate_1_id, spu_cate_2_id, date_type))
```
    * **reduce：**

```
# 根据用户id进行group
for key, group in groupby(fromstdin(), lambda x:x[0]):
        fea_dict = dict()
        
        uid = key
        
        # 设置默认值
        user_max_price, user_min_price, user_sum_price, user_avg_price = 0, 1e10, 0, 0 
        click_price_cnt = 0        
        click_spu, click_keywords, click_cate_1, click_cate_2, click_brand = dict(), dict(), dict(), dict(), dict()

        for (_, fea_line) in group:
            value_list = fea_line.strip("\n").split("\t")
            
            # 解析map的结果
            spu_id = value_list[0]
            price = value_list[1]
            spu_keywords = value_list[2]
            spu_brand_id = str(value_list[3])
            spu_cate_1_id = str(value_list[4])
            spu_cate_2_id = str(value_list[5])
            date_type = value_list[6]
            
            # 记录用户点击行为的最大、最小、总商品价格
            if is_number(price):
                user_max_price = max(float(price), user_max_price)
                user_min_price = min(float(price), user_min_price)
                user_sum_price += float(price)
                click_price_cnt += 1
            
            # 下述剩余特征计算需要统计7天内的行为
            if date_type != "7d":
                continue
            
            # 统计用户点击的商品id
            click_spu[spu_id] = click_spu.get(spu_id, 0) + 1
            
            # 统计用户点击过的商品关键词
            spu_keyword_list = spu_keywords.split(";")
            for keyword in spu_keyword_list:
                click_keywords[keyword] = click_keywords.get(keyword, 0) + 1
            
            # 统计用户点击过的商品品牌id
            click_brand[spu_brand_id] = click_brand.get(spu_brand_id, 0) + 1

            # 统计用户点击过的商品一级类目id
            click_cate_1[spu_cate_1_id] = click_cate_1.get(spu_cate_1_id, 0) + 1
            
            # 统计用户点击过的商品二级类目id
            click_cate_2[spu_cate_2_id] = click_cate_2.get(spu_cate_2_id, 0) + 1
            
...
```
* **例行化部署：**
    * ejob平台部署每日例行化特征任务产出
    * ejob平台部署每日例行化特征从hdfs同步至undb


#### 在线特征dump
##### **baise介绍**
Baise（百色）是搜索中台的检索系统，包含：vs-rank、vs-bs、vs-build等模块。

**模块介绍：**

* **vs-rank**：一般承担请求侧的解析、召回请求的构建以及返回结果的精排功能，分为vs-root和vs-node，其中node用于做计算的并行化；vs-rank为无状态模块，所有需要的信息都来自于外部；
* **vs-bs**：承担召回和粗排的功能；vs-bs上存储了倒排、向量、属性等数据；其中找回手段包含ANN向量索引和INDEX倒排索引
* **vs-build**：承担包括文档解析在内的建库功能，负责将商品的数据转换为检索系统使用的数据，

**关键配置：**

* **检索插件：**用于编排策略插件算子的执行顺序和拓扑；
* **策略插件：**即策略算子，每个插件一般代表单一的功能单元，比如打散、统计、算分、召回这些功能；
* **架构组件：**为策略算子提供基础功能，比如rpc调用等，为策略屏蔽底层服务和介质；
* **建库配置：**用于设置构建vs-build中商品正排信息建库的策略和搜索索引库的构建策略

##### baise开发
baise开发平台：[https://vs.baidu-int.com/baise/index](https://vs.baidu-int.com/baise/index)

![](/personal-site-mvp/img/doc-placeholder.svg "")


*这里以新增商品特征和用户特征为例*

* **vs-build（新增商品特征）：**
    * **spu正排字段更新：**
        * 策略修改-建库逻辑**：**
            * 路径**：**vs-build**/**strategies/build_spu/default_build_forward_strategy/build_spu_build_forward.conf




```
[@forward_info]
    ### 资源名  数据来源
    [.resource_name]
        field_key: "spu"
    ### 表名    数据来源
    [.schema]
        field_key: "spu_info"
    ### 唯一标识
    [.identifier]
        field_key: "@id"
        field_type: item_string_factor
    ### 版本
    [.label]
        field_key: ""
    ### 数据包类型
    [.message_type]
        field_key: "message_type"
        field_type: attribute_map
        default_value: "ADD"
    ### 正排字段列表
    [.@forward]
        ### 正排类型：
        ###      1. textrel-相关性正排，会对原文进行切词，然后将切词后的结果建立正排，数据包含切词term、tern权重、offset信息；
        ###      2. oritext-原文正排；
        type: textrel
        ### 字段数据类型
        text_type: STRING
        [..value]
            ### 字段key
            field_key: "name_textrel_wordseg"
            ### 字段类型
            field_type: item_string_factor
            ### 默认值
            default_value: ""
        ### 正排目标名
        [..name]
            field_key: "name_textrel"
        ### 字段权重
        [..weight]
            field_key: 1
    
    ......
    ### 新增正排字段示例：
    [.@forward]
        ### 正排字段类型是原文本
        type: oritext
        [..value]
            ### 数据字段key是feature下的spu_pic_embed
            field_key: "feature#spu_pic_embed"
            ### 数据字段类型是string
            field_type: item_string_factor
            ### 没有数据的默认是为0
            default_value: "0"
        [..name]
            ### 正排目标名称
            field_key: "spu_pic_embed"

```
        * 建库主流程：
            * 路径**：**vs-build/tables/build_spu


```
[handler_info]
    handler_so_file: "./so/handlers/liball_default_handlers.so"
    handler_class_name: "DefaultBuildHandler"
    handler_name: "build_spu"
[strategies]
    [.build]
        [..@strategies]
            name: build_spu_preprocess
        [..@strategies]
            name: build_spu_text_process
        [..@strategies]
            name: build_spu_da_service
        [..@strategies]
            name: build_spu_preprocess_text
        [..@strategies]
            name: build_spu_predictor
        [..@strategies]
            name: build_spu_predictor_exp1
        [..@strategies]
            name: build_spu_scoring_vector_norm
        [..@strategies]
            name: build_spu_build_index
        [..@strategies]
            name: build_spu_build_ann
        [..@strategies]
            name: build_spu_build_forward
        [..@strategies]
            name: build_spu_build_digest
        [..@strategies]
            name: build_spu_logwriter

```
        * 构建正排输入数据示例：

```
{
    "@id": "shv2_0de5f51a946ac0e309d38c5d887502e6",
    "category_tag_list": null,
    "classify": [

    ],
    "classify_id": [

    ],
    "default_sku_price": "129",
    "extract_name": "",
    "hot": [
        {
            "@value": 334
        }
    ],
    "loc": "shv2_0de5f51a946ac0e309d38c5d887502e6",
    "name": "五粮液 五粮醇 畅享版 白酒 50度浓香型",
    "new_goods_sale_bookable": [
        {
            "@value": 0
        }
    ],
    "new_goods_sale_timestamp": null,
    "params": [
        {
            "@value": {
                "key": "酒精度",
                "value": "50度"
            }
        },
        {
            "@value": {
                "key": "生产原料",
                "value": "高粱,糯米,大米,小麦,玉米"
            }
        },
        {
            "@value": {
                "key": "香型",
                "value": "浓香型"
            }
        },
        {
            "@value": {
                "key": "包装方式",
                "value": "盒装,瓶装"
            }
        },
        {
            "@value": {
                "key": "适用场景",
                "value": "婚礼喜宴,团圆小酌,自斟自饮"
            }
        },
        {
            "@value": {
                "key": "生产地区",
                "value": "四川省宜宾市"
            }
        }
    ],
    "price": [
        {
            "@value": "129"
        }
    ],
    "qp_brand": "五粮液",
    "qp_category": [
        "酒类@中外名酒@白酒"
    ],
    "qp_category_id": [
        "12259@12260@9435",
        "9987@653@655",
        "12259@14718@15603",
        "1320@1581@12217",
        "1320@1584@13790"
    ],
    "qp_product": "白酒",
    "sales_volume": null,
    "sh_appraise_num": [
        {
            "@value": 0
        }
    ],
    "sh_brand_name": [
        {
            "@value": {
                "level1": "五粮液",
                "level1_id": 5158,
                "level2": "五粮醇",
                "level2_id": 5205
            }
        }
    ],
    "sh_category_name": [
        {
            "@value": {
                "level1": "酒类",
                "level1_id": 495,
                "level2": "白酒/调香白酒",
                "level2_id": 496
            }
        }
    ],
    "sh_default_sku": [
        {
            "@value": "五粮液 五粮醇 畅享版 白酒 50度浓香型 500ml 2瓶"
        }
    ],
    "sh_keywords": [
        {
            "@value": "五粮液"
        },
        {
            "@value": "白酒"
        },
        {
            "@value": "调香白酒"
        },
        {
            "@value": "五粮液3"
        }
    ],
    "feature": {
        "spu_price_diff_1d": 1,
        "spu_price_diff_3d": 2,
        "spu_price_diff_7d": 3,
        "spu_price_diff_30d": 4,
        "spu_price_ratio_1d": 5,
        "spu_price_ratio_3d": 6,
        "spu_price_ratio_7d": 7,
        "spu_price_ratio_30d": 8,
        "spu_hot_ratio_1d": 9,
        "spu_hot_ratio_3d": 10,
        "spu_hot_ratio_7d": 11,
        "spu_hot_ratio_30d": 12,
        "spu_default_sku": "shv2_52234ee3feca1ee3b593aac640fe3c46",
        "spu_pic_embed": "-0.3843969404697418,0.5590825080871582,0.47696077823638916"
    }
}
```
        * 正排结果示例：
            * 自主查询：[https://vs.baidu-int.com/baise/tool/data](https://vs.baidu-int.com/baise/tool/data)，key：9[ShopChart]3[spu]8[spu_info]0[]37[shv2_0de5f51a946ac0e309d38c5d887502e6]


![](/personal-site-mvp/img/doc-placeholder.svg "")
            * 数据示例：

```
{
    "oritext_forward_list": [
        {
          "key.AsUTF8": "spu_clk_3d",
          "key.AsGB18030": "spu_clk_3d",
          "key.AsBinary": "c3B1X2Nsa18zZA==",
          "value.AsUTF8": "0",
          "value.AsGB18030": "0",
          "value.AsBinary": "MA=="
        },
        {
          "key.AsUTF8": "spu_sh_category_tag_list",
          "key.AsGB18030": "spu_sh_category_tag_list",
          "key.AsBinary": "c3B1X3NoX2NhdGVnb3J5X3RhZ19saXN0",
          "value.AsUTF8": "",
          "value.AsGB18030": "",
          "value.AsBinary": ""
        },
        ....
     "textrel_forward_list": [
        {
          "key.AsUTF8": "name_textrel",
          "key.AsGB18030": "name_textrel",
          "key.AsBinary": "bmFtZV90ZXh0cmVs",
          "textrel_field_list": [
            {
              "weight": 1,
              "term_info_list": [
                {
                  "name.AsUTF8": "",
                  "name.AsGB18030": "畅享",
                  "name.AsBinary": "s6nP7Q==",
                  "sign": 17136101693432267000,
                  "weight": 0.082087,
                  "offset_list": [
                    25
                  ]
                }
                ...
```
* **vs-rank（新增用户特征）:**
    * **user特征获取：**
        * 策略组件添加：
            * 路径**：**vs-rank/strategies/common/default_k_v_dict_strategy/rank_spu_search_user_feature_kvdict_strategy.conf




```
[@kvdict_info]
    process_level: request
    ### 数据来源
    [.dict_name]
        field_key: "feature_dict"
    [.@key_value]
        ### 生成获取数据的key值
        [..key]
            ### 对query添加前缀
            field_processors: algorithm(String.concat(),"bijia_ranker_qry_stat_v1_",query)
            [...sub_fields]
                [....query]
                    field_key: "query"
                    field_type: query_rank_info
                    ### 对query进行小写处理后，再用md5加密
                    field_processors: algorithm(String.to_lower(),field_value), generate_sign_str(MD5,LOWER_HEXADECIMAL)
                    mode: PRE_FILL
        ### value结果
        [..value]
            ### value格式为json
            value_type: json
            ### 结果名称
            [...result_name]
                field_key: "query_feature"
            ### 取空时默认值
            [...default_value]
                field_key: "{}"
            ### value的子字段
            [...@sub_key]
                ### 子字段名称
                key: "qry_name"
                ### 默认值
                default_value: ""
                ### 结果取名
                result_name: "qry_name"
        ......
```
        * 策略加入到搜索流程
            * 路径：vs-rank/tables/spu_search_ann/spu_search_ann.conf和vs-rank/tables/spu_search_ann/spu_search_index.conf，下述文件介绍spu_search_ann的修改，spu_search_ann/spu_search_index.conf的修改和ann修改一致，不做过多赘述


```
......

[strategies]

    .......
    
    [.after_search]
    
        ......
        
        [..@strategies]
            name: rank_spu_search_query_feature_kvdict_strategy
        [..@strategies]
            name: rank_spu_search_user_feature_kvdict_strategy
            [...skip_condition]
                type: ||
                [....@field_info]
                    field_key: "uid"
                    field_type: param_map
                    default_value: ""
                    field_processors: mapping("": 1; DEFAULT: 0)
                    
......
```
    * **dump更新：**
        * 策略组件更新：
            * 路径：vs-rank/strategies/spu_search/default_dump_feature_strategy/rank_spu_dump_feature.conf



```
[dump_mode]
    field_key: "DUMP_TO_DISK"
[query_level_feature]
    # 基础字段dump
    [.param_map]
    [.custom]
        [..@feature_info]
            [...feature_name]
                field_key: "sid_list"
            [...feature_value]
                field_key: ALL
                field_type: exp_id_set,get_key
                default_value: 123321
                multiple_value_merger: concat(",")
    # 额外添加的字段dump
    [.string_factor_dict]
        white_key_list: usr_avg_price,usr_min_price,usr_max_price,usr_last7d_clk_spu,usr_last7d_clk_keywords,usr_last7d_clk_brand,usr_last7d_clk_cate1,usr_last7d_clk_cate2,qry_name,qry_include_male,qry_include_female,qry_male_ratio,qry_female_ratio,qry_expose_price_max,qry_expose_price_min,qry_expose_price_avg,qry_click_price_max,qry_click_price_min,qry_click_price_avg
[item_level_feature]
    # 额外添加的字段dump
    [.string_factor_dict]
        white_key_list: scs_model_kv_score
    [.double_factor_dict]
    # 基于正排字段dump
    [.forward_dict]
[meta_info]
    use_default: 0
```
* **架构组件（新增undb配置）：**
    * 因为新的特征存入的undb之前并没有被该场景的服务所调用过，所以需要在架构组件中加入该undb的配置


![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 新架构组件的文件名称需要策略组件中的[.dict_name]中的存储的key一致，组件里填充的是undb的信息

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 模型
### 模型结构
#### **模型：**wideAndDeep
* Wide&Deep 模型是由谷歌提出的一种用于推荐系统等任务的深度学习模型。它结合了线性模型（“Wide” 部分）和深度神经网络（“Deep” 部分）的优点。“Wide” 部分是一个广义线性模型，用于处理大量的原始特征和交叉特征。这些交叉特征是通过人工特征工程得到的，能够有效地记忆用户的历史行为模式。例如，在电商推荐中，可能包括用户购买的商品类别和品牌的交叉特征，像 “购买运动品牌的运动服装” 这样的特征组合。“Deep” 部分是一个深度神经网络，通常由多个全连接层组成。它可以自动地从原始特征中提取高阶特征。比如，对于用户的年龄、性别、浏览历史等多种特征，深度神经网络可以挖掘出其中潜在的复杂关系，如不同年龄段和性别的用户在浏览行为上的深层次差异。

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 价格表使用的模型结构：

[流程图]
    * deep:6层全连接

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * wide:1层全连接

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * output:concat后过一层全连接

![](/personal-site-mvp/img/doc-placeholder.svg "")
* **模型目标：**单目标，预估商品点击率

#### **模型：**CGC
* CGC是在MMOE模型的结构上进行改进，除了所有任务共享的专家（Experts Shared）外，还为每个任务加入了特有的专家部分（如 task A 的 Experts A、task B 的 Experts B 等）。模型输入会先映射到这些共享和特有的专家模块，专家模块通常是 ReLU 激活函数的全连接层。每个任务都有自己独立的门控网络，该门控网络是一个没有 bias 和激活函数的全连接层，然后接 softmax。通过门控网络，每个任务可以选择共享的 Experts 和自己特有的 Experts，然后将选择的专家加权平均后输入到任务对应的 Tower 层（MLP 网络层），最终由多个 Tower 决定最终的结果。

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 价格表使用的模型结构：

[流程图]
    * 构建网络

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * expert_shared（共享专家模块）

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * expert_special（独有专家模块）

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * input_net

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 模型目标：多目标，预估商品点击率和价格表点击率

### 模型训练
* **训练配置：**
    * **配置文件**：


```
mode: train

datasets:
  # 训练结束日期
  train_date: yesterday
  # 训练周期
  train_date_range: 30
  # 过滤日期
  skip_date: 
    - "20241020"
    - "20241021"
    - "20241022"
    - "20241023"
    - "20241024"
    - "20241025"
    - "20241026"
    - "20241027"
    - "20241028"
    - "20241029"
    - "20241212"
    - "20241213"
  dataset_type: InMemoryDataset
  # 训练数据路径
  train_data_path: 
    - "afs://wolong.afs.baidu.com:9902/user/sasd-goods/goods-search/wanghe25/bijia/train_data/"
  test_data_path: 
    - "afs://wolong.afs.baidu.com:9902/user/sasd-goods/goods-search/wanghe25/bijia/train_data/"

# hdfs配置
hdfs:
  fs_name: xxxxx
  fs_ugi: xxxxx

# 训练参数
train:
  batch_size: 64
  thread_num: 12
  shuffle_thread: 12
  preload_thread: 12
  join_common_thread: 16
  update_thread: 12
  pipe_command: tools/python/bin/python script/dataset_generator.py
  request_timeout_ms: 500000
  connect_timeout_ms: 10000
  max_retry: 3
  debug: False
  learning_rate: 0.0005
  write_stdout_frequency: 1
  save_delta_frequency: 1
  checkpoint_per_pass: 1
  pass_num: 1
  save_xbox_before_update: False
  split_interval: 5
  split_per_pass: 2

model:
  # 模型存储地址
  output_path: afs://wolong.afs.baidu.com:9902/user/sasd-goods/goods-search/wanghe25/bijia/PersonalModelOnline
  save_first_base: False

# 离线预测配置
infer:
  init_model_path: afs://wolong.afs.baidu.com:9902/user/sasd-goods/goods-search/wanghe25/bijia/PersonalModelOnline
  infer_data_path: afs://wolong.afs.baidu.com:9902/user/sasd-goods/goods-search/wanghe25/bijia/PersonalModelOnline
  # load mode:
  #     0  checkpoinnt
  #     1  delta
  #     2  base
  #     3  batch
  load_mode: 0


```
    * **训练数据：**
        * **数据来源：**线上曝光点击样本，使用hdfs存储
        * **特征：**
            * 特征列表：见上述介绍
            * 特征处理：
                * 使用mr任务结合mxfeat算子对特征进行处理，任务执行如下




![](/personal-site-mvp/img/doc-placeholder.svg "")
                    * 算子任务主要关注红框标注的配置文件，其中算子会先处理preprocess_*开头文件里的特征，为context中交叉特征的计算做好数据准备

![](/personal-site-mvp/img/doc-placeholder.svg "")
                    * 特征算子举例介绍：所有算子都在mxfeat定义并实现，这一步线上线下使用的是同一个算子，确保线上下的特征值的数据是一致的，其中所有sparse特征算子处理后会分别获取其hash值作为特征值结果
                        * ***name=f_user_uid;class=Gsc_sparse_repeated_uint64;slot=30001;depend=query_feature;arg=f_user_uid,30001***，该配置处理**user_uid**特征，使用的算子类方法是***Gsc_sparse_repeated_uint64，***处理逻辑为记录该sparse特征值***，***基础数据从**query_feature**词典中获取，获取key为**f_user_uid**，slot记录的是编号
                        * ***name=f_spu_price;class=Gsc_log_norm_float;slot=70001;depend=item_feature[$0];arg=f_spu_price,1,0,15，***该配置处理spu_price特征，使用的算子类方法是***Gsc_log_norm_float，***处理逻辑为将特征值用log计算后在记录值，基础数据从**item_feature**词典中获取，获取**key**为f_spu_price，**1,0,15**分别表示数据维度、默认值和裁剪比例
                        * 其余算子如下，不一一介绍，具体算子实现在mxfeat查看，可以自行开发加入
                            * ***name=f_spu_imp_3d;class=Gsc_min_max_norm_float;slot=70005;depend=item_feature[$0];arg=f_spu_imp_3d,1,0,1,20000***
                            * ***name=f_spu_ctr_3d ;class=Gsc_no_process_float;slot=70011;depend=item_feature[$0];arg=f_spu_ctr_3d,1,0***
                            * ***name=f_query_cate_spu_cate_2;class=Gsc_cross_combination;slot=10015;depend=query_feature,item_feature[$0];arg=f_query_qp_category,f_spu_category_2_name,0,10015***


                    * 特征处理后结果输出顺序优先级：
                        * 先sparse后dense，再按文件顺序（上图为例，先context，后preprocess），最后按文件内的特征顺序


                * 基于顺序获取样本特征数据

![](/personal-site-mvp/img/doc-placeholder.svg "")
                * 基于特征map初始化输入层，这里需要注意输入层是按上述特征值顺序进行注入的

![](/personal-site-mvp/img/doc-placeholder.svg "")
                * 基于特征类型（sparse/dense）进行处理，sparse特征将转变成embeding，dense使用原输入层

![](/personal-site-mvp/img/doc-placeholder.svg "")
        * **batch_size：64**

    * **训练模式：**每日增量训练，连续训练30天
    * **学习率：**0.0005
    * **测试模式：**每日增量训练完成后，使用下一日的训练数据进行作为测试集进行测试
    * **损失函数：**
        * wide&deep:$LogLoss= - [y_{label}\log(y_{pred})+(1 - y_{label})\log(1 - y_{pred})]$


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
        * cgc：$Loss=LogLoss_{spu}+LogLoss_{card}$

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
        * 其中$y_{label}$是线上用户真实点击行为（有点击为1，无点击为0），$y_{pred}$是模型预测的结果

* **评估指标：**AUC
    * 目前线上模型的AUC是0.8136

* **训练代码：**
    * 读取训练参数


![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 准备必要环境，如hdfs服务器的连接

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 初始化优化器

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 初始化数据集路径

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 循环增量训练，并过滤数据有问题的日期

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 准备该轮训练的训练数据：

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 准备该轮训练的测试数据：

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 训练，并计算auc：

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 测试，并计算auc：

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 一轮训练完成，保存模型

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 模型上线
* **模型参数修改：**
    * 新特征线上时修改cube.conf文件的table_name，该table_name主要存储的是sparse特征的embedding数据


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 如果有新增特征，也需要修改model.conf文件

```
# 模型名称
model_name: goods_personality_predict_xuzhi05_ctr_model_20250120

resource_num : 5
predictor_type : PaddleFluidEx
# 特征处理算子插件
preprocess_plugin : GoodsSearchCommonPreprocessHandler
feature_fetch_plugin: GoodsCubeTransTensorFetcher
predict_plugin : DefaultPredictHandler
postprocess_plugin : GoodsCtrEmbeddingPostprocessHandler

batch: 0
batch_max_time_ms: 0
batch_max_size: 0

model_file: dnn_plugin/__model__
model_param: dnn_plugin/params

use_magent: 1
# embedding表
table_name: goods-search-bijia-ctr-v2-dalton

use_click : 1
click_ratio : 8
use_show : 1
show_ratio : 1
use_lr : 1
lr_ratio : 1000000
mf_ratio : 1000000

# 特征索引信息
can_fill_with_zeros : 1
sparse_index : 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99
sparse_slots : 10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034,10035,10036,10037,10038,10039,10040,10041,10042,10043,10044,10045,10046,10047,10048,10049,10050,10051,10052,10053,10054,10055,10056,10057,10058,10059,10060,10061,10062,10063,10064,20001,20002,20003,20004,20005,20006,20007,30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028
sparse_embedding_size : 8
dense_index : 99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136
dense_slots: 70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024,70025,70026,40001,40002,40003,40004,40005,40006,40007,40008,50001,50002,50003
dense_embedding_size : 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,768,1,1,1,1,1,1,1,1,1,1,1

process_mode : PARALLEL
parallel_process_degree : 3
max_batch_size : 40

parallel_on_slots : 1
# 并行处理配置，这里会有三个线程，并行处理索引为0-63、64-98、99-135的特征
opt_process_index_ranges : 0~63,64~98,99~135

dump_mode: 0 
# 样本类型，决定用什么类进行封装
sample_type: 7

fill_zero_after_cvm: 1 
```
* **模型仓库部署**
    * 模型仓库链接：[https://sdp.baidu-int.com/269/model-center/model-repository/model-info/23809?tab=basicData](https://sdp.baidu-int.com/269/model-center/model-repository/model-info/23809?tab=basicData)
    * 需要配置模型的基本信息、上线信息和模型数据，当版本状态为已保存时，为配置成功


![](/personal-site-mvp/img/doc-placeholder.svg "")
* **上线实验**
    * 实验id申请：[https://ab.baidu-int.com/sample/#/ab/detail?product=172&id=129499](https://ab.baidu-int.com/sample/#/ab/detail?product=172&id=129499)
    * baise配置：
        * 在baise/324/vsrank/tables/spu_search/spu_search.conf文件中[scene_info]子栏下配置实验



![](/personal-site-mvp/img/doc-placeholder.svg "")
        * 在baise/324/vsrank/tables/spu_search_index/spu_search_index.conf文件中配置实验判断规则，根据黑白名单中的实验名称来决定实验组流量走哪个规则

![](/personal-site-mvp/img/doc-placeholder.svg "")

