---
title: "Definition for singly-linked list."
description: "leetcode 100题汇总"
date: "2026-04-27"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\05_algorithm_backup\\ku_backup_20260427\\06_leetcode100题汇总.md"
---
leetcode 100题汇总

重点看mid难度

### 1 两数相加
[https://leetcode.cn/problems/add-two-numbers/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/add-two-numbers/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        p = dummy
        cin = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = (val1 + val2 + cin) % 10
            cin = (val1 + val2 + cin) // 10

            p.next = ListNode(val)
            p = p.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if cin:
            p.next =  ListNode(1)
        
        return dummy.next
```
### 2 最长回文子串
[https://leetcode.cn/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 遍历字符串中的每一个字符，将其作为回文中心
        # 向左右两边扩展，寻找以该字符为中心的最长回文子串
        # 考虑回文长度为奇数和偶数的两种情况

        def sub(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -=1
                r += 1 
            return s[l + 1: r]
        
        res = ''
        for i in range(len(s)):
            l1 = sub(i, i, s)
            l2 = sub(i, i + 1, s)
            res = res if len(l1) < len(res) else l1
            res = res if len(l2) < len(res) else l2
        return res

```
### 3 LRU缓存
[https://leetcode.cn/problems/lru-cache/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/lru-cache/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = {}
        self.ord = deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.data:
            return -1
        self.ord.remove(key)
        self.ord.append(key)
        return self.data.get(key)


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.data:
            self.ord.remove(key)
        else:
            if len(self.data) == self.capacity:
                del_key = self.ord.popleft()
                del self.data[del_key]

        self.ord.append(key)
        self.data[key] = value
```
### 4 三数之和
[https://leetcode.cn/problems/3sum/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/3sum/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i + 1,  len(nums) - 1
            while l < r:
                add = nums[l] + nums[r] 
                if add < target:
                    l += 1
                elif add > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 继续
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
```
### 5 岛屿数量
[https://leetcode.cn/problems/number-of-islands/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/number-of-islands/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(grid, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] != '1':
                return
            grid[i][j] = '2'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
        return res
```
### 6 [易]买卖股票的最佳时机
[https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_cur = float('inf')
        res = 0
        for p in prices:
            min_cur = min(min_cur, p)
            res = max(res, p - min_cur)
        return res
```
### 7 最长连续序列
[https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 遍历每个数 num，只从序列起点开始（也就是 num-1 不在 set）往后找连续数字
        res = 0
        dataset = set(nums)
        for i in dataset:
            if i - 1 not in dataset:
                length = 1
                while i + length in dataset:
                    length += 1
                res = max(res, length)
        return res
```
### 8 数组中第k个最大元素
[https://leetcode.cn/problems/kth-largest-element-in-an-array/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/kth-largest-element-in-an-array/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 最小堆
        data = nums[:k]
        heapq.heapify(data)
        for num in nums[k:]:
            if num > data[0]:
                heapq.heappop(data)
                heapq.heappush(data, num)
        return data[0]
```
### 9 [易]二分查找
[https://leetcode.cn/problems/binary-search/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/binary-search/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2        
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
```
### 10 螺旋矩阵
[https://leetcode.cn/problems/spiral-matrix/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/spiral-matrix/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n - 1, 0, m - 1
        i, j = 0, 0
        path = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 0右  1下  2左  3上
        pos = 0  # 0右  1下  2左  3上
        while len(res) != m * n:
            res.append(matrix[i][j])
            if pos == 0 and j == right:
                pos += 1
                up += 1
            elif pos == 1 and i == down:
                pos += 1
                right -= 1
            elif pos == 2 and j == left:
                pos += 1
                down -= 1
            elif pos == 3 and i == up:
                pos += 1
                left += 1

            pos %= 4
            i += path[pos][0]
            j += path[pos][1]
            
        return res
```
### 11 [难]滑动窗口最大值
[https://leetcode.cn/problems/sliding-window-maximum/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/sliding-window-maximum/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 单调队列
        maxq = deque()
        res = []
        for i, c in enumerate(nums):
            if i < k - 1:
                while maxq and maxq[-1] < c:
                    maxq.pop()
                maxq.append(c)
                continue

            # 入元素
            while maxq and maxq[-1] < c:
                maxq.pop()
            maxq.append(c)
            # 更新max
            max_val = maxq[0]
            res.append(max_val)
            # 出元素
            if maxq[0] == nums[i - k + 1]:
                maxq.popleft()
        return res
   
```
### 12 和为k的子数组
[https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 设 pre_sum 为从数组开头到当前位置的和
        # 如果 pre_sum - k 在前面出现过，说明从前面某个点到当前的子数组和为 k
        prefix = defaultdict(int)
        prefix[0] = 1
        pre_sum = 0
        res = 0
        for n in nums:
            pre_sum += n
            res += prefix[pre_sum - k] 
            prefix[pre_sum] += 1
        return res
```
### 13 括号生成
[https://leetcode.cn/problems/generate-parentheses/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/generate-parentheses/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def back(cur, l, r):
            if len(cur) == 2 * n:
                res.append(cur)
            if l < n:
                back(cur + '(', l + 1, r)
            if r < l:
                back(cur + ')', l, r + 1)
        back('', 0, 0)
        return res
```
### 14 编辑距离
[https://leetcode.cn/problems/edit-distance/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/edit-distance/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        # m+1 * n+1
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i  # word1 转空串
        for j in range(n + 1):
            dp[0][j] = j  # 空串转 word2
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        return dp[m][n]
```
### 15 删除有序数组中的重复项
[https://leetcode.cn/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if nums[i] != n:
                i += 1
                nums[i] = n
        return i + 1
```
### 16 [难]N皇后
[https://leetcode.cn/problems/n-queens/](https://leetcode.cn/problems/n-queens/)

```
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [-1] * n  # board[i]表示第i行皇后所在的列
        res = []
        def gen():
            return ['.' * i + 'Q' + '.' * (n - i - 1) for i in board]
                
        def is_ok(i, j):
            for x in range(i):
                # 列
                if board[x] == j:
                    return False
                # 对角线
                if abs(x - i) == abs(board[x] - j):
                    return False
            return True

        def back(i):
            if i == n:
                res.append(gen())
                return
            for j in range(n):
                if is_ok(i, j):
                    board[i] = j
                    back(i + 1)
                    board[i] = -1

        back(0)
        return res
```
### 17 [难]最长有效括号
[https://leetcode.cn/problems/longest-valid-parentheses/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/longest-valid-parentheses/description/?envType=problem-list-v2&envId=vi8yu3g)

### 18 [难]K 个一组翻转链表
[https://leetcode.cn/problems/reverse-nodes-in-k-group/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/reverse-nodes-in-k-group/?envType=problem-list-v2&envId=vi8yu3g)

### 19 打家劫舍
[https://leetcode.cn/problems/house-robber/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/house-robber/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
```
### 20 跳跃游戏
[https://leetcode.cn/problems/jump-game/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/jump-game/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # max_reach 表示当前能跳到的最远位置
        # 只要当前下标 i <= max_reach，就可以跳过去
        max_reach = 0
        for i, n in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + n)
        return True
```
### 21 找出字符串中第一个匹配项的下标
[https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=vi8yu3g)

简单：

```
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1
```
kmp：

自己写

### 22 旋转图像
[https://leetcode.cn/problems/rotate-image/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/rotate-image/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 先转置矩阵（行列互换）
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 然后反转每一行
        for row in matrix:
            row.reverse()
```
### 23 排序数组
[https://leetcode.cn/problems/sort-an-array/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/sort-an-array/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sift_down(nums, i, size):
            """下沉操作，将堆顶元素下沉到正确的位置"""
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < size and nums[largest] < nums[left]:
                largest = left
            if right < size and nums[largest] < nums[right]:
                largest = right
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                sift_down(nums, largest, size)

        # 构建最大堆
        for i in range(len(nums) // 2, -1, -1):
            sift_down(nums, i, len(nums))

        # 堆排序
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            # 堆化剩下部分
            sift_down(nums, 0, i)
        return nums
```
### 24 反转链表 II
[https://leetcode.cn/problems/reverse-linked-list-ii/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/reverse-linked-list-ii/description/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # pre_l: left 前一个节点
        # next_r: right 后一个节点

        # 寻找pre_l
        dummy = ListNode(0, head)
        pre_l = dummy
        for _ in range(left - 1):
            pre_l = pre_l.next

        # 寻找next_r，并切断right
        r = l = pre_l.next
        for _ in range(right - left):
            r = r.next
        next_r = r.next
        r.next = None

        # 反转left
        p, pre = l, None
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        
        # 拼接
        l.next = next_r
        pre_l.next = pre
        
        return dummy.next
```
### 25 最长递增子序列
[https://leetcode.cn/problems/longest-increasing-subsequence/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/longest-increasing-subsequence/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
```
### 26 加油站
[https://leetcode.cn/problems/gas-station/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/gas-station/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # tank 表示当前油箱剩下的油
        total, tank = 0, 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start if total >= 0 else -1
```
### 27 删除有序数组中的重复项 II
[https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        i = 2
        for n in nums[2:]:
            if nums[i-2] != n:
                nums[i] = n
                i += 1
        return i
```
### 28 [难]合并 K 个升序链表
[https://leetcode.cn/problems/merge-k-sorted-lists/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/merge-k-sorted-lists/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        p = dummy
        data = []
        for node in lists:
            if node:
                heapq.heappush(data, (node.val, node))
        while data:
            _, cur = heapq.heappop(data)
            p.next = ListNode(cur.val)
            p = p.next
            if cur.next:
                heapq.heappush(data, (cur.next.val, cur.next))

        return dummy.next
```
### 29 复原 IP 地址
[https://leetcode.cn/problems/restore-ip-addresses/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/restore-ip-addresses/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def back(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            # 1 2 3
            for i in range(1, 4):
                if start + i > len(s):
                    break
                seg = s[start: start + i]
                if (seg[0] == '0' and len(seg) > 1) or int(seg) > 255:
                    continue
                path.append(seg)
                back(start + i, path)
                path.pop() 
        back(0, [])
        return res
```
### 30 二叉树的最近公共祖先
[https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```
### 31 跳跃游戏 II
[https://leetcode.cn/problems/jump-game-ii/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/jump-game-ii/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # end 表示跳跃的最远边界
        res = 0
        end = 0
        max_reach = 0
        for i, n in enumerate(nums[:-1]):
            max_reach = max(max_reach, i + n)
            # 如果走到end，说明已经跳完了当前一步，必须增加跳跃次数，并更新end为能跳的最远地方
            if i == end:
                end = max_reach
                res += 1
        return res
```
### 32 排序链表
[https://leetcode.cn/problems/sort-list/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/sort-list/description/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next
```
### 33 搜索二维矩阵 II
[https://leetcode.cn/problems/search-a-2d-matrix-ii/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/search-a-2d-matrix-ii/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0  # 左下角和右上角都可以
        while row >= 0 and col < n:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False
```
### 34 两两交换链表中的节点
[https://leetcode.cn/problems/swap-nodes-in-pairs/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/swap-nodes-in-pairs/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        p = dummy

        while p.next and p.next.next:
            a = p.next
            b = a.next

            # 交换指针
            p.next, a.next, b.next = b, b.next, a

            # 向后移动 p
            p = a

        return dummy.next
```
### 35 二叉树的层序遍历
[https://leetcode.cn/problems/binary-tree-level-order-traversal/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/binary-tree-level-order-traversal/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            cur_res = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                cur_res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(cur_res)
        return res
```
### 36 下一个排列
[https://leetcode.cn/problems/next-permutation/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/next-permutation/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 找第一个下降点
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 找第一个比 nums[i] 大的数 nums[j]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 把 i+1 之后的所有数翻转
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```
### 37 从前序与中序遍历序列构造二叉树
[https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # 根 左*m 右*n
        # 左*m 根 右*n
        if not preorder:
            return None
        
        root_val = preorder[0]
        index = inorder.index(preorder[0])

        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:1+index], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
        
```
### 38 单词拆分
[https://leetcode.cn/problems/word-break/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/word-break/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空字符串可拆分

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break 
        return dp[n]
```
### 39 最大数
[https://leetcode.cn/problems/largest-number/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/largest-number/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        nums_str = [str(i) for i in nums]
        sorted_nums = sorted(nums_str, key=cmp_to_key(compare))

        # 000
        if sorted_nums[0] == '0':
            return '0'

        return ''.join(sorted_nums)
```
### 40 字符串相乘
[https://leetcode.cn/problems/multiply-strings/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/multiply-strings/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        res = [str(i) for i in res]
        res = ''.join(res).lstrip('0')
        return res or "0"
        
```
### 41 移掉 K 位数字
[https://leetcode.cn/problems/remove-k-digits/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/remove-k-digits/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for c in num:
            while k > 0 and stack and c < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(c)

        while k > 0:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0')
        return res if res else '0'
```
### 42 最接近的三数之和
[https://leetcode.cn/problems/3sum-closest/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/3sum-closest/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf')
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target 
        return res
```
### 43 最大正方形
[https://leetcode.cn/problems/maximal-square/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/maximal-square/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # dp[i][j] 表示以 (i, j) 为右下角的正方形的最大边长
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # 边界
                    else:
                        dp[i][j] = min(
                            dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                        ) + 1
                    res = max(res, dp[i][j])

        return res ** 2
```
### 44 用 Rand7() 实现 Rand10()
[https://leetcode.cn/problems/implement-rand10-using-rand7/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/implement-rand10-using-rand7/description/?envType=problem-list-v2&envId=vi8yu3g)

```
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        # 通过两次 Rand7() 得到一个更大的范围，然后取模到 [1, 10]
        while True:
            row = rand7()
            col = rand7()
            num = (row - 1) * 7 + col  # 得到均匀分布的范围 [1, 49]
            # 如果值在 [1, 40]，可以直接用 ((num - 1) % 10) + 1 映射到 [1, 10]
            # 如果不在范围内（41~49），就丢弃，重新生成
            if num <= 40:
                return (num - 1) % 10 + 1
```
### 45 除自身以外数组的乘积
[https://leetcode.cn/problems/product-of-array-except-self/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/product-of-array-except-self/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res[i] = 左边所有数的乘积 * 右边所有数的乘积
        n = len(nums)
        res = [1] * n

        # 第一次遍历：从左往右，计算左边乘积
        l = 1 
        for i in range(n):
            res[i] = l
            l *= nums[i]

        # 第二次遍历：从右往左，乘上右边乘积
        r = 1
        for i in range(n - 1, -1, -1):
            res[i] *= r
            r *= nums[i]

        return res
```
### 46 两数之和 II - 输入有序数组
[https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        l, r = 0, len(numbers) - 1
        while l < r:
            add = numbers[l] + numbers[r]
            if add > target:
                r -= 1
            elif add < target:
                l += 1
            else: 
                return [l + 1, r + 1]
        return [-1, -1]
```
### 47 有效的数独
[https://leetcode.cn/problems/valid-sudoku/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/valid-sudoku/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_ok(i, j, n):
            # 检查横竖
            for k in range(9):
                if k != j and board[i][k] == n:
                    return False    
                if k != i and board[k][j] == n:
                    return False  
            # 检查3*3
            start_i, start_j = 3 * (i // 3), 3 * (j // 3)
            for x in range(3):
                for y in range(3):
                    ni, nj = start_i + x, start_j + y
                    if  (ni, nj) != (i, j) and board[ni][nj] == n:
                        return False  
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and not is_ok(i, j, board[i][j]):
                    return False
        return True
```
### 48 矩阵置零
[https://leetcode.cn/problems/set-matrix-zeroes/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/set-matrix-zeroes/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # matrix[i][0] 标记“第 i 行需要置 0”
        # matrix[0][j] 标记“第 j 列需要置 0”
        # 最后处理第一行、第一列本身是否有 0
        m, n = len(matrix), len(matrix[0])
        row_flag = any(matrix[0][j] == 0 for j in range(n))
        col_flag = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_flag:
            for j in range(n):
                matrix[0][j] = 0
        if col_flag:
            for i in range(m):
                matrix[i][0] = 0
```
### 49 [易]同构字符串
[https://leetcode.cn/problems/isomorphic-strings/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/isomorphic-strings/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def get_index(s):
            lst = []
            info = {}
            idx = 0
            for c in s:
                if c not in info:
                    info[c] = idx
                    idx += 1
                lst.append(info[c])
            return lst

        return get_index(s) == get_index(t)
```
### 50 字母异位词分组
[https://leetcode.cn/problems/group-anagrams/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/group-anagrams/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        info = defaultdict(list)
        for s in strs:
            s_ord = ''.join(sorted(s))
            info[s_ord].append(s)
        return list(info.values())
```
### 51 搜索旋转排序数组
[https://leetcode.cn/problems/search-in-rotated-sorted-array/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/search-in-rotated-sorted-array/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # 左半部分是有序的
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 右半部分是有序的
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
```
### 52 寻找重复数
[https://leetcode.cn/problems/find-the-duplicate-number/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/find-the-duplicate-number/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 索引 i 看作链表的一个“节点”，它的 next 是 nums[i]，类似链表找环
        # node.val = i
        # node.next = nums[i]
        
        # 第一步：快慢指针找到相遇点
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # 存在环
                break

        # 第二步：重置一个指针，再次相遇即为重复数
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```
### 53 绝对差不超过限制的最长连续子数组
[https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        maxq = deque()  # 递减队列，队首是当前窗口最大值
        minq = deque()  # 递增队列，队首是当前窗口最小值
        # 滑动窗口, 只要 max_q[0] - min_q[0] > limit，就收缩左边界
        l, r = 0, 0
        res = 0
        while r < len(nums):
            # push right
            right = nums[r]
            while maxq and maxq[-1] < right:
                maxq.pop()
            maxq.append(right)

            while minq and minq[-1] > right:
                minq.pop()
            minq.append(right)

            while maxq[0] - minq[0] > limit:
                # pop left
                left = nums[l]
                if maxq[0] == left:
                    maxq.popleft()
                if minq[0] == left:
                    minq.popleft()
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        return res
```
### 54 字符串的排列
[https://leetcode.cn/problems/permutation-in-string/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/permutation-in-string/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1_dic, s2_dic = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1_dic[s1[i]] += 1
            s2_dic[s2[i]] += 1
        if s1_dic == s2_dic:
            return True

        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            left = s2[l]
            right = s2[r + 1]
            if s2_dic[left] == 1:
                del s2_dic[left]
            else:
                s2_dic[left] -= 1
            s2_dic[right] += 1

            if s1_dic == s2_dic:
                return True
                
            l += 1
            r += 1
        return False
```
### 55 全排列
[https://leetcode.cn/problems/VvJkup/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/VvJkup/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        use = [False] * (len(nums))
        def back(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return 
            for i in range(len(nums)):
                if use[i]:
                    continue
                cur.append(nums[i])
                use[i] = True
                back(cur)
                cur.pop()
                use[i] = False
        back([])
        return res
```
### 56 最大子数组和
[https://leetcode.cn/problems/maximum-subarray/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/maximum-subarray/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_sum = max_sum = nums[0]
        for i in nums[1:]:
            c_sum = max(i, c_sum + i)
            max_sum = max(max_sum, c_sum)
        return max_sum
```
### 57 四数相加 II
[https://leetcode.cn/problems/4sum-ii/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/4sum-ii/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        info = defaultdict(int)
        # 统计 A + B 的所有组合和
        for a in nums1:
            for b in nums2:
                info[a + b] += 1

        # 遍历 C + D，统计匹配数量
        res = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                res += info.get(target, 0)

        return res
```
### 58 随机链表的复制
[https://leetcode.cn/problems/copy-list-with-random-pointer/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/copy-list-with-random-pointer/?envType=problem-list-v2&envId=vi8yu3g)

```
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        info = {}

        # 第一次遍历：复制所有节点，并存在 info 映射中
        p = head
        while p:
            info[p] = Node(p.val)
            p = p.next

        # 第二次遍历：设置 next 和 random
        p = head
        while p:
            if p.next:
                info[p].next = info.get(p.next)
            if p.random:
                info[p].random = info.get(p.random)
            p = p.next

        return info[head]
```
### 59 最大连续1的个数 III
[https://leetcode.cn/problems/max-consecutive-ones-iii/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/max-consecutive-ones-iii/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 滑动窗口：如果窗口内的 0 超过 k 个，就收缩 left，直到窗口合法
        l = 0
        count = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1

            # 当窗口中 0 的个数超过 k，需要收缩左边
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
```
### 60 四数之和
[https://leetcode.cn/problems/4sum/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/4sum/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                l, r = j + 1,  len(nums) - 1
                while l < r:
                    add = nums[i] + nums[j] + nums[l] + nums[r] 
                    if add < target:
                        l += 1
                    elif add > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        # 继续
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res  
```
### 61 乘积最大子数组
[https://leetcode.cn/problems/maximum-product-subarray/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/maximum-product-subarray/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 正负都需要记录
        max_res = min_res = res = nums[0]

        for n in nums[1:]:
            max_res, min_res = max(n, n * max_res, n * min_res), min(n, n * max_res, n * min_res)
            res = max(res, max_res)
        return res
```
### 62 课程表
[https://leetcode.cn/problems/course-schedule/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/course-schedule/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 邻接表
        adj_list = defaultdict(list)
        # 入度
        in_degree = defaultdict(int)
        for i, j in prerequisites:
            adj_list[j].append(i)
            in_degree[i] += 1

        # 初始化队列 入度为0
        queue = deque([k for k in range(numCourses) if in_degree[k] == 0])
        
        # 排序
        res = []
        while queue:
            cur = queue.popleft()
            for next_cur in adj_list[cur]:
                in_degree[next_cur] -= 1
                if in_degree[next_cur] == 0:
                    queue.append(next_cur)
            res.append(cur)
        return len(res) == numCourses
```
### 63 用最少数量的箭引爆气球
[https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 每次选择最靠右的重叠区间的终点射箭
        
        # 按气球的右端点升序排序
        points.sort(key=lambda x: x[1])
        
        res = 1
        pos = points[0][1]

        for start, end in points[1:]:
            if start > pos:
                res += 1
                pos = end  # 新的箭位置为当前气球的右边界

        return res
```
### 64 最低票价
[https://leetcode.cn/problems/minimum-cost-for-tickets/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/minimum-cost-for-tickets/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # dp[i] 表示从第 1 天到第 i 天的最低费用
        dp = [0] * (days[-1] + 1)

        for i in range(1, days[-1] + 1):
            if i not in days:
                dp[i] = dp[i - 1]  # 不出门，费用等于前一天
            else:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )

        return dp[days[-1]]
```
### 65 数组中的最长山脉
[https://leetcode.cn/problems/longest-mountain-in-array/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/longest-mountain-in-array/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 3:
            return 0

        up = [0] * n
        down = [0] * n

        # 从左到右构建上升长度
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = up[i - 1] + 1

        # 从右到左构建下降长度
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1

        res = 0
        for i in range(n):
            if up[i] > 0 and down[i] > 0:
                res = max(res, up[i] + down[i] + 1)

        return res
```
### 66 零钱兑换 II
[https://leetcode.cn/problems/coin-change-ii/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/coin-change-ii/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(amount + 1):
                if j >= coin:
                    dp[j] = dp[j] + dp[j - coin]
        return dp[-1]
```
### 67 从中序与后序遍历序列构造二叉树
[https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # 9, 3, 15,20,7 左 中 右
        # 9, 15,7,20, 3 左 右 中 i = 1
        if not postorder:
            return None 
        root_val = postorder[-1]
        index = inorder.index(root_val)

        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root
```
### 68 二叉树展开为链表
[https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        p = root
        while p:
            if p.left:
                # 找到左子树的最右节点
                pre = p.left
                while pre.right:
                    pre = pre.right
                # 接到右子树前
                pre.right = p.right
                # 移动左子树到右边
                p.right = p.left
                p.left = None
            p = p.right
```
### 69 一和零
[https://leetcode.cn/problems/ones-and-zeroes/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/ones-and-zeroes/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j] 表示在 最多有 i 个 0 和 j 个 1 的限制下，最多能选择多少个字符串
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
```
### 70 基本计算器 II
[https://leetcode.cn/problems/basic-calculator-ii/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/basic-calculator-ii/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 栈保存当前的结果项
        stack = []
        num = 0
        sign = '+'  # 上一个运算符 sign
        s += '+'  # 补个符号，保证最后一个数被处理
        for c in s:
            if c == ' ':
                continue
            elif c in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / float(num))
                sign = c
                num = 0
            else:
                num = num * 10 + int(c)  # 连续读取多位数字时

        return sum(stack)
```
### 71 解码方法
[https://leetcode.cn/problems/decode-ways/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/decode-ways/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] 表示字符串前 i 个字符的解码方法数
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # 空字符串有 1 种解码方式
        dp[1] = 1  # 第一位不为 '0'，就有一种方式

        for i in range(2, n + 1):
            one = int(s[i - 1])        # 取最后一位
            two = int(s[i - 2:i])      # 取最后两位

            if 1 <= one <= 9:
                dp[i] += dp[i - 1]

            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
```
### 72 寻找旋转排序数组中的最小值
[https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # 最小值在右侧
                l = mid + 1
            else:
                # 最小值在左侧或就是 mid
                r = mid

        return nums[l]
```
### 73 连续数组
[https://leetcode.cn/problems/contiguous-array/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/contiguous-array/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        info = {0: -1}  # 前缀和为 0 的初始下标是 -1
        count = 0
        res = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in info:
                res = max(res, i - info[count])
            else:
                info[count] = i  # 只保留第一次出现的位置

        return res
```
### 74 下一个更大元素 II
[https://leetcode.cn/problems/next-greater-element-ii/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/next-greater-element-ii/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        info = {}
        stack = []
        for i in range(n * 2):
            idx = i % n
            while stack and nums[idx] > nums[stack[-1]]:
                info[stack.pop()] = nums[idx]
            if i < n:
                stack.append(idx)

        return [info.get(i, -1) for i in range(n)]
```
### 75 买卖股票的最佳时机含冷冻期
[https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # 今天持有股票的最大利润
        buy = [0] * n
        # 今天卖出股票后的最大利润
        sell = [0] * n
        # 今天处于冷冻期（不能买）的利润
        cool = [0] * n

        buy[0] = -prices[0]
        sell[0] = 0
        cool[0] = 0

        for i in range(1, n):
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])
            sell[i] = buy[i-1] + prices[i]
            cool[i] = max(cool[i-1], sell[i-1])

        return max(sell[-1], cool[-1])
```
### 76 爱吃香蕉的珂珂
[https://leetcode.cn/problems/koko-eating-bananas/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/koko-eating-bananas/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def can_finish(k):
            res = 0
            for pile in piles:
                res += math.ceil(pile * 1.0 / k)
            return res <= h

        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1
        return l
```
### 77 找到字符串中所有字母异位词
[https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        s_dic, p_dic = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            s_dic[s[i]] += 1
            p_dic[p[i]] += 1

        res = []
        if s_dic == p_dic:
            res.append(0)
        
        l, r = 0, len(p) - 1
        while r < len(s) - 1:
            right = s[r + 1]
            left = s[l]
            if s_dic[left] == 1:
                del s_dic[left]
            else:
                s_dic[left] -= 1
            
            s_dic[right] += 1
            if s_dic == p_dic:
                res.append(l + 1)

            l += 1
            r += 1

        return res


```
### 78 求根节点到叶节点数字之和
[https://leetcode.cn/problems/sum-root-to-leaf-numbers/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/sum-root-to-leaf-numbers/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = 0
        def dfs(node, cur):
            if not node:
                return 
            cur = cur * 10 + node.val
            if not node.left and not node.right:  
                self.res += cur
                return 
            dfs(node.left, cur)
            dfs(node.right, cur)
        dfs(root, 0)
        return self.res
```
### 79 去除重复字母
[https://leetcode.cn/problems/remove-duplicate-letters/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/remove-duplicate-letters/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 统计字符最后出现的位置
        info = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and info[stack[-1]] > i:
                stack.pop()
            stack.append(c)
        return ''.join(list(stack))
```
### 80 颜色分类
[https://leetcode.cn/problems/sort-colors/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/sort-colors/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # low 指向下一个该放 0 的位置
        # high 指向下一个该放 2 的位置
        low, i, high = 0, 0, len(nums) - 1
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
            elif nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
                i -= 1  # 注意
            i += 1
```
### 81 比较版本号
[https://leetcode.cn/problems/compare-version-numbers/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/compare-version-numbers/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l, r = 0, 0
        while l < len(version1) or r < len(version2):
            cur1, cur2 = 0, 0
            while l < len(version1):
                if version1[l] == '.':
                    break
                else:
                    cur1 = cur1 * 10 + int(version1[l])
                    l += 1
            while r < len(version2):
                if version2[r] == '.':
                    break
                else:
                    cur2 = cur2 * 10 + int(version2[r])
                    r += 1
            if cur1 < cur2:
                return -1
            elif cur1 > cur2:
                return 1
            else:
                l += 1
                r += 1
        return 0
```
### 82 单词搜索
[https://leetcode.cn/problems/word-search/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/word-search/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        def dfs(board, word, i, j, index):
            if index == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False
            
            tmp = board[i][j]
            board[i][j] = '.'
            res = (
                dfs(board, word, i + 1, j, index + 1) or 
                dfs(board, word, i - 1, j, index + 1) or 
                dfs(board, word, i, j + 1, index + 1) or 
                dfs(board, word, i, j - 1, index + 1)    
            )
            board[i][j] = tmp
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(board, word, i, j, 0):
                    return True
        return False
```
### 83 [难]矩阵中的最长递增路径
[https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/?envType=problem-list-v2&envId=vi8yu3g)

### 84 字符串解码
[https://leetcode.cn/problems/decode-string/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/decode-string/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 存储当前的结果和重复次数
        stack = []
        cur = "" 
        num = 0
        
        for char in s:
            if char.isdigit(): 
                num = num * 10 + int(char)
            elif char == '[':  
                stack.append((cur, num))
                cur = ""
                num = 0
            elif char == ']':  
                pre_cur, repeat = stack.pop()
                cur = pre_cur + cur * repeat
            else: 
                cur += char
        
        return cur
```
### 85 最长公共子序列
[https://leetcode.cn/problems/longest-common-subsequence/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/longest-common-subsequence/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp[i][j] 表示 text1[0:i] 与 text2[0:j] 的最长公共子序列长度
        m, n = len(text1), len(text2)
        # m+1 * n+1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
```
### 86 全平方数
[https://leetcode.cn/problems/perfect-squares/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/perfect-squares/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] 表示和为 i 的最少平方数数量
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
```
### 87 最小栈
[https://leetcode.cn/problems/min-stack/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/min-stack/?envType=problem-list-v2&envId=vi8yu3g)

```
class MinStack(object):

    def __init__(self):
        self.data = []
        self.stack = []
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.data.append(val)
        if not self.stack or self.stack[-1] >= val:
            self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        cur = self.data.pop()
        if cur == self.stack[-1]:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1]
```
### 88 分割回文串
[https://leetcode.cn/problems/palindrome-partitioning/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/palindrome-partitioning/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def is_ok(subs):
            return subs == subs[::-1]

        def backtrack(l, cur):
            if l == len(s):
                res.append(cur[:])  
                return
            for r in range(l, len(s)):
                if is_ok(s[l:r+1]):
                    cur.append(s[l:r+1])
                    backtrack(r + 1, cur)
                    cur.pop()

        backtrack(0, [])
        return res
```
### 89 反转字符串中的单词
[https://leetcode.cn/problems/reverse-words-in-a-string/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/reverse-words-in-a-string/?envType=problem-list-v2&envId=vi8yu3g)

面试一般原地实现：

```
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = list(s)

        def trim_spaces(s):
            while s and s[0] == ' ':
                s.pop(0)
            while s and s[-1] == ' ':
                s.pop(-1)
            i = 0
            while i < len(s):
                if s[i] == ' ' and i > 0 and s[i - 1] == ' ':
                    s.pop(i)
                else:
                    i += 1

        def reverse(s, l, r):
            while l <= r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        def reverse_word(s):
            l, r = 0, 0
            while l < len(s):
                while r < len(s) and s[r] != ' ':
                    r += 1
                reverse(s, l, r - 1)
                l = r + 1
                r = l

        # 1. 去除多余空格（原地）
        trim_spaces(s)
        # 2. 反转整个字符串
        reverse(s, 0, len(s)-1)
        # 3. 逐个反转单词
        reverse_word(s)
        
        return ''.join(s)
```
### 90 Z 字形变换
[https://leetcode.cn/problems/zigzag-conversion/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/zigzag-conversion/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cur = 0
        pos = -1  # 向下1 向上-1

        for c in s:
            rows[cur] += c
            if cur == 0 or cur == numRows - 1:
                pos *= -1
            cur += pos

        return ''.join(rows)Z 字形变换
```
### 91 对角线遍历
[https://leetcode.cn/problems/diagonal-traverse/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/diagonal-traverse/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        res = []
        i, j = 0, 0
        pos = 1  # 1: ↗, -1: ↙
        for _ in range(m * n):
            res.append(mat[i][j])

            if pos == 1:  # ↗

                if j == n - 1:  # 右触边 向下
                    i += 1
                    pos = -1
                elif i == 0:  # 上触边 向右
                    j += 1
                    pos = -1
                else:
                    i -= 1
                    j += 1
            else:  # ↙
                if i == m - 1:
                    j += 1
                    pos = 1
                elif j == 0:
                    i += 1
                    pos = 1
                else:
                    i += 1
                    j -= 1

        return res
```
### 92 腐烂的橘子
[https://leetcode.cn/problems/rotting-oranges/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/rotting-oranges/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 把所有腐烂橘子（2）加入队列
        # 每一轮 BFS 表示“过了一分钟”

        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # 初始化队列：找到所有腐烂橘子 & 统计新鲜橘子
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (位置 + 当前分钟数)
                elif grid[r][c] == 1:
                    fresh += 1

        # 方向数组：上、下、左、右
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        minutes = 0

        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # 被感染
                    fresh -= 1
                    queue.append((nr, nc, minutes + 1))

        return minutes if fresh == 0 else -1
```
### 93 简化路径
[https://leetcode.cn/problems/simplify-path/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/simplify-path/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        parts = path.split("/")
        stack = []
        for c in parts:
            if c == '' or c == '.':
                continue
            if c == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(c)
        return '/' + '/'.join(list(stack))
```
### 94 最小路径和
[https://leetcode.cn/problems/minimum-path-sum/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/minimum-path-sum/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp[i][j]表示从(0,0)到位置(i,j)的最小路径和
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        # 第一列
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        # 第一行
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]
```
### 95 删除并获得点数
[https://leetcode.cn/problems/delete-and-earn/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/delete-and-earn/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 类似于打家劫舍，选择了n就不能选择 n-1 和 n+1
        # dp[i] 表示考虑到数字 i 时的最大点数
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num

        dp = [0] * (max_num + 1)
        dp[0] = points[0]
        dp[1] = max(points[0], points[1])
        
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])

        return dp[max_num]
```
### 96 H 指数
[https://leetcode.cn/problems/h-index/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/h-index/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h
```
### 97 压缩字符串
[https://leetcode.cn/problems/string-compression/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/string-compression/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return len(chars)
            
        def helper(chars, l, cur, num):
            chars[l] = cur
            l += 1
            if num > 1:  # 只有num > 1时才写入次数
                for digit in str(num):  # 次数可能超过一位数
                    chars[l] = digit
                    l += 1
            return l
            
        l = 0
        cur, num = chars[0], 0
        for c in chars:
            if c != cur:
                l = helper(chars, l, cur, num)
                cur = c
                num = 1
            else:
                num += 1
        l = helper(chars, l, cur, num)
        return l
```
### 98 环形子数组的最大和
[https://leetcode.cn/problems/maximum-sum-circular-subarray/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/maximum-sum-circular-subarray/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 非循环部分 中间最大子数组和
        c_sum = max_sum = nums[0]
        for i in nums[1:]:
            c_sum = max(i, c_sum + i)
            max_sum = max(max_sum, c_sum)

        # 循环部分 总和 - 最小子数组和
        c_sum = min_sum = nums[0]
        for i in nums[1:]:
            c_sum = min(i, c_sum + i)
            min_sum = min(min_sum, c_sum)

        # 全是负的  循环部分：总和 - 最小子数组和 = 0
        if max_sum < 0:
            return max_sum

        return max(max_sum, sum(nums) - min_sum)
```
### 99 奇偶链表
[https://leetcode.cn/problems/odd-even-linked-list/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/odd-even-linked-list/?envType=problem-list-v2&envId=vi8yu3g)

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        l = head
        r = head.next
        r_head = r  # 保存偶数头部，最后连接用

        while r and r.next:
            l.next = r.next
            l = l.next

            r.next = l.next
            r = r.next

        l.next = r_head  # 连接奇数尾部和偶数头部
        return head
```
### 100 合并区间
[https://leetcode.cn/problems/merge-intervals/description/?envType=problem-list-v2&envId=vi8yu3g](https://leetcode.cn/problems/merge-intervals/description/?envType=problem-list-v2&envId=vi8yu3g)

```
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 排序，遍历如果当前区间与结果中的最后一个区间 重叠，就合并它们
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for cur in intervals[1:]:
            last = res[-1]
            if cur[0] <= last[1]:
                last[1] = max(cur[1], last[1])
            else:
                res.append(cur)
        return res
```
### 

