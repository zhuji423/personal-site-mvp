---
title: "pWuV"
description: "使用下面的接口批量化的将func.md 的所有扩展函数都上传到测试curl --location 'https://apismart-test.now.baidu-int.com/core/script/create' \\ --header"
date: "2026-01-08"
category: "未分类"
source: "F:\\百度工作\\06_comate_aiide_config\\User\\History\\5ed79e83\\pWuV.md"
---
使用下面的接口批量化的将func.md 的所有扩展函数都上传到测试curl --location 'https://apismart-test.now.baidu-int.com/core/script/create' \
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