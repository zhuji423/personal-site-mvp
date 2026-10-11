---
title: "error"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\error.md"
---
## 错误处理规范
- **使用项目标准错误打印**
  - 出现错误一定要进行错误判断并使用 `logger.WarningF` 或者 `logger.ErrWF` 统一封装错误函数进行打印
  - 在关键流程节点记录日志，但避免过度记录
示例：
```go
    if err != nil {
        logger.WarningF(ctx, "getSIDByABTest ccs-gray get tokenmap err: %v", err)
    }
```
或者
```go
    if err != nil {
       logger.ErrWF(ctx, errno.ConfInitError, "gcp.Fetch err, appID=%s key=%s err=%v", constant.GCPMatrixAppID, gcpConsts.TaskPanelStyleExp, err)
    }
```