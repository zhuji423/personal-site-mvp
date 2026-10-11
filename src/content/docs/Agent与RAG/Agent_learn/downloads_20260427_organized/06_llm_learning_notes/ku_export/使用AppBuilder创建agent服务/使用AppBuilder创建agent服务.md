---
title: "使用AppBuilder创建agent服务"
description: "func browserHapFindUa, matchStr, name, browserID string, res BrowserInfo int { UALow := strings.ToLowerUa uaLen := lenUA"
date: "2026-04-28"
category: "Agent与RAG"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\使用AppBuilder创建agent服务\\使用AppBuilder创建agent服务.md"
---
# 使用AppBuilder创建agent服务
一、背景单测生成场景：为函数生成单测，举个例子

func browserHapFind(Ua, matchStr, name, browserID string, res *BrowserInfo) int {	UALow := strings.ToLower(Ua)	uaLen := len(UALow)	if uaLen == 0 || uaLen < 10 {		return -1	}	if pos := strings.Index(UALow, "hap/"); pos == -1 {		return -1	}	if pos := strFind(UALow, "packagename"); pos == -1 {		return -1	}	nextPos := strings.Index(UALow, matchStr)	if nextPos == -1 {		return -1	}	res.MobileBrowser = name	res.Browser = name	res.MobileBrowserID = browserID	return 0}二、创建agent应用1、创建工具组件![](/personal-site-mvp/img/doc-placeholder.svg)



![](/personal-site-mvp/img/doc-placeholder.svg)

2、创建应用这里的组件类似于coze中的工作流

package mainimport (	"strings"	"testing"	"github.com/stretchr/testify/assert")type BrowserInfo struct {	Browser        string	MobileBrowser  string	BrowserID      string	MobileBrowserID string}func Test_browserHapFind(t *testing.T) {	var res BrowserInfo	ret := browserHapFind("", "test", "testName", "testID", &res)	assert.Equal(t, -1, ret)	ret = browserHapFind("testUa", "hap/", "testName", "testID", &res)	assert.Equal(t, -1, ret)	ret = browserHapFind("hap/1.0 testUa", "version/", "testName", "testID", &res)	assert.Equal(t, -1, ret)	ret = browserHapFind("hap/1.0 packagename=com.example.app nonexistent/1.0.0 Chrome/xx.x.xxxx.xx Mobile", "nonexistent/", "testName", "testID", &res)	assert.Equal(t, -1, ret)	ret = browserHapFind("hap/1.0 packagename=com.example.app version/1.0.0 Chrome/xx.x.xxxx.xx Mobile", "version/", "testName", "testID", &res)	assert.Equal(t, 0, ret)	assert.Equal(t, "testName", res.Browser)	assert.Equal(t, "testName", res.MobileBrowser)	assert.Equal(t, "testID", res.MobileBrowserID)}三、发布使用1、发布![](/personal-site-mvp/img/doc-placeholder.svg)

2、使用支持页面使用与sdk使用

页面使用![](/personal-site-mvp/img/doc-placeholder.svg)

试用地址：https://appbuilder.baidu.com/s/T1lQoJ7A

sdk使用import appbuilderimport osos.environ["APPBUILDER_TOKEN"] = ''app_id = '93585567-7f08-4f08-8aa5-ba5b1d015829'  # 已发布AppBuilder应用ID# 初始化智能体builder = appbuilder.AppBuilderClient(app_id)# 创建会话conversation_id = builder.create_conversation()# 运行对话with open('tool/data/file') as fp:    func = fp.read()  # file中为函数体文本out = builder.run(conversation_id, func)# 打印会话结果print(out.content.answer)![](/personal-site-mvp/img/doc-placeholder.svg)





