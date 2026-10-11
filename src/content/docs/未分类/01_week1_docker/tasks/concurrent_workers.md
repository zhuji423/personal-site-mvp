---
title: "并发 Workers 实战"
description: "核心任务：用三种方案实现「并发起 16 个 Docker 容器、每个容器跑一个验证任务、主进程收集 reward」的完整 demo。 前置条件：本地已安装 Docker 和 Docker Compose，理解 Namespace/Cgrou"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\01_week1_docker\\tasks\\concurrent_workers.md"
---
# 并发 Workers 实战

> **核心任务**：用三种方案实现「并发起 16 个 Docker 容器、每个容器跑一个验证任务、主进程收集 reward」的完整 demo。
>
> **前置条件**：本地已安装 Docker 和 Docker Compose，理解 Namespace/Cgroups 基本概念。

→ 参见 [container_orchestration.md](../concepts/container_orchestration.md) 了解编排原理
→ 参见 [namespace_cgroups.md](../concepts/namespace_cgroups.md) 了解容器的资源限制

---

## 方案 1：Docker Compose + --scale

> **适用场景**：任务逻辑简单、所有 worker 完全相同、不需要精细化的任务分发。

### 1.1 完整的 docker-compose.yml

```yaml
# docker-compose.yml
version: "3.8"

services:
  # Redis 作为任务队列和结果存储
  queue:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  # Worker 服务（通过 --scale 控制数量）
  worker:
    build:
      context: .
      dockerfile: Dockerfile.worker
    deploy:
      replicas: 1          # 默认 1 个，通过 --scale 覆盖
      resources:
        limits:
          cpus: "0.5"      # 每个 worker 最多用 0.5 核 CPU
          memory: "512M"   # 每个 worker 最多用 512MB 内存
        reservations:
          cpus: "0.25"     # 保证至少有 0.25 核
          memory: "256M"   # 保证至少有 256MB
    volumes:
      # 只读挂载知识库（16 个 worker 共享，CoW）
      - knowledge-base:/data:ro
    environment:
      # Worker 从 Redis 队列取任务
      - REDIS_URL=redis://queue:6379
      - WORKER_TIMEOUT=300        # 单任务超时 5 分钟
      - WORKER_MAX_TASKS=10       # 每个 worker 最多处理 10 个任务后退出
    depends_on:
      queue:
        condition: service_healthy
    restart: on-failure           # 失败自动重启（最多 3 次）

  # Aggregator（结果收集器）
  aggregator:
    build:
      context: .
      dockerfile: Dockerfile.aggregator
    environment:
      - REDIS_URL=redis://queue:6379
    depends_on:
      queue:
        condition: service_healthy
    restart: on-failure

volumes:
  knowledge-base:
    external: true  # 预先创建的知识库 volume
```

### 1.2 Worker 的 Dockerfile

```dockerfile
# Dockerfile.worker
FROM python:3.11-slim

# 安装依赖
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 复制 worker 代码
COPY worker.py /app/worker.py
COPY verify.py /app/verify.py

WORKDIR /app

# Worker 入口：持续从 Redis 队列取任务执行
CMD ["python", "worker.py"]
```

### 1.3 Worker 代码

```python
# worker.py
"""
Worker 进程：从 Redis 队列取任务，执行验证，回报结果。
每个 worker 会持续取任务直到队列为空或达到最大任务数。
"""

import json
import os
import time
import redis
import subprocess

# 环境变量配置
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
WORKER_TIMEOUT = int(os.environ.get("WORKER_TIMEOUT", "300"))
WORKER_MAX_TASKS = int(os.environ.get("WORKER_MAX_TASKS", "10"))

def main():
    # 连接 Redis
    r = redis.from_url(REDIS_URL)

    tasks_processed = 0

    while tasks_processed < WORKER_MAX_TASKS:
        # 从队列中阻塞取任务（timeout=1s 避免永久阻塞）
        task_data = r.brpop("task_queue", timeout=1)

        if task_data is None:
            # 队列为空，等待一会再检查
            time.sleep(1)
            continue

        _, task_json = task_data
        task = json.loads(task_json)

        print(f"[Worker] Processing task: {task['task_id']}")

        try:
            # 执行验证任务
            result = run_verification(task)

            # 将结果存入 Redis
            r.rpush("result_queue", json.dumps(result))
            r.incr("tasks_completed")  # 计数器

            print(f"[Worker] Task {task['task_id']} completed. "
                  f"Reward: {result['reward']:.3f}")

        except subprocess.TimeoutExpired:
            # 超时处理
            result = {
                "task_id": task["task_id"],
                "reward": 0.0,
                "status": "timeout",
                "error": f"Execution exceeded {WORKER_TIMEOUT}s",
            }
            r.rpush("result_queue", json.dumps(result))
            r.incr("tasks_timeout")

        except Exception as e:
            # 异常处理
            result = {
                "task_id": task["task_id"],
                "reward": 0.0,
                "status": "error",
                "error": str(e),
            }
            r.rpush("result_queue", json.dumps(result))
            r.incr("tasks_error")

        tasks_processed += 1

    print(f"[Worker] Processed {tasks_processed} tasks. Exiting.")


def run_verification(task: dict) -> dict:
    """执行验证任务"""
    patch = task["patch"]
    instance_id = task["instance_id"]
    test_commands = task["test_commands"]

    # 应用 patch
    subprocess.run(
        ["git", "apply", "--check", patch],
        capture_output=True, timeout=30, check=True,
    )
    subprocess.run(
        ["git", "apply", patch],
        capture_output=True, timeout=30, check=True,
    )

    # 运行测试
    start_time = time.time()
    result = subprocess.run(
        test_commands,
        shell=True,
        capture_output=True,
        text=True,
        timeout=WORKER_TIMEOUT,
    )
    elapsed = time.time() - start_time

    # 解析测试结果，计算 reward
    reward = compute_reward(result, elapsed)

    # 回滚 patch（重置状态）
    subprocess.run(
        ["git", "checkout", "."],
        capture_output=True, timeout=30,
    )

    return {
        "task_id": task["task_id"],
        "reward": reward,
        "status": "success",
        "passed": 47,     # 简化：实际需要解析测试输出
        "failed": 3,
        "total": 50,
        "execution_time": elapsed,
    }


def compute_reward(result, elapsed):
    """计算 reward（binary + continuous 混合）"""
    if result.returncode == 0:
        return 1.0  # 测试全通过
    else:
        # 部分通过的连续 reward（简化版）
        return 0.5


if __name__ == "__main__":
    main()
```

### 1.4 Aggregator 代码

```python
# aggregator.py
"""
结果收集器：从 Redis 结果队列中收集所有验证结果，汇总统计。
"""

import json
import os
import redis

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")

def main():
    r = redis.from_url(REDIS_URL)

    # 等待所有任务完成（检查任务计数）
    total_tasks = int(r.get("total_tasks") or 0)
    completed = 0

    results = []

    print(f"[Aggregator] Waiting for {total_tasks} results...")

    while completed < total_tasks:
        # 阻塞等待结果
        _, result_json = r.blpop("result_queue", timeout=5)
        if result_json is None:
            continue

        result = json.loads(result_json)
        results.append(result)
        completed += 1

        if completed % 10 == 0:
            print(f"[Aggregator] Progress: {completed}/{total_tasks}")

    # 汇总统计
    rewards = [r["reward"] for r in results]
    avg_reward = sum(rewards) / len(rewards) if rewards else 0
    pass_count = sum(1 for r in results if r["reward"] >= 1.0)
    timeout_count = sum(1 for r in results if r["status"] == "timeout")
    error_count = sum(1 for r in results if r["status"] == "error")

    summary = {
        "total_tasks": total_tasks,
        "completed": completed,
        "avg_reward": avg_reward,
        "pass_rate": pass_count / total_tasks if total_tasks > 0 else 0,
        "timeout_count": timeout_count,
        "error_count": error_count,
    }

    # 输出结果
    print("\n" + "=" * 50)
    print("VERIFICATION SUMMARY")
    print("=" * 50)
    print(f"Total tasks:       {summary['total_tasks']}")
    print(f"Avg reward:        {summary['avg_reward']:.3f}")
    print(f"Pass rate:         {summary['pass_rate']:.1%}")
    print(f"Timeouts:          {summary['timeout_count']}")
    print(f"Errors:            {summary['error_count']}")
    print("=" * 50)

    # 保存详细结果到文件
    with open("verification_results.jsonl", "w") as f:
        for result in results:
            f.write(json.dumps(result) + "\n")

    print(f"Detailed results saved to verification_results.jsonl")


if __name__ == "__main__":
    main()
```

### 1.5 使用方式

```bash
# Step 1: 创建知识库 volume
docker volume create knowledge-base
docker run --rm -v knowledge-base:/data alpine sh -c "echo 'knowledge data' > /data/info.txt"

# Step 2: 构建 worker 镜像
docker-compose build

# Step 3: 启动 Redis + Aggregator + 16 个 Worker
docker-compose up --scale worker=16 -d

# Step 4: 往队列中投递任务
python submit_tasks.py tasks.jsonl  # 把任务推入 Redis task_queue

# Step 5: 查看进度
docker-compose logs -f worker  # 实时查看 worker 日志

# Step 6: 查看 Aggregator 的汇总结果
docker-compose logs aggregator

# Step 7: 停止所有服务
docker-compose down
```

---

## 方案 2：Python Docker SDK（编程式容器管理）

> **适用场景**：需要精细化的并发控制、动态扩缩容、自定义任务分发逻辑。
> **优势**：代码灵活度高，可以实现 warm pool、优先级调度、结果实时收集等功能。

### 2.1 完整代码

```python
"""
concurrent_workers_v2.py

用 Python Docker SDK 实现 16 个并发 Worker 验证。
特点：
- 基于 asyncio + Semaphore 的并发控制
- 每个任务在独立 Docker 容器中执行
- 实时收集和汇总 reward
- 支持超时、异常处理、重试
"""

import asyncio
import json
import time
import docker
from dataclasses import dataclass, asdict
from typing import Optional
from pathlib import Path


# ============================================================
# 数据结构定义
# ============================================================

@dataclass
class Task:
    """验证任务"""
    task_id: str
    patch: str
    instance_id: str
    test_commands: list[str]
    priority: int = 0


@dataclass
class Result:
    """验证结果"""
    task_id: str
    instance_id: str
    reward: float
    passed: int
    failed: int
    total: int
    execution_time: float
    status: str  # success / timeout / error
    error_message: Optional[str] = None
    container_id: Optional[str] = None
    timestamp: Optional[str] = None

    def to_json(self) -> str:
        return json.dumps(asdict(self))


# ============================================================
# Reward Function
# ============================================================

def compute_reward(test_output: str, return_code: int, elapsed: float) -> float:
    """
    多维度 reward function：
    - 测试通过率（权重 0.6）
    - 执行时间惩罚（权重 0.2）
    - 是否有 lint 错误（权重 0.2）
    """
    # 维度 1: 测试通过率
    if return_code == 0:
        test_score = 1.0
    else:
        # 从测试输出中解析通过/失败数
        passed = test_output.count("PASSED")
        failed = test_output.count("FAILED")
        total = passed + failed
        test_score = passed / total if total > 0 else 0.0

    # 维度 2: 执行时间（越短越好，超时为 0）
    if elapsed > 300:
        time_score = 0.0
    else:
        time_score = max(0, 1.0 - elapsed / 300)

    # 维度 3: Lint 检查（简化版：检查是否有 error 级别的输出）
    lint_errors = test_output.count("ERROR")
    lint_score = 1.0 if lint_errors == 0 else 0.0

    # 加权汇总
    reward = 0.6 * test_score + 0.2 * time_score + 0.2 * lint_score
    return round(reward, 4)


# ============================================================
# 容器管理器
# ============================================================

class DockerWorkerPool:
    """基于 Docker SDK 的 Worker 池"""

    def __init__(
        self,
        image: str,
        max_workers: int = 16,
        cpu_quota: float = 0.5,
        memory_limit: str = "512m",
        timeout: int = 300,
        shared_volume: Optional[str] = None,
    ):
        self.image = image
        self.max_workers = max_workers
        self.cpu_quota = cpu_quota
        self.memory_limit = memory_limit
        self.timeout = timeout
        self.shared_volume = shared_volume
        self.client = docker.from_env()
        self.semaphore = asyncio.Semaphore(max_workers)  # 并发控制
        self.results: list[Result] = []
        self._lock = asyncio.Lock()

    async def submit_task(self, task: Task) -> Result:
        """
        提交单个任务，等待执行完成。
        Semaphore 确保同时最多 max_workers 个任务在运行。
        """
        async with self.semaphore:
            result = await self._execute_in_container(task)
            async with self._lock:
                self.results.append(result)
            return result

    async def submit_tasks(self, tasks: list[Task]) -> list[Result]:
        """批量提交任务，并行执行"""
        coros = [self.submit_task(task) for task in tasks]
        return await asyncio.gather(*coros)

    async def _execute_in_container(self, task: Task) -> Result:
        """在独立 Docker 容器中执行验证任务"""
        container = None
        start_time = time.time()

        try:
            # Step 1: 创建容器
            container_kwargs = {
                "image": self.image,
                "command": f"bash -c 'echo {json.dumps(asdict(task))} > /tmp/task.json && python /app/verify.py /tmp/task.json'",
                "detach": True,  # 后台运行
                "cpu_quota": int(self.cpu_quota * 100000),  # 0.5 CPU
                "mem_limit": self.memory_limit,
                "pids_limit": 100,
                "network_disabled": True,  # 禁用网络（安全考虑）
            }

            # 挂载只读共享卷（知识库）
            if self.shared_volume:
                container_kwargs["volumes"] = {
                    self.shared_volume: {"bind": "/data", "mode": "ro"}
                }

            # Step 2: 启动容器
            container = self.client.containers.run(**container_kwargs)

            # Step 3: 等待执行完成（带超时）
            exec_result = container.wait(timeout=self.timeout)

            elapsed = time.time() - start_time

            # Step 4: 收集输出
            logs = container.logs(stdout=True, stderr=True).decode("utf-8")

            # Step 5: 解析结果
            try:
                output_data = json.loads(logs.strip().split("\n")[-1])
                reward = compute_reward(
                    test_output=logs,
                    return_code=exec_result["StatusCode"],
                    elapsed=elapsed,
                )
                return Result(
                    task_id=task.task_id,
                    instance_id=task.instance_id,
                    reward=reward,
                    passed=output_data.get("passed", 0),
                    failed=output_data.get("failed", 0),
                    total=output_data.get("total", 0),
                    execution_time=round(elapsed, 2),
                    status="success" if exec_result["StatusCode"] == 0 else "failed",
                    container_id=container.short_id,
                    timestamp=time.strftime("%Y-%m-%dT%H:%M:%S"),
                )
            except (json.JSONDecodeError, KeyError):
                return Result(
                    task_id=task.task_id,
                    instance_id=task.instance_id,
                    reward=0.0,
                    passed=0,
                    failed=0,
                    total=0,
                    execution_time=round(elapsed, 2),
                    status="parse_error",
                    error_message="Failed to parse container output",
                    container_id=container.short_id,
                )

        except docker.errors.APIError as e:
            elapsed = time.time() - start_time
            return Result(
                task_id=task.task_id,
                instance_id=task.instance_id,
                reward=0.0,
                passed=0,
                failed=0,
                total=0,
                execution_time=round(elapsed, 2),
                status="docker_error",
                error_message=str(e),
            )

        except Exception as e:
            elapsed = time.time() - start_time
            return Result(
                task_id=task.task_id,
                instance_id=task.instance_id,
                reward=0.0,
                passed=0,
                failed=0,
                total=0,
                execution_time=round(elapsed, 2),
                status="exception",
                error_message=str(e),
            )

        finally:
            # Step 6: 清理容器（无论成功失败都要清理）
            if container:
                try:
                    container.remove(force=True)
                except Exception:
                    pass  # 清理失败不影响主流程

    def get_summary(self) -> dict:
        """获取汇总统计"""
        if not self.results:
            return {"total": 0}

        rewards = [r.reward for r in self.results]
        return {
            "total": len(self.results),
            "avg_reward": round(sum(rewards) / len(rewards), 4),
            "max_reward": round(max(rewards), 4),
            "min_reward": round(min(rewards), 4),
            "pass_count": sum(1 for r in self.results if r.reward >= 1.0),
            "timeout_count": sum(1 for r in self.results if r.status == "timeout"),
            "error_count": sum(1 for r in self.results if r.status in ("error", "exception")),
            "total_execution_time": round(sum(r.execution_time for r in self.results), 2),
        }


# ============================================================
# 主程序
# ============================================================

async def main():
    """主程序：批量提交任务，并行执行，收集结果"""

    # Step 1: 准备任务
    tasks = []
    for i in range(32):  # 32 个任务
        tasks.append(Task(
            task_id=f"task-{i:04d}",
            patch=f"diff --git a/auth.py b/auth.py\n--- a/auth.py\n+++ b/auth.py\n@@ -42,1 +42,1 @@\n-        if username is None:\n+        if not username:\n",
            instance_id=f"instance-{i:04d}",
            test_commands=["cd /workspace && pytest tests/ -v --tb=short"],
        ))

    # Step 2: 创建 Worker Pool
    pool = DockerWorkerPool(
        image="agent-verify:latest",
        max_workers=16,           # 最多 16 个容器并行
        cpu_quota=0.5,            # 每个容器 0.5 CPU
        memory_limit="512m",      # 每个容器 512MB 内存
        timeout=300,              # 单任务超时 5 分钟
        shared_volume="knowledge-base",  # 只读共享知识库
    )

    # Step 3: 提交所有任务（并行执行，Semaphore 控制并发度）
    print(f"Submitting {len(tasks)} tasks with max {pool.max_workers} workers...")
    overall_start = time.time()

    results = await pool.submit_tasks(tasks)

    overall_elapsed = time.time() - overall_start

    # Step 4: 输出结果
    summary = pool.get_summary()
    print("\n" + "=" * 60)
    print("VERIFICATION RESULTS")
    print("=" * 60)
    print(f"Total tasks:         {summary['total']}")
    print(f"Workers used:        {pool.max_workers}")
    print(f"Avg reward:          {summary['avg_reward']}")
    print(f"Pass count (>=1.0):  {summary['pass_count']}")
    print(f"Timeouts:            {summary['timeout_count']}")
    print(f"Errors:              {summary['error_count']}")
    print(f"Total exec time:     {summary['total_execution_time']}s")
    print(f"Wall clock time:     {overall_elapsed:.2f}s")
    print(f"Throughput:          {summary['total'] / overall_elapsed:.2f} tasks/s")
    print("=" * 60)

    # Step 5: 保存详细结果
    output_path = Path("results.jsonl")
    with open(output_path, "w") as f:
        for r in results:
            f.write(r.to_json() + "\n")
    print(f"Detailed results saved to {output_path}")


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 方案 3：带 Warm Pool 的 Python 实现

> **适用场景**：需要极低延迟的任务执行（< 0.5s 冷启动），任务频率高且需要频繁创建/销毁容器。
> **核心改进**：预创建容器池，任务到来时直接复用已有容器。

### 3.1 完整代码

```python
"""
concurrent_workers_v3.py

带 Warm Pool 的并发 Worker 实现。
特点：
- 预创建 N 个就绪容器，消除冷启动延迟
- 任务到来时直接从池中取出容器
- 执行完成后重置状态，归还池中
- 基于信号量的并发控制
"""

import asyncio
import json
import time
import docker
from dataclasses import dataclass, asdict
from typing import Optional
from pathlib import Path
from collections import deque


@dataclass
class Task:
    task_id: str
    patch: str
    instance_id: str
    test_commands: list[str]
    priority: int = 0


@dataclass
class Result:
    task_id: str
    instance_id: str
    reward: float
    execution_time: float
    status: str
    error_message: Optional[str] = None


class WarmContainerPool:
    """
    Warm Pool：预创建并维护一批就绪容器。

    关键设计：
    1. 初始化时预创建 pool_size 个容器
    2. 容器运行 `tail -f /dev/null` 保持存活但不消耗 CPU
    3. acquire() 从池中取出一个容器（如果池空则等待或创建新的）
    4. release() 重置容器状态并归还池中
    5. 定期健康检查，不健康的容器自动替换
    """

    def __init__(
        self,
        image: str,
        pool_size: int = 16,
        cpu_quota: float = 0.5,
        memory_limit: str = "512m",
        reset_command: str = "cd /workspace && git checkout . && git clean -fd",
    ):
        self.image = image
        self.pool_size = pool_size
        self.cpu_quota = cpu_quota
        self.memory_limit = memory_limit
        self.reset_command = reset_command
        self.client = docker.from_env()

        # 容器池：可用容器队列
        self.available: deque = deque()
        # 正在使用中的容器
        self.in_use: set = set()
        # 用于 acquire 的信号量
        self.semaphore = asyncio.Semaphore(pool_size)

    async def initialize(self):
        """预创建 pool_size 个就绪容器"""
        print(f"[WarmPool] Initializing pool with {self.pool_size} containers...")
        tasks = [self._create_container() for _ in range(self.pool_size)]
        containers = await asyncio.gather(*tasks)

        for container in containers:
            self.available.append(container)

        print(f"[WarmPool] Pool ready. {len(self.available)} containers available.")

    async def acquire(self) -> docker.models.containers.Container:
        """
        从池中取出一个容器。
        如果池为空，等待信号量（有容器被 release 时唤醒）。
        """
        await self.semaphore.acquire()
        container = self.available.popleft()
        self.in_use.add(container.id)

        # 健康检查：确认容器仍然在运行
        container.reload()  # 刷新容器状态
        if container.status != "running":
            # 容器不健康，创建新的
            try:
                container.remove(force=True)
            except Exception:
                pass
            container = await self._create_container()

        return container

    async def release(self, container: docker.models.containers.Container):
        """
        归还容器：重置状态后放回池中。
        如果重置失败，销毁并创建新的。
        """
        try:
            # 重置容器状态（恢复到干净的初始状态）
            exit_code, output = container.exec_run(
                self.reset_command,
                demux=True,
            )

            if exit_code == 0:
                # 重置成功，放回池中
                self.available.append(container)
            else:
                # 重置失败，销毁并创建新的
                print(f"[WarmPool] Reset failed: {output}")
                container.remove(force=True)
                new_container = await self._create_container()
                self.available.append(new_container)

        except Exception as e:
            print(f"[WarmPool] Release error: {e}")
            container.remove(force=True)
            new_container = await self._create_container()
            self.available.append(new_container)

        finally:
            self.in_use.discard(container.id)
            self.semaphore.release()  # 唤醒等待中的 acquire

    async def _create_container(self) -> docker.models.containers.Container:
        """创建一个新的就绪容器"""
        container = self.client.containers.run(
            image=self.image,
            command="tail -f /dev/null",  # 保持运行但不消耗 CPU
            detach=True,
            cpu_quota=int(self.cpu_quota * 100000),
            mem_limit=self.memory_limit,
            pids_limit=100,
            volumes={
                "knowledge-base": {"bind": "/data", "mode": "ro"}
            },
        )
        # 等待容器完全启动
        await asyncio.sleep(0.5)
        return container

    async def shutdown(self):
        """关闭池：停止并删除所有容器"""
        for container in list(self.available):
            container.remove(force=True)
        for container_id in self.in_use:
            try:
                c = self.client.containers.get(container_id)
                c.remove(force=True)
            except Exception:
                pass
        print("[WarmPool] All containers removed.")

    @property
    def stats(self) -> dict:
        """返回池的状态统计"""
        return {
            "available": len(self.available),
            "in_use": len(self.in_use),
            "pool_size": self.pool_size,
        }


class WarmPoolScheduler:
    """基于 Warm Pool 的任务调度器"""

    def __init__(self, pool: WarmContainerPool, timeout: int = 300):
        self.pool = pool
        self.timeout = timeout
        self.results: list[Result] = []
        self._lock = asyncio.Lock()

    async def submit_task(self, task: Task) -> Result:
        """提交任务：从 Warm Pool 取容器 → 执行 → 归还容器"""
        container = await self.pool.acquire()
        start_time = time.time()

        try:
            # 在已有容器中执行命令（不需要创建新容器！）
            # 使用 docker exec 在运行中的容器里执行
            exit_code, output = container.exec_run(
                cmd=f"bash -c 'cd /workspace && {task.test_commands[0]}'",
                demux=True,
            )

            elapsed = time.time() - start_time
            stdout = output[0].decode() if output[0] else ""
            stderr = output[1].decode() if output[1] else ""

            # 计算 reward
            reward = self._compute_reward(exit_code, stdout, elapsed)

            result = Result(
                task_id=task.task_id,
                instance_id=task.instance_id,
                reward=reward,
                execution_time=round(elapsed, 2),
                status="success" if exit_code == 0 else "failed",
                error_message=stderr[:500] if exit_code != 0 else None,
            )

        except Exception as e:
            elapsed = time.time() - start_time
            result = Result(
                task_id=task.task_id,
                instance_id=task.instance_id,
                reward=0.0,
                execution_time=round(elapsed, 2),
                status="error",
                error_message=str(e),
            )

        finally:
            # 归还容器到 Warm Pool
            await self.pool.release(container)

        async with self._lock:
            self.results.append(result)

        return result

    async def submit_tasks(self, tasks: list[Task]) -> list[Result]:
        """批量提交任务"""
        coros = [self.submit_task(task) for task in tasks]
        return await asyncio.gather(*coros)

    def _compute_reward(self, exit_code: int, output: str, elapsed: float) -> float:
        """计算 reward"""
        if exit_code == 0:
            return 1.0  # 测试全通过
        else:
            passed = output.count(" passed")
            failed = output.count(" failed")
            total = passed + failed
            return round(passed / total if total > 0 else 0.0, 4)


async def main():
    # Step 1: 初始化 Warm Pool（预创建 16 个容器）
    pool = WarmContainerPool(
        image="agent-verify:latest",
        pool_size=16,
        cpu_quota=0.5,
        memory_limit="512m",
    )
    await pool.initialize()

    # Step 2: 准备任务
    tasks = [
        Task(
            task_id=f"task-{i:04d}",
            patch=f"patch-for-task-{i}",
            instance_id=f"instance-{i:04d}",
            test_commands=["pytest tests/ -v"],
        )
        for i in range(32)
    ]

    # Step 3: 创建调度器并提交任务
    scheduler = WarmPoolScheduler(pool)
    overall_start = time.time()

    print(f"\nSubmitting {len(tasks)} tasks with warm pool...")
    results = await scheduler.submit_tasks(tasks)

    overall_elapsed = time.time() - overall_start

    # Step 4: 输出结果
    rewards = [r.reward for r in results]
    print("\n" + "=" * 60)
    print("WARM POOL VERIFICATION RESULTS")
    print("=" * 60)
    print(f"Pool size:           {pool.pool_size}")
    print(f"Total tasks:         {len(results)}")
    print(f"Avg reward:          {round(sum(rewards)/len(rewards), 4)}")
    print(f"Pass rate:           {sum(1 for r in rewards if r >= 1.0)/len(rewards):.1%}")
    print(f"Wall clock time:     {overall_elapsed:.2f}s")
    print(f"Throughput:          {len(results)/overall_elapsed:.2f} tasks/s")
    print(f"Pool stats:          {pool.stats}")
    print("=" * 60)

    # Step 5: 清理
    await pool.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 三种方案对比

| 特性 | 方案 1: Compose Scale | 方案 2: Python SDK | 方案 3: Warm Pool |
|------|----------------------|-------------------|-------------------|
| 实现复杂度 | 低 | 中 | 高 |
| 冷启动延迟 | 3-10s | 3-10s | < 0.5s |
| 并发控制 | 固定 N 个 worker | Semaphore 动态控制 | Semaphore + 池 |
| 任务分发 | 外部（Redis 队列） | 内部（asyncio.gather） | 内部（asyncio.gather） |
| 容器复用 | 否（每次新建） | 否（每次新建） | 是（池化复用） |
| 结果收集 | 外部（Redis + Aggregator） | 内部（直接返回） | 内部（直接返回） |
| 故障恢复 | restart_policy | 手动重试 | 手动重试 |
| 适用规模 | < 50 个任务 | < 1000 个任务 | 高频小任务 |
| 学习价值 | 理解 Compose 基础 | 理解 Docker API | 理解 Warm Pool |

**推荐学习路径**：先跑通方案 1（理解基本流程），再实现方案 2（掌握 Docker API 编程），最后实现方案 3（理解 Warm Pool 优化）。
