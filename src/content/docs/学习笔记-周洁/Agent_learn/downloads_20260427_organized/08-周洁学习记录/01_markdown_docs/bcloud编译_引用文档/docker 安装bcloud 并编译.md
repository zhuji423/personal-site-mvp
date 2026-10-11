---
title: "docker 安装bcloud 并编译"
description: "docker 安装bcloud 并编译"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\bcloud编译_引用文档\\docker 安装bcloud 并编译.md"
---
docker 安装bcloud 并编译

### 1、启动容器centos7
```
docker pull centos:7.6.1810
docker run -itd --name centos7_bcloud -v /home/star/zhoujie19:/work --net=host centos:7.6.1810
docker exec -it centos7_bcloud /bin/bash
```
查看centos版本

```
cat /etc/centos-release  # CentOS Linux release 7.6.1810 (Core)
```
### 2、安装python2.7
```
yum install -y python2 
yum install -y python2-setuptools  # 安装pip
python -V  # Python 2.7.5
```
### 3、安装git
centos7 系统默认的 git 安装版本是 1.8，但是在项目构建中发现 git 版本过低，于是用源码编译的方式安装git 2.38.1

##### 1) 安装一些依赖
```
yum install wget make which curl-devel expat-devel gettext-devel openssl-devel zlib-devel asciidoc -y
yum install  gcc perl-ExtUtils-MakeMaker -y
yum remove git  # 卸载旧版本，这一步必须的
```
##### 2) 源码编译安装git
```
cd /usr/local/src/
wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.38.1.tar.gz
tar -xvf git-2.38.1.tar.gz
cd git-2.38.1/

./configure --prefix=/usr/local/git all
make -j && make install

echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/bashrc
source /etc/bashrc

git --version  # git version 2.38.1
which git  # /usr/local/git/bin/git
```
##### 3) 配置git
a. 每个用户生成一对自己专属的SSH密钥（不要使用默认密钥地址）

```
ssh-keygen -t rsa -f ~/.ssh/zhoujie19.id_rsa
```
一直回车

b. 在~/.ssh/config中指定各个用户的密钥地址

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
c. 配置完成后，将公钥配置到icode上

```
cat ~/.ssh/zhoujie19.id_rsa.pub   # 注意：这里后缀有.pub
```
把内容copy到icode

![](../../../_remote_images/08-周洁学习记录/local_assets/1juDMv7kylZDXG/image_001.bin "")
![](../../../_remote_images/08-周洁学习记录/local_assets/1juDMv7kylZDXG/image_002.bin "")
测试一下，ok

```
ssh -p 8235 icode.baidu.com
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 4、安装bcloud
```
yum install -y  bzip2 file 
wget http://bcloud-buildkit.bj.bcebos.com/client/install.sh
bash install.sh
```
按照提示要求生效配置

```
source /root/.bash_profile
```
验证是否安装成功

```
bcloud
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 5、连接测试
退出容器，连接测试

```
ssh root@127.0.0.1 -p 8083
```
* root：容器内部系统的root账号，不是服务器的用户账号
* 127.0.0.1：服务器本机ip

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 6、编译
使用git从icode拉取代码后，cd到含有BCLOUD的目录，执行 bcloud build

执行成功后会生成output文件

### 7、不进入容器情况下进行编译并校验是否编译成功
```
docker exec -it centos7_bcloud /bin/bash -c 'source /root/.bash_profile && cd /work/baidu/hpb/feature-extractor && bcloud build'
```
通过output是否存在判断是否编译成功：

```
if docker exec centos7_bcloud ls /work/baidu/hpb/feature-extractor/output > /dev/null 2>&1; then
  echo "编译成功"
else
  echo "编译失败"
fi
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 8、bcloud build 运行可能遇到的异常
##### [ERROR] Not found logined user info, run 'bcloud login-icode -u ${username} -p ${http password}' to save icode account info
![](/personal-site-mvp/img/doc-placeholder.svg "")
原因：未登录，执行以下命令进行登录

```
bcloud login-icode -u zhoujie19 -p **密码**
```
密码需要在icode平台上设置

![](/personal-site-mvp/img/doc-placeholder.svg "")
登录成功

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### [ERROR] The source directory (/) does not appear to contain BCLOUD
原因：当前目录下无BCLOUD目录

打开到正常的项目目录：

![](/personal-site-mvp/img/doc-placeholder.svg "")
再执行bcloud build

#####  is not under version control! Only support source code under svn/icode control!
![](/personal-site-mvp/img/doc-placeholder.svg "")
原因：仅支持版本控制下模块的编译。因为bcloud执行时要获取模块的代码库信息，利用代码库信息做相关的业务逻辑判断，因此要求代码在git/svn控制之下，可通过执行。

解决方案：

1、bcloud要求git版本不低于2.2.3才能正常使用

2、创建版本控制下模块，然后再用bcloud进行编译

#####  [WARNING] Found duplicate tasks
原因：已经有任务在运行了，把已有的kill掉

```
 bcloud warden --query
bcloud warden --kill --task_id={task_id}
```
![](/personal-site-mvp/img/doc-placeholder.svg "")



