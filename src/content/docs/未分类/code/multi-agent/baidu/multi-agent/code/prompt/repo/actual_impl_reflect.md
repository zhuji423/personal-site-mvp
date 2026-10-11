---
title: "actual_impl_reflect"
description: "根据上面的分析结果，给出最终格式化的答案： - 如果需要保留所有实现，则返回： json { \"keepallimpl\": true } - 如果只保留与当前接口直接相关的实现，则返回需要保留的函数签名： json { \"keepallim"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\repo\\actual_impl_reflect.md"
---
根据上面的分析结果，给出最终格式化的答案：
- 如果需要保留所有实现，则返回：
```json
{
   "keep_all_impl": true
}
```
- 如果只保留与当前接口直接相关的实现，则返回需要保留的函数签名：
```json
{
   "keep_all_impl": false,
   "actual_impl": ["完整的函数签名"]
}
```