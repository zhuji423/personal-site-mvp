---
title: "1、[易]两数之和"
description: "leetcode 热题HOT100"
date: "2026-04-28"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\05_algorithm_backup\\ku_backup_20260427\\13_leetcode热题HOT100.md"
---
leetcode 热题HOT100

# 1、[易]两数之和
[https://leetcode.cn/problems/two-sum/description/](https://leetcode.cn/problems/two-sum/description/)

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        info = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in info:
                return [i, info[value]]
            else:
                info[num] = i
        return []
```
```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(n)
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res(2);
        unordered_map<int,int> map;
        for(int i=0;i<nums.size();i++){
            int tmp = target - nums[i];
            if(map.find(tmp)!=map.end()){
                res[0] = i;
                res[1] = map[tmp];
                break;
            }
            map[nums[i]] = i;
        }
        return res;
    }
};
```
# 2、[中]两数相加
[https://leetcode.cn/problems/add-two-numbers/](https://leetcode.cn/problems/add-two-numbers/)

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

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
        head = ListNode()
        p = head

        cin = 0
        while l2 or l1:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            val = (x + y + cin) % 10
            cin = (x + y + cin) // 10

            p.next = ListNode(val)
            p = p.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if cin:
            p.next = ListNode(1)

        return head.next 
```
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 // 时间复杂度：O(max(m,n))，空间复杂度：O(max(m,n))， 新列表的长度最多为max(m,n)+1
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(0);
        ListNode* head = res;
        int flag = 0;
        while(l1 || l2){
            int x = l1?l1->val:0;
            int y = l2?l2->val:0;
            head->next = new ListNode((x+y+flag)%10);
            flag = x+y+flag>9?1:0;
            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
            head = head->next;
        }
        if(flag==1){
            head->next = new ListNode(1);
        }
        return res->next;
    }
};
```
# 3、[中]无重复字符的最长子串
[https://leetcode.cn/problems/longest-substring-without-repeating-characters/](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 如果 s[right] 不在集合中，扩大右边界 right，并更新最大长度
        # 如果 s[right] 在集合中，缩小左边界 left，直到无重复
        char_set = set()
        max_len = 0
        left = right = 0
        
        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
            
        return max_len
```
```
// 时间复杂度：O(n)，空间复杂度：O(m)，m 是字符集的大小
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        unordered_map<char,int> map;
        int i = 0;
        for(int j=0;j<s.size();j++){
            if(map.find(s[j])!=map.end()){
                i = max(map[s[j]],i);
            }
            map[s[j]] = j+1;
            res = max(j-i+1, res);
        }
        return res;
    }
};
```
# 4~~、[难]寻找两个有序数组的中位数~~
[https://leetcode.cn/problems/median-of-two-sorted-arrays/description/](https://leetcode.cn/problems/median-of-two-sorted-arrays/description/)

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5



```
class Solution {
public:
    // 时间复杂度：O(log(min(m,n)))，空间复杂度：O(1)O(1)
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()>nums2.size())
            return findMedianSortedArrays(nums2,nums1);
        int m = nums1.size(), n = nums2.size();
        int lmax1,rmin1,lmax2,rmin2,c1,c2,low=0,heigh=2*m;
        while(low <= heigh){
            int c1 = (low+heigh)/2;
            int c2 = m+n-c1;
            lmax1 = c1 == 0? INT_MIN:nums1[(c1-1)/2];
            rmin1 = c1 == 2*m? INT_MAX:nums1[c1/2];
            lmax2 = c2 == 0? INT_MIN:nums2[(c2-1)/2];
            rmin2 = c2 == 2*n? INT_MAX:nums2[c2/2];
            if(lmax1>rmin2) heigh = c1-1;
            else if(lmax2>rmin1) low = c1+1;
            else break;
        }
        return (max(lmax1,lmax2)+min(rmin1,rmin2))/2.0;
    }
};
```
# 5、[中]最长回文子串
[https://leetcode.cn/problems/longest-palindromic-substring/description/](https://leetcode.cn/problems/longest-palindromic-substring/description/)

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

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

        def sub(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -=1
                r += 1 
            return r - l - 1

        l = r = 0
        for i in range(len(s)):
            l1 = sub(i, i)
            l2 = sub(i, i + 1)
            max_l = max(l1, l2)
            if max_l > r - l:
                l = i - (max_l - 1) // 2
                r = i + max_l // 2
        return s[l:r + 1]

```
```
class Solution {
public:
    // 时间复杂度：O(n^2)，空间复杂度：O(1)
    string longestPalindrome(string s) {
        int start=0, len=0;
        for(int i=0;i<s.size();i++){
            int tmp = max(getsub(i,i,s),getsub(i,i+1,s));
            if(tmp>len){
                len = tmp;
                start = i-(len-1)/2;
            }
        }
        return s.substr(start,len);
    }

    int getsub(int i,int j,string s){
        while(i>=0 && j<s.size() && s[i]==s[j]){
            i--;
            j++;
        }
        return j-i-1;
    }
};
```
# 6~~、[难]正则表达式匹配~~
[https://leetcode.cn/problems/regular-expression-matching/](https://leetcode.cn/problems/regular-expression-matching/)

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

```

```
```
class Solution {
public:
    bool isMatch(string s, string p) {
        const char* str = s.c_str();
        const char* pattern = p.c_str();
        return match(str,pattern);
    }

    bool match(const char* str, const char* pattern)
    {
        if(*str == '\0' && *pattern == '\0') return true;
        if(*str != '\0' && *pattern == '\0') return false;
        if(*(pattern+1) != '*'){
            if(*str==*pattern || *pattern=='.'&&*str!='\0'){
                return match(str+1,pattern+1);
            }
            else return false;
        }
        else{
            if(*str==*pattern || *pattern=='.'&&*str!='\0'){
                return match(str,pattern+2)|| match(str+1,pattern+2)|| match(str+1,pattern);
            }
            else return match(str,pattern+2);
        }
    }
};
```
```
class Solution {
public:
    // 时间复杂度：O(TP)，空间复杂度：O(TP)
    bool isMatch(string s, string p) {
        int l1 = s.size(),l2 = p.size();
        vector<vector<bool>> dp(l1+1,vector<bool>(l2+1));
        dp[l1][l2]=true;
        for(int i=l1;i>=0;i--){
            for(int j=l2-1;j>=0;j--){
                bool tmp = i<l1 && ( s[i] == p[j] || p[j] == '.');
                if(j+1<l2 && p[j+1] == '*'){
                    dp[i][j] = dp[i][j+2] || tmp && dp[i+1][j];
                }
                else{
                    dp[i][j] = tmp && dp[i+1][j+1];
                }
            }
        }
        return dp[0][0];
    }
};
```
# 7、[中]盛最多水的容器
[https://leetcode.cn/problems/container-with-most-water/](https://leetcode.cn/problems/container-with-most-water/)

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。


示例:

![](/personal-site-mvp/img/doc-placeholder.svg "")

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0 
        r = len(height) - 1
        while l <= r:
            res = max(res, (r - l) * (min(height[l], height[r])))
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return res
```
```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(1)
    int maxArea(vector<int>& height) {
        int res=0;
        int i=0,j=height.size()-1;
        while(i<j){
            res = max(res,(j-i)*min(height[i],height[j]));
            if(height[i]<height[j]) i++;
            else j--;
        }
        return res;
    }
};
```
# 8、[中]三数之和
[https://leetcode.cn/problems/3sum/](https://leetcode.cn/problems/3sum/)

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
[-1, 0, 1],
[-1, -1, 2]
]

```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 排序数组：方便跳过重复元素和使用双指针
        # 固定一个数：遍历数组，固定 nums[i] 作为第一个数
        # 双指针查找：在剩余部分使用双指针寻找 -nums[i] 的组合
        # 去重处理：跳过重复元素避免重复解
        res = []

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    # 继续
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return res
```
```
class Solution {
public:
    // 时间复杂度：O(n^2)，空间复杂度：O(1)
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.empty()) return res;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++){
            if(i>=1 && nums[i] == nums[i-1]) continue;
            if(nums[i]>0) break;
            int l=i+1,r=nums.size()-1;
            while(l<r){
                if(nums[l]+nums[r]+nums[i] < 0) l++;
                else if(nums[l]+nums[r]+nums[i] > 0) r--;
                else{
                    res.push_back({nums[i],nums[l],nums[r]});
                    l++;
                    r--;
                    while(l<r && nums[l]==nums[l-1]) l++;
                    while(l<r && nums[r]==nums[r+1]) r--;
                }
            }
        }
        return res;
    }
};
```
# 9、[中]电话号码的字母组合
[https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/)

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。


示例:

![](/personal-site-mvp/img/doc-placeholder.svg "")

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

```
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 使用回溯法：
        # 维护当前组合和结果列表
        # 递归构建所有可能的组合
        # 当组合长度等于输入数字长度时，加入结果
        if not digits:
            return []

        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def back(index, cur):
            if index == len(digits):
                result.append(''.join(cur))
                return

            for c in digit_map[digits[index]]:
                cur.append(c)
                back(index + 1, cur)
                cur.pop()

        back(0, [])
        return result
```
```
class Solution {
public:
    // 时间复杂度：O(3^N*4^M)，空间复杂度：O(3^N*4^M)
    unordered_map<char,string> map{{'2',"abc"},{'3',"def"},{'4',"ghi"},{'5',"jkl"},{'6',"mno"},{'7',"pqrs"},{'8',"tuv"},{'9',"wxyz"}};

    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if(digits.empty()) return res;
        help("",digits,res);
        return res;
    }

    void help(string str, string digits, vector<string> &res) {
        if(str.size() == digits.size()){
            res.push_back(str);
            return;
        }
        string tmp = map[digits[str.size()]];
        for(int i=0;i<tmp.size();i++){
            str += tmp[i];
            help(str,digits,res);
            str.pop_back();
        }
        return;
    }
};
```
注：可以联系剑指offer27题一起看

```
class Solution {
public:
    // 时间复杂度：O(3^N*4^M)，空间复杂度：O(3^N*4^M)
    vector<string> letterCombinations(string digits) {
        unordered_map<char,string> map{{'2',"abc"},{'3',"def"},{'4',"ghi"},{'5',"jkl"},{'6',"mno"},{'7',"pqrs"},{'8',"tuv"},{'9',"wxyz"}};
        vector<string> res;
        if(digits.empty()) return res;
        if(digits.size() == 1){
            string tmp = map[digits[0]];
            for(char w : tmp) {
                string s(1,w);
                res.push_back(s);
            }
            return res;
        }
        vector<string> last = letterCombinations(digits.substr(0,digits.size()-1));
        string tmp = map[digits[digits.size()-1]]; //abc def
        for(int i=0;i<last.size()||i==0;i++){
            for(int j=0;j<tmp.size();j++){
                res.push_back(last[i]+tmp[j]);
            }
        }
        return res;
    }
};
```
# 10、[中]删除链表的倒数第N个节点
[https://leetcode.cn/problems/remove-nth-node-from-end-of-list/](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # 使用两个指针 fast 和 slow，初始都指向头结点
        # 先让 fast 向前移动 n 步
        # 然后 fast 和 slow 同时移动，直到 fast 到达链表末尾
        # 此时 slow 指向的就是倒数第 n+1 个结点
        # 修改 slow.next 指针来删除倒数第 n 个结点
        dummy = ListNode(0, head)
        l = r = dummy

        for _ in range(n):
            r = r.next
        
        while r.next:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next
```
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1)
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(!head || n==0) return head;
        ListNode* l1 = head;
        ListNode* l2 = head;
        int k=0;
        while(l1){
            if(k>n) l2 = l2->next;
            l1 = l1->next;
            k++;
        }
        // 倒数第k-1个结点l2
        if(k == n) return head->next;
        l2->next = l2->next->next;
        return head;
    }
};
```
# 11、[易]有效的括号
[https://leetcode.cn/problems/valid-parentheses/description/](https://leetcode.cn/problems/valid-parentheses/description/)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

```
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False

        def isok(a, b):
            return a == '(' and b == ')' or a == '[' and b == ']' or a == '{' and b == '}'
        
        d = []
        for c in s:
            if len(d) == 0 or not isok(d[-1], c):
                d.append(c)
            else:
                d.pop()
                
        return len(d) == 0
        
```
```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n)
    bool isValid(string s) {
        stack<char> stack;
        for(int i=0;i<s.size();i++){
            if(stack.empty() || !isok(stack.top(),s[i])){
                stack.push(s[i]);
            }
            else stack.pop();
        }
        return stack.empty();
    }

    bool isok(char a, char b) {
        return a=='('&&b==')' || a=='['&&b==']' || a=='{'&&b=='}';
    }
};
```
# 12、[易]合并两个有序链表
[https://leetcode.cn/problems/merge-two-sorted-lists/description/](https://leetcode.cn/problems/merge-two-sorted-lists/description/)

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        p = dummy
        while list1 and list2:
            val = list1.val
            if list1.val < list2.val:
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            p.next = ListNode(val)
            p = p.next

        if list1:
            p.next = list1
        if list2:
            p.next = list2

        return dummy.next
```
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n+m)，空间复杂度：O(1)
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(0);
        ListNode* head = res;
        while(l1 && l2){
            if(l1->val<l2->val){
                head->next = l1;
                l1 = l1->next;
            }
            else{
                head->next = l2;
                l2 = l2->next;
            }
            head = head->next;
        }
        head->next = l1?l1:l2;
        return res->next;
    }
};
```
# 13、[中]括号生成
[https://leetcode.cn/problems/valid-parentheses/](https://leetcode.cn/problems/valid-parentheses/)

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]

```
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 递归构建有效括号组合：
        # 维护当前字符串和左右括号的计数
        # 只有在左括号数量小于n时可以添加左括号
        # 只有在右括号数量小于左括号时可以添加右括号
        # 终止条件：
        # 当字符串长度达到2n时，将当前组合加入结果
        
        res = []
        def back(cur, l, r):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if l < n:
                back(cur + '(', l + 1, r)
            if r < l:
                back(cur + ')', l, r + 1)

        back('', 0, 0)
       
        return res
```
```
class Solution {
public:
    // 时间复杂度：O(4^n/sqrt(n))，空间复杂度：O(4^n/sqrt(n))
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if(n==0) return {""};
        for(int i=0;i<n;i++){
            vector<string> left = generateParenthesis(i);
            vector<string> right = generateParenthesis(n-1-i);
            for(string l :left){
                for(string r :right){
                    res.push_back("("+l+")"+r);
                }
            }
        }
        return res;
    }
};
```
# 14、[难]合并K个排序链表
[https://leetcode.cn/problems/merge-k-sorted-lists/description/](https://leetcode.cn/problems/merge-k-sorted-lists/description/)

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
1->4->5,
1->3->4,
2->6
]
输出: 1->1->2->3->4->4->5->6

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

        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        while heap:
            val, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))

        return dummy.next
```
# ~~15、[中]下一个排列~~
[https://leetcode.cn/problems/next-permutation/](https://leetcode.cn/problems/next-permutation/)

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1)
    void nextPermutation(vector<int>& nums) {
        int i= nums.size()-2;
        while(i>=0 && nums[i]>=nums[i+1]){
            i--;
        }
        if(i>=0) {
            int j = nums.size()-1;
            while(j>=0 && nums[j]<=nums[i]){
                j--;
            }
            swap(nums[i],nums[j]);
        }
        reverse(nums,i+1);
    }

    void reverse(vector<int>& nums,int n){
        int l=n,r=nums.size()-1;
        while(l<r){
            swap(nums[l],nums[r]);
            l++;
            r--;
        }
    }
};
```
# ~~16、[难]最长有效括号~~
[https://leetcode.cn/problems/longest-valid-parentheses/](https://leetcode.cn/problems/longest-valid-parentheses/)

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1)
    int longestValidParentheses(string s) {
        int l = 0, r = 0 , res = 0;
        for(int i=0;i<s.size();i++){
            if(s[i] == '(') l++;
            if(s[i] == ')') r++;
            if(l==r) res = max(res,2*l);
            if(r>l) l=r=0;
        }
        l=0,r=0;
        for(int i=s.size()-1;i>=0;i--){
            if(s[i] == '(') l++;
            if(s[i] == ')') r++;
            if(l==r) res = max(res,2*l);
            if(l>r) l=r=0;
        }
        return res;
    }
};
```
# 17、[中]搜索旋转排序数组
[https://leetcode.cn/problems/search-in-rotated-sorted-array/description/](https://leetcode.cn/problems/search-in-rotated-sorted-array/description/)

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

```
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 确定有序部分：虽然数组整体不是有序的，但旋转后的数组至少有一半是有序的
        # 判断目标值位置：
        # 如果 target 在有序部分，继续在有序部分搜索
        # 否则在另一部分搜索
        # 调整搜索范围：根据比较结果调整左右指针
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1
```
```
class Solution {
public:
	// 时间复杂度：O(logN)，空间复杂度：O(1)
    int search(vector<int>& nums, int target) {
        return help(nums,target,0,nums.size()-1);
    }
    int help(vector<int>& nums, int target, int l, int r) {
        if(l>r) return -1;
        int mid = (l+r)/2;
        if(nums[mid] == target) return mid;
        if(nums[mid]>nums[r]){ // 3 4 7 8 1 2  旋转点在右，左顺序
            if(nums[l]<=target && target <nums[mid]) return help(nums,target,l,mid-1);
            else return help(nums,target,mid+1,r);
        }
        else{ // 7 8 1 2 3 4
            if(nums[mid]<target && target <=nums[r]) return help(nums,target,mid+1,r);
            else return help(nums,target,l,mid-1);
        }
    }
};
```
# 18、[中]在排序数组中查找元素的第一个和最后一个位置
[https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/)

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

```
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def helper(n, nums):
            l, r = n, n
            while l >= 0 and nums[l] == nums[n]:
                l -= 1
            while r < len(nums) and nums[r] == nums[n]:
                r += 1
            return [l + 1, r - 1]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return helper(mid, nums)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return [-1, -1]
```
```
class Solution {
public:
	// 时间复杂度：O(logN)，空间复杂度：O(1)
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res{-1,-1};
        int l=0,r=nums.size()-1;
        while(l<=r){
            int mid=(l+r)/2;
            if(nums[mid] == target) {
                help(nums,mid,res);
                break;
            }
            else if(nums[mid] > target) r = mid-1;
            else l = mid+1;
        }
        return res;
    }
    void help(vector<int> nums, int n,vector<int> &res) {
        int l=n,r=n;
        while(l>=0&&nums[l]==nums[n]){
            l--;
        }
        while(r<nums.size()&&nums[r]==nums[n]){
            r++;
        }
        res[0]=l+1;
        res[1]=r-1;
    }
};
```
# 19、[中]组合总和
[https://leetcode.cn/problems/combination-sum/description/](https://leetcode.cn/problems/combination-sum/description/)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
[7],
[2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
[2,2,2,2],
[2,3,3],
[3,5]
]

```
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def back(index, cur, sum):
            if sum == target:
                res.append(cur[:])
                return
            # 避免无限重复 需要结束条件
            if sum > target:
                return
            
            for i in range(index, len(candidates)):
                cur.append(candidates[i])
                sum += candidates[i]
                # 从i开始 可以重复
                back(i, cur, sum)
                cur.pop()
                sum -= candidates[i]

        back(0, [], 0)
        return res
```
```
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<vector<int>> res;
        vector<int> path;
        dfs(candidates,target,0,path,res);
        return res;
    }
    void dfs(vector<int>& candidates, int target, int start, vector<int> &path, vector<vector<int>> &res) {
        if(target == 0) {
            res.push_back(path);
            return;
        }
        for(int i=start;i<candidates.size()&&target>=candidates[i];i++){
            path.push_back(candidates[i]);
            dfs(candidates,target-candidates[i],i,path,res);
            path.pop_back();
        }
    }
};
```
# ~~20、[难]接雨水~~
[https://leetcode.cn/problems/trapping-rain-water/description/](https://leetcode.cn/problems/trapping-rain-water/description/)


上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

![](/personal-site-mvp/img/doc-placeholder.svg "")

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(1)
    int trap(vector<int>& height) {
        int res = 0;
        int l = 0, r = height.size()-1;
        int max_left = 0, max_right = 0;
        while(l<r){
            if(height[l]<height[r]){
                if(height[l]>=max_left) max_left = height[l];
                else res += max_left-height[l];
                l++;
            }
            else{
                if(height[r]>=max_right) max_right = height[r];
                else res += max_right-height[r];
                r--;
            }
        }
        return res;
    }
};
```
# 21、[中]全排列
[https://leetcode.cn/problems/permutations/](https://leetcode.cn/problems/permutations/)

给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
[1,2,3],
[1,3,2],
[2,1,3],
[2,3,1],
[3,1,2],
[3,2,1]
]

```
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def back(cur, use):
            if len(cur) == len(nums):
                res.append(cur[:])
                return 
            for i in range(len(nums)):
                if use[i]:
                    continue
                cur.append(nums[i])
                use[i] = True
                back(cur, use)
                cur.pop()
                use[i] = False
        back([], [False] * (len(nums)))
        return res
        
```
```
class Solution {
public:
    // 时间复杂度：O(n!)，空间复杂度：O(1)
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        help(nums,res,0);
        return res;
    }
    void help(vector<int>& nums, vector<vector<int>> &res, int k){
        if(k==nums.size()-1) res.push_back(nums);
        for(int i=k;i<nums.size();i++){
            swap(nums[i],nums[k]);
            help(nums,res,k+1);
            swap(nums[i],nums[k]);
        }
    }
};
```
# 22、旋转图像
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
[1,2,3],
[4,5,6],
[7,8,9]
],

原地旋转输入矩阵，使其变为:
[
[7,4,1],
[8,5,2],
[9,6,3]
]
示例 2:

给定 matrix =
[
[ 5, 1, 9,11],
[ 2, 4, 8,10],
[13, 3, 6, 7],
[15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
[15,13, 2, 5],
[14, 3, 4, 1],
[12, 6, 8, 9],
[16, 7,10,11]
]

```
class Solution {
public:
    // 时间复杂度：O(n^2)，空间复杂度：O(1)
    void rotate(vector<vector<int>>& matrix) {
        int n= matrix.size();
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                swap(matrix[i][j],matrix[j][i]);
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n/2;j++){
                swap(matrix[i][j],matrix[i][n-1-j]);
            }
        }
    }
};
```
# 23、字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
["ate","eat","tea"],
["nat","tan"],
["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

```
class Solution {
public:
	// 时间复杂度：O(NK)，空间复杂度：O(NK)
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,int> map;
        vector<vector<string>> res;
        int k = 0;
        for(int i=0;i<strs.size();i++){
            string str = strs[i];
            string node(26,'0'); 
            for(int j=0;j<str.size();j++){
                int t = node[str[j]-'a']-'0'+1;
                node[str[j]-'a']= '0' + t;
            }
            if(map.find(node)!=map.end()){
                res[map[node]].push_back(str);
            }
            else{
                map[node] = k;
                res.push_back(vector<string>{str});
                k++;
            }
        }
        return res;
    }
};
```
# 24、最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(1)
    int maxSubArray(vector<int>& nums) {
        int res = INT_MIN;
        int add = 0;
        for(int i=0;i<nums.size();i++){
            add+=nums[i];
            res=max(res,add);
            if(add<0) add=0;
        }
        return res;
    }
};
```
# 25、跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(1)
    bool canJump(vector<int>& nums) {
       int last = nums.size()-1;
       for(int i=nums.size()-2;i>=0;i--){
           if(i+nums[i]>=last) last = i;
       }
       return last == 0;
    }
};
```
# 26、合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

```
class Solution {
public:
	// 时间复杂度：O(nlogn)，空间复杂度：O(1)
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        sort(intervals.begin(),intervals.end(),Sort);
        for(int i=0;i<intervals.size();i++){
            if(res.empty() || intervals[i][0]>res[res.size()-1][1])
                res.push_back(intervals[i]);
            else
                res[res.size()-1][1] = max(res[res.size()-1][1],intervals[i][1]);
        }
        return res;
    }
    static bool Sort(vector<int> &a,vector<int> &b) {
        return a[0]<b[0];
    }
};
```
# 27、不同路径

例如，上图是一个7 x 3 的网格。有多少可能的路径？

![](/personal-site-mvp/img/doc-placeholder.svg "")

例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。

1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:

输入: m = 7, n = 3
输出: 28

```
class Solution {
public:
	// 时间复杂度：O(nm)，空间复杂度：O(nm)
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m+1,vector<int>(n+1));
        dp[0][0] = 0;
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(i==1||j==1) dp[i][j] = 1;
                else dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[m][n];
    }
};
```
# 28、最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
[1,3,1],
[1,5,1],
[4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

```
class Solution {
public:
	// 时间复杂度：O(nm)，空间复杂度：O(nm)
    int minPathSum(vector<vector<int>>& grid) {
        int res = INT_MAX;
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m,vector<int>(n,0));
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(i==0&&j==0) dp[i][j] = grid[i][j];
                else{
                    if(i==0) dp[i][j] = dp[i][j-1] + grid[i][j];
                    else if(j==0) dp[i][j] = dp[i-1][j] + grid[i][j];
                    else dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j];
                }
            }
        }
        return dp[m-1][n-1];
    }
};
```
# 29、爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。

1. 1 阶 + 1 阶
2. 2 阶

示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。

1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1)
    int climbStairs(int n) {
        // 1 2 3 5
        int i=0,j=1,k=0;
        while(k<n){
            int t = j;
            j = i+j;
            i = t;
            k++;
        }
        return j;
    }
};
```
# 30、编辑距离
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

```
class Solution {
public:
	// 时间复杂度：O(mn)，空间复杂度：O(mn)
    int minDistance(string word1, string word2) {
        int m= word1.size(), n=word2.size();
        vector<vector<int>> dp(m+1,vector<int>(n+1));
        for(int i=0;i<=m;i++){
            for(int j=0;j<=n;j++){
                if(i==0||j==0) dp[i][j]= max(i,j);
                else if(word1[i-1]==word2[j-1]) dp[i][j] = dp[i-1][j-1];
                else dp[i][j]= min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1])) + 1;
            }
        }
        return dp[m][n];
    }
};
```
# 31、颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1)
    void sortColors(vector<int>& nums) {
        int p0 = 0, p2 = nums.size()-1, cur = 0;
        while(cur<=p2){
            if(nums[cur] == 0){
                swap(nums[p0],nums[cur]); 
                p0++;
                cur++;
            }
            else if(nums[cur] == 2){
                swap(nums[p2],nums[cur]); 
                p2--;
            }
            else cur++;
        }
    }
};
```
# 32、最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

```
class Solution {
public:
	// 时间复杂度：O(S+T)，空间复杂度：O(S+T)
    string minWindow(string s, string t) {
        int start = 0, len = INT_MAX;
        int l = 0, r = 0;
        unordered_map<char,int> map;
        unordered_map<char,int> match;
        for(char c : t) map[c]++;
        
        int count = 0;
        while(r<s.size()){
            char t = s[r];
            if(map.count(t)){
                match[t]++;
                if(map[t] == match[t]){
                    count++;
                }
            }
            r++;

            while(map.size()==count){
                if(r-l<len){
                    start = l;
                    len = r-l;
                }
                char t2 = s[l];
                if(map.count(t2)){
                    match[t2]--;
                    if(match[t2]<map[t2]){
                        count--;
                    }
                }
                l++;
            }
        }
        return len == INT_MAX? "":s.substr(start,len);
    }
};
```
# 33、子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
[3],
[1],
[2],
[1,2,3],
[1,3],
[2,3],
[1,2],
[]
]

```
class Solution {
public:
    // 利用二进制，时间复杂度：O(2^n)，空间复杂度：O(2^n)
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        int len = 1<<nums.size();
        for(int i=0;i<len;i++){
            vector<int> tmp;
            for(int j=0;j<nums.size();j++){
                if(i&(1<<j)) tmp.push_back(nums[j]);
            }
            res.push_back(tmp);
        }
        return res;
    }
};
```
```
class Solution {
public:
	// 时间复杂度：O(2^n)，空间复杂度：O(2^n)
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res{{}};
        for(int i=0;i<nums.size();i++){
            int len = res.size();
            for(int j=0;j<len;j++){
                vector<int> tmp(res[j]);
                tmp.push_back(nums[i]);
                res.push_back(tmp);
            }
        }
        return res;
    }
};
```
# 34、单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

```
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if(help(board,i,j,word,0)) return true;
            }
        }
        return false;
    }
    bool help(vector<vector<char>> &board, int i, int j, string word, int k) {
        if(i<0||i>=board.size()||j<0||j>=board[0].size()||board[i][j]=='*'||board[i][j]!=word[k]) return false;
        if(k==word.size()-1) return true;
        char tmp = board[i][j];
        board[i][j] = '*';
        if(help(board,i-1,j,word,k+1)
        || help(board,i+1,j,word,k+1)
        || help(board,i,j-1,word,k+1)
        || help(board,i,j+1,word,k+1)){
            return true;
        }
        board[i][j] = tmp;
        return false;
    }
};
```
# 35、柱状图中最大的矩形

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

![](/personal-site-mvp/img/doc-placeholder.svg "")

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

![](/personal-site-mvp/img/doc-placeholder.svg "")

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10

```
class Solution {
public:
    // 时间复杂度：O(nlogn)，空间复杂度：O(n) 有时候通过有时候超时
    int largestRectangleArea(vector<int>& heights) {
        return help(heights,0,heights.size()-1);
    }
    int help(vector<int> &heights, int l, int r){
        if(l>r) return 0;
        int low = l;
        for(int i=l;i<=r;i++){
            if(heights[i]<heights[low]) low = i;
        }
        return max(heights[low]*(r-l+1),max(help(heights,l,low-1),help(heights,low+1,r)));
    }
};
```
```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(n)
    int largestRectangleArea(vector<int>& heights) {        
        stack<int> st;
        heights.push_back(0);
        int size = heights.size();
        int res = 0;
        for (int i = 0; i < size; i++) {
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                int val = st.top();
                st.pop();
                res = max(res, heights[val] * (st.empty() ? i : (i - st.top() - 1)));
            }
            st.push(i);
        }
        return res;
    } 
};
```
# 36、最大矩形
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]
输出: 6

```
class Solution {
public:
	// 时间复杂度：O(n*m)，空间复杂度：O(m)
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.empty()) return 0;
        int res = 0;
        vector<int> vec(matrix[0].size(),0);
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                vec[j] = matrix[i][j]=='1'?vec[j]+1:0;
            }
            res = max(res,help(vec));
        }
        return res;
    }
    int help(vector<int> &vec){
        stack<int> stack;
        int res = 0;
        vec.push_back(0);
        for(int i=0;i<vec.size();i++){
            while(!stack.empty()&&vec[stack.top()]>=vec[i]){
                int tmp = stack.top();
                stack.pop();
                res = max(res,vec[tmp]*(stack.empty()?i:(i-stack.top()-1)));
            }
            stack.push(i);
        }
        vec.pop_back();
        return res;
    }
};
```
# 37、二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]

```
   1
    \
     2
    /
   3
```
输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(logn) 递归
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        help(res,root);
        return res;
    }
    void help(vector<int> &res, TreeNode* root){
        if(!root) return;
        help(res,root->left);
        res.push_back(root->val);
        help(res,root->right);
    }
};
```
```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(n) 栈
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> stack;
        TreeNode* cur = root;
        while(cur || !stack.empty()){
            while(cur){
                stack.push(cur);
                cur = cur->left;
            }
            cur = stack.top();
            stack.pop();
            res.push_back(cur->val);
            cur = cur->right;
        }
        return res;
    }
};
```
```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(n) 线索二叉树
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        TreeNode* cur = root;
        TreeNode* next;
        while(cur){
            if(!cur->left){
                res.push_back(cur->val);
                cur = cur->right;
            }
            else{
                next = cur->left;
                while(next->right){
                    next = next->right;
                }
                next->right = cur;
                TreeNode* tmp = cur;
                cur = cur->left;
                tmp->left = NULL;
            }
        }
        return res;
    }
};
```
# 38、不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```
```
class Solution {
public:
    // 时间复杂度：O(n^2)，空间复杂度：O(n)
    int numTrees(int n) {
        vector<int> res(n+1);
        res[0] = 1;
        res[1] = 1;
        for(int i=2;i<=n;i++){
            for(int j=1;j<=i;j++){
                res[i] += res[j-1]*res[i-j];
            }
        }
        return res[n];
    }
};
```
# 39、验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:

```
    2
   /  \
  1    3
```
输出: true
示例 2:

输入:

```
    5
   /  \
  1    4
      /  \
      3   6
```
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
根节点的值为 5 ，但是其右子节点值为 4 。

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(n) 中序遍历递增
    bool isValidBST(TreeNode* root) {
        stack<TreeNode*> stack;
        TreeNode* cur = root;
        //int tmp = INT_MIN; // 测试用例用[-2147483648]卡边界值过分了。。。
        long tmp = LONG_MIN;
        while(cur || !stack.empty()){
            while(cur){
                stack.push(cur);
                cur=cur->left;
            }
            cur = stack.top();
            stack.pop();
            if(cur->val<=tmp){
                return false;
            }
            tmp = cur->val;
            cur = cur->right;
        }
        return true;
    }
};
```
# 40、对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

```
    1
   / \
  2   2
   \   \
   3    3
```
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n) 递归
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return help(root->left,root->right);
    }
    bool help(TreeNode* l,TreeNode* r) {
        if(!l && !r) return true;
        if(!l || !r) return false;
        return l->val==r->val && help(l->right,r->left) && help(l->left,r->right);
    }
};
```
```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n) 迭代
    bool isSymmetric(TreeNode* root) {
        queue<TreeNode*> queue;
        queue.push(root);
        queue.push(root);
        while(!queue.empty()){
            TreeNode* t1 = queue.front();
            queue.pop();
            TreeNode* t2 = queue.front();
            queue.pop();
            if(!t1 && !t2) continue;
            if(!t1 || !t2) return false;
            if(t1->val != t2->val) return false;
            queue.push(t1->left);
            queue.push(t2->right);
            queue.push(t2->left);
            queue.push(t1->right);
        }
        return true;
    }
};
```
# 41、二叉树的层次遍历
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```
返回其层次遍历结果：

```
[
  [3],
  [9,20],
  [15,7]
]
```
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n) 
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> queue;
        if(root) queue.push(root);
        while(!queue.empty()){
            int count = queue.size();
            vector<int> tmp;
            while(count!=0){
                tmp.push_back(queue.front()->val);
                count--;
                if(queue.front()->left) queue.push(queue.front()->left);
                if(queue.front()->right) queue.push(queue.front()->right);
                queue.pop();
            }
            res.push_back(tmp);
        }
        return res;
        
    }
};
```
# 42、二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

```
    3
   / \
  9  20
    /  \
   15   7
```
返回它的最大深度 3 。

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(logn) 
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
};
```
# 43、从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

```
    3
   / \
  9  20
    /  \
   15   7·
```
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n) 
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return help(preorder,0,preorder.size()-1,inorder,0,inorder.size()-1);
    }
    TreeNode* help(vector<int>& pre,int pl,int pr,vector<int>& vin,int vl,int vr) {
        if(pl>pr || vl>vr) return NULL;
        TreeNode* head = new TreeNode(pre[pl]);
        int i;
        for(i=vl;i<=vr;i++){
            if(vin[i]==pre[pl]) break;
        }
        int num = i-vl;
        head->left=help(pre,pl+1,pl+num,vin,vl,vl+num-1);
        head->right=help(pre,pl+num+1,pr,vin,vl+num+1,vr);
        return head;
    }
};
```
# 44、二叉树展开为链表
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

```
    1
   / \
  2   5
 / \   \
3   4   6
```
将其展开为：

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 先序遍历 线索二叉树
    // 时间复杂度：O(n)，空间复杂度：O(1) 
    void flatten(TreeNode* root) {
        TreeNode* cur = root;
        TreeNode* next;
        while(cur){
            if(!cur->left){
                cur = cur->right;
            }
            else{
                next = cur->left;
                while(next->right){
                    next = next->right;
                }
                next->right = cur->right;
                cur->right = cur->left;
                cur->left = NULL;
                cur = cur->right;
            }
        }
    }
    /*
    // 中序遍历 线索二叉树
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        TreeNode* cur = root;
        TreeNode* next;
        while(cur){
            if(!cur->left){
                res.push_back(cur->val);
                cur = cur->right;
            }
            else{
                next = cur->left;
                while(next->right){
                    next = next->right;
                }
                next->right = cur;
                TreeNode* tmp = cur;
                cur = cur->left;
                tmp->left = NULL;
            }
        }
        return res;
    }
    */
};
```
# 45、买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1) 
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int minp = INT_MAX;
        for(int i=0;i<prices.size();i++){
            minp=min(minp,prices[i]);
            res = max(res,prices[i]-minp);
        }
        return res;
    }
};
```
# 46、二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

```
   1
  / \
 2   3
```
输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

-10
/ 9  20
/  15   7

输出: 42

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(logn) 
    int maxPathSum(TreeNode* root) {
        int res=INT_MIN;
        help(root,res);
        return res;
    }
    int help(TreeNode* root,int &res){ // 从root向下走的最长距离
        if(!root) return 0;
        int l = max(0, help(root->left,res));
        int r = max(0, help(root->right,res));
        res = max(res,root->val+l+r);
        return root->val+max(l,r);
    }
};
```
# 47、最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n) 
    int longestConsecutive(vector<int>& nums) {
        int res = 0;
        set<int> s(nums.begin(),nums.end());
        set<int>::iterator it;
        for(it = s.begin();it!=s.end();it++){
            int beg = *it;
            if(s.find(beg-1)==s.end()){
                int len = 1;
                while(s.find(beg+1)!=s.end()){
                    len++;
                    beg++;
                }
                res=max(res,len);
            }
        }
        return res;
    }
};
```
# 48、只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1) 
    int singleNumber(vector<int>& nums) {
        int res;
        for(int num:nums) res^=num;
        return res;
    }
};
```
# 49、单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

```
class Solution {
public:
	// 时间复杂度：O(n^2)，空间复杂度：O(n) 
    // dp[i]表示字符串s的前i个字符能否拆分成wordDict
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> flag(s.size()+1,false);
        unordered_set<string> set(wordDict.begin(),wordDict.end());
        flag[0] = true;
        for(int i=1;i<=s.size();i++){
            for(int j=0;j<i;j++){
                if(flag[j] && set.find(s.substr(j,i-j))!=set.end()){
                    flag[i]=true;
                    break;
                }
            }
        }
        return flag[s.size()];
    }
};
```
# 50、环形链表
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：


示例 2：

![](/personal-site-mvp/img/doc-placeholder.svg "")

示例 2：


示例 3：

![](/personal-site-mvp/img/doc-placeholder.svg "")

示例 3：


进阶：

![](/personal-site-mvp/img/doc-placeholder.svg "")

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1) 
    bool hasCycle(ListNode *head) {
        if(!head) return false;
        ListNode * fast = head;
        ListNode * slow = head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow) return true;
        }
        return false;
    }
};
```
# 51、环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。


示例 1：

![](/personal-site-mvp/img/doc-placeholder.svg "")

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：


示例 3：

![](/personal-site-mvp/img/doc-placeholder.svg "")

示例 3：


进阶：
你是否可以不用额外空间解决此题？

![](/personal-site-mvp/img/doc-placeholder.svg "")

进阶：
你是否可以不用额外空间解决此题？

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(1) 
    ListNode *detectCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow = head;
        bool flag = false;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast){
                flag = true;
                break;
            }
        }
        if(flag){
            fast = head;
            while(fast != slow){
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
        return NULL;
    }
};
```
# 52、LRU缓存机制
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

```
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
```
```
class LRUCache {
public:
    LRUCache(int capacity) {
         _capacity =  capacity;
    }
    // 时间复杂度：O(1)，空间复杂度：O(capacity) 
    int get(int key) {
        auto iter = _map.find(key);
        if(iter == _map.end()) return -1;
        int res = iter->second->second;
        _list.erase(iter->second);
        _list.push_front(make_pair(key,res));
        _map[key] = _list.begin();
        return res;
    }
	// 时间复杂度：O(1)，空间复杂度：O(capacity) 
    void put(int key, int value) {
        auto iter = _map.find(key);
        if(iter != _map.end()){
            _list.erase(iter->second);
        }
        _list.push_front(make_pair(key,value));
        _map[key] = _list.begin();
        if(_list.size()>_capacity){
            _map.erase(_list.back().first);
            _list.pop_back();
        }
    }
private:
    unordered_map<int,list<pair<int,int>>::iterator> _map;
    list<pair<int,int>> _list;
    int _capacity;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```
# 53、排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // 时间复杂度：O(nlogn)，空间复杂度：O(1) 
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next && fast->next->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        fast = slow->next;
        slow->next = NULL;
        slow = head;
        ListNode* l1 = sortList(slow);
        ListNode* l2 = sortList(fast);

        //合并有序链表
        ListNode* res = new ListNode(0);
        ListNode* root = res;
        while(l1 && l2){
            if(l1->val < l2->val){
                root->next = l1;
                l1 = l1->next;
            }
            else{
                root->next = l2;
                l2 = l2->next;
            }
            root = root->next;
        }
        root->next = l1?l1:l2;
        return res->next;
    }
};
```
# 54、乘积最大子序列
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(1) 
    int maxProduct(vector<int>& nums) {
        int res = INT_MIN;
        int imax = 1, imin = 1;
        for(int i=0;i<nums.size();i++){
            if(nums[i]<0){
                int tmp = imax;
                imax = imin;
                imin = tmp;
            }
            imax = max(nums[i],imax*nums[i]);
            imin = min(nums[i],imin*nums[i]);

            res = max(res,imax);
        }
        return res;
    }
};
```
# 55、最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```
```
class MinStack {
private:
    stack<int> s;
    stack<int> sMin;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    // 时间复杂度：O(1)，空间复杂度：O(n) 
    void push(int x) {
        if(sMin.empty() || x<=sMin.top()){
            sMin.push(x);
        }
        s.push(x);
    }
    
    void pop() {
        if(!sMin.empty() && sMin.top()==s.top()){
            sMin.pop();
        }
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return sMin.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```
# 56、相交链表
编写一个程序，找到两个单链表相交的起始节点。


在节点 c1 开始相交。

![](/personal-site-mvp/img/doc-placeholder.svg "")

在节点 c1 开始相交。


输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

![](/personal-site-mvp/img/doc-placeholder.svg "")

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

![](/personal-site-mvp/img/doc-placeholder.svg "")

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。


输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

![](/personal-site-mvp/img/doc-placeholder.svg "")

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // 时间复杂度：O(m+n)，空间复杂度：O(1) 
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(!headA || !headB) return NULL;
        ListNode* l1=headA;
        ListNode* l2=headB;
        while(l1!=l2){
            l1 = l1? l1->next:headB;
            l2 = l2? l2->next:headA;
        }
        return l1;
    }
};
```
# 57、多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(1) 
    int majorityElement(vector<int>& nums) {
        int cur = nums[0];
        int time = 0;
        for(int i=0;i<nums.size();i++){
            if(cur==nums[i]){
                time++;
            }
            else{
                time--;
                if(time==0){
                    cur=nums[i];
                    time=1;
                }
            }
        }
        return cur;
    }
};
```
# 58、打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
偷窃到的最高金额 = 2 + 9 + 1 = 12 。

```
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(1) 
    int rob(vector<int>& nums) {
        // f(k)=max(f(k-2)+ak,f(k-1));  f(–1) = f(0) = 0
        int cur=0,pre=0;
        for(int n:nums){
            int tmp = cur;
            cur = max(pre+n,cur);
            pre = tmp;
        }
        return cur;
    }
};
```
# 59、岛屿数量
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

```
class Solution {
public:
	// 时间复杂度：O(n*m)，空间复杂度：最坏O(n*m) 
    int numIslands(vector<vector<char>>& grid) {
        if(grid.empty()) return 0;
        int res = 0;
        int m=grid.size(),n=grid[0].size();
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j] == '1'){
                    res++;
                    dfs(grid,i,j);
                }
            }
        }
        return res;
    }
    void dfs(vector<vector<char>>& grid, int i, int j) {
        grid[i][j]='0';
        int m=grid.size(),n=grid[0].size();
        if(i-1>=0 && grid[i-1][j]=='1') dfs(grid,i-1,j);
        if(i+1<m && grid[i+1][j]=='1') dfs(grid,i+1,j);
        if(j-1>=0 && grid[i][j-1]=='1') dfs(grid,i,j-1);
        if(j+1<n && grid[i][j+1]=='1') dfs(grid,i,j+1);
    }
};
```
# 60、反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // 迭代
    // 时间复杂度：O(n)，空间复杂度：O(1) 
    ListNode* reverseList(ListNode* head) {
        ListNode* res = NULL;
        while(head){
            ListNode* tmp = head->next;
            head->next = res;
            res = head;
            head = tmp;
        }
        return res;
    }
};
```
```
class Solution {
public:
    // 递归
    // 时间复杂度：O(n)，空间复杂度：O(n) 
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode* res = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return res;
    }
};
```
# 61、课程表
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。

```
class Solution {
public:
    // 时间复杂度：O(n+m)节点数量和临边数量，空间复杂度：O(n) 
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> inDegree(numCourses,0);
        vector<vector<int>> list(numCourses,vector<int>());
        for(vector<int> t : prerequisites){
            inDegree[t[0]]++;
            list[t[1]].push_back(t[0]);
        }
        queue<int> queue;
        for(int i=0;i<numCourses;i++){
            if(inDegree[i]==0) queue.push(i);
        }
        vector<int> res;
        while(!queue.empty()){
            int tmp = queue.front();
            queue.pop();
            res.push_back(tmp);
            for(int c : list[tmp]){
                if(--inDegree[c] == 0) queue.push(c);
            } 
        }
        return res.size()==numCourses;
    }
};
```
# 62、实现 Trie (前缀树)
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

```
class Trie {
private:
    bool is_end = false;
    Trie* next[26] = {nullptr};
public:
    /** Initialize your data structure here. */
    Trie() {
        
    }
    // 时间复杂度：O(m)键长，空间复杂度：最坏O(m) 
    /** Inserts a word into the trie. */
    void insert(string word) {
        Trie* root = this;
        for(char c : word){
            if(root->next[c-'a']==nullptr) root->next[c-'a']=new Trie();
            root = root->next[c-'a'];
        }
        root->is_end = true;
    }
    // 时间复杂度：O(m)，空间复杂度：O(1) 
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Trie* root = this;
        for(char c : word){
            if(root->next[c-'a']==nullptr) return false;
            root = root->next[c-'a'];
        }
        return root->is_end;
    }
    // 时间复杂度：O(m)，空间复杂度：O(1) 
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Trie* root = this;
        for(char c : prefix){
            if(root->next[c-'a']==nullptr) return false;
            root = root->next[c-'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```
# 63、数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

```
class Solution {
public:
	// 时间复杂度：O(nlogk)，空间复杂度：O(k) 
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,greater<int>> queue;
        for(int n: nums){
            if(queue.size()<k) queue.push(n);
            else{
                if(n>queue.top()){
                    queue.pop();
                    queue.push(n);
                }
            }          
        }
        return queue.top();
    }
};
```
```
class Solution {
public:
	// 时间复杂度：O(n)最坏O(n^2)，空间复杂度：O(1) 
    int findKthLargest(vector<int>& nums, int k) {
        return quicksort(nums,0,nums.size()-1,k);
    }
    int quicksort(vector<int>& nums, int l, int r, int k){
        int index = part(nums,l,r);
        if(index==nums.size()-k) return nums[index];
        if(index>nums.size()-k) return quicksort(nums,l,index-1,k);
        if(index<nums.size()-k) return quicksort(nums,index+1,r,k);
        return -1;
    }
    int part(vector<int>& nums, int l, int r) {
        int i=l,j=r;
        while(i<j){
            while(nums[j]>=nums[l] && i<j) j--;
            while(nums[i]<=nums[l] && i<j) i++;
            swap(nums[i],nums[j]);
        }
        swap(nums[i],nums[l]);
        return i;
    }
};
```
```
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return quicksort(nums,0,nums.size()-1,k);
    }
    int quicksort(vector<int>& nums, int l, int r, int k){
        if(l<r){   
            int i=l,j=r;
            while(i<j){
                while(nums[j]>=nums[l] && i<j) j--;
                while(nums[i]<=nums[l] && i<j) i++;
                swap(nums[i],nums[j]);
            }
            swap(nums[i],nums[l]);
            if(i==nums.size()-k) return nums[i];
            else if(i<nums.size()-k) return quicksort(nums,i+1,r,k);
            else return quicksort(nums,l,i-1,k);
        }
        return nums[l];
    }
};
```
# 64、最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

```
class Solution {
public:
    // 若某格子值为 1 ，则以此为右下角的正方形的、最大边长
    // 时间复杂度：O(nm)，空间复杂度：O(nm) 
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix.size()?matrix[0].size():0;
        int res = 0;
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(matrix[i-1][j-1]=='1'){
                    dp[i][j]=min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1]))+1;
                    res = max(res,dp[i][j]);
                }
            }
        }
        return res*res;
    }
};
```
# 65、翻转二叉树
翻转一棵二叉树。

示例：

输入：

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```
输出：

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 时间复杂度：O(n)，空间复杂度：O(n) 
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return NULL;
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};
```
# 66、回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n) 
    bool isPalindrome(ListNode* head) {
        if(!head||!head->next) return true;
        ListNode* fast = head;
        ListNode* slow = head;
        stack<int> stack;
        stack.push(head->val);
        while(fast->next && fast->next->next){
            fast=fast->next->next;
            slow= slow->next;
            stack.push(slow->val);
        }
        if(!fast->next) stack.pop();
        while(!stack.empty()){
            slow=slow->next;
            if(slow->val==stack.top()){
                stack.pop();
            }
            else return false;
        }
        return true;
    }
};
```
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1) 
    bool isPalindrome(ListNode* head) {
        if(!head||!head->next) return true;
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* cur = head;
        ListNode* res = NULL;
        while(fast && fast->next){
            fast = fast->next->next;
            cur = slow;
            slow = slow->next;
            cur->next = res;
            res = cur;    
        }
        if(fast) slow = slow->next;
        while(slow){
            if(slow->val!=cur->val){
                return false;
            }
            else{
                slow=slow->next;
                cur=cur->next;
            }
        }
        return true;
    }
};
```
# 67、二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


示例 1:

![](/personal-site-mvp/img/doc-placeholder.svg "")

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n) 
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root) return NULL;
        if(root==p || root==q) return root;
        TreeNode* l = lowestCommonAncestor(root->left,p,q);
        TreeNode* r = lowestCommonAncestor(root->right,p,q);
        if(l&&r) return root;
        if(l)return l;
        if(r) return r;
        return NULL;
    }
};
```
# 68、除自身以外数组的乘积
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1) 
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size());
        int l=1;
        for(int i=0;i<nums.size();i++){
            res[i] = l;
            l *= nums[i];
        }
        l=1;
        for(int i=nums.size()-1;i>=0;i--){
            res[i] *= l;
            l *= nums[i];
        }
        return res;
    }
};
```
# 69、滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

```
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```
提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

进阶：

你能在线性时间复杂度内解决此题吗？

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(n) 
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        deque<int> q;
        for(int i=0;i<nums.size();i++){
            while(!q.empty() && nums[q.back()]<nums[i]){
                q.pop_back();
            }
            q.push_back(i);
            if(!q.empty() && q.front()==i-k) q.pop_front();
            if(k && i+1>=k) res.push_back(nums[q.front()]);
        }
        return res;
    }
};
```
# 70、搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
[1,   4,  7, 11, 15],
[2,   5,  8, 12, 19],
[3,   6,  9, 16, 22],
[10, 13, 14, 17, 24],
[18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

```
class Solution {
public:
	// 时间复杂度：O(n+m)，空间复杂度：O(1) 
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty()) return false;
        int i = matrix.size()-1, j = 0;
        while(i>=0 && j<matrix[0].size()){
            if(matrix[i][j] == target) return true;
            if(matrix[i][j] > target) i--;
            else j++;
        }
        return false;
    }
};
```
# 71、会议室 II
没会员 题没法看

# 72、完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

```
class Solution {
public:
	// 时间复杂度：O(n*sqrt(n))，空间复杂度：O(n) 
    int numSquares(int n) {
        vector<int> res(n+1);
        for(int i=1;i<=n;i++){
            res[i]=i;
            for(int j=1;j*j<=i;j++){
                res[i]=min(res[i],res[i-j*j]+1);
            }
        }
        return res[n];
    }
};
```
# 73、移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1) 
    void moveZeroes(vector<int>& nums) {
        int cur=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=0){
                swap(nums[i],nums[cur++]);
            }
        }
    }
};
```
# 74、寻找重复数
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

```
class Solution {
public:
    // 能更改原数组 见剑指offer 50、数组中重复的数字
    int findDuplicate(vector<int>& nums) {
        int len = nums.size();
        for(int i=0;i<nums.size();i++){
            int cur = nums[i];
            if(cur>=len) cur=cur-len;
            if(nums[cur]>=len){
                return cur;
            }
            nums[cur]+=len;
        }
        return -1;
    }
};
```
```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1) 
    int findDuplicate(vector<int>& nums) {
        int fast=nums[0],slow=nums[0];
        do{
            slow=nums[slow];
            fast=nums[nums[fast]];
        }while(fast!=slow);
        fast=nums[0];
        while(fast!=slow){
            slow=nums[slow];
            fast=nums[fast];
        }
        return slow;
    }
};
```
# 75、二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例:

你可以将以下二叉树：

```
    1
   / \
  2   3
     / \
    4   5
```
序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
   	// 时间复杂度：O(n)，空间复杂度：O(1) 
    string serialize(TreeNode* root) {
       if(!root) return "#_";
       string res=to_string(root->val)+"_"; 
       res += serialize(root->left);
       res += serialize(root->right);
       return res;
    }

    // Decodes your encoded data to tree.
   	// 时间复杂度：O(n)，空间复杂度：O(1) 
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        string str;
        queue<string> q;
        while(getline(ss,str,'_')) q.push(str);
        return help(q);
    }
    TreeNode* help(queue<string> &q) {
        string val=q.front();
        q.pop();
        if(val=="#") return NULL;
        TreeNode* node = new TreeNode(stoi(val));
        node->left = help(q);
        node->right = help(q);
        return node;
    }   
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```
# 76、最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

```
class Solution {
public:
   	// 时间复杂度：O(n^2)，空间复杂度：O(n) 
    int lengthOfLIS(vector<int>& nums) {
        if(nums.empty()) return 0;
        int res = 0;
        vector<int> dp(nums.size(),1);
        // dp[i]的值代表以nums[i]结尾的最长子序列长度
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j]){
                    dp[i]=max(dp[i],dp[j]+1);
                }
            }
            res = max(res,dp[i]);
        }
        return res;
    }
};
```
```
class Solution {
public:
    // 时间复杂度：O(nlogn)，空间复杂度：O(n) 
    int lengthOfLIS(vector<int>& nums) {
        if(nums.empty()) return 0;
        vector<int> tail;
        for(int n:nums){
            if(tail.empty()||n>tail.back()){
                tail.push_back(n);
            }
            else{
                int l=0,r=tail.size();
                while(l<r){
                    int m=(l+r)/2;
                    if(tail[m]<n) l=m+1;
                    else r=m;
                }
                tail[l]=n;
            }
        }
        return tail.size();
    }
};
```
# 77、删除无效的括号
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]

```
class Solution {
public:
	// 时间复杂度：O(2^n)，空间复杂度：O(n) 
    vector<string> removeInvalidParentheses(string s) {
        vector<string> res;
        int left=0,right=0;
        for(char c:s){
            if(c=='(') 
                left++;
            if(c==')'){
                if(left>0) left--;
                else right++;
            }
        }
        dfs(s,0,left,right,res);
        return res;
    }
    void dfs(string s, int n, int l, int r, vector<string> &res){
        if(l==0 && r==0){
            if(isok(s)) res.push_back(s);
            return;
        }
        for(int i=n;i<s.size();i++){
            if(i-1>=n&&s[i]==s[i-1]) continue;
            if(l>0&&s[i]=='(')
                dfs(s.substr(0,i)+s.substr(i+1,s.size()-1-i),i,l-1,r,res);
            if(r>0&&s[i]==')')
                dfs(s.substr(0,i)+s.substr(i+1,s.size()-1-i),i,l,r-1,res);
        }
    }
    bool isok(string s){
        int left=0;
        for(char c:s){
            if(c=='(') 
                left++;
            if(c==')'){
                left--;
                if(left<0) return false;
            }
        }
        return left==0;
    }
};
```
# 78、最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

```
class Solution {
public:
	// 时间复杂度：O(n)，空间复杂度：O(1) 
    int maxProfit(vector<int>& prices) {
        int dp0=0,dp1=INT_MIN,pre=0;
        for(int i=0;i<prices.size();i++){
            int t=dp0;
            dp0=max(dp0,dp1+prices[i]);
            dp1=max(dp1,pre-prices[i]);
            pre=t;
        }
        return dp0;
    }
};
```
```
// 股票买卖问题总结

// 状态转移方程：
// dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
// dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

// 第一题 只进行一次交易，相当于 k = 1
int maxProfit_k_1(vector<int>& prices) {
    int dp_i_0 = 0, dp_i_1 = INT_MIN;
    for (int i = 0; i < prices.size(); i++) {
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = max(dp_i_1, -prices[i]);
    }
    return dp_i_0;
}

// 第二题 不限交易次数，相当于 k = +infinity（正无穷）
int maxProfit_k_inf(vector<int>& prices) {
    int dp_i_0 = 0, dp_i_1 = INT_MIN;
    for (int i = 0; i < prices.size(); i++) {
    	int tmp = dp_i_0;
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = max(dp_i_1, tmp - prices[i]);
    }
    return dp_i_0;
}

// 第三题 不限交易次数，有冷却一天，k = +infinity 
int maxProfit_with_cd(vector<int>& prices) {
    int dp_i_0 = 0, dp_i_1 = INT_MIN, dp_pre_0 = 0;
    for (int i = 0; i < prices.size(); i++) {
    	int tmp = dp_i_0;
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i]);
        // 第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1
        dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i]);
        dp_pre_0 = tmp;
    }
    return dp_i_0;
}

// 第四题 不限交易次数，有手续费 fee，k = +infinity 
int maxProfit_with_fee(vector<int>& prices, int fee) {
    int dp_i_0 = 0, dp_i_1 = INT_MIN;
    for (int i = 0; i < prices.size(); i++) {
    	int tmp = dp_i_0;
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = max(dp_i_1, tmp - prices[i]-fee);
    }
    return dp_i_0;
}

// 第五题 限交易次数2次，相当于 k = 2
int maxProfit_k_2(vector<int>& prices) {
    int n = prices.size(), k = 2;
    int dp[k+1][2];
    dp[0][0] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = k; j > 0; j--) {
            if (i == 0) { 
                dp[j][0] = 0;
                dp[j][1] = -prices[i];
            }
            else{
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i]);
                dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i]);
            }
        }
    }
    return dp[k][0];
}
int maxProfit_k_2(vector<int>& prices) {
    int dp_i10 = 0, dp_i11 = INT_MIN;
    int dp_i20 = 0, dp_i21 = INT_MIN;
    for (int price : prices) {
        dp_i20 = max(dp_i20, dp_i21 + price);
        dp_i21 = max(dp_i21, dp_i10 - price);
        dp_i10 = max(dp_i10, dp_i11 + price);
        dp_i11 = max(dp_i11, -price);
    }
    return dp_i20;
}

// 第六题 限交易次数n次，相当于 k = n
int maxProfit_k_n(int k, vector<int>& prices) {
    int n = prices.size();
    if (k > n / 2) 
        return maxProfit_k_inf(prices); // 相当于 k = +infinity

    int dp[k+1][2];
    dp[0][0] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = k; j > 0; j--) {
            if (i == 0) { 
                dp[j][0] = 0;
                dp[j][1] = -prices[i];
            }
            else{
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i]);
                dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i]);
            }
        }
    }
    return dp[k][0];
}
```
# 79、戳气球
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

```
输入: [3,1,5,8]
输出: 167 
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```
```
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(),1);
        nums.push_back(1);
        int n = nums.size();
        vector<vector<int>> dp(n,vector<int>(n));
        // dp[i][j] 表示戳破 [i+1...j-1] 号气球的最大收益
        // 假设 k 号气球（i+1 <= k <= j-1）是 [i+1...j-1] 中最后一个被戳破的
        for(int len=2;len<n;len++){
            for(int i=0;i+len<n;i++){
                int j=i+len;
                for(int k=i+1;k<j;k++){
                    dp[i][j]=max(dp[i][j],nums[i]*nums[k]*nums[j]+dp[i][k]+dp[k][j]);
                }
            }
        }
        return dp[0][n-1];
    }
};
```
# 80、零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

```
class Solution {
public:
	// 时间复杂度：O(nS)，空间复杂度：O(S) S 是金额，n 是面额数
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1,amount+1);
        dp[0]=0;
        for(int i=1;i<=amount;i++){
            for(int c:coins){
                if(i>=c) dp[i] = min(dp[i],dp[i-c]+1);
            }
        }
        return dp[amount]==amount+1?-1:dp[amount];
    }
};
```
# 81、打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

```
     3
    / \
   2   3
    \   \ 
     3   1
```
输出: 7

解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

```
     3
    / \
   4   5
  / \   \ 
 1   3   1
```
输出: 9

解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map<TreeNode*,int> map;
    int rob(TreeNode* root) {
        return help(root);
    }
    int help(TreeNode* root) {
        if(!root) return 0;
        if(map.count(root)) return map[root];
        int res = root->val;
        if(root->left) res+=help(root->left->left)+help(root->left->right);
        if(root->right) res+=help(root->right->left)+help(root->right->right);
        res = max(res,help(root->left)+help(root->right));
        map[root] = res;
        return res;
    }
};
```
# 82、比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

```
class Solution {
public:
    // i & (i - 1)可以去掉i最右边的一个1
    vector<int> countBits(int num) {
        vector<int> res(num+1,0);
        int i=1;
        while(i<=num){
            res[i]=res[i&(i-1)]+1;
            i++;
        }
        return res;
    }
};
```
```
class Solution {
public:
    // i >> 1会把最低位去掉
    vector<int> countBits(int num) {
        vector<int> res(num+1,0);
        int i=1;
        while(i<=num){
            res[i]=res[i>>1]+(i&1);
            i++;
        }
        return res;
    }
};
```
# 83、前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

```
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res(k);
        unordered_map<int,int> map;
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> q;
        for(int n:nums) map[n]++;
        for(auto p:map){
            if(q.size()==k){
                if(q.top().first>p.second) continue;
                q.pop();
            }
            q.push(make_pair(p.second,p.first));
        }
        int index=k-1;
        while(!q.empty()){
            res[index]=q.top().second;
            q.pop();
            index--;
        }
        return res;
    }
};
```
# 84、字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

```
class Solution {
public:
    string decodeString(string s) {
        string res;
        stack<pair<int,string>> stack;
        int times=0;
        for(char c:s){
            if(c>='0'&&c<='9') times=10*times+(c-'0');
            else if(c>='a'&&c<='z'||c>='A'&&c<='Z') res+=c;
            else if(c=='['){
                stack.push(make_pair(times,res));
                times=0;
                res.clear();
            }
            else if(c==']'){
                string t = res;
                for(int i=1;i<stack.top().first;i++) res+=t;
                res=stack.top().second+res;
                stack.pop();
            }
        }
        return res;
    }
};
```
# 85、除法求值
给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为: vector<pair<string, string>> equations, vector& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector类型。

基于上述例子，输入如下：

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。

```

```
