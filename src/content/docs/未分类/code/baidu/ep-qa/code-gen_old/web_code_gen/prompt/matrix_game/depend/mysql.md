---
title: "mysql"
description: "// 分表配置 var // 线上分表配置 tableNumRelease = mapstringint64{ TestTable: 1, }"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_game\\depend\\mysql.md"
---
#### db数据库底层操作
##### 表名和分表的配置代码，文件路径：`model/consts/db/模块包占位/base.go`
```go
// 表名配置
const (
    TestTable = "test_table"  // 测试表
)

// 分表配置
var (
    // 线上分表配置
    tableNumRelease = map[string]int64{
        TestTable: 1,
    }
    
    // 测试分表配置
    tableNumDebug = map[string]int64{
        TestTable: 1,
    }
)
```
##### 数据库底层操作逻辑代码，文件路径：`model/dao/db/模块包占位/包名_test_table.go
```go
package db

import (
    "context"
    "time"

	"gorm.io/gorm"
    
    "icode.baidu.com/baidu/searchbox/ug-game/library/constant"
	"icode.baidu.com/baidu/searchbox/ug-game/library/errno"
	"icode.baidu.com/baidu/searchbox/ug-game/library/logger"
	"icode.baidu.com/baidu/searchbox/ug-game/library/resource"
	"icode.baidu.com/baidu/searchbox/ug-game/library/utils"
	
	"icode.baidu.com/baidu/searchbox/ug-game/model/consts"
	srvConsts "icode.baidu.com/baidu/searchbox/ug-game/model/consts/srv/模块包占位"
	
	typesTest "icode.baidu.com/baidu/searchbox/ug-game/model/types/模块包占位/游戏模块名/接口路径占位"
)

// 注意：db数据库表结构定义在此文件即可，不要定义在其他文件中
// TestTable ...
type TestTable struct {
	TestID              int64     `gorm:"column:test_id"`                         // ID
	TestName            string    `gorm:"column:test_name"`                       // 名称
}

// TestTableList 数组
type TestTableList []*TestTable

// TableName 表名
func (t *TestTable) TableName() string {
	return TestTableName
}

// db连接
func (t *TestTable) getDB(ctx context.Context) *gorm.DB {
	return resource.UGGameCenterDB.WithContext(ctx).Table(t.TableName())
}

// db数据库操作，示例如下：
// TestDBFunc ...
func (t *TestTable) TestDBFunc(ctx context.Context, testId int64) (*typesTest.TestDBData, error) {
    testDBData := &typesTest.TestDBData{}
    err := t.getDB(ctx).
        Where("test_id = ?, test_name = ?", testId, srvConsts.TestName).
        Take(testDBData).
        Error
    if err != nil && !errors.Is(err, gorm.ErrRecordNotFound) {
		   logger.ErrWF(ctx, errno.DBExecuteError, "xxx from db error: %v", err)
		   return nil, err
	   }
    return testDBData, err
}
```