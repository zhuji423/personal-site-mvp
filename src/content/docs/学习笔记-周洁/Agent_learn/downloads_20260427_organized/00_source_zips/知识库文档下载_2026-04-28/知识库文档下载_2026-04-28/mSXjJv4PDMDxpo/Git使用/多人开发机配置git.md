---
title: "多人开发机配置git"
description: "多人开发机配置git"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Git使用\\多人开发机配置git.md"
---
多人开发机配置git

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
### 第一步：每个用户生成一对自己专属的SSH密钥（不要使用默认密钥地址）
```
ssh-keygen -t rsa -f ~/.ssh/zhoujie19.id_rsa
```
一直回车

###  第二步：在~/.ssh/config中指定各个用户的密钥地址
打开配置

```
vi ~/.ssh/config
```
最后面添加3行内容

```
Host icode.baidu.com
User zhoujie19
IdentityFile ~/.ssh/zhoujie19.id_rsa
```
### 第三步：配置完成后，将公钥配置到icode上
```
cat ~/.ssh/zhoujie19.id_rsa.pub
```
注意：这里后缀有.pub

把内容copy到icode

![](../../assets/6K9ewpLNXkWt6A/image_001.bin "")
![](../../assets/6K9ewpLNXkWt6A/image_002.bin "")

