---
title: "购买并使用DuClaw首月套餐"
description: "【🦞教程】手把手教你购买DuClaw对接飞书"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\【🦞教程】手把手教你购买DuClaw对接飞书.md"
---
【🦞教程】手把手教你购买DuClaw对接飞书

#### 🧑‍🏫 案例作者：[@张业鹏](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：办公、OpenClaw、工作流自动化
#### 🔧 使用工具：OpenClaw
#### 📒 案例概要：教程：购买DuClaw套餐并切换GLM-5模型，对接飞书机器人实现自动回复。
# 购买并使用DuClaw首月套餐
## 打开DuClaw链接
[https://cloud.baidu.com/product/duclaw.html](https://cloud.baidu.com/product/duclaw.html)

![](/personal-site-mvp/img/doc-placeholder.svg "")
## **开通DuClaw**
### 账号注册（尽量用自己的个人账户）
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 实名认证
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 购买DuClaw
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 确认购买规格
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 扫码支付
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 购买成功
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 使用DuClaw
### 点击DuClaw控制台，等待激活
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 激活完成
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 查看订阅管理
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 切换模型
将模型切换为GLM-5，并确保自动续费关闭

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 开始使用
### 首次打招呼
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 设定小龙虾人格
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 对接飞书实战
## 登录飞书开放平台
1、登录飞书开放平台：[https://open.feishu.cn/](https://open.feishu.cn/)

2、选择：开发者后台

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 创建企业自建应用
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 设置机器人信息并创建
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 进入应用管理后台
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 获取【App ID】和【App Secret】
获取相关信息保存备用

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 出现机器人选项
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 点击权限管理和开通权限
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 开通即时通讯软件
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 创建版本并发布
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
查看发布成功状态

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 配置DuClaw飞书信息
点击消息平台，配置飞书【App ID】和【App Secret】

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 配置事件订阅方式
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 配置回调配置方式
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 配置事件配置-添加事件
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 批量导入权限
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
**清空后填写以下内容（右侧展开复制）**

```
{
  "scopes": {
    "tenant": [
      "aily:file:read",
      "aily:file:write",
      "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "cardkit:card:write",
      "contact:user.base:readonly",
      "contact:user.employee_id:readonly",
      "corehr:file:download",
      "docs:document.content:read",
      "event:ip_list",
      "im:chat",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.members:bot_access",
      "im:chat:read",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.group_msg",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:resource",
      "sheets:spreadsheet",
      "wiki:wiki:readonly"
    ],
    "user": [
      "aily:file:read",
      "aily:file:write",
      "contact:contact.base:readonly",
      "im:chat.access_event.bot_p2p_chat:read"
    ]
  }
}

```
## 权限开通确认
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 发布版本
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 打开飞书客户端-发起会话
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
