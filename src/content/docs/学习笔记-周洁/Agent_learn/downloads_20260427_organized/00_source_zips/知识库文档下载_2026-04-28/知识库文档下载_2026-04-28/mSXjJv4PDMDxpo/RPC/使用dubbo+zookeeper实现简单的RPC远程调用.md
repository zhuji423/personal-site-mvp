---
title: "Pattern to output the caller's file name and line number."
description: "使用dubbo+zookeeper实现简单的RPC远程调用"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\RPC\\使用dubbo+zookeeper实现简单的RPC远程调用.md"
---
使用dubbo+zookeeper实现简单的RPC远程调用

### 一、安装zookeeper
参考：[zookeeper](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/poFmyJlCHXOEFT?source=137?t=mention&mt=doc&dt=doc)

为了方便，我是安装在了自己的mac上

![](/personal-site-mvp/img/docs-assets/image_001_33.png "")
### 二、下载并编译运行 dubbo-admin
参考：[Dubbo](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/WfsTJJhwZEMThf?source=137?t=mention&mt=doc&dt=doc)

![](/personal-site-mvp/img/docs-assets/image_002_26.png "")
### 三、构建springboot生产者和消费者
#### 创建父项目
rpcdemo

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<packaging>pom</packaging>
	<modules>
		<module>rpc-api</module>
		<module>rpc-api</module>
		<module>rpc-provider</module>
		<module>rpc-consumer</module>
		<module>rpc-consumer2</module>
	</modules>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.1.6.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.example</groupId>
	<artifactId>rpcdemo</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>rpcdemo</name>
	<description>Demo project for Spring Boot</description>

	<!-- 统一版本管理 -->
	<properties>
		<maven.compiler.source>8</maven.compiler.source>
		<maven.compiler.target>8</maven.compiler.target>
		<java.version>1.8</java.version>
		<zk.version>3.6.2</zk.version>
		<dubbo.version>2.7.7</dubbo.version>
		<curator.framework.version>5.1.0</curator.framework.version>
		<curator.recipes.version>5.1.0</curator.recipes.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
			<exclusions>
				<exclusion>
					<artifactId>logback-classic</artifactId>
					<groupId>ch.qos.logback</groupId>
				</exclusion>
			</exclusions>
		</dependency>

<!--		<dependency>-->
<!--			<groupId>org.springframework.boot</groupId>-->
<!--			<artifactId>spring-boot-starter</artifactId>-->
<!--		</dependency>-->

<!--		<dependency>-->
<!--			<groupId>org.springframework.boot</groupId>-->
<!--			<artifactId>spring-boot-starter-test</artifactId>-->
<!--			<scope>test</scope>-->
<!--		</dependency>-->

		<dependency>
			<groupId>org.apache.dubbo</groupId>
			<artifactId>dubbo-spring-boot-starter</artifactId>
			<version>${dubbo.version}</version>
		</dependency>

		<dependency>
			<groupId>org.apache.zookeeper</groupId>
			<artifactId>zookeeper</artifactId>
			<version>${zk.version}</version>
		</dependency>

		<dependency>
			<groupId>org.apache.curator</groupId>
			<artifactId>curator-framework</artifactId>
			<version>${curator.framework.version}</version>
		</dependency>

		<dependency>
			<groupId>org.apache.curator</groupId>
			<artifactId>curator-recipes</artifactId>
			<version>${curator.recipes.version}</version>
		</dependency>

		<dependency>
			<groupId>log4j</groupId>
			<artifactId>log4j</artifactId>
			<version>1.2.17</version>
		</dependency>


	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

</project>

```
#### 子项目 api
![](/personal-site-mvp/img/docs-assets/image_003_22.png "")
#### 子项目 provider
是对api的实现

![](/personal-site-mvp/img/docs-assets/image_004_15.png "")
```
package com.example.rpc.provider.service.impl;

import com.example.rpc.api.service.UserService;
import org.apache.dubbo.config.annotation.DubboService;
import org.springframework.stereotype.Component;

@Component
@DubboService(version = "1.0")
public class UserServiceImpl implements UserService {
    @Override
    public String hello(String str) {
        return str;
    }
}
```
```
package com.example.rpc.provider;

import org.apache.dubbo.config.spring.context.annotation.EnableDubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableDubbo
public class RpcProviderApplication {
    public static void main(String[] args) {
        SpringApplication.run(RpcProviderApplication.class, args);
    }
}
```
```
server.port=8085

dubbo.registry.address=zookeeper://127.0.0.1:2181
dubbo.metadata-report.address=zookeeper://127.0.0.1:2181
dubbo.registry.timeout=20000
dubbo.application.name=rpc-provider
dubbo.protocol.name=dubbo
dubbo.protocol.port=1234
dubbo.scan.base-packages=com.example.rpc.provider.service
```
```
log4j.rootLogger=debug, stdout, R

log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout

# Pattern to output the caller's file name and line number.
log4j.appender.stdout.layout.ConversionPattern=%5p [%t] (%F:%L) - %m%n

log4j.appender.R=org.apache.log4j.RollingFileAppender
log4j.appender.R.File=logs/provider.log

log4j.appender.R.MaxFileSize=100KB
# Keep one backup file
log4j.appender.R.MaxBackupIndex=5

log4j.appender.R.layout=org.apache.log4j.PatternLayout
log4j.appender.R.layout.ConversionPattern=%p %t %c - %m%n
```
#### 子项目 consumer
![](/personal-site-mvp/img/docs-assets/image_005_9.png "")
```
package com.example.rpc.consumer.controller;

import com.example.rpc.api.service.UserService;
import org.apache.dubbo.config.annotation.DubboReference;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    @DubboReference(version="1.0")
    private UserService userService;

    @GetMapping("/user")
    public String user() {
        return userService.hello("hi");
    }
}
```
```
package com.example.rpc.consumer;

import org.apache.dubbo.config.spring.context.annotation.EnableDubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableDubbo
public class RpcConsumerApplication {
    public static void main(String[] args) {
        SpringApplication.run(RpcConsumerApplication.class, args);
    }
}
```
```
server.port=8086

dubbo.registry.address=zookeeper://127.0.0.1:2181
dubbo.registry.timeout=20000
dubbo.application.name=rpc-consumer
dubbo.protocol.name=dubbo
dubbo.protocol.port=1235
dubbo.scan.base-packages=com.example.rpc.consumer.controller
```
```
log4j.rootLogger=debug, stdout, R

log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout

# Pattern to output the caller's file name and line number.
log4j.appender.stdout.layout.ConversionPattern=%5p [%t] (%F:%L) - %m%n

log4j.appender.R=org.apache.log4j.RollingFileAppender
log4j.appender.R.File=logs/consumer.log

log4j.appender.R.MaxFileSize=100KB
# Keep one backup file
log4j.appender.R.MaxBackupIndex=5

log4j.appender.R.layout=org.apache.log4j.PatternLayout
log4j.appender.R.layout.ConversionPattern=%p %t %c - %m%n
```
#### 子项目 consumer2
类似的方法创建consumer2

![](/personal-site-mvp/img/docs-assets/image_006_7.png "")
```
server.port=8087

dubbo.registry.address=zookeeper://127.0.0.1:2181
dubbo.registry.timeout=20000
dubbo.application.name=rpc-consumer2
dubbo.protocol.name=dubbo
dubbo.protocol.port=1236
dubbo.scan.base-packages=com.example.rpc.consumer2.controller
```
#### 运行
先运行provider

后运行consumer、consumer2

### 四、dubbo-admin控制台
#### 服务查询
在服务查询中

![](/personal-site-mvp/img/docs-assets/image_007_7.png "")
查看 com.example.rpc.api.service.UserService 详情

![](/personal-site-mvp/img/docs-assets/image_008_6.png "")
##### 元数据
需要dubbo版本 > 2.7 ，且生产者配置了dubbo.metadata-report.address

![](/personal-site-mvp/img/docs-assets/image_009_7.png "")
#### 服务测试
用于 生产者 写好后，不用写 消费者， 也可以进行测试

![](/personal-site-mvp/img/docs-assets/image_010_6.png "")
![](/personal-site-mvp/img/docs-assets/image_011_4.png "")
#### 服务关系
![](/personal-site-mvp/img/docs-assets/image_012_2.png "")

