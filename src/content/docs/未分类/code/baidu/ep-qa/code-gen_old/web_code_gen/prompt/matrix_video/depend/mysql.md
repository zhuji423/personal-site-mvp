---
title: "mysql"
description: "import \"context\" \"time\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\mysql.md"
---
### dao层封装mysql底层数据库操作，文件路径：`model/dao/test_table.go`
* 直接调用基类数据库已封装好的公共方法（如：SelectConvert）进行操作，其他未封装的逻辑则采用mysql原生库操作
* 关联`UID`、`uid`、`CUID`等ID/id类关键词在结构体名、方法名、变量名等中必须大写，示例：表名为`test_uid`，则对应结构体为`type TestUID struct {}`
```go
package dao

import (
	"context"
	"time"

	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/consts"

	"icode.baidu.com/baidu/gdp/logit"

	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/resource"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/store/mysql"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/library/util"
)

// 注意：关联`UID`、`uid`、`CUID`等ID/id类关键词在结构体名、方法名、变量名等中必须大写

// TestDBDao，示例：
type TestDBDao struct {
	Ctx           context.Context
	TestProductID int  // 测试产品线ID，参数示例，实际根据需求命名
	*mysql.IDB
}

// TestDB表结构，示例：
type TestDBRecord struct {
	TestID             uint64 `ddb:"test_id" json:"test_id"`                   // 测试id
	TestProductId      uint64 `ddb:"test_product_id" json:"test_product_id"`   // 测试产品线id
}

// TestDB表名，示例：
const TestDBTableName = "test_db_name"

// TestDB表默认select字段，示例：
var TestDBDefaultFields = []string{
    "test_id",
    "test_product_id",
}

func NewTestDBDao(ctx context.Context) *TestDBDao {
	return &TestDBDao{
		Ctx: ctx,
		IDB: mysql.InitIDB(ctx, resource.MySQLClient, TestDBTableName),
	}
}

// 数据库操作方法TestGetGetUIDRecord，示例如下：
func (tdd *TestDBDao) TestGetGetUIDRecord(testId int64) (*TestDBDao, error) {
    where := map[string]interface{}{
        "test_id":         testId,
		"test_product_id": money.TestProductID,
	}
	var res *TestDBRecord
	// 注意：此处为调用基类封装好的SelectConvert公共方法，此方法无需实现
	err := tdd.SelectConvert(where, TestDBDefaultFields, &res)
	if res == nil {
		return nil, nil
	}
	return res, err
}
```
* 封装好的mysql数据库基类公共方法使用参考（以下函数直接调用即可，无需生成）
```go
func (i *IDB) SelectConvert(where map[string]interface{}, fields []string, target interface{}) error  // 查询输出结构体 
func (i *IDB) Tx() (tx mysql.Tx, err error)  // 开启事务
func (i *IDB) Select(where map[string]interface{}, fields []string) (mysql.Rows, error)  // 查询数据
func (i *IDB) InsertStruct(raws interface{}) (affected int64, lastInsertID int64, err error)  // 封装NewInsertBuilder
func (i *IDB) InsertIgnoreStruct(raws interface{}) (affected int64, lastInsertID int64, err error)  //封装NewIgnoreInsertBuilder
func (i *IDB) Insert(raws map[string]interface{}) (affected int64, lastInsertID int64, err error)  // 封装NewInsertBuilder
func (i *IDB) Update(where map[string]interface{}, assigns map[string]interface{}) (sql.Result, error)
func (i *IDB) Delete(where map[string]interface{}) (int64, error) 
func (i *IDB) Query(sql string, data map[string]interface{}, target interface{}) error
func (i *IDB) Count(where map[string]interface{}) (int, error)
```