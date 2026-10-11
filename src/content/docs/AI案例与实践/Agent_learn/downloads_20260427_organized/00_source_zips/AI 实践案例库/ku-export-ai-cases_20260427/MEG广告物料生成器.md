---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "MEG广告物料生成器"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\MEG广告物料生成器.md"
---
MEG广告物料生成器

#### 🧑‍🏫 案例作者：[@余笑阳](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：秒哒
#### 📒 案例概要：本文介绍了MEG广告物料生成器的开发案例，该工具利用秒哒平台简化广告物料生成过程。物料分为凤巢和原生广告两种，均需解析三层结构。生成器支持自由组合物料、生成json片段，并兼容不同物料类型。通过UI界面，用户可拖拽、编辑、组合及下载物料，极大提升了广告制作的灵活性和效率。
LU中间页的物料生成，需要麻烦的字符串处理



物料分为两种

1.凤巢广告物料 - 需要解析三层结构

2.原生广告物料 - 需要解析三层结构



预期生成器的作用

1.希望可以自由组合物料，生产最终可供消费的json片段

2.希望可以支持不同类型的原生物料json片段，更新对应层级的数据



#### 懒的看内容，直接用点击 [https://app-7yj1bkw5b18h.appmiaoda.com/](https://app-7yj1bkw5b18h.appmiaoda.com/)


### 凤巢物料 - 三层结构
#### 2.1 大图广告（Big Picture Ads）
**触发条件：** `materiel.style` 中特定物料ID

* idea11019 - 大图广告
* idea11055 - 大图广告
* idea10015 - 大图广告（带图片）

#### 2.2 三图广告（Three Pictures Ads）
**触发条件：** `materiel.style` 中特定物料ID

* idea2892
* idea9050
* idea3138
* idea11027
* idea3037
* idea3198（旅游页面专用）

#### 2.3 单图广告（Single Picture Ads）
**触发条件：** `materiel.style` 中特定物料ID

* idea2062
* idea3009
* idea80001
* idea10008
* idea2409

#### 2.4 其他特殊类型
* idea80003 - 根据图片数量动态判断（1-2图为单图，3+图为三图）
* 抽奖广告用到的物料：idea80001、idea10008、idea80003
* 下载类广告：idea2028



```
{
            "ad_type": 1,
            "ad_info": {
                "info": "{\"title\":\"广告1 idea10008凤巢单图 淘宝零食实惠不停全场低至3元9件，限时秒杀快...\", \"recom_reason\":\"秒杀0.1折起\", \"user_portrait\":\"https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/103450ee-ec1a-47a3-8519-a7841c4c5ce0\", \"desc\":\"中国<font color=\\\"#CC0000\\\">鲜花</font>中国鲜花,完美的信誉,顶尖的服务,鲜花,免费送货热线:400-800-2610,1-3小时送达全国\",\"url\":\"京东\",\"link\":\"https://m.baidu.com/baidu.php?url=K00000K3Zd4fCW_uEVFYJhlJ4E0B89A-S8TYumnp2_-9mrpfs3jSdpHiPkVNtgdXkvl4oSHmqq5-2aT1kbuYl9SVfbvB44Mx8NvBXYO4NF0PxNWZWyxb4drcY0yv4Hv67RCLosWRKFK27J2Fi-M2by6M0zeFSaNspW2CCvPPH6gJQy_4upEwfmIgyWR6cZ3SWd-phbfygEDyKrZADke3cCyJuxl0.7b_iHF8xnhA94wEYL_SNK-deQbfHgI3ynDgg6msw5I7AMHdeyQleEZWYqMHEovpS5Zkol3vPrM-zI5HkzuPv1-3eorzEFb4XrHI8eQPMWdEmORSOzOBXTx4SZHgJOr1Zsu5qoNOvr_UZgykNfCm3t5Zv3TMds45o6C_kgXNK-deQbmTMdWHGY3TMdCgkGuh9JstxonMgWkmX5zYlXgFYq5ZFbLUrgW8_e2thH-34Pve__vXrZFYqJIZ0lpejkSyZF8tSMjbLUqSZF8qxU9zUE5u9zUVMZjbLXEzs4PLM8s4PLVttrHIlqrZF8tqvZF8qptrHI_LmThe1tTrHIltTrHIlS8ZF8tOZjbLXEo9zUVOds4PLM8s4PLVttrHI_L3The1vmThevtTrHI_LmTMHxjzll5QZPj93OFhBOi1Gu4mYlXyoIzlI5QblXMWbzUVMQkLyI-XHFztTheIvyU57mhPXzA8l4POQjWhyAp7WFb3470.U1Ykn0Kk5U1i1pgyktHT_Q2LsnSd1Un0mywkXHvtY_v-d_xDLQazVtj5VTv10A7bTgfqn6KspynqnfKY5IUZkPztYoeH1egP_eazde00pyYqrjR10ATqILPYT6KdpHY0TA-b5HDY0APGujY1nWf0Ugfqrj0snj7xnH0snjuxnW0dnfKopHYs0ZFY5HmYn6KBpHYznjuxnW03g1RsndtLnjPxP10Yg1csnj0zg1csnjnk0AdW5HKxn7tznjRk0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5HD0ThCqn0KhIjYz0ZKC5H00ULnqn6KBI1YY0A4Y5HD0TLCq0A71gv-bm1dsTzd-mvC0pywW5fKspZw45fKYmgFMugfqn17xn1Dzg1b0IZN15HDvP1m3P1csnHmsnWT3rHTkPjnk0ZF-TgfqnHm1P1fvnH6LnHmznfK8IZws5Hn0mv6qUZNxmvklpMb0IZRqP1mkPj6sPfK15yw-rA7WmHw-uAn4rH0LnhD0IAYqn0KWuWYk0ZFB5HD0UZNopHYk0AP8IA3quW9WnywbuyFxmLKz0ZP1TjYz0ZP1Tjcqn0KYIZ0qnsKbIZ0qn6KGIAYqn0K9uAP_mgP15HD10A7bXjYs0ZPbpdqv5HD0IvbqP0KhTvPCUyfqn6KYujYs0AkdT1YLmyRvmvnzP1bsP1TvujTk0AkdTLfqPWD4ry7-uWD0UZNWIjYvnHb4mymvu6K1mvRqnsK_INqGuAnqUhCsn6KvUWY3nj0d0A7sT7q1pyfquW9Wnywbuyc0uMcqnHf0TLcqn1cY0AF-TvsqQHD0UZNLIZcqPWndnWfLP1TYrjfznjmYn1R3PsKYTh7buHDqn0KYTh7buHcqn0K-XZKGujYznjDLn1NxnW0znHc4g1csnWc1n7tznjczPWuxnW0znWb4g1csnWf4n-tznjndPjwxnW0vPH0zg1csPWm4ndtznj6krHFxnW04rjTY0ZNzUjdCIZwsrBtEPAFbmWw9QidhrAnkuAw-mB4WUvYE0A-Vuy-xUyfd5HDsPHmLuHTYuhf3mvNBnAubPjnsrH6kuHPWrHD3mHD40ZPGujdhnAR4rjb3Pvf1nHf3PW790AP1UHd7nDmYwWN7PbckPjNAPHPA0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg100uA78IyF-gLK_my4GuZnqn7tsg100TA7Ygvu_myTqn0KsThqb5HDznWTsnjD1PjTY0APY5iY0uAPGujY10ANYpyfqPWf0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0A7buhk9u1Yk0Akhm1Ys0AwWmvfqnb7APHm1wHmsnDmLwWR4wWm3nWbzPYn4nYc4PHmYwbwtn0KYTh7buHYs0AFbpyfqrjPKfW0dPW9DwjuafYDdfbRzf1uAwDDzPjTdfWDdfbR0IvuzUvYq0AFY5H00Uv7YI1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wnansc1nWna3snj0snj0Wni3snj0knj00uAkxIA7M5HD0TNqv5H08PH9xna3sn7tsQW0sg108njKxna3sndtkQW0sg108nWNxn0KBTdqsThqbpyfqn0KzUv-hUA7M5H00mLmq0A-1gvPsmHYs0APs5H00ugPY5H00mLFW5HRsnWcz&us=newvui&ai=0_429107157_1&word=&qid=f0e98987d314861a&bdrank=9&rank=10&sourceid=1400&placeid=1#dplk=tbopen://m.taobao.com/tbopen/index.html?source=alimama_bd_sem_feeds&bc_fl_src=alimama_sem_mm_26632258_3504122_32554087&action=ali.open.nav&module=h5&bootImage=0&appkey=24532550&appName=%C3%A7%C2%99%C2%BE%C3%A5%C2%BA%C2%A6&backURL=baiduboxapp://&h5Url=http://redirect.simba.taobao.com/rd?c=un&w=unionsem&k=b1d73646918f3371&p=mm_26632258_3504122_32554087&b=GIDMEsQzm1gQasw2JgY&s=&f=https%3A%2F%2Fuland.taobao.com%2Fsemm%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32554087%26keyword%3D%25E6%2599%25BA%25E8%2583%25BD%25E5%25AE%25B6%25E5%25B1%2585%25E7%25B3%25BB%25E7%25BB%259F%25E5%25AE%2589%25E8%25A3%2585%26bc_fl_src%3Dalimama_sem_h5_mm_26632258_3504122_32554087\",\"style\":{\"idea1017\":{},\"idea10008\":{\"image\":\"https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/27291187-b673-4ee3-b53b-9fcfc5f8e7b4\", \"link\":\"http://www.baidu.com\",\"price\":\"1219\",\"ori_price\":\"2000\",\"name\":\"小米手机’小米手机小米手机小米手机小米手机小米手机\",\"tags\":\"9.6英寸高清大屏，清晰护眼！4800 mAh大电池，长续航追剧一整天！【限时直降50元】限时直降50\",\"attributes\":\"麟980 AI处理器，3D仿生感光技术智能识别人脸，后置2400万 AI三摄，40W安全超级快充，石墨烯散热技术带来畅快游戏体验。【到手价：4499元】限时优惠800元，下单再减500元，再赠价值268元礼包（荣耀音乐小巨蛋+二合一数据线），一降到底！\",\"sales_volume\":\"满意度99%\",\"seller_name\":\"京东\",\"display_type\":\"0\"}},\"general_data\":{\"cpm\":4500080000,\"bidword\":\"各种花朵\",\"search_id\":\"7deaf65d964e86a8\",\"from\":\"FC\",\"word_id\":119291861,\"ad_type\":131072,\"extra_type\":0,\"ip\":\"172.10.4.5\",\"winfo_id\":1523719733,\"idea_id\":24493271524,\"user_id\":30553688,\"plan_id\":68977154,\"unit_id\":68977154,\"rank\":0,\"ad_price\":104,\"baiduid\":\"79FDBBC5D9034AD629968C5391F7D14E\",\"passport\":0,\"ovlexp_id_list\":\"\",\"cmatch\":822,\"wmatch\":63,\"search_time\":\"1534497213\"}}"
            },
            "extra": []
         }
```
```
{
    "title": "广告1 idea10008凤巢单图 淘宝零食实惠不停全场低至3元9件，限时秒杀快...",
    "recom_reason": "秒杀0.1折起",
    "user_portrait": "https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/103450ee-ec1a-47a3-8519-a7841c4c5ce0",
    "desc": "中国<font color=\"#CC0000\">鲜花</font>中国鲜花,完美的信誉,顶尖的服务,鲜花,免费送货热线:400-800-2610,1-3小时送达全国",
    "url": "京东",
    "link": "https://m.baidu.com/baidu.php?url=K00000K3Zd4fCW_uEVFYJhlJ4E0B89A-S8TYumnp2_-9mrpfs3jSdpHiPkVNtgdXkvl4oSHmqq5-2aT1kbuYl9SVfbvB44Mx8NvBXYO4NF0PxNWZWyxb4drcY0yv4Hv67RCLosWRKFK27J2Fi-M2by6M0zeFSaNspW2CCvPPH6gJQy_4upEwfmIgyWR6cZ3SWd-phbfygEDyKrZADke3cCyJuxl0.7b_iHF8xnhA94wEYL_SNK-deQbfHgI3ynDgg6msw5I7AMHdeyQleEZWYqMHEovpS5Zkol3vPrM-zI5HkzuPv1-3eorzEFb4XrHI8eQPMWdEmORSOzOBXTx4SZHgJOr1Zsu5qoNOvr_UZgykNfCm3t5Zv3TMds45o6C_kgXNK-deQbmTMdWHGY3TMdCgkGuh9JstxonMgWkmX5zYlXgFYq5ZFbLUrgW8_e2thH-34Pve__vXrZFYqJIZ0lpejkSyZF8tSMjbLUqSZF8qxU9zUE5u9zUVMZjbLXEzs4PLM8s4PLVttrHIlqrZF8tqvZF8qptrHI_LmThe1tTrHIltTrHIlS8ZF8tOZjbLXEo9zUVOds4PLM8s4PLVttrHI_L3The1vmThevtTrHI_LmTMHxjzll5QZPj93OFhBOi1Gu4mYlXyoIzlI5QblXMWbzUVMQkLyI-XHFztTheIvyU57mhPXzA8l4POQjWhyAp7WFb3470.U1Ykn0Kk5U1i1pgyktHT_Q2LsnSd1Un0mywkXHvtY_v-d_xDLQazVtj5VTv10A7bTgfqn6KspynqnfKY5IUZkPztYoeH1egP_eazde00pyYqrjR10ATqILPYT6KdpHY0TA-b5HDY0APGujY1nWf0Ugfqrj0snj7xnH0snjuxnW0dnfKopHYs0ZFY5HmYn6KBpHYznjuxnW03g1RsndtLnjPxP10Yg1csnj0zg1csnjnk0AdW5HKxn7tznjRk0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5HD0ThCqn0KhIjYz0ZKC5H00ULnqn6KBI1YY0A4Y5HD0TLCq0A71gv-bm1dsTzd-mvC0pywW5fKspZw45fKYmgFMugfqn17xn1Dzg1b0IZN15HDvP1m3P1csnHmsnWT3rHTkPjnk0ZF-TgfqnHm1P1fvnH6LnHmznfK8IZws5Hn0mv6qUZNxmvklpMb0IZRqP1mkPj6sPfK15yw-rA7WmHw-uAn4rH0LnhD0IAYqn0KWuWYk0ZFB5HD0UZNopHYk0AP8IA3quW9WnywbuyFxmLKz0ZP1TjYz0ZP1Tjcqn0KYIZ0qnsKbIZ0qn6KGIAYqn0K9uAP_mgP15HD10A7bXjYs0ZPbpdqv5HD0IvbqP0KhTvPCUyfqn6KYujYs0AkdT1YLmyRvmvnzP1bsP1TvujTk0AkdTLfqPWD4ry7-uWD0UZNWIjYvnHb4mymvu6K1mvRqnsK_INqGuAnqUhCsn6KvUWY3nj0d0A7sT7q1pyfquW9Wnywbuyc0uMcqnHf0TLcqn1cY0AF-TvsqQHD0UZNLIZcqPWndnWfLP1TYrjfznjmYn1R3PsKYTh7buHDqn0KYTh7buHcqn0K-XZKGujYznjDLn1NxnW0znHc4g1csnWc1n7tznjczPWuxnW0znWb4g1csnWf4n-tznjndPjwxnW0vPH0zg1csPWm4ndtznj6krHFxnW04rjTY0ZNzUjdCIZwsrBtEPAFbmWw9QidhrAnkuAw-mB4WUvYE0A-Vuy-xUyfd5HDsPHmLuHTYuhf3mvNBnAubPjnsrH6kuHPWrHD3mHD40ZPGujdhnAR4rjb3Pvf1nHf3PW790AP1UHd7nDmYwWN7PbckPjNAPHPA0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg100uA78IyF-gLK_my4GuZnqn7tsg100TA7Ygvu_myTqn0KsThqb5HDznWTsnjD1PjTY0APY5iY0uAPGujY10ANYpyfqPWf0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0A7buhk9u1Yk0Akhm1Ys0AwWmvfqnb7APHm1wHmsnDmLwWR4wWm3nWbzPYn4nYc4PHmYwbwtn0KYTh7buHYs0AFbpyfqrjPKfW0dPW9DwjuafYDdfbRzf1uAwDDzPjTdfWDdfbR0IvuzUvYq0AFY5H00Uv7YI1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wnansc1nWna3snj0snj0Wni3snj0knj00uAkxIA7M5HD0TNqv5H08PH9xna3sn7tsQW0sg108njKxna3sndtkQW0sg108nWNxn0KBTdqsThqbpyfqn0KzUv-hUA7M5H00mLmq0A-1gvPsmHYs0APs5H00ugPY5H00mLFW5HRsnWcz&us=newvui&ai=0_429107157_1&word=&qid=f0e98987d314861a&bdrank=9&rank=10&sourceid=1400&placeid=1#dplk=tbopen://m.taobao.com/tbopen/index.html?source=alimama_bd_sem_feeds&bc_fl_src=alimama_sem_mm_26632258_3504122_32554087&action=ali.open.nav&module=h5&bootImage=0&appkey=24532550&appName=%C3%A7%C2%99%C2%BE%C3%A5%C2%BA%C2%A6&backURL=baiduboxapp://&h5Url=http://redirect.simba.taobao.com/rd?c=un&w=unionsem&k=b1d73646918f3371&p=mm_26632258_3504122_32554087&b=GIDMEsQzm1gQasw2JgY&s=&f=https%3A%2F%2Fuland.taobao.com%2Fsemm%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32554087%26keyword%3D%25E6%2599%25BA%25E8%2583%25BD%25E5%25AE%25B6%25E5%25B1%2585%25E7%25B3%25BB%25E7%25BB%259F%25E5%25AE%2589%25E8%25A3%2585%26bc_fl_src%3Dalimama_sem_h5_mm_26632258_3504122_32554087",
    "style": {
        "idea1017": {},
        "idea10008": {
            "image": "https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/27291187-b673-4ee3-b53b-9fcfc5f8e7b4",
            "link": "http://www.baidu.com",
            "price": "1219",
            "ori_price": "2000",
            "name": "小米手机’小米手机小米手机小米手机小米手机小米手机",
            "tags": "9.6英寸高清大屏，清晰护眼！4800 mAh大电池，长续航追剧一整天！【限时直降50元】限时直降50",
            "attributes": "麟980 AI处理器，3D仿生感光技术智能识别人脸，后置2400万 AI三摄，40W安全超级快充，石墨烯散热技术带来畅快游戏体验。【到手价：4499元】限时优惠800元，下单再减500元，再赠价值268元礼包（荣耀音乐小巨蛋+二合一数据线），一降到底！",
            "sales_volume": "满意度99%",
            "seller_name": "京东",
            "display_type": "0"
        }
    },
    "general_data": {
        "cpm": 4500080000,
        "bidword": "各种花朵",
        "search_id": "7deaf65d964e86a8",
        "from": "FC",
        "word_id": 119291861,
        "ad_type": 131072,
        "extra_type": 0,
        "ip": "172.10.4.5",
        "winfo_id": 1523719733,
        "idea_id": 24493271524,
        "user_id": 30553688,
        "plan_id": 68977154,
        "unit_id": 68977154,
        "rank": 0,
        "ad_price": 104,
        "baiduid": "79FDBBC5D9034AD629968C5391F7D14E",
        "passport": 0,
        "ovlexp_id_list": "",
        "cmatch": 822,
        "wmatch": 63,
        "search_time": "1534497213"
    }
}
```
```
"idea10008": {
    "image": "https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/27291187-b673-4ee3-b53b-9fcfc5f8e7b4",
    "link": "http://www.baidu.com",
    "price": "1219",
    "ori_price": "2000",
    "name": "小米手机’小米手机小米手机小米手机小米手机小米手机",
    "tags": "9.6英寸高清大屏，清晰护眼！4800 mAh大电池，长续航追剧一整天！【限时直降50元】限时直降50",
    "attributes": "麟980 AI处理器，3D仿生感光技术智能识别人脸，后置2400万 AI三摄，40W安全超级快充，石墨烯散热技术带来畅快游戏体验。【到手价：4499元】限时优惠800元，下单再减500元，再赠价值268元礼包（荣耀音乐小巨蛋+二合一数据线），一降到底！",
    "sales_volume": "满意度99%",
    "seller_name": "京东",
    "display_type": "0"
}
```


## 原生物料 - 三层结构
**物料ID列表：**

* idea3176 - 三图原生广告
* idea3177 - 单图原生广告
* idea16511 - 三图下载类原生广告
* idea16513 - 大图下载类原生广告
* idea16515 - 大图原生广告
* idea16525 - 视频下载类原生广告
* idea16518 - 视频原生广告
* idea16532 - 视频原生广告
* idea16538 - 视频原生广告



```
{
            "ad_type": 2,
            "ad_info": {
                "info": "{\"ad_base_info\":{\"rank\":1,\"idea_id\":312271870159,\"winfo_id\":312262814879,\"user_id\":33099442,\"plan_id\":165987486,\"unit_id\":6140546568,\"ad_cpm\":86338,\"ad_type\":188,\"ad_flag\":2,\"title\":\"16518财务自由,家庭和睦,考了国际汉语教师证,全职太太在家即可兼职!\",\"desc1\":\"DFT\",\"desc2\":\"\",\"rcv_url\":\"http://m.baidu.com/baidu.php?url=a00000jCx3p_KaPSJb8h2ziG6GaoxtHuJHP4dkirc26bnwPmA_6SJ_cVCUOg-vpS3P6N2aUa4vz0kkfMBcaY_nCeV6d-RSHv4zGwksPihG_PPu1tGUHyYrvFLdZJG8vQ7PAKkg8C30gLjmsivVcIXTfg19W7vA4Zpo5ggGwWkYK_iKyqLmyX4F-NI0FRi9eHeeuQ2mK4vQGoQW9a56DbSDmf5PZa.Db_NR2Ar5Od66uxAS6Mz3D4g_kTPHniccLYDsTAg9CyHNtDD5WbvuPLH34qhOTM5vyUvTe5WEE1G8ood_eP-OW3q5xgBmhzlUGELSM9OP-Ofex1xEOlSZtvyOW7SLuZP3Yrnyg6lcVxyAGWWdEd3hPISjlt7bgO6OAQg-OfISxGO5JlUQAIXy1gPs4xrOOsNqMeX5OBSgHuum1Yxe5B1OvZvyyyxSjOguMW_Ox___CtEQO_1R5EYxlOSkfE4x5tL4O1xJxeQE1I_NMQ4GoOtZaMSFwt3EqJW_O3VLM4OCN45d5SQZxSXQdITeQ7OVRr7dL4EqJ9OvZT5Omtl7Nj_O3_TTrEq8UVOPSxtEUOsnEKOkxEqMUO_1xCQDk8LyIhOIuk4mTTzs1f_UOZWER0.U1Yk0ZDqz2EjtTUhE252de5b8_R0IjLrkPQNkXjwVfKGUHY3njf0u1Y0Iybq0ZKGujYznfKWpyfqnHRk0AwGujYznH01rjD0UgfqnHmdnH60mhnqn6KEIhsqn10snj0kQHc0TZ0qn0KYIgnqnHn3rjnYnjckPjDYPjbvrjb1n0Kzug7Y5HDvn1DLrjmsnjcLP1D0Tv-b5HT3nhw-nAczP1csnvnYuW60TA3qnfKET1Yz0ZIG5Hf0uh3qPHRsPjbdnjPxmLKz0APYp1Y0IZRqIHmvnj6zPHc0mywWUA71T1Y0IAYqnWTdnHT1nH630A7Wpyfq0ZPbpdqv5fK1TL0qnfKYujYvPW03nWRz0APC5ykdgvP_XhG40A4YIZ0qn6K9TZKxTv-b5fKGIAYqn0KVIZ-suHYkrfK9uZw4TARqnH630A7YTA-b5H00mLKGujYknj0k0ZK_pyfqnHR1nH6kPHcsrHRdnsKWpA-b5fK9TZKvUWY0IA735fKVIZnqnHmdnH60UvPsm1Y1c1cWnznknW0snanznHcdc1cknWRWranWc108rj0sc108PjDscznWnanzc1D8nj0Wcznsc1DWnansg10Wninsc10WnHcsnj0Wnansc1DWni3snankQW0snankQW0snankQW0snansQW0snansQW0snankQW0sc10Wnansc10Wni3snjKxn7tkQW0sn7tkQW0snansc10WnanWnansg1D8nj0sg1Kxna3snjKxni3snjKxn7tsg1Kxna3snansc10Wn7tsg1Kxn7tsg1Kxna3snj0snjKxn7tkQW0snj0sn7tsg1D8nj0snj0sg1Kxn7tsQW0snj0sn7tsg1Kxna3snj0snjKxna3snj0snjKxn7tsg1Kxn7tsg1Kxni3snj0snj0Wn7tsg108nj0snj0sg1Kxn7ts0ZGJXjYs0ZGJXHYsQWfkn0KlpMCqna3YnH00XhGY5HD8nj0s0A-WIjYkPWnsPj6YrjT30AuBTWYsQW6sn0KYTWcqn0KhUZDqn0KluLDqn0KluLcqni3snj00mvFY5H00mMPY5HKxn7tsg1Kxn7tsg1Kxna3sn7tsQW0s0APBT1YkPWnsPj6Yn1Dvg1Kxn7tsg1fzrHnsrjRYPsKBTvcqn0KEIWY4QW08n0KsIjY1n1R1rfKsULPGIA-EUWYs0ZKETv-Ypyq8gvPCmy4MuNqzuy71Uv3qn0KETh-xUgfqnH63rj60UgwxTZfqn0K9mvPY5fKbmvPb5fKbmLFs5fKbuguYTjY0Tv3q0ZKzUvfq0AqWTAPxUA7BgLPYmgwdT1Ys0APYTWYknWn1P0KdmhYqn0KEmLKWgvP_pyPo5H0Wnansc10Wnansc1D8nj0sc1D8nj0s0AuYXgK-5H00myw1U-q15H00myw1U-qGT1Y0mhd_5H00UgKY5H00UgKYIWYs0Ad9m1Rq0Aq95fK9uAPo5H00UZfqn0K1m1Ys0AqW5HD0Ih-buyqGujYknjm3nWn4Pj60mhN1UjYs0A-1uAsqn0KEUAw_5H00TZFEuv7bIWYk0A71XHYs0A7bTZTqn1Ts0A7bTA6qnWfd0A-1TjdBphkk0A91UATqn00k5H00nWY0n1Y0PjY0PHYknj0snjD0PWYkPj0vP1DvP1RkP1fLPj6vrHRLnf0L5Hc0rjY1nHczP1D3P1m4rj60rHY0TZFEudqYT1YkP1bsnjRvrHm4n1n3PHD3Pjf4P0KsThqMgLK15HDvnHf3PWTdn103rjndnjfLnHcL0ZKzUvIxIAbqn1DznWTkrjTvrHbs0ZKzUvIxTAbq0ZKWpHYknHfvnjfdrjcdP1cYnWcdPW6sP0KWpybqn1DznWTkrjTsnHR40ZPJpjYzPHR0TMF15H00mMNYmyTqn0KBmL0qnfK8ugfqnfKzIADqn0K-TLfqn0K1Uy_q0ZP1Tjcqn6KYIZ0qnfK_IgF9UhV-T-q15yfzmhu-rj6kuA7bPHfzuyR0UZN15ycvPWnsuhRYnWDsuWPbPWR0UZN1IjYvnHf1nHPWP0K_IyPY5HmkPjnkPjDz0Zwbpyfq0A7sTZPGujYzP1RkP1nkrj60mhN1UjYVnfK1mvRqPfKYIHddPWmsrjcdn6KWThnqn1Dvn1f0&wd=\",\"show_url\":\"DFT\",\"mt_newstyle\":\"{\\\"idea16518\\\":{\\\"apk_name\\\":null,\\\"doc_id\\\":null,\\\"duration\\\":39,\\\"exposure_url\\\":null,\\\"isSmartUrl\\\":false,\\\"item\\\":[{\\\"height\\\":640,\\\"url\\\":\\\"https:\\\\/\\\\/feed-image.baidu.com\\\\/0\\\\/pic\\\\/-535060830_1346111191.jpg\\\",\\\"width\\\":1140}],\\\"midpage_url\\\":null,\\\"monitor_url\\\":\\\"\\\",\\\"mt\\\":16518,\\\"na_url\\\":null,\\\"ori_landing_url\\\":\\\"https:\\\\/\\\\/aisite.wejianzhan.com\\\\/site\\\\/wjzt0r1w\\\\/c7282567-895e-409a-a79b-ed11fa88b776\\\",\\\"poster\\\":\\\"https:\\\\/\\\\/feed-image.baidu.com\\\\/0\\\\/pic\\\\/-535060830_1346111191.jpg\\\",\\\"reserved\\\":{\\\"hasGif\\\":null,\\\"siteid\\\":55365015,\\\"sjhAppid\\\":255,\\\"tit_t\\\":0,\\\"usePublic\\\":1,\\\"videoid\\\":104864400},\\\"title\\\":\\\"财务自由,家庭和睦,考了国际汉语教师证,全职太太在家即可兼职!\\\",\\\"ulkUrl\\\":null,\\\"url\\\":\\\"https:\\\\/\\\\/aisite.wejianzhan.com\\\\/site\\\\/wjzt0r1w\\\\/c7282567-895e-409a-a79b-ed11fa88b776?fid=rjmdrH6zPjTkPHRzPjb3nW0sr7t3njwxnf&ch=3&bfid=fbuFw0nKSnfjToQ6Qg600afj0frzjEbK14WpVD6000axU7aYi0000KR0-s0H000l__UrtIxRYtb_EPQPGUoPkn0_Ee1KzeMlEnJl8V5EET12GVpbQnBodojnJtzodPJtYozYEtht4VpscfWrkPQNkXjwVH4kUrT\\\",\\\"user_icon\\\":\\\"\\\",\\\"user_name\\\":\\\"国际汉语教师证\\\",\\\"user_portrait\\\":\\\"https:\\\\/\\\\/feed-image.baidu.com\\\\/0\\\\/pic\\\\/7681477b6591df838d0b6cc327192195.jpg\\\",\\\"video_target_rcv_url\\\":\\\"http:\\\\/\\\\/m.baidu.com\\\\/baidu.php?url=a00000jCx3p_KaPSJ967OtWnJOn74spAYHG7H11MEdTDBvK4oURi02yJTDqPZQC3hIac3rLyKDA4NvDyvanec1PZ74zFclfqIibK4BEKMq13853xGUJrYrurToVX-CB2Y9lDWlWjCkik05cHCh_lUeL32h-qbV-IgLbXYFnddt3CO-dMfsK_WfxpqxN5aFSG-TLEzzuQWD0zeuQZcACqFZ-JIdRK.Db_NR2Ar5Od66uxAS6Mz3D4g_kTPHniccLYDsTAg9CyHNtDD5WbvuPLH34qhOTM5vyUvTe5WEE1G8ood_eP-OW3q5xgBmhzlUGELSM9OP-Ofex1xEOlSZtvyOW7SLuZP3Yrnyg6lcVxyAGWWdEd3hPISjlt7bgO6OAQg-OfISxGO5JlUQAIXy1gPs4xrOOsNqMeX5OBSgHuum1Yxe5B1OvZvyyyxSjOguMW_Ox___CtEQO_1R5EYxlOSkfE4x5tL4O1xJxeQE1I_NMQ4GoOtZaMSFwt3EqJW_O3VLM4OCN45d5SQZxSXQdITeQ7OVRr7dL4EqJ9OvZT5Omtl7Nj_O3_TTrEq8UVOPSxtEUOsnEKOkxEqMUO_1xCQDk8LyIhOIuk4mTTzs1f_UOZWER0.U1Yk0ZDqz2EjtTUhE252de5b8_R0IjLrkPQNkXjwVfKGUHY3njf0u1Y0Iybq0ZKGujYznfKWpyfqnHRk0AwGujYznH01rjD0UgfqnHmdnH60mhnqn6KEIhsqn10snj0kQHc0TZ0qn0KYIgnqnHn3rjnYnjckPjDYPjbvrjb1n0Kzug7Y5HDvn1DLrjmsnjcLP1D0Tv-b5HT3nhw-nAczP1csnvnYuW60TA3qnfKET1Yz0ZIG5Hf0uh3qPHRsPjbdnjPxmLKz0APYp1Y0IZRqIHmvnj6zPHc0mywWUA71T1Y0IAYqnWTdnHT1nH630A7Wpyfq0ZPbpdqv5fK1TL0qnfKYujYvPW03nWRz0APC5ykdgvP_XhG40A4YIZ0qn6K9TZKxTv-b5fKGIAYqn0KVIZ-suHYkrfK9uZw4TARqnH630A7YTA-b5H00mLKGujYknj0k0ZK_pyfqnHR1nH6kPHcsrHRdnsKWpA-b5fK9TZKvUWY0IA735fKVIZnqnHmdnH60UvPsm1Y1c1cWnznknW0snanznHcdc1cknWRWranWc108rj0sc108PjDscznWnanzc1D8nj0Wcznsc1DWnansg10Wninsc10WnHcsnj0Wnansc1DWni3snankQW0snankQW0snankQW0snansQW0snansQW0snankQW0sc10Wnansc10Wni3snjKxn7tkQW0sn7tkQW0snansc10WnanWnansg1D8nj0sg1Kxna3snjKxni3snjKxn7tsg1Kxna3snansc10Wn7tsg1Kxn7tsg1Kxna3snj0snjKxn7tkQW0snj0sn7tsg1D8nj0snj0sg1Kxn7tsQW0snj0sn7tsg1Kxna3snj0snjKxna3snj0snjKxn7tsg1Kxn7tsg1Kxni3snj0snj0Wn7tsg108nj0snj0sg1Kxn7ts0ZGJXjYs0ZGJXHYsQWfkn0KlpMCqna3YnH00XhGY5HD8nj0s0A-WIjYkPWnsPj6YrjT30AuBTWYsQW6sn0KYTWcqn0KhUZDqn0KluLDqn0KluLcqni3snj00mvFY5H00mMPY5HKxn7tsg1Kxn7tsg1Kxna3sn7tsQW0s0APBT1YkPWnsPj6Yn1Dvg1Kxn7tsg1fzrHnsrjRYPsKBTvcqn0KEIWY4QW08n0KsIjY1n1R1rfKsULPGIA-EUWYs0ZKETv-Ypyq8gvPCmy4MuNqzuy71Uv3qn0KETh-xUgfqnH63rj60UgwxTZfqn0K9mvPY5fKbmvPb5fKbmLFs5fKbuguYTjY0Tv3q0ZKzUvfq0AqWTAPxUA7BgLPYmgwdT1Ys0APYTWYknWn1P0KdmhYqn0KEmLKWgvP_pyPo5H0Wnansc10Wnansc1D8nj0sc1D8nj0s0AuYXgK-5H00myw1U-q15H00myw1U-qGT1Y0mhd_5H00UgKY5H00UgKYIWYs0Ad9m1Rq0Aq95fK9uAPo5H00UZfqn0K1m1Ys0AqW5HD0Ih-buyqGujYknjm3nWn4Pj60mhN1UjYs0A-1uAsqn0KEUAw_5H00TZFEuv7bIWYk0A71XHYs0A7bTZTqn1Ts0A7bTA6qnWfd0A-1TjdBphkk0A91UATqn00k5H00nWY0n1Y0PjY0PHYknj0snjD0PWYkPj0vP1DvP1RkP1fLPj6vrHRLnf0L5Hc0rjY1nHczP1D3P1m4rj60rHY0TZFEudqYT1YkP1bsnjRvrHm4n1n3PHD3Pjf4P0KsThqMgLK15HDvnHf3PWTdn103rjndnjfLnHcL0ZKzUvIxIAbqn1DznWTkrjTvrHbs0ZKzUvIxTAbq0ZKWpHYknHfvnjfdrjcdP1cYnWcdPW6sP0KWpybqn1DznWTkrjTsnHR40ZPJpjYzPHR0TMF15H00mMNYmyTqn0KBmL0qnfK8ugfqnfKzIADqn0K-TLfqn0K1Uy_q0APzm1YYP1Tz&word=1&xst=TjYs0ynq0ycqnWDkwWR1nRm4n1-DfWbswHIAfbn1Pbf3fWTvPbc3fbDKIHY1n104rHfYn6715H6vPHb3nWfLnHRdnWf4rjcsnj9xrj0Yg10Kmv6quhN-u0DYPHTYnj6drHb\\\",\\\"video_url\\\":\\\"http:\\\\/\\\\/nadvideo2.baidu.com\\\\/9dead27cf45cbee0f01554705fd6431b_1280_720.mp4\\\",\\\"videoid\\\":106823948},\\\"mts\\\":[16518],\\\"rule16518\\\":{\\\"links\\\":[]},\\\"version\\\":1}\",\"target_url\":\"https://aisite.wejianzhan.com/site/wjzt0r1w/c7282567-895e-409a-a79b-ed11fa88b776?fid=rjmdrH6zPjTkPHRzPjb3nW0sr7t3njwxnf&ch=3&bfid=fbuFw0nKSnfjToQ6Qg600afj0frzjEbK14WpVD6000axU7aYi0000KR0-s0H000l__UrtIxRYtb_EPQPGUoPkn0_Ee1KzeMlEnJl8V5EET12GVpbQnBodojnJtzodPJtYozYEtht4VpscfWrkPQNkXjwVH4kUrT\",\"position_step\":0,\"target_type\":1,\"cpm\":86338000,\"hot_key\":0,\"trans_num\":\"27人咨询\"},\"ad_extra_info\":{\"word\":\"文艺培训\",\"word_id\":5006,\"match_type\":19,\"atp_id\":0,\"fdmc_id\":\"\",\"pricesort_q\":563,\"price\":7,\"charge_method\":\"6\",\"feedback_url\":\"\",\"ad_brand\":\"国际汉语教师证\",\"second_industry_category\":\"\",\"product_type\":33539,\"asp_reqt\":1631786002771,\"feed_rewrite_query\":\"全民奇迹首充号\",\"mts\":\"16518\",\"position\":0,\"bid_type\":3,\"ocpc_level\":2,\"trans_type\":3,\"ori_bid\":12000,\"ocpc_bid\":12000,\"ocpc_trans_from\":2,\"is_ocpc_cancel_1stage\":true,\"ocpc_lab_status\":0,\"charge_mode\":0,\"subject\":\"429308547\",\"triggered_query\":\"\",\"pa_product_list\":\"\",\"is_ocpc_cancel_1stage_new\":1,\"ftype\":0,\"ori_mt_id\":18888,\"ztc_cpa_info\":\"{\\\"siteid\\\":55365015,\\\"sjhAppid\\\":255,\\\"usePublic\\\":1,\\\"videoid\\\":104864400}\",\"msa_pegasus_ctrq\":33539,\"title_sign\":17900569693385184494,\"brand_sign\":6135324580514217137,\"pay_type\":1,\"feed_csid_list\":\"16148675308835047127\",\"title_sign_str\":\"17900569693385184494\",\"brand_sign_str\":\"6135324580514217137\",\"videoid\":\"106823948\",\"gd_ext_info\":\"\",\"gd_expend\":\"\",\"article_ad_position\":0,\"device_id\":\"\",\"bes_level\":0,\"is_deeplink\":0,\"only_deeplink\":0,\"subject_sign\":\"429308547\",\"refresh_state\":\"-\",\"ad_pic_width\":370,\"ad_pic_height\":245,\"prog_title_id\":312271876990,\"is_pic_set\":0,\"is_prog\":1,\"prog_pic_id\":\"\",\"ori_ad_cpm\":0,\"video_sign_str\":\"14067167517474869571\",\"scene\":0,\"has_league\":0,\"is_ocpc_deep\":0,\"deep_trans_type\":0,\"deep_ocpc_bid\":0,\"app_info\":\"0\",\"android_id\":\"\",\"ori_qleft\":12334,\"ori_qright\":12334,\"bid\":8,\"roiq\":2125,\"prog_stage\":2,\"prog_video_sign\":\"14067167517474869571\",\"prog_strategy\":2,\"prog_video_id\":312271876988,\"media_id\":\"100001\",\"gd_speed\":0,\"video_duration\":0,\"sjh_appid\":255,\"bs_ctrq\":8000,\"prog_comb_id\":\"11460458257242256804\",\"mining_type\":0,\"asroiq_type\":0,\"ad_dup_reason\":1,\"ubmq\":0,\"pricing_type\":0,\"risk_control_trade_id\":0,\"bsdeeproiq_value\":0,\"rec_reason_sign\":\"0\",\"trade2\":0,\"hot_tag_sign\":\"0\",\"novel_adv_page_interval\":0,\"banner_adv_time_interval\":0,\"cali_price_q\":0,\"deep_bid\":0,\"shallow_bid\":0,\"ocpc_deep_bid_weight\":0.0,\"preconvq\":0,\"preconvq_bid_ratio\":1.0,\"feed_ad_entity_tag\":\"\",\"feed_ubmq_right\":0,\"ocpc_deep_from\":0,\"deep_ocpc_status\":0,\"floating_icon\":\"0\",\"floating_title\":\"0\",\"floating_subtitle\":\"0\",\"floating_button\":\"0\",\"is_rta\":false,\"com_idea_id\":312271870159,\"adv_quality_level\":2,\"cold_boot_tag\":0,\"is_bes_coldboot\":false,\"dynamic_interval_floor\":0,\"is_cache\":false,\"is_rta_use_cache\":false,\"bes_cold_boot_cpm_decay\":0,\"is_bes_cold_boot_rank_first\":false,\"feed_ad_interest_tag\":\"\",\"use_roi\":0,\"roi_ratio\":0,\"roi_ocpc_bid\":0,\"charge_name\":\"55049503_cpr\",\"boost_id\":0,\"boost_spend_budget\":0,\"eplay_check_time\":0.0,\"trade1_meg\":2019,\"trade1_meg_name\":\"教育培训\",\"unitid_created_time\":1630484316,\"boost_type\":0,\"boost_target_budget\":\"0\",\"boost_budget_cost\":\"0\",\"is_boost_budget\":false,\"boost_exit_status\":0,\"is_boost_adv\":false,\"boost_target_effect\":\"0|0|312271870159|0|0\",\"boost_cpm_delta\":\"0.0000\",\"boost_id_new\":\"0\",\"inter_tag\":0,\"dynamic_back_time_interval\":0,\"exposure_duration\":3600,\"reach_adjust_coe_tag\":0.0,\"ocpc_deep_feedback_coef\":1.0,\"ocpc_shallow_feedback_coef\":0.4099999964237213,\"reach_adjust_coe\":0.4099999964237213,\"dislike_qianka_trade1_meg\":2019,\"dislike_qianka_trade1_meg_name\":\"教育培训\",\"dislike_qianka_feed_ad_entity_tag\":\"\",\"form_front_sid\":\"\",\"bes_deviceid_pv\":-1,\"bes_support_type\":0,\"bes_support_cpm_decay\":0,\"adv_price_ratio\":1.0,\"ad_cpm_ratio\":1.0,\"adv_target_tag\":0,\"customer_id\":\"429308547\",\"doc_id\":\"0\",\"getui_applist_flag\":0,\"iad_ex_string\":\"\",\"bes_novel_price_tag\":0},\"res_extra_info\":{\"src_id\":1414,\"cmatch\":804,\"timestamp\":32}}",
                "template_id": ""
            },
            "dsp_id": "",
            "extra": [
                {
                    "k": "extraParam",
                    "v": "AFD52X3F1YWxpdHlfbGV2ZWwiOjIsImNvbGRfYm9vdF90YWciOjAsImJlc19uZXdfc2NlbmUiOjUsImNoYXJnZV9uYW1lIjoiNTUwNDk1MDNfY3ByIiwiYm9vc3RfaWQiOjAsImJvb3N0X3NwZW5kX2J1ZGdldCI6MCwiZGlkIjoyMTAzODEsImVwbGF5X2NoZWNrX3RpbWUiOjAuMCwiZHluYW1pY19pbnRlcnZhbF9mbG9vciI6MCwidHJhZGUxX21lZyI6MjAxOSwidHJhZGUxX21lZ19uYW1lIjoi5pWZ6IKy5Z+56K6tIiwiaW50ZXJfdGFnIjowLCJ1bml0aWRfY3JlYXRlZF90aW1lIjoxNjMwNDg0MzE2LCJib29zdF90eXBlIjowLCJib29zdF90YXJnZXRfYnVkZ2V0IjoiMCIsImJvb3N0X2J1ZGdldF9jb3N0IjoiMCIsImlzX2Jvb3N0X2J1ZGdldCI6ZmFsc2UsImJvb3N0X2V4aXRfc3RhdHVzIjowLCJpc19ib29zdF9hZHYiOmZhbHNlLCJib29zdF90YXJnZXRfZWZmZWN0IjoiMHwwfDMxMjI3MTg3MDE1OXwwfDAiLCJib29zdF9jcG1fZGVsdGEiOiIwLjAwMDAiLCJib29zdF9pZF9uZXciOiIwIiwiZHluYW1pY19iYWNrX3RpbWVfaW50ZXJ2YWwiOjAsImV4cG9zdXJlX2R1cmF0aW9uIjozNjAwLCJyZWFjaF9hZGp1c3RfY29lX3RhZyI6MC4wLCJvY3BjX2RlZXBfZmVlZGJhY2tfY29lZiI6MS4wLCJvY3BjX3NoYWxsb3dfZmVlZGJhY2tfY29lZiI6MC40MDk5OTk5OTY0MjM3MjEzLCJyZWFjaF9hZGp1c3RfY29lIjowLjQwOTk5OTk5NjQyMzcyMTMsImZlZWRfYWRfaW50ZXJlc3RfdGFnIjoiIiwiZGlzbGlrZV9xaWFua2FfdHJhZGUxX21lZyI6MjAxOSwiZGlzbGlrZV9xaWFua2FfdHJhZGUxX21lZ19uYW1lIjoi5pWZ6IKy5Z+56K6tIiwiZGlzbGlrZV9xaWFua2FfZmVlZF9hZF9lbnRpdHlfdGFnIjoiIiwiZm9ybV9mcm9udF9zaWQiOiIiLCJ1c2Vfcm9pIjowLCJyb2lfcmF0aW8iOjAsInJvaV9vY3BjX2JpZCI6MCwiY3VzdG9tZXJfaWQiOiI0MjkzMDg1NDciLCJkb2NfaWQiOiIwIiwiZ2V0dWlfYXBwbGlzdF9mbGFnIjowfQ==GUiOiItIiwiYWRfcGljX3dpZHRoIjozNzAsImFkX3BpY19oZWlnaHQiOjI0NSwib3JpX2FkX2NwbSI6MCwidmlkZW9fc2lnbl9zdHIiOiIxNDA2NzE2NzUxNzQ3NDg2OTU3MSIsImhhc19sZWFndWUiOjAsIm9yaV9xbGVmdCI6MTIzMzQsIm9yaV9xcmlnaHQiOjEyMzM0LCJjcGlkIjoxMDAxLCJsb2dpZCI6IjAiLCJmcm9tIjoiRkMiLCJwbGFjZV9pZCI6IjE1MzE4MTUyMDk1NTMiLCJpZGMiOiJ0YyIsIm5ldFR5cGUiOjEsInNlYXJjaF90aW1lIjoxNjMxNzg2MDAyLCJzZWFyY2hfaWQiOjg2NTk4MjQ3MTU1MjQ5ODIwMDgsImVpZF9saXN0IjoiIiwid2luZm9faWQiOiIzMTIyNjI4MTQ4NzkiLCJpZGVhX2lkIjoiMzEyMjcxODcwMTU5IiwidXNlcl9pZCI6MzMwOTk0NDIsInBsYW5faWQiOjE2NTk4NzQ4NiwidW5pdF9pZCI6NjE0MDU0NjU2OCwicGwiOjE2NTk4NzQ4NiwidW4iOjYxNDA1NDY1NjgsImFkX2NwbSI6ODYzMzgsImFkX3R5cGUiOjE4OCwiYWRfZmxhZyI6MiwicmFuayI6MSwiY20iOjgwNCwic3JjIjoxNDE0LCJwb3NpdGlvbl9zdGVwIjowLCJwdiI6MjEsImN0IjoxNTEsImFkaWQiOiIzMTIyNjI4MTQ4NzkiLCJ1c2VyaWQiOjMzMDk5NDQyLCJjbWF0Y2giOjgwNCwibXQiOiIxNjUxOCIsImFkX3ByaWNlIjo3LCJhc3FfcmVxdCI6MTYzMTc4NjAwMjc3MSwiY2xpY2tfdXJsIjoiIiwiZm1pZCI6IiIsInRyaWdnZXJfd29yZCI6IuaWh+iJuuWfueiurSIsImRhX21lbnUxIjoidTY2MDgyNTIiLCJmZWVkX2NvdW50IjowLCJmcmVzaFR5cGUiOjIsImZyZXNoQ291bnQiOjAsIm92aWRfZWlkX2xpc3QiOiIzMDAwMDEtMiM0MDA0NS0xIzU3MjU4LTEjNzA4NjItZHojNzQ0MDMtZHojNzQ3MDEtMSM3NDcxMy0zIiwicGtfY3BtIjo4Ni4zMzgsInNpcCI6IjE3NS4xNDcuMjIuMTI1IiwiZmVlZF9yZXdyaXRlX3F1ZXJ5Ijoi5YWo5rCR5aWH6L+56aaW5YWF5Y+3IiwicHJpY2UiOjEsInJlcV9udW0iOjE1LCJwcm9kdWN0X2lkIjoyMiwiYWZkX3RyYW5zX2RhdGEiOnsic2hvd25fa2V5IjoiMjJfMV8yMTFGNTMxRjkzOURCOTBFN0ZCQzM2RDhCNzY2QjhCQSIsInRpdGxlX3NpZ24iOiIxNzkwMDU2OTY5MzM4NTE4NDQ5NCIsImJyYW5kX3NpZ24iOiI2MTM1MzI0NTgwNTE0MjE3MTM3In0sInBhc3Nwb3J0SWQiOiJBRkQxPUE9TSIsImRhX21lbnUyIjoiMjc1MTczMTg4IiwicHJpY2luZ190eXBlIjowLCJpc19wcm9nIjoxLCJub3ZlbF9hZHZfcGFnZV9pbnRlcnZhbCI6MCwiYmFubmVyX2Fkdl90aW1lX2ludGVydmFsIjowLCJhcHBfaW5mbyI6IjAiLCJpc19vY3BjX2RlZXAiOjAsImRlZXBfdHJhbnNfdHlwZSI6MCwiZGVlcF9vY3BjX2JpZCI6MCwic2poX2FwcGlkIjoyNTUsImZsb2F0aW5nX2ljb24iOiIwIiwiZmxvYXRpbmdfdGl0bGUiOiIwIiwiZmxvYXRpbmdfc3VidGl0bGUiOiIwIiwiZmxvYXRpbmdfYnV0dG9uIjoiMCIsImFuZHJvaWRfaWQiOiIiLCJwcm9nX3RpdGxlX2lkIjozMTIyNzE4NzY5OTAsImlzX3BpY19zZXQiOjAsImJpZCI6OCwicm9pcSI6MjEyNSwicHJvZ19zdGFnZSI6MiwicHJvZ192aWRlb19zaWduIjoiMTQwNjcxNjc1MTc0NzQ4Njk1NzEiLCJwcm9nX3N0cmF0ZWd5IjoyLCJwcm9nX3ZpZGVvX2lkIjozMTIyNzE4NzY5ODgsIm1lZGlhX2lkIjoiMTAwMDAxIiwidmlkZW9fZHVyYXRpb24iOjAsImJzX2N0cnEiOjgwMDAsInByb2dfY29tYl9pZCI6IjExNDYwNDU4MjU3MjQyMjU2ODA0IiwibWluaW5nX3R5cGUiOjAsImFzcm9pcV90eXBlIjowLCJhZF9kdXBfcmVhc29uIjoxLCJ1Ym1xIjowLCJyaXNrX2NvbnRyb2xfdHJhZGVfaWQiOjAsInJlY19yZWFzb25fc2lnbiI6IjAiLCJ0cmFkZTIiOjAsImhvdF90YWdfc2lnbiI6IjAiLCJjYWxpX3ByaWNlX3EiOjAsImZlZWRfYWRfZW50aXR5X3RhZyI6IiIsImRlZXBfb2NwY19zdGF0dXMiOjAsInByb2dfcGljX2lkIjoiIiwidWlfZnJvbSI6NCwiaXNfcnRhIjpmYWxzZSwiYWReyJ3b3JkX2lkIjo1MDA2LCJtYXRjaF90eXBlIjoxOSwiYXRwX2lkIjowLCJwcmljZXNvcnRfcSI6NTYzLCJjaGFyZ2VfbWV0aG9kIjoiNiIsImFkX2JyYW5kIjoi5Zu96ZmF5rGJ6K+t5pWZ5biI6K+BIiwic2Vjb25kX2luZHVzdHJ5X2NhdGVnb3J5IjoiIiwicHJvZHVjdF90eXBlIjozMzUzOSwibXRzIjoiMTY1MTgiLCJwb3NpdGlvbiI6MCwiYmlkX3R5cGUiOjMsIm9jcGNfbGV2ZWwiOjIsInRyYW5zX3R5cGUiOjMsIm9yaV9iaWQiOjEyMDAwLCJvY3BjX2JpZCI6MTIwMDAsIm9jcGNfdHJhbnNfZnJvbSI6MiwiaXNfb2NwY19jYW5jZWxfMXN0YWdlIjp0cnVlLCJvY3BjX2xhYl9zdGF0dXMiOjAsImNoYXJnZV9tb2RlIjowLCJzdWJqZWN0IjoiNDI5MzA4NTQ3IiwidHJpZ2dlcmVkX3F1ZXJ5IjoiIiwicGFfcHJvZHVjdF9saXN0IjoiIiwiaXNfb2NwY19jYW5jZWxfMXN0YWdlX25ldyI6MSwiZnR5cGUiOjAsIm9yaV9tdF9pZCI6MTg4ODgsInp0Y19jcGFfaW5mbyI6IntcInNpdGVpZFwiOjU1MzY1MDE1LFwic2poQXBwaWRcIjoyNTUsXCJ1c2VQdWJsaWNcIjoxLFwidmlkZW9pZFwiOjEwNDg2NDQwMH0iLCJtc2FfcGVnYXN1c19jdHJxIjozMzUzOSwidGl0bGVfc2lnbiI6MTc5MDA1Njk2OTMzODUxODQ0OTQsImJyYW5kX3NpZ24iOjYxMzUzMjQ1ODA1MTQyMTcxMzcsInBheV90eXBlIjoxLCJmZWVkX2NzaWRfbGlzdCI6IjE2MTQ4Njc1MzA4ODM1MDQ3MTI3IiwidGl0bGVfc2lnbl9zdHIiOiIxNzkwMDU2OTY5MzM4NTE4NDQ5NCIsImJyYW5kX3NpZ25fc3RyIjoiNjEzNTMyNDU4MDUxNDIxNzEzNyIsInZpZGVvaWQiOiIxMDY4MjM5NDgiLCJnZF9leHRfaW5mbyI6IiIsImdkX2V4cGVuZCI6IiIsImFydGljbGVfYWRfcG9zaXRpb24iOjAsImRldmljZV9pZCI6IiIsImJlc19sZXZlbCI6MCwiaXNfZGVlcGxpbmsiOjAsIm9ubHlfZGVlcGxpbmsiOjAsInN1YmplY3Rfc2lnbiI6IjQyOTMwODU0NyIsInJlZnJlc2hfc3Rhd"
                }
            ],
            "rank_tag": 2,
            "little_video_list": []
        },
```
```
{
    "ad_base_info": {
        "rank": 6,
        "idea_id": 153322092908,
        "winfo_id": 153322092895,
        "user_id": 27724717,
        "plan_id": 119123968,
        "unit_id": 4484081768,
        "ad_cpm": 1513083,
        "ad_type": 187,
        "ad_flag": 1,
        "title": "16538现在9块9能充话费100元！这活动力度真的没谁了，不抢太亏！",
        "desc1": "DFT",
        "desc2": "",
        "rcv_url": "http://cq01-cs-anti-remora14.cq01.baidu.com:8765/baidu.php?url=af0000KJY7PAPBPmEJ4vqJs7TR5tUxVpvSoDtepSI8cjajCFSGMe7zOOfY9WX1lWdPqvTXnNMFdRe8Iwa9UPy5iHiIhnhfPRLHVwt-VeP3Ogo0WFq1hjEUz6ICgIP2fPgydhgsD.DR_NR2Ar5Od66Y8ExwH4g_3_acZYDlXq1CTHAHGlX5uu_oRtjr5-3cd9h9m3vIh1cC0.U1Yk0ZDqE2S1zTXqsSUg_nor__HK1e1U85D0IjLgzVAv0A-V5HRYPfKM5fKdpHY0TA-b5Hf0mv-b5HDkn0KVIjYkPWRzPfKBm1Yk0AVG5H00uy-b5fKBpHY0Uynq0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0KEIhsqnH0snj0dPaYkg1Dsnj0sPHmVnNtknj0snjRLQH7xn10snj0kQHD0mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5fKbuAqs5fKzpWYs0ZPl5fKYIgnqnHb4PHbLPHcdP1fLPjmdrj6dn0Kzug7Y5HDdP1TkP1n3njndnH60Tv-b5H0snyn1nhcLuAN-uynYn1D0TA3qn0KET1Yz0AdYXgK-5Hn0mywYXgK-5HD3PsK9IZKGujYs0APspyfqnH0snfKsUA-b5HDYPWc3PHnznjnLrHD0mv9GujYk0A7sTZu85HDkQWD1QW08nH00IA735fKVIZnqnHmdnWR0UvPsm1Y1c1DWPanvnj0sc10WnanYPinWc1D8nj0sc1D8nj0scznWnankc108nj0snj0sg1cWcznsc1DWnansc10WPjcWnandnansc10WninkQW0sc1D8nj0sc1D8nj0sc108nj0sc108nj0sc108nj0sc1D8nj0Wnansc10WnankQW0snansc10WnanWnansc100TZfqnfKsULPGIA-EUWYY0ZKETv-Ypyq8gvPCmy4MuNqzuy71Uv3qPsKETh-xUgfqnHmdnWR0UgwxTZfqn0K9mvPY5fKbmvPb5HbYwDu7fbDvPHKKrjRswWDvnYnvfWP7nWb1rHIanY77xjR1PHT4nWc1nj6vrHRvr0KbmLFs5fKbuguYTjY0Tv3q0ZKzUvfq0AqWTAPxUA7BgLPYmgwdT1Ys0AqWTAPxmvkGmv_qnansc10Wnansc10Wni3snj0Wni3snj00uMw4TARqnfK9uZP8gLnqn0K9uZP8gv-15fKBUysqn0KVmynd5HcYnj9WP1DsrHTLnHTLrjDduW0kuhFWn1fYuANbm19B0Aq95fK9uAPo5H00UZfqn0K1m1Ys0ZuGuANEpyfqnWTLrj64P1D0mhN1UjYs0A-1uAsqnfKEUAw_5H00TZFEuv7bIWYs0A71XHYs0A7bTZTqnHDYn0K9uZKC5HmYn0KGTL0qmLf0pZP_u1Ys0jDqPjDsPWTknjD3nj0sPj6dn1b40jcqrjTkPHczmvPbPAc3nyu-n0015H6vPHbvrj01nWc4P1R1Pf0Y5RwNizdKHjcs0jRqn00v5H00P1Ys0j6qn0045fKsThqMgLw15HT1rH6LPHb1PHcYPWndnHRzP1D0TZFEudqsT1YvnWc4rHRLPWDLn1DdnjR1njTd0ZKzUvIxIAbqn0KsThqMgLKG5fKsmvbqnHndPjbYrjT4PjTdnHn3PHm0TvGC5HcdPfKBIgw9u1Yk0A4-IjYY0APzm1YzrjR4P6&ck=__CPC_ANTI_CK__",
        "show_url": "DFT",
        "mt_newstyle": "{\"mts\":[16540],\"idea16540\":{\"apk_name\":\"com.jingdong.app.mall\",\"app_name\":null,\"bes_trade_id\":202202,\"doc_id\":null,\"dump_title\":\" \",\"exposure_url_type\":1,\"isSmartUrl\":false,\"item\":[{\"height\":1920,\"url\":\"https://feed-image.baidu.com/0/pic/721238428_-108975812_-1124910856.jpg\",\"width\":1080}],\"monitor_url\":\"https://ccc-x.jd.com/dsp/media?delivery_system_type=10&v=713&event_type=2&idfa=NULL&imei_md5=NULL&oaid=NULL&oaid_md5=NULL&caid=%5B%7B%22caid%22%3A%5B%7B%22caid%22%3A%2200_EAFC1BF933ED1C62E6E8EE1D4BB1F337_B414E9FD07CBBA2D580CA49E47289006%22%2C%22version%22%3A%2200%22%7D%5D%2C%22generateTime%22%3A%221764032431%22%2C%22vendor%22%3A%220%22%7D%2C%7B%22caid%22%3A%5B%7B%22caid%22%3A%22f701cd57b18a864dc38de87e9befb555%22%2C%22version%22%3A%2220230330%22%7D%2C%7B%22caid%22%3A%224a684ea04660788860092661e1bcee60%22%2C%22version%22%3A%2220250325%22%7D%5D%2C%22generateTime%22%3A%221764032431%22%2C%22vendor%22%3A%221%22%7D%5D&ua=Mozilla%2F5%2E0+%28iPhone%3B+CPU+iPhone+OS+26%5F0%5F1+like+Mac+OS+X%29+AppleWebKit%2F605%2E1%2E15+%28KHTML%2C+like+Gecko%29+Mobile%2F15E148&media_click_time={{TS}}&user_ip=2409:8a3c:1611:a0e1:41:c5b8:af96:82ab&ip_type=v6&media_advertiser_id=68805293&media_campaign_id=1221302851&os=1&media_adgroup_id=12473547576&media_ad_id=1197068885917&sku_id={{PRODUCT_ID}}&mac1_md5=NULL&external_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&utm_source=baidu-ys&media_trace_id=068aa730ccba7122&request_id=6908578967182354418&ocpc_callback_url={{CALLBACK_URL}}&mid=0&media_click_id=068aa730ccba71224c6_1197068885917&sk_ocpc_convert_type=11&akey=Njg4MDUyOTM=\",\"monitor_url_type\":1,\"mt\":16540,\"na_url\":\"openapp.jdmobile://virtual?params=%7B%22category%22%3A%22jump%22%2C%22des%22%3A%22m%22%2C%22url%22%3A%22https%3A%2F%2Funion%2Dclick%2Ejd%2Ecom%2Fsem%2Ephp%3Fsource%3Dbaidu%2Dys%26unionId%3D262767352%26siteId%3Dbaiduys_1197068885917%26sk_os%3D1%26sk_request_id%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26sk_trace_id%3D068aa730ccba7122%26to%3Dhttps%253A%252F%252Fre.m.jd.com%252Fitem%252F10086969111818.html%253Fad_od%253D3%2526re_dcp%253DwUmutbkHvgyR-bcPUMXyCA%2526bd_vid%253DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%22%2C%22m_param%22%3A%7B%22jdv%22%3A%22null%7Cbaidu%2Dys%7Ct_262767352_baiduys%7Ccpc%7C1197068885917_0_1197068885917baiduys%22%7D%2C%22kepler_param%22%3A%7B%22source%22%3A%22kepler%2Dopen%22%2C%22channel%22%3A%22b4dc3278288f4a25982ccdec07ebdc41%22%7D%2C%22keplerFrom%22%3A%221%22%2C%22keplerID%22%3A%22%22%7D\",\"ori_img\":\"https://feed-image.baidu.com/0/pic/721238428_-108975812_-1124910856.jpg\",\"ori_landing_url\":\"https://union-click.jd.com/sem.php?source=baidu-ys&unionId=262767352&siteId=baiduys_1197068885917&sk_os=1&sk_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&sk_trace_id=068aa730ccba7122&to=https%3A%2F%2Fre.m.jd.com%2Fitem%2F10086969111818.html%3Fad_od%3D3%26re_dcp%3DwUmutbkHvgyR-bcPUMXyCA%26bd_vid%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL\",\"poster\":null,\"realMaterialStyle\":null,\"reserved\":{\"hasGif\":null,\"sjhAppid\":null,\"tit_t\":0,\"usePublic\":0},\"title\":\"精选推荐\",\"ulkScheme\":\"openapp.jdmobile://\",\"ulkUrl\":\"https://linkst.m.jd.com/ul/ul.action?openapp.jdmobile://virtual?params=%7B%22category%22%3A%22jump%22%2C%22des%22%3A%22m%22%2C%22url%22%3A%22https%3A%2F%2Funion%2Dclick%2Ejd%2Ecom%2Fsem%2Ephp%3Fsource%3Dbaidu%2Dys%26unionId%3D262767352%26siteId%3Dbaiduys_1197068885917%26sk_os%3D1%26sk_request_id%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26sk_trace_id%3D068aa730ccba7122%26to%3Dhttps%253A%252F%252Fre.m.jd.com%252Fitem%252F10086969111818.html%253Fad_od%253D3%2526re_dcp%253DwUmutbkHvgyR-bcPUMXyCA%2526bd_vid%253DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%22%2C%22m_param%22%3A%7B%22jdv%22%3A%22null%7Cbaidu%2Dys%7Ct_262767352_baiduys%7Ccpc%7C1197068885917_0_1197068885917baiduys%22%7D%2C%22kepler_param%22%3A%7B%22source%22%3A%22kepler%2Dopen%22%2C%22channel%22%3A%22b4dc3278288f4a25982ccdec07ebdc41%22%7D%2C%22keplerFrom%22%3A%221%22%2C%22keplerID%22%3A%22%22%7D\",\"url\":\"https://union-click.jd.com/sem.php?source=baidu-ys&unionId=262767352&siteId=baiduys_1197068885917&sk_os=1&sk_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&sk_trace_id=068aa730ccba7122&to=https%3A%2F%2Fre.m.jd.com%2Fitem%2F10086969111818.html%3Fad_od%3D3%26re_dcp%3DwUmutbkHvgyR-bcPUMXyCA%26bd_vid%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL\",\"user_icon\":\"\",\"user_name\":\"京东\",\"user_portrait\":\"https://feed-image.baidu.com/0/pic/-898471769_1360572184_1746933561.jpg\",\"user_portrait_id\":12658457314,\"video_target_rcv_url\":null,\"video_url\":null,\"videoid\":null},\"rule16540\":{\"links\":[]},\"version\":1}",
        "target_url": "https://mobile.baidu.com/item?docid=26634081",
        "position_step": 3
    },
    "ad_extra_info": {
        "word": "资讯",
        "word_id": 3,
        "match_type": 3,
        "atp_id": 0,
        "fdmc_id": "8367658966223100182",
        "pricesort_q": 4585,
        "price": 33,
        "charge_method": "7",
        "feedback_url": "https://at.pinduoduo.com/a/baidu?userid=27724717&aid=153322092908&pid=119123968&uid=4484081768&callback_url={{CALLBACK_URL}}&click_id={{CLICK_ID}}&idfa=NULL&imei_md5=faf5a17ffeac8416e7613f2ef0f1bdb1&ip=223.104.64.82&ip_type=v4&ua=okhttp%2F3.11.0+Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+9%3B+DUK-AL20+Build%2FHUAWEIDUK-AL20%29+baiduboxapp%2F11.13.0.10+%28Baidu%3B+P1+9%29&os=2&ts={{TS}}&sign={{SIGN}}&media_id=0&product_id={{PRODUCT_ID}}&oaid_md5=NULL&akey=Mjc3MjQ3MTc=",
        "ad_brand": "拼多多-充话费",
        "second_industry_category": "生活食材",
        "product_type": 1,
        "asp_reqt": 1577173803518,
        "feed_rewrite_query": "集成墙面装饰材料价格",
        "mts": "16538",
        "position": 4,
        "bid_type": 3,
        "ocpc_level": 1,
        "trans_type": 4,
        "ori_bid": 50,
        "ocpc_bid": 6000,
        "ocpc_trans_from": 1,
        "is_ocpc_cancel_1stage": false,
        "ocpc_lab_status": 0,
        "charge_mode": 0,
        "subject": "428037823",
        "triggered_query": "",
        "pa_product_list": "",
        "is_ocpc_cancel_1stage_new": 0,
        "ftype": 1,
        "ori_mt_id": 16538,
        "ztc_cpa_info": "{\"tit_t\":0,\"usePublic\":0,\"videoid\":27788971}",
        "msa_pegasus_ctrq": 1,
        "title_sign": 7398759352463516000,
        "brand_sign": 2021044165387781600,
        "pay_type": 1,
        "feed_csid_list": "6229957617315053075",
        "title_sign_str": "7398759352463515271",
        "brand_sign_str": "2021044165387781607",
        "videoid": "27788971",
        "gd_ext_info": "",
        "gd_expend": "",
        "article_ad_position": 0,
        "device_id": "865968032297535",
        "bes_level": 0,
        "is_deeplink": 1,
        "only_deeplink": 0,
        "subject_sign": "428037823",
        "refresh_state": "4",
        "ad_pic_width": 1140,
        "ad_pic_height": 640,
        "ori_ad_cpm": 1513083,
        "video_sign_str": "13454858827620169693",
        "has_league": 0,
        "is_ocpc_deep": 0,
        "deep_trans_type": 0,
        "deep_ocpc_bid": 0,
        "app_info": "410671018000485399",
        "android_id": "871522ccd4b81fe0",
        "ori_qleft": 35281,
        "ori_qright": 45851,
        "bid": 45,
        "roiq": 0,
        "media_id": "0",
        "video_duration": 0,
        "sjh_appid": 255,
        "bs_ctrq": 15000,
        "mining_type": 42,
        "asroiq_type": 1,
        "ubmq": 30009,
        "pricing_type": 0,
        "risk_control_trade_id": 0
    },
    "res_extra_info": {
        "src_id": 1416,
        "cmatch": 806,
        "timestamp": 56
    }
}
```
```
{
    "mts": [
        16540
    ],
    "idea16540": {
        "apk_name": "com.jingdong.app.mall",
        "app_name": null,
        "bes_trade_id": 202202,
        "doc_id": null,
        "dump_title": " ",
        "exposure_url_type": 1,
        "isSmartUrl": false,
        "item": [
            {
                "height": 1920,
                "url": "https://feed-image.baidu.com/0/pic/721238428_-108975812_-1124910856.jpg",
                "width": 1080
            }
        ],
        "monitor_url": "https://ccc-x.jd.com/dsp/media?delivery_system_type=10&v=713&event_type=2&idfa=NULL&imei_md5=NULL&oaid=NULL&oaid_md5=NULL&caid=%5B%7B%22caid%22%3A%5B%7B%22caid%22%3A%2200_EAFC1BF933ED1C62E6E8EE1D4BB1F337_B414E9FD07CBBA2D580CA49E47289006%22%2C%22version%22%3A%2200%22%7D%5D%2C%22generateTime%22%3A%221764032431%22%2C%22vendor%22%3A%220%22%7D%2C%7B%22caid%22%3A%5B%7B%22caid%22%3A%22f701cd57b18a864dc38de87e9befb555%22%2C%22version%22%3A%2220230330%22%7D%2C%7B%22caid%22%3A%224a684ea04660788860092661e1bcee60%22%2C%22version%22%3A%2220250325%22%7D%5D%2C%22generateTime%22%3A%221764032431%22%2C%22vendor%22%3A%221%22%7D%5D&ua=Mozilla%2F5%2E0+%28iPhone%3B+CPU+iPhone+OS+26%5F0%5F1+like+Mac+OS+X%29+AppleWebKit%2F605%2E1%2E15+%28KHTML%2C+like+Gecko%29+Mobile%2F15E148&media_click_time={{TS}}&user_ip=2409:8a3c:1611:a0e1:41:c5b8:af96:82ab&ip_type=v6&media_advertiser_id=68805293&media_campaign_id=1221302851&os=1&media_adgroup_id=12473547576&media_ad_id=1197068885917&sku_id={{PRODUCT_ID}}&mac1_md5=NULL&external_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&utm_source=baidu-ys&media_trace_id=068aa730ccba7122&request_id=6908578967182354418&ocpc_callback_url={{CALLBACK_URL}}&mid=0&media_click_id=068aa730ccba71224c6_1197068885917&sk_ocpc_convert_type=11&akey=Njg4MDUyOTM=",
        "monitor_url_type": 1,
        "mt": 16540,
        "na_url": "openapp.jdmobile://virtual?params=%7B%22category%22%3A%22jump%22%2C%22des%22%3A%22m%22%2C%22url%22%3A%22https%3A%2F%2Funion%2Dclick%2Ejd%2Ecom%2Fsem%2Ephp%3Fsource%3Dbaidu%2Dys%26unionId%3D262767352%26siteId%3Dbaiduys_1197068885917%26sk_os%3D1%26sk_request_id%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26sk_trace_id%3D068aa730ccba7122%26to%3Dhttps%253A%252F%252Fre.m.jd.com%252Fitem%252F10086969111818.html%253Fad_od%253D3%2526re_dcp%253DwUmutbkHvgyR-bcPUMXyCA%2526bd_vid%253DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%22%2C%22m_param%22%3A%7B%22jdv%22%3A%22null%7Cbaidu%2Dys%7Ct_262767352_baiduys%7Ccpc%7C1197068885917_0_1197068885917baiduys%22%7D%2C%22kepler_param%22%3A%7B%22source%22%3A%22kepler%2Dopen%22%2C%22channel%22%3A%22b4dc3278288f4a25982ccdec07ebdc41%22%7D%2C%22keplerFrom%22%3A%221%22%2C%22keplerID%22%3A%22%22%7D",
        "ori_img": "https://feed-image.baidu.com/0/pic/721238428_-108975812_-1124910856.jpg",
        "ori_landing_url": "https://union-click.jd.com/sem.php?source=baidu-ys&unionId=262767352&siteId=baiduys_1197068885917&sk_os=1&sk_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&sk_trace_id=068aa730ccba7122&to=https%3A%2F%2Fre.m.jd.com%2Fitem%2F10086969111818.html%3Fad_od%3D3%26re_dcp%3DwUmutbkHvgyR-bcPUMXyCA%26bd_vid%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL",
        "poster": null,
        "realMaterialStyle": null,
        "reserved": {
            "hasGif": null,
            "sjhAppid": null,
            "tit_t": 0,
            "usePublic": 0
        },
        "title": "精选推荐",
        "ulkScheme": "openapp.jdmobile://",
        "ulkUrl": "https://linkst.m.jd.com/ul/ul.action?openapp.jdmobile://virtual?params=%7B%22category%22%3A%22jump%22%2C%22des%22%3A%22m%22%2C%22url%22%3A%22https%3A%2F%2Funion%2Dclick%2Ejd%2Ecom%2Fsem%2Ephp%3Fsource%3Dbaidu%2Dys%26unionId%3D262767352%26siteId%3Dbaiduys_1197068885917%26sk_os%3D1%26sk_request_id%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26sk_trace_id%3D068aa730ccba7122%26to%3Dhttps%253A%252F%252Fre.m.jd.com%252Fitem%252F10086969111818.html%253Fad_od%253D3%2526re_dcp%253DwUmutbkHvgyR-bcPUMXyCA%2526bd_vid%253DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%22%2C%22m_param%22%3A%7B%22jdv%22%3A%22null%7Cbaidu%2Dys%7Ct_262767352_baiduys%7Ccpc%7C1197068885917_0_1197068885917baiduys%22%7D%2C%22kepler_param%22%3A%7B%22source%22%3A%22kepler%2Dopen%22%2C%22channel%22%3A%22b4dc3278288f4a25982ccdec07ebdc41%22%7D%2C%22keplerFrom%22%3A%221%22%2C%22keplerID%22%3A%22%22%7D",
        "url": "https://union-click.jd.com/sem.php?source=baidu-ys&unionId=262767352&siteId=baiduys_1197068885917&sk_os=1&sk_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&sk_trace_id=068aa730ccba7122&to=https%3A%2F%2Fre.m.jd.com%2Fitem%2F10086969111818.html%3Fad_od%3D3%26re_dcp%3DwUmutbkHvgyR-bcPUMXyCA%26bd_vid%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL",
        "user_icon": "",
        "user_name": "京东",
        "user_portrait": "https://feed-image.baidu.com/0/pic/-898471769_1360572184_1746933561.jpg",
        "user_portrait_id": 12658457314,
        "video_target_rcv_url": null,
        "video_url": null,
        "videoid": null
    },
    "rule16540": {
        "links": []
    },
    "version": 1
}
```
### 生成器代码
```
const idea16515 = require('./16515.json');
const idea16540 = require('./16540.json');
const idea10008 = require('./10008.json');

// 原生广告
const feed_ad = {
    "ad_type": 2,
    "ad_info": {
        "info": "{\"ad_base_info\":{\"rank\":6,\"idea_id\":153322092908,\"winfo_id\":153322092895,\"user_id\":27724717,\"plan_id\":119123968,\"unit_id\":4484081768,\"ad_cpm\":1513083,\"ad_type\":187,\"ad_flag\":1,\"title\":\"16532\u73b0\u57289\u57579\u80fd\u5145\u8bdd\u8d39100\u5143\uff01\u8fd9\u6d3b\u52a8\u529b\u5ea6\u771f\u7684\u6ca1\u8c01\u4e86\uff0c\u4e0d\u62a2\u592a\u4e8f\uff01\",\"desc1\":\"DFT\",\"desc2\":\"\",\"rcv_url\":\"http://cq01-cs-anti-remora14.cq01.baidu.com:8765/baidu.php?url=af0000KJY7PAPBPmEJ4vqJs7TR5tUxVpvSoDtepSI8cjajCFSGMe7zOOfY9WX1lWdPqvTXnNMFdRe8Iwa9UPy5iHiIhnhfPRLHVwt-VeP3Ogo0WFq1hjEUz6ICgIP2fPgydhgsD.DR_NR2Ar5Od66Y8ExwH4g_3_acZYDlXq1CTHAHGlX5uu_oRtjr5-3cd9h9m3vIh1cC0.U1Yk0ZDqE2S1zTXqsSUg_nor__HK1e1U85D0IjLgzVAv0A-V5HRYPfKM5fKdpHY0TA-b5Hf0mv-b5HDkn0KVIjYkPWRzPfKBm1Yk0AVG5H00uy-b5fKBpHY0Uynq0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0KEIhsqnH0snj0dPaYkg1Dsnj0sPHmVnNtknj0snjRLQH7xn10snj0kQHD0mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5fKbuAqs5fKzpWYs0ZPl5fKYIgnqnHb4PHbLPHcdP1fLPjmdrj6dn0Kzug7Y5HDdP1TkP1n3njndnH60Tv-b5H0snyn1nhcLuAN-uynYn1D0TA3qn0KET1Yz0AdYXgK-5Hn0mywYXgK-5HD3PsK9IZKGujYs0APspyfqnH0snfKsUA-b5HDYPWc3PHnznjnLrHD0mv9GujYk0A7sTZu85HDkQWD1QW08nH00IA735fKVIZnqnHmdnWR0UvPsm1Y1c1DWPanvnj0sc10WnanYPinWc1D8nj0sc1D8nj0scznWnankc108nj0snj0sg1cWcznsc1DWnansc10WPjcWnandnansc10WninkQW0sc1D8nj0sc1D8nj0sc108nj0sc108nj0sc108nj0sc1D8nj0Wnansc10WnankQW0snansc10WnanWnansc100TZfqnfKsULPGIA-EUWYY0ZKETv-Ypyq8gvPCmy4MuNqzuy71Uv3qPsKETh-xUgfqnHmdnWR0UgwxTZfqn0K9mvPY5fKbmvPb5HbYwDu7fbDvPHKKrjRswWDvnYnvfWP7nWb1rHIanY77xjR1PHT4nWc1nj6vrHRvr0KbmLFs5fKbuguYTjY0Tv3q0ZKzUvfq0AqWTAPxUA7BgLPYmgwdT1Ys0AqWTAPxmvkGmv_qnansc10Wnansc10Wni3snj0Wni3snj00uMw4TARqnfK9uZP8gLnqn0K9uZP8gv-15fKBUysqn0KVmynd5HcYnj9WP1DsrHTLnHTLrjDduW0kuhFWn1fYuANbm19B0Aq95fK9uAPo5H00UZfqn0K1m1Ys0ZuGuANEpyfqnWTLrj64P1D0mhN1UjYs0A-1uAsqnfKEUAw_5H00TZFEuv7bIWYs0A71XHYs0A7bTZTqnHDYn0K9uZKC5HmYn0KGTL0qmLf0pZP_u1Ys0jDqPjDsPWTknjD3nj0sPj6dn1b40jcqrjTkPHczmvPbPAc3nyu-n0015H6vPHbvrj01nWc4P1R1Pf0Y5RwNizdKHjcs0jRqn00v5H00P1Ys0j6qn0045fKsThqMgLw15HT1rH6LPHb1PHcYPWndnHRzP1D0TZFEudqsT1YvnWc4rHRLPWDLn1DdnjR1njTd0ZKzUvIxIAbqn0KsThqMgLKG5fKsmvbqnHndPjbYrjT4PjTdnHn3PHm0TvGC5HcdPfKBIgw9u1Yk0A4-IjYY0APzm1YzrjR4P6&ck=__CPC_ANTI_CK__\",\"show_url\":\"DFT\",\"mt_newstyle\":\"{\\\"mts\\\": [16532], \\\"idea16532\\\": {\\\"reserved\\\": {\\\"sjhAppid\\\": null, \\\"tit_t\\\": 0, \\\"usePublic\\\": 0, \\\"videoid\\\": 27788971}, \\\"app_name\\\": \\\"\\\\u9650\\\\u65f6\\\\u7279\\\\u60e0\\\", \\\"video_url\\\": \\\"http://nadvideo.baidu.com/14790aa9f455e77222124f8f5809af40_1280_720_mp4.mp4\\\", \\\"item\\\": [{\\\"url\\\": \\\"https://feed-image.baidu.com/0/pic/1062195400_1759853955_26977759.jpg\\\", \\\"width\\\": 1140, \\\"height\\\": 640}], \\\"apk_name\\\": \\\"com.xunmeng.pinduoduo\\\", \\\"app_id\\\": \\\"5695136\\\", \\\"ios_client_version\\\": \\\"11.13.0.10\\\", \\\"jump_url\\\": \\\"https://mobile.baidu.com/item?docid=26634081\\\", \\\"na_url\\\": \\\"pddopen://?appKey=4b5749f97a514035a74e830388f32a71&packageId={{DEEPLINK_PACKAGENAME}}&backUrl={{DEEPLINK_BACKURL}}&h5Url=mtr_portals.html%3F_pdd_tc%3Dffffff%26_pdd_fs%3D1%26x_id%3D119%26_pdd_sbs%3D1%26lego_type%3Dv3%26sn%3D190902o4sk%26thomas_id%3Dad_land%26_pdd_nc%3DF52B4A%26lego_minversion%3D4.71.0%26_p_ads_channel%3Dbaidu%26_oc_ads_channel%3Dbaidu%26_p_ads_type%3Dlaxin%26_p_launch_type%3Dadv%26account_id%3D27724717%26_p_ads_set%3D119123968%26_p_ads_id%3D4484081768\\\", \\\"duration\\\": 9, \\\"subtitle\\\": \\\"\\\\u9650\\\\u65f6\\\\u7279\\\\u60e0\\\", \\\"monitor_url\\\": \\\"https://at.pinduoduo.com/a/baidu?userid=27724717&aid=153322092908&pid=119123968&uid=4484081768&callback_url={{CALLBACK_URL}}&click_id={{CLICK_ID}}&idfa=NULL&imei_md5=faf5a17ffeac8416e7613f2ef0f1bdb1&ip=223.104.64.82&ip_type=v4&ua=okhttp%2F3.11.0+Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+9%3B+DUK-AL20+Build%2FHUAWEIDUK-AL20%29+baiduboxapp%2F11.13.0.10+%28Baidu%3B+P1+9%29&os=2&ts={{TS}}&sign={{SIGN}}&media_id=0&product_id={{PRODUCT_ID}}&oaid_md5=NULL&akey=Mjc3MjQ3MTc=\\\", \\\"app_url\\\": \\\"https://api.pinduoduo.com/api/app/channel/pinduoduo_baidufeed_latest.apk\\\", \\\"title\\\": \\\"\\\\u73b0\\\\u57289\\\\u57579\\\\u80fd\\\\u5145\\\\u8bdd\\\\u8d39100\\\\u5143\\\\uff01\\\\u8fd9\\\\u6d3b\\\\u52a8\\\\u529b\\\\u5ea6\\\\u771f\\\\u7684\\\\u6ca1\\\\u8c01\\\\u4e86\\\\uff0c\\\\u4e0d\\\\u62a2\\\\u592a\\\\u4e8f\\\\uff01\\\", \\\"user_portrait\\\": \\\"http://aod-image.baidu.com/5/pic/c7e54c44ec07a52bfa4e2818d4240619.jpg\\\", \\\"exposure_url\\\": null, \\\"videoid\\\": 27788971, \\\"user_icon\\\": \\\"\\\", \\\"app_version\\\": \\\"4.84.0\\\", \\\"user_name\\\": \\\"\\\\u62fc\\\\u591a\\\\u591a-\\\\u5145\\\\u8bdd\\\\u8d39\\\", \\\"poster\\\": \\\"http://aod-image.baidu.com/5/pic/67de519c4d18c6e93c4be6338f549f16.jpg\\\", \\\"url_type\\\": \\\"3\\\", \\\"android_client_version\\\": \\\"9\\\", \\\"ori_landing_url\\\": \\\"https://mobile.baidu.com/item?docid=26634081\\\", \\\"firm_name\\\": \\\"\\\", \\\"mt\\\": 16532, \\\"isSmartUrl\\\": false, \\\"doc_id\\\": \\\"26634081\\\"}, \\\"version\\\": 1, \\\"rule16532\\\": {\\\"links\\\": []}}\",\"target_url\":\"https://mobile.baidu.com/item?docid=26634081\",\"position_step\":3},\"ad_extra_info\":{\"word\":\"\u8d44\u8baf\",\"word_id\":3,\"match_type\":3,\"atp_id\":0,\"fdmc_id\":\"8367658966223100182\",\"pricesort_q\":4585,\"price\":33,\"charge_method\":\"7\",\"feedback_url\":\"https://at.pinduoduo.com/a/baidu?userid=27724717&aid=153322092908&pid=119123968&uid=4484081768&callback_url={{CALLBACK_URL}}&click_id={{CLICK_ID}}&idfa=NULL&imei_md5=faf5a17ffeac8416e7613f2ef0f1bdb1&ip=223.104.64.82&ip_type=v4&ua=okhttp%2F3.11.0+Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+9%3B+DUK-AL20+Build%2FHUAWEIDUK-AL20%29+baiduboxapp%2F11.13.0.10+%28Baidu%3B+P1+9%29&os=2&ts={{TS}}&sign={{SIGN}}&media_id=0&product_id={{PRODUCT_ID}}&oaid_md5=NULL&akey=Mjc3MjQ3MTc=\",\"ad_brand\":\"\u62fc\u591a\u591a-\u5145\u8bdd\u8d39\",\"second_industry_category\":\"\u751f\u6d3b\u98df\u6750\",\"product_type\":1,\"asp_reqt\":1577173803518,\"feed_rewrite_query\":\"\u96c6\u6210\u5899\u9762\u88c5\u9970\u6750\u6599\u4ef7\u683c\",\"mts\":\"16532\",\"position\":4,\"bid_type\":3,\"ocpc_level\":1,\"trans_type\":4,\"ori_bid\":50,\"ocpc_bid\":6000,\"ocpc_trans_from\":1,\"is_ocpc_cancel_1stage\":false,\"ocpc_lab_status\":0,\"charge_mode\":0,\"subject\":\"428037823\",\"triggered_query\":\"\",\"pa_product_list\":\"\",\"is_ocpc_cancel_1stage_new\":0,\"ftype\":1,\"ori_mt_id\":16532,\"ztc_cpa_info\":\"{\\\"tit_t\\\":0,\\\"usePublic\\\":0,\\\"videoid\\\":27788971}\",\"msa_pegasus_ctrq\":1,\"title_sign\":7398759352463516000,\"brand_sign\":2021044165387781600,\"pay_type\":1,\"feed_csid_list\":\"6229957617315053075\",\"title_sign_str\":\"7398759352463515271\",\"brand_sign_str\":\"2021044165387781607\",\"videoid\":\"27788971\",\"gd_ext_info\":\"\",\"gd_expend\":\"\",\"article_ad_position\":0,\"device_id\":\"865968032297535\",\"bes_level\":0,\"is_deeplink\":1,\"only_deeplink\":0,\"subject_sign\":\"428037823\",\"refresh_state\":\"4\",\"ad_pic_width\":1140,\"ad_pic_height\":640,\"ori_ad_cpm\":1513083,\"video_sign_str\":\"13454858827620169693\",\"has_league\":0,\"is_ocpc_deep\":0,\"deep_trans_type\":0,\"deep_ocpc_bid\":0,\"app_info\":\"410671018000485399\",\"android_id\":\"871522ccd4b81fe0\",\"ori_qleft\":35281,\"ori_qright\":45851,\"bid\":45,\"roiq\":0,\"media_id\":\"0\",\"video_duration\":0,\"sjh_appid\":255,\"bs_ctrq\":15000,\"mining_type\":42,\"asroiq_type\":1,\"ubmq\":30009,\"pricing_type\":0,\"risk_control_trade_id\":0},\"res_extra_info\":{\"src_id\":1416,\"cmatch\":806,\"timestamp\":56}}",
        "template_id": ""
    },
    "module_type": 0,
    "client_type": 0,
    "page_type": null,
    "dsp_id": "",
    "extra": [
        {
            "k": "extraParam",
            "v": "MVlkvkSgy11Lm6bPpJ/Ba4uyPaYIw1+HYclWLk3mO2mx11yiKjKHEpCypj2mdrbFiRxakaFZOwBDgky6YgA2KIguWTuNlU4FxhVMk4N05149D+aYyHYdCQc9iJablMBuBqm/YfaEdHvOMd0JlUfrAHDYF1h4yjRoHadzIQV07woJS5EcqPXITcbIyg/UUa1wwyf41LTl28zpUmBOTqfX6uza2hH0kqALTvf7N+MSNPNBU7W1/2Ap1v8H05wjjONAX773NBFgM3WwMwLMxTgAf1IYtL11V+LFlPZq23mMlTTXxb2Pmjb/9cM+g7dSWIEceZ3bM0SHjoUeo1tPYsxSfEbVX7AzPNRObd2bnRqXEeLUCV2N6/tHkjvBC8Rw0DgcVh4dp1nGmBAnVmSRTTgvxRm1wfj5HrLERSKxSc2t17pO+WWvEFEjsMmpAjohDkx054Ciyywu3jXzZYG9Y3wpxYrbznVFWKM1+nSd+ucuijP1Qdp54HuzMPBODRCOtzcDu/hzPPgb59e2t6eJFGT3hHPd/awAME3Eobe7SScz8LUZcmZ5FSCvtqL/5fyp8TaeeTkl5OguurrZvVLxWEvay0ubps+kn8FrxL8qfMVHxzoGAMsk0BH+27BUy8NfNcFi8E4NEI63NwNgIAgq3mEmtEtfvlFAv3jKV6I53oqK0sHR2X522fU/rljmszjVkTKrLtP2zlLwdMBrrapOjUe6DuBDzygxovIdG50l/qwKXynHGI31eT9uZoqUcvkFsa6atreniRRk94Rz3f2sADBNxIeCX3j4b5k7JtO662asYRJY270sTzTJIm9Iifj/aZz5w9aEmZa9UbjJmuFJtwiaWxm1wfj5HrLE7rBUwC4fK0lP+v7pzE0wxq5NZQannyR01CYy0tgYQ2JyrX3jRGbq1n/VtraT2f4gOO1R0bvIl/u12JGaeNdOJLXuDqr58nmqGR/cNXGcB1GfJRsk5u8xR+X1xcMX+beuw0AuNdfMaQgm5PAY+FxYI+POUW6MUVVY8rrFmpo4BTGGsCF9IpoQOzHUMkX4C61S81Edoty2uyW6YAW5hFgP5FE0H7i5dnrG14mZrFlQm61G/IGNr9jJu8KimQXG1+7Mrvrh1MCoO30dkq5ykKbNDYYtw5baJh+pFreCogKranYTmE/GLQSKxxaSCG4X5RH1BnDZS8CfBrY="
        }
    ]
};
// 其中feed_ad中的具体内容，feed_ad.ad_info.ad_info
const feed_ad_detail = {
    "ad_base_info": {
        "rank": 6,
        "idea_id": 153322092908,
        "winfo_id": 153322092895,
        "user_id": 27724717,
        "plan_id": 119123968,
        "unit_id": 4484081768,
        "ad_cpm": 1513083,
        "ad_type": 187,
        "ad_flag": 1,
        "title": "现在9块9能充话费100元！这活动力度真的没谁了，不抢太亏！",
        "desc1": "DFT",
        "desc2": "",
        "rcv_url": "http://cq01-cs-anti-remora14.cq01.baidu.com:8765/baidu.php?url=af0000KJY7PAPBPmEJ4vqJs7TR5tUxVpvSoDtepSI8cjajCFSGMe7zOOfY9WX1lWdPqvTXnNMFdRe8Iwa9UPy5iHiIhnhfPRLHVwt-VeP3Ogo0WFq1hjEUz6ICgIP2fPgydhgsD.DR_NR2Ar5Od66Y8ExwH4g_3_acZYDlXq1CTHAHGlX5uu_oRtjr5-3cd9h9m3vIh1cC0.U1Yk0ZDqE2S1zTXqsSUg_nor__HK1e1U85D0IjLgzVAv0A-V5HRYPfKM5fKdpHY0TA-b5Hf0mv-b5HDkn0KVIjYkPWRzPfKBm1Yk0AVG5H00uy-b5fKBpHY0Uynq0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0KEIhsqnH0snj0dPaYkg1Dsnj0sPHmVnNtknj0snjRLQH7xn10snj0kQHD0mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5fKbuAqs5fKzpWYs0ZPl5fKYIgnqnHb4PHbLPHcdP1fLPjmdrj6dn0Kzug7Y5HDdP1TkP1n3njndnH60Tv-b5H0snyn1nhcLuAN-uynYn1D0TA3qn0KET1Yz0AdYXgK-5Hn0mywYXgK-5HD3PsK9IZKGujYs0APspyfqnH0snfKsUA-b5HDYPWc3PHnznjnLrHD0mv9GujYk0A7sTZu85HDkQWD1QW08nH00IA735fKVIZnqnHmdnWR0UvPsm1Y1c1DWPanvnj0sc10WnanYPinWc1D8nj0sc1D8nj0scznWnankc108nj0snj0sg1cWcznsc1DWnansc10WPjcWnandnansc10WninkQW0sc1D8nj0sc1D8nj0sc108nj0sc108nj0sc108nj0sc1D8nj0Wnansc10WnankQW0snansc10WnanWnansc100TZfqnfKsULPGIA-EUWYY0ZKETv-Ypyq8gvPCmy4MuNqzuy71Uv3qPsKETh-xUgfqnHmdnWR0UgwxTZfqn0K9mvPY5fKbmvPb5HbYwDu7fbDvPHKKrjRswWDvnYnvfWP7nWb1rHIanY77xjR1PHT4nWc1nj6vrHRvr0KbmLFs5fKbuguYTjY0Tv3q0ZKzUvfq0AqWTAPxUA7BgLPYmgwdT1Ys0AqWTAPxmvkGmv_qnansc10Wnansc10Wni3snj0Wni3snj00uMw4TARqnfK9uZP8gLnqn0K9uZP8gv-15fKBUysqn0KVmynd5HcYnj9WP1DsrHTLnHTLrjDduW0kuhFWn1fYuANbm19B0Aq95fK9uAPo5H00UZfqn0K1m1Ys0ZuGuANEpyfqnWTLrj64P1D0mhN1UjYs0A-1uAsqnfKEUAw_5H00TZFEuv7bIWYs0A71XHYs0A7bTZTqnHDYn0K9uZKC5HmYn0KGTL0qmLf0pZP_u1Ys0jDqPjDsPWTknjD3nj0sPj6dn1b40jcqrjTkPHczmvPbPAc3nyu-n0015H6vPHbvrj01nWc4P1R1Pf0Y5RwNizdKHjcs0jRqn00v5H00P1Ys0j6qn0045fKsThqMgLw15HT1rH6LPHb1PHcYPWndnHRzP1D0TZFEudqsT1YvnWc4rHRLPWDLn1DdnjR1njTd0ZKzUvIxIAbqn0KsThqMgLKG5fKsmvbqnHndPjbYrjT4PjTdnHn3PHm0TvGC5HcdPfKBIgw9u1Yk0A4-IjYY0APzm1YzrjR4P6&ck=__CPC_ANTI_CK__",
        "show_url": "DFT",
        "mt_newstyle": "{\"mts\":[16538], \"idea16538\":{\"reserved\":{\"sjhAppid\":null, \"tit_t\":0, \"usePublic\":0, \"videoid\":27788971}, \"app_name\":\"\\u9650\\u65f6\\u7279\\u60e0\", \"video_url\":\"http://nadvideo.baidu.com/14790aa9f455e77222124f8f5809af40_1280_720_mp4.mp4\", \"item\":[{\"url\":\"http://aod-image.baidu.com/5/pic/67de519c4d18c6e93c4be6338f549f16.jpg\", \"width\":1140, \"height\":640}], \"apk_name\":\"com.xunmeng.pinduoduo\", \"app_id\":\"5695136\", \"ios_client_version\":\"11.13.0.10\", \"jump_url\":\"https://mobile.baidu.com/item?docid=26634081\", \"na_url\":\"pddopen://?appKey=4b5749f97a514035a74e830388f32a71&packageId={{DEEPLINK_PACKAGENAME}}&backUrl={{DEEPLINK_BACKURL}}&h5Url=mtr_portals.html%3F_pdd_tc%3Dffffff%26_pdd_fs%3D1%26x_id%3D119%26_pdd_sbs%3D1%26lego_type%3Dv3%26sn%3D190902o4sk%26thomas_id%3Dad_land%26_pdd_nc%3DF52B4A%26lego_minversion%3D4.71.0%26_p_ads_channel%3Dbaidu%26_oc_ads_channel%3Dbaidu%26_p_ads_type%3Dlaxin%26_p_launch_type%3Dadv%26account_id%3D27724717%26_p_ads_set%3D119123968%26_p_ads_id%3D4484081768\", \"duration\":9, \"subtitle\":\"\\u9650\\u65f6\\u7279\\u60e0\", \"monitor_url\":\"https://at.pinduoduo.com/a/baidu?userid=27724717&aid=153322092908&pid=119123968&uid=4484081768&callback_url={{CALLBACK_URL}}&click_id={{CLICK_ID}}&idfa=NULL&imei_md5=faf5a17ffeac8416e7613f2ef0f1bdb1&ip=223.104.64.82&ip_type=v4&ua=okhttp%2F3.11.0+Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+9%3B+DUK-AL20+Build%2FHUAWEIDUK-AL20%29+baiduboxapp%2F11.13.0.10+%28Baidu%3B+P1+9%29&os=2&ts={{TS}}&sign={{SIGN}}&media_id=0&product_id={{PRODUCT_ID}}&oaid_md5=NULL&akey=Mjc3MjQ3MTc=\", \"app_url\":\"https://api.pinduoduo.com/api/app/channel/pinduoduo_baidufeed_latest.apk\", \"title\":\"\\u73b0\\u57289\\u57579\\u80fd\\u5145\\u8bdd\\u8d39100\\u5143\\uff01\\u8fd9\\u6d3b\\u52a8\\u529b\\u5ea6\\u771f\\u7684\\u6ca1\\u8c01\\u4e86\\uff0c\\u4e0d\\u62a2\\u592a\\u4e8f\\uff01\", \"user_portrait\":\"http://aod-image.baidu.com/5/pic/c7e54c44ec07a52bfa4e2818d4240619.jpg\", \"exposure_url\":null, \"videoid\":27788971, \"user_icon\":\"\", \"app_version\":\"4.84.0\", \"user_name\":\"\\u62fc\\u591a\\u591a-\\u5145\\u8bdd\\u8d39\", \"poster\":\"http://aod-image.baidu.com/5/pic/67de519c4d18c6e93c4be6338f549f16.jpg\", \"url_type\":\"3\", \"android_client_version\":\"9\", \"ori_landing_url\":\"https://mobile.baidu.com/item?docid=26634081\", \"firm_name\":\"\", \"mt\":16538, \"isSmartUrl\":false, \"doc_id\":\"26634081\"}, \"version\":1, \"rule16538\":{\"links\":[]}}",
        "target_url": "https://mobile.baidu.com/item?docid=26634081",
        "position_step": 3
    },
    "ad_extra_info": {
        "word": "资讯",
        "word_id": 3,
        "match_type": 3,
        "atp_id": 0,
        "fdmc_id": "8367658966223100182",
        "pricesort_q": 4585,
        "price": 33,
        "charge_method": "7",
        "feedback_url": "https://at.pinduoduo.com/a/baidu?userid=27724717&aid=153322092908&pid=119123968&uid=4484081768&callback_url={{CALLBACK_URL}}&click_id={{CLICK_ID}}&idfa=NULL&imei_md5=faf5a17ffeac8416e7613f2ef0f1bdb1&ip=223.104.64.82&ip_type=v4&ua=okhttp%2F3.11.0+Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+9%3B+DUK-AL20+Build%2FHUAWEIDUK-AL20%29+baiduboxapp%2F11.13.0.10+%28Baidu%3B+P1+9%29&os=2&ts={{TS}}&sign={{SIGN}}&media_id=0&product_id={{PRODUCT_ID}}&oaid_md5=NULL&akey=Mjc3MjQ3MTc=",
        "ad_brand": "拼多多-充话费",
        "second_industry_category": "生活食材",
        "product_type": 1,
        "asp_reqt": 1577173803518,
        "feed_rewrite_query": "集成墙面装饰材料价格",
        "mts": "16538",
        "position": 4,
        "bid_type": 3,
        "ocpc_level": 1,
        "trans_type": 4,
        "ori_bid": 50,
        "ocpc_bid": 6000,
        "ocpc_trans_from": 1,
        "is_ocpc_cancel_1stage": false,
        "ocpc_lab_status": 0,
        "charge_mode": 0,
        "subject": "428037823",
        "triggered_query": "",
        "pa_product_list": "",
        "is_ocpc_cancel_1stage_new": 0,
        "ftype": 1,
        "ori_mt_id": 16538,
        "ztc_cpa_info": "{\"tit_t\":0,\"usePublic\":0,\"videoid\":27788971}",
        "msa_pegasus_ctrq": 1,
        "title_sign": 7398759352463516000,
        "brand_sign": 2021044165387781600,
        "pay_type": 1,
        "feed_csid_list": "6229957617315053075",
        "title_sign_str": "7398759352463515271",
        "brand_sign_str": "2021044165387781607",
        "videoid": "27788971",
        "gd_ext_info": "",
        "gd_expend": "",
        "article_ad_position": 0,
        "device_id": "865968032297535",
        "bes_level": 0,
        "is_deeplink": 1,
        "only_deeplink": 0,
        "subject_sign": "428037823",
        "refresh_state": "4",
        "ad_pic_width": 1140,
        "ad_pic_height": 640,
        "ori_ad_cpm": 1513083,
        "video_sign_str": "13454858827620169693",
        "has_league": 0,
        "is_ocpc_deep": 0,
        "deep_trans_type": 0,
        "deep_ocpc_bid": 0,
        "app_info": "410671018000485399",
        "android_id": "871522ccd4b81fe0",
        "ori_qleft": 35281,
        "ori_qright": 45851,
        "bid": 45,
        "roiq": 0,
        "media_id": "0",
        "video_duration": 0,
        "sjh_appid": 255,
        "bs_ctrq": 15000,
        "mining_type": 42,
        "asroiq_type": 1,
        "ubmq": 30009,
        "pricing_type": 0,
        "risk_control_trade_id": 0
    },
    "res_extra_info": {
        "src_id": 1416,
        "cmatch": 806,
        "timestamp": 56
    }
};
// 具体物料的信息，feed_ad_detail.ad_base_info.mt_newstyle
const feed_ad_detail_item = {
    "mts": [
        16538
    ],
    "idea16538": {
        "reserved": {
            "sjhAppid": null,
            "tit_t": 0,
            "usePublic": 0,
            "videoid": 27788971
        },
        "app_name": "限时特惠",
        "video_url": "http://nadvideo.baidu.com/14790aa9f455e77222124f8f5809af40_1280_720_mp4.mp4",
        "item": [
            {
                "url": "http://aod-image.baidu.com/5/pic/67de519c4d18c6e93c4be6338f549f16.jpg",
                "width": 1140,
                "height": 640
            }
        ],
        "apk_name": "com.xunmeng.pinduoduo",
        "app_id": "5695136",
        "ios_client_version": "11.13.0.10",
        "jump_url": "https://mobile.baidu.com/item?docid=26634081",
        "na_url": "pddopen://?appKey=4b5749f97a514035a74e830388f32a71&packageId={{DEEPLINK_PACKAGENAME}}&backUrl={{DEEPLINK_BACKURL}}&h5Url=mtr_portals.html%3F_pdd_tc%3Dffffff%26_pdd_fs%3D1%26x_id%3D119%26_pdd_sbs%3D1%26lego_type%3Dv3%26sn%3D190902o4sk%26thomas_id%3Dad_land%26_pdd_nc%3DF52B4A%26lego_minversion%3D4.71.0%26_p_ads_channel%3Dbaidu%26_oc_ads_channel%3Dbaidu%26_p_ads_type%3Dlaxin%26_p_launch_type%3Dadv%26account_id%3D27724717%26_p_ads_set%3D119123968%26_p_ads_id%3D4484081768",
        "duration": 9,
        "subtitle": "限时特惠",
        "monitor_url": "https://at.pinduoduo.com/a/baidu?userid=27724717&aid=153322092908&pid=119123968&uid=4484081768&callback_url={{CALLBACK_URL}}&click_id={{CLICK_ID}}&idfa=NULL&imei_md5=faf5a17ffeac8416e7613f2ef0f1bdb1&ip=223.104.64.82&ip_type=v4&ua=okhttp%2F3.11.0+Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+9%3B+DUK-AL20+Build%2FHUAWEIDUK-AL20%29+baiduboxapp%2F11.13.0.10+%28Baidu%3B+P1+9%29&os=2&ts={{TS}}&sign={{SIGN}}&media_id=0&product_id={{PRODUCT_ID}}&oaid_md5=NULL&akey=Mjc3MjQ3MTc=",
        "app_url": "https://api.pinduoduo.com/api/app/channel/pinduoduo_baidufeed_latest.apk",
        "title": "现在9块9能充话费100元！这活动力度真的没谁了，不抢太亏！",
        "user_portrait": "http://aod-image.baidu.com/5/pic/c7e54c44ec07a52bfa4e2818d4240619.jpg",
        "exposure_url": null,
        "videoid": 27788971,
        "user_icon": "",
        "app_version": "4.84.0",
        "user_name": "拼多多-充话费",
        "poster": "http://aod-image.baidu.com/5/pic/67de519c4d18c6e93c4be6338f549f16.jpg",
        "url_type": "3",
        "android_client_version": "9",
        "ori_landing_url": "https://mobile.baidu.com/item?docid=26634081",
        "firm_name": "",
        "mt": 16538,
        "isSmartUrl": false,
        "doc_id": "26634081"
    },
    "version": 1,
    "rule16538": {
        "links": []
    }
}
// 凤巢广告
const fc_ad = {
    "ad_type": 1,
    "ad_info": {
        "info": "{\"title\":\"广告1 idea10008凤巢单图 淘宝零食实惠不停全场低至3元9件，限时秒杀快...\", \"recom_reason\":\"秒杀0.1折起\", \"user_portrait\":\"https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/103450ee-ec1a-47a3-8519-a7841c4c5ce0\", \"desc\":\"中国<font color=\\\"#CC0000\\\">鲜花</font>中国鲜花,完美的信誉,顶尖的服务,鲜花,免费送货热线:400-800-2610,1-3小时送达全国\",\"url\":\"京东\",\"link\":\"https://m.baidu.com/baidu.php?url=K00000K3Zd4fCW_uEVFYJhlJ4E0B89A-S8TYumnp2_-9mrpfs3jSdpHiPkVNtgdXkvl4oSHmqq5-2aT1kbuYl9SVfbvB44Mx8NvBXYO4NF0PxNWZWyxb4drcY0yv4Hv67RCLosWRKFK27J2Fi-M2by6M0zeFSaNspW2CCvPPH6gJQy_4upEwfmIgyWR6cZ3SWd-phbfygEDyKrZADke3cCyJuxl0.7b_iHF8xnhA94wEYL_SNK-deQbfHgI3ynDgg6msw5I7AMHdeyQleEZWYqMHEovpS5Zkol3vPrM-zI5HkzuPv1-3eorzEFb4XrHI8eQPMWdEmORSOzOBXTx4SZHgJOr1Zsu5qoNOvr_UZgykNfCm3t5Zv3TMds45o6C_kgXNK-deQbmTMdWHGY3TMdCgkGuh9JstxonMgWkmX5zYlXgFYq5ZFbLUrgW8_e2thH-34Pve__vXrZFYqJIZ0lpejkSyZF8tSMjbLUqSZF8qxU9zUE5u9zUVMZjbLXEzs4PLM8s4PLVttrHIlqrZF8tqvZF8qptrHI_LmThe1tTrHIltTrHIlS8ZF8tOZjbLXEo9zUVOds4PLM8s4PLVttrHI_L3The1vmThevtTrHI_LmTMHxjzll5QZPj93OFhBOi1Gu4mYlXyoIzlI5QblXMWbzUVMQkLyI-XHFztTheIvyU57mhPXzA8l4POQjWhyAp7WFb3470.U1Ykn0Kk5U1i1pgyktHT_Q2LsnSd1Un0mywkXHvtY_v-d_xDLQazVtj5VTv10A7bTgfqn6KspynqnfKY5IUZkPztYoeH1egP_eazde00pyYqrjR10ATqILPYT6KdpHY0TA-b5HDY0APGujY1nWf0Ugfqrj0snj7xnH0snjuxnW0dnfKopHYs0ZFY5HmYn6KBpHYznjuxnW03g1RsndtLnjPxP10Yg1csnj0zg1csnjnk0AdW5HKxn7tznjRk0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5HD0ThCqn0KhIjYz0ZKC5H00ULnqn6KBI1YY0A4Y5HD0TLCq0A71gv-bm1dsTzd-mvC0pywW5fKspZw45fKYmgFMugfqn17xn1Dzg1b0IZN15HDvP1m3P1csnHmsnWT3rHTkPjnk0ZF-TgfqnHm1P1fvnH6LnHmznfK8IZws5Hn0mv6qUZNxmvklpMb0IZRqP1mkPj6sPfK15yw-rA7WmHw-uAn4rH0LnhD0IAYqn0KWuWYk0ZFB5HD0UZNopHYk0AP8IA3quW9WnywbuyFxmLKz0ZP1TjYz0ZP1Tjcqn0KYIZ0qnsKbIZ0qn6KGIAYqn0K9uAP_mgP15HD10A7bXjYs0ZPbpdqv5HD0IvbqP0KhTvPCUyfqn6KYujYs0AkdT1YLmyRvmvnzP1bsP1TvujTk0AkdTLfqPWD4ry7-uWD0UZNWIjYvnHb4mymvu6K1mvRqnsK_INqGuAnqUhCsn6KvUWY3nj0d0A7sT7q1pyfquW9Wnywbuyc0uMcqnHf0TLcqn1cY0AF-TvsqQHD0UZNLIZcqPWndnWfLP1TYrjfznjmYn1R3PsKYTh7buHDqn0KYTh7buHcqn0K-XZKGujYznjDLn1NxnW0znHc4g1csnWc1n7tznjczPWuxnW0znWb4g1csnWf4n-tznjndPjwxnW0vPH0zg1csPWm4ndtznj6krHFxnW04rjTY0ZNzUjdCIZwsrBtEPAFbmWw9QidhrAnkuAw-mB4WUvYE0A-Vuy-xUyfd5HDsPHmLuHTYuhf3mvNBnAubPjnsrH6kuHPWrHD3mHD40ZPGujdhnAR4rjb3Pvf1nHf3PW790AP1UHd7nDmYwWN7PbckPjNAPHPA0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg100uA78IyF-gLK_my4GuZnqn7tsg100TA7Ygvu_myTqn0KsThqb5HDznWTsnjD1PjTY0APY5iY0uAPGujY10ANYpyfqPWf0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0A7buhk9u1Yk0Akhm1Ys0AwWmvfqnb7APHm1wHmsnDmLwWR4wWm3nWbzPYn4nYc4PHmYwbwtn0KYTh7buHYs0AFbpyfqrjPKfW0dPW9DwjuafYDdfbRzf1uAwDDzPjTdfWDdfbR0IvuzUvYq0AFY5H00Uv7YI1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wnansc1nWna3snj0snj0Wni3snj0knj00uAkxIA7M5HD0TNqv5H08PH9xna3sn7tsQW0sg108njKxna3sndtkQW0sg108nWNxn0KBTdqsThqbpyfqn0KzUv-hUA7M5H00mLmq0A-1gvPsmHYs0APs5H00ugPY5H00mLFW5HRsnWcz&us=newvui&ai=0_429107157_1&word=&qid=f0e98987d314861a&bdrank=9&rank=10&sourceid=1400&placeid=1#dplk=tbopen://m.taobao.com/tbopen/index.html?source=alimama_bd_sem_feeds&bc_fl_src=alimama_sem_mm_26632258_3504122_32554087&action=ali.open.nav&module=h5&bootImage=0&appkey=24532550&appName=%C3%A7%C2%99%C2%BE%C3%A5%C2%BA%C2%A6&backURL=baiduboxapp://&h5Url=http://redirect.simba.taobao.com/rd?c=un&w=unionsem&k=b1d73646918f3371&p=mm_26632258_3504122_32554087&b=GIDMEsQzm1gQasw2JgY&s=&f=https%3A%2F%2Fuland.taobao.com%2Fsemm%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32554087%26keyword%3D%25E6%2599%25BA%25E8%2583%25BD%25E5%25AE%25B6%25E5%25B1%2585%25E7%25B3%25BB%25E7%25BB%259F%25E5%25AE%2589%25E8%25A3%2585%26bc_fl_src%3Dalimama_sem_h5_mm_26632258_3504122_32554087\",\"style\":{\"idea1017\":{},\"idea10008\":{\"image\":\"https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/27291187-b673-4ee3-b53b-9fcfc5f8e7b4\", \"link\":\"http://www.baidu.com\",\"price\":\"1219\",\"ori_price\":\"2000\",\"name\":\"小米手机’小米手机小米手机小米手机小米手机小米手机\",\"tags\":\"9.6英寸高清大屏，清晰护眼！4800 mAh大电池，长续航追剧一整天！【限时直降50元】限时直降50\",\"attributes\":\"麟980 AI处理器，3D仿生感光技术智能识别人脸，后置2400万 AI三摄，40W安全超级快充，石墨烯散热技术带来畅快游戏体验。【到手价：4499元】限时优惠800元，下单再减500元，再赠价值268元礼包（荣耀音乐小巨蛋+二合一数据线），一降到底！\",\"sales_volume\":\"满意度99%\",\"seller_name\":\"京东\",\"display_type\":\"0\"}},\"general_data\":{\"cpm\":4500080000,\"bidword\":\"各种花朵\",\"search_id\":\"7deaf65d964e86a8\",\"from\":\"FC\",\"word_id\":119291861,\"ad_type\":131072,\"extra_type\":0,\"ip\":\"172.10.4.5\",\"winfo_id\":1523719733,\"idea_id\":24493271524,\"user_id\":30553688,\"plan_id\":68977154,\"unit_id\":68977154,\"rank\":0,\"ad_price\":104,\"baiduid\":\"79FDBBC5D9034AD629968C5391F7D14E\",\"passport\":0,\"ovlexp_id_list\":\"\",\"cmatch\":822,\"wmatch\":63,\"search_time\":\"1534497213\"}}"
    },
    "extra": []
};

const fc_ad_detail = {
    "title": "广告1 idea10008凤巢单图 淘宝零食实惠不停全场低至3元9件，限时秒杀快...",
    "recom_reason": "秒杀0.1折起",
    "user_portrait": "https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/103450ee-ec1a-47a3-8519-a7841c4c5ce0",
    "desc": "中国<font color=\"#CC0000\">鲜花</font>中国鲜花,完美的信誉,顶尖的服务,鲜花,免费送货热线:400-800-2610,1-3小时送达全国",
    "url": "京东",
    "link": "https://m.baidu.com/baidu.php?url=K00000K3Zd4fCW_uEVFYJhlJ4E0B89A-S8TYumnp2_-9mrpfs3jSdpHiPkVNtgdXkvl4oSHmqq5-2aT1kbuYl9SVfbvB44Mx8NvBXYO4NF0PxNWZWyxb4drcY0yv4Hv67RCLosWRKFK27J2Fi-M2by6M0zeFSaNspW2CCvPPH6gJQy_4upEwfmIgyWR6cZ3SWd-phbfygEDyKrZADke3cCyJuxl0.7b_iHF8xnhA94wEYL_SNK-deQbfHgI3ynDgg6msw5I7AMHdeyQleEZWYqMHEovpS5Zkol3vPrM-zI5HkzuPv1-3eorzEFb4XrHI8eQPMWdEmORSOzOBXTx4SZHgJOr1Zsu5qoNOvr_UZgykNfCm3t5Zv3TMds45o6C_kgXNK-deQbmTMdWHGY3TMdCgkGuh9JstxonMgWkmX5zYlXgFYq5ZFbLUrgW8_e2thH-34Pve__vXrZFYqJIZ0lpejkSyZF8tSMjbLUqSZF8qxU9zUE5u9zUVMZjbLXEzs4PLM8s4PLVttrHIlqrZF8tqvZF8qptrHI_LmThe1tTrHIltTrHIlS8ZF8tOZjbLXEo9zUVOds4PLM8s4PLVttrHI_L3The1vmThevtTrHI_LmTMHxjzll5QZPj93OFhBOi1Gu4mYlXyoIzlI5QblXMWbzUVMQkLyI-XHFztTheIvyU57mhPXzA8l4POQjWhyAp7WFb3470.U1Ykn0Kk5U1i1pgyktHT_Q2LsnSd1Un0mywkXHvtY_v-d_xDLQazVtj5VTv10A7bTgfqn6KspynqnfKY5IUZkPztYoeH1egP_eazde00pyYqrjR10ATqILPYT6KdpHY0TA-b5HDY0APGujY1nWf0Ugfqrj0snj7xnH0snjuxnW0dnfKopHYs0ZFY5HmYn6KBpHYznjuxnW03g1RsndtLnjPxP10Yg1csnj0zg1csnjnk0AdW5HKxn7tznjRk0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5HD0ThCqn0KhIjYz0ZKC5H00ULnqn6KBI1YY0A4Y5HD0TLCq0A71gv-bm1dsTzd-mvC0pywW5fKspZw45fKYmgFMugfqn17xn1Dzg1b0IZN15HDvP1m3P1csnHmsnWT3rHTkPjnk0ZF-TgfqnHm1P1fvnH6LnHmznfK8IZws5Hn0mv6qUZNxmvklpMb0IZRqP1mkPj6sPfK15yw-rA7WmHw-uAn4rH0LnhD0IAYqn0KWuWYk0ZFB5HD0UZNopHYk0AP8IA3quW9WnywbuyFxmLKz0ZP1TjYz0ZP1Tjcqn0KYIZ0qnsKbIZ0qn6KGIAYqn0K9uAP_mgP15HD10A7bXjYs0ZPbpdqv5HD0IvbqP0KhTvPCUyfqn6KYujYs0AkdT1YLmyRvmvnzP1bsP1TvujTk0AkdTLfqPWD4ry7-uWD0UZNWIjYvnHb4mymvu6K1mvRqnsK_INqGuAnqUhCsn6KvUWY3nj0d0A7sT7q1pyfquW9Wnywbuyc0uMcqnHf0TLcqn1cY0AF-TvsqQHD0UZNLIZcqPWndnWfLP1TYrjfznjmYn1R3PsKYTh7buHDqn0KYTh7buHcqn0K-XZKGujYznjDLn1NxnW0znHc4g1csnWc1n7tznjczPWuxnW0znWb4g1csnWf4n-tznjndPjwxnW0vPH0zg1csPWm4ndtznj6krHFxnW04rjTY0ZNzUjdCIZwsrBtEPAFbmWw9QidhrAnkuAw-mB4WUvYE0A-Vuy-xUyfd5HDsPHmLuHTYuhf3mvNBnAubPjnsrH6kuHPWrHD3mHD40ZPGujdhnAR4rjb3Pvf1nHf3PW790AP1UHd7nDmYwWN7PbckPjNAPHPA0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg100uA78IyF-gLK_my4GuZnqn7tsg100TA7Ygvu_myTqn0KsThqb5HDznWTsnjD1PjTY0APY5iY0uAPGujY10ANYpyfqPWf0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0A7buhk9u1Yk0Akhm1Ys0AwWmvfqnb7APHm1wHmsnDmLwWR4wWm3nWbzPYn4nYc4PHmYwbwtn0KYTh7buHYs0AFbpyfqrjPKfW0dPW9DwjuafYDdfbRzf1uAwDDzPjTdfWDdfbR0IvuzUvYq0AFY5H00Uv7YI1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wnansc1nWna3snj0snj0Wni3snj0knj00uAkxIA7M5HD0TNqv5H08PH9xna3sn7tsQW0sg108njKxna3sndtkQW0sg108nWNxn0KBTdqsThqbpyfqn0KzUv-hUA7M5H00mLmq0A-1gvPsmHYs0APs5H00ugPY5H00mLFW5HRsnWcz&us=newvui&ai=0_429107157_1&word=&qid=f0e98987d314861a&bdrank=9&rank=10&sourceid=1400&placeid=1#dplk=tbopen://m.taobao.com/tbopen/index.html?source=alimama_bd_sem_feeds&bc_fl_src=alimama_sem_mm_26632258_3504122_32554087&action=ali.open.nav&module=h5&bootImage=0&appkey=24532550&appName=%C3%A7%C2%99%C2%BE%C3%A5%C2%BA%C2%A6&backURL=baiduboxapp://&h5Url=http://redirect.simba.taobao.com/rd?c=un&w=unionsem&k=b1d73646918f3371&p=mm_26632258_3504122_32554087&b=GIDMEsQzm1gQasw2JgY&s=&f=https%3A%2F%2Fuland.taobao.com%2Fsemm%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32554087%26keyword%3D%25E6%2599%25BA%25E8%2583%25BD%25E5%25AE%25B6%25E5%25B1%2585%25E7%25B3%25BB%25E7%25BB%259F%25E5%25AE%2589%25E8%25A3%2585%26bc_fl_src%3Dalimama_sem_h5_mm_26632258_3504122_32554087",
    "style": {
        "idea1017": {},
        "idea10008": {
            "image": "https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/27291187-b673-4ee3-b53b-9fcfc5f8e7b4",
            "link": "http://www.baidu.com",
            "price": "1219",
            "ori_price": "2000",
            "name": "小米手机’小米手机小米手机小米手机小米手机小米手机",
            "tags": "9.6英寸高清大屏，清晰护眼！4800 mAh大电池，长续航追剧一整天！【限时直降50元】限时直降50",
            "attributes": "麟980 AI处理器，3D仿生感光技术智能识别人脸，后置2400万 AI三摄，40W安全超级快充，石墨烯散热技术带来畅快游戏体验。【到手价：4499元】限时优惠800元，下单再减500元，再赠价值268元礼包（荣耀音乐小巨蛋+二合一数据线），一降到底！",
            "sales_volume": "满意度99%",
            "seller_name": "京东",
            "display_type": "0"
        }
    },
    "general_data": {
        "cpm": 4500080000,
        "bidword": "各种花朵",
        "search_id": "7deaf65d964e86a8",
        "from": "FC",
        "word_id": 119291861,
        "ad_type": 131072,
        "extra_type": 0,
        "ip": "172.10.4.5",
        "winfo_id": 1523719733,
        "idea_id": 24493271524,
        "user_id": 30553688,
        "plan_id": 68977154,
        "unit_id": 68977154,
        "rank": 0,
        "ad_price": 104,
        "baiduid": "79FDBBC5D9034AD629968C5391F7D14E",
        "passport": 0,
        "ovlexp_id_list": "",
        "cmatch": 822,
        "wmatch": 63,
        "search_time": "1534497213"
    }
}

// 最终返回的广告数据格式
const ad_list = {
    "err_no": 0,
    "err_msg": "",
    "search_id": "2376811251339280530",
    "fc_imTimeSign": 45,
    "feed_imTimeSign": 0,
    "ad_list": [
    ],
    "query_tradeid": 0,
    "shown_info": "{\"pv\":[{\"ad\":[{\"adq\":\"xianhua\",\"uid\":7856860,\"wdid\":53063327285},{\"adq\":\"xianhua\",\"uid\":22305829,\"wdid\":61575514436},{\"adq\":\"xianhua\",\"uid\":23005909,\"wdid\":56358286050}],\"q\":\"xianhua\"}]}",
    "ovlexp_id_list": "",
    "recv_s": "99999",
    "is_ready_for_bda": false,
    "render_type": 1
};

const feed_ad_list = [
    'idea3176',
    'idea3177',
    'idea16511',
    'idea16513',
    'idea16515',
    'idea16518',
    'idea16525',
    'idea16532',
    'idea16538',
    'idea16540',
];
const fc_ad_list = [
    'idea11019',
    'idea11055',
    'idea10015',
    'idea2892',
    'idea9050',
    'idea3138',
    'idea11027',
    'idea3037',
    'idea3198',
    'idea11027',
    'idea2062',
    'idea3009',
    'idea80001',
    'idea10008',
    'idea2409',
    'idea80003',
    'idea80001',
    'idea2028',
]

// 1. 创建单个原生物料广告
const createFeedStyle = (mtInfo) => {
    try {
        let feed_item = {};
        const newFeedAd = {
            mts: [mtInfo.mt],
            [`idea${mtInfo.mt}`]: mtInfo,
            [`rule${mtInfo.mt}`]: { links: [] },
            version: 1,
        };
        feed_item = {
            ...feed_item,
            ...newFeedAd
        };
        // console.log('feed_item', feed_item);
        return feed_item;
    } catch (error) {
        console.error('错误步骤1:', error.message);
        throw error;
    }
};

// 2. 生成feed_ad.ad_info.ad_info
const generateFeedAdInfo = ({ adTemplate, newMtJson, mt, mtInfo, ...args }) => {
    try {
        const newFeedAd = JSON.parse(JSON.stringify(adTemplate));

        if (args.replace) {
            newFeedAd.ad_info.info = JSON.stringify(newMtJson[mt]);
        }
        else {
            const mt_newstyle = createFeedStyle(mtInfo);
            const ad_base_info = {
                ...(args.ad_base_info || feed_ad_detail.ad_base_info),
                mt_newstyle: JSON.stringify(mt_newstyle),
                title: `${mtInfo.mt}${feed_ad_detail.ad_base_info.title}`
            };
            const new_feed_ad_detail = {
                ad_base_info,
                ad_extra_info: args.ad_extra_info || feed_ad_detail.ad_extra_info,
                res_extra_info: args.res_extra_info || feed_ad_detail.res_extra_info
            };
            newFeedAd.ad_info.info = JSON.stringify(new_feed_ad_detail);
        }
        return newFeedAd;
    } catch (error) {
        console.error('错误步骤2:', error.message);
        throw error;
    }
};
// 生成单个凤巢广告
const generateFCAdInfo = ({ adTemplate, newMtJson }) => {
    try {
        const newFcAd = JSON.parse(JSON.stringify(adTemplate));
        const ad_info = {
            ...fc_ad_detail,
            style: {
                ...newMtJson,
            }
        };
        // console.log('fc_item', ad_info);
        newFcAd.ad_info.info = JSON.stringify(ad_info);
        return newFcAd;
    } catch (error) {
        console.error('错误步骤2:', error.message);
        throw error;
    }
};

// 3. 生成最终的单个广告物料
const generateAdList = ({ adTemplate, newMtJson, ...args }) => {
    try {
        let newAd;
        for (const mt in newMtJson) {
            const mtInfo = newMtJson[mt];
            if (feed_ad_list.includes(mt)) {
                newAd = generateFeedAdInfo({ adTemplate, newMtJson, mt, mtInfo, ...args });
            }
            else {
                newAd = generateFCAdInfo({ adTemplate, newMtJson, mt, mtInfo, ...args });
            }
        }
        return newAd;
    } catch (error) {
        console.error('错误步骤3:', error.message);
        throw error;
    }
};
```




### 使用方式
### 凤巢广告
```
{
    "idea10008": {
        "image": "https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/27291187-b673-4ee3-b53b-9fcfc5f8e7b4",
        "link": "http://www.baidu.com",
        "price": "1219",
        "ori_price": "2000",
        "name": "小米手机’小米手机小米手机小米手机小米手机小米手机",
        "tags": "9.6英寸高清大屏，清晰护眼！4800 mAh大电池，长续航追剧一整天！【限时直降50元】限时直降50",
        "attributes": "麟980 AI处理器，3D仿生感光技术智能识别人脸，后置2400万 AI三摄，40W安全超级快充，石墨烯散热技术带来畅快游戏体验。【到手价：4499元】限时优惠800元，下单再减500元，再赠价值268元礼包（荣耀音乐小巨蛋+二合一数据线），一降到底！",
        "sales_volume": "满意度99%",
        "seller_name": "京东",
        "display_type": "0"
    },
    "idea1017": {}
}
```
```
const idea10008 = require('./10008.json');

const newAd = generateAdList(
    {
        adTemplate: fc_ad,
        newMtJson: idea10008
    }
);

const newAdList = JSON.parse(JSON.stringify(ad_list));
newAdList.ad_list.push(newAd);
console.log(JSON.stringify(newAdList, null, 2));
```


### 原生广告
* ✅ 支持单个修改第二层结构
* ✅ 支持直接替换整个第二层结构
* ✅ 支持单个修改第三层结构

```
const idea16515 = require('./16515.json');
const idea16540 = require('./16540.json');
```
```
// 使用示例
const newAd1 = generateAdList(
    {
        adTemplate: feed_ad,
        newMtJson: idea16540
    }
);

const newAd2 = generateAdList(
    {
        adTemplate: feed_ad,
        newMtJson: idea16515,
        replace: true // 直接替换
    }
);

newAdList.ad_list.push(newAd1);
newAdList.ad_list.push(newAd2);
console.log(JSON.stringify(newAdList, null, 2));
```


### 1.支持单个修改第二层结构
比如你想要16515的 `ad_extra_info/res_extra_info/ad_base_info` 但是想用16540的物料信息

```
const { idea16515 } = require('./16515.json');
const idea16540 = require('./16540.json');

const newAd = generateAdList(
    {
        adTemplate: feed_ad,
        newMtJson: idea16540, 
        ad_base_info: idea16515.ad_extra_info,
        ad_extra_info: idea16515.ad_extra_info,
        res_extra_info: idea16515.res_extra_info
    }
);
```


### 2.支持全量替换 - replace: true 直接覆盖
比如你有一个全量的原生物料，不希望修改里面的任何内容，只要你提供的片段，直接替换

#### 16515.json - 可以直接定义json第二层结构
```
{
    "idea16515": {
        "ad_base_info": {
            //....很多字段
        },
        "ad_extra_info": {
            //....很多字段
        },
        "res_extra_info": {
           //....很多字段
        }
    }
}
```


```
const idea16515 = require('./16515.json');

const newAd = generateAdList(
    {
        adTemplate: feed_ad,
        newMtJson: idea16515, 
        replace: true. // 按照你给的json替换
    }
);
```


### 3.修改第三层结构 - newMtJson控制mt_newstyle内容
####  也可以定义单个物料信息, 会直接根据newMtJson控制mt_newstyle内容
注意里面的

ad_base_info: feed_ad_detail.ad_extra_info,

ad_extra_info: feed_ad_detail.ad_extra_info 

res_extra_info: feed_ad_detail.res_extra_info



使用默认的feed_ad_detail里面的，如果想要修改，可以直接自定义修改

```
{
    "idea16540": {
        "apk_name": "com.jingdong.app.mall",
        "app_name": null,
        "bes_trade_id": 202202,
        "doc_id": null,
        "dump_title": " ",
        "exposure_url_type": 1,
        "isSmartUrl": false,
        "item": [
            {
                "height": 1920,
                "url": "https://feed-image.baidu.com/0/pic/721238428_-108975812_-1124910856.jpg",
                "width": 1080
            }
        ],
        "monitor_url": "https://ccc-x.jd.com/dsp/media?delivery_system_type=10&v=713&event_type=2&idfa=NULL&imei_md5=NULL&oaid=NULL&oaid_md5=NULL&caid=%5B%7B%22caid%22%3A%5B%7B%22caid%22%3A%2200_EAFC1BF933ED1C62E6E8EE1D4BB1F337_B414E9FD07CBBA2D580CA49E47289006%22%2C%22version%22%3A%2200%22%7D%5D%2C%22generateTime%22%3A%221764032431%22%2C%22vendor%22%3A%220%22%7D%2C%7B%22caid%22%3A%5B%7B%22caid%22%3A%22f701cd57b18a864dc38de87e9befb555%22%2C%22version%22%3A%2220230330%22%7D%2C%7B%22caid%22%3A%224a684ea04660788860092661e1bcee60%22%2C%22version%22%3A%2220250325%22%7D%5D%2C%22generateTime%22%3A%221764032431%22%2C%22vendor%22%3A%221%22%7D%5D&ua=Mozilla%2F5%2E0+%28iPhone%3B+CPU+iPhone+OS+26%5F0%5F1+like+Mac+OS+X%29+AppleWebKit%2F605%2E1%2E15+%28KHTML%2C+like+Gecko%29+Mobile%2F15E148&media_click_time={{TS}}&user_ip=2409:8a3c:1611:a0e1:41:c5b8:af96:82ab&ip_type=v6&media_advertiser_id=68805293&media_campaign_id=1221302851&os=1&media_adgroup_id=12473547576&media_ad_id=1197068885917&sku_id={{PRODUCT_ID}}&mac1_md5=NULL&external_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&utm_source=baidu-ys&media_trace_id=068aa730ccba7122&request_id=6908578967182354418&ocpc_callback_url={{CALLBACK_URL}}&mid=0&media_click_id=068aa730ccba71224c6_1197068885917&sk_ocpc_convert_type=11&akey=Njg4MDUyOTM=",
        "monitor_url_type": 1,
        "mt": 16540,
        "na_url": "openapp.jdmobile://virtual?params=%7B%22category%22%3A%22jump%22%2C%22des%22%3A%22m%22%2C%22url%22%3A%22https%3A%2F%2Funion%2Dclick%2Ejd%2Ecom%2Fsem%2Ephp%3Fsource%3Dbaidu%2Dys%26unionId%3D262767352%26siteId%3Dbaiduys_1197068885917%26sk_os%3D1%26sk_request_id%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26sk_trace_id%3D068aa730ccba7122%26to%3Dhttps%253A%252F%252Fre.m.jd.com%252Fitem%252F10086969111818.html%253Fad_od%253D3%2526re_dcp%253DwUmutbkHvgyR-bcPUMXyCA%2526bd_vid%253DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%22%2C%22m_param%22%3A%7B%22jdv%22%3A%22null%7Cbaidu%2Dys%7Ct_262767352_baiduys%7Ccpc%7C1197068885917_0_1197068885917baiduys%22%7D%2C%22kepler_param%22%3A%7B%22source%22%3A%22kepler%2Dopen%22%2C%22channel%22%3A%22b4dc3278288f4a25982ccdec07ebdc41%22%7D%2C%22keplerFrom%22%3A%221%22%2C%22keplerID%22%3A%22%22%7D",
        "ori_img": "https://feed-image.baidu.com/0/pic/721238428_-108975812_-1124910856.jpg",
        "ori_landing_url": "https://union-click.jd.com/sem.php?source=baidu-ys&unionId=262767352&siteId=baiduys_1197068885917&sk_os=1&sk_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&sk_trace_id=068aa730ccba7122&to=https%3A%2F%2Fre.m.jd.com%2Fitem%2F10086969111818.html%3Fad_od%3D3%26re_dcp%3DwUmutbkHvgyR-bcPUMXyCA%26bd_vid%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL",
        "poster": null,
        "realMaterialStyle": null,
        "reserved": {
            "hasGif": null,
            "sjhAppid": null,
            "tit_t": 0,
            "usePublic": 0
        },
        "title": "精选推荐",
        "ulkScheme": "openapp.jdmobile://",
        "ulkUrl": "https://linkst.m.jd.com/ul/ul.action?openapp.jdmobile://virtual?params=%7B%22category%22%3A%22jump%22%2C%22des%22%3A%22m%22%2C%22url%22%3A%22https%3A%2F%2Funion%2Dclick%2Ejd%2Ecom%2Fsem%2Ephp%3Fsource%3Dbaidu%2Dys%26unionId%3D262767352%26siteId%3Dbaiduys_1197068885917%26sk_os%3D1%26sk_request_id%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26sk_trace_id%3D068aa730ccba7122%26to%3Dhttps%253A%252F%252Fre.m.jd.com%252Fitem%252F10086969111818.html%253Fad_od%253D3%2526re_dcp%253DwUmutbkHvgyR-bcPUMXyCA%2526bd_vid%253DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%26bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL%22%2C%22m_param%22%3A%7B%22jdv%22%3A%22null%7Cbaidu%2Dys%7Ct_262767352_baiduys%7Ccpc%7C1197068885917_0_1197068885917baiduys%22%7D%2C%22kepler_param%22%3A%7B%22source%22%3A%22kepler%2Dopen%22%2C%22channel%22%3A%22b4dc3278288f4a25982ccdec07ebdc41%22%7D%2C%22keplerFrom%22%3A%221%22%2C%22keplerID%22%3A%22%22%7D",
        "url": "https://union-click.jd.com/sem.php?source=baidu-ys&unionId=262767352&siteId=baiduys_1197068885917&sk_os=1&sk_request_id=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&sk_trace_id=068aa730ccba7122&to=https%3A%2F%2Fre.m.jd.com%2Fitem%2F10086969111818.html%3Fad_od%3D3%26re_dcp%3DwUmutbkHvgyR-bcPUMXyCA%26bd_vid%3DPjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL&bd_vid=PjTkn1TzrHn4njf3PWTLPWmvg1mLn-tkg1nsnjKxndtknHbLnjm3rj6drHDL",
        "user_icon": "",
        "user_name": "京东",
        "user_portrait": "https://feed-image.baidu.com/0/pic/-898471769_1360572184_1746933561.jpg",
        "user_portrait_id": 12658457314,
        "video_target_rcv_url": null,
        "video_url": null,
        "videoid": null
    }
}
```
```
const idea16540 = require('./16540.json');

const newAd = generateAdList(
    {
        adTemplate: feed_ad,
        newMtJson: idea16540
    }
);
```


### 函数式方式
```
const idea16515 = require('./16515.json');
const idea16540 = require('./16540.json');
const idea10008 = require('./10008.json');

// ============ 常量定义 ============
const AD_TYPES = Object.freeze({
    FEED: 2,
    FC: 1
});

const MATERIAL_TYPES = Object.freeze({
    FEED_LIST: [
        'idea3176', 'idea3177', 'idea16511', 'idea16513', 'idea16515',
        'idea16518', 'idea16525', 'idea16532', 'idea16538', 'idea16540'
    ],
    FC_LIST: [
        'idea11019', 'idea11055', 'idea10015', 'idea2892', 'idea9050',
        'idea3138', 'idea11027', 'idea3037', 'idea3198', 'idea11027',
        'idea2062', 'idea3009', 'idea80001', 'idea10008', 'idea2409',
        'idea80003', 'idea80001', 'idea2028'
    ]
});

// ============ 默认模板数据 ============
const DEFAULT_TEMPLATES = {
    feedAd: {
        ad_type: 2,
        ad_info: {
            info: "",
            template_id: ""
        },
        module_type: 0,
        client_type: 0,
        page_type: null,
        dsp_id: "",
        extra: [{
            k: "extraParam",
            v: "MVlkvkSgy11Lm6bPpJ/Ba4uyPaYIw1+HYclWLk3mO2mx11yiKjKHEpCypj2mdrbFiRxakaFZOwBDgky6YgA2KIguWTuNlU4FxhVMk4N05149D+aYyHYdCQc9iJablMBuBqm/YfaEdHvOMd0JlUfrAHDYF1h4yjRoHadzIQV07woJS5EcqPXITcbIyg/UUa1wwyf41LTl28zpUmBOTqfX6uza2hH0kqALTvf7N+MSNPNBU7W1/2Ap1v8H05wjjONAX773NBFgM3WwMwLMxTgAf1IYtL11V+LFlPZq23mMlTTXxb2Pmjb/9cM+g7dSWIEceZ3bM0SHjoUeo1tPYsxSfEbVX7AzPNRObd2bnRqXEeLUCV2N6/tHkjvBC8Rw0DgcVh4dp1nGmBAnVmSRTTgvxRm1wfj5HrLERSKxSc2t17pO+WWvEFEjsMmpAjohDkx054Ciyywu3jXzZYG9Y3wpxYrbznVFWKM1+nSd+ucuijP1Qdp54HuzMPBODRCOtzcDu/hzPPgb59e2t6eJFGT3hHPd/awAME3Eobe7SScz8LUZcmZ5FSCvtqL/5fyp8TaeeTkl5OguurrZvVLxWEvay0ubps+kn8FrxL8qfMVHxzoGAMsk0BH+27BUy8NfNcFi8E4NEI63NwNgIAgq3mEmtEtfvlFAv3jKV6I53oqK0sHR2X522fU/rljmszjVkTKrLtP2zlLwdMBrrapOjUe6DuBDzygxovIdG50l/qwKXynHGI31eT9uZoqUcvkFsa6atreniRRk94Rz3f2sADBNxIeCX3j4b5k7JtO662asYRJY270sTzTJIm9Iifj/aZz5w9aEmZa9UbjJmuFJtwiaWxm1wfj5HrLE7rBUwC4fK0lP+v7pzE0wxq5NZQannyR01CYy0tgYQ2JyrX3jRGbq1n/VtraT2f4gOO1R0bvIl/u12JGaeNdOJLXuDqr58nmqGR/cNXGcB1GfJRsk5u8xR+X1xcMX+beuw0AuNdfMaQgm5PAY+FxYI+POUW6MUVVY8rrFmpo4BTGGsCF9IpoQOzHUMkX4C61S81Edoty2uyW6YAW5hFgP5FE0H7i5dnrG14mZrFlQm61G/IGNr9jJu8KimQXG1+7Mrvrh1MCoO30dkq5ykKbNDYYtw5baJh+pFreCogKranYTmE/GLQSKxxaSCG4X5RH1BnDZS8CfBrY="
        }]
    },

    fcAd: {
        ad_type: 1,
        ad_info: {
            info: ""
        },
        extra: []
    },

    feedAdDetail: {
        ad_base_info: {
            rank: 6,
            idea_id: 153322092908,
            winfo_id: 153322092895,
            user_id: 27724717,
            plan_id: 119123968,
            unit_id: 4484081768,
            ad_cpm: 1513083,
            ad_type: 187,
            ad_flag: 1,
            title: "现在9块9能充话费100元！这活动力度真的没谁了，不抢太亏！",
            desc1: "DFT",
            desc2: "",
            rcv_url: "http://example.com/click",
            show_url: "DFT",
            mt_newstyle: "",
            target_url: "https://mobile.baidu.com/item?docid=26634081",
            position_step: 3
        },
        ad_extra_info: {
            word: "资讯",
            word_id: 3,
            match_type: 3,
            mts: "16538",
            position: 4
        },
        res_extra_info: {
            src_id: 1416,
            cmatch: 806,
            timestamp: 56
        }
    },

    fcAdDetail: {
        title: "",
        recom_reason: "秒杀0.1折起",
        user_portrait: "https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/103450ee-ec1a-47a3-8519-a7841c4c5ce0",
        desc: "优质商品推荐",
        url: "京东",
        link: "http://example.com",
        style: {},
        general_data: {
            cpm: 4500080000,
            from: "FC",
            ad_type: 131072
        }
    },

    adListWrapper: {
        err_no: 0,
        err_msg: "",
        search_id: "2376811251339280530",
        fc_imTimeSign: 45,
        feed_imTimeSign: 0,
        ad_list: [],
        query_tradeid: 0,
        shown_info: "",
        ovlexp_id_list: "",
        recv_s: "99999",
        is_ready_for_bda: false,
        render_type: 1
    }
};

// ============ 工具函数 ============
const pipe = (...fns) => x => fns.reduce((v, f) => f(v), x);
const compose = (...fns) => x => fns.reduceRight((v, f) => f(v), x);

const deepClone = obj => JSON.parse(JSON.stringify(obj));

const isNil = value => value === null || value === undefined;

const defaultTo = defaultValue => value =>
    isNil(value) ? defaultValue : value;

const prop = key => obj => obj?.[key];

const merge = (...objs) => Object.assign({}, ...objs);

const assoc = (key, value, obj) => ({ ...obj, [key]: value });

const assocPath = (path, value, obj) => {
    if (path.length === 0) return value;
    const [head, ...tail] = path;
    return {
        ...obj,
        [head]: assocPath(tail, value, obj[head] || {})
    };
};

// ============ 类型判断 ============
const isFeedMaterial = materialId =>
    MATERIAL_TYPES.FEED_LIST.includes(materialId);

const isFcMaterial = materialId =>
    MATERIAL_TYPES.FC_LIST.includes(materialId);

const getMaterialType = materialId =>
    isFeedMaterial(materialId) ? 'FEED' :
        isFcMaterial(materialId) ? 'FC' :
            'UNKNOWN';

// ============ Feed 广告相关函数 ============
const createMaterialStyle = materialInfo => ({
    mts: [materialInfo.mt],
    [`idea${materialInfo.mt}`]: materialInfo,
    [`rule${materialInfo.mt}`]: { links: [] },
    version: 1
});

const buildFeedBaseInfo = (materialInfo, customBaseInfo) => {
    const defaultBaseInfo = DEFAULT_TEMPLATES.feedAdDetail.ad_base_info;
    const mtNewstyle = createMaterialStyle(materialInfo);

    // 如果传入了完整的 customBaseInfo，优先使用它
    if (customBaseInfo && Object.keys(customBaseInfo).length > 0) {
        return merge(
            customBaseInfo,
            {
                mt_newstyle: JSON.stringify(mtNewstyle),
                title: customBaseInfo.title || `${materialInfo.mt}${defaultBaseInfo.title}`
            }
        );
    }

    // 否则使用默认模板
    return merge(
        defaultBaseInfo,
        {
            mt_newstyle: JSON.stringify(mtNewstyle),
            title: `${materialInfo.mt}${defaultBaseInfo.title}`
        }
    );
};

const buildFeedDetail = ({ materialInfo, ad_base_info, ad_extra_info, res_extra_info }) => ({
    ad_base_info: buildFeedBaseInfo(materialInfo, ad_base_info),
    ad_extra_info: ad_extra_info || DEFAULT_TEMPLATES.feedAdDetail.ad_extra_info,
    res_extra_info: res_extra_info || DEFAULT_TEMPLATES.feedAdDetail.res_extra_info
});

const createFeedAd = options => {
    const { materialInfo, replace, ...customFields } = options;
    const template = deepClone(DEFAULT_TEMPLATES.feedAd);

    const adInfo = replace
        ? options.materialJson[options.materialId]
        : buildFeedDetail({ materialInfo, ...customFields });

    return assocPath(
        ['ad_info', 'info'],
        JSON.stringify(adInfo),
        template
    );
};

// ============ FC 广告相关函数 ============
const buildFcDetail = materialJson => {
    const template = DEFAULT_TEMPLATES.fcAdDetail;
    return merge(template, { style: materialJson });
};

const createFcAd = ({ materialJson }) => {
    const template = deepClone(DEFAULT_TEMPLATES.fcAd);
    const adInfo = buildFcDetail(materialJson);

    return assocPath(
        ['ad_info', 'info'],
        JSON.stringify(adInfo),
        template
    );
};

// ============ 广告生成主函数 ============
const extractMaterialInfo = materialJson => {
    const materialId = Object.keys(materialJson)[0];
    return {
        materialId,
        materialInfo: materialJson[materialId],
        materialType: getMaterialType(materialId)
    };
};

const selectAdCreator = materialType =>
    materialType === 'FEED' ? createFeedAd : createFcAd;

const generateSingleAd = options => {
    const { materialJson, template, ...rest } = options;
    const { materialId, materialInfo, materialType } = extractMaterialInfo(materialJson);

    const creator = selectAdCreator(materialType);

    return creator({
        materialJson,
        materialInfo,
        materialId,
        template,
        ...rest
    });
};

// ============ 广告列表生成 ============
const createAdListWrapper = (ads = []) => {
    const wrapper = deepClone(DEFAULT_TEMPLATES.adListWrapper);
    return assoc('ad_list', ads, wrapper);
};

const addAdToList = ad => adList =>
    assoc('ad_list', [...adList.ad_list, ad], adList);

const generateAdList = adsConfigs => {
    const ads = adsConfigs.map(generateSingleAd);
    return createAdListWrapper(ads);
};

// ============ 导出 API ============
const AdGenerator = {
    // 生成单个广告
    generateAd: generateSingleAd,

    // 生成广告列表
    generateList: generateAdList,

    // 创建空的广告列表包装器
    createEmptyList: () => createAdListWrapper(),

    // 添加广告到列表
    addAd: (adList, adConfig) => addAdToList(generateSingleAd(adConfig))(adList),

    // 工具函数
    utils: {
        isFeedMaterial,
        isFcMaterial,
        getMaterialType,
        deepClone
    }
};

// ============ 使用示例 ============

// 示例1: 生成单个 Feed 广告（使用默认模板）
const ad1 = AdGenerator.generateAd({
    materialJson: idea16540,
    template: DEFAULT_TEMPLATES.feedAd
});

// 示例2: 生成单个 FC 广告
const ad2 = AdGenerator.generateAd({
    materialJson: idea10008,
    template: DEFAULT_TEMPLATES.fcAd
});

// 示例3: 直接替换模式
const ad3 = AdGenerator.generateAd({
    materialJson: idea16515,
    template: DEFAULT_TEMPLATES.feedAd,
    replace: true
});

// 示例4: 自定义字段
const ad4 = AdGenerator.generateAd({
    materialJson: idea16540,
    template: DEFAULT_TEMPLATES.feedAd,
    ad_base_info: idea16515.idea16515.ad_base_info,
    ad_extra_info: idea16515.idea16515.ad_extra_info,
    res_extra_info: idea16515.idea16515.res_extra_info
});

// 示例5: 批量生成广告列表
const adList = AdGenerator.generateList([
    { materialJson: idea16540, template: DEFAULT_TEMPLATES.feedAd },
    { materialJson: idea10008, template: DEFAULT_TEMPLATES.fcAd },
    { materialJson: idea16515, template: DEFAULT_TEMPLATES.feedAd, replace: true }
]);

// 示例6: 渐进式构建广告列表
const buildAdListProgressively = pipe(
    AdGenerator.createEmptyList,
    list => AdGenerator.addAd(list, {
        materialJson: idea16540,
        template: DEFAULT_TEMPLATES.feedAd
    }),
    list => AdGenerator.addAd(list, {
        materialJson: idea10008,
        template: DEFAULT_TEMPLATES.fcAd
    })
);

const progressiveAdList = buildAdListProgressively();

// 输出结果
console.log('=== 单个广告示例ad1 ===');
console.log(JSON.stringify(ad1, null, 2));

console.log('=== 单个广告示例ad2 ===');
console.log(JSON.stringify(ad2, null, 2));

console.log('=== 单个广告示例ad3 ===');
console.log(JSON.stringify(ad3, null, 2));

console.log('=== 单个广告示例ad4 ===');
console.log(JSON.stringify(ad4, null, 2));

console.log('\n=== 批量广告列表 ===');
console.log(JSON.stringify(adList, null, 2));

console.log('\n=== 渐进式构建列表 ===');
console.log(JSON.stringify(progressiveAdList, null, 2));

```
### UI界面方式


[https://app-7yj1bkw5b18h.appmiaoda.com](https://app-7yj1bkw5b18h.appmiaoda.com)



* 支持拖拽json
* 支持组合物料
* 支持编辑物料
* 支持复制/下载

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=64a2dd9f889e4684afcd7df5d0a832b0&docGuid=N4LEFQa8N7HRNR "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1ec5ed45209f404da174343127f2f174&docGuid=N4LEFQa8N7HRNR "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=79cd3743c0744e88ab0626fca69ec443&docGuid=N4LEFQa8N7HRNR "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
