---
title: "Zulu首先分析项目结构，理解SDK架构"
description: "Zulu AI辅助Python SDK测试实践案例"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Zulu AI辅助Python SDK测试实践案例.md"
---
Zulu AI辅助Python SDK测试实践案例

#### 🧑‍🏫 案例作者：[@闫世锋](https://ku.baidu-int.com?t=mention&mt=contact&id=37022de0-fce7-11f0-91f7-e5cc77644706)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了利用Zulu AI智能体辅助完成数管平台物理机凭证托管Python SDK的测试工作，通过AI辅助开发构建了包含创建、获取、删除凭证的全流程自动化测试脚本。实现了凭证自动管理、核心功能覆盖，并形成了可复用的测试框架，显著提升了测试效率与质量。
## 概述
### 基本信息
* **案例贡献人**: yanshifeng
* **实践时间**: 2025年11月
* **技术栈**: Python SDK测试、Zulu AI辅助开发、数管平台凭证托管

### 核心内容简介
本实践展示了如何利用Zulu AI智能体辅助完成数管平台物理机凭证托管Python SDK的测试工作。通过AI辅助开发，成功构建了一个包含**创建凭证→SDK获取凭证→删除凭证**全流程的自动化测试脚本，为开发团队提供了完善的测试工具。

**关键成果**：

* 开发了包含12个测试场景的完整SDK测试套件
* 实现了凭证自动创建和清理机制
* 覆盖了版本控制、特征匹配、缓存刷新等核心功能
* 形成了可复用的测试框架供开发团队使用

## 背景
### 业务背景
      数管平台需要将物理机上的硬编码凭证信息托管到平台统一管理，为此开发了Python SDK。业务方提测时，需要验证SDK的完整功能流程，确保凭证托管机制的安全性和可靠性。

### 业务逻辑
[流程图]
![工作流程](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=def60d1ba26b466fa17d0f59e0cff0dc&docGuid=qSKBvv7pmjWM5r "工作流程")
### **SDK提测**
提测链接：[python sdk 提测](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/HsaDGrX8HH/Uz_ASXAP2V/mT75Z5DaNPtsjL?t=mention&mt=doc&dt=doc)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=11805fe6459f4cd79cd258b75139fcff&docGuid=qSKBvv7pmjWM5r "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fdbfac5eb4c74ab1ac912919ea9e30bc&docGuid=qSKBvv7pmjWM5r "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ba91cedb13ca4f9abfff5439fd102245&docGuid=qSKBvv7pmjWM5r "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a2a39492b03c43a0b9eda94cd1a5885b&docGuid=qSKBvv7pmjWM5r "")
## AI开发流程
### 整体流程
* 项目理解与测试点分析

```
# Zulu首先分析项目结构，理解SDK架构
- 扫描项目目录结构
- 分析pyproject.toml配置
- 阅读核心模块代码
- 识别关键测试场景
```
* 通过多轮对话，引导Zulu逐步构建测试脚本

### 开发细节
1. 让zulu通读项目细节（源代码/实现流程/知识库文档等）

![请求](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1aa8b2d365fd452a9815cd66ae345c03&docGuid=qSKBvv7pmjWM5r "请求")
![思考响应](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=030ea7aeeafe43008fd2aeebb61bae5a&docGuid=qSKBvv7pmjWM5r "思考响应")
![响应](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=03d5c09a6b024be3a9c60afb0871e589&docGuid=qSKBvv7pmjWM5r "响应")
2. 补充cookie 测试环境

![补充测试环境](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=deb1f299ff0046289053419b495aef95&docGuid=qSKBvv7pmjWM5r "补充测试环境")
![补充cookie](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0d34c45d63994e60bd4c48191f9201ae&docGuid=qSKBvv7pmjWM5r "补充cookie")
3. 完成凭证创建/删除的闭环

![api请求闭环](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=de754ff7182b48b586e043587dc6fc1b&docGuid=qSKBvv7pmjWM5r "api请求闭环")
4. 要求模型按照demo调用sdk，并完善含有版本号/不含版本号/缓存验证等场景

![关键测试点补充](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cdc77a9d832548b2835fd4c5bb4be4fe&docGuid=qSKBvv7pmjWM5r "关键测试点补充")
5. 引导模型不要mock服务，需要调用真实的后端服务

![意图修正](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ad44ffdf7ab947dabd6d19ac1d8cf064&docGuid=qSKBvv7pmjWM5r "意图修正")
![模型理解不要mock服务](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bc386064a9094668b5fa49f5800faf98&docGuid=qSKBvv7pmjWM5r "模型理解不要mock服务")
6. 保存现有代码环境，新开会话

![新开会话](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8bd476cca02449b0b02297c7480863d1&docGuid=qSKBvv7pmjWM5r "新开会话")
7. 补充测试点，并让模型发散补充一些场景

![补充测试点](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=26650e16ef384d79804200ab3116e35d&docGuid=qSKBvv7pmjWM5r "补充测试点")
8. python代码验证通过后，让模型转为go/java等版本

### 取得的效果
##### 技术亮点
1.  智能特征匹配测试

```
# 自动生成真实系统特征
def get_real_system_features():
    # 获取真实IP、BNS、工作目录等信息
    # 用于验证特征匹配算法的准确性
```
2. 自动化凭证生命周期管理

* 自动创建测试凭证
* 测试完成后自动清理
* 异常情况下的回滚机制

3. 全面的测试场景覆盖

* 基础功能测试
* 边界条件测试

#####  测试代码平移
* 使用大模型将python版本的代码平移到java/go版本的，测试对应的java/go sdk

#####  测试覆盖率提升
* 从基础功能测试扩展到12个测试场景
* 覆盖SDK所有核心功能和边界条件
* 测试脚本开发时间从数天缩短到数小时
* 提供了可复用的测试框架模板
* 降低了后续维护成本

## 复盘总结
* 在关键的流程节点上需要和模型讲清楚，例如要先让模型实现什么，然后接着实现什么
* 在接口测试等场景下，要避免模型直接去mock服务，而非调用真实的后端服务
* 在增加新的开发点/测试点/功能点时，要避免影响现有的代码逻辑，让模型不要修改已有的代码，可以在开始就告诉模型要模块化的生成
* 当对话轮数达到一定程度后，无论是响应时间还是效果都会变差，可以此时考虑代码封版，然后在封版的基础上，开启新的对话再继续对话

---

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
