---
title: "pdcms 编码规则"
description: "rule := foundation.GetPdCmsRulectx list, err := pdcms.APP.GetOpDatapdcmsDefaultQuery, rule if err = nil { return nil, er"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\pdcms.md"
---
# pdcms 编码规则
**pdcms主要是针对B端页面上配置的数据获取进行请求的封装**  
pdcms 相关写法可以参考以下示例：
```go
func (s *service) FetchDefaultQueryPDCMSData(ctx context.Context) (*dto.PdcmsDefaultData, error) {
	var result []dto.PdcmsDefaultData

	rule := foundation.GetPdCmsRule(ctx)
	list, err := pdcms.APP().GetOpData(pdcmsDefaultQuery, rule)
	if err != nil {
		return nil, errno.ErrPdcmsGet
	}
	if len(list) == 0 || len(list[0].Assets) == 0 {
		return nil, errno.ErrPdcmsNotFount
	}

	item := list[0]
	assetJSON, err := json.Marshal(item.Assets)
	if nil != err {
		return nil, errno.ErrPdcmsNotFount
	}

	if err = json.Unmarshal(assetJSON, &result); err != nil {
		return nil, errno.ErrPdcmsNotFount
	}

	if len(result) == 0 {
		return nil, errno.ErrPdcmsNotFount
	}

	queryList := result[0]

	return &queryList, nil
}
````
1.调用方式
使用统一入口：
```go
    list, err := pdcms.APP().GetOpData(queryKey, rule)
```
 1) pdcms.APP()：获取 PDCMS SDK 实例。
 2) GetOpData(queryKey, rule)：按规则从 PDCMS 拉取指定配置。
 3) rule := foundation.GetPdCmsRule(ctx)：上下文内统一获取拉取规则。
 规范：所有服务从 PDCMS 拉取数据时，必须通过 foundation.GetPdCmsRule(ctx) 获取当前 rule
 
2.错误处理
1) 请求异常
```go
    if err != nil {
	    return nil, errno.ErrPdcmsGet
    }
```
① 当调用 GetOpData 出错，统一返回 errno.ErrPdcmsGet。
② 不直接暴露底层 error，以保持上层统一处理。
2) 数据为空
```go
    if len(list) == 0 || len(list[0].Assets) == 0 {
        return nil, errno.ErrPdcmsNotFount
    }
```
若结果为空或 Assets 为空，统一返回 errno.ErrPdcmsNotFount。
3) 序列化/反序列化错误
```go
    assetJSON, err := json.Marshal(item.Assets)
    if err != nil {
        return nil, errno.ErrPdcmsNotFount
    }
    if err = json.Unmarshal(assetJSON, &result); err != nil {
        return nil, errno.ErrPdcmsNotFount
    }
```
① 所有 JSON 处理异常统一视为“未找到配置”。
② 不区分序列化/反序列化阶段。
4) 最终数据为空
```go
    if len(result) == 0 {
        return nil, errno.ErrPdcmsNotFount
    }
```
3.数据结构约定
① 原始返回：[]dto.PdcmsDefaultData 是数组，但通常只使用首项 list[0]。
② Assets 字段为复杂结构，需 json.Marshal → json.Unmarshal 进行二次解析
③ 最终返回值为：*dto.PdcmsDefaultData