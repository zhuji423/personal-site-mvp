---
title: "当前代码库"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\baidu_jady_ug-duoduo-video.md"
---
# 当前代码库
baidu/jady/ug-duoduo-video这是一个存钱罐业务实现代码库，主要提供对内部服务，实现存钱罐业务逻辑，供sbox-basic服务调用
- **主要的代码库层级目录**
  - controller：处理 HTTP 请求，参数验证，路由转发，！！！注意controller层不做什么业务逻辑处理。
  - model：主要做业务逻辑实现，其中service目录实现核心业务逻辑，协调各个组件和服务调用，给controller提供调用方法,data层做数据聚合，到层做数据库相关逻辑。
  - conf和conf_online：自身服务和下游服务的相关配置，其中conf为测试环境配置目录，conf_line为生产环境配置目录。
  - httpapi：主要做路由注册和定义实现，接口的path在此定义。
  - middlewares：中间件层，在进入业务层之前进行统一逻辑处理，比如：日志pblog定义，跨域处理等。
  - library:工具层，主要封装通用的工具方法，提供给业务调用。
  - thirdparty：负责第三方下游服务的封装和实现
- **依赖方向**
  - 严格遵循依赖方向：controller → service → data
  - 禁止循环依赖
  - 上层模块不能依赖于下层模块实现细节，应通过接口进行依赖
- **下游的逻辑**
  - 可以参照代thirdparty中ral的请求方式