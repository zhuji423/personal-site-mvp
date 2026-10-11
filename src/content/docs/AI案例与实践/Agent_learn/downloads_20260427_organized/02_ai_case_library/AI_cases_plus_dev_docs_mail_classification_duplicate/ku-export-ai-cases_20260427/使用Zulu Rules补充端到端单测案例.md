---
title: "1. 设置模型路径"
description: "使用Zulu Rules补充端到端单测案例"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\使用Zulu Rules补充端到端单测案例.md"
---
使用Zulu Rules补充端到端单测案例

#### 🧑‍🏫 案例作者：[@张玉龙](https://ku.baidu-int.com?t=mention&mt=contact&id=039513d0-fce4-11f0-af4b-6bed22987a43)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了使用Coding Agent Rules在FastDeploy项目中补充端到端单测的实践经验。通过制定系统的提示规则，Coding Agent能自动分析代码逻辑，生成高质量测试用例，确保新增单测逻辑可靠、风格统一。文章详细介绍了Rules的概述、单测补充案例及实践经验总结，展示了Rules在遗留功能单测补充、大规模重构后回归覆盖等方面的显著提效作用。
## 1. 背景
FastDeploy项目迭代节奏较快，随着代码规模和复杂度的增加，确保新增单测逻辑可靠、风格统一、规范变得愈发重要。Coding Agent 能通过规则化的提示（Coding Agent Rules）协助我们生成高质量测试代码，尤其适合：

* 遗留端到端功能单测补充
* 大规模重构后的回归覆盖（比如新增封装的工具类）
* 希望统一测试风格与规范
* 对复杂逻辑进行分支覆盖补全

FastDeploy库还存在许多功能单测未覆盖，或是一些特殊场景下的case补充，可以尝试用rules来提效

## 2. Coding Agent Rules 概述
Coding Agent Rules 是一套系统的提示规则，用于帮助模型：

* 分析代码逻辑
* 找到潜在的分支和边界
* 自动生成对应的测试用例

这些规则可以让模型更加结构化地思考，而不是简单“补几个 case”。

典型规则包括：

1. **分析输入参数类型及约束**
2. **分析各种已经封装好的工具类**
3. **列出关键分支条件**
4. **识别异常分支或错误路径**
5. **为每个分支生成最小可执行测试用例**
6. **校验现有测试覆盖情况，补齐缺失部分**

## 3. Coding Agent Rules 单测补充案例
### Step 1：让Agent 分析现有单测，生成一个规范化的rules用于约束后续单测生成
**prompt：分析一下tests/e2e/test_EB_Lite_serving.py这个端到端单测，按这个单测启动服务后跑case的规范，整理一个添加端到端单测的规则**



我将分析`tests/e2e/test_EB_Lite_serving.py`文件，梳理端到端测试的规范流程，并整理添加新端到端测试的规则。请稍等，我先读取文件内容。

分析test_EB_Lite_serving.py1364 lines

我需要查看文件的完整内容，特别是被截断的部分，以确保完整理解端到端测试的规范流程。

分析test_EB_Lite_serving.py36 lines

根据分析，`tests/e2e/test_EB_Lite_serving.py`文件展示了端到端测试的完整规范流程。以下是添加端到端单测的规则总结：

#### 端到端单测添加规则
1. **测试结构**

    * 使用`pytest`框架
    * 遵循`setup -> test -> teardown`模式
    * 使用`pytest.fixture`管理测试资源

2. **服务启动规范**

```
@pytest.fixture(scope="session", autouse=True)
def setup_and_run_server():
    # 1. 设置模型路径
    base_path = os.getenv("MODEL_PATH")
    model_path = os.path.join(base_path, "model-name") if base_path else "./model-name"
    
    # 2. 配置服务参数
    server_args = [
        "--tensor-parallel-size", "1",
        "--max-model-len", "32768",
        # 其他必要参数...
    ]
    
    # 3. 使用 FDServer 上下文管理器启动服务
    with FDServer(model_path, server_args) as fd_server:
        yield fd_server
```
3. **测试用例设计原则**

    * **基础功能测试**：验证API基本功能
    * **一致性测试**：相同输入应有相似输出
    * **流式/非流式对比**：分别测试两种模式
    * **参数边界测试**：测试各种参数组合

4. **测试验证要点**

```
def test_case(api_url):
    # 1. 发送请求并验证状态码
    resp = requests.post(api_url, headers=headers, json=payload)
    assert resp.status_code == 200
    
    # 2. 验证响应结构
    result = resp.json()
    assert "choices" in result
    assert len(result["choices"]) > 0
    
    # 3. 验证业务逻辑
    assert validate_output(result["choices"][0]["message"]["content"])
```
5. **特殊测试场景**

    * **流式测试**：验证分块数据完整性
    * **token相关测试**：验证token计数和返回
    * **特殊参数测试**：如`bad_words`,`min_tokens`等

6. **辅助工具**

    * 使用`utils.serving_utils`中的工具类
    * 添加必要的断言和验证工具函数

7. **日志和监控**

    * 检查服务日志中的关键指标
    * 验证监控指标是否符合预期

8. **性能基准**

```
def test_performance():
    baseline = 31446  # 基准值
    actual = get_actual_value()
    assert (baseline * 0.95) <= actual <= (baseline * 1.05)
```


### Step 2：让 Agent 根据rules补充一个具体场景的单测
现在需要补充metrcis接口单测，场景是并发10条请求，请求推理和排队过程中，请求http://0.0.0.0:$FD_API_PORT/clear_load_weight清空权重，这时候请求metrics接口，断言fastdeploy:num_requests_running和fastdeploy:num_requests_waiting非0，再请求curl -X POST "http://0.0.0.0:$FD_CONTROLLER_PORT/controller/reset_scheduler" -H "Content-Type: application/json" -d '{"reset": true}'执行reset，然后请求metrics接口，断言fastdeploy:num_requests_running和fastdeploy:num_requests_waiting为0，添加到tests/e2e/test_metrics.py中，服务启动配置参考tests/ce/stable_cases/launch_model.sh



![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
初版case：

```
import os
import pytest
import requests
from concurrent.futures import ThreadPoolExecutor
from utils.serving_utils import FDServer

@pytest.fixture(scope="session", autouse=True)
def setup_and_run_server():
    """启动测试服务"""
    base_path = os.getenv("MODEL_PATH")
    model_path = os.path.join(base_path, "TP1") if base_path else "./model-name"
    
    server_args = [
        "--tensor-parallel-size", "1",
        "--port", "8000",
        "--engine-worker-queue-port", "8001",
        "--metrics-port", "8002",
        "--cache-queue-port", "8003",
        "--max-model-len", "32768",
        "--max-num-seqs", "1",
        "--gpu-memory-utilization", "0.9",
        "--model", model_path,
        "--load-strategy", "ipc_snapshot",
        "--dynamic-load-weight"
    ]
    
    with FDServer(model_path, server_args) as fd_server:
        yield fd_server

def send_concurrent_requests(num_requests, api_url):
    """并发发送请求"""
    def send_request():
        return requests.post(api_url, json={"prompt": "test"})
    
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        return [f.result() for f in futures]

def test_metrics_with_weight_clear_and_reset(setup_and_run_server):
    """测试metrics接口在清空权重和重置调度器后的行为"""
    # 1. 并发发送10个请求
    api_url = "http://0.0.0.0:8000/v1/completions"
    responses = send_concurrent_requests(10, api_url)
    
    # 2. 清空权重并验证metrics
    clear_url = "http://0.0.0.0:8000/clear_load_weight"
    requests.post(clear_url)
    
    metrics_url = "http://0.0.0.0:8002/metrics"
    metrics = requests.get(metrics_url).text
    assert "fastdeploy:num_requests_running 0" not in metrics
    assert "fastdeploy:num_requests_waiting 0" not in metrics
    
    # 3. 重置调度器并验证metrics
    reset_url = "http://0.0.0.0:8001/controller/reset_scheduler"
    reset_payload = {"reset": True}
    requests.post(reset_url, json=reset_payload)
    
    metrics = requests.get(metrics_url).text
    assert "fastdeploy:num_requests_running 0" in metrics
    assert "fastdeploy:num_requests_waiting 0" in metrics
```
整体上大差不差，还有些小问题：【感觉可能是受限于模型效果】

* 重复传了FD的通用端口参数
* launch_model中的环境变量，没有放进server的env里
* TP2的配置和模型，误生成T1
* 需要在请求推理过程中调用metrics，查看实时running的数据
* requests + ThreadPoolExecutor 不能保证真正并发

--max-num-seqs 1代表running 最多 = 1，如果请求被快速串行处理，可能永远看不到waiting的请求

### Step 3：Agent 再优化 + 手工微调 → 最终可用的单测
手动改一版，再让agent优化流程

**目前tests/e2e/test_metrics.py存在问题，需要在请求推理过程中请求metrics来监测running数大于0，并限制max_tokens为50，避免case耗时过长，且****不用等待请求完成**

优化case：

```

import os
import time
import pytest
import requests
from concurrent.futures import ThreadPoolExecutor
from utils.serving_utils import (
    FD_API_PORT,
    FD_CACHE_QUEUE_PORT,
    FD_ENGINE_QUEUE_PORT,
    FD_METRICS_PORT,
    FDServer,
    clean_ports,
    is_port_open,
)

FD_CONTROLLER_PORT = int(os.getenv("FD_CONTROLLER_PORT", 8333))


@pytest.fixture(scope="session", autouse=True)
def setup_and_run_server():
    """启动测试服务"""
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = "0,1"
    env["ENABLE_V1_KVCACHE_SCHEDULER"] = "1"

    base_path = os.getenv("MODEL_PATH")
    if base_path:
        model_path = os.path.join(base_path, "TP2")
    else:
        model_path = "./TP2"

    server_args = [
        "--controller-port", str(FD_CONTROLLER_PORT),
        "--tensor-parallel-size", "2",
        "--quantization", "wint8",
        "--max-model-len", "32768",
        "--max-num-seqs", "1",
        "--gpu-memory-utilization", "0.9",
        "--load-strategy", "ipc_snapshot",
        "--dynamic-load-weight"
    ]

    with FDServer(model_path, server_args, env_dict=env) as fd_server:
        yield fd_server


def send_concurrent_requests(num_requests, api_url):
    """并发发送请求"""

    def send_request():
        return requests.post(api_url, json={"prompt": "test"})

    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        return [f.result() for f in futures]


def test_metrics_with_weight_clear_and_reset(setup_and_run_server):
    """测试metrics接口在清空权重和重置调度器后的行为"""
    # 使用环境变量中的端口配置
    api_url = f"http://0.0.0.0:{FD_API_PORT}/v1/completions"
    metrics_url = f"http://0.0.0.0:{FD_METRICS_PORT}/metrics"
    clear_url = f"http://0.0.0.0:{FD_API_PORT}/clear_load_weight"
    reset_url = f"http://0.0.0.0:{FD_CONTROLLER_PORT}/controller/reset_scheduler"

    # 限制max_tokens为50避免耗时过长
    request_data = {
        "prompt": "test",
        "max_tokens": 50,
        "stream": True
    }

    # 启动请求线程
    def send_request():
        with requests.post(api_url, json=request_data, stream=True) as resp:
            for _ in resp.iter_content():
                pass  # 消耗流式响应

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(send_request)

        # 等待请求开始处理
        time.sleep(0.5)

        # 清空权重并验证metrics
        requests.post(clear_url)
        metrics = requests.get(metrics_url).text
        print(metrics)
        assert "fastdeploy:num_requests_running 0" not in metrics
        # assert "fastdeploy:num_requests_waiting 0" not in metrics

        # 重置调度器并验证metrics
        reset_payload = {"reset": True}
        requests.post(reset_url, json=reset_payload)

        metrics = requests.get(metrics_url).text
        assert "fastdeploy:num_requests_running 0" in metrics
        assert "fastdeploy:num_requests_waiting 0" in metrics

        # 取消未完成的请求
        future.cancel()

```
存在bug：开了流式后resp.iter_content()会一直hang住，没有设置基础的超时，或者直接用非流式就可以解决

修改后可以正常测试metrics这个reset scheduler的场景

```
import os
import time
import pytest
import requests
from concurrent.futures import ThreadPoolExecutor
from utils.serving_utils import (
    FD_API_PORT,
    FD_CACHE_QUEUE_PORT,
    FD_ENGINE_QUEUE_PORT,
    FD_METRICS_PORT,
    FDServer,
    clean_ports,
    is_port_open,
)

FD_CONTROLLER_PORT = int(os.getenv("FD_CONTROLLER_PORT", 8333))


@pytest.fixture(scope="session", autouse=True)
def setup_and_run_server():
    """启动测试服务"""
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = "0,1"
    env["ENABLE_V1_KVCACHE_SCHEDULER"] = "1"

    base_path = os.getenv("MODEL_PATH")
    if base_path:
        model_path = os.path.join(base_path, "TP2")
    else:
        model_path = "./TP2"

    server_args = [
        "--controller-port", str(FD_CONTROLLER_PORT),
        "--tensor-parallel-size", "2",
        "--quantization", "wint8",
        "--max-model-len", "32768",
        "--max-num-seqs", "1",
        "--gpu-memory-utilization", "0.9",
        "--load-strategy", "ipc_snapshot",
        "--dynamic-load-weight"
    ]

    with FDServer(model_path, server_args, env_dict=env) as fd_server:
        yield fd_server


def send_concurrent_requests(num_requests, api_url):
    """并发发送请求"""

    def send_request():
        return requests.post(api_url, json={"prompt": "test"})

    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        return [f.result() for f in futures]


def test_metrics_with_weight_clear_and_reset(setup_and_run_server):
    """测试metrics接口在清空权重和重置调度器后的行为"""
    # 使用环境变量中的端口配置
    api_url = f"http://0.0.0.0:{FD_API_PORT}/v1/completions"
    metrics_url = f"http://0.0.0.0:{FD_METRICS_PORT}/metrics"
    clear_url = f"http://0.0.0.0:{FD_API_PORT}/clear_load_weight"
    reset_url = f"http://0.0.0.0:{FD_CONTROLLER_PORT}/controller/reset_scheduler"

    # 限制max_tokens为50避免耗时过长
    request_data = {
        "prompt": "test",
        "max_tokens": 50,
        "stream": False
    }

    # 启动请求线程
    def send_request():
        try:
            requests.post(api_url, json=request_data, timeout=10)
        except Exception as e:
            print(e)

    with ThreadPoolExecutor(max_workers=10) as executor:
        future = executor.submit(send_request)

        time.sleep(0.5)

        # 清空权重并验证metrics
        requests.post(clear_url)
        metrics = requests.get(metrics_url).text
        print(metrics)
        assert "fastdeploy:num_requests_running 0" not in metrics
        # assert "fastdeploy:num_requests_waiting 0" not in metrics

        # 重置调度器并验证metrics
        r = requests.post(reset_url, json={"reset": True}, timeout=30)
        assert r.status_code == 200, f"reset_scheduler failed: {r.status_code}"

        metrics = requests.get(metrics_url).text
        print(metrics, "RESET")
        assert "fastdeploy:num_requests_running 0" in metrics
        assert "fastdeploy:num_requests_waiting 0" in metrics

```


## 4. 实践经验总结
* **Rules 的方式比传统 chat prompt 更稳定且易用，对于已有代码库的结构化改造或场景补充方面效果比较好**：**主动分析代码并受rules制约**
* **对于场景明确、流程清晰的需求，效果更好**

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
