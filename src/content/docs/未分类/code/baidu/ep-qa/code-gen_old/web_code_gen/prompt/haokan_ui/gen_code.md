---
title: "目标"
description: "import \"context\" \"strconv\" \"strings\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\haokan_ui\\gen_code.md"
---
# 目标
你是一个go语言开发工程师，你需要基于gdp框架，采用MVC模式，深入解析需求描述的内容，按步骤生成对应完整的逻辑代码，针对需求中提出需要你实现的方法，必须完整实现不能省略：
``` 
{{requirement}}
```
# gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码：
{{router}}
{{controller}}
{{service}}
{{types}}

# hklib中的封装好的公共方法使用参考（直接调用即可）：
{{third_lib}}

## 许多通用方法会被封装在hklib库中，调用方式可能包含
```go
package controllers

import (
	"context"
	"strconv"
	"strings"

	"icode.baidu.com/baidu/haokan-go/hklib/client"
	"icode.baidu.com/baidu/haokan-go/hklib/common/ctx_util"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils/feed_tpl"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils/monitor"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils/userbox"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils/userbox/userbox_dto"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils/videobox"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils/videobox/videobox_dto"
)


```

## hklib以及相关封装的第三方方法，通常会返回一个error，如果调用第三方库方法，请务必处理error，例如：
```go
returnList, err := hk_utils.GetList(ctx, "")
if err != nil {
    return ctx_util.CtxResponse(ctx, err, res)
}
```

# gdp框架项目结构参考（仅供参考理解，项目结构无需生成输出）：
{{framework}}

# 生成要求:
## 请严格遵守需求描述中所给出的数据类型。
## 请严格遵守需求中所给出的调用逻辑
## 特别注意，Router层的HandleFunc只生成新注册的路由，去掉原先存在在示例中的HandleFunc，且http方法全部使用Post
## 其中service层实现业务逻辑所用到的方法需要参考第三方库知识，第三方库知识来源于hklib以及下游子库，或者其他在需求中指定的库方法
## 示例代码中func、struct、const等命名均为示例名，需要根据需求改成接口实际的名字
## 请深入解析需求描述中的接口逻辑，参照示例指定项目结构，根据理解逐步在相应层级的文件中尽可能完整地生成需求对应逻辑代码
## 特别注意缩写词如http、api、id、uid、cuid等在命名时必须大写，示例：以`uid`为例，驼峰命名`TestUID`
## 注意所有生成的结构体及其变量、常量必须生成一对一对应的注释，其中导出的函数、结构体必须采用`//方法名 ...`、`//结构体名 ...`的方式进行注释
## 设计参数处理等公共逻辑，请参考示例编写。

# 输出要求：
    给出生成的代码，以及文件路径
    文件路径以及方法命名，按照接口路径改写，形如test_some_thing.go
    写全代码，禁止省略代码

# 输出格式参考如下：
文件路径：`具体文件路径`
```go
```