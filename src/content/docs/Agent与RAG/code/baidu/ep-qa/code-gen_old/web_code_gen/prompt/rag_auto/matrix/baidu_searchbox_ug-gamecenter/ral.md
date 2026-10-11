---
title: "下游服务名称"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\matrix\\baidu_searchbox_ug-gamecenter\\ral.md"
---
## 涉及到ral第三方下游服务数据获取时，严格按以下步骤进行生成：
### 参考补充检索知识完整生成.toml配置文件，注意参考路径和文件内容中的`test`关键词需替换成需求相关名称，完整配置文件参考示例如下：
* 文件名：`conf/servicer/service_test.toml`
```toml
# 下游服务名称
Name = "service_test"
ConnTimeOut = 300
WriteTimeOut = 150
ReadTimeOut = 500
# 请求失败后的重试次数：总请求次数 = Retry + 1
Retry = 1
# 资源使用策略，非必选，默认使用 RoundRobin
# RoundRobin: 依次轮询
[Strategy]
Name = "RoundRobin"

## 资源定位: BNS 配置，支持智能 BNS
[Resource.BNS]
BNSName = "group.bdapp-auncel-server.searchbox.all"
EnableSmartBNS = true
UsePort = "main"
```
### 在常量配置文件`library/constant/service.go`中完成下游服务名配置；
### 参考补充检索知识的实现方式，生成需求描述涉及到的ral下游第三方服务数据的完整操作代码；