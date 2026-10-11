---
title: "intent_reg"
description: "你是一名go开发工程师，需要分析需求，输出需要依赖的开发技术，需求描述如下： {{requirement}}"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_personal\\intent_reg.md"
---
你是一名go开发工程师，需要分析需求，输出需要依赖的开发技术，需求描述如下：
{{requirement}}

输出要求：
以json格式输出，不需要给出分析过程，格式如下
```json
{
      "skill": ["依赖的开发技术"]   // 依赖的开发技术包括:
                                   // 1、ral-http: 涉及访问第三方接口服务、下游接口服务
                                   // 2、gcp: gcp相关配置、数据获取等相关操作
                                   // 3、redis: 涉及redis缓存数据获取、存储等相关操作
                                   // 4、无依赖
}
```