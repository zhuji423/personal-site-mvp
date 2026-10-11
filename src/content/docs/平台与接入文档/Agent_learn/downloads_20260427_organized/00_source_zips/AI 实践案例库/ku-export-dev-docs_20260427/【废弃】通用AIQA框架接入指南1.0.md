---
title: "定义项目目录变量"
description: "【废弃】通用AIQA框架接入指南1.0"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-dev-docs_20260427\\【废弃】通用AIQA框架接入指南1.0.md"
---
【废弃】通用AIQA框架接入指南1.0

请参考最新方案：

* [🤖AI-Agent开发指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/eA4VS0xNyhsBRu?source=137?t=mention&mt=doc&dt=doc)
* [🚀QuickStart：30分钟快速看见效果](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/rKjIOhc7cB82Rv?source=137?t=mention&mt=doc&dt=doc)



---

以下内容已废弃，请勿参考

---

## 代码下载
代码库地址：[文件页：baidu/ep-qa/testone-llm  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/testone-llm/tree/master?t=mention&mt=doc&dt=sdk)



下载完成后进入项目目录，以 agno_aiqa_demo 为模板，复制这个demo项目，作为自己的项目

```
cp -r agno_aiqa_demo digital_agent
```
这里是创建了一个digital_aiqa项目，后续在 digital_agent 目录下开发自己的Agent即可





## 环境配置








python环境安装

麒麟的环境是3.11，这里最好和他对齐，使用python3.11+版本也可以

> 如果是icoding，请看[iCoding PyCharm Python3.11开发环境搭建](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/UaF7Alnr5tTh2Q?t=mention&mt=doc&dt=doc)


进入项目目录

cd digital_agent  



使用 venv 创建虚拟环境，方便管理

python3.11 -m venv myenv



激活环境（mac os）

source myenv/bin/activate



验证环境

python --version



输出3.11就可以了





安装依赖

直接运行脚本即可，所有的外部依赖会下载到本地src/libs目录下

由于麒麟环境与许多插件库有冲突，因此需要采用这种 外部依赖 下载到本地的方式进行引用

sh build.sh    





安装完成后，在目录下把.env里的大模型sk配置下，这里以deepseek官网的api为例

export DEEPSEEK_API_KEY=sk-1388c

配置完成后，把文件改名为.env



如果是千帆平台的模型，则需要配置千帆平台的KEY

千帆平台key的获取，可以参考下面的文档

[https://cloud.baidu.com/doc/WENXINWORKSHOP/s/wm9cvs292](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/wm9cvs292)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9fa482986aa448e9b644c84bbeee8205&docGuid=hSxm6qPSyIBIU7 "")
创建完成后，在代码中，把模型替换为如下形式

```
from agno.models.openai.like import OpenAILike
from os import getenv

agent = Agent(
    model=OpenAILike(
        id="deepseek-v3.1-250821", # 模型名称可以参考千帆支持的模型名称
        api_key=getenv("QIANFAN_DEEPSEEK_API_KEY"),
        base_url="https://qianfan.baidubce.com/v2",
    ),
    instructions=dedent("""\

    """),
    markdown=True)
```
并在.env文件中添加

```
export QIANFAN_DEEPSEEK_API_KEY=bce-v3/ALxxxxxxx
```




安装完成后可以尝试运行一下

用刚刚创建的虚拟环境去运行, vscode的话，就是shift + alt + p ，输入 Select Interpreter，选择对应的环境



运行 src/basic_agent.py 如果能成功运行，说明框架依赖正常

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e877ea5649384e1da947a5fd80db0205&docGuid=hSxm6qPSyIBIU7 "")






## 开发
开发常用的API已经在demo里有体现，如果想看更多使用方法，可以参考[https://docs.agno.com/introduction](https://docs.agno.com/introduction)，这里已经支持这个框架的调用。



Agent的代码都在src目录下，src结构如下

```
├── agents // 存放自己编写的agent
├── aiqa
├── app
├── basic_agent.py // 演示agno功能用，验证功能用
├── common // 存放一些公共工具，以及一些常量、配置信息
├── infoflow_cards
├── libs // 安装依赖后会产生这个文件夹，存放的各类依赖，会打包到麒麟上运行
├── main.py // aiqa入口文件
└── tools // 自定义的工具类，可以是本地工具，也可以是一些接口调用
```


可以参考 src/agents/testone_mcp_agent.py 的Agent实现，只需创建一个自定义的Agent即可

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f00bcb3646cb4f3abd3b2a601a682674&docGuid=hSxm6qPSyIBIU7 "")
然后在 src/agents/aiqa_common_agent.py 里引入即可

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c0ab5b8acd034c459979241cb96fb186&docGuid=hSxm6qPSyIBIU7 "")


## 调试验证
编写Agent时，想调试的话，可以在 src/common/constants.py 中更改环境为RUN_MODE = 'OFFLINE'。

并main.py里修改调试参数，运行main.py 在控制台查看输出。

```

def get_debug_parameters():
    """
    获取调试环境使用的预设参数
    
    Returns:
        tuple: 包含三个元素的元组:
            - str: JSON格式的任务参数字符串，包含requestType、aiqaId等字段
            - int: 麒麟任务ID
            - str: 回调URL(调试模式下为空字符串)

            这里可以问：
                1、帮我查询1003产品线安卓端15.21.0.2版本的任务信息（会调起自己写的tool）
                2、查询卡片megqaend-19625信息（会调起MCP工具）
            
    Note:
        该函数仅在RUN_MODE为'OFFLINE'时调用，用于本地开发和测试
    """
    return (
        '''
        {
            "requestType": "CALL_AIQA_AGENT",
            "testoneBaseUrl": "http://testone-test.bcc-szzj.baidu.com",
            "aiqaId": 9,
            "aiqaName": "众测",
            "recordId": 3114,
            "deptId": 26674,
            "subDirection": "众测",
            "taskType": 0,
            "taskIndex": "cwtest-1",
            "operator": "chenwei57",
            "taskId": "main_b285e54f-5a60-417b-bb50-fce8e9ed4651",
            "parentTaskId": null,
            "operateType": 1,
            "debug": false,
            "detail": {
                "description": "查询卡片megqaend-19625信息"
            }
        }
        ''',
        7584048753,
        ''
    )
```
用户query是从 

            "detail": {

                "description": "查询卡片megqaend-19625信息"

            }

里获取。





## 打包上线
### MacOS
提交代码，会触发流水线打包，安装麒麟环境的一些依赖，替换本地的libs依赖（mac的libs有些库在麒麟上无法用）



需要创建一条自己业务的流水线，并配置对应的ci.yml文件

样例如下

```
  - profile:
    name: agno_aiqa_demo
    mode: AGENT
    environment:
      image: DECK_STD_CENTOS7
      tools:
        - python: 3.11.2
    build:
      command: sh build_kirin_aiqa.sh
    artifacts:
      release: true
```
修改name为自己的目录

    name: digital_agent



这里在打包的时候会执行 sh build_kirin_aiqa.sh，需要创建自己的 build_kirin_aiqa.sh 并修改

```
#!/bin/bash

# 定义项目目录变量
PROJECT_DIR="agno_aiqa_demo"

cd "$PROJECT_DIR/" || {
    echo "Error: Directory $PROJECT_DIR not found"
    exit 1
}

pip install --upgrade pip

# 使用指定pip源安装依赖
pip3 install -r requirements.txt \
    --target=src/libs \
    --no-deps \
    --index-url http://pip.baidu.com/root/baidu/+simple/ \
    --trusted-host pip.baidu.com || {
    echo "Error: Dependency installation failed"
    exit 1
}

echo "All dependencies installed successfully in libs directory"
echo "Used pip source: http://pip.baidu.com/root/baidu/+simple/"

cd "$BUILD_REPO_WS" || {
    echo "Error: Failed to change to BUILD_REPO_WS: $BUILD_REPO_WS"
    exit 1
}

# 创建 output 文件夹
mkdir -p output

# 复制项目目录到 output
cp -r "$PROJECT_DIR" output/

echo "Project $PROJECT_DIR copied to output/"
```


主要是修改目录，PROJECT_DIR="agno_aiqa_demo"，这里我改为PROJECT_DIR="digital_agent"



并在编译流水线里，配置指定这个name编译

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=663a7b9111ca435598af9c4b788a4876&docGuid=hSxm6qPSyIBIU7 "")




编译完成后，下载这个包，本地解压后，会得到一个output文件夹，里面是项目和麒麟环境的编译结果。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=52466f90c6424df89c7e359c1f16cae7&docGuid=hSxm6qPSyIBIU7 "")
可以自己本地重新打包这个项目，并上传到麒麟上，配置执行的入口src/main.py



麒麟调试参数样例如下

```
{"requestType":"CALL_AIQA_AGENT","testoneBaseUrl":"http://testone-test.bcc-szzj.baidu.com","aiqaId":9,"aiqaName":"众测","recordId":3114,"deptId":26674,"subDirection":"众测","taskType":0,"taskIndex":"cwtest-1","operator":"chenwei57","taskId":"main_b285e54f-5a60-417b-bb50-fce8e9ed4651","parentTaskId":null,"operateType":1,"debug":false,"detail":{"description":"帮我查询1003产品线安卓端15.21.0.2版本的任务信息，并总结反馈"}}
```


如果能正常执行，则说明成功了，然后联系chenwei57、guyouda注册一个aiqa，配置麒麟地址即可。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5c987c5a68934356bb4296127fb9a03b&docGuid=hSxm6qPSyIBIU7 "")




### icoding
> 如果是icoding环境安装，请看[iCoding PyCharm Python3.11开发环境搭建](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/UaF7Alnr5tTh2Q?t=mention&mt=doc&dt=doc)
如果是icoding （linux系统）

直接打包整个项目文件夹即可

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d0d9f9a0ce994274889d285de9034e14&docGuid=hSxm6qPSyIBIU7 "")


```
zip -r kirin.zip agno_aiqa_demo          
```




上传到麒麟上，配置执行的命令

python3.11 agno_aiqa_demo/src/main.py

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e1eee45f7c8343dda1a8cd00c87302af&docGuid=hSxm6qPSyIBIU7 "")


麒麟调试参数样例如下

```
{"requestType":"CALL_AIQA_AGENT","testoneBaseUrl":"http://testone-test.bcc-szzj.baidu.com","aiqaId":9,"aiqaName":"众测","recordId":3114,"deptId":26674,"subDirection":"众测","taskType":0,"taskIndex":"cwtest-1","operator":"chenwei57","taskId":"main_b285e54f-5a60-417b-bb50-fce8e9ed4651","parentTaskId":null,"operateType":1,"debug":false,"detail":{"description":"帮我查询1003产品线安卓端15.21.0.2版本的任务信息，并总结反馈"}}
```


如果能正常执行，则说明成功了，然后联系chenwei57、guyouda注册一个aiqa，配置麒麟地址即可。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5c987c5a68934356bb4296127fb9a03b&docGuid=hSxm6qPSyIBIU7 "")







