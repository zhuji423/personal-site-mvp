---
title: "README"
description: "本页面由v姚宇辰于2022/03/02迁移自wiki 周洁空间"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\开发机\\README.md"
---
开发机

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间



#### 后台运行，日志存在nohup.out
nohup sh run.sh & 

nohup yourcommand > myout.log 2>&1 &  后台运行且日志存到文件

 python test.py 2>&1 | tee output  日志存到文件同时控制台打印

#### 查看日志
tail -f no.out

#### vim
显示行号:set number

gg           ： 跳转到文件头

Shift+g   ： 跳转到文件末尾

文件开头:0，文件末尾 :$  ,第n行:n，行首^，行尾$,快速下移shift+0

移动到下一个词"w"，移动到上一个词"b"，移动到文档开始"gg"，移动到文档结束"G"，移动光标到屏幕顶端"H"，移动到屏幕中间"M"，移动到底部"L"

上一页：，下一页：

vim查找：命令模式下，输入 /word 后回车，即查找word，按 n 查找下一个匹配单词，按 N 查找上一个匹配单词。



#### 输入命令行常用快捷键
Ctrl+a 将光标移到行首

Ctrl+e 将光标移到末尾

Ctrl+u 删除整行

Ctrl+k 向后删除，从光标开始直至行尾

Alt+Backspace 光标向前删除一个单词

Alt+f 将光标移动到后一个单词

Alt+b 将光标移动到前一个单词

#### 查看虚拟机版本
 lsb_release -a

查看ip ubuntu

ifconfig

#### 前5行存储
head -n 5 dasouurl_data  > select

#### 查看大小
du -m file

ll -lh

#### 查看隐藏文件
ls -la

#### 查看文件行数
wc -l filename 

#### 大文件切割与合并
split支持自定义输出文件大小和输出文件行数两种模式，此外还可以定义每一行最大的值。

*          -l   按输出文件行数 ： split -l 200 input_file out_file
*          -b  按输出文件大小 ： split -b 200 input_file out_file（注意-b后边跟的数字需要换算成字节数） 50M=50*1024*1024（B）=52428800字节
*         -d   如果加上-d则后缀为数字，不加则默认为字母
*         -a   默认为2，意思是后缀的位数，这个是根据你分出来的文件个数决定的

split -l 300 -d nodeui3000 part_ --verbose 

split -b 52428800 -d ep-codedb-baidu-im-goldengate-deploy-intentservice.zip part_ --verbose

cat part_* > merge_file.txt



#### 压缩与解压
压缩

```
tar -cvf jpg.tar *.jpg //将目录里所有jpg文件打包成jpg.tar
tar -czf jpg.tar.gz *.jpg //将目录里所有jpg文件打包成jpg.tar后，并且将其用gzip压缩，生成一个gzip压缩过的包，命名为jpg.tar.gz
tar -cjf jpg.tar.bz2 *.jpg //将目录里所有jpg文件打包成jpg.tar后，并且将其用bzip2压缩，生成一个bzip2压缩过的包，命名为jpg.tar.bz2
tar -cZf jpg.tar.Z *.jpg //将目录里所有jpg文件打包成jpg.tar后，并且将其用compress压缩，生成一个umcompress压缩过的包，命名为jpg.tar.Z
rar a jpg.rar *.jpg //rar格式的压缩，需要先下载rar for linux
zip jpg.zip *.jpg //zip格式的压缩，需要先下载zip for linux
```
解压

```
tar -xvf file.tar //解压 tar包
tar -xzvf file.tar.gz //解压tar.gz
tar -xjvf file.tar.bz2 //解压 tar.bz2
tar -xZvf file.tar.Z //解压tar.Z
unrar e file.rar //解压rar
unzip file.zip //解压zip
```
#### 更改apt源
```
sudo vim /etc/apt/sources.list
```
#### 端口
mac查询端口在监听：netstat -AaLlnW

查看端口是否占用： lsof -i tcp:6006

![](/personal-site-mvp/img/doc-placeholder.svg "")
kill -9 6265

ubuntu有哪些端口在监听

sudo netstat -tulpn | grep LISTEN



#### 后台运行python
在跑时间比较长的程序，或者打印信息比较多，或者网络不稳定时，可以采用后台运行程序，然后把打印信息保存在文件中，等程序结束后再检查日志，完成该功能可以用以下命令

```
nohup python3 -u test.py >test.log 2>&1 &
```
* 最后一个“&”表示后台运行程序
* “nohup” 表示程序不被挂起
* “-u”表示不启用缓存，实时输出打印信息到日志文件（如果不加-u，则会导致日志文件不会实时刷新代码中的print函数的信息）
* “test.py”表示python的源代码文件
* “test.log”表示输出的日志文件
* “>”表示将打印信息重定向到日志文件
* “2>&1”表示将标准错误输出转变化标准输出，可以将错误信息也输出到日志文件中（0-> stdin, 1->stdout, 2->stderr）



 tail -f test.log 查看日志

#### 杀掉正运行的python
```
ps -ef |grep python
sudo kill -9 816459
```
#### 看磁盘还剩多少空间
整体磁盘空间

df -h

当前目录最大的前10个文件或目录

du -hsx * | sort -rh | head -10

查看目录或文件大小

sudo du -xh --max-depth=1 /var

![](/personal-site-mvp/img/doc-placeholder.svg "")




注：

[115个最常用的Linux命令行大全](https://zhuanlan.zhihu.com/p/420247468?t=mention&mt=doc&dt=sdk)
