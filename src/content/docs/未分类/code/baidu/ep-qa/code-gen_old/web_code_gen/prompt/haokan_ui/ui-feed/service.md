---
title: "service"
description: "import \"context\" \"encoding/json\" \"net/url\" \"sort\" \"strconv\" \"strings\" \"time\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\haokan_ui\\ui-feed\\service.md"
---
## service层代码
* 文件路径：`services/playlet_service.go`
```go
package services

import (
	"context"
	"encoding/json"
	"net/url"
	"sort"
	"strconv"
	"strings"
	"time"

	"icode.baidu.com/baidu/haokan-go/hklib/base_utils"
	"icode.baidu.com/baidu/haokan-go/hklib/hk_utils"
	"icode.baidu.com/baidu/haokan-go/ui-feed/bootstrap/dao"
	"icode.baidu.com/baidu/haokan-go/ui-feed/bootstrap/hk_logger"
	"icode.baidu.com/baidu/haokan-go/ui-feed/models/dto"
	"icode.baidu.com/baidu/haokan-go/ui-feed/models/response"
)

// 获取短剧ID简单例子，演示了如何使用封装了一层的Redis，以及Redis没有找到数据后的兜底
func GetPlayletIDs(ctx context.Context) ([]string, bool) {
	pvListAll, _ := dao.RedisHaokanPlayletSeries.ZRevRange(ctx, PVPlayletKey, 0, -1).Result()

	if len(pvListAll) > 0 {
		return pvListAll, false
	}

	if len(pvListAll) == 0 {
		monitor.AddSiaLog(ctx, library.MonitorPlayletPVEmpty, "1")
	}

	// 没取到时 使用iconf兜底配置
	collectionIDs := iconf_client.GetStringValueWithAppGroup("pm_config", "collection_ids", "")
	res := strings.Split(collectionIDs, ",")
	if len(res) > 0 {
		return res, true
	}

	// 兜底配置
	for k := range library.PlayletResource {
		res = append(res, k)
	}
	return res, true
}
```

## GDP框架中的nshead包
```go
// @Desc:	 nshead request
// @Author:	 陈志峰(chenzhifeng01@baidu.com)
// @Date:	 2020-07-13 19:47:12

package nshead

import (
	"context"
	"fmt"
	"math"
	"net"
	"strconv"
	"sync"
	"time"

	"icode.baidu.com/baidu/gdp/codec"
	"icode.baidu.com/baidu/gdp/extension/limit"
	"icode.baidu.com/baidu/gdp/extension/option"
	"icode.baidu.com/baidu/gdp/logit"
	"icode.baidu.com/baidu/gdp/net/connector"
	"icode.baidu.com/baidu/gdp/net/ral"
)

// RalRequest 基本类实现 ral.Request
type RalRequest struct {
	// APIName 调用的 API 的名称，会用于日志、监控等
	APIName string

	// Header 可选，当需要自定义 nshead 头的时候使用
	Header *NsHead

	// Body 必填 发送的消息体，同时需要 设置正确的 Encoder
	Body interface{}

	// Encoder 是对数据做 Encode 的 Encoder 实例
	Encoder codec.Encoder

	// Hedging 是发请求时做 RalRequest Hedging 的配置
	Hedging limit.Hedging

	// bodyBytes 缓存从Body中读到的数据，便于重试
	bodyBytes []byte

	// Tracers _
	Tracers []ral.Tracer

	// TracerMeta
	TracerMeta *ral.TracerMeta
}

// Protocol 协议名称,返回固定值 nshead
func (req *RalRequest) Protocol() string {
	return "nshead"
}

// Name 请求名称
func (req *RalRequest) Name() string {
	return "nshead"
}

// String 用于描述请求的内容
func (req *RalRequest) String() string {
	if req == nil {
		return "nil"
	}
	return req.APIName
}

// TracerType nshead 协议 tracer 类型
var TracerType ral.TracerType = ral.NewTracerType()

// RegisterTracer 注册 tracer
func (req *RalRequest) RegisterTracer(tracers ...ral.Tracer) error {
	if len(req.Tracers) == 0 {
		req.Tracers = make([]ral.Tracer, 0, len(tracers))
	}
	for _, tracer := range tracers {
		if tracer.Type() == TracerType || tracer.Type() == ral.TracerTypeGeneral {
			req.Tracers = append(req.Tracers, tracer)
		}
	}
	return nil
}

// Do 实现 ral.Request，发起 NsHead 请求。
// 要求传入的 RalResponse 实现 RalResponseHandler 接口
func (req *RalRequest) Do(ctx context.Context, resp ral.Response, cnctr connector.Connector, opt option.Option) (err error) {
	return req.roundTrip(ctx, resp.(RalResponseHandler), cnctr, opt)
}

// roundTrip 发起请求并将第一个成功的请求数据交给 RalResponseHandler 处理。
func (req *RalRequest) roundTrip(ctx context.Context, respHdlr RalResponseHandler, cnctr connector.Connector, opt option.Option) (err error) {
	var buildOnce sync.Once
	var errPack error
	raw := &ral.RawRequest{
		APIName:      req.String(),
		ProtocolName: req.Protocol(),
		Tracers:      req.Tracers,
		TracerMeta:   req.TracerMeta,
		Hedging:      req.Hedging,
		BuildRequest: func(ctx context.Context, opt option.Option, addr net.Addr) (interface{}, error) {
			buildOnce.Do(func() {
				errPack = req.preloadBody(ctx)
			})
			return req.bodyBytes, errPack
		},

		WriteRead: func(ctx context.Context, conn net.Conn, payload interface{}) (resp interface{}, err error) {
			return req.writeRead(ctx, conn, payload, opt)
		},

		HandleResponse: func(ctx context.Context, respRaw interface{}, handler ral.Response) error {
			ret := respRaw.(*HeadBody)
			return handler.(RalResponseHandler).HandleResponse(ctx, ret.Head, ret.Body)
		},
	}
	if len(req.Tracers) > 0 && req.TracerMeta == nil {
		defer func() {
			req.TracerMeta = raw.TracerMeta
		}()
	}
	return raw.Do(ctx, respHdlr, cnctr, opt)
}

func (req *RalRequest) writeRead(ctx context.Context, conn net.Conn, payload interface{}, opt option.Option) (interface{}, error) {
	defer conn.Close()
	cli := NewReadWriter(conn)
	if req.Header != nil {
		cli.SetWriteHeader(req.Header.Clone())
	}
	req.setLogID(ctx, cli.GetWriteHeader())

	writeTimeout := option.WriteTimeout(opt)
	_ = conn.SetWriteDeadline(time.Now().Add(writeTimeout))

	_, err1 := cli.Write(payload.([]byte))
	if err1 != nil {
		return nil, err1
	}

	readTimeout := option.ReadTimeout(opt)
	_ = conn.SetReadDeadline(time.Now().Add(readTimeout))

	hd, body, err2 := cli.ReadHeadBody()
	if err2 != nil {
		return nil, err2
	}
	ret := &HeadBody{
		Head: hd,
		Body: body,
	}
	return ret, nil
}

func (req *RalRequest) setLogID(ctx context.Context, h *NsHead) {
	if h.LogID == 0 {
		if logid := req.findLogID(ctx); logid > 0 {
			h.LogID = logid
		}
	}
}

func (req *RalRequest) findLogID(ctx context.Context) uint32 {
	if logField := logit.FindLogIDField(ctx); logField != nil {
		id, _ := strconv.ParseUint(fmt.Sprint(logField.Value()), 10, 64)
		if id < math.MaxUint32 {
			return uint32(id)
		}
		// 保留低位，如  4294967297  -> 294967297
		return uint32(id % 1e9)
	}
	return 0
}

// preloadBody 预先将body加载到bytes数据中，使于并发重复读取。
func (req *RalRequest) preloadBody(_ context.Context) (err error) {
	if req.Body == nil {
		return nil
	}
	req.bodyBytes, err = codec.Pack(req.Body, req.Encoder)
	return err
}

var _ ral.Request = (*RalRequest)(nil)

```

### 通常，如果返回为空或者返回列表长度为0等情况发生，需要写入日志，并返回错误。
```go
	import {
		"icode.baidu.com/baidu/haokan-go/ui-feed/library"
		"icode.baidu.com/baidu/haokan-go/ui-feed/bootstrap/hk_logger"
	}
	
	if err != nil || len(ExampleList) == 0 {
		hk_logger.Logger.Warning(ctx, "err info", logit.AutoField("errorContent", ExampleList))
		return nil, library.ExampleListErrorType
	}
```

