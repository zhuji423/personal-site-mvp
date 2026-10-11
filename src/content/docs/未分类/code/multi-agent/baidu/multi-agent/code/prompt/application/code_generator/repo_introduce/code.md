---
title: "硬编码字符串规范"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\code.md"
---
# 硬编码字符串规范
- **使用常量定义字符串字面量**
  - 所有 Mode、Type、Status、Key、Action 等字符串字面量必须定义为常量，禁止硬编码 
  - 常量统一放在 const 块内，名称使用大写驼峰，如：
```go
const (
   ModeCoupon = "coupon"
)
```
示例
```go
if params.Mode == ModeCoupon {
    couponInfo, err := c.getCommunityCouponInfo(ctx, uid)
    if err != nil {
        return nil, err
    }
    resp.CouponInfo = couponInfo
}
```