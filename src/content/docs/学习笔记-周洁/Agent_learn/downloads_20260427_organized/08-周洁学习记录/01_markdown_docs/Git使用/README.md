---
title: "README"
description: "本页面由v姚宇辰于2022/03/02迁移自wiki 周洁空间"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Git使用\\README.md"
---
Git使用

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间

## 一、安装
安装HomeBrew，[https://brew.sh/](https://brew.sh/)

$ brew install git

## 二、配置
生成密钥，一路回车、用默认选项

$ ssh-keygen -t rsa

使用命令行复制到粘贴板

$ cat ~/.ssh/id_rsa.pub | pbcopy

在[http://icode.baidu.com/account/keys](http://icode.baidu.com/account/keys) 中粘贴，添加ssh公钥

使用ssh密钥连接iCode

$ ssh -p 8235 [icode.baidu.com](http://icode.baidu.com)

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_001.bin "")
## 三、常用指令
### 拉取代码
进入 [https://console.cloud.baidu-int.com/devops/icode](https://console.cloud.baidu-int.com/devops/icode) 代码库

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 提交代码（带卡片）
1、开发完代码，执行git add

```
git add .
```
2、提交代码应与需求相关，在 [icafe](https://console.cloud.baidu-int.com/devops/icafe/workspace) 点开需求卡片，点击研发数据链

![](/personal-site-mvp/img/doc-placeholder.svg "")
```
git commit -m "xxxx"  # 根据需求而定 
```
3、执行

```
git push origin HEAD:refs/for/master
```
4、若代码规范未通过或其他小修改

修改代码后，执行

```
git add .
git commit --amend --no-edit
git push origin HEAD:refs/for/master
```


## 四、相关知识
### 基本操作
#### git init 
在目录中创建新的Git仓库

$ git init 

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_004.bin "")
#### git clone
克隆数据库

git clone 

#### git add
将文件添加到缓存

$ git add Main.java

添加当前项目的所有文件

$ git add . 

查看项目的当前状态 

绿"M": 改动后添加到缓存 红"M": 有改动 绿"M"红"M": 在添加到缓存后又有改动

$ git status -s

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_005.bin "")
#### git diff
查看执行 git status 的结果的详细信息

尚未缓存的改动：git diff

查看已缓存的改动： git diff --cached

查看已缓存的与未缓存的所有改动：git diff HEAD

显示摘要而非整个 diff：git diff --stat

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_006.bin "")
#### git commit
使用 git add 命令将想要快照的内容写入缓存区， 执行 git commit 将缓存区内容添加到仓库

commit后再输入git status很干净

$ git commit -m '第一次提交'

#### git reset HEAD 
取消已缓存的内容

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_007.bin "")
#### git rm
从工作目录中手工删除文件 运行$ git status 显示 红D Main.java

从已跟踪文件清单中移除，然后提交

$ git rm <file>

仅从跟踪清单中删除，仍然保留在当前工作目录中

$ git rm --cached <file>

进入某个目录，删除该目录下的所有文件和子目录 $ git rm –r * 

#### git mv
移动或重命名一个文件、目录、软连接'

$ git add README 

$ git mv README [README.md](http://README.md)

### 分支
#### 列出分支
$ git branch

查看所有分支

$ git branch -a 

#### 创建分支
$ git branch dev 

#### 切换分支
$ git checkout dev

创建并切换到分支 

$ git checkout -b dev 

#### 删除分支
$ git branch -d dev 

#### 合并分支
$ git merge dev

#### 合并冲突
查看所有分支：master（当前）和1.0

$ git branch -a

master分支：修改Main.java内容为1

$ vi Main.java 

$ git add Main.java

$ git commit -m "change branch1"

切换到1.0分支：修改Main.java内容为2

$ git checkout 1.0

$ vi Main.java

$ git add Main.java

$ git commit -m "change branch1"

合并master到当前分支

$ git merge master

提示冲突，因为两个分支库中内容有冲突，对冲突内容进行修改

$ vi Main.java

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_008.bin "")
<<<<<<,>>>>>>,=====分隔的上下就是冲突的部分,只保留上面或者下面，将<<<<<<，>>>>>>和=====这3行都删掉，这里Main.java只保留2

$ git add Main.java

$ git commit -m "chang branch"

$ git merge master

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_009.bin "")
### 查看提交历史 
$ git log 

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_010.bin "")
按q退出log

参数：

--oneline 查看历史记录的简洁的版本  --oneline -5 只显示5行 --graph 查看历史中什么时候出现了分支、合并 开启拓扑图选项 --reverse 参数来逆向显示所有日志 --author=zhoujie19  --before={3.weeks.ago}  --after={2020-07-18}

$ git log --oneline -5 --graph --author=zhoujie19

![](../../../_remote_images/08-周洁学习记录/local_assets/pDNB2avd9iQNsN/image_011.bin "")


### 常见问题
#### 1、git忽略
在git忽略目录中，新建的文件在git中会有缓存，如果某些文件已经被纳入了版本管理中，就算是在.gitignore中已经声明了忽略路径也是不起作用的， 这时候我们就应该先把本地缓存删除，然后再进行git的提交，这样就不会出现忽略的文件了。

解决方法: git清除本地缓存: git rm -r --cached . git add . git commit -m 'update .gitignore' git push -u origin master

#### 2、撤销操作
**撤销只修过文件（未执行 git add）** git checkout -- file.txt

**撤销已添加到暂存区（执行 git add，未执行 git commit），也就是取消使用git add命令添加的文件** git rm –-cached filename 或者是 git reset head file.txt

**撤销已添加到版本中（执行过 git commit）** git reset HEAD~1 // 回退到上一个版本 git reset 版本号 // 指定到某个版本

**删掉缓存区add的文件，但不修改本地文件（执行 git add，未执行 git commit）**

git restore --staged filename

**代码格式问题，commit****后修改**

git add 文件、git commit --amend --no-edit、git push origin HEAD:refs/for/master

**commit后发现某个数据文件夹，想删掉**

git rm -r --cached data/ 、git commit --amend --no-edit

#### 3、执行完commit后，想撤回commit
**git reset --soft HEAD^**

如果进行了2次commit，想都撤回，可以使用HEAD~2 **--mixed** 意思是：不删除工作空间改动代码，撤销commit，并且撤销git add . 操作 这个为默认参数,git reset --mixed HEAD^ 和 git reset HEAD^ 效果是一样的。

**--soft** 不删除工作空间改动代码，撤销commit，不撤销git add .

**--hard** 删除工作空间改动代码，撤销commit，撤销git add . 注意完成这个操作后，就恢复到了上一次的commit状态。 如果commit注释写错了，只是想改一下注释，只需要： git commit --amend 此时会进入默认vim编辑器，修改注释完毕后保存就好了

#### 4、Git pull 强制拉取并覆盖本地代码
git fetch --all

git reset --hard origin/master

git pull

## 
