---
title: "Dubbo"
description: "Dubbo提供了三大核心能力：面向接口的远程方法调用、只能容错和负载均衡，以及服务自动注册和发现。"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\RPC\\Dubbo.md"
---
Dubbo

### 简介
Apache的 Dubbo是一款**高性能java RPC**框架，其前身是阿里巴巴公司开源的一个高性能、轻量级的开源RPC框架，可以和spring框架无缝集成。

Dubbo提供了三大核心能力：面向接口的远程方法调用、只能容错和负载均衡，以及服务自动注册和发现。

### 调用流程
![](/personal-site-mvp/img/docs-assets/image_001_30.png "")


|**节点**|**角色名称**|
|-|-|
|Provider	|暴露服务的服务提供方|
|Consumer|调用远程服务的服务消费方|
|Registry|服务注册与发现的注册中心|
|Monitor|统计服务的调用次数和调用时间的监控中心|
|Container|服务运行容器（spring）|

* 虚线：异步调用；
* 实线：通过网络同步调用；
* 012（启动，注册，订阅）：是在启动时候完成的功能；
* 345（通知，调用，监控）：都是在程序在运行过程中调用的功能；

调用流程如下所述：

1、服务启动，包括服务提供者和消费者的启动，封装服务调用链路。

2、服务提供者在启动时，向注册中心注册自己提供的服务。

3、服务消费者在启动时，向注册中心订阅自己所需的服务。

4、注册中心返回服务提供者地址列表给消费者，如果有变更，注册中心将基于长连接推送变更数据给消费者。

5、服务消费者，从提供者地址列表中，基于服务路由信息、负载均衡规则，选一台提供者进行调用。

6、服务消费者和提供者，在内存中累计调用次数和调用时间，定时发送一次统计数据到监控中心。

7、服务提供方停止服务或者服务调用方关闭JVM的时候，会将provider及consumer进行销毁处理。

### 架构
![](/personal-site-mvp/img/docs-assets/image_002_24.png "")
Dubbo框架设计一共划分了10个层，而最上面的Service层是留给实际想要使用Dubbo开发分布式服务的开发者实现业务逻辑的接口层。图中左边淡蓝背景的为服务消费方使用的接口，右边淡绿色背景的为服务提供方使用的接口， 位于中轴线上的为双方都用到的接口。

**服务接口层（Service）：**该层是与实际业务逻辑相关的，根据服务提供方和服务消费方的业务设计对应的接口和实现。

**配置层（Config）：**对外配置接口，以ServiceConfig和ReferenceConfig为中心，可以直接new配置类，也可以通过spring解析配置生成配置类。

**服务代理层（Proxy）：**服务接口透明代理，生成服务的客户端Stub和服务器端Skeleton，以ServiceProxy为中心，扩展接口为ProxyFactory。

**服务注册层（Registry）：**封装服务地址的注册与发现，以服务URL为中心，扩展接口为RegistryFactory、Registry和RegistryService。可能没有服务注册中心，此时服务提供方直接暴露服务。

**集群层（Cluster）：**封装多个提供者的路由及负载均衡，并桥接注册中心，以Invoker为中心，扩展接口为Cluster、Directory、Router和LoadBalance。将多个服务提供方组合为一个服务提供方，实现对服务消费方来透明，只需要与一个服务提供方进行交互。

**监控层（Monitor）：**RPC调用次数和调用时间监控，以Statistics为中心，扩展接口为MonitorFactory、Monitor和MonitorService。

**远程调用层（Protocol）：**封将RPC调用，以Invocation和Result为中心，扩展接口为Protocol、Invoker和Exporter。Protocol是服务域，它是Invoker暴露和引用的主功能入口，它负责Invoker的生命周期管理。Invoker是实体域，它是Dubbo的核心模型，其它模型都向它靠扰，或转换成它，它代表一个可执行体，可向它发起invoke调用，它有可能是一个本地的实现，也可能是一个远程的实现，也可能一个集群实现。

**信息交换层（Exchange）：**封装请求响应模式，同步转异步，以Request和Response为中心，扩展接口为Exchanger、ExchangeChannel、ExchangeClient和ExchangeServer。

**网络传输层（Transport）：**抽象mina和netty为统一接口，以Message为中心，扩展接口为Channel、Transporter、Client、Server和Codec。

**数据序列化层（Serialize）：**可复用的一些工具，扩展接口为Serialization、 ObjectInput、ObjectOutput和ThreadPool。

### 安装 dubbo-admin
1. 下载代码: `git clone https://github.com/apache/dubbo-admin.git`
2. 在 `dubbo-admin-server/src/main/resources/application.properties`中指定注册中心地址，将默认端口设置为7001，避免8080端口冲突

![](/personal-site-mvp/img/docs-assets/image_003_21.png "")
3. 构建

    * `mvn clean package -Dmaven.test.skip=true`

![](/personal-site-mvp/img/docs-assets/image_004_14.png "")
4. 启动

    * `mvn --projects dubbo-admin-server spring-boot:run` 或者
    * `cd dubbo-admin-distribution/target; java -jar dubbo-admin-0.5.0.jar`

![](/personal-site-mvp/img/docs-assets/image_005_8.png "")
5. 访问 `http://localhost:7001`

![](/personal-site-mvp/img/docs-assets/image_006_6.png "")
###### Dubbo常用配置
![](/personal-site-mvp/img/docs-assets/image_007_6.png "")
### 参考
[Dubbo 中文文档](https://dubbo.gitbooks.io/dubbo-user-book/content/configuration/xml.html)
