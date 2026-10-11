---
title: "bcloud编译"
description: "bcloud编译"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\bcloud编译.md"
---
bcloud编译

使用手册：[http://buildcloud.baidu.com/bcloud](http://buildcloud.baidu.com/bcloud)

安装：[docker 安装bcloud 并编译](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/1juDMv7kylZDXG?t=mention&mt=doc&dt=doc)

## 一、bcloud 分布式构建
**登录**

bcloud login-icode -u zhoujie19 -p 密码

**编译主模块**

bcloud build

**选择性编译**

* 不下载编译产出

```
bcloud build --no-output
```
* 禁止执行release.bcloud

```
bcloud build --no-release.bcloud
```
* 仅编译cpp文件

```
bcloud build --source-file='src/server.cpp util/common.cpp proto/log.proto'
```
* 指定发布产出的类型

```
bcloud build --exclude-artifact-type="static shared"  # 不发布静态库类型和动态库类型产出
```
## 二、bcloud 本地构建
### 1. 基本步骤
**bcloud local = bcloud local -U && bcloud local -M ALL**, 直接执行bcloud local, 等于同时完成依赖模块版本打平、代码下载、生成makefile

**本地编译分为三个步骤**

**1) 打平依赖模块版本, 下载依赖模块代码**

bcloud local -U

**2) 对各模块进行预处理(处理proto和idl文件, 执行Gensources等), 生成主模块和依赖模块的makefile文件**

bcloud local -M ALL

注意:

bcloud local生成的makefile存放于: 代码根目录下的.bcloud.cache目录下, 一个模块一个makefile

/opt/compiler/gcc-4.8.2/bin/tree .bcloud.cache/
.bcloud.cache/
             ├── bcloud.pretreatment
             ├── bcloud.workspace
             ├── makefile.baidu_bcloud-demo_hello-git
             ├── makefile.baidu_bcloud-demo_hello-svn
             ├── makefile.config
             ├── makefile.quality_autotest_reportlib_cpp
             ├── makefile.third-64_protobuf
             └── makefile.thirdsrc_gtest

**3) 编译**

make -j 4

**注意:**

**make -j 的参数4, 根据实际需求修改, 以实现多并发编译, 不指定-j参数的话,默认单并发**

* bcloud local -M 表示只生成主模块的makefile文件
* bcloud local -M ALL 表示生成所有模块的makefile文件
* bcloud local -M baidu/bcloud/bcloud 表示只生成模块baidu/bcloud/bcloud的makefile文件

### 2. make help
生成Makefile之后，执行make help 会打印出相关的编译选项，可以按选选择使用，示例如下

/usr/bin/make64 MAC=64 help
all available targets of make(3.80):

    all              : will compile all targets and run release.bcloud
    no-release.bcloud: will compile all targets and not run release.bcloud
    no-ut            : will compile all targets without ut and run release.bcloud
    test             : will compile all targets, run ut and run release.bcloud
    clean            : will only cleanup Intermediate files(such as .o, .so, .a, ut and bin) of main module:
                       /xxx/bc_out/baidu/bcloud-demo/hello-git/output/bin
                       /xxx/bc_out/baidu/bcloud-demo/hello-git/output/lib
                       /xxx/bc_out/baidu/bcloud-demo/hello-git/output/so
                       /xxx/bc_out/baidu/bcloud-demo/hello-git/\*.o
                       /xxx/bc_out/baidu/bcloud-demo/hello-git/output/test
                       /xxx/baidu/bcloud-demo/hello-git/output
    distclean        : will cleanup makefile, intermediate files(such as .o, .so, .a, ut and bin) and pb.cc/pb.h idl.h/idl.cpp of main module:
                       /xxx/baidu/bcloud-demo/hello-git/Makefile
                       /xxx/baidu/bcloud-demo/hello-git/.bcloud.cache/makefile.baidu_bcloud-demo_hello-git
                       /xxx/bc_out/baidu/bcloud-demo/hello-git
                       /xxx/baidu/bcloud-demo/hello-git/output
    cleanall         : will cleanup makefiles, intermediate files(such as .o, .so, .a, ut and bin) and pb.cc/pb.h idl.h/idl.cpp of all modules:
                       /xxx/bc_out
                       /xxx/baidu/bcloud-demo/hello-git/output
                       /xxx/baidu/bcloud-demo/hello-git/Makefile
                       /xxx/baidu/bcloud-demo/hello-git/.bcloud.cache/makefile*
    help             : list all available make targets

targets for the compile of dependency module:
    baidu/bcloud-demo/hello-svn
    quality/autotest/reportlib/cpp
    thirdsrc/gtest

**make 选项**

|编译命令|作用|
|-|-|
|make all -j 4 or make -j 4|编译所有编译目标并且执行release.bcloud文件|
|make no-release.bcloud -j 4|编译所有编译目标但是不执行release.bcloud|
|make no-ut -j 4|编译除ut之外的所有编译目标并且执行release.bcloud|
|make test|编译所有编译目标并且执行ut和release.bcloud|
|make clean|删除主模块的中间编译结果文件(.o, .a, .so, ut, bin等)|
|make distclean|删除主模块的预处理结果(proto, idl, GenSources的结果文件、发布的头文件、OUTPUT发布的配置文件等)、makefile文件以及中间编译结果文件(.o, .a, .so, ut, bin等)|
|make cleanall|删除所有模块的编译相关的结果文件|
|make 依赖模块名|编译某个依赖模块，比如 make baidu/bcloud-demo/hello-svn -j 4|

### 3. 主模块第一次编译
在主模块的代码根目录下执行bcloud local && make -j 4

### 4. 主模块第二次(增量)编译
**4.1) 修改了源代码**

根据是否改变头文件的依赖关系, 有以下几种场景:

> **场景1** 未改变源代码中的include, 编译目标的依赖关系未发生变化, 执行make -j 4
> **场景2** 修改了源代码中的include, 编译目标的依赖关系发生变化, 需要重新生成makefile文件再编译, bcloud local -M && make -j 4
> **场景3** 新增、删除了cpp或头文件, 需要重新生成makefile文件再编译, 执行bcloud local -M && make -j 4
**修改了proto, idl以及GenSources标签的脚本文件**

> bcloud local -M && make -j 4, 此时需要重新生成pb.cc, idl.cc以及重新执行GenSources, 因此主模块要重新生成makefile文件才能再编译
**修改了BCLOUD文件**

> bcloud local && make -j 4, 此时需要重新进行依赖打平、生成makefile文件, 才能再编译
**依赖了不稳定的模块版本**

> 不稳定依赖是指在BCLOUD文件中, CONFIGS标签中使用了@ci-base, @trunk, @git_branch, 此时用户要自行判断是否更新依赖模块的代码, 以确保编译使用的是依赖模块最新的代码
> 如果要更新依赖模块代码, 需要重新打平, 重新生成makefile文件, 再编译； 即执行bcloud local && make -j 4 如果不更新依赖模块代码, 按照2.3.1~3 章节说明分情况进行判断
**执行了make clean**

> make clean会删除主模块的中间编译结果文件(.o, .a, .so, bin等); 此时执行make即可
**执行了make distclean**

> make distclean会删除主模块的预处理结果(proto, idl, GenSources的结果文件、发布的头文件、OUTPUT发布的配置文件等)、makefile文件以及中间编译结果文件(.o, .a, .so, bin等); 此时执行bcloud local -M && make -j 4即可
**执行了make cleanall**

> make cleanall会删除所有模块的编译相关的结果文件, 此时需要对所有模块重新做预处理,生成makefile文件(此时并不需要对依赖模块版本重新打平); 此时执行bcloud local -M ALL && make -j 4即可
**跳过依赖打平, 使用当前代码重新生成makefile文件**

> bcloud local --keep --keep 参数会跳过打平阶段, 直接使用当前workspace下的代码, 重新生成makefile
### 5. 编译依赖模块
这种情况一般是在主模块的workspace下, 修改主模块代码的同时还会修改依赖模块的代码, 要通过编译验证修改的代码是否OK 假设主模块A, 依赖模块B, 此时编译模块B有三种使用场景

**场景1: 在主模块A下编译模块B**

在模块A的代码目录下编译模块B, 模块B复用模块A的依赖打平版本信息, 有两种选择:

> option 1: make -j 4 B, 例如 make -j 4 baidu/base/ub 此时模块B编译目标的依赖关系没有发生变化, 直接编译B即可
> option 2: bcloud local -M B && make -j 4 B, 例如bcloud local -M baidu/base/ub && make -j 4 baidu/base/ub 此时模块B编译目标的依赖关系变化, 例如源文件发生了增删, include造成的头文件发生变化等 先更新模块B的makefile文件, 再编译
**场景2: 在模块B下编译模块B**

模块B作为模块A的依赖, 要在模块B的代码目录下编译B, 只有一种选择:

> option 1: bcloud local && make -j 4, 此时将模块B当做主模块, 先进行依赖打平, 再生成模块B以及其依赖模块的makefile文件, 最后再编译
**场景3: 编译模块A间接编译模块B**

在模块A的代码目录下, 编译模块B, 这种情况看似很简单, 但存在非常多的变数因素, 因此建议:

> **option 1** make -j 4 B && make -j 4, 先编译模块B再编译模块A, 此时模块B编译目标的依赖关系未发生变化
> **option 2** bcloud local -M B && bcloud local -M && make -j 4, 先重新生成模块B和模块A的makefile文件, 再编译；此时模块B编译目标的依赖关系发生变化, 需要先重新生成模块B和模块A的makefile文件, 再编译
> **option 3** make cleanall && bcloud local && make -j 4, 清理编译缓存, 生成所有模块的makefile, 再编译; 此时模块B的BCLOUD文件中CONFIGS发生变化, 重新打平, 重新生成makefile文件, 再编译
### 6. 多模块共用一个workspace
多个模块共用同一个workspace, 编译时会相互影响, 污染彼此的编译环境, 例如: 依赖模块的版本, 编译的中间缓存文件等, 因此不建议多个模块复用同一个workspace; 当然有时候复用同一个workspace很方便, 此时我们建议:

**场景1 模块间存在依赖关系**

> 一个workspace下存在模块A和模块B, 模块A依赖模块B, 此时参照2.4章节进行操作
**场景2 模块间不存在依赖关系**

> 一个workspace下存在模块A和模块B, 两个模块彼此相互独立, 不存在依赖关系; 例如在icode上, 一个部门下的模块路径前两级是一样的,这样很容易出现复用一个workspace的情况, 这个时候将两个模块都当做主模块进行编译, 例如：
> 第一次编译A：bcloud local && make -j 4, 此时模块A先打平, 再编译
> 第二次编译A：make -j 4, 直接编译
> 第一次编译B：bcloud local && make -j 4, 在模块B代码根目录下先打平, 再编译
> 第二次编译B：make -j 4, 直接编译
**如果两个模块毫无规律的交替编译, 此时需要注意：**

1. 模块A切换到模块B编译时, 第一次编译最好执行make cleanall清理编译缓存避免环境被污染导致编译失败,执行make cleanall && bcloud local && make -j 4
2. 模块A和B依赖了都的模块C, 执行bcloud local 出现版本更新提示时, 根据实际情况判断是否更新模块C的版本

### 7. 其他情况
本地编译的场景情况无法一一罗列, 需要用户根据自身的实际情况自行判断 是否需要更新依赖模块代码(bcloud local -U) 是否需要更新makefile(bcloud local -M ALL 或 bcloud local -M xx/xx/xx)

如果编译环境被污染出现莫名其妙的编译问题, 或想要一个干净的编译环境, 执行

```
make cleanall && bcloud local && make -j 4
```
## 三、编译提速
### 1、编译过程
#### 1）预处理(Preprocess)
该阶段编译器对源文件做展开处理，包括:

> * 将#include 的头文件展开
> * 将#define语句指定的值转换为变量
> * 将将宏定义转换为具体代码
> * 根据#if #elif 和#endif指定的位置包含或排除特定部分的代码
> 
```
$ gcc -E hello.cpp -o hello.i
或
$ cpp hello.cpp > hello.i
```
#### 2）编译(Compilation)
该阶段对展开后的源文件hello.i 进行语法检查，确认代码是否满足语言相关的语法规则，检查通过后生成汇编文件hello.s

```
$ gcc -S hello.i -o hello.s
```
#### 3）汇编(Assembly)
该阶段汇编器将汇编文件转换为机器可以执行的指令，生成目标文件hello.o

```
$ gcc -c hello.s -o hello.o
或者
$ as hello.s -o hello.o
```
#### 4）链接(Link)
示例hello.cpp文件中调用了printf函数，目标文件hello.o中引用的printf符号还未解析，hello.o还无法正常运行，还需要将系统运行库libc和相关的启动文件(crt文件)链接在一起，才能生成最终可执行的程序hello

在整个编译过程中，在第1、第2和第4阶段会出现不同的编译报错

|错误描述|阶段|描述|
|-|-|-|
|头文件找不到|第1阶段：预处理||
|语法错误|第2阶段：编译||
|符号未定义|第4阶段：链接||
|符号重定义|第4阶段：链接||
|recompile with -fPIC|第4阶段：链接||

## 
### 2、编译耗时信息详情
编译后在隐藏目录.bcloud.cache下生成汇总文件build_summary.json

```
=> task info
   - repo name                : baidu/bcloud/bcloud                # repo fulll name
   - compile master           : 10.102.26.41                       # 主编译机
   - taskid                   : 3e0b2fd4c5a227153cf03a8c69493d0a   # task id
   - user                     : zhangsan                           # 用户名
   - command                  : bcloud build --dwarf               # 编译命令
   - client start             : 2020-05-20 12:43:53                # 客户端起始时间
   - client stop              : 2020-05-20 12:46:04                # 客户端结束时间

=> analyze dependency                                              # 依赖模块情况
   - repo count               : 29                                 # 依赖模块个数
   - time consuming           : 22.887s                            # 依赖打平耗时，打平动作在bcloud客户端完成
   - repo check               : 0.010s                             # 依赖规则检查耗时，例如stable检查
   - stable repo              : 9  (31.0%)                         # stable分支依赖模块个数
   - 3rd repo                 : 17 (58.6%)                         # 第三方开源模块个数
   - others repo              : 3  (10.3%)                         # 除stable, 第三方开源模块外其他依赖情况的模块个数

=> queue
   - time consuming           : 0.000s                             # 用户编译任务的排队耗时

=> create workspace                                                # 创建任务工作空间情况
   - time consuming           : 4.327s                             # 创建工作空间总耗时, 指下载代码耗时
   - master                   : 2.287s                             # 主编译机耗时
   - slave(max)               : 2.040s                             # salve 最大耗时
   - dep repo hit cache       : 100.0%                             # 依赖模块源代码缓存命中率

=> preprocess                                                      # 预处理阶段情况
   - gen sources              : 1.194s                             # gensources 标签耗时
   - proto and idl            : 1.468s                             # 处理proto, idl耗时
   - publish header files     : 2.375s                             # 发布头文件耗时
   - pack result              : 1.929s                             # 打包预处理结果耗时，如果预处理结果比较大，耗时会比较长

=> compile                                                         # 编译阶段情况
   - time consuming           : 67.955s                            # 编译总耗时
   - target cache info                                             # 编译目标、编译结果缓存命中情况
     all                      : 999/1131  (88.3%)                  # 命中编译缓存总数/本次任务总编译目标数
     object file              : 864/945   (91.4%)                  # .o 文件命中缓存数/本次任务.o文件总数
     static lib               : 134/150   (89.3%)                  # .a 文件命中缓存数/本次任务.a文件总数
     bin                      : 1/3       (33.3%)                  # bin 文件命中缓存数/本次任务bin文件总数
     ut                       : 0/33      (0.0%)                   # ut 文件命中缓存数/本次编译任务ut文件总数

=> FDO process                                                     # FDO优化编译相关信息
   - FDO object file          : 1/1       (100.0%)                 # 编译过程中应用到FDO优化的.o文件总数及占比
   - sample data              : https://******                     # 本次FDO优化编译使用的sample data数据地址

=> dwarf process                                                   # dwarf 编译耗时
   - download dwo             : 0.229s                             # 下载dwo文件耗时
   - generate dwp             : 1.856s                             # merge dwo文件耗时

=> run test                                                        # ut 运行情况
   - time consuming           : 0.000s                             # ut 运行总耗时

=> client download artifacts                                       # bcloud客户端下载编译产出情况
   - download                 : 24.998s                            # 下载耗时
   - run release.bcloud       : 0.024s                             # bcloud客户端执行release.bcloud脚本耗时

=> prodserver upload artifacts                                     # 发布编译产出情况
   - download                 : 0.000s                             # 下载编译产出耗时
   - run release.bcloud       : 0.000s                             # 发布服务执行release.bcloud脚本耗时
   - upload                   : 0.000s                             # 上传编译产出到产皮库耗时

```
### 3、提速方法
1. **提高缓存命中率**

bcloud build执行结束后，会在终端输出编译任务统计信息

```
=> compile
   - time consuming           : 62.619s               # 编译总耗时
   - target cache info
     all                      : 1330/1334 (99.7%)     # 命中编译缓存总数/本次任务总编译目标数
```
2. **避免超大的cpp文件**

减少cpp文件的体积，将一个大的cpp文件拆分成多个小的cpp文件。要减小源文件的大小，可以通过拆分proto文件、cpp文件(每个类的实现可对应到多个cpp文件中)、避免引入不必要的头文件等多种形式完成。

3. **移除与编译无关的业务逻辑**

bcloud支持用户通过release.bcloud脚本对编译产出做目录调整，有些模块图方便，会在这个脚本中执行单测、下载外部依赖包或访问外部服务等一些与编译无关的业务逻辑。本地开发时，可以通过指定--no-release-bcloud参数跳过release.bcloud脚本的执行。

4. **选择性编译**

在本地开发时，有时候仅需要快速验证代码的正确性，不需要执行完整的编译过程，此时可以参数仅编译一部分文件。

* 不下载编译产出

```
bcloud build --no-output
```
* 禁止执行release.bcloud

```
bcloud build --no-release.bcloud
```
* 仅编译cpp文件

```
bcloud build --source-file='src/server.cpp util/common.cpp proto/log.proto'
```
仅编译指定源文件对应的.o文件，用于开发阶段快速验证。




