---
title: "一、企微接入Agent对内部员工、外部客服简单介绍，后面有具体实际操作流程"
description: "业务自建agent/openclaw提供企微（内/外部客户）使用实践+接入代码"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\业务自建agentopenclaw提供企微（内外部客户）使用实践+接入代码.md"
---
业务自建agent/openclaw提供企微（内/外部客户）使用实践+接入代码

#### 🧑‍🏫 案例作者：[@王琦](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：研发全流程
#### 🔧 使用工具：AppBuilder、OpenClaw
#### 📒 案例概要：企业微信接入Agent指南：通过微信客服（对外）和自建应用（对内）实现智能服务，需公网域名、HTTPS、API认证及消息加解密。
# 一、企微接入Agent对内部员工、外部客服简单介绍，后面有具体实际操作流程
将企业自有的Agent接入企业微信，主要有两条路径：**微信客服（对外的客户服务）** 和**企业微信自建应用（对内的员工助手）**。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9dbdfc691c1c440ab5cdfa723875dddc&docGuid=JgeTBfNP0qPsDe "")
### 🛠️ 路径一：接入“微信客服”（对外）
这种方式适合将你的Agent打造成一个对外的智能客服，客户可以在微信生态内（如品牌视频号、网页等）直接发起咨询。

|步骤|核心任务|关键操作与说明|
|-|-|-|
|**1. 准备Agent服务**|确保你的自有Agent已开发完成，并具备可通过API调用的接口（如`/v1/chat`），能接收问题并返回答案。||
|**2. 企微后台获取信息**|登录企业微信管理后台，进入**微信客服** > **账号管理**，创建一个客服账号。获取企业的**企业ID**和该客服账号的**Secret**。||
|**3. 在Agent开发平台配置**|在你的Agent开发平台（如腾讯云智能开发平台、自有后台）中，选择发布渠道为“微信客服”。填入上一步获取的**企业ID**和**Secret**。平台会生成回调配置所需的**URL、Token和EncodingAESKey**，请复制保存。||
|**4. 企微后台配置回调**|回到企业微信后台的客服账号详情页，找到“接收消息”或类似的配置入口，将上一步复制的**URL、Token和EncodingAESKey**填入并保存，完成连接验证。||
|**5. 发布与使用**|在Agent平台发布应用。发布成功后，你可以从平台获取该微信客服的二维码，将其配置在网页、小程序或视频号上，用户扫码即可与你的Agent对话。||

### 💼 路径二：接入“自建应用”（对内）
这种方式是将Agent作为企业内部工具，嵌入到企业微信的工作台中，供员工在单聊或群聊中使用。

|步骤|核心任务|关键操作与说明|
|-|-|-|
|**1. 准备Agent服务**|同样，确保你的自有Agent服务可用。同时，你需要**一个已备案的域名**，并配置好代理（如Nginx），将企业微信的请求转发到你的Agent服务。||
|**2. 企微后台创建应用**|登录企业微信管理后台，进入**应用管理** > **应用**，点击“创建应用”。填写应用信息并设置可见范围。创建成功后，记录下**企业ID**、应用的**AgentId**和**Secret**。||
|**3. 配置API接收**|在应用详情页的“功能”下找到“接收消息”，点击“设置API接收”。这里需要填入你准备好的**URL**，并自行生成**Token**和**EncodingAESKey**，保存后暂不关闭页面。||
|**4. 开发适配层**|这是技术开发的核心环节。你需要写一个轻量级的适配程序（如Python/Flask或FastAPI），主要做三件事：• **接收与解密**：接收企业微信发来的消息，使用上一步的Token和EncodingAESKey进行解密，解析出用户消息内容。• **调用Agent内核**：将解析出的消息，作为请求参数，调用你自己Agent服务的核心API（如`/v1/chat`）获取回答。• **加密与回复**：将Agent的回答，按照企业微信要求的格式加密后，再返回给企业微信。||
|**5. 打通网络与权限**|• **配置IP白名单**：将你的服务器公网IP地址，添加到企业微信应用详情页底部的“企业可信IP”中。• **配置域名**：如果使用域名，需将其配置到应用的“网页授权及JS-SDK”等功能的可信域名中，并完成域名所有权验证。||
|**6. 发布上线**|完成以上所有配置和开发后，你的Agent就可以在企业微信工作台中使用了。员工点击应用图标即可进入聊天，或在群聊中@你的Agent进行交互。||

### 💡 核心注意事项
* **网络要求**：企业微信的回调接口必须通过**公网可访问**，且强烈建议配置**HTTPS**协议以确保安全。如果使用域名，必须已**备案**。
* **身份认证**：所有API调用都需要使用`access_token`，它基于`CorpID`和`Secret`获取，有效期2小时，需要在程序中做好缓存和刷新机制。
* **消息加解密**：企业微信的消息体是加密的XML格式，必须使用后台配置的`Token`和`EncodingAESKey`进行解密和加密操作，不能直接处理明文。

# 二、实际操作-资源准备（必要）
### 1、认证过的企微账号；按步骤验证
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fc5ac1e4c8cf4aff96b6ae35a1687813&docGuid=JgeTBfNP0qPsDe "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=91ad09dbc46b4740ae125e1ff52f165c&docGuid=JgeTBfNP0qPsDe "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=866aa2bd889f4c1bb24d6220ddf372f2&docGuid=JgeTBfNP0qPsDe "")


### 2、和企微账号同主体的公网可访问的域名；（企微回调限制）
### 3、挂载到域名下可访问公网环境的云服务器（发送企微消息需要出网公网权限）；
# 三、企微配置
### 1、创建自建应用（内部）
#### 点击应用管理-自建-创建应用
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3536868ba60e4f9b93e72f5a23dbcba7&docGuid=JgeTBfNP0qPsDe "")
#### 按要求填应用名称和logo
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2555e725c0134b03a2242915c9872788&docGuid=JgeTBfNP0qPsDe "")
#### 设置API接收，同时保留agent必要信息，secret获取后会发送到管理员企微账号，以消息的形式
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9b7bf0a7263b448d913d4fc86b547046&docGuid=JgeTBfNP0qPsDe "")


#### 需要用到前面提到的公网域名
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1da140fd32704f1392df0854d7a9fccc&docGuid=JgeTBfNP0qPsDe "")
#### 回调代码，可参考，包含agent降级逻辑，可以先把降级逻辑调通（消息从企微到服务端），后面在接agent
保存时报错按要求处理，即可。

```
"""
独立的企业微信回调服务启动文件。
提供 URL 验证、消息接收、Agent 异步处理和主动回发能力。
"""
import asyncio
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import Response
import uvicorn

# 加载 .env 环境变量（需在读取 os.getenv 之前执行）
try:
    from dotenv import load_dotenv
    _env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    load_dotenv(_env_file)
except ImportError:
    pass

print("加载环境变量...")

# 企业微信核心配置
WEWORK_TOKEN = os.getenv("WEWORK_TOKEN", "")
WEWORK_ENCODING_AES_KEY = os.getenv("WEWORK_ENCODING_AES_KEY", "")
WEWORK_CORP_ID = os.getenv("WEWORK_CORP_ID", "")
WEWORK_AGENT_ID = os.getenv("WEWORK_AGENT_ID", "")
WEWORK_AGENT_SECRET = os.getenv("WEWORK_AGENT_SECRET", "")

# 常量配置
WEWORK_GET_TOKEN_API = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
WEWORK_SEND_MESSAGE_API = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
WEWORK_KF_SYNC_MSG_API = "https://qyapi.weixin.qq.com/cgi-bin/kf/sync_msg"
WEWORK_KF_SEND_MSG_API = "https://qyapi.weixin.qq.com/cgi-bin/kf/send_msg"
DEFAULT_AGENT_ID = "default"
HTTP_TIMEOUT_SECONDS = 10
TOKEN_REFRESH_BUFFER_SECONDS = 200
DUPLICATE_CHECK_INTERVAL_SECONDS = 300
MAX_REPLY_CHARS_PER_MESSAGE = 1800
KF_SYNC_LIMIT = 1000

# AccessToken 内存缓存
ACCESS_TOKEN = ""
TOKEN_EXPIRE_TIME = 0.0
TOKEN_LOCK = threading.Lock()

print(f"Token: {WEWORK_TOKEN[:10]}..." if WEWORK_TOKEN else "Token: <empty>")
print(f"CorpID: {WEWORK_CORP_ID}")
print(f"AgentID: {WEWORK_AGENT_ID}")

# 导入 backend 目录下的依赖
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.append(BACKEND_DIR)

try:
    from WXBizMsgCrypt import WXBizMsgCrypt

    crypt = WXBizMsgCrypt(WEWORK_TOKEN, WEWORK_ENCODING_AES_KEY, WEWORK_CORP_ID)
    print("WXBizMsgCrypt 初始化成功")
except Exception as exc:
    print(f"[WARNING] WXBizMsgCrypt 初始化失败: {exc}")
    sys.exit(1)

try:
    from agent_manager import AgentManager

    agent_manager = AgentManager()
    print("AgentManager 初始化成功")
except Exception as exc:
    agent_manager = None
    print(f"[WARNING] AgentManager 初始化失败: {exc}")


def log_time():
    """返回格式化的时间戳，精确到毫秒。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def warning_log(event, message):
    """统一 warning 日志输出。"""
    print(f"[{log_time()}] [WARNING] [{event}] {message}")


def split_text_by_length(content, max_chars):
    """按固定长度切分消息，避免超长文本发送失败。"""
    if not content:
        return []

    text = content.strip()
    if not text:
        return []

    chunks = []
    for index in range(0, len(text), max_chars):
        chunks.append(text[index:index + max_chars])
    return chunks


def get_access_token():
    """获取并缓存 access_token。"""
    global ACCESS_TOKEN, TOKEN_EXPIRE_TIME

    now = time.time()
    if ACCESS_TOKEN and now < TOKEN_EXPIRE_TIME:
        return ACCESS_TOKEN

    with TOKEN_LOCK:
        now = time.time()
        if ACCESS_TOKEN and now < TOKEN_EXPIRE_TIME:
            return ACCESS_TOKEN

        params = urllib.parse.urlencode(
            {
                "corpid": WEWORK_CORP_ID,
                "corpsecret": WEWORK_AGENT_SECRET,
            }
        )
        token_url = f"{WEWORK_GET_TOKEN_API}?{params}"

        request = urllib.request.Request(url=token_url, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
                response_text = response.read().decode("utf-8", errors="ignore")
                payload = json.loads(response_text)
        except Exception as exc:
            raise RuntimeError(f"request gettoken failed: {exc}") from exc

        errcode = payload.get("errcode", -1)
        if errcode != 0:
            errmsg = payload.get("errmsg", "unknown")
            raise RuntimeError(f"gettoken errcode={errcode}, errmsg={errmsg}")

        access_token = payload.get("access_token", "")
        expires_in = int(payload.get("expires_in", 7200))
        if not access_token:
            raise RuntimeError("empty access_token from wework")

        ACCESS_TOKEN = access_token
        TOKEN_EXPIRE_TIME = time.time() + max(expires_in - TOKEN_REFRESH_BUFFER_SECONDS, 60)
        return ACCESS_TOKEN


def post_wework_json(api_url, payload):
    """调用企业微信 JSON 接口。"""
    try:
        access_token = get_access_token()
    except Exception as exc:
        return False, f"get access_token failed: {exc}", {}

    request_url = f"{api_url}?access_token={urllib.parse.quote(access_token)}"
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    request = urllib.request.Request(url=request_url, method="POST", data=body, headers=headers)

    try:
        with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            response_text = response.read().decode("utf-8", errors="ignore")
            result = json.loads(response_text)
    except urllib.error.HTTPError as exc:
        response_text = exc.read().decode("utf-8", errors="ignore")
        return False, f"request http error: {exc.code}, body={response_text}", {}
    except Exception as exc:
        return False, f"request failed: {exc}", {}

    errcode = result.get("errcode", -1)
    if errcode != 0:
        errmsg = result.get("errmsg", "unknown")
        return False, f"request failed errcode={errcode}, errmsg={errmsg}, result={result}", result

    return True, "ok", result


def send_text_message(to_user, content):
    """发送文本消息给企微应用用户。"""
    if not to_user:
        return False, "empty to_user"
    if not content:
        return False, "empty content"

    payload = {
        "touser": to_user,
        "msgtype": "text",
        "agentid": int(WEWORK_AGENT_ID),
        "text": {"content": content},
        "enable_duplicate_check": 1,
        "duplicate_check_interval": DUPLICATE_CHECK_INTERVAL_SECONDS,
    }

    ok, message, _ = post_wework_json(WEWORK_SEND_MESSAGE_API, payload)
    return ok, message


def send_kf_text_message(external_userid, open_kfid, content):
    """发送文本消息给企微客服会话用户。"""
    if not external_userid:
        return False, "empty external_userid"
    if not open_kfid:
        return False, "empty open_kfid"
    if not content:
        return False, "empty content"

    payload = {
        "touser": external_userid,
        "open_kfid": open_kfid,
        "msgtype": "text",
        "text": {"content": content},
    }

    ok, message, _ = post_wework_json(WEWORK_KF_SEND_MSG_API, payload)
    return ok, message


def parse_xml_text(xml_root, tag_name):
    """提取 XML 节点文本。"""
    node = xml_root.find(tag_name)
    if node is None or node.text is None:
        return ""
    return node.text.strip()


def sync_kf_messages(sync_token, open_kfid=""):
    """通过企微客服 token 拉取最新客服消息。"""
    if not sync_token:
        return False, "empty kf sync token", {}

    payload = {
        "token": sync_token,
        "limit": KF_SYNC_LIMIT,
    }
    if open_kfid:
        payload["open_kfid"] = open_kfid
    return post_wework_json(WEWORK_KF_SYNC_MSG_API, payload)


def pick_latest_kf_text_message(sync_result, expected_open_kfid):
    """从客服消息列表中选择最新文本消息。"""
    msg_list = sync_result.get("msg_list") or []
    if not msg_list:
        return "", "", ""

    selected = None
    selected_time = -1
    for message in msg_list:
        if expected_open_kfid and message.get("open_kfid") != expected_open_kfid:
            continue
        if message.get("msgtype") != "text":
            continue

        message_time = int(message.get("send_time") or 0)
        if message_time >= selected_time:
            selected = message
            selected_time = message_time

    if not selected:
        return "", "", ""

    text_payload = selected.get("text") or {}
    return (
        selected.get("external_userid") or "",
        (text_payload.get("content") or "").strip(),
        selected.get("open_kfid") or "",
    )


async def resolve_callback_message(decrypted_msg):
    """解析回调消息，兼容普通消息和企微客服事件。"""
    try:
        xml_root = ET.fromstring(decrypted_msg)
    except Exception as exc:
        warning_log("wework_parse_message_failed", f"invalid xml: {exc}")
        return {
            "channel": "unknown",
            "to_user": "",
            "content": "",
            "msg_type": "",
            "open_kfid": "",
        }

    msg_type = parse_xml_text(xml_root, "MsgType")
    from_user = parse_xml_text(xml_root, "FromUserName")
    content = parse_xml_text(xml_root, "Content")

    if msg_type == "text" and from_user and content:
        return {
            "channel": "app",
            "to_user": from_user,
            "content": content,
            "msg_type": msg_type,
            "open_kfid": "",
        }

    event_name = parse_xml_text(xml_root, "Event")
    if msg_type == "event" and event_name == "kf_msg_or_event":
        sync_token = parse_xml_text(xml_root, "Token")
        open_kfid = parse_xml_text(xml_root, "OpenKfId")

        ok, message, sync_result = sync_kf_messages(sync_token, open_kfid)
        if not ok:
            warning_log("wework_kf_sync_failed", message)
            return {
                "channel": "kf",
                "to_user": "",
                "content": "",
                "msg_type": msg_type,
                "open_kfid": open_kfid,
            }

        external_userid, kf_content, kf_open_kfid = pick_latest_kf_text_message(sync_result, open_kfid)
        return {
            "channel": "kf",
            "to_user": external_userid,
            "content": kf_content,
            "msg_type": msg_type,
            "open_kfid": kf_open_kfid or open_kfid,
        }

    if msg_type and not content:
        content = f"[企微{msg_type}消息]"

    return {
        "channel": "app",
        "to_user": from_user,
        "content": content,
        "msg_type": msg_type,
        "open_kfid": "",
    }


async def run_agent_once(message_content, from_user):
    """执行一次 Agent，返回文本回复。"""
    if agent_manager is None:
        warning_log("wework_agent_manager_unavailable", "agent_manager is not initialized")
        return "当前为降级模式：Agent 依赖未就绪，已收到你的消息。"

    session_id = f"wework_{from_user}"

    try:
        agent = await agent_manager.get_agent(
            agent_id=DEFAULT_AGENT_ID,
            model_id=None,
            session_id=session_id,
        )
    except Exception as exc:
        warning_log("wework_get_agent_failed", str(exc))
        return ""

    parts = []
    error_msg = ""
    try:
        try:
            stream = agent.astream(
                {"messages": [{"role": "user", "content": message_content}]},
                config={"configurable": {"thread_id": session_id}},
                stream_mode="messages",
                durability="exit",
            )
        except TypeError:
            stream = agent.astream(
                {"messages": [{"role": "user", "content": message_content}]},
                config={"configurable": {"thread_id": session_id}},
            )

        async for chunk in stream:
            if isinstance(chunk, tuple) and len(chunk) == 2:
                msg_obj, _ = chunk
                content = getattr(msg_obj, "content", None)

                appended = False
                if isinstance(content, str) and content:
                    parts.append(content)
                    appended = True
                elif isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict):
                            text = item.get("text")
                            if text:
                                parts.append(text)
                                appended = True

                if not appended and hasattr(msg_obj, "content_blocks"):
                    for block in getattr(msg_obj, "content_blocks", []):
                        if block.get("type") == "text" and block.get("text"):
                            parts.append(block.get("text"))

            elif isinstance(chunk, dict):
                block_type = chunk.get("block_type")
                content = chunk.get("content")
                if block_type == "text" and content:
                    parts.append(content)
    except Exception as exc:
        error_msg = str(exc)
        warning_log("wework_agent_stream_failed", error_msg)

    result = "".join(parts).strip()
    if result:
        return result

    # 与现有逻辑保持一致：无输出时给出可读提示
    if getattr(agent, "__class__", None) and agent.__class__.__name__ == "FallbackAgent":
        return "当前为降级模式（FallbackAgent）：服务可用，但未接入真实模型依赖（deepagents）。"
    if error_msg:
        return "AI执行异常：" + error_msg
    return "（当前未提取到模型文本输出，可能是工具调用阶段）"


async def process_message_and_reply(decrypted_msg):
    """后台处理消息并主动回发。"""
    message_info = await resolve_callback_message(decrypted_msg)
    channel = message_info.get("channel") or "app"
    to_user = message_info.get("to_user") or ""
    content = message_info.get("content") or ""
    msg_type = message_info.get("msg_type") or ""
    open_kfid = message_info.get("open_kfid") or ""

    if not to_user:
        preview = str(decrypted_msg).replace("\n", " ")[:300]
        warning_log(
            "wework_from_user_missing",
            f"skip send reply because to_user is empty, channel={channel}, msg_type={msg_type}, content={content}, raw_preview={preview}",
        )
        return
    if not content:
        warning_log(
            "wework_content_missing",
            f"skip agent run because content is empty, channel={channel}, msg_type={msg_type}, uid={to_user}",
        )
        return

    agent_reply = await run_agent_once(content, to_user)
    if not agent_reply:
        warning_log("wework_empty_agent_reply", f"skip send because agent reply is empty, uid={to_user}")
        return

    reply_chunks = split_text_by_length(agent_reply, MAX_REPLY_CHARS_PER_MESSAGE)
    for chunk in reply_chunks:
        if channel == "kf":
            ok, message = send_kf_text_message(to_user, open_kfid, chunk)
        else:
            ok, message = send_text_message(to_user, chunk)

        if not ok:
            warning_log("wework_send_text_failed", f"channel={channel}, uid={to_user}, errmsg={message}")
            return


# 创建 FastAPI 应用
app = FastAPI(title="企业微信回调服务")


@app.get("/api/wework/callback")
async def wework_verify_url(
    msg_signature: str,
    timestamp: str,
    nonce: str,
    echostr: str,
):
    """企业微信 URL 验证接口。"""
    try:
        ret, echo_str = crypt.VerifyURL(msg_signature, timestamp, nonce, echostr)
        if ret != 0:
            warning_log("wework_verify_url_failed", f"ret={ret}")
            return Response(content="验证失败", status_code=400)

        return Response(content=echo_str, media_type="text/plain")
    except Exception as exc:
        warning_log("wework_verify_url_exception", str(exc))
        return Response(content="验证异常", status_code=500)


@app.post("/api/wework/callback")
async def wework_receive_message(
    request: Request,
    msg_signature: str,
    timestamp: str,
    nonce: str,
):
    """企业微信消息接收接口。"""
    try:
        post_data = await request.body()
        ret, decrypted_msg = crypt.DecryptMsg(post_data, msg_signature, timestamp, nonce)
        if ret != 0:
            warning_log("wework_decrypt_message_failed", f"ret={ret}")
            return Response(content="解密失败", status_code=400)

        # 先快速 ACK，后台异步处理并主动回发。
        # Python 3.6 不支持 asyncio.create_task，使用 ensure_future 兼容。
        asyncio.ensure_future(process_message_and_reply(decrypted_msg))
        return Response(content="success", media_type="text/plain")
    except Exception as exc:
        warning_log("wework_message_callback_exception", str(exc))
        return Response(content="处理异常", status_code=500)


@app.get("/")
async def health_check():
    return {"status": "ok", "message": "企业微信回调服务正在运行"}


@app.get("/api/health")
async def api_health():
    return {"status": "ok", "timestamp": log_time()}


if __name__ == "__main__":
    print(f"[{log_time()}] 启动企业微信回调服务...")
    print(f"[{log_time()}] 监听端口: 8000")
    print(f"[{log_time()}] 企业微信回调URL: http://your-server:8000/api/wework/callback")
    print(f"[{log_time()}] 健康检查: http://localhost:8000/")

    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(server.serve())

```
#### 保存成功后，显示已启用API接收，此时自建应用基本OK了
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1f2443604e4b4699b2111f5a79104a10&docGuid=JgeTBfNP0qPsDe "")
### 2、创建微信客服（外部）
#### 应用管理-微信客服
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f7096ae83a1340a99cc08f3b2d1255b2&docGuid=JgeTBfNP0qPsDe "")
#### 创建账号
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=317bc53b6820400bb79344de347d4f7d&docGuid=JgeTBfNP0qPsDe "")
#### 正常按要求填写
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=64678cfe360848fd9956266fc5562c0c&docGuid=JgeTBfNP0qPsDe "")
#### 保存成功后在微信客服列表可见，下一步点击api（**比较隐蔽**）
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=85975835b602496784ad101fee6238af&docGuid=JgeTBfNP0qPsDe "")
#### 按要求设置接收事件服务器
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=90f80e1bfa814926923e60cb2722e646&docGuid=JgeTBfNP0qPsDe "")
#### 点击可调用接口应用，选中后点击确认
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9aede9f249dd4a3d92e91190917679ca&docGuid=JgeTBfNP0qPsDe "")
#### 点击前往配置，把前面创建的微信客服和自建应用关联上，此时企微配置就搞定了
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2d17bf5a6ba0438ca9b81983f6e34c5b&docGuid=JgeTBfNP0qPsDe "")


# 四、拉外部客户群，分享微信客服
发送消息成功被服务端获取，agent处理后通过企微接口发送消息返回企微

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=14dad5db5adf4b57b50cf69ba0f55754&docGuid=JgeTBfNP0qPsDe "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bec916f7e33f429ca59c59ac51188207&docGuid=JgeTBfNP0qPsDe "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9835b6b46a81495fb34f32ea47e49e59&docGuid=JgeTBfNP0qPsDe "")




# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
