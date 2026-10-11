---
title: "任务一、iCode&git使用任务"
description: "【码神特训营】研发工具链实战/获得QC认证"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\【码神特训营】研发工具链实战获得QC认证.md"
---
【码神特训营】研发工具链实战/获得QC认证



[码神特训营 主页](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1136256431)

[必读·研发工具链课程说明](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1172923576)

# 任务一、iCode&git使用任务
## 1、点击链接新建考试代码库
![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_001.bin "")
## 2、配置git 客户端与iCode间的认证（否则下载代码报错Permission Denied）；
**以Mac为例**

安装HomeBrew，[https://brew.sh/](https://brew.sh/) 

`brew ``install` `git`

git账号配置

> git config --global [user.name](http://user.name/) xxx
> git config --global user.email [xxx@baidu.com](mailto:weiyalin01@baidu.com)


`生成密钥，一路回车、用默认选项`

`$ ssh``-keygen -t rsa`

`使用命令行复制到粘贴板`

`$ cat` `~/.``ssh``/id_rsa``.pub | pbcopy`

在[http://icode.baidu.com/account/keys](http://icode.baidu.com/account/keys) 中粘贴，添加ssh公钥

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_002.bin "")
使用ssh密钥连接iCode

`$ ssh` `-p 8235 icode.baidu.com`

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_003.bin "")
若报错：

```
Unable to negotiate with 10.11.81.103 port 8235: no matching host key type found. Their offer: ssh-rsa
```
是因为本地电脑ssh不支持rsa类型密钥，需按照以下步骤配置：

1. 新建`vi ～/.ssh/cofig`文件
2. 写入以下内容保存即可：

```
Host *
HostkeyAlgorithms +ssh-rsa
PubkeyAcceptedKeyTypes +ssh-rsa
```
克隆代码库，复制icode代码库中克隆的第一个地址到git bash回车

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_004.bin "")
克隆完成后，进入zhoujie19文件夹

$ cd baidu/qualifiedcoder/zhoujie19

## 3、代码库中有两个已有分支，分别是master分支和1.0分支；
查看所有分支

$ git branch -a

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_005.bin "")
代码库中有两个已有分支，分别是master分支和1.0分支，带*为当前分支，位于master

补充：

git branch dev 创建分支 git branch -d dev 删除分支 git checkout dev 切换分支 git merge dev 合并dev分支到当前分支

## 4、基于库中已有master分支，修改Main.java中的编码规范问题：“在第5行，不能有两个分号，无用的import java.util.List;”，修改完成后提交评审，自己评审+2通过且合入分支；
修改master中的Main.java文件，第5行修改这一行为2行；删除第一行无效行

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_006.bin "")
不要使用tab，两行输出语句前的空格用空格键一个个敲

$ git add .

$ git commit -m "change Main.java"

提交评审

$ git push origin HEAD:refs/for/master

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_007.bin "")
在浏览器中打开返回的链接，点击打分/评论，选择2，不用写评论，点击发表

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_008.bin "")
自动化任务检查会花一段时间，如流会收到两条通知，代码扫描通过/持续集成通过。刷新页面显示任务检查通过。如果代码格式没有问题，点击合入。

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_009.bin "")
如果格式有问题，比如偷懒空格没用空格键敲，重新修改。git add Main.java → git commit -m "change2 Main.java" → git push origin HEAD:refs/for/master 浏览器打开返回的链接重新操作。

## 5、将1.0分支merge到master分支，提交评审并合入，过程中需要解决冲突；
将1.0分支merge到master分支

$ git merge 1.0

一部分人会出现下图提示，改为origin/1.0

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_010.bin "")
合并时会提示出现冲突，使用vim打开冲突的文件

$ vi favorite_fruits.dict

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_011.bin "")
<<<<<<,>>>>>>,=====分隔的上下就是冲突的部分,只保留上面或者下面，将第一行，最后一行和=====这行都删掉

输入i，进入insert模式，进行编辑，编辑后得到

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_012.bin "")
按esc，退出insert模式，输入:wq退出保存

$ git add favorite_fruits.dict

$ git commit -m "change favorite_fruits.dict"

$ git push origin HEAD:refs/for/master

在浏览器中打开返回的链接，和上面步骤一样，提交评审并合入

# 任务二、流水线Agile任务
### 第一部分 配置一条，加上编译和发布任务
#### 1、找到流水线系统中代码库对应的模块


打开agile：[http://agile.baidu.com/](http://agile.baidu.com/) ，搜索baidu/qualifiedcoder/zhoujie19（自己邮箱前缀），进入模块

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_013.bin "")
后面的shell测试需要动态资源，在进行流水线新建前，先进行资源配置

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_014.bin "")
新建动态资源，新增套餐和新增镜像库，全部选第一个

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_015.bin "")
#### 2、新建一条用户名同名的流水线
点击创建流水线，名称填入zhoujie19，选择从零新建

#### 3、配置编译和发布任务
先不管，后面做完了发布

#### 4、让流水线监听master分支
![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_016.bin "")
### 第二部分 在编译和发布之间加上测试任务
右边点击＋，然后拖动至中间，修改名字为测试shell

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_017.bin "")
#### 1、选择测试——其他测试——执行脚本插件（Shell插件）
在测试shell的配置页，任务配置：点击添加新任务/新建任务



![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_018.bin "")
选择测试——其他测试——执行脚本插件（Shell插件）

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_019.bin "")
#### 2、录入Shell脚本


选择动态资源，依次选择之前配置的资源，并输入shell命令，命令在QC认证代码库的readMe中有，复制即可

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_020.bin "")
### 第三部分 在编译阶段增加单测任务
#### 1、在编译任务后加单测任务
#### 2、选择代码准入——Unit Test——单元测试插件
![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_021.bin "")
语言类型选择java，覆盖率30

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_022.bin "")
配置完点击保存

### 第四部分 执行流水线，得到测试报告
#### 1、手动触发执行流水线
选择zhoujie19/master，点击执行构建

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_023.bin "")
#### 2、手动触发发布阶段
等待模块依次完成后，完成任务。如果选择模块为手动需自己点击执行

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_024.bin "")
#### 3、查看单测的覆盖率报告详情
选择编译 单元测试 ，点击右侧的1m42s 前的单元测试

![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_025.bin "")
![](../../../_remote_images/08-周洁学习记录/local_assets/jiOH4pVoJV4Ojo/image_026.bin "")


![](/personal-site-mvp/img/doc-placeholder.svg "")

