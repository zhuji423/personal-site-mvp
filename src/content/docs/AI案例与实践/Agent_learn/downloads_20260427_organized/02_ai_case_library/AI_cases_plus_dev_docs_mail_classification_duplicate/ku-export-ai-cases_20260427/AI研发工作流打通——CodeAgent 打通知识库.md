---
title: "知识库 MCP Server 配置指南（Claude Code & Cursor）"
description: "AI研发工作流打通——CodeAgent 打通知识库"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI研发工作流打通——CodeAgent 打通知识库.md"
---
AI研发工作流打通——CodeAgent 打通知识库

#### 🧑‍🏫 案例作者：[@刘国元](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：设计、开发、通用
#### 🔧 使用工具：数字员工、Cursor、Claude
#### 📒 案例概要：本文介绍如何在Claude Code与Cursor中配置百度知识库MCP Server，实现AI工具直接读写知识库。Claude Code需通过curl调用JSON-RPC接口；Cursor因网络与认证问题，需通过本地HTTP代理中转并注入鉴权头。文档提供了详细配置步骤、可用工具列表（如查询、创建、管理文档）及数据提取方法。
开发者协议：

* 按照最小必要原则申请、使用数据，不必要时不存储原始数据。
* 按照用户知情同意原则处理个人信息，对不必要的个人信息做好脱敏。
* 数据使用过程做到加密传输、加密存储、访问留痕、不使用时及时销毁。
* 做好数字员工及其API数据权限及生命周期管理，定期维护与清理，并承担数据安全及其管理责任。
* 如需使用大模型等分析聊天内容，必须使用百度内部模型，避免如流数据脱离百度内部环境。

注意：

* 注意严格限制数字员工对知识库等厂内组件的操作权限，尽量只读，严禁授予删除等高危权限。
* 注意遵守厂内安全规范，严格限制 Agent 权限，务必使用private mode、限制 Agent 读取配置文件等。

# 知识库 MCP Server 配置指南（Claude Code & Cursor）
本文介绍如何在 Claude Code 和 Cursor 中接入百度知识库 MCP Server（`ku_open_api`），实现 AI 工具直接读写知识库文档。

---

## 基本信息
|项目|值|
|-|-|
|MCP Server 名称|`ku_open_api`|
|传输协议|`streamableHttp`|
|端点 URL|`https://mcp-proxy.baidu-int.com/server/ku_open_api/mcp-plugin-center/mcp/`|
|鉴权方式|自定义请求头 `ak` / `sk`|
|Accept 头|必须同时包含 `application/json, text/event-stream`|

> **注意**：URL 末尾必须带 `/`，否则服务端返回 307 重定向，POST body 会丢失。
---

## 一、在 Claude Code 中配置
### 配置文件
编辑 `~/.claude/.mcp.json`：

```
{
  "mcpServers": {
    "ku_open_api": {
      "url": "https://mcp-proxy.baidu-int.com/server/ku_open_api/mcp-plugin-center/mcp/",
      "headers": {
        "ak": "<your_ak>",
        "sk": "<your_sk>"
      },
      "type": "streamableHttp",
      "timeout": 30
    }
  }
}
```
### 已知限制
Claude Code 当前版本对 `streamableHttp` 类型 MCP Server **不能在会话内自动注册为原生工具**（`ListMcpResourcesTool` 找不到该 server），即使配置文件在会话启动前已存在。

**绕过方案**：直接通过 `Bash curl` 调用 MCP JSON-RPC 接口。

### curl 调用模板
```
curl -L -s -X POST 'https://mcp-proxy.baidu-int.com/server/ku_open_api/mcp-plugin-center/mcp/' \
  -H 'ak: <your_ak>' \
  -H 'sk: <your_sk>' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"queryContent","arguments":{"url":"<知识库文档链接>"}}}'
```
响应为 SSE 格式，Python 解析示例：

```
lines = [l for l in raw.split('\n') if l.startswith('data:')]
data = json.loads(lines[0][5:])
```
---

## 二、在 Cursor 中配置
### Cursor 无法直连的根因
Cursor 接入 `streamableHttp` MCP Server 存在两个问题：

1. **ECONNRESET**：Cursor（Electron 应用）不继承终端的系统代理 / VPN，无法直连百度内网域名。
2. `headers`** 字段无效**：Cursor MCP SDK 走 OAuth 2.0 认证流程，不读取配置中自定义的 `ak`/`sk` header。

### 解决方案：本地代理中转
在本地起一个轻量 HTTP 代理，注入鉴权 header 后转发至百度内网，Cursor 只需连本地代理。

#### Step 1：创建代理脚本
保存为 `~/.claude/local_ku_proxy.py`（已预置，可直接使用）：

```
import urllib.request, urllib.error
from http.server import HTTPServer, BaseHTTPRequestHandler

TARGET = "https://mcp-proxy.baidu-int.com/server/ku_open_api/mcp-plugin-center/mcp/"
AUTH_HEADERS = {"ak": "<your_ak>", "sk": "<your_sk>"}
LISTEN_HOST, LISTEN_PORT = "127.0.0.1", 7890

class ProxyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        req = urllib.request.Request(TARGET, data=body, method="POST")
        for k, v in AUTH_HEADERS.items():
            req.add_header(k, v)
        req.add_header("Content-Type", self.headers.get("Content-Type", "application/json"))
        req.add_header("Accept", "application/json, text/event-stream")
        try:
            with urllib.request.urlopen(req) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.send_header("Content-Type", resp.headers.get("Content-Type", "text/event-stream"))
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            err_body = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(err_body)))
            self.end_headers()
            self.wfile.write(err_body)

    def do_GET(self):
        body = b'{"status":"ok","proxy":"ku_open_api"}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"[ku-proxy] {self.address_string()} - {fmt % args}")

if __name__ == "__main__":
    server = HTTPServer((LISTEN_HOST, LISTEN_PORT), ProxyHandler)
    print(f"[ku-proxy] 监听 http://{LISTEN_HOST}:{LISTEN_PORT}/")
    server.serve_forever()
```
#### Step 2：启动代理
```
python3 ~/.claude/local_ku_proxy.py &

# 验证
curl http://127.0.0.1:7890/
# 预期返回: {"status":"ok","proxy":"ku_open_api"}
```
> **注意**：系统重启后需重新执行上述命令启动代理。
#### Step 3：配置 Cursor
编辑 `~/.cursor/mcp.json`（或通过 Cursor 设置 → MCP 页面添加）：

```
{
  "mcpServers": {
    "ku_open_api": {
      "url": "http://127.0.0.1:7890/",
      "type": "streamableHttp"
    }
  }
}
```
重启 Cursor，MCP Server 应显示为已连接状态。

---

## 三、可用工具列表
|工具名|用途|必填参数|
|-|-|-|
|`queryContent`|读取文档正文（块结构）|`url` 或 `docId`|
|`pageByRepo`|分页查询知识库文档列表|`repoId`|
|`createDoc`|创建文档（支持 Markdown）|`repositoryGuid`|
|`copyDoc`|复制文档|`docId`|
|`moveDoc`|移动文档|`docId`, `toRepoGuid`|
|`deleteDoc`|删除文档|`docId`|
|`changeScope`|修改文档可见范围（私密 `20` / 公开可读 `5` / 公开可编辑 `6`）|`docId`, `scope`|
|`queryUserPermission`|查询用户权限|`docId`|
|`addUserPermission`|添加用户权限|`docId`, `usernames`, `roleName`|
|`updateUserPermission`|修改用户角色|`docId`, `username`, `roleName`|
|`queryComments`|查询文档评论|`docId`|
|`queryRecentView`|查询文档浏览记录|`docId`|
|`queryUserInfo`|查询用户信息|`username`|
|`queryFlowchart`|获取流程图数据|`docGuid`, `flowchartId`|
|`downloadAttachments`|下载附件（zip 流）|`docGuid`|

> **权限说明**：`createDoc`、`deleteDoc`、`moveDoc` 等写操作需要 ak 申请对应 API 权限，只读 ak 调用会返回错误码 `60411`。
---

## 四、queryContent 返回结构说明
文档以**块嵌套结构**返回（非纯文本），需递归提取文字：

```
result.content[]               ← block 列表
  └── children[]               ← 子块或叶子节点
        └── { "text": "..." }  ← 实际文字
```
Python 提取示例：

```
import json

def extract_paragraphs(blocks):
    paragraphs = []

    def collect(node):
        if isinstance(node, list):
            for item in node:
                collect(item)
        elif isinstance(node, dict):
            children = node.get("children", [])
            if children:
                all_leaf = all(
                    isinstance(ch, dict) and isinstance(ch.get("text"), str)
                    for ch in children
                )
                if all_leaf:
                    line = "".join(ch["text"] for ch in children)
                    if line.strip():
                        paragraphs.append(line)
                else:
                    collect(children)

    collect(blocks)
    return paragraphs

# 使用示例
raw = "<curl 响应>"
lines = [l for l in raw.split('\n') if l.startswith('data:')]
data = json.loads(lines[0][5:])
inner = json.loads(data['result']['content'][0]['text'])
blocks = inner['result']['content']
print('\n'.join(extract_paragraphs(blocks)))
```
---

## 五、URL 与 ID 提取规则
```
https://ku.baidu-int.com/knowledge/{repoId}/{...}/{...}/{docId}
```
* `repoId`：`/knowledge/` 后第一段，用于 `pageByRepo`、`createDoc` 的 `repositoryGuid`
* `docId`：URL 最后一段，用于 `queryContent`、`queryComments`、`deleteDoc` 等



# 参考
[🗂️ 知识库开放能力](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/83jpltYsT1u0cu#anchor-docyg-9d29c9cc-e937-11f0-9ea5-993bcd03966f?t=mention&mt=doc&dt=doc)

[如流知识库开放API的MCP介绍](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/nClcfHbEv8/VjAFmeoRCplvIq?t=mention&mt=doc&dt=doc)

[「数字员工」创建指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/ewNKeMwvuP/z-qUc6Ncl9LfrA?t=mention&mt=doc&dt=doc)

[Cursor清理历史配置及设置隐私模式使用手册](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/BMaLudR2QF/vQV2GNoZP5/CZwADxuk_J07cE?t=mention&mt=doc&dt=doc)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
