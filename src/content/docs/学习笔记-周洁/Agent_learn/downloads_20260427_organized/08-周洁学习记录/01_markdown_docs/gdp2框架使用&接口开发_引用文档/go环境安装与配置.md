---
title: "go version go1.22.3 darwin/arm64"
description: "go环境安装与配置"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\gdp2框架使用&接口开发_引用文档\\go环境安装与配置.md"
---
go环境安装与配置

### 1、下载安装包
查看mac是arm还是X86

![](/personal-site-mvp/img/doc-placeholder.svg "")
在 [https://go.dev/dl/](https://go.dev/dl/) ，下载对应安装包

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 2、安装go环境
#### mac
下载完成打开根据引导安装 ，一路下一步

![](/personal-site-mvp/img/doc-placeholder.svg "")
安装完成后，查看版本

```
go version
# go version go1.22.3 darwin/arm64
```
#### linux
```
# 下载Go 1.22 Linux版本
wget https://dl.google.com/go/go1.22.6.linux-amd64.tar.gz
 
# 解压缩到/usr/local目录
sudo tar -C /usr/local -xzf go1.22.6.linux-amd64.tar.gz
 
# 设置环境变量
echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.profile
echo "export GOPATH=\$HOME/go" >> ~/.profile
source ~/.profile
```
### 3、环境
查看环境 go env

```
GO111MODULE='on'
GOARCH='arm64'
GOBIN='/Users/zhoujie19/go/bin'
GOCACHE='/Users/zhoujie19/Library/Caches/go-build'
GOENV='/Users/zhoujie19/Library/Application Support/go/env'
GOEXE=''
GOEXPERIMENT=''
GOFLAGS=''
GOHOSTARCH='arm64'
GOHOSTOS='darwin'
GOINSECURE=''
GOMODCACHE='/Users/zhoujie19/go/pkg/mod'
GONOPROXY='*.baidu.com'
GONOSUMDB='*.baidu.com'
GOOS='darwin'
GOPATH='/Users/zhoujie19/go'
GOPRIVATE='*.baidu.com'
GOPROXY='https://goproxy.baidu-int.com,direct'
GOROOT='/usr/local/go'
GOSUMDB='sum.golang.org'
GOTMPDIR=''
GOTOOLCHAIN='auto'
GOTOOLDIR='/usr/local/go/pkg/tool/darwin_arm64'
GOVCS=''
GOVERSION='go1.22.3'
GCCGO='gccgo'
AR='ar'
CC='clang'
CXX='clang++'
CGO_ENABLED='1'
GOMOD='/dev/null'
GOWORK=''
CGO_CFLAGS='-O2 -g'
CGO_CPPFLAGS=''
CGO_CXXFLAGS='-O2 -g'
CGO_FFLAGS='-O2 -g'
CGO_LDFLAGS='-O2 -g'
PKG_CONFIG='pkg-config'
GOGCCFLAGS='-fPIC -arch arm64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -ffile-prefix-map=/var/folders/gy/y19q4z8n7r98x98zl2_5m9dh0000gn/T/go-build3606529936=/tmp/go-build -gno-record-gcc-switches -fno-common'
```
关注其中3个重点项

```
 go env
 # GOBIN='/Users/zhoujie19/go/bin'
 # GOPATH='/Users/zhoujie19/go'
 # GOROOT='/usr/local/go'
```
若 go env以上3个值有异常比如GOBIN为空，修改vi ~/.bash_profile (注意zsh对应的~/.zshrc， bash对应的~/.bash_profile)，加入以下内容：

```
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
export GOPATH=/Users/zhoujie19/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOPATH/bin
```
使生效source ~/.bash_profile (注意zsh对应的source ~/.zshrc)

#### 多版本切换
[go 多版本切换](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/vn3qkhvaf50Rws?t=mention&mt=doc&dt=doc)

#### 安装gdp2
配置 Go Proxy，命令行执行

```
go env -w GOPRIVATE=\*.baidu.com                        # 厂内如 icode 等是私有库，不需要走代理和验证 sumdb          
go env -w GOPROXY=https://goproxy.baidu-int.com,direct 	# 可以下载墙外代码
```
安装gdp

```
go install icode.baidu.com/baidu/gdp/gps/gdp@master
```
`go install`会将命令安装到 `$GOBIN` 目录下。如果报错connect: connection refused就是未配置 Go Proxy

![](/personal-site-mvp/img/doc-placeholder.svg "")
go install 命令会把gdp存放在 ~/go/bin下面

![](/personal-site-mvp/img/doc-placeholder.svg "")
重新开一个终端，查看是否安装成功： gdp help

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 4、开发工具
##### GoLand（推荐）
[Goland安装与配置](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/xVc_EuG9o0exZj?source=137?t=mention&mt=doc&dt=doc)

##### icoding & vscode： 安装go插件
[icoding安装与comate插件使用](./icoding安装与comate插件使用.md)

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 5、执行
```
package main 

import "fmt" 

func main() {
	fmt.Println("hello world")
}
```
1、运行：go run xx.go

![](/personal-site-mvp/img/doc-placeholder.svg "")
2、打包运行(类似c++)：go build xx.go

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 6、单元测试
[go编写单元测试 产出覆盖率报告](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/sNr9JWCbHjrXGM?source=137?t=mention&mt=doc&dt=doc)

### 7、Go mod包管理工具
Go mod是Go语言自带的依赖管理工具，通过go.mod文件来管理项目依赖的包。go.mod文件包含了项目依赖的版本、依赖关系、引入和删除等信息。使用Go mod可以方便地管理项目依赖的包，并自动处理包的版本冲突和依赖关系等问题。

Go mod管理包的基本步骤:

* 初始化项目：使用go mod init命令来初始化一个新的Go模块，生成一个go.mod文件，用于管理项目依赖。
* 添加依赖：使用go get命令来添加一个新的依赖包到项目中。
* 更新依赖：使用go get -u命令来更新依赖包到最新版本。
* 整洁依赖：使用go mod tidy命令把项目所需要的依赖添加到go.mod,并删除go.mod中没有被项目使用的依赖。
* 查看依赖：使用go list命令来查看当前项目的依赖包



```
.
├── coverage.out
├── go.mod
├── go.sum
├── perm  // 依赖库 perm
│   ├── getBawuList.pb.go
│   └── perm.go
├── main.go  
├── main_test.go
└── utils  // 依赖库 utils
    ├── ref.go
    └── util.go
```
当前项目名为ut

![](/personal-site-mvp/img/doc-placeholder.svg "")
导入依赖

![](/personal-site-mvp/img/doc-placeholder.svg "")
1）本地依赖库

main.go  中导入本地perm库、utils库

```
import (
	metaPerm "ut/perm"  // 导入perm库并重命名为metaPerm
	"ut/utils"
)
```
使用本地perm库、utils库

```
func getBawuInfo(bawuInfo *metaPerm.BawuOut) map[uint64]string {
    // 函数具体实现 
}

func browserHapFind(Ua, matchStr, name, browserID string, res *utils.BrowserInfo) int {
    // 函数具体实现
}
```
2）第三方库

```
import (
	jsoniter "github.com/json-iterator/go"
	"google.golang.org/protobuf/proto"
)
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
修改代码有了新的第三方依赖库后，需要在执行 go run main.go之前需要先整洁依赖

```
go mod tidy  # 把项目所需要的依赖添加到go.mod，并删除go.mod中没有被项目使用的依赖
```

