---
title: "当前代码库"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\baidu_searchbox_ug-game.md"
---
# 当前代码库
baidu/searchbox/ug-gamecenter 架构情况。
.
├── httpserver
│   ├── api
│   │   └── ddz.go                    //API注册,按照业务拆分文件
│   │   └── sum.go
│   ├── register                      //业务聚合注册，在此文件中能看到整个服务的业务视图。（在此文件中区分内网|外网）
│   ├── router.go
│   └── server.go
├── library                           //内部基础库，没有 RPC 调用的 Go 代码可以放在这里。
│   ├── resource
│   │   └── resource.go
│   ├── utils                         
│   │   └── xxxx.go 
│   └── render
│       └── response.go
├── controller                        //接口控制器
│   ├── ddz
│   │   └── ddz.go                    //只做参数格式化（入参+返回值），具体接口的实现逻辑在model层实现，在文件中要new依赖的类，不要提供全局类，防止下层类的属性也是全局的，互相影响
├── model         
│   └── ral
│       └── usertag                   //下游服务调用
│           └── usertag.go            //方法
│           └── types.go              //输入输出定义
│   └── dao                           //DB、redis、配置等数据获取            
│       └── db
│           └── sum.go
│       └── redis
│           └── sum.go
│       └── gcp
│           └── sum.go
│       └── pdcms
│           └── sum.go
│   └── data                          //以能力组件拆分，不以接口去划分，可复用，且同层不可以相互调用
│       └── usertag                   
│           └── usertag.go
│   └── service
│       └── ddz                       //接口具体流程、逻辑实现
│           └── ddz.go
├── middleware                        //中间件
├── task                              //task单独建立目录，按照SDK形式编写代码
├── conf                              //线下环境配置
│   ├── app.toml
│   ├── logit
│   ├── port.conf
│   └── servicer                      //ral配置
│       ├── gdp_site.toml
│       └── service_ecosystem.toml
├── conf_online                       //线上环境配置
│   ├── app.toml.template
│   ├── logit
│   │   ├── ral-worker.toml
│   │   ├── ral.toml
│   │   └── service.toml
│   ├── pandora.ini
│   ├── pandora.ini.hestia
│   └── servicer                      //ral配置
│       └── gdp_site.toml
├── bin
├── bootstrap                         //启动初始化
├── go.mod
├── go.sum