---
title: "使用coze扣子平台（字节）创建agent服务"
description: "给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。示例 1：输入: “babad”输出: “bab”注意: “aba” 也是一个有效答案。示例 2：输入: “cbbd”输出: “bb”分析：至少需要3个"
date: "2026-04-28"
category: "Agent与RAG"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\使用coze扣子平台（字节）创建agent服务\\使用coze扣子平台（字节）创建agent服务.md"
---
# 使用coze扣子平台（字节）创建agent服务
coze平台：https://www.coze.cn/home一、场景任务背景：根据需求编写代码，执行代码，并根据执行的报错信息修复代码，得到最终符合需求的代码实现。

举个例子：

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。示例 1：输入: “babad”输出: “bab”注意: “aba” 也是一个有效答案。示例 2：输入: “cbbd”输出: “bb”分析：至少需要3个功能：需求生成代码、代码执行器、代码修复

二、创建需要的工作流1、主工作流leetcode：需求生成代码并执行![](/personal-site-mvp/img/doc-placeholder.svg)

工作流由5部分组成：

开始：输入为编程题目大模型：由需求生成代码（扣子除了文心，其他模型基本都支持，包括豆包、glm4、千问max、百川4、minimax6.5、月之暗面）代码：提取代码部分（支持js、python）coderunner：执行提取的代码结束：返回代码、报错信息、执行结果每一步都有中间结果，debug很方便

当前主流成缺乏代码修复能力，下一步创建修复代码工作流。

2、子工作流codefix：代码修复![](/personal-site-mvp/img/doc-placeholder.svg)

工作流由5部分组成：

开始：输入为编程题目、代码、代码出错信息大模型：给出修复后的代码（扣子除了文心，其他模型基本都支持，包括豆包、glm4、千问max、百川4、minimax6.5、月之暗面）代码：提取代码部分（支持js、python）coderunner：执行提取的代码结束：返回修复代码、报错信息、执行结果每一步都有中间结果，debug很方便

3、最终实现完整流程将子流程codefix应用于主流程leetcode：

应用![](/personal-site-mvp/img/doc-placeholder.svg)

三、发布后实验效果1、发布![](/personal-site-mvp/img/doc-placeholder.svg)

2、使用页面使用![](/personal-site-mvp/img/doc-placeholder.svg)

sdk使用curl --location --request POST 'https://api.coze.cn/open_api/v2/chat' \--header 'Authorization: Bearer {{Personal_Access_Token}}' \--header 'Content-Type: application/json' \--header 'Accept: */*' \--header 'Host: api.coze.cn' \--header 'Connection: keep-alive' \--data-raw '{    "conversation_id": "123",    "bot_id": "{{Bot_Id}}",    "user": "CustomizedString123",    "query": "{{yourquery}}",    "stream":false}'{{Personal_Access_Token}}：生成的个人访问令牌。{{Bot_Id}}：Bot ID。![](/personal-site-mvp/img/doc-placeholder.svg)

3、效果| 困难程度 | 题目 | 模型输出 | 结果 |
| --- | --- | --- | --- |
| 简单 | 给定一个整数数组nums 和一个整数目标值target，请你在该数组中找出和为目标值target  的那 两个 整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。示例 1：输入：nums = [2,7,11,15], target = 9输出：[0,1]解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。示例 2：输入：nums = [3,2,4], target = 6输出：[1,2]示例 3：输入：nums = [3,3], target = 6输出：[0,1] | 以下是使用 Python 解决此问题的代码：def two_sum(nums, target):    for i in range(len(nums)):        for j in range(i + 1, len(nums)):            if nums[i] + nums[j] == target:                return [i, j]# 测试代码nums = [2, 7, 11, 15]target = 9print(two_sum(nums, target))  # 输出: [0, 1]nums = [3, 2, 4]target = 6print(two_sum(nums, target))  # 输出: [1, 2]nums = [3, 3]target = 6print(two_sum(nums, target))  # 输出: [0, 1]这段代码定义了一个名为two_sum的函数，它接受一个整数数组nums和一个整数目标值target作为参数。函数通过两个嵌套的循环遍历数组中的每个元素，找到两个元素的和等于目标值的情况，并返回它们的下标。在测试代码中，我们定义了三个不同的数组和目标值，并调用two_sum函数来查找和为目标值的两个元素的下标。 | 提交通过 |
| 中等 | 给你一个无重叠的，按照区间起始端点排序的区间列表intervals，其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。在 intervals中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。返回插入之后的 intervals。注意你不需要原地修改 intervals。你可以创建一个新数组然后返回它。示例 1：输入：intervals = [[1,3],[6,9]], newInterval = [2,5]输出：[[1,5],[6,9]]示例 2：输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]输出：[[1,2],[3,10],[12,16]]解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。 | 以下是使用 Python 解决此问题的代码：def insert_interval(intervals, newInterval):    result = []    placed = False    for interval in intervals:        # 如果新区间在当前区间的右侧且没有重叠，直接添加当前区间        if interval[1] < newInterval[0]:            result.append(interval)        # 如果新区间在当前区间的左侧且没有重叠，添加新区间然后退出循环        elif interval[0] > newInterval[1]:            if not placed:                result.append(newInterval)                placed = True            result.append(interval)        # 如果有重叠，则合并区间        else:            newInterval[0] = min(newInterval[0], interval[0])            newInterval[1] = max(newInterval[1], interval[1])    # 如果新区间没有放置，添加到结果列表的末尾    if not placed:        result.append(newInterval)    return result# 下面是单元测试用例def test_insert_interval():    assert insert_interval([], [1, 3]) == [[1, 3]]    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]    assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9]) == [[1, 2], [3, 10], [12, 16]]    assert insert_interval([[1, 3], [6, 9]], [4, 5]) == [[1, 3], [4, 5], [6, 9]]    assert insert_interval([[1, 3], [6, 9]], [10, 11]) == [[1, 3], [6, 9], [10, 11]]    print("All tests passed!")# 运行单元测试test_insert_interval()这段代码定义了一个名为insert_interval的函数，它接受两个参数：一个区间列表intervals和一个新区间newInterval。函数的目的是在 | 提交通过 |
| 困难 | 给定两个大小分别为m和n的正序（从小到大）数组 nums1和 nums2。请你找出并返回这两个正序数组的中位数。算法的时间复杂度应该为O(log (m+n))。示例 1：输入：nums1 = [1,3], nums2 = [2]输出：2.00000解释：合并数组 = [1,2,3] ，中位数 2示例 2：输入：nums1 = [1,2], nums2 = [3,4]输出：2.50000解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5 | 以下是使用 Python 解决此问题的代码：def findMedianSortedArrays(nums1, nums2):    # 保证 nums1 是较短的数组    if len(nums1) > len(nums2):        nums1, nums2 = nums2, nums1    m, n = len(nums1), len(nums2)    imin, imax, half_len = 0, m, (m + n + 1) // 2    while imin <= imax:        i = (imin + imax) // 2        j = half_len - i        if i < m and nums2[j-1] > nums1[i]:            imin = i + 1  # i 偏小了，需要增加        elif i > 0 and nums1[i-1] > nums2[j]:            imax = i - 1  # i 偏大了，需要减小        else:            # 找到了合适的 i 和 j            if i == 0:                max_of_left = nums2[j-1]            elif j == 0:                max_of_left = nums1[i-1]            else:                max_of_left = max(nums1[i-1], nums2[j-1])            if (m + n) % 2 == 1:                return max_of_left            if i == m:                min_of_right = nums2[j]            elif j == n:                min_of_right = nums1[i]            else:                min_of_right = min(nums1[i], nums2[j])            return (max_of_left + min_of_right) / 2.0# 下面是单元测试用例def test_findMedianSortedArrays():    assert findMedianSortedArrays([1, 3], [2]) == 2    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5    assert findMedianSortedArrays([0, 0], [0, 0]) == 0    assert findMedianSortedArrays([], [1]) == 1    assert findMedianSortedArrays([], [2, 3]) == 2.5    print("All tests | 提交通过太长了没输出完，生成的函数部分提交通过了 |



