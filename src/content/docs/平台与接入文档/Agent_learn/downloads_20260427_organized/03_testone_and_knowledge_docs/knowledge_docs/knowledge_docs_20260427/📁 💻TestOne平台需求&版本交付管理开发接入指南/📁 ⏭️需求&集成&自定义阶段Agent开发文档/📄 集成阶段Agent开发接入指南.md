---
title: "1、升级依赖环境"
description: "集成阶段Agent开发接入指南"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档\\📄 集成阶段Agent开发接入指南.md"
---
集成阶段Agent开发接入指南

如按照文档操作依旧遇到问题，可联系[@楼瀚琼](https://ku.baidu-int.com?t=mention&mt=contact&id=e21fef70-392d-11ef-9d94-cb510e86cf15)[@顾友达](https://ku.baidu-int.com?t=mention&mt=contact&id=e6101560-392d-11ef-9d94-cb510e86cf15)协助解决

# 1、升级依赖环境
> 以下几个依赖包大于等于给定的版本均可
修改：requirements.txt，升级版本号，[SDK版本升级指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/tuuZlyo_neWnQq?source=137?t=mention&mt=doc&dt=doc)



# 2、更新本地依赖包
```
pip3 install -r requirements.txt -U --index-url http://pip.baidu.com/root/baidu/+simple/ --trusted-host pip.baidu.com  --no-cache-dir
```


# 3、修改编译打包脚本
修改：build.sh，新增qep_delivery_data 依赖的引入

```
data_sdk_version=$(cat requirements.txt | grep '^qep-delivery-data' | awk -F '^qep-delivery-data*==*' '{print $2}')
pip3 install --no-deps --target=output/agent --no-cache-dir -i http://pip.baidu-int.com/simple/ --trusted-host pip.baidu-int.com qep-delivery-data==${data_sdk_version}
```
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 4、添加集成维度各阶段Agent
参考agents目录下各代码文件，复制到agents目录下，具体业务逻辑后续自行升级：[评审：megqaend-14690【智能交付】集成Agent开源代码编写](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/reviews/112862324/files/base...latest/agent/agents/integration_core_case_test_stage_agent.py?t=mention&mt=doc&dt=sdk)

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 5、修改Agent注册调度代码
修改：main.py  新增集成各阶段Agent的注册，参考：[评审：megqaend-14690【智能交付】集成Agent开源代码编写](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/reviews/112862324/files/base...latest/agent/main.py?t=mention&mt=doc&dt=sdk)

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 6、执行单测用例，确保上述过程被正确执行
方式1：IDE里直接运行

![](/personal-site-mvp/img/doc-placeholder.svg "")


方式2：命令行

```
cd tests
python3 run_all_case.py
```


# 7、自行完善业务逻辑



