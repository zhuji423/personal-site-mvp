---
title: "案例"
description: "Claude自动记忆"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\如流&ducc&skills&沙箱开发接入指南\\怎么管理记忆\\Claude自动记忆.md"
---
Claude自动记忆

# 案例
在日常任务中，关键经验AI记下来

[附件]


![总结的经验](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2b22569399a642b0a823d2c59b58d187&docGuid=jEqBeO1L5FNDbH "总结的经验")


清空本次会话，启动一个全新的任务，看看是否生效

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=02e44e8239524297bd3ce6fc83a4a9b3&docGuid=jEqBeO1L5FNDbH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=457eb08a2fab4ee6a630894e4db3701b&docGuid=jEqBeO1L5FNDbH "")
# 方案
Claude提供的系统自带的项目级别的跨会话自动总结记忆, [详见官方文档](https://code.claude.com/docs/zh-CN/memory)

* 开启方式

```
{
  "autoMemoryEnabled": true,
  "autoMemoryDirectory": "<YOUR_CUSTOM_MEMORY_DIR>"
}
```


* 存储位置 ${HOME}/.claude/projects/xxxxx/memory 也可以自己指定目录，建议自己指定目录，方便多项目共享

> 特别注意，如果自己指定目录， 不能配置在工作空间的 .claude/sesstings.json ，可以配置在 .claude/sesstings.local.json  [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f1c3c350072e4fc39cacbef9688e9bbf&docGuid=jEqBeO1L5FNDbH "")


* memory/MEMORY.md存储了记忆的关键信息索引  每一条记忆的详细数据存储在其他文件，方便需要的时候按需加载

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a7f275b0e1954395887725bffd450f09&docGuid=jEqBeO1L5FNDbH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=953f702845df463ca183adf3db9e9220&docGuid=jEqBeO1L5FNDbH "")


补充方案，详见 [文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/ai-agent/resources/settings.json?t=mention&mt=doc&dt=sdk)

> 此处仅提供思路&方案采参考，大家也可以基于Tool基于SKILL实现，也可以选择记忆内容存在数据库，API读写，方便集中管理
* CLAUDE.md 关于记忆章节
* resources/memory目录



# 原理
claude在每次请求模型前，会自动加载 记忆目录下的MEMORY.md的前200行或者25KB数据。追加在CLAUDE.md后面

> 所以不建议MEMORY.md写的太长，保留核心信息即可，每条记忆的详细内容使用独立的文档存储，命中对应记忆的时候会自动去加载详细信息
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4725e240910c4f04be59e1514dbb62ff&docGuid=jEqBeO1L5FNDbH "")
# 例子
请求的时候自动加载MEMORY.md

![官方说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aee4959d363544689b177013ec8cc1cd&docGuid=jEqBeO1L5FNDbH "官方说明")


后续按需加载记忆里面链接的详细记忆信息

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3058512b436c462fac5541c75abbdf57&docGuid=jEqBeO1L5FNDbH "")
