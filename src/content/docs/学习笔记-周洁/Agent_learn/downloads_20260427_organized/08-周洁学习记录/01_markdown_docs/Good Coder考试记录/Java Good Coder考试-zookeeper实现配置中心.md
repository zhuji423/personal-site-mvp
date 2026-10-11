---
title: "Java Good Coder考试-zookeeper实现配置中心"
description: "Java Good Coder考试-zookeeper实现配置中心"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\Java Good Coder考试-zookeeper实现配置中心.md"
---
Java Good Coder考试-zookeeper实现配置中心

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
zookeeper 实现配置中心

背景： 分布式开发的应用需要部署到不同的服务器上，这些分布在不同节点上的应用使用的是相同的配置。当我们配置文件中有个配置属性需要改变，需要改变每个程序的配置属性，这样会很麻烦的去修改配置。配置中心是java 分布式开发中常用到的一个独立功能模块，可以实现配置统一管理。

实现功能： 1）配置管理模块， 可能通过http api向配置中心写入，删除，修改和查询功能 2）数据同步功能， 实现client端， 订阅将zk_path1中的内容， 同步到zk_path2中。且当zk_path1中配置有变更，client 可以将变更内容自动同步到zk_path2节点下

要求规范： 0）严禁抄袭，一旦被发现，会被取消申请资格，并在部门、甚至公司全员通报！！ 1）对外暴露的http api调试符合restful 风格 2）必须包含单测，且单测行覆盖率要>=80% 3）用maven 搭建工程目录 4）readme需要说明2部分内容： 源码设计&模块组织说明， 工程打包部署方案及使用说明 5) 禁止用curator 等封装好的开源客户端实现

题目代码必须符合百度java代码规范： 参考wiki: [1.1 百度Java编码规范V1.3](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=706204530)


