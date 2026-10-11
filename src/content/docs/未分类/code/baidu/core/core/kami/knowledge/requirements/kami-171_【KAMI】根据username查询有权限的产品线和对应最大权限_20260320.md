---
title: "kami-171 [Story] 【KAMI】根据username查询有权限的产品线和对应最大权限"
description: "- 卡片 ID：kami-171 - 类型：Story - 状态：开发中 - 负责人：maxiaolong01 - 日期：2026-03-20"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\core\\.kami\\knowledge\\requirements\\kami-171_【KAMI】根据username查询有权限的产品线和对应最大权限_20260320.md"
---
# kami-171 [Story] 【KAMI】根据username查询有权限的产品线和对应最大权限

## 卡片信息

- **卡片 ID**：kami-171
- **类型**：Story
- **状态**：开发中
- **负责人**：maxiaolong01
- **日期**：2026-03-20

## 需求描述

在 kamixmgt 下新增 AuthController，提供根据 username 查询其有权限的产品线和最大权限的接口，业务逻辑放在 AuthService 里。接口不需要鉴权，加入白名单。

## 权限模型说明

AuthPo.access 含义：
- 0-super：超管，有所有模块权限
- 1-二级产品线admin：product_id 即 moduleId
- 2-write：product_id 即 moduleId
- 3-read：product_id 即 moduleId
- 4-一级产品线admin：super_product_id 下所有 moduleId

同一 moduleId 有多条记录时，取 min(access) 作为最大权限。

## 涉及文件

**新建：**
- `entity/po/AuthPo.java` — qamate_auth 表对应 PO
- `entity/po/LazyoneProductPo.java` — lazyone_product 表对应 PO
- `mapper/AuthMapper.java` — @Repository("kamiAuthMapper") @DS("oldsource")
- `mapper/LazyoneProductMapper.java`
- `entity/req/UserAuthQueryReq.java` — 请求（username，必填）
- `entity/resp/UserProductAuthResp.java` — 响应（moduleId, moduleName, maxAccess, accessName）
- `service/AuthService.java` — Service 接口
- `service/impl/AuthServiceImpl.java` — Service 实现
- `controller/AuthController.java` — POST /kami/v2/auth/user/product/list

**修改：**
- `mapper/ModuleAgentConfigMapper.java` — 新增 findAllModuleIds()
- `components/config/FilterConfig.java` — 白名单新增 /kami/v2/auth/user/product/list

## 实现要点

1. 查 qamate_auth（username=?, valid=1, account_type=0）
2. 按 access 类型展开 moduleId 列表：
   - access=0：findAllModuleIds() 取全量
   - access=4：findModuleIdsBySuperProductId(super_product_id)
   - 其他：product_id 直接作为 moduleId
3. Map<moduleId, minAccess> 去重取最大权限
4. 批量查 lazyone_product 取 moduleName
5. 组装返回，accessName 映射：0→super, 1→二级产品线admin, 2→write, 3→read, 4→一级产品线admin

## 注意事项

- kamixmgt 包内新建了 AuthMapper，与 othermgt 包的 AuthMapper 同名，使用 @Repository("kamiAuthMapper") 解决 Bean 冲突，注入时用 @Resource(name = "kamiAuthMapper")

## 接口文档

**POST** `/core/kami/v2/auth/user/product/list`，无需鉴权

请求：
```json
{
  "username": "hanqiqi01"
}
```

返回：
```json
{
  "code": 0,
  "msg": "SUCCESS",
  "data": [
    {
      "moduleId": 12345,
      "moduleName": "商业小刚",
      "maxAccess": 1,
      "accessName": "二级产品线admin"
    }
  ]
}
```
