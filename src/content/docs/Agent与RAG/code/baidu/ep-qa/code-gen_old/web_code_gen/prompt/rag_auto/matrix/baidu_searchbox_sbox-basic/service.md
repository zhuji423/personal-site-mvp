---
title: "service"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\matrix\\baidu_searchbox_sbox-basic\\service.md"
---
## service层实现的导出方法，必须在指定目标文件`model/service/ddmission/service.go`（该路径为固定路径）添加生成的导出方法声明，示例如下：
* 此文件仅需生成追加内容即可，不要导包。
```go
// TestFunc ...
TestFunc(ctx context.Context, req request.TestReq) (*response.TestResp, error)
```