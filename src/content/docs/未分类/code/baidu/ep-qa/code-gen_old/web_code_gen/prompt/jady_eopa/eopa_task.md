---
title: "eopa_task"
description: "请根据提供的接口信息，包括请求地址、请求参数和响应参数，帮我编写请求第三方平台接口的代码： 接口信息如下： {{requirement}} {{webpage}}"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\jady_eopa\\eopa_task.md"
---
请根据提供的接口信息，包括请求地址、请求参数和响应参数，帮我编写请求第三方平台接口的代码：
## 接口信息如下：
{{requirement}}
{{webpage}}

## 代码结构示例如下：

### 实例注册
#### 文件路径：`models/service/data/proxy/proxy_register.go`
#### 首先需要在externalTypeMapping下注册对应的实例函数，Example为平台名称
```go
var externalTypeMapping = map[int]externalTypeInitFunc{
	TaskTypeProxyExample:      NewProxyExample,
}
```

### 参数配置 
#### 部分参数需要从配置中读取，需要按平台定义ProxyExampleConf结构体
#### 文件路径：`models/service/data/proxy/proxy_common.go`
```go
type ProxyBaseConf struct {
	Host   string `json:"host"`
	Port   string `json:"port"`
	Path   string `json:"path"`
	Method string `json:"method"`
	Scheme string `json:"scheme"`
}

// ProxyExampleConf 代理xx配置
type ProxyExampleConf struct {
	// 根据实际情况补充
	ProxyBaseConf
}
```

### 接口调用
#### 文件路径：`models/service/data/proxy/proxy_平台名称.go`
```go
package data

import (
	"encoding/hex"
	"encoding/json"
	"errors"
	"fmt"
	"net/url"
	"sort"
	"strconv"
	"strings"
	"time"

	ualib "icode.baidu.com/baidu/jady/ug-commonlib/ua"

	"icode.baidu.com/baidu/jady/eopa-task/library/extends"
	"icode.baidu.com/baidu/jady/eopa-task/models/dao"
)


// ExampleRequest 请求结构体
type ExampleRequest struct {
	//根据实际情况填写
}


// ExampleResponse 返回信息
type ExampleResponse struct {
	//根据实际情况填写
}


// ProxyExample ...
type ProxyExample struct {
	*baseExternalType
	ctx           *extends.WebContext
	proxyConf     *ProxyExampleConf
	params        *ExampleRequest
	NowTimeFormat string
}

// NewProxyExample returns a new ProxyExample
func NewProxyExample(ctx *extends.WebContext, conf *dao.ExternalTask) ExternalType {
	return &ProxyExample{
		newBaseExternalType(ctx, conf),
		ctx,
		&ProxyExampleConf{},
		&ExampleRequest{},
		time.Now().Format("2006-01-02 15:04:05"),
	}
}

// ParseParams 解析参数
func (p *ProxyExample) ParseParams() error {
	// 获取配置
	conf, err := p.unmarshle(p.conf.Config)
	if err != nil {
		p.ctx.AddNotice("unmarshle-example-conf-fail", err.Error())
		return err
	}
	p.proxyConf = conf

	// 解析其他参数，例如
	// 默认值
	// p.params.AppName = "baiduboxapp"
	// p.params.AppVersion = "1.0"
	// p.params.Platform = "android"
	// 尝试获取请求头中的User-Agent字段
	// if ua, ok := p.ctx.Request.Header("User-Agent"); ok {
	// 	 appName, ver := ualib.GetAppNameAndVersion(ua)
	// 	 if ver != "" && appName != "" {
	//		p.params.AppName = appName.String()
	//		p.params.AppVersion = ver
	// 	 }
	// 	 p.params.Platform = ualib.GetSystem(ua)
	// }

	// 解析参数
	// p.params.Token = p.GetParamByKey("token", "")

	return nil
}



// DoRal 发送请求 
func (p *ProxyExample) DoRal() error {
	bodyParams := map[string]interface{}{
		// 根据实际情况填写，例如
		// "method":      "taobao.pentaprism.task.trigger.from",
		// "app_key":     p.proxyConf.AppKey,
		// "timestamp":   p.NowTimeFormat, // 当前时间 2020-09-30 12:27:16
	}

	// 如果需要，生成签名
	Params["sign"] = p.encryption(bodyParams)

	// 发送请求
	item := &RalItem{

		Host:   p.proxyConf.Host,
		Path:   p.proxyConf.Path,
		Method: p.proxyConf.Method,
		Header: map[string][]string{"Content-Type": {"application/x-www-form-urlencoded"}},
		Body:   bodyParams,
	}
	resp, err := p.Do(item)
	if err != nil {
		return err
	}
	return p.FormatResp(resp)
}


// unmarshle 将字符串反序列化为 ProxyExampleConf 结构体指针
func (p *ProxyExample) unmarshle(conf string) (*ProxyExampleConf, error) {
	exampleConf := &ProxyExampleConf{}
	err := json.Unmarshal([]byte(conf), exampleConf)
	if err != nil {
		p.ctx.AddNotice("unmarshle-example-conf-fail", err.Error())
		return exampleConf, err
	}
	return exampleConf, nil
}


// GetResult 获取返回信息
func (p *ProxyExample) GetResult() interface{} {
	return map[string]interface{}{
		"scheme": p.proxyConf.Scheme,
		"schema": p.proxyConf.Scheme,
	}
}

// FormatResp 格式化返回信息
func (p *Example) FormatResp(resp interface{}) error {
	m, ok := resp.(map[string]interface{})
	if !ok {
		return errors.New("external-biz-resp-not-a-map")
	}

	// 根据实际响应结构，检查是否正常响应，例如
	// res, ok := m["response"].(map[string]interface{})
	// if !ok {
	// 	return errors.New("xx-res-no-map")
	// }
	// code, ok:= res["code"]
	// if !ok {
	// 	return errors.New("alipay-ret-no-code")
	// }
	// 假设10000是响应成功的状态码
	// if code != "10000" { 
	// 	return fmt.Errorf("alipay-ret-error:%v", res["result_desc"])
	// }

	return nil
}
	
// encryption 生成签名
func (p *ProxyExample) encryption(data map[string]interface{}) string {
	keys := make([]string, 0, len(data))
	for k := range data {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	var signStr = ""
	for _, key := range keys {
		value := keys[key]
		signStr = signStr + fmt.Sprintf("%v%v", key, value)
	}
	// 具体的签名根据需求描述生成，例如使用hmac-sha256，需要实现HmacSha256方法
	// sign := strings.ToUpper(p.HmacSha256(signStr))
	return sign
}
```


## 生成要求:
### 请求/响应结构体中的参数根据实际情况定义，并为参数生成注释，注意多级结构的struct不要嵌套
### 生成时需要将示例中的example替换为实际的平台名称
### 涉及到签名需要根据需求描述来实现encryption方法，并且使用crypto包实现对应的签名算法，否则不需要生成
### 进行必要的错误校验

## 输出要求：
    给出生成的代码以及文件路径
    写全代码，禁止省略代码