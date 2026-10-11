---
title: "安装UV"
description: "【墙裂推荐】使用uv代替pip-提速10x~100x"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🧰【必看】工欲善必先利其器\\📄 【墙裂推荐】使用uv代替pip-_提速10x~100x.md"
---
【墙裂推荐】使用uv代替pip->提速10x~100x

日常安装python的各种依赖方式，pip install -r requirements.txt 非常慢，可以切换至uv, 提速10x~100x

> Github主页：[https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
> 关于uv比pip快10~100倍的测试说明：[https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 安装UV
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
> icoding等没有外网权限的机器，可以使用这个
> wget [https://qep-testone.bj.bcebos.com/packages/uvx](https://qep-testone.bj.bcebos.com/packages/uvx) -O  {YOUR_PATH}/uvx
> wget [https://qep-testone.bj.bcebos.com/packages/uv](https://qep-testone.bj.bcebos.com/packages/uv) -O {YOUR_PATH}/uv
> chmod +x {YOUR_PATH}/uv {YOUR_PATH}/uvx


# 使用UV
> 和之前使用pip的方式一样，前面加上uv 即可
|pip|uv|
|-|-|
|pip install xxxx|uv pip install xxx|
|pip install -r requirements.txt|uv pip install -r requirements.txt|



![](/personal-site-mvp/img/doc-placeholder.svg "")

