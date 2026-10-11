---
title: "一. 重构复杂的单一功能函数"
description: "使用zulu尝试重构业务复杂函数和业务"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\使用zulu尝试重构业务复杂函数和业务.md"
---
使用zulu尝试重构业务复杂函数和业务

#### 🧑‍🏫 案例作者：[@刘庆贺](https://ku.baidu-int.com?t=mention&mt=contact&id=847cadd0-fce1-11f0-92d1-d3b00e303c30)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了使用zulu重构复杂业务函数的实践经验。针对网盘PCS业务中的复杂函数，如DealPath和delete接口，通过制定基础rules并逐步补充业务逻辑，成功梳理了函数主逻辑，并沉淀了可复用的rules。实践表明，zulu在有指导的情况下能有效梳理复杂业务逻辑，但需注意rules的健全度和业务理解的一致性。总结了与zulu协作的心法、rules编写和执行处理的最佳实践。
# 一. 重构复杂的单一功能函数
## 实验目的
网盘PCS业务主代码承载着所有网盘的文件操作，是一个标准的“老代码”。

本文想对其中比较复杂的DealPath函数使用zulu进行重构，看看AI coding Agent能否在有指导下进行单一功能但复杂的函数的梳理。过程中对其中的不同rules进行结果的比较。

最终目的：**理清DealPath函数主逻辑，并沉淀可重复使用的rules，以及对业务忽略的进行补全。**

## 函数复杂原因
PCS的DealPath函数是网盘进行文件操作前，对传入的路径进行合理化判断。

其中问题如下：

1.因为涉及无数正则/字符串替换逻辑，没有注释可读性差，导致**我们自己也不知道网盘认为什么路径是异常的，平时只能靠经验判断**。

2.**有哪些语义上也是异常路径但是函数未挡住的，无法预判**。

使用zulu尝试**解决这两个问题**，之后**生成DealPath函数的rule文件复用**，为了项目内/项目间使用。

原始代码如下，可以看出基本看不懂：

```
func (f *File) DealPath(uid uint64, path string, strictAuthCheck bool) (map[string]interface{}, error) {
    //check path format
    if !f.Valid(path) {
        return nil, errors.New(conf.ERROR_FILE_NAME_INVALID)
    }

    //check authority
    appid := f.Ctx.GetSessionKey(conf.APPID).(int)
    if !(f._streamPass || f._allAppPass) {
        notSpeAppPath := len(path) != 0 && `/` != path && `/baiduapp` != path && `/apps` != path &&
            !utils.InStringArray(conf.INIT_DIR, path)
        if strictAuthCheck || notSpeAppPath {
            if !(&App{f.Ctx}).IsAppDir(appid, path) {
                f.Ctx.L.Warn("[path not authorize] [appid:%d] [path:%s]", appid, path)
                return nil, errors.New(conf.ERROR_FILE_NOT_AUTHORIZE)
            }
        }
    }

    path = utils.PregReplace(`\/+`, `/`, path)
    srcPath := path
    //add some prefix
    tmpPath := utils.Rtrim(path, " /.")
    //to filtrate the empty path and avoid hurt root like "/" or '//////'
    if len(tmpPath) == 0 && len(utils.Rtrim(srcPath, `/`)) != 0 {
        f.Ctx.L.Warn("[path invalid] [appid:%d] [path:%s]", appid, srcPath)
        return nil, errors.New(conf.ERROR_FILE_NAME_INVALID)
    }
    path = utils.Rtrim(path, " /")
    root := fmt.Sprintf("%d:", uid)
    f._rootLen = len(root)
    if len(path) == 0 {
        path = root
    } else {
        if []byte(path)[0] == '/' {
            path = root + path
        } else {
            path = root + "/" + path
        }
    }

    if strings.Contains(path, "/") {
        tmpPath := strings.Split(path, "/")
        for k, aPath := range tmpPath {
            if !conf.Bool(conf.API_ARGUMENT_SET, "file_commit", "allow_leading_space") {
                aPath = utils.Ltrim(aPath, " ")
            }
            aPath = utils.Rtrim(aPath, " ")
            // 判断如果trim之后aPath为空，则禁止操作，返回err
            if len(aPath) == 0 {
                f.Ctx.L.Warn("[path is null after trim right space] [appid:%d] [path:%s]", appid, path)
                return nil, errors.New(conf.ERROR_FILE_NAME_INVALID)
            }
            tmpPath[k] = aPath
        }
        path = strings.Join(tmpPath, "/")
    }

    meta := make(map[string]interface{})
    rpos := strings.LastIndex(path, "/")
    //兼容php逻辑!
    if rpos == -1 {
        rpos = 0
    }
    meta["name"] = utils.Substr(path, rpos+1, -1)
    meta["dir"] = utils.Substr(path, 0, rpos)
    meta["ns"] = uid
    meta["path"] = path
    return meta, nil
}

func (f *File) Valid(name string) bool {
    _, err := utils.JSONEncode(name)
    if err != nil {
        f.Ctx.L.Warn("[path can not json encode] [path:%s] [err:%v]", name, err)
        return false
    }

    illegalChars := []byte{'\\', '?', '|', '"', '>', '<', '*', ':', '\t', '\n', '\r', '\v', '\f', 0x00}
    if !utf8.ValidString(name) {
        f.Ctx.L.Warn("[path is not valid utf8] [path:%s]", name)
        return false
    }

    for _, eachByte := range []byte(name) {
        if (utils.Ord(string(eachByte)) & 0xF0) == 0xF0 {
            f.Ctx.L.Warn("[path has more than 3 bytes] [path:%s] [rune_list:%v]", name, []rune(name))
            return false
        }
        // 存在非法字符
        for _, illegalChar := range illegalChars {
            if eachByte == illegalChar {
                f.Ctx.L.Warn("[path has illegal byte] [path:%s] [illegal_byte_of_hex:0x%X]", name, eachByte)
                return false
            }
        }
    }

    // 去掉多余/ 判断每个小段的path是否以空格结尾，如果是则返回失败
    // 和原先正则逻辑一致，由于已经不允许存在 vtnrf 的换行字符，\s仅代表空格，简化正则
    name = utils.PregReplace(`\/+`, `/`, name)
    if strings.Contains(name, "/") {
        tmpPath := strings.Split(name, "/")
        for _, aPath := range tmpPath {
            runeList := []rune(aPath)
            if len(runeList) > 0 && runeList[len(runeList)-1] == ' ' {
                f.Ctx.L.Warn("[there is space char at the end of file name] [name:%s] [whole_path:%s]", aPath, name)
                return false
            }
        }
    }
    return true
}
```
## 测试流程
流程分享：[https://console.cloud.baidu-int.com/comatestack/share/2927?token=88286e81](https://console.cloud.baidu-int.com/comatestack/share/2927?token=88286e81)

因为我是要zulu为我总结规律，所以我仅仅提供一个基础rule（里面仅有几个名词）去要求重构。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0432976ab53544eb816e5114582f71c1&docGuid=bAmleth4TG9XDp "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bf68c6850f774b3abe5df9b154c1b357&docGuid=bAmleth4TG9XDp "")
看看最终的效果。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e66c5c8d7a154bc080617e7d810fca7e&docGuid=bAmleth4TG9XDp "")
可以看到zulu总结了整个函数要做的事情，并生成了一个path_validator.go的判断函数放到utils里以便后续调用（基础规则里说了utils是基础函数文件夹，所以其自动放到了utils里）。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ec62aa240f0848cd85822852283d260d&docGuid=bAmleth4TG9XDp "")
原函数自动增加步骤注释，合并了一些细节代码，编译，自测通过，合入后itpcase通过。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bc3a4e574d3342b2b455f0c8610589f4&docGuid=bAmleth4TG9XDp "")
## 波折
因为我要求了要对**路径应有规则进行补全**，部分补全代码如下

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e4633fff97ae4cfd8e3e08224bd0bdc6&docGuid=bAmleth4TG9XDp "")
很明显zulu认为我们是linux/windows文件系统，这里说明zulu认为这不是个云存储系统。和我们的认知有冲突。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d3117328afc64c3993433a7d36703cde&docGuid=bAmleth4TG9XDp "")
于是我让其更新项目是云存储的属性到base规则里

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7a5b65c11edb49b5b3f02b97e5d327c9&docGuid=bAmleth4TG9XDp "")
可以看出，zulu给出了更多的豁免规则，后续新分支使用zulu就不会再有这个问题。

## 使用总结
```
1. 业务rules文件更像是我们对项目的理解的合集，而不是zulu的理解，我们应该尝试降低我们问题的复杂度。
很多我们的问题在AI角度看是复杂度过高的问题（NP-Hard问题），所以最好先让其说他的理解。
2. 如果让zulu做一些扩展/创新的工作，要细心查代码，因为zulu对业务场景的理解角度和现实不同（比如zulu理解的是一个通用的场景，业务是个特化的场景）
这里的差异要及时让zulu更新到rules里去。
3. 要改什么可以让zulu先介绍一下对代码/项目的理解，这样可以提前发现一些他的理解和实际有偏差的地方，因为直接执行会花费大量时间。（多次踩坑）
```
# 二. 尝试重构大型项目
## 实验目的
对网盘文件操作比较复杂的**delete接口**的主流程使用zulu进行重构，看看AI coding Agent能否在有指导下进行复杂业务流程的梳理的可能。过程中对其中的不同rules进行结果的比较。

最终目的：**仅仅突出主要逻辑，不同产品/不同文件类型的删除逻辑要拆分出来，并可配置。**

## 业务复杂原因
PCS的delete接口的作用是删除一个文件夹/文件。具体操作是变更一个文件夹及其子文件的元信息。

但是这个接口在**产品上**涉及工作盘逻辑，企业盘逻辑..

**数据库源操作上**分为操作日志表，文件元信息表，工作盘版本表逻辑..

**文件类型上**分为操作隐藏目录，共享目录，正常文件，回收站文件，清空回收站..

**实际数据操作上**有判断文件是否存在，是否存在重复组，路径是否合理等等。

## 基本不使用rules的表现
先仅仅提供一个基础rule（里面仅有几个名词）去要求重构，看看最终的效果。

[https://console.cloud.baidu-int.com/comatestack/share/2921?token=e20c5a86](https://console.cloud.baidu-int.com/comatestack/share/2921?token=e20c5a86)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=eea62e4eb12e41e58a7a3bcce2bdead4&docGuid=m3OdWu-f2g8Dsj "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a2be7edc4e9a4769a49fd155e5c5ee06&docGuid=m3OdWu-f2g8Dsj "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=76c549be04c043b49e0920d8b1abea59&docGuid=m3OdWu-f2g8Dsj "")
这里可以看出，zulu确实识别到了一些逻辑，但是仅仅是**字面上的**进行了归纳，改动也很少，不带业务逻辑的rules根本不行。

## 增加名词解释和delete接口流程介绍
这次尝试为其增加delete接口的基本流程逻辑介绍，看看其能否实现我的需求。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f7bb7e549c6042d8a70655bf6ee72bcc&docGuid=m3OdWu-f2g8Dsj "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=858d355674544f358994c85e8fd95bf2&docGuid=m3OdWu-f2g8Dsj "")
增加了一些项目基础知识后，生产的文件明显标准多了

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9914b8ec2e3547a7b982693dd149cce3&docGuid=m3OdWu-f2g8Dsj "")
一些特定的逻辑也明显分出去了：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e99e27ea147444f09f3499e5f4fde2f1&docGuid=m3OdWu-f2g8Dsj "")
但是还是没有完全修改，比如“清空回收站”仍和删除回收站搅在一起，没有单独作为功能拆出去。但是这个可能和rules的健全度不足有关。他不认为这是个需要分拆的逻辑。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=609ba628314249c8aa2ad7a6614a8e46&docGuid=m3OdWu-f2g8Dsj "")
时间关系没有继续进行探索，但是理论上搭个框架是可行的。

## 使用总结
```
大型项目改造目前看搭建框架还是OK的，但是rules需要包含很多的业务逻辑，看起来比较难，需要常年累月的积累逻辑rules。
但是反过来，如果随着使用我们输入了接近全量的现实业务逻辑，理论上它是能做到的。
```
# 总结
```
1.心法上：当成百度分给你的实习生，当成是做管理，在对齐。主要以询问的方式让他输出而不是我们输出，我们主要做纠正，做引导，给例子。主要目的是让
他懂而不是我们懂。提供业务逻辑rule的过程其实也是对自己懂不懂业务的回馈。

2.rules编写比较好的实践：先让zulu根据业务逻辑生成个基础的模版，他生成的肯定有和我们理解不一致的（比如这次的云存储系统），
人为修复，或者矫正他让他进行补充，这是个好的循环。

3.执行处理比较好的实践：做之前先问一下他想怎么做，避免错误方向上的尝试；期间和他不同的观点也是让其自己整理成规则，不断的让其往现实业务靠拢。

4.细节：要给例子，通常给个例子他就明白一类问题了，最好把业务例子也写到rule里。

5.惊喜：无人认领的老逻辑可以让其分析，可以得到一个当时大概干了什么。
```


# 小组心得
[AI Coding Agent第四组使用心得](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/yttB9Iu9O7/6qbKKvJuo3WSZu?t=mention&mt=doc&dt=doc)

|组员|业务场景|心得|
|-|-|-|
|李强强|解决Easy框架线下开发一些常见通用性问题排查&修复|规则在执行的时候，判断zulu有没有实际加载，可以看下执行过程中生成的那个**Todos，**我上面第一次尝试的时候发现Todos和规则里面写的完全对不上，怀疑是规则问题，结果实际上是没加载，可以在后续使用中关注下这个点，上面只是一个规则可能比较好发现，如果规则很多，需要关注下实际执行过程是否符合预期一个规则里面不同的场景case匹配最好不要出现歧义或者交叉的地方，一开始写的规则里面有部分关键词错误信息有交叉，导致同一个错误它匹配上了2条路径，最后反而没有按照预期执行（后面在规则里面加**禁止同时匹配多条规则**）来规避，或者态度强硬点，让模型严格按照执行|
|何思敏|网盘云端搜索评测机制完善，输出更具体的评测报告|代码需要处理文件时，使用rules描述清楚文件的数据格式和要点。例如，某文件每行代表一条数据，每行内的数据是如何组织的，行与行之间的顺序信息是否需要在处理过程中关注。对于特定业务，可能既需要并发处理数据、又需要保留原有顺序，这些信息会影响zulu在编写代码时如何选择正确的数据结构。当zulu不清楚输入输出文件的数据组织形式时，每次修改一点代码都需要完整描述一遍数据背景，效率很低。工程效能上的关注点可以用rules约束，例如要求zulu在处理过程中及时提交数据。在实践中出现了zulu一次性读取一个大型文件，批量处理完所有数据才进行一次性写入的现象，某次代码在结果整理阶段抛异常，导致前期处理的输出数据全部丢失。另外，这种代码也会造成大量内存占用。|
|李梦奇|风控任务调度系统自动注册|1、交给模型的一定是最具代表性的任务，若内容要求差别较多则无法抽象成一个rule2、单次调通了让模型自己总结rule，再根据此rule做一次任务，然后对话调整增加要求3、多轮过后再重新总结rule，避免太过冗杂|
|温鸿飞|根据描述，修改已有代码，完成简单需求。|1、要尽可能的描述清楚需求，避免过于笼统、宽泛。描述需求后，可以先输入自己大概的写代码思路，让AI按照自己思路先写一个版本。2、不要指望AI能一次性写好，可以先写一个版本，之后不断提出建议，让AI进行修改，直到最后符合需求。|
|刘庆贺|重构PCS文件操作里路径处理函数，并尝试拆分delete接口操作流程。|1.心法上：当成百度分给你的给你干活的啥都会的实习生，当成是做管理，在对齐。提供业务逻辑rule的过程其实也是对自己懂不懂业务的回馈。2.rules编写比较好的实践：先让zulu根据业务逻辑生成个基础的模版，他生成的肯定有和我们理解不一致的，人为修复，或者矫正他让他进行补充，这是个好的循环。3.执行处理比较好的实践：做之前先问一下他想怎么做，避免错误方向上的尝试；期间和他不同的观点也是让其自己整理成规则，不断的让其往现实业务靠拢。4.细节：要给例子，通常给个例子他就明白一类问题了，最好把业务例子也写到rule里。5.惊喜：无人认领的老逻辑可以让其分析，可以得到一个当时大概干了什么。|

总结：

```
强强：执行过程中要仔细看rules是否加载上了，rules里不要有交叉的逻辑。
思敏：提前做好任务相关联点业务rule描述，处理过程中可以要求zulu执行一点提交一点，避免最终失败整个全返工，也可以早期发现问题。
梦奇：开始写需求时突出主要任务，过程中让模型自己总结rule，并不断用总结的rule再作为输入执行任务。
鸿飞：需求可以先把自己的思路作为一个rule输入，让其先写一个版本，过程中再纠正。
庆贺：当成管理一个实习生同学，主要以询问的方式让他输出而不是我们输出，我们主要做纠正，给例子。
```
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
