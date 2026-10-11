---
title: "1、获取iCafe卡片详细信息"
description: "password: 浏览器打开 https://console.cloud.baidu-int.com/api/icafe/users/virtualhttps://console.cloud.baidu-int.com/api/icafe"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🛠️TestOne-SDK\\📁 📦qep-delivery-data\\📄 ICafe相关.md"
---
ICafe相关

iCafe：

* password: 浏览器打开 [https://console.cloud.baidu-int.com/api/icafe/users/virtual](https://console.cloud.baidu-int.com/api/icafe/users/virtual) 获取
* username: 自己的邮箱前缀

# 1、获取iCafe卡片详细信息
功能：

获取单张iCafe卡片详细信息

版本：

>=0.0.1

需要权限：

是

输入：

Icafe空间，卡片序号

输出：

卡片所有字段详细信息  数据定义详见 qep_delivery_data.ICafeCardInfo

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    card_info = utils.get_icafe_info("routine00", 16536)
    print(card_info)


if __name__ == '__main__':
    sample()

```
# 2、批量获取iCafe卡片详细信息
功能：

批量获取iCafe卡片详细信息

版本：

>=0.0.1

需要权限：

是

输入：

Icafe空间，卡片序号列表

输出：

卡片所有字段详细信息  数据定义详见 qep_delivery_data.ICafeCardInfo

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    result = utils.batch_get_icafe_info("routine00", [16536, 16537, 16538])
    for card_info in result:
        print(card_info)


if __name__ == '__main__':
    sample()
```


# 3、根据iCafe表达式获取符合要求的卡片信息
功能：

根据iCafe表达式获取符合要求的卡片信息

版本：

>=0.0.1

需要权限：

是

输入：

Icafe空间，查询表达式

输出：

卡片所有字段详细信息 数据定义详见 qep_delivery_data.ICafeCardInfo

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    cards = utils.get_icafe_cards_with_iql("routine00", "类型=Story AND 创建时间 = before-7-days")
    for card in cards:
        print(card)


if __name__ == '__main__':
    sample()
```
# 4、获取卡片的代码研发数据链信息
功能：

获取卡片的代码研发数据链信息

版本：

>=0.0.3

需要权限：

是

输入：

卡片ID

输出：

卡片研发数据链信息，数据定义详见 qep_delivery_data.ICafeCodeDevInfo

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    
    # 单张卡片
    result = utils.get_code_dev_info("routine00", 17103)  
    print(result)
    
    # 批量
    result = utils.batch_get_code_dev_info("routine00", [17103, 17104, 17105, 17106])
    print(result)


if __name__ == '__main__':
    sample()
```
# 5、创建卡片
功能：

创建卡片

版本：

>=0.0.4

需要权限：

是

输入：

字段KV

输出：

创建的卡片  例如 youtrack-1

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    result = utils.create_icafe_card(
        "youtrack", "Story",
        "测试新建卡片-{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "测试新建卡片\n{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        {
            "负责人": "guyouda"
        }
        )
    print(result)


if __name__ == '__main__':
    sample()
```
# 6、修改卡片
功能：

修改卡片

版本：

>=0.0.4

需要权限：

是

输入：

|参数|含义|类型|是否必须|示例|
|-|-|-|-|-|
|card_space|卡片空间|string|是|haokanapp-all|
|card_id|卡片ID|int|是|12345|
|field_value_dict|*需要更新的字段信息，key为字段名称，value为字段值*|Dict|是|如无字段需更新，赋值 {}|
|check_status|*是否进行流程状态可达检查*|bool|否|false|
|rel_issue_operation|*添加关联卡片或删除关联卡片，add或delete*|string|否|add|
|*rel_issue*|*关联卡片，支持批量修改，比如：rel_issue=["test-1","test-2"]*|List[str]|否|*["test-1","test-2"]*|
|*comment*|评论|string|否|添加评论|

输出：

是否修改成功

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")  # 有对应空间编辑权限的账号密码
    result = utils.update_icafe_card(
        "youtrack",   # 你要修改的卡片的空间
        465,          # 你要修改的卡片ID
        {             # 你要修改的卡片的KEY  和 VALUE
            "负责人": "guyouda",
            "标题": "测试修改卡片-{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            "内容": "测试修改卡片-{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }
    )
    print(result)


if __name__ == '__main__':
    sample()
```
# 7、评论卡片
功能：

评论卡片

版本：

>=0.0.4

需要权限：

是

输入：

卡片，评论

输出：

是否成功

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    result = utils.comment_card("youtrack", 1, "测试添加评论")
    print(result)


if __name__ == '__main__':
    sample()
```
# 8、获取评论卡片
功能：

获取评论卡片

版本：

>=0.0.4

需要权限：

是

输入：

卡片

输出：

评论列表，详见 qep_delivery_data.ICafeCardComment

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    result = utils.get_card_comments("youtrack", 1)
    for comment in result:
        print(comment.id)
        print(comment.username)
        print(comment.chineseName)
        print(comment.createTime)
        print(comment.content)


if __name__ == '__main__':
    sample()
```
# 9、获取卡片状态变化历史记录
功能：

获取卡片的状态变化历史

版本：

>=0.0.7

需要权限：

是

输入：

卡片ID

输出：

评论列表，详见 qep_delivery_data..data.icafe.ICafeCardStatusHistory

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    result = utils.get_card_status_history("youtrack", [466,467])
    for card in result:
        print(item.sequence)
        for history in item.histories:
            print(history.operator)
            print(history.operationTime)
            print(history.targetStatusId)
            print(history.targetStatusName)


if __name__ == '__main__':
    sample()
```
# 10、获取卡片字段变化历史记录
功能：

获取卡片的字段变化历史

版本：

>=0.0.7

需要权限：

是

输入：

卡片ID

输出：

评论列表，详见 qep_delivery_data..data.icafe.ICafeCardChangeRecord

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    result = utils.get_card_history("youtrack", [466,467])
    for card in result:
        print(item.sequence)
        for history in item.histories:
            print(history.operator)
            print(history.operationTime)
            print(history.operationType)
            print(history.diffDescription)


if __name__ == '__main__':
    sample()
```
# 11、获取空间类型列表
功能：

获取空间的卡片类型列表

版本：

>=0.3.3

需要权限：

是

输入：

卡片ID

输出：

类型列表，详见 qep_delivery_data..data.icafe.ICafeField

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    result = self.utils.get_fields_for_create("feed00", "Story")
    for item in result:
        print(item)


if __name__ == '__main__':
    sample()
```
# 12、获取特定类型的状态列表
功能：

获取状态列表

版本：

>=0.3.3

需要权限：

是

输入：

卡片ID

输出：

类型列表，详见 qep_delivery_data..data.icafe.ICafeIssueStatus

```

from qep_delivery_data import ICafeUtils


def sample():
    utils = ICafeUtils("ICAFE_USERNAME", "ICAFE_PASSWORD")
    result = self.utils.get_issue_status_list("feed00", "Story")
    for item in result:
        print(item)


if __name__ == '__main__':
    sample()
```
## 
