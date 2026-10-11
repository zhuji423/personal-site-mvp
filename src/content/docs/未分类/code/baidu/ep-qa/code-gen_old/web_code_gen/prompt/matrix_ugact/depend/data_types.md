---
title: "data_types"
description: "// TestTaskData ... type TestTaskData struct { TestTaskName string json:\"testTaskName\" gorm:\"column:testTaskName\" // 测试任"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\data_types.md"
---
#### data层涉及到的结构体、常量、数据库表定义文件，文件路径：`service/包名/data/功能名/types.go`
* 注意常量、结构体等生成时需要生成对应注释
```go
package 功能名

// TestTaskData ...
type TestTaskData struct {
    TestTaskName string `json:"testTaskName" gorm:"column:testTaskName"` // 测试任务名称
}

// TestSqlData ...
type  struct {
    TestSqlID string `json:"testSqlId" gorm:"column:testSqlId"`  // 测试sqlId
}

// TestTable ...
type TestTable struct {
	NID      string `json:"nid" gorm:"column:nid"`             // 短剧子集ID
	Reason   string `json:"reason" gorm:"column:reason"`       // 类型原因 xukan:续看 gengxin:更新
}

// TableName ...
func (TestTable) TableName() string {
	return "test_table"
}

// TestRedisData ...
type TestRedisData struct {
    TestRedisID string `json:"testRedisId" gorm:"column:testRedisId"`  // 测试redisId
}

// TestFmtHttpData ...
type TestFmtHttpData struct {
    TestRalID string `json:"testRalId" form:"testRalId"`  // 测试ralId
}
```