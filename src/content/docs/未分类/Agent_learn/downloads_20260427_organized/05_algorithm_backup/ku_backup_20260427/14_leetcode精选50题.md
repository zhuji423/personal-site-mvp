---
title: "1、两数相加"
description: "leetcode 精选50题"
date: "2026-04-27"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\05_algorithm_backup\\ku_backup_20260427\\14_leetcode精选50题.md"
---
leetcode 精选50题

# 1、两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(0);
        ListNode* head = res;
        int flag = 0;
        while(l1 || l2){
            int x = l1?l1->val:0;
            int y = l2?l2->val:0;
            head->next = new ListNode((x+y+flag)%10);
            flag = x+y+flag>9?1:0;
            if(l1) l1= l1->next;
            if(l2) l2 = l2->next;
            head = head->next;                         
        }
        if(flag) head->next = new ListNode(1);
        return res->next;
    }
};

```
# 2、寻找两个有序数组的中位数
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
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        if(m > n) return findMedianSortedArrays(nums2, nums1); //保证nums1更短
        int lMax1,rMin1,lMax2,rMin2,c1,c2,low=0,high=2*m;
        while(low <= high){
            c1 = (low + high)/2;
            c2 = m + n - c1;
            lMax1 = c1==0? INT_MIN:nums1[(c1-1)/2];
            rMin1 = c1==2*m? INT_MAX:nums1[c1/2];
            lMax2 = c2==0? INT_MIN:nums2[(c2-1)/2];
            rMin2 = c2==2*n? INT_MAX:nums2[c2/2];
            if(lMax1 > rMin2) high=c1-1;
            else if(lMax2 > rMin1) low=c1+1;
            else break;
        }
        return (max(lMax1,lMax2)+min(rMin1,rMin2))/2.0;
    }
};
```
# 3、最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

输入: "cbbd"
输出: "bb"

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
# 4、整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

输入: 123
输出: 321

输入: -123
输出: -321

输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

```
class Solution {
public:
    int reverse(int x) {
        int res=0;
        while(x!=0){
            if(res>INT_MAX/10 || res==INT_MAX/10 && x%10>7) return 0;
            if(res<INT_MIN/10 || res==INT_MIN/10 && x%10<-8) return 0;
            res=res*10+x%10;
            x=x/10;
        }
        return res;
    }
};
```
# 5、字符串转换整数 (atoi)
请你来实现一个 atoi 函数，使其能将字符串转换成整数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。
说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

输入: "42"
输出: 42

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
因此无法执行有效的转换。

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
因此返回 INT_MIN (−231) 。

```
class Solution {
public:
    int myAtoi(string str) {
        int res = 0;
        bool flag = true;
        int i = 0;
        while(i<str.size() && str[i]==' ') i++;
        if(str[i] == '+'){flag=true;i++;}
        else if(str[i] == '-'){flag=false;i++;}
        for(;i<str.size();i++){
            if(str[i]<='9' && str[i]>='0'){
                if(res>INT_MAX/10 || res==INT_MAX/10&&(str[i]-'0')>7) return flag?INT_MAX:INT_MIN;
                res = res*10+(str[i]-'0');
            }
            else return flag?res:-res;
        }
        return flag?res:-res;
    }
};
```
# 6、回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

输入: 121
输出: true

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

```
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        string s = to_string(x);
        int l=0,r=s.size()-1;
        while(l<=r){
            if(s[l] == s[r]){
                l++;
                r--;
            }
            else return false;
        }
        return true;
    }
};
```
# 7、盛最多水的容器
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

```
class Solution {
public:
    int maxArea(vector<int>& height) {
        int smax = 0;
        int i = 0,j = height.size()-1;
        while(i<=j){
            int s = min(height[i],height[j])*(j-i);
            if(s > smax) smax = s;
            if(height[i]<height[j]) i++;
            else j--;
        }
        return smax;
    }
};
```
# 8、最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入: ["flower","flow","flight"]
输出: "fl"

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

```
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int imin = 0; //最短的字符串
        for(int i=0;i<strs.size();i++){
            if(strs[i].size()<strs[imin].size()) imin = i;
        }
        string res;
        for(int i=0;i<strs[imin].size();i++){
            for(int j=0;j<strs.size();j++){
                if(strs[j][i] != strs[imin][i]) return res;
            }
            res.push_back(strs[imin][i]);
        }
        return res;
    }
};
```
# 9、三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
[-1, 0, 1],
[-1, -1, 2]
]

```
class Solution {
public:
    vector<vector<int> > threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int> > res;
        int add;
        for(int i=0;i<nums.size();i++){
            if(i>0 && nums[i] == nums[i-1]) continue; //i和前面一样，跳过
            if((add = nums[i])>0) break;
            
            int l = i+1, r = nums.size()-1; //双指针，找和为add
            while(l<r){
                if(nums[l]+nums[r]+add>0) r--;
                else if(nums[l]+nums[r]+add<0) l++;
                else {
                    res.push_back({add,nums[l],nums[r]});
                    l++;r--;
                    while(l<r && nums[l] == nums[l-1]) l++;
                    while(l<r && nums[r] == nums[r+1]) r--;
                }
            }  
        }
        return res;
    }
};
```
# 10、最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

```
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int add = 0,dis = INT_MAX;
        for(int i=0;i<nums.size();i++){
            int l = i+1, r = nums.size()-1;
            while(l<r){
                int tadd = nums[i]+nums[l]+nums[r];
                if(tadd == target) return tadd;
                int tdis = abs(tadd-target);
                if(tdis < dis){
                    add = tadd;
                    dis = tdis;
                }
                if(tadd < target) l++;
                else r--;
            }
        }
        return add;
    }
};
```
# 11、有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

输入: "()"
输出: true

输入: "()[]{}"
输出: true

输入: "(]"
输出: false

输入: "([)]"
输出: false

输入: "{[]}"
输出: true

```
class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for(int i=0;i<s.size();i++){
            if(!stack.empty() && check(stack.top(),s[i])) stack.pop();
            else stack.push(s[i]);
        }
        return stack.empty();
    }
    
    bool check(char a,char b) {
        return a=='('&&b==')' || a=='['&&b==']' || a=='{'&&b=='}';
    }
};
```
# 12、合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4···c

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(0);
        ListNode* head = res;
        while(l1 && l2){
            if(l1->val < l2->val){
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
# 13、合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

输入:
[
1->4->5,
1->3->4,
2->6
]
输出: 1->1->2->3->4->4->5->6

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* list = NULL;
        for(int i=0;i<lists.size();i++){
            list = merge2Lists(list,lists[i]);
        }
        return list; 
    }
    
    ListNode* merge2Lists(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(0);
        ListNode* head = res;
        while(l1 && l2){
            if(l1->val < l2->val){
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
# 14、删除排序数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.empty()) return 0;
        int i = 0; //双指针
        for(int j=1;j<nums.size();j++){
            if(nums[i] != nums[j]){
                i++;
                nums[i]=nums[j];
            }
        }
        return i+1;
    }
};
```
# 15、搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

```
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return helper(nums,target,0,nums.size()-1);
    }
    
    int helper(vector<int>& nums, int target, int i, int j) {
        if(i>j) return -1;
        int mid = (i+j)/2;
        if(nums[mid] == target) return mid;
        if(nums[mid] < nums[j]){ //7 8 1 2 3 4  旋转点在左，右顺序
            if(nums[mid] < target && target <= nums[j]) return helper(nums,target,mid+1,j);
            else return helper(nums,target,i,mid-1);
        }
        else{ //3 4 7 8 1 2  旋转点在右，左顺序
            if(nums[mid] > target && target >= nums[i]) return helper(nums,target,i,mid-1);
            else return helper(nums,target,mid+1,j);
        }
    }
};
```
# 16、字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

输入: num1 = "2", num2 = "3"
输出: "6"

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

```
class Solution {
public:
    string multiply(string num1, string num2) {
        int len1 = num1.size(),len2 = num2.size();
        string res(len1+len2,'0');
        for(int i=len1-1;i>=0;i--){
            for(int j=len2-1;j>=0;j--){
                int t = (res[i+j+1]-'0')+(num1[i]-'0')*(num2[j]-'0');
                res[i+j+1] = t%10 +'0';
                res[i+j] += t/10;
            }
        }
        for(int i=0;i<len1+len2;i++){
            if(res[i] != '0') return res.substr(i);
        }
        return "0";
    }
};
```
# 17、全排列
给定一个没有重复数字的序列，返回其所有可能的全排列。

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
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        backtrack(nums,res,0);
        return res;
    }
    void backtrack(vector<int> &nums,vector<vector<int>> &res,int n) {
        if(n == nums.size()-1) res.push_back(nums);
        else{
            for(int i=n;i<nums.size();i++){
                swap(nums[i],nums[n]);
                backtrack(nums,res,n+1);
                swap(nums[i],nums[n]);
            }
        }
    }
};

//剑指offer 27题 字典序输出有重复字符串序列的全排列
/*
 问题转换为先固定第一个字符，求剩余字符的排列
 再把第一个字符与后面每一个字符交换，并同样递归获得首位后面的字符串组合
 a b b c:
 a+f(bbc),b+f(abc),c+f(cbba); 遍历出所有可能出现在第一个位置的字符
 f(bbc)=b+f(bc),c+f(bb);
 f(bc)=b+f(c),c+f(b);
 f(c)=c;
class Solution {
public:
    vector<string> Permutation(string str) {
        vector<string> res;
        helper(str,res,0);
        sort(res.begin(),res.end());
        return res;
    }
    void helper(string s, vector<string> &res, int n) {
        if(n == s.size()-1){ //终止条件
            if(find(res.begin(),res.end(),s) == res.end()) res.push_back(s);
        }
        else{
            for(int i=n;i<s.size();i++){
                swap(s[i],s[n]);
                helper(s,n+1);
                swap(s[i],s[n]);
            }
        }
    }
    void swap(char &i ,char &j) {
        char t = i; i = j; j = t;
    }
};

*/
```
# 18、最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

```
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = nums[0];
        int add = 0;
        for(int i=0;i<nums.size();i++){
            add += nums[i];
            if(add > max) max = add;
            if(add < 0) add = 0;
        }
        return max;
    }
};
```
# 19、螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

输入:
[
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

输入:
[
[1, 2, 3, 4],
[5, 6, 7, 8],
[9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

```
class Solution {
public:
    /*
       m   n
     i 1 2 3
       4 5 6
     j 7 8 9
    */
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(matrix.empty() || matrix[0].empty()) return {};
        vector<int> res;
        int i=0,j=matrix.size()-1,m=0,n=matrix[0].size()-1;
        while(i<=j && m<=n){
            for(int k=m;k<=n;k++) res.push_back(matrix[i][k]);
            i++;
            if(i>j) break;
            for(int k=i;k<=j;k++) res.push_back(matrix[k][n]);
            n--;
            if(m>n) break;
            for(int k=n;k>=m;k--) res.push_back(matrix[j][k]);
            j--;
            if(i>j) break;
            for(int k=j;k>=i;k--) res.push_back(matrix[k][m]);
            m++;
        }
        return res;
    }
};
```
# 20、螺旋矩阵 II
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

输入: 3
输出:
[
[ 1, 2, 3 ],
[ 8, 9, 4 ],
[ 7, 6, 5 ]
]

```
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> arr(n,vector<int>(n,0));
        int c = 1,k = 0;
        while(c<=n*n){
            for(int i=k;i<n-k;i++) arr[k][i]=c++;
            for(int i=k+1;i<n-k;i++) arr[i][n-k-1]=c++;
            for(int i=n-k-2;i>=k;i--) arr[n-k-1][i]=c++;
            for(int i=n-k-2;i>=k+1;i--) arr[i][k]=c++;
            k++;
        }
        return arr;
    }
};
```
# 21、旋转链表
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

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
    ListNode* rotateRight(ListNode* head, int k) { //1->2->3->4->5->NULL, k = 2
        if(k==0 || !head) return head;
        int len = getlen(head);
        if((k = k%len)==0) return head;
        ListNode* cur = head; // 1->2->3->NULL
        for(int i=0;i<len-k-1;i++){
            cur = cur->next;
        }
        ListNode* last = cur->next; //4->5->NULL
        cur->next = NULL;
        cur = last;
        while(cur->next){
            cur = cur->next;
        }
        cur->next = head; //4->5->1->2->3->NULL
        return last; 
    }
    
    int getlen(ListNode* head){
        int res = 0;
        while(head){
            res++;
            head = head->next;
        }
        return res;
    }
};

```
# 22、不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
例如，上图是一个7 x 3 的网格。有多少可能的路径？
说明：m 和 n 的值均不超过 100。

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。

1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

输入: m = 7, n = 3
输出: 28

```
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m,vector<int>(n,0));//m*n零矩阵
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(i==0 || j==0) dp[i][j]=1;
                else dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```
# 23、爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。

1. 1 阶 + 1 阶
2. 2 阶

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。

1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

```
//当n=45时，结果已经超出了返回值类型int有效范围无法通过，不知道测试怎么回事，同剑指offer 8，剑指可通过
class Solution {
public:
    int climbStairs(int n) {
        int i=1,j=1;
        while(n > 0){
            int t = i;
            i = j;
            j = t+j;
            n--;
        }
        return i;
    }
};
```
# 24、子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

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
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        int l = 1 << nums.size();
        for(int i=0;i<l;i++){
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
# 25、合并两个有序数组
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]

```
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1,j=n-1,cur=n+m-1;
        while(i>=0 && j>=0){
            if(nums1[i]<nums2[j]){
                nums1[cur]=nums2[j];
                j--;
            }else{
                nums1[cur]=nums1[i];
                i--;
            }
            cur--;
        }
        while(i>=0){
            nums1[cur]=nums1[i];i--;cur--;
        }
        while(j>=0){
            nums1[cur]=nums2[j];j--;cur--;
        } 
    }
};
```
# 26、格雷编码
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。
00 - 0
10 - 2
11 - 3
01 - 1

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
因此，当 n = 0 时，其格雷编码序列为 [0]。

```
class Solution {
public:
/*n: 0   1   2   3
     0   0  00  000
         1  10  100
                010
            01  110
            11
                001
                101
                011
                111
*/
    vector<int> grayCode(int n) {
        if(n==0) return {0};
        vector<int> res{0,1};
        for(int i=1;i<n;i++){
            for(int j=0;j<res.size();j++){
                res[j]*=2; //末位加0
            }
            for(int j=res.size()-1;j>=0;j--){
                res.push_back(res[j]+1); //末位加1
            }
        }
        return res;
    }
};
```
# 27、二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

给定二叉树 [3,9,20,null,null,15,7]，
3
/ 9  20
/  15   7
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
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
};
```
# 28、买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        for(int i=0;i<prices.size();i++){  
            for(int j=i+1;j<prices.size();j++){ 
                if(prices[j]-prices[i]>max){
                    max = prices[j]-prices[i];
                }
            }   
        }
        return max;
    }
};
```
# 29、买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()) return 0;
        int max = 0;
        for(int i=0;i<prices.size()-1;i++){
            if(prices[i+1]>prices[i]) max += prices[i+1]-prices[i];
        }
        return max;
    }
};
```
# 30、二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

输入: [1,2,3]
1
/ 2   3
输出: 6

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
    int res = INT_MIN;
    int maxPathSum(TreeNode* root) {
        submax(root);
        return res;
    }
    int submax(TreeNode* root) { //从root向下走的最长距离
        if(!root) return 0;
        int l = max(0,submax(root->left));
        int r = max(0,submax(root->right));
        if(root->val+l+r > res) res=root->val+l+r;
        return root->val+max(l,r);
    }
};
```
# 31、只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

输入: [2,2,1]
输出: 1

输入: [4,1,2,1,2]
输出: 4

```
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for(int i=0;i<nums.size();i++){
            res ^= nums[i];
        }
        return res;
    }
};
```
# 32、环形链表
给定一个链表，判断链表中是否有环。

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
    bool hasCycle(ListNode *head) {
        if(!head) return false;
        ListNode *fast = head;
        ListNode *slow = head;
        while(fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast) return true;
        }
        return false;
    }
};
```
# 33、环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。

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
    ListNode *detectCycle(ListNode *head) {
        if(!head) return NULL;
        bool loop = false;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next&&fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast){
                loop = true;
                break;
            }
        }
        if(loop){
            ListNode* res = head;
            while(res!=slow){
                res = res->next;
                slow = slow->next;
            }
            return res;
        }
        return NULL;
    }
};
```
# 34、LRU缓存机制
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？

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
class LRUCache {
public:
    LRUCache(int capacity) {
        _cap = capacity;
    }
    
    int get(int key) {
        auto iter = _map.find(key);
        if(iter == _map.end()) return -1;
        int res = iter->second->second;
        _list.erase(iter->second);
        _list.push_front(make_pair(key,res));
        _map[key] = _list.begin();
        return res;
    }
    
    void put(int key, int value) {
        auto iter = _map.find(key);
        if(iter != _map.end()) _list.erase(iter->second);
        _list.push_front(make_pair(key,value));
        _map[key] = _list.begin();
        if(_list.size()>_cap){
            int t = _list.back().first;
            _map.erase(t);
            _list.pop_back();
        }   
    }
private:
    unordered_map<int,list<pair<int,int>>::iterator> _map;
    list<pair<int,int>> _list;
    int _cap;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```
# 35、排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

输入: 4->2->1->3
输出: 1->2->3->4

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
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* bk = slow->next;
        slow->next = NULL;
        ListNode* l1 = sortList(head);
        ListNode* l2 = sortList(bk);
        //合并有序链表
        ListNode* res = new ListNode(0);
        ListNode* h = res;
        while(l1 && l2){
            if(l1->val>l2->val){
                h->next = l2;
                l2 = l2->next;
            }
            else{
                h->next = l1;
                l1 = l1->next;
            }
            h = h->next;
        }
        h->next = l1?l1:l2;
        return res->next;
    }
};
```
# 36、最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

```
class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        if(smin.empty() || x <= smin.top()) smin.push(x);
        s.push(x);
    }
    
    void pop() {
        if(smin.top() == s.top()) smin.pop();
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return smin.top();
    }
private:
    stack<int> s;
    stack<int> smin;
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
# 37、相交链表
编写一个程序，找到两个单链表相交的起始节点。

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int len1 = getlen(headA);
        int len2 = getlen(headB);
        int step = abs(len1-len2);
        while(step!=0){
            if(len1>len2) headA = headA->next;
            else headB = headB->next;
            step--;
        }
        while(headA){
            if(headA == headB) return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }
    int getlen(ListNode* l) {
        int res = 0;
        while(l){
            res++;
            l = l->next;
        }
        return res;
    }
};
```
# 38、求众数
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。

输入: [3,2,3]
输出: 3

输入: [2,2,1,1,1,2,2]
输出: 2

```
class Solution {
public:
    /*
     如果重复的次数超过一半的话，一定有相邻的数字相同这种情况的
     对数组同时去掉两个不同的数字，到最后剩下的一个数就是该数字
    */
    int majorityElement(vector<int>& nums) {
        int res = nums[0];
        int count = 1;
        for(int i=1;i<nums.size();i++){
            if(nums[i] == res) count++;
            else{
                count--;
                if(count == 0){
                    res = nums[i];
                    count = 1;
                }
            }
        }
        return res;
    }
};
```
# 39、反转链表
反转一个单链表。

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

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
    ListNode* reverseList(ListNode* head) {
        ListNode* res = NULL;
        while(head){
            ListNode* tmp = new ListNode(head->val);
            tmp->next = res;
            res = tmp;
            head = head->next;
        }
        return res;
    }
};
```
# 40、数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

```
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue <int,vector<int>,greater<int>> q;
        for(int i=0;i<nums.size();i++){
            if(q.size()==k){
                if(q.top()<nums[i]){
                    q.pop();
                    q.push(nums[i]);
                }
            }
            else{
                q.push(nums[i]);
            }
        }
        return q.top();
    }
};
```
# 41、存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

输入: [1,2,3,1]
输出: true

输入: [1,2,3,4]
输出: false

```
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> m;
        for(int i=0;i<nums.size();i++){
            if(m.find(nums[i]) != m.end()) return true;
            else m[nums[i]] = 1;
        }
        return false;
    }
};
```
# 42、二叉搜索树中第K小的元素
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

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
    int res;
    int cur = 0;
    int kthSmallest(TreeNode* root, int k) {
        midfor(root, k);
        return res;
    }
    void midfor(TreeNode* root, int k) {
        if(!root) return;
        if(cur != k) midfor(root->left,k);
        cur++;
        if(cur == k){
            res = root->val;
        }
        if(cur != k) midfor(root->right,k);
    }
};
```
# 43、2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

```
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0) return false;
        while(n!=1){
            double t = n/2.0;
            if(!isint(t)) return false;
            n /= 2;
        }
        return true;
    }
    bool isint(double d){
        return abs(d-(int)d)<1e-5;
    }
};
```
# 44、 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。

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
    TreeNode* res;
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        search(root,p,q);
        return res;
    }
    void search(TreeNode* root, TreeNode* p, TreeNode* q) {
        if((root->val-p->val)*(root->val-q->val)<=0) res = root;
        else if(p->val > root->val && q->val > root->val) search(root->right,p,q);
        else search(root->left,p,q);
    }
};
```
# 45、二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root) return NULL;
        if(root == p || root == q) return root;
        TreeNode* l = lowestCommonAncestor(root->left,p,q);
        TreeNode* r = lowestCommonAncestor(root->right,p,q);
        if(l&&r) return root;
        if(l) return l;
        if(r) return r;
        return NULL;
    }
};
```
# 46、删除链表中的节点
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
现有一个链表 -- head = [4,5,1,9]，它可以表示为:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

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
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```
# 47、除自身以外数组的乘积
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

```
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int l=1, r=1;
        vector<int> res(nums.size());
        for(int i=0;i<nums.size();i++){
            res[i] = l;
            l *= nums[i];
        }
        for(int i=nums.size()-1;i>=0;i--){
            res[i] *= r;
            r *= nums[i];
        }
        return res;
    }
};
```
# 48、Nim 游戏
你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。
你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。

输入: 4
输出: false
解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。

```
class Solution {
public:
    bool canWinNim(int n) {
        return !(n%4==0);
    }
};
```
# 49、反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]·

```
class Solution {
public:
    void reverseString(vector<char>& s) {
        int i=0,j=s.size()-1;
        while(i<j){
            swap(s[i],s[j]);
            i++;j--;
        }
    }
};
```
# 50、反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

```
class Solution {
public:
    string reverseWords(string s) {
        string res;
        stack<char> stack;
        for(int i=0;i<s.size();i++){
            if(s[i] == ' '){
                while(!stack.empty()){
                    res.push_back(stack.top());
                    stack.pop();
                }
                res.push_back(' ');
            }
            else{
                stack.push(s[i]);
            }
        }
        while(!stack.empty()){
            res.push_back(stack.top());
            stack.pop();
        }
        return res;
    }
};
```
