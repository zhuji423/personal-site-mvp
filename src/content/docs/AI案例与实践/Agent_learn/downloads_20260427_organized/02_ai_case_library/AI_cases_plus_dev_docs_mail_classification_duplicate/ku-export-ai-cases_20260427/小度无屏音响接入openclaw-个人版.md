---
title: "目标"
description: "小度无屏音响接入openclaw-个人版"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\小度无屏音响接入openclaw-个人版.md"
---
小度无屏音响接入openclaw-个人版

#### 🧑‍🏫 案例作者：[@刘金帅](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：其他
#### 🔧 使用工具：OpenClaw
#### 📒 案例概要：小度音响通过自定义技能接入openclaw，实现语音交互，适合儿童和老人使用。需部署中转服务、配置Webhook
# 目标
利用小度音响终端的语音识别功能，实现通过语音与openclaw对话，方便学龄前小朋友和老人体验AI Agent。

# 准备资源
* 小度音响
* 云上公网地址+openclaw(由于百度云个人账号限制，这里使用的腾讯云的)

# 方案
```

  ┌─────────────────────────────────────────────────────────────────────────────────────┐
  │                        小度音箱接入 OpenClaw 整体架构图                                 │
  └─────────────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐      语音       ┌──────────────┐      HTTPS       ┌──────────────────┐
  │              │  ─────────────▶ │              │  ──────────────▶ │                  │
  │   小度音箱    │                 │  DuerOS 云端  │                  │   tgw.py (网关)   │
  │              │ ◀───────────── │              │ ◀────────────── │   FastAPI:5000   │
  └──────────────┘      TTS播报    └──────────────┘      JSON        └────────┬─────────┘
                                                                              │
                                                                              │ HTTP POST
                                                                              ▼
                                                                     ┌──────────────────┐
                                                                     │   OpenClaw API   │
                                                                     │  (GLM-5 模型)     │
                                                                     │  127.0.0.1:13406 │
                                                                     └──────────────────┘

  ═══════════════════════════════════════════════════════════════════════════════════════
```
##  请求处理流程详解
由于Openclaw响应实效性有限，如果DuerOS 云端等待时间超过3-5秒有可能走默认的主干意图，所以主要分为两个以下两个场景

场景1，Openclaw响应小于2秒的话，就直接响应

场景2，Openclaw响应大于2秒的话，中转网关给DuerOS 云端发送SendPart，等待DuerOS 云端请求NextRequired时，再把Openclaw的响应进行播放。

场景3，Openclaw响应大于2秒的话，中转网关给DuerOS 云端发送SendPart，DuerOS 云端不会请求NextRequired，需要在小度重启发起query，第二次query时会命中缓存快速响应。(这种方式体验交差，如果小度音响不能响应NextRequired，需要断电重启，才能支持场景2)

```
                                 

  ┌─────────────────────────────────────────────────────────────────────────────────────┐
  │ 场景1: 快速响应 (LLM < 2秒)                                                          │
  ├─────────────────────────────────────────────────────────────────────────────────────┤
  │                                                                                     │
  │  用户          小度音箱          DuerOS           tgw.py            OpenClaw        │
  │   │              │                │                 │                  │            │
  │   │──"你好"────▶│                │                 │                  │            │
  │   │              │──IntentReq───▶│                 │                  │            │
  │   │              │               │───webhook──────▶│                  │            │
  │   │              │               │                 │────LLM请求──────▶│            │
  │   │              │               │                 │◀───1.5s返回──────│            │
  │   │              │               │◀──直接返回结果──│                  │            │
  │   │              │◀──TTS播报────│                 │                  │            │
  │   │◀──"你好呀"──│               │                 │                  │            │
  │                                                                                     │
  └─────────────────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────────────────┐
  │ 场景2: 慢速响应 (LLM > 2秒) - StreamResponse 机制                                    │
  ├─────────────────────────────────────────────────────────────────────────────────────┤
  │                                                                                     │
  │  用户          小度音箱          DuerOS           tgw.py            OpenClaw        │
  │   │              │                │                 │                  │            │
  │   │──"讲故事"──▶│                │                 │                  │            │
  │   │              │──IntentReq───▶│                 │                  │            │
  │   │              │               │───webhook──────▶│                  │            │
  │   │              │               │                 │────LLM请求──────▶│            │
  │   │              │               │                 │     (异步执行)    │            │
  │   │              │               │◀─2s超时+SendPart│                  │            │
  │   │              │◀─"让我想想"──│                 │                  │            │
  │   │◀──播报中───│               │                 │                  │            │
  │   │              │               │                 │◀───4s返回────────│            │
  │   │              │               │                 │   (存入缓存)      │            │
  │   │              │               │──NextRequired─▶│                  │            │
  │   │              │               │◀──返回缓存结果──│                  │            │
  │   │              │◀──TTS播报────│                 │                  │            │
  │   │◀──故事内容──│               │                 │                  │            │
  │                                                                                     │
  └─────────────────────────────────────────────────────────────────────────────────────┘

  ═══════════════════════════════════════════════════════════════════════════════════════
```
# 操作步骤
## 云端创建openclaw
eip+openclaw，配置openclaw。

## 部署中转服务
```
root@VM-0-14-ubuntu:~# cat tgw_as_dcc3.py
from fastapi import FastAPI, Request
import httpx
import logging
import json
import time
import asyncio
import uuid

# ================= 日志配置 =================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('/root/tgw.log')
    ]
)
logger = logging.getLogger("DuerOS-Bridge")

app = FastAPI()

# ================= 配置项 =================
OPENCLAW_API_URL = "http://127.0.0.1:13406/v1/chat/completions"
OPENCLAW_API_TOKEN = "c44cb50145e162e7958c1175a1be86b589179666c5f38d11"

# 结果缓存: {device_id: {"result": str, "timestamp": float, "pending": bool}}
results_cache = {}


async def query_openclaw(user_query: str, trace_id: str) -> str:
    """调用大模型接口"""
    payload = {
        "model": "qianfan/glm-5",
        "user": "xiaoyu",
        "messages": [
            {"role": "system", "content": "你是小语的好朋友。简洁口语回答，不超过25字。"},
            {"role": "user", "content": user_query}
        ],
        "stream": False,
        "max_tokens": 60
    }
    headers = {"Authorization": f"Bearer {OPENCLAW_API_TOKEN}"}

    logger.info(f"[{trace_id}] -> [LLM Request] URL: {OPENCLAW_API_URL}")
    logger.info(f"[{trace_id}] -> [LLM Request] Payload: {json.dumps(payload, ensure_ascii=False)}")

    async with httpx.AsyncClient() as client:
        try:
            start_t = time.perf_counter()
            response = await client.post(OPENCLAW_API_URL, json=payload, headers=headers, timeout=60.0)
            elapsed = time.perf_counter() - start_t

            logger.info(f"[{trace_id}] <- [LLM Response] Status: {response.status_code} | Time: {elapsed:.2f}s")
            logger.info(f"[{trace_id}] <- [LLM Response] Body: {response.text[:500]}")

            if response.status_code == 200:
                reply = response.json()["choices"][0]["message"]["content"]
                logger.info(f"[{trace_id}] <- [LLM Reply] {reply}")
                return reply
            else:
                logger.error(f"[{trace_id}] <- [LLM Error] Status: {response.status_code}")
                return "哎呀，大脑开小差了。"
        except Exception as e:
            logger.error(f"[{trace_id}] <- [LLM Exception] {str(e)}")
            return "连接大脑超时了。"


async def handle_request_and_cache(user_query: str, device_id: str, trace_id: str):
    """后台异步任务：执行并更新缓存"""
    results_cache[device_id] = {"pending": True, "timestamp": time.time(), "result": None}

    reply = await query_openclaw(user_query, trace_id)

    results_cache[device_id] = {
        "result": reply,
        "timestamp": time.time(),
        "pending": False
    }
    logger.info(f"[{trace_id}] [Task] 结果已存入缓存")
    return reply


@app.post("/dueros/webhook")
async def dueros_webhook(request: Request):
    trace_id = str(uuid.uuid4())[:8]
    start_time = time.perf_counter()

    try:
        data = await request.json()
        req_obj = data.get("request", {})
        req_type = req_obj.get("type")
        session = data.get("session", {})
        system_ctx = data.get("context", {}).get("System", {})
        device_id = system_ctx.get("device", {}).get("deviceId", "default")

        # 打印完整请求
        logger.info(f"{'='*60}")
        logger.info(f"[{trace_id}] >>>>>> 收到请求 <<<<<<")
        logger.info(f"[{trace_id}] Type: {req_type}")
        logger.info(f"[{trace_id}] Device: {device_id}")
        logger.info(f"[{trace_id}] Session New: {session.get('new', 'N/A')}")
        logger.info(f"[{trace_id}] Session ID: {session.get('sessionId', 'N/A')[:20]}...")
        logger.info(f"[{trace_id}] Request Detail: {json.dumps(req_obj, ensure_ascii=False)}")
        logger.info(f"[{trace_id}] Cache Status: {device_id in results_cache} | Cache Data: {results_cache.get(device_id, 'None')}")
        logger.info(f"{'='*60}")

        # 1. 处理技能启动
        if req_type == "LaunchRequest":
            return log_and_return(trace_id, build_response("小龙虾openclaw在呢，当前是GLM-5模型,想聊点什么？", False), start_time)

        # 2. 处理 StreamResponse.NextRequired 事件 - DuerOS 播完"思考中"后会发这个
        if req_type == "StreamResponse.NextRequired":
            token = req_obj.get("token", "")
            logger.info(f"[{trace_id}] [Stream] 收到 NextRequired, token: {token}")

            # 检查缓存中是否有结果
            if device_id in results_cache:
                cache = results_cache[device_id]

                # 结果已就绪
                if not cache.get("pending") and cache.get("result"):
                    result = cache["result"]
                    del results_cache[device_id]
                    logger.info(f"[{trace_id}] [Stream] 返回缓存结果: {result}")
                    return log_and_return(trace_id, build_response(result, False), start_time)

                # 还在处理中，等待一下（最多等 5 秒）
                if cache.get("pending"):
                    logger.info(f"[{trace_id}] [Stream] 结果未就绪，等待中...")
                    for _ in range(50):  # 最多等 5 秒
                        await asyncio.sleep(0.1)
                        cache = results_cache.get(device_id, {})
                        if not cache.get("pending") and cache.get("result"):
                            result = cache["result"]
                            del results_cache[device_id]
                            logger.info(f"[{trace_id}] [Stream] 等待后返回结果: {result}")
                            return log_and_return(trace_id, build_response(result, False), start_time)

                    # 超时了还没结果
                    logger.warning(f"[{trace_id}] [Stream] 等待超时")
                    return log_and_return(trace_id, build_response("还在想呢，再等等我。", False, send_part=True), start_time)

            # 没有缓存，可能是异常情况
            logger.warning(f"[{trace_id}] [Stream] 无缓存数据")
            return log_and_return(trace_id, build_response("我好像忘了你问什么了。", False), start_time)

        # 3. 处理核心意图
        if req_type == "IntentRequest":
            user_query = req_obj.get("query", {}).get("original") or req_obj.get("query", {}).get("text")
            dialog_state = req_obj.get("dialogState", "UNKNOWN")
            logger.info(f"[{trace_id}] [Intent] Query: {user_query} | DialogState: {dialog_state}")

            # --- 优先检查缓存：如果有已完成的结果，直接返回 ---
            if device_id in results_cache:
                cache = results_cache[device_id]
                # 结果已就绪且未过期（60秒内）
                if not cache.get("pending") and cache.get("result") and (time.time() - cache.get("timestamp", 0) < 60):
                    result = cache["result"]
                    del results_cache[device_id]
                    logger.info(f"[{trace_id}] [Cache] 命中缓存结果: {result}")
                    return log_and_return(trace_id, build_response(result, False), start_time)

                # 如果还在处理中，告诉用户稍等
                if cache.get("pending"):
                    logger.info(f"[{trace_id}] [Cache] 任务处理中，引导用户")
                    return log_and_return(trace_id, build_response("还在想呢，马上就好。", False), start_time)

            # --- 没有缓存，开始新请求 ---
            logger.info(f"[{trace_id}] [Logic] 开启同步竞争，阈值 2.0s")
            task = asyncio.create_task(handle_request_and_cache(user_query, device_id, trace_id))

            try:
                reply = await asyncio.wait_for(asyncio.shield(task), timeout=2.0)

                if device_id in results_cache:
                    del results_cache[device_id]

                cost = time.perf_counter() - start_time
                logger.info(f"[{trace_id}] [Logic] 同步成功 | 耗时: {cost:.2f}s")
                return log_and_return(trace_id, build_response(reply, False), start_time)

            except asyncio.TimeoutError:
                # 超时：返回"思考中" + SendPart 指令，让 DuerOS 播完后发 NextRequired
                cost = time.perf_counter() - start_time
                logger.warning(f"[{trace_id}] [Logic] 2s 超时({cost:.2f}s) | 返回 SendPart")

                return log_and_return(trace_id, build_response(
                    "让我想一想...",
                    False,
                    send_part=True  # 关键：添加 SendPart 指令
                ), start_time)

        if req_type == "SessionEndedRequest":
            # 清理该设备的缓存
            if device_id in results_cache:
                del results_cache[device_id]
            return {"version": "2.0", "response": {"shouldEndSession": True}}

    except Exception as e:
        logger.error(f"[{trace_id}] [Critical] {str(e)}", exc_info=True)
        return build_response("哎呀，小龙虾有点累了。", True)


def build_response(text: str, should_end: bool, send_part: bool = False, token: str = None):
    """
    构建 DuerOS 响应格式
    send_part=True 时添加 StreamResponse.SendPart 指令
    """
    # 添加 StreamResponse.SendPart 指令时，使用特殊格式（无 outputSpeech）
    if send_part and not should_end:
        part_token = token or f"part_{int(time.time())}"
        response = {
            "version": "2.0",
            "session": {"attributes": {}},
            "response": {
                "outputSpeech": {"type": "PlainText", "text": text},
                "directives": [
                    {
                        "type": "StreamResponse.SendPart",
                        "token": part_token
                    }
                ],
                "expectSpeech": False,
                "shouldEndSession": False
            }
        }
        logger.info(f"[SendPart] 添加指令，token: {part_token}")
        logger.info(f"[SendPart] 完整响应: {json.dumps(response, ensure_ascii=False)}")
        return response

    # 普通响应
    return {
        "version": "2.0",
        "session": {"attributes": {}},
        "response": {
            "outputSpeech": {"type": "PlainText", "text": text},
            "shouldEndSession": should_end,
        }
    }


def log_and_return(trace_id: str, response: dict, start_time: float = None):
    text = response.get('response', {}).get('outputSpeech', {}).get('text', '')
    has_directive = 'directives' in response.get('response', {})
    cost = f"{(time.perf_counter() - start_time)*1000:.1f}ms" if start_time else "N/A"

    logger.info(f"{'='*60}")
    logger.info(f"[{trace_id}] <<<<<< 返回响应 >>>>>>")
    logger.info(f"[{trace_id}] Text: {text}")
    logger.info(f"[{trace_id}] ShouldEnd: {response.get('response', {}).get('shouldEndSession')}")
    logger.info(f"[{trace_id}] HasDirective: {has_directive}")
    logger.info(f"[{trace_id}] 总耗时: {cost}")
    logger.info(f"[{trace_id}] Full Response: {json.dumps(response, ensure_ascii=False)}")
    logger.info(f"{'='*60}")
    return response


if __name__ == "__main__":
    import uvicorn
    logger.info(">>> StreamResponse 方案服务启动 <<<")
    uvicorn.run(app, host="0.0.0.0", port=5000)
root@VM-0-14-ubuntu:~# 
```
## 配置https webhook


## 配置小度意图
1、进去[https://developer.dueros.baidu.com/dbp/main/console](https://developer.dueros.baidu.com/dbp/main/console)技能控制台

2、创建自定义技能

调用名称，命名时需要注意技巧，不要用太通用的名字，比如，小龙虾，打开技能的成功率就比较低，如果用小龙虾助手，打开技能的成功率就很高。

![](/personal-site-mvp/img/doc-placeholder.svg "")
3、应用缺省意图

![](/personal-site-mvp/img/doc-placeholder.svg "")
4、配置webhook

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 模拟调试
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 真机调试
进入技能调试模型：小度小度，打开技能调试模式

进入技能：小度小度，打开小龙虾助手

这是场景3，需要再次询问才能回答的效果，不清楚dueros内部的逻辑，拔电源重启后，对话就比较流畅了。

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 经验
1、技能调用名称，不要用太通用的名字，比如，小龙虾，『打开小龙虾』成功率就比较低，小度会理解成你要吃小龙虾；如果用小龙虾助手，打开技能的成功率就很高。

2、打开技能时，如果提示，技能好像出现了问题，小度正在抓紧修复，有可能webhook的不通。

3、如果query后，没有进行播报，由于个人不支持主动推送给小度音响播报，只能用stream模式，而小度经常不发送NextRequired，需要把小度断电重启后，就会出现NextRequired，否则只能再次问答，把上次的openclaw的回答带回来，体验不好。

4、个人开发版不支持主动推送，限制了openclaw的很多功能，希望能开放更多能力，或者谁有好办法可以share一下

# API参考
[https://developer.dueros.baidu.com/doc/dueros-bot-platform/dbp-custom/request_markdown](https://developer.dueros.baidu.com/doc/dueros-bot-platform/dbp-custom/request_markdown)





---

感谢裴林涵和杜鑫卓提供的支持。



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
