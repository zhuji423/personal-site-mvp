---
title: "qep-delivery-data >= 0.2.18"
description: "使用TestOne服务号给用户发消息"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne-API\\用户相关\\使用TestOne服务号给用户发消息.md"
---
使用TestOne服务号给用户发消息

```
# qep-delivery-data >= 0.2.18
# pip3 install qep-delivery-data==0.2.18 --index-url http://pip.baidu.com/root/baidu/+simple/ --trusted-host pip.baidu.com  --no-cache-dir

from qep_delivery_data import TestoneUtils
from qep_delivery_data import ServiceAccountMsg

content = ("【警告】引擎回调平台失败，请及时跟进排查问题\n"
           "engineTaskId: cebb2366-857a-407a-850f-6d523b2d94b7\n"
           "errorMsg: 500 Internal Server Error: [no body]\n"
           "env: 1.opera-engine-qepdelivery-000-bj.TOOS.bjyz)\n"
           "https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/SNsADSWPchsxiI")
msg = ServiceAccountMsg(usernames=["guyouda", "zhangtao77"], content=content, msg_type="MARKDOWN")
TestoneUtils("YOUR_NAME", "YOUR_TOKEN").send_msg(msg)
```




![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=899bd6e6552c4deb905936192260841c&docGuid=Q-SJ0hDSkZwR1G "")
