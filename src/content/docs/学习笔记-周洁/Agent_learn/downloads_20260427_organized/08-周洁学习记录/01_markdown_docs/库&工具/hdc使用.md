---
title: "hdc介绍"
description: "本页面由v姚宇辰于2022/03/02迁移自wiki 周洁空间"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\库&工具\\hdc使用.md"
---
hdc使用

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间

# hdc介绍
数据管理平台(HDFS&HDC)。HDFS是IM用来存放测试数据的分布式集群， HDFS每天从OP的MFS集群同步线上各个模块的数据至QA集群，HDC是专门访问HDFS的client，这让qa能方便的进行测试数据的维护和管理。

## 下载hdc：
wget hdc.baidu-int.com:9119/home/nfs/release/hdc

## 获取hdc权限：
执行chmod 755 hdc

## 获取hdc上的output
./hdc -get hdc-im.baidu.com:/home/nfs/ecom_im/hudson/CI/hudson/jobs/exact-index_trunk_quick.html ~/

## 查看hdc上的文件
./hdc -ls hdc-im.baidu.com:/home/nfs/ecom_im/hudson/CI/hudson/jobs/exact-index_trunk_quick.html

## 新建文件
./hdc -mkdir -p CAPHI2008 hdc-im.baidu.com:/home/nfs/ecom_im/bs

## hdc使用帮助
./hdc -h

## hdc上传
./hdc -inc-put -p CAPHI2008 ctp2.0-client-latest-linux.tar.gz hdc-im.baidu.com:/home/nfs/ecom_im/bs/ctp2.0-client-latest-linux.tar.gz

## 其他
hdc 工具路径：[ftp://hdc-im.baidu.com:/home/nfs/release/hdc ](ftp://hdc-im.baidu.com/home/nfs/release/hdc )

上传命令：hdc -inc-put -p pw snapshot hdc-im.baidu.com:/home/nfs/ecom_im/SYNC_ENV/chunhua/adapp_env_xstp/adappbs/data/ADAPP_DATA/version_0/ 

下载命令：hdc -get -p pw hdc-im.baidu.com:/home/nfs/ecom_im/SYNC_ENV/chunhua/adapp_env_xstp/adappbs/data/ADAPP_DATA/version_0/ 

浏览数据：hdc -ls hdc-im.baidu.com:/home/hdc/test/ 

创建目录：hdc -mkdir -p pw hdc-im.baidu.com:/home/hdc/test/env 

删除数据：hdc -rmr -p pw hdc-im.baidu.com:/home/hdc/test/env 

移动数据：hdc -mv -p pw hdc-im.baidu.com:/home/hdc/test/env 

              hdc -put -p pw src des 
              hdc -cp -p pw src des 


# hdc使用
登录远程测试机：ssh relay.baidu-int.com

邮箱密码+手机如流手势 登录

ssh [work@cp01-bjyz-slient-02.epc.baidu.com ](mailto:work@cp01-bjyz-slient-02.epc.baidu.com )

cd /home/work/zhoujie

./hdc -get hdc-im.baidu.com:/home/nfs/ecom_im/hudson/CI/hudson/jobs/exact-index_trunk_quick.html ~/

lynx report_37053384_1594644471.html
