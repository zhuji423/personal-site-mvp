---
title: "环境构建搭建与调试文档"
description: "https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-Ma/U-RwwdZ7ut/hSxm6qPSyIBIU7"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\testone-llm\\common_aiqa\\README.md"
---

# 环境构建搭建与调试文档


https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/hSxm6qPSyIBIU7


# 环境要求
```
python 3.11+
```

## MacOS 依赖安装
```
sh build.sh
```

## deepseek密钥配置：
```
# 修改.env文件，配置DEEPSEEK_API_KEY
export DEEPSEEK_API_KEY=your_api_key
```

## 验证依赖是否安装成功：
```bash
# 进入src目录运行
python3 basic_agent.py
```
在控制台正常输出结果，则说明依赖安装成功。


若报错，请检查python版本与依赖是否安装成功。

python版本检查：
```
python3 --version
```

# 启动入口

项目有两个启动入口：
```
src/basic_agent.py
```

```
src/main.py
```

src/basic_agent.py用于快速验证环境是否搭建成功。以及agno框架的基本功能使用验证。

src/main.py用于启动整个AIQA项目。






