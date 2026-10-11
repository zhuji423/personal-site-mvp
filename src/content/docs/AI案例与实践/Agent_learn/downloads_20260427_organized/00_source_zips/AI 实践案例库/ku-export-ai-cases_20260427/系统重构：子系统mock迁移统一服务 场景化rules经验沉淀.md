---
title: "文心Mock服务器项目开发规则"
description: "系统重构：子系统mock迁移统一服务 场景化rules经验沉淀"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\系统重构：子系统mock迁移统一服务 场景化rules经验沉淀.md"
---
系统重构：子系统mock迁移统一服务 场景化rules经验沉淀

#### 🧑‍🏫 案例作者：[@杨晨琦](https://ku.baidu-int.com?t=mention&mt=contact&id=19356c80-fce4-11f0-a591-8f2d8f797d14)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了在文心一言调度子系统mock能力迁移项目中的经验，通过制定详细的开发流程rules，将分散的mock能力统一迁移至新服务，实现了统一管理和融合。文中详细介绍了rules的生成、调优、分发及具体实现过程，包括服务实现规范、日志管理、配置管理、Mock数据管理、错误处理模式等，为类似项目提供了可借鉴的场景化rules经验沉淀。
项目背景：文心一言调度有众多的下游子系统，以往子系统的mock能力都是在不同的目录下分别开发，现在需要迁移到一个统一服务下进行统一管理和融合。

## 开发流程rules生成
可以先让zulu写出一个初版的rules并直接写入到rules目录下。

这里让它依据过去的实践总结出一个迁移的规则

```
参考grpc_mock/eb45_preprocess迁移到grpc_mock_server/sub_servers/preprocess和grpc_mock_server/grpc_src中的方式，帮我总结一个子系统迁移的rules
将以上rules内容写入到.comate/rules/server-move-rules.mdr这个文件里
```


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7b780641520b469a92de5f9cbdd61302&docGuid=EupZzcoRxNM8hf "")


对于场景级的rules：不需要重新写一遍系统级别的介绍。确立一个主要rules，该rules主要是对项目的**整体介绍+开发规范+拆分场景索引**，然后在不同开发流程索引中填充负责各模块/功能需求的具体的rules。

## 依照rules提出开发需求
```
将grpc_mock/eb45_ds迁移到grpc_mock_server中   #server-move-rules.mdr
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3fc75b158d0f4d3aa9c26f2a260dbe1c&docGuid=EupZzcoRxNM8hf "")


对于场景级的rules：不应该是泛泛的开发规范，而应该罗列出来具体的步骤和检查list

## rules调优
核心：根据实际需要，在zulu生成代码过程中按照需求进行干预，并且及时沉淀到rules中

```
参考grpc_mock_server/sub_servers下其他server文件的实现，对Server类进行服务类基类改造，去除掉例如setup_logger,print_thread_count等单独实现函数，使用SUBServer类中的相关实现替代。 #server-move-rules.mdr
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c548eff455f84ccd8c02a0348e00dc14&docGuid=EupZzcoRxNM8hf "")


对于场景级的rules：在rules中**补充对应的信息和步骤要求**，能够减少不同风格或者不合符项目上下文的代码生成。

## rules分发
往往项目的整体介绍+开发规范是无论什么开发环节都需要的前置知识

所以主要的rules可以是对项目的整体介绍+开发规范+拆分场景索引，在不同开发流程索引中填充具体的rules

## 附
```
---
description: 文心Mock服务器项目开发规则
globs: 
alwaysApply: true
---
# 文心Mock服务器项目开发规则

## 项目概述

**项目名称**: 文心Mock服务器 (Wxyy Mock Server)
**核心目标**: 为百度文心产品线提供模拟服务支持，用于测试和开发环境
**技术栈**: Python 3.9 + gRPC + Protocol Buffers + WireMock
**架构模式**: 微服务 + Mock服务容器

## 核心开发契约

### 服务实现规范

**服务创建标准流程**:
1. 定义`.proto`文件创建服务接口
2. 使用`grpc_tools.protoc`生成`{service}_pb2.py`和`{service}_pb2_grpc.py`
3. 实现服务类继承生成的`Servicer`类：`class {Service}Server({service}_pb2_grpc.{Service}Servicer, SUBServer)`
4. 使用标准服务模板，包含日志初始化、mock数据加载、异常处理

**统一服务架构**:
```python
# 标准服务模板结构
class ServiceServer(pb2_grpc.ServiceServicer):
    def __init__(self):
        self.logger = LoggerHelper("service_name").get_logger()
        self.setup_mock_data()

    def ServiceMethod(self, request, context):
        # 1. 获取logid 2. 解析请求 3. 判断mock条件 4. 返回响应
```

### 日志管理契约

**统一日志格式**: `%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s`
**双输出模式**: 同时输出到文件和控制台
**日志文件命名**: `{service_name}.log`（如`eb45_ds.log`）
**日志工具类**: 统一使用`LoggerHelper`进行日志初始化
**默认级别**: INFO级别，支持动态调整
**日志打印规范**: 以下场景必须打印日志：子系统入参（如果是双向流式，则需要打印首尾入参）、首尾出参、转发到真实服务的地址、异常场景

### 配置管理规范

**主配置文件**: `config.yaml`统一管理所有服务配置
**服务端口**: 默认8041端口，支持多服务共存
**消息大小限制**: 统一设置为500MB（524288000字节）
**环境变量**: 支持通过环境变量覆盖配置项

### Mock数据管理

**数据获取优先级**:
1. 本地mock文件（最高优先级）
2. BOS存储数据（`https://bj.bcebos.com/taas/dispatch_mock_data`）
3. 运行时生成的mock数据
4. 转发到真实服务（最低优先级）

**本地文件规范**:
- 目录结构: `{service}_result/`
- 文件格式: 支持JSON和JSONL
- 命名模式: `{model_id}__{scenario}.json`

**数据重构**: 统一使用`restruct_data()`方法保证请求ID一致性

### 错误处理模式

**gRPC状态码**: 使用`grpc.StatusCode.OK`模拟服务断开
**异常处理**: 所有服务必须包含try-catch块并记录异常信息
**超时模拟**: 支持5s、10s、25s、121s等多种超时场景
**错误响应**: 统一格式包含错误码和消息

## 命名与结构规范

### 文件命名约定

**Python文件**:
- 服务文件: `{service}_server.py`
- 客户端文件: `{service}_client.py`
- 生成文件: `{service}_pb2.py`, `{service}_pb2_grpc.py`

**Protocol Buffer文件**:
- 服务定义: `{service}.proto`
- 通用定义: `{domain}_common.proto`
- 版本化服务: `{service}{version}.proto`

**Mock数据文件**:
- 响应文件: `{service}_{feature}_{scenario}.json`
- 测试文件: `api{number}__{test_name}.json`
- 性能测试: `*_perf_test.json`

### 目录结构标准

```
grpc_mock_server/                     # GRPC服务
├── grpc_src/                         # protobuf定义文件
    ├── agrpc_tool.sh                 # 用于根据proto生成该目录下的所有pb2和pb2_grpc文件
    ├── {service}.proto               # proto定义
    ├── {service}_pb2.py
    └── {service}_pb2_grpc.py  
├── sub_servers/                       # 子服务实现
    ├── {service}/
        ├── {service}_result/          # 存储mock数据
        ├── {service}_server.py        # 子系统mock能力实现
        └── ...                        # 子系统相关实现拆分文件
    └── sub_server.py                  # 子系统mock基类，存放子系统通用能力
├── utils/                             # 工具类
├── log/                               # 日志组件
└── mock_server.py                     # mock入口

http_mock/                             # HTTP服务
└── wiremock/mappings/                 # 按业务分类的映射文件
```

### 代码组织规范

**类命名**: `{Service}Server`模式，继承生成的gRPC servicer
**方法命名**: gRPC方法使用PascalCase，工具方法使用snake_case
**包结构**: 按服务类型组织，使用下划线命名法
**注释规范**: 中英文注释，包含参数和返回值说明

## 性能监控与运维

### 监控指标

**核心指标**: CPU使用率、内存使用率、线程数、请求率、错误率
**采集频率**: 默认60秒采集一次
**告警阈值**: CPU>80%、内存>85%、线程数>1000
**线程管理**: 线程池大小100-2000，统一使用`service_worker`前缀

### 部署规范

**Docker基础镜像**: `iregistry.baidu-int.com/baidu-base/python:3.9-centos-unstable`
**工作目录**: `/home/work/`
**依赖安装**: 统一安装`grpcio-tools grpcio requests`
**启动命令**: `python3 /home/work/{service}_server.py`

## 版本与依赖管理

**版本控制**: 遵循Semantic Versioning和PEP-440规范
**依赖源**: 使用百度内部PyPI源`http://pip.baidu.com/root/baidu/+simple/`
**核心依赖**: grpcio、grpcio-tools、PyYAML、requests、psutil、google-protobuf

## 子服务开发指南

**服务端口**: 默认8041端口
**最大并发**: 支持2000线程
**功能特性**:
- 文件响应功能（通过logid指定响应文件）
- 异常场景模拟（超时、服务断开、错误响应）
- 丢包模拟支持

**响应文件格式**: JSON格式，每行一个有效JSON对象

## 关键开发命令

**服务启动**: `/home/work/.deck/1.0/python/3.7.6/bin/python3 /home/disk1/yangchenqi/baidu/nlp-qa/wxyy-mock-server/grpc_mock_server/mock_server.py`
**依赖安装**: `pip install -r requirements.txt -i http://pip.baidu.com/root/baidu/+simple/`
**proto生成**: `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. {service}.proto`

## 开发细则

### 场景开发细则
**子系统迁移**: 若需求为子系统迁移场景，进一步参考server-move-rules.mdr中的迁移步骤进行

### 文件开发细则
... 定义某某文件夹或者某某文件的规范

---

**补充规则**: 所有回答均使用中文
```
```
# 文心Mock服务器子系统迁移规则

## 文件迁移规则

1. **文件类型** | **源路径** | **目标路径** | **处理方式**
   ------------|------------|--------------|-------------
   .proto文件  | `grpc_mock/{service}/{service}.proto` | `grpc_mock_server/grpc_src/{service}.proto` | 保持原名
   服务实现    | `grpc_mock/{service}/{service}_server.py` | `grpc_mock_server/sub_servers/{service}/{service}_server.py` | 保持原名
   mock数据    | `grpc_mock/{service}/mock_data/` | `grpc_mock_server/sub_servers/{service}/{service}_result/` | 保持JSON/JSONL格式

2. **特殊文件处理**  
   - `grpc_tool.sh` → 不再需要，使用`grpc_src/agrpc_tool.sh`统一生成
   - `__init__.py` → 需在`sub_servers/{service}/`下新建

## 代码调整规则

### 统一逻辑改造
参考grpc_mock_server/sub_servers下其他server文件的实现，对Server类进行服务类基类改造，去除掉例如setup_logger,print_thread_count等单独实现函数，使用SUBServer类中的相关实现替代。

### 服务类基类改造
```python
from sub_servers.sub_server import SUBServer

class {Service}Server({service}_pb2_grpc.{Service}Servicer, SUBServer):
    def __init__(self):
        self.logger = LoggerHelper("{SERVICE}").get_logger()  # 注意使用统一日志
        self.setup_mock_data()  # 实现mock数据加载
```

### Mock数据加载规范
```python
def setup_mock_data(self):
    self.mock_data = {}
    for file in glob.glob("sub_servers/{service}/{service}_result/*.json"):
        with open(file) as f:
            self.mock_data.update(json.load(f))
```

## mock_server.py注册规则

### 统一服务
1. grpc_mock_server中的服务统一入口是grpc_mock_server/mock_server.py，迁移后需要删除掉子系统server中的启动函数，改为在mock_server中注册。
2. 启动目录为项目根目录
3. 启动命令为/home/work/.deck/1.0/python/3.7.6/bin/python3 /home/disk1/yangchenqi/baidu/nlp-qa/wxyy-mock-server/grpc_mock_server/mock_server.py

### 导入规范
```python
from grpc_src import {service}_pb2_grpc
from sub_servers.{service} import {service}_server
```

### 注册模板
```python
{service}_pb2_grpc.add_{Service}Servicer_to_server(
    {service}_server.{Service}Server(), 
    server
)
```

### 完整示例（以preprocess为例）
```python
from grpc_src import preprocess_pb2_grpc
from sub_servers.preprocess import preprocess_server

preprocess_pb2_grpc.add_MultimodalPreprocessServicer_to_server(
    preprocess_server.PreprocessServer(),
    server
)
```

## 验证清单

1. [ ] `.proto`文件已正确生成pb2文件
2. [ ] 服务类继承正确的Servicer基类
3. [ ] 所有RPC方法已实现
4. [ ] 日志系统使用`LoggerHelper`初始化
5. [ ] mock数据能正确加载
6. [ ] 服务在mock_server.py中正常注册，并能正常启动mock_server.py
7. [ ] 配置文件`config.yaml`已添加服务端口配置

## 注意事项

1. 服务名称保持snake_case（如`eb45_preprocess`），但是要去除掉'eb45_'相关特征，命名尽量简洁
2. 类名使用PascalCase（如`PreprocessServer`）
3. 确保所有RPC方法都有异常处理
4. 日志需包含请求ID（logid）
5. 性能监控数据需通过`global_monitor`上报
```
```


[AI Coding 经验总结](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/zUMY7EE3Bt/fSAtqNVA_6bto1?t=mention&mt=doc&dt=doc)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
