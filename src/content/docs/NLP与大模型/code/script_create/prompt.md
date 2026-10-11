---
title: "prompt"
description: "使用下面的接口批量化的将func.md 的所有扩展函数都上传到测试"
date: "2026-10-11"
category: "NLP与大模型"
source: "F:\\百度工作\\01_code\\code\\script_create\\prompt.md"
---
使用下面的接口批量化的将func.md 的所有扩展函数都上传到测试

###
测试接口
curl --location 'https://apismart-test.now.baidu-int.com/core/script/create' \
--header 'QAMate-Token: super-9a796933bf024ebfa0420dce6f864a51' \
--header 'QAMate-Moduleld: 0' \
--header 'Content-Type: application/json' \
--data '{
   "moduleId": 6,       
   "scriptName": "test1",      
   "remark": "",                
   "language": "python",        
   "scriptCode": "print(\"hello\")",      
   "updateUser": "",       
   "scriptType":2, 
   "visible":1 ,
   "params":[
           {
               "name":"test",
               "description":"这是一个测试入参",
               "demo": "test"
           }
       ],
       "resKey":"testRes",
       "timeout":60 
}'
###

## 要求：
1. scirptname 按照1.1时间相关函数time,1.2时间函数timestamp 进行相对应的修改
2. 脚本描述放在remark中，例如下面的例子
```
函数名称： 获取指定格式的时间
函数介绍： 根据指定的日期格式和时间偏移量，返回格式化的时间字符串。支持年、月、日、时、分、秒等多种时间单位的偏移计算。
参数说明：
* format_str：日期格式，如 yyyy-MM-dd HH:mm:ss
* shifting：时间偏移量，如 -1d（昨天），+1y（明年），可选参数
```
3. params 中需要将函数的入参输入，如果有多个入参，写多个字典放在列表中