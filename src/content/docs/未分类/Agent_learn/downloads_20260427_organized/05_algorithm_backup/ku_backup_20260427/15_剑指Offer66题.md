---
title: "1、二维数组中的查找"
description: "剑指Offer 66题"
date: "2026-04-27"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\05_algorithm_backup\\ku_backup_20260427\\15_剑指Offer66题.md"
---
剑指Offer 66题

# 1、二维数组中的查找
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

```
/* 
 3 4 5
 4 5 6
 6 7 8
 从左下角开始查找，当target比左下角数字大时，右移；小时，上移
*/
class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int rows = array.size(), cols = array[0].size();
        int i = rows - 1, j = 0;
        while(i>=0&&j<cols){
            if(array[i][j] == target) return true;
            else if(array[i][j] > target) i--;
            else j++;
        }
        return false;
    }
};
```
# 2、替换空格
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

```
/*
 从前往后替换，后面的字符要多次移动，效率低下
 从后往前，先计算需要多少空间，每个字符只移动一次，效率更高
 例如：a b c
 从后往前，当前第i位为'c'（非空格），前有n个空格，则i+2*n位为c
 当前第i位为' '（空格）,前有n个空格，则i+2*n位为%，i+2*n+1位为2，i+2*n+2位为0
*/
class Solution {
public:
	void replaceSpace(char *str,int length) {
        int sum = 0;
        for(int i=0;i<length;i++){
            if(str[i] == ' ') sum++;
        }
        for(int i=length-1;i>=0;i--){
            if(str[i] != ' ') str[i + 2*sum] = str[i];
            else{
                sum--;
                str[i + 2*sum] = '%';
                str[i + 2*sum + 1] = '2';
                str[i + 2*sum + 2] = '0';
            }
        }
    }
};
```
# 3、从尾到头打印链表
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

```
/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> res;
        stack<int> stack;
        while(head){
            stack.push(head->val);
            head = head->next;
        }
        while(!stack.empty()){
            res.push_back(stack.top());
            stack.pop();
        }
        return res;
    }
};
```
# 4、重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

```
/*
 前序遍历序列{1,2,4,7,3,5,6,8} 1是根元素
 中序遍历序列{4,7,2,1,5,3,8,6} 1之前4,7,2是左子树中序，之后5,3,8,6是右子树中序
 前序中1后的3个是左子树前序，之后是右子树前序
 问题转换为根元素已知，求左子树和右子树的重建二叉树，进行递归
*/
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        return buildtree(pre,vin,0,pre.size()-1,0,vin.size()-1);
    }
    
    TreeNode* buildtree(vector<int> pre,vector<int> vin,int pl,int pr,int vl,int vr) {
        if(pl > pr || vl > vr) return NULL;
        TreeNode* root = new TreeNode(pre[pl]);
        int i;
        for(i=vl;i<=vr;i++){
            if(vin[i] == pre[pl]) break;
        }
        int num = i - vl; //左子树个数
        root->left =  buildtree(pre,vin,pl+1,pl+num,vl,vl+num-1);
        root->right =  buildtree(pre,vin,pl+num+1,pr,vl+num+1,vr);
        return root;
    }
};
```
# 5、用两个栈实现队列
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

```
/*
 用两个栈实现一个队列的功能
 入队：将元素进栈A
 出队：判断栈B是否为空，如果为空，则将栈A中所有元素pop，并push进栈B，栈B出栈；
 如果不为空，栈B直接出栈。
 
 用两个队列实现一个栈的功能
 入栈：将元素进队列A
 出栈：判断队列A中元素的个数是否为1，如果等于1，则出队列，否则将队列A中的元素依次出队列并放入队列B，直到队列A中的元素留下一个，然后队列A出队列，再把队列B中的元素出队列以此放入队列A中。
*/
class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        if(stack2.empty()){
            while(!stack1.empty()){
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        int res = stack2.top();
        stack2.pop();
        return res;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};
```
# 6、旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

```
class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        if(rotateArray.size() == 0) return 0;
        int i = 0, j = rotateArray.size()-1;
        while(i < j){
            int mid = (i + j)/2;
            if(rotateArray[mid] > rotateArray[j]){ 
                i = mid + 1; //3 4 7 8 1 2  旋转点在右，左顺序
            }
            else if(rotateArray[mid] < rotateArray[j]){ 
                j = mid; //7 8 1 2 3 4  旋转点在左，右顺序
            }
            else{ //1 0 1 1 1  或  1 1 1 0 1 顺序部分为常数
                i ++; //或 j --;
            }
        }
        return rotateArray[i];
    }
};
```
# 7、斐波那契数列
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

```
class Solution {
public:
    int Fibonacci(int n) { //0 1 1 2 3 5 …,使用动态规划
        int i = 0, j = 1;
        while(n>0){
            int tmp = j;
            j = i+j;
            i = tmp;
            n--;
        }
        return i;
    }
};
```
# 8、跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

```
/*
 最后一步跳1，有f(n-1)种情况
 最后一步跳2，有f(n-2)种情况
 共f(n)=f(n-1)+f(n-2)，1 1 2 3 5（斐波那契数列）使用动态规划
*/
class Solution {
public:
    int jumpFloor(int number) {
        int i = 1, j = 1;
        while(number>0){
            int tmp = j;
            j = i + j;
            i = tmp;
            number--;
        }
        return i;
    }
};
```
# 9、变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

```
//f(n) = f(1) + f(2) + f(3) +...+ f(n-1) + 1
//1 2 4 8 ...
class Solution {
public:
    int jumpFloorII(int number) {
        vector<int> step;
        while(number>0){
            int sum = 0;
            for(int i=0;i<step.size();i++){
                sum += step[i];
            }
            step.push_back(sum+1); 
            number--;
        }
        return step.back();
    }
};
/*
class Solution {
public:
    int jumpFloorII(int number) {
        int res = 1;
        for(int i=1;i<number;i++){
            res += jumpFloorII(i);
        }
        return res;
    }
};
*/
```
# 10、矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

```
/*
|    | | |   f(n-1)
|    | | |
 
— —    | |   f(n-2)
— —    | |
f(n) = f(n-1) + f(n-2),1 2 3 5 8…,动态规划
*/
class Solution {
public:
    int rectCover(int number) {
        if(number == 0) return 0;
        int i = 1, j = 1;
        while(number>0){
            int tmp = j;
            j = i + j;
            i = tmp;
            number--;
        }
        return i;
    }
};
```
# 11、二进制中1的个数
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

```
/*
 将n与n-1相与会把n的最右边的1变为0，比如
 1100&1011 = 1000
*/
class Solution {
public:
     int  NumberOf1(int n) {
         int res=0;
         while(n!=0){
             res++;
             n = n&(n-1);
         }
         return res;
     }
};

/*
 #include <bitset>
*/
class Solution {
public:
     int  NumberOf1(int n) {
         bitset<32>a(n); //32位的2进制
         return a.count(); //返回1的个数
     }
};
```
# 12、数值的整数次方
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

```
/*
 10^1101 = 10^0001*10^0100*10^1000，即base*1 * base^2 * base^4 * …
 通过&1和>>1来逐位读取1101
*/
class Solution {
public:
    double Power(double base, int exponent) {
        double res = 1;
        int e = abs(exponent);
        while(e!=0){
            if(e&1 == 1){
                res *= base;
            }
            base *= base;
            e = e>>1;
        }
        return exponent>0?res:1/res;
    }
};
```
# 13、调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

```
/*
 要想保证原有次序，则只能顺次移动或相邻交换。
 1.i从左向右遍历，找到第一个偶数。
 2.j从i+1开始向后找，找到第一个奇数。
 3.将[i,...,j-1]的元素整体后移一位，将找到的奇数放入i位置
*/
class Solution {
public:
    void reOrderArray(vector<int> &array) {
        for(int i=0;i<array.size();i++){
            if(array[i]%2 == 0){
                for(int j=i+1;j<array.size();j++){
                    if(array[j]%2 == 1){
                        int tmp = array[j];
                        for(int k=j-1;k>=i;k--){
                            array[k+1] = array[k];
                        }
                        array[i] = tmp;
                        break;
                    }
                }
            }
        }
    }
};
```
# 14、链表中倒数第k个结点
输入一个链表，输出该链表中倒数第k个结点。

```
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
/*
 两指针指向头结点，
 第一个指针走(k-1)步，到k节点
 两个指针同时往后移动，当第一个结点到达末尾的时候，第二个结点所在位置就是倒数第k个节点
*/
class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        ListNode* p1 = pListHead;
        for(int i=0;i<k;i++){
            if(!p1) return NULL;
            p1=p1->next;
        }
        ListNode* p2 = pListHead;
        while(p1){
            p1=p1->next;
            p2=p2->next;
        }
        return p2;
    }
};
```
# 15、反转链表
输入一个链表，反转链表后，输出新链表的表头。

```
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
/*
1 2 3 4 5
遍历链表，当前值为4时，相当于新建值为4的链表node，node->next = 前面链表反转，node即为所求
当前值为5时，相当于新建值为5的链表node，node->next = 上一步的值
*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
        ListNode* res = NULL;
        while(pHead){
            ListNode* tmp = new ListNode(pHead->val);
            tmp -> next = res;
            res = tmp;
            pHead = pHead -> next;
        }
        return res;
    }
};

//原地修改
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
        ListNode* res = NULL;
        while(pHead){
            ListNode* tmp = pHead->next;
            pHead->next = res;
            res = pHead;
            pHead = tmp;
        }
        return res;
    }
};

```
# 16、合并两个排序的链表
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

```
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        ListNode* res = new ListNode(0);//初始化，取几不重要
        ListNode* here = res; //标记位置
        while(pHead1 && pHead2){
            if(pHead1->val < pHead2->val){
                res -> next = pHead1;
                pHead1 = pHead1 -> next;
            }
            else{
                res -> next = pHead2;
                pHead2 = pHead2 -> next;
            }
            res = res -> next;
        }
        res -> next = pHead1 ? pHead1:pHead2;
        return here->next;
    }
};
```
# 17、树的子结构
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

```
/*
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2) {
        if(pRoot1 && pRoot2){
            return issub(pRoot1,pRoot2)|| 
                HasSubtree(pRoot1->left,pRoot2)|| 
                HasSubtree(pRoot1->right,pRoot2);
        }
        return false;
    }
    
    bool issub(TreeNode* l1, TreeNode* l2) {
        if(l2){
            return l1&& l1->val==l2->val&& 
                issub(l1->left,l2->left)&& 
                issub(l1->right,l2->right);
        }
        return true;
    }
};
```
# 18、二叉树的镜像
操作给定的二叉树，将其变换为源二叉树的镜像。

```
二叉树的镜像定义：
         源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
```
```
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    void Mirror(TreeNode *pRoot) {
        if(!pRoot) return;
        TreeNode *tmp = pRoot->left;
        pRoot->left = pRoot->right;
        pRoot->right = tmp;
        Mirror(pRoot->left);
        Mirror(pRoot->right);
    }
};
```
# 19、顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

```
/*
   m   n
 i 1 2 3
   4 5 6
 j 7 8 9
*/
class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector<int> res;
        int i = 0,j = matrix.size()-1,m = 0,n = matrix[0].size()-1;
        while(i<=j && m<=n){
            for(int k=m;k<=n;k++) res.push_back(matrix[i][k]);
            i++;//削首行
            if(i>j) break;
            for(int k=i;k<=j;k++) res.push_back(matrix[k][n]);
            n--;//削尾列
            if(m>n) break;
            for(int k=n;k>=m;k--) res.push_back(matrix[j][k]); 
            j--;//削尾行
            if(i>j) break;
            for(int k=j;k>=i;k--) res.push_back(matrix[k][m]);
            m++;//削首列
        }
        return res;
    }
};
```
# 20、包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

```
/*
 用stack1保存数据，用stack2做辅助栈保存依次入栈最小的数
 stack1:5, 4, 3, 8, 10, 11, 12, 1
 stack2:5, 4, 3,no, no, no, no, 1
 no代表此次不入栈
 入栈，如果stack1的压入比stack2压入大，stack2不压;小于等于，两栈同时压入
 出栈，如果两栈顶元素不等，stack1出，stack2不出;相等，都出
*/
class Solution {
public:
    stack<int> stack1,stack2;
    void push(int value) {
        stack1.push(value);
        if(stack2.empty()) stack2.push(value);
        else{
            if(value <= stack2.top()) stack2.push(value);
        }
    }
    void pop() {
        if(stack1.top() == stack2.top()) stack2.pop();
        stack1.pop();
    }
    int top() {
        return stack1.top();
    }
    int min() {
        return stack2.top();
    }
};
```
# 21、栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

```
class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        stack<int> s;
        int k = 0,len = pushV.size();
        for(int i=0;i<len;i++){
            s.push(pushV[i]);
            while(k<len && popV[k] == s.top()){
                s.pop();
                k++;
            }
        }
        return s.empty();
    }
};
```
# 22、从上往下打印二叉树
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

```
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        vector<int> res;
        queue<TreeNode* > q;
        if(root) q.push(root);
        while(!q.empty()){
            if(q.front()->left) q.push(q.front()->left);
            if(q.front()->right) q.push(q.front()->right);
            res.push_back(q.front()->val);
            q.pop();
        }
        return res;
    }
};
```
# 23、二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

```
/*
 二叉搜索树BST 左子树值都比root小，右子树值都比root大。
 去掉最后一个元素root，其他分成两段:
 前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是BST的后序遍历
*/
class Solution {
public:
    bool VerifySquenceOfBST(vector<int> sequence) {
        if(sequence.size()==0) return false;
        return isok(sequence,0,sequence.size()-1);
    }
    bool isok(vector<int> arr,int l,int r) {
        if(l >= r) return true;
        int i=l;
        while(i<r && arr[i]<arr[r]) i++; //找到满足BST的右子树开头
        for(int j=i;j<r;j++) if(arr[j] < arr[r]) return false; //判断剩下是否为右子树
        return isok(arr,l,i-1)&& isok(arr,i,r-1);
    } 
};
```
# 24、二叉树中和为某一值的路径
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

```
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    vector<vector<int> > res;
    vector<int> tmp;
    vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {
        if(root) helper(root,expectNumber);
        return res;
    }
    void helper(TreeNode* root,int n) {
        if(!root) return;
        tmp.push_back(root->val);
        if(root->val == n && !root->left && !root->right) res.push_back(tmp);
        helper(root->left,n-root->val);
        helper(root->right,n-root->val);
        tmp.pop_back();
    }
};
```
# 25、复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

```
/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
/*
 复制节点，如：复制节点A得到A1，将A1插入节点A后面
 复制random，遍历链表，A1->random = A->random->next;
 将链表拆分成原链表和复制后的链表
*/
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead)
    {
        if(!pHead) return NULL;
        
        RandomListNode* cur = pHead;//从头复制节点 A->B->C 变成A->A'->B->B'->C->C'
        while(cur){
            RandomListNode* copynode = new RandomListNode(cur->label);
            copynode -> next = cur -> next;
            cur->next = copynode;
            cur = cur -> next -> next;
        }
        
        cur = pHead;//从头复制random,A1->random = A->random->next;
        while(cur){
            if(cur -> random) cur -> next -> random = cur -> random -> next;
            cur = cur -> next -> next;
        }
        
        cur = pHead;//从头将链表拆分成原链表和复制后的链表
        RandomListNode* res = cur -> next; //复制后的链表,标记位置
        RandomListNode* tmp;
        while(cur -> next){
            tmp = cur -> next;
            cur -> next = tmp -> next;
            cur = tmp;
        }
        return res;
    }
};
```
# 26、二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

```
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
	//树的线索化，利用了二叉树结点中的空指针，让它们分别指向本结点的前驱或者后继
    TreeNode* head = NULL;
    TreeNode* res = NULL;
    TreeNode* Convert(TreeNode* pRootOfTree) {
        if(!pRootOfTree) return NULL;
        helper(pRootOfTree);
        return res;
    }
    void helper(TreeNode* root) {
        if(!root) return;
        helper(root->left);
        if(!head){ //中序遍历第一个，即树的左下角
            head = root;
            res = root;
        }
        else{
            head -> right = root;
            root -> left = head;
            head = root;
        }
        helper(root->right);
    } 
};
```
# 27、字符串的排列
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

```
/*
 问题转换为先固定第一个字符，求剩余字符的排列
 再把第一个字符与后面每一个字符交换，并同样递归获得首位后面的字符串组合
 a b b c:
 a+f(bbc),b+f(abc),c+f(abb); 遍历出所有可能出现在第一个位置的字符
 f(bbc)=b+f(bc),b+f(bc),c+f(bb);
 f(bc)=b+f(c),c+f(b);
 f(c)=c;
*/
class Solution {
public:
    vector<string> res;
    vector<string> Permutation(string str) {
        if(str.empty()) return res;
        help(str,0);
        sort(res.begin(),res.end());
        return res;
    }
    void help(string s,int n) {
        if(n==s.size()-1){
            if(find(res.begin(),res.end(),s)==res.end()) res.push_back(s);
        }
        else{
            for(int i=0;i<s.size();i++){
                swap(s[i],s[n]);
                help(s,n+1);
                swap(s[n],s[i]);
            }
        }
    }
};
```
# 28、数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

```
/*
 如果重复的次数超过一半的话，一定有相邻的数字相同这种情况的
 对数组同时去掉两个不同的数字，到最后剩下的一个数就是该数字
*/
class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {
        if(numbers.empty()) return 0;
        int res = numbers[0];
        int times = 0;
        for(int i=0;i<numbers.size();i++){
            if(numbers[i] == res) times++;
            else{
                times--;
                if(times == 0){
                    res = numbers[i];
                    times = 1;
                }
            }
        }
        //check
        times = 0;
        for(int i=0;i<numbers.size();i++){
            if(numbers[i] == res) times++;
        }
        return times>numbers.size()/2?res:0;
    }
};
/* 涉及到快排sort，其时间复杂度为O(NlogN)并非最优
class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers)
    {
        // 因为用到了sort，时间复杂度O(NlogN)，并非最优
        if(numbers.empty()) return 0;
         
        sort(numbers.begin(),numbers.end());
        int middle = numbers[numbers.size()/2];//假设存在众数may
        
        //check
        int count=0; // 出现次数
        for(int i=0;i<numbers.size();++i)
        {
            if(numbers[i]==middle) ++count;
        }
         
        return (count>numbers.size()/2) ? middle :  0;
    }
};
*/
```
# 29、最小的k个数
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

```
/*
 基于堆排序算法，构建最大堆。时间复杂度为O(nlogk)
 用最大堆保存这k个数，每次只和堆顶比，如果比堆顶小，删除堆顶，新数入堆
 如果用快速排序，时间复杂度为O(nlogn)；
*/
class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        vector<int> res;
        priority_queue<int> q; 
        //priority_queue<int,vector<int>,greater<int>> q;最小堆
        if(input.empty() || k>input.size() || k==0) return res;
        for(int i=0;i<input.size();i++){
            if(i<k) q.push(input[i]);
            else{
                if(input[i] < q.top()){
                    q.pop();
                    q.push(input[i]);
                }
            }
        }
        while(!q.empty()){
            res.push_back(q.top());
            q.pop();
        }
        return res;
    }
};
```
# 30、连续子数组的最大和
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

```
class Solution {
public:
    int FindGreatestSumOfSubArray(vector<int> array) {
        int res = array[0];
        int max = 0;
        for(int i=0;i<array.size();i++){
            max += array[i];
            if(max > res) res = max;
            if(max < 0) max = 0;
        }
        return res;
    }
};
```
# 31、整数中1出现的次数
求出1~~13的整数中1出现的次数,并算出100~~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

```
/*
 n=10917 1~10917
 所有数里在个位的1的数量：
 前面为0~1090，个位后无，排列组合共1*1091种情况；前面为1091时，个位后为1。总共：1*1091+1(m=1，情况3)
 所有数里在十位的1的数量：
 前面为0~108，十位后为0~9，排列组合共10*109种情况；前面为109时，十位后为0~7。总共：10*109+8(m=8，情况2)
 所有数里在百位的1的数量：
 前面为0~9，百位后为0~99，排列组合共100*10种情况；前面为10时，百位后为0~99。总共：100*10+100(m=100，情况3)
 所有数里在千位的1的数量：
 前面为0~0，千位后为0~999，排列组合共1000*1种情况；前面为1时，千位后没有满足的。总共：1000*1+0(m=0，情况1)
 所有数里在万位的1的数量：
 前面为无，万位后为0~917。总共：1000*0+918(m=918，情况2)
 
 精髓在于后面部分m值分三种情况：
 ①当前位为0时，m=0；②当前位为1时，m=后面值+1；③当前位为2~9时，m=10^(后面的位数)
*/
class Solution {
public:
    int NumberOf1Between1AndN_Solution(int n) {
        if(n == 0) return 0;
        int res = 0;
        int base = 1,t = n,m;
        while(t!=0){
            if(t%10 == 0) m = 0;
            else if(t%10 == 1) m = n-t*base+1;
            else m = base;
            t/=10; res+=base*t+m; base*=10; 
        }
        return res;
    }
};
```
# 32、把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

```
class Solution {
public:
    //sort中的比较函数compare要声明为静态成员函数或全局函数，不能作为普通成员函数
    string PrintMinNumber(vector<int> numbers) {
        string res = "";
        sort(numbers.begin(),numbers.end(),cmp);
        for(int i=0;i<numbers.size();i++){
            res += to_string(numbers[i]); 
        }
        return res;
    }
    static bool cmp(int &i,int &j) {
        string si = to_string(i);
        string sj = to_string(j);
        return si+sj<sj+si; // 2 23和23 2
    }
};
```
# 33、丑数
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

```
/*
 如果p是丑数，那么p=2^x * 3^y * 5^z, 且x,y,z需满足是前面的丑数
 初始x=y=z=1， 2^x、3^y、5^z最小的数2^x加进结果，x在结果中位置后移一位
*/
class Solution {
public:
    int GetUglyNumber_Solution(int index) {
        if(index < 7) return index;
        vector<int> res(index);
        res[0] = 1;
        int x=0, y=0, z=0;
        for(int i=1;i<index;i++){
            res[i] = min(min(res[x]*2,res[y]*3),res[z]*5);
            if(res[i] == res[x]*2) x++;
            if(res[i] == res[y]*3) y++;
            if(res[i] == res[z]*5) z++;
        }
        return res[index-1];
    }
};
```
# 34、第一个只出现一次的字符
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

```
class Solution {
public:
    int FirstNotRepeatingChar(string str) {
        //字符在计算机中以ASCII码的形式存储，当字符作为数组下标时，其表示的下标值为该字符的ASCII码的十进制值
        //0-9:  48-57， A-Z:  65-90， a-z:  97-122
        map<char,int> map; //map支持int，char，string
        for(int i=0;i<str.size();i++){
            map[str[i]]++;
        }
        for(int i=0;i<str.size();i++){
            if(map[str[i]] == 1) return i;
        }
        return -1;
    }
};
```
# 35、数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

```
输入描述:
题目保证输入的数组中没有的相同的数字
数据范围：
	对于%50的数据,size<=10^4
	对于%75的数据,size<=10^5
	对于%100的数据,size<=2*10^5

示例:
输入   1,2,3,4,5,6,7,0
输出   7
```
```
/*
 先把数组分割成子数组，先统计出子数组内部的逆序对的数目，然后再统计出两个相邻子数组之间的逆序对的数目
 在统计逆序对的过程中，还需要对数组进行排序,每一次比较的时候
 都把较大的数字从后面往前复制到一个辅助数组中，确保辅助数组copy中的数字是递增排序的
 交换copy和data:在每次的操作中，当前传入函数中第一项，比较的结果都存放到第二项中,需要交叉保证下一次是排序的
 输入[7,5,6,4], 最后的结果copy[4,5,6,7], data[5,7,4,6]
*/
class Solution {
public:
    int InversePairs(vector<int> data) {
        if(data.size()==0) return 0;
        vector<int>copy(data); //使用data初始化copy
        long long P = InversePairsCore(data,copy,0,data.size()-1);
        return P%1000000007;
    }
    long long InversePairsCore(vector<int> &data,vector<int> &copy,int l,int r) {
        if(l == r){
            copy[l] = data[l]; return 0;
        }
        int mid = (l+r)/2;
        long long left = InversePairsCore(copy,data,l,mid);
        long long right = InversePairsCore(copy,data,mid+1,r);
        int i = mid,j = r;
        long long count = 0; //需要long long,int的话最后一个例子会溢出测试不通过
        int cur = r;
        while(i>=l && j>=mid+1){
            if(data[i]>data[j]){ //3 8,4 6  8>6
                count += j-mid;
                copy[cur--] = data[i]; i--;
            }
            else{
                copy[cur--] = data[j]; j--;
            }
        }
        while(i>=l){
            copy[cur--] = data[i]; i--;
        }
        while(j>=mid+1){
            copy[cur--] = data[j]; j--;
        }
        return left+right+count;
    }
};
```
# 36、两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共结点。

```
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
        //找出2个链表的长度，然后让长的先走两个链表的长度差，然后再一起走
        int len1 = getlen(pHead1);
        int len2 = getlen(pHead2);
        int dis = len1-len2>0?len1-len2:len2-len1;
        while(dis!=0){
            if(len1>len2) pHead1 = pHead1->next;
            else pHead2 = pHead2->next;
            dis--;
        }
        while(pHead1){
            if(pHead1 == pHead2) return pHead1;
            pHead1 = pHead1->next;
            pHead2 = pHead2->next;
        }
        return NULL;
    }
    
    int getlen(ListNode* p) {
        int res = 0;
        ListNode* root = p;
        while(root){
            res++;
            root = root->next;
        }
       return res;
    }
};
```
# 37、数字在排序数组中出现的次数
统计一个数字在排序数组中出现的次数。

```
class Solution {
public:
    int GetNumberOfK(vector<int> data ,int k) {
        if(data.empty()) return 0;
        int l=0,r=data.size()-1;
        while(l<=r){
            int mid = (l+r)/2;
            if(data[mid]==k){ //计数
                int res=0,i=mid;
                while(i>=l){
                    if(data[i]==k){
                        i--;
                        res++;
                    }
                    else break;
                }
                i=mid+1;
                while(i<=r){
                    if(data[i]==k){
                        i++;
                        res++;
                    }
                    else break;
                }
                return res;
            }
            else if(data[mid] > k) r=mid-1;
            else l=mid+1;
        }
        return 0;
    }
};
```
# 38、二叉树的深度
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

```
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    int TreeDepth(TreeNode* pRoot) {
        if(!pRoot) return 0;
        return max(TreeDepth(pRoot->left),TreeDepth(pRoot->right))+1;
    }
};
```
# 39、平衡二叉树
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

```
class Solution {
public:
    //左右子树均为平衡二叉树，且左右子树层高不超过1
    bool IsBalanced_Solution(TreeNode* pRoot) {
        if(!pRoot) return true;
        return IsBalanced_Solution(pRoot->left)
            && IsBalanced_Solution(pRoot->right)
            && abs(getlen(pRoot->left)-getlen(pRoot->right))<=1;
    }
    int getlen(TreeNode* p){
        if(!p) return 0;
        return max(getlen(p->left),getlen(p->right))+1;
    }
};
```
# 40、数组中只出现一次的数字
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

```
/*
 异或性质：
 交换律：a ^ b ^ c  <=> a ^ c ^ b,俩两相同的移到一起
 相同的数异或为0: n ^ n => 0
 任何数于0异或为任何数 0 ^ n => n
 
 遍历异或后，只剩下两单个的异或了，结果res的二进制至少有一位为1
 取第一个1所在的位数index，原数组分成第index位为1和为0
 相同的数肯定在一个组，两个单的在不同的组
*/
class Solution {
public:
    void FindNumsAppearOnce(vector<int> data,int* num1,int *num2) {
        int add = 0;
        for(int i=0;i<data.size();i++){
            add ^= data[i];
        }
        int index = 0;
        while((add&1)==0){
            add = add >> 1;
            index++;
        }
        for(int i=0;i<data.size();i++){
            if((data[i]>>index&1)==0) num1[0]^=data[i];
            else num2[0]^=data[i];
        }
    }
};
```
# 41、和为S的连续正数序列
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

```
class Solution {
public:
    vector<vector<int> > FindContinuousSequence(int sum) {
        vector<vector<int> > res;
        vector<int> part;
        int i = 1,j = 2;
        while(i < j){
            int count = (i+j)*(j-i+1)/2; //i~j的和
            if(count == sum){ //将i~j插入res
                part.clear();
                for(int k=i;k<=j;k++){
                    part.push_back(k);
                }
                res.push_back(part);
                i++;
            }
            else if(count < sum) j++; //右窗口右移
            else i++; //左窗口右移
            
        }
        return res;
    }
};
```
# 42、和为S的两个数字
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。

```
class Solution {
public:
    vector<int> FindNumbersWithSum(vector<int> array,int sum) {
        vector<int> res;
        int i = 0, j = array.size()-1;
        while(i<j){
            if(array[i]+array[j] == sum){ //1 3 4 6,1*6<3*4,越边边乘积越小
                res.push_back(array[i]);
                res.push_back(array[j]);
                break;
            }
            else if(array[i]+array[j] > sum) j--;
            else i++;
        }
        return res;
    }
};
```
# 43、左旋转字符串
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

```
class Solution {
public:
    string LeftRotateString(string str, int n) {
        if(str.empty()) return "";
        n%=str.size();
        return str.substr(n)+str.substr(0,n);
    }
};
```
# 44、翻转单词顺序列
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

```
class Solution {
public:
    string ReverseSentence(string str) {
        string res;
        stack<string> stack;
        string tmp;
        for(int i=0;i<str.size();i++){
            if(str[i] == ' '){
                stack.push(tmp);
                tmp.clear();
            }
            else tmp.push_back(str[i]);
        }
        stack.push(tmp);
        while(!stack.empty()){
            res += ' ' + stack.top();
            stack.pop();
        }
        return res.erase(0,1);
    }
};
```
# 45、扑克牌顺子
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

```
/*
 max 记录 最大值,min 记录  最小值,min ,max 都不记0
 满足条件 max - min <5;除0外没有重复的数字(牌);数组长度 为5
*/
class Solution {
public:
    bool IsContinuous( vector<int> numbers ) { // 5张牌
        if(numbers.size()!=5) return false;
        int max = -1, min = 14;
        int* flag = new int[14](); //初始化数组全为 0
        for(int i=0;i<numbers.size();i++){
            if(numbers[i] == 0) continue;
            int tmp = numbers[i];
            if(flag[tmp] == 1) return false; //重复
            else{
                if(tmp < min) min = tmp;
                if(tmp > max) max = tmp;
                flag[tmp] = 1;
            }
        }
        delete[] flag;
        return max-min<5;
    }
};
```
# 46、孩子们的游戏（圆圈中最后剩下的数）
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

```
class Solution {
public:
    int LastRemaining_Solution(int n, int m) {
        if (m == 0 || n == 0) return -1;
        int* flag = new int[n]();//初始化数组全为 0
        int i = -1,left = n,step = 0;
        while(left>0){
            i++; //0
            if(i == n) i = 0; //模拟环
            if(flag[i] == 1) continue; //跳过被删除的对象
            step++;
            if(step == m){
                step = 0;
                flag[i] = 1;
                left--;
            }
        }
        return i;
    }
};
```
# 47、求1+2+3+...+n
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

```
/*
 int Sum_Solution(int n) {
     if(n == 0) return 0;
     return n+Sum_Solution(n-1);
 }
 将此段代码改写成不使用for、while、if、else、switch、case等关键字及条件判断语句
*/
class Solution {
public:
    int Sum_Solution(int n) {
        int res = n;
        res && (res+=Sum_Solution(n-1));
        //当n==0时，只执行前面的判断，为false，然后直接返回0；
        //当n>0时，执行sum+=Sum_Solution(n-1)，实现递归计算Sum_Solution(n)
        return res;
    }
};
```
# 48、不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

```
/*
 两数相与再左移一位，表示相加进位的值 101&111=101 左移1，1010
 两数异或，表示相加不算进位的值 101^111=010
 两者相加为和，(101&111)<<1 + 101^111 = 1100,即调用函数本身，直到进位为0
*/
class Solution {
public:
    int Add(int num1, int num2) {
        while(num2!=0){
            int tmp = num1^num2; //相加不算进位的值
            num2 = (num1&num2)<<1; //相加进位的值
            num1 = tmp;
        }
        return num1;
    }
};
```
# 49、把字符串转换成整数
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0

输入: +2147483647  ,  1a33
输出: 2147483647  ,  0

```
/*
字符"0123456789"的值是连续的，如果c"0123456789"范围内
int a = c - '0'就是对应整数值
从后往前，最后判断符号位
*/
class Solution {
public:
   int StrToInt(string str) {
       if(str.empty()) return 0;
       int res = 0,base = 1;
       for(int i = str.size()-1;i>=0;i--){
           if(str[i]>='0' && str[i]<='9'){
               res += base*(int)(str[i]-'0');
               base *= 10;
           }
           else if(str[i] == '-'){
               if(i == 0) return -res; //-123
           }
           else if(str[i] == '+'){
               if(i == 0) return res; //+123
           }
           else return 0; //1a3
       }
       return res; //123
   }
};
```
# 50、数组中重复的数字
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

```
/*
 数字的范围保证在0 ~ n-1 之间，所以可以利用现有数组设置标志
 当一个数字i被访问过后，可以设置对应位上的数numbers[i] += n
 再次访问i时，发现numbers[i] >=n，直接返回i
*/
class Solution {
public:
    // Parameters:
    //        numbers:     an array of integers
    //        length:      the length of array numbers
    //        duplication: (Output) the duplicated number in the array number
    // Return value:       true if the input is valid, and there are some duplications in the array number
    //                     otherwise false
    bool duplicate(int numbers[], int length, int* duplication) {
        for(int i=0;i<length;i++){ //2,3,1,0,2,5,3
            int cur = numbers[i];
            if(cur >= length) cur = cur-length;
            if(numbers[cur] >= length){
                *duplication = cur;
                return true;
            }
            numbers[cur] += length;
        }
        return false;
    }
};
```
# 51、构建乘积数组
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

```
/*
 1                             第一项左侧
 a[0]                          第二项左侧
 a[0]*a[1]
 a[0]*a[1]*a[2]
 a[0]*a[1]*a[2]...*a[n-2]      第n项左侧
 
 1                             第n项右侧
 a[n-1]
 a[n-1]*a[n-2]
 a[n-1]*a[n-2]*a[n-3]...*a[2]  第二项左侧
 a[n-1]*a[n-2]*a[n-3]...*a[1]  第一项右侧
*/
class Solution {
public:
    vector<int> multiply(const vector<int>& A) {
        vector<int> res;
        if(A.empty()) return res;
        int tmp = 1;
        for(int i=0;i<A.size();i++){ //左边乘
            res.push_back(tmp);
            tmp *= A[i];
        } 
        tmp = 1;
        for(int i=A.size()-1;i>=0;i--){ //右边乘
            res[i] *= tmp;
            tmp *= A[i];
        }
        return res;
    }
};
```
# 52、正则表达式匹配
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

```
/*
 当第二个字符不是“*”时：
 1、第一个字符匹配，字符串和模式后移1个字符，继续匹配 
 2、第一个字符不匹配，返回false
 当第二个字符是“*”时：
 1、第一个字符不匹配，模式后移2个字符，继续匹配
 2、第一个字符匹配，可以有3种情况：
    （1）模式后移2字符，相当于x*被忽略，x出现0次；
    （2）字符串后移1字符，模式后移2字符，相当于x出现一次；
    （3）字符串后移1字符，模式不变，相当于x出现多次次；
 注：匹配指值相同，或pattern为'.',字符串未到尾
*/
class Solution {
public:
    bool match(char* str, char* pattern)
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
# 53、表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

```
/*
 1、+、-
  第一次出现+-符号，且不在首位，必须紧接在e之后
  第二次出现+-符号，必须紧接在e之后
 2、e、E
  e后不为空
  不能双e
 3、.
  .前不能有.或e
 4、其他
  return false
*/
class Solution {
public:
    bool isNumeric(char* string) {
        // 标记符号、小数点、e是否出现过
        bool hasSign = false, hasPoint = false, hasE = false; 
        for(int i=0;string[i];i++){
            if(string[i] == '+' || string[i] == '-'){
                if(!hasSign && i>0 && string[i-1]!='e' && string[i-1]!='E') return false;
                if(hasSign && string[i-1]!='e' && string[i-1]!='E') return false;
                hasSign = true;
            }
            else if(string[i] == 'e' || string[i] == 'E'){
                if(string[i+1] == '\0' || hasE) return false;
                hasE = true;
            }
            else if(string[i] == '.'){
                if(hasPoint || hasE) return false;
                hasPoint = true;
            }
            else if(string[i] < '0' || string[i] > '9') return false;
        }
        return true;
    }
};
```
# 54、字符流中第一个不重复的字符
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。

```
/*
 字符在计算机中以ASCII码的形式存储，当字符作为数组下标时，其表示的下标值为该字符的ASCII码的十进制值
 0-9:  48-57  ,A-Z:  65-90  ,a-z:  97-122   ASCII码:0~127
*/
class Solution
{
public:
    string s;
    char flag[128] = {0}; 
    void Insert(char ch) {
        s += ch;
        flag[ch]++;
    }
    
    char FirstAppearingOnce() {
        for(int i=0;i<s.size();i++){
            if(flag[s[i]] == 1) return s[i];
        }
        return '#';
    }
};
```
# 55、链表中环的入口结点
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

```
/*
 如果有环，快慢指针总会相遇
 1——2——3——4——5——6
          |     |
          9——8——7
 假设快慢指针相遇在6，有1~6走的=6~6走的
 1~6走的 = 1~入环点+入环点~6
 6~6走的 = 6~入环点+入环点~6
 则当快指针从1重新开始，两指针速度相同，再次相遇即为入口节点
*/
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* EntryNodeOfLoop(ListNode* pHead) {
        //快慢指针，判断是否有环
        bool hasLoop = false;
        ListNode* fast = pHead;
        ListNode* slow = pHead;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow){
                hasLoop = true;
                break;
            }
        }
        //寻找环的入口节点
        if(hasLoop){
            fast = pHead;
            while(fast != slow){
                fast = fast->next;
                slow = slow->next;
            }
            return slow;
        }
        return NULL;
    }
};
```
# 56、删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

```
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* deleteDuplication(ListNode* pHead) {
        ListNode* root = new ListNode(0);//设为几无所谓
        ListNode* h = root; //标记当前位置
        h->next = pHead;
        while(h->next && h->next->next){//至少两个节点
            ListNode* tmp = h->next->next;
            if(h->next->val == tmp->val){//两节点相同
                while(tmp && h->next->val == tmp->val){
                    tmp = tmp->next;
                }
                h->next = tmp; //删除操作
            }
            else h = h->next;
        }
        return root->next;
    }
};
```
# 57、二叉树的下一个结点
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

```
/*
 3种情况：
       1              1              1
      / \            / \            / \
     2   3          2   4          2   5
        / \        /              / \
       4   5      3              3   4
  cur=1,next=4   cur=2,next=1   cur=4,next=1
 情况1，有右子树，返回右子树的左下角
 情况2，无右子树，且是父结点的左子树，返回父结点
 情况3，无右子树，且是父结点的右子树，返回父结点的左上角的父结点
*/
/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {
        
    }
};
*/
class Solution {   
public:
    TreeLinkNode* GetNext(TreeLinkNode* pNode) {
        if(pNode->right){
            TreeLinkNode* res = pNode->right;
            while(res->left){
                res = res->left;
            }
            return res;
        }
        else{  
            while(pNode->next && pNode->next->right == pNode){
                pNode = pNode->next;
            }
            return pNode->next;
        }
        
    }
};
```
# 58、对称的二叉树
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NUL L) {
    }
};
*/
class Solution {
public:
    bool isSymmetrical(TreeNode* pRoot){
        if(!pRoot) return true;
        return ismoir(pRoot->left,pRoot->right);
    }
    bool ismoir(TreeNode* l,TreeNode* r){//是镜像的
        if(!l && !r) return true;//都不存在
        if(l && r) return l->val==r->val && ismoir(l->left,r->right) && ismoir(r->left,l->right);
        return false;// 有且仅有1个存在
    }
};
```
# 59、按之字形顺序打印二叉树
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

```
/*
        1         ——> stack1 存奇数层，顺序
       / \
      2   3       <—— stack2 存偶数层，逆序,先left后right
     / \  / \
    4  5 6   7    ——> stack1 存奇数层，顺序,先right后left
*/
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    vector<vector<int> > Print(TreeNode* pRoot) {
        vector<vector<int> > res;
        if(!pRoot) return res;
        stack<TreeNode*> stack1,stack2;
        stack1.push(pRoot);
        while(!stack1.empty() || !stack2.empty()){
            if(!stack1.empty()){
                vector<int> tmp;
                while(!stack1.empty()){
                    if(stack1.top()->left) stack2.push(stack1.top()->left);
                    if(stack1.top()->right) stack2.push(stack1.top()->right);
                    tmp.push_back(stack1.top()->val);
                    stack1.pop();
                }
                res.push_back(tmp);
            }
            if(!stack2.empty()){
                vector<int> tmp;
                while(!stack2.empty()){
                    if(stack2.top()->right) stack1.push(stack2.top()->right);
                    if(stack2.top()->left) stack1.push(stack2.top()->left);
                    tmp.push_back(stack2.top()->val);
                    stack2.pop();
                }
                res.push_back(tmp);
            }
        }
        return res;
    }
};
```
# 60、把二叉树打印成多行
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
        vector<vector<int> > Print(TreeNode* pRoot) {
            vector<vector<int> > res;
            if(!pRoot) return res;
            queue<TreeNode*> queue;
            queue.push(pRoot);
            while(!queue.empty()){
                int num = queue.size();
                vector<int> tmp;
                while(num!=0){
                    if(queue.front()->left) queue.push(queue.front()->left);
                    if(queue.front()->right) queue.push(queue.front()->right);
                    tmp.push_back(queue.front()->val);
                    queue.pop();
                    num--;
                }
                res.push_back(tmp);
            }
            return res;
        }
    
};
```
# 61、序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树

```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    char* Serialize(TreeNode *root) {
        if(!root) return NULL;
        string s;
        queue<TreeNode*> queue;
        queue.push(root);
        while(!queue.empty()){
            if(queue.front()){
                queue.push(queue.front()->left);
                queue.push(queue.front()->right);
                s += to_string(queue.front()->val)+",";
            }
            else s += "#,";
            queue.pop();
        }
        char* res = strdup(s.c_str());
        /* 另一种写法，不用strdup()
        char* res = new char[s.size() + 1];
        int i;
        for(i=0;i<s.size();i++) res[i]=s[i];
        res[i] = '\0';
        */
        return res;
    }
    TreeNode* Deserialize(char *str) {
        if(!str) return NULL;
        int i = 0;
        auto head = getnode(str,i);
        queue<TreeNode*> queue;
        queue.push(head);
        while(!queue.empty()){
            queue.front()->left = getnode(str,i);
            queue.front()->right = getnode(str,i);
            if(queue.front()->left) queue.push(queue.front()->left);
            if(queue.front()->right) queue.push(queue.front()->right);
            queue.pop();
        }
        return head;
    }
    TreeNode* getnode(char *str,int &i){
        if(str[i] == ',') i++;
        if(str[i] == '#'){
            i += 2;
            return NULL;
        }
        string s;
        while(str[i] != ',' && str[i] != '\0'){
            s += str[i];
            i++;
        }
        if(!s.empty()) return new TreeNode(stoi(s));
        return NULL;
    }
};
```
# 62、二叉搜索树的第k个结点
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

```
/*
 二叉搜索树：左子树上所有结点的值均小于它的根结点的值,右子树上所有结点的值均大于它的根结点的值
 二叉搜索树按照中序遍历得到递增的顺序，压入栈，第k个结点就是结果
*/
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/

class Solution {
public:
    stack<TreeNode*> stack;
    TreeNode* KthNode(TreeNode* pRoot, int k){
        if(k <= 0) return NULL;
        sortmid(pRoot,k);
        if(stack.size() < k) return NULL; //k大于节点数
        return stack.top();
    }
    
    void sortmid(TreeNode* pRoot, int k) {
        if(!pRoot) return;
        if(stack.size()!=k) sortmid(pRoot->left,k);
        if(stack.size()!=k) stack.push(pRoot);
        if(stack.size()!=k) sortmid(pRoot->right,k);
    }
};
```
# 63、数据流中的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

```
/*
 使用大小顶堆，中位数是大顶堆的根节点与小顶堆的根节点和的平均数
 大顶堆,由大到小，存较小的数 7 6 5
 小顶堆,由小到大，存较大的数 8 9 10
 步骤：
 第一个插入的元素装大顶堆
 1、每来一个插入的元素，比大顶堆堆顶元素小的装大顶堆，否则装小顶堆（保证大顶堆的数都比小顶堆的数小）
 2、判断是否大顶堆装多了，大顶堆最多比小顶堆多一个，如果是，将大顶堆堆顶元素插入小顶堆
 3、判断是否小顶堆装多了，小顶堆小于等于大顶堆，如果是，将小顶堆堆顶元素插入大顶堆
*/
class Solution {
public:
    priority_queue<int,vector<int>,less<int> > big_heap;
    priority_queue<int,vector<int>,greater<int> > small_heap;
    void Insert(int num) {
        if(big_heap.empty() || num < big_heap.top()) big_heap.push(num);
        else small_heap.push(num);
        if(big_heap.size() == small_heap.size()+2){
            small_heap.push(big_heap.top());
            big_heap.pop();
        }
        if(big_heap.size() == small_heap.size()-1){
            big_heap.push(small_heap.top());
            small_heap.pop();
        }
    }

    double GetMedian() { 
        return small_heap.size()==big_heap.size()?(small_heap.top()+big_heap.top())/2.0:big_heap.top();
    }
};
```
# 64、滑动窗口的最大值
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

```
class Solution {
public:
    vector<int> maxInWindows(const vector<int>& num, unsigned int size)
    {
        vector<int> res;
        deque<int> q;//队首为当前窗口下最大值下标
        for(unsigned int i=0;i<num.size();i++){
            while(!q.empty() && num[i]>num[q.back()]){//q删掉所有比当前元素小的，保证q降序
                q.pop_back();
            }
            if(!q.empty() && q.front()+size == i){ //若队首超过窗口位置,删掉
                q.pop_front();
            }
            q.push_back(i);
            if(size && i+1>=size) res.push_back(num[q.front()]); //防止size=0
        }
        return res;
    }
};
```
# 65、矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

```
class Solution {
public:
    bool hasPath(char* matrix, int rows, int cols, char* str)
    {
        //if(!matrix || rows<=0 || cols<=0 || !str) return false;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(help(matrix,i,j,str,0,rows,cols)) return true;
            }
        }
        return false;
    }
    bool help(char* matrix, int i, int j, char* str, int k, int rows, int cols) {
        int index = i*cols+j;
        if(i<0||i>=rows||j<0||j>=cols||matrix[index]=='#'||str[k]!=matrix[index]) return false;
        if(str[k+1]=='\0') return true;
        char tmp = matrix[index];
        matrix[index] = '#';
        if(help(matrix,i+1,j,str,k+1,rows,cols) 
           || help(matrix,i-1,j,str,k+1,rows,cols)
           || help(matrix,i,j+1,str,k+1,rows,cols) 
           || help(matrix,i,j-1,str,k+1,rows,cols)){
            return true;
        }
        matrix[index] = tmp;
        return false;
    }
};
```
# 66、机器人的运动范围
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

```
class Solution {
public:
    int movingCount(int threshold, int rows, int cols) {
        if(rows<=0 || cols<=0 || threshold<0) return 0;
        bool* flag = new bool[rows*cols];
        memset(flag,false,rows*cols);
        return helper(threshold,rows,cols,0,0,flag);
    }
    int helper(int threshold, int rows, int cols,int i, int j, bool* flag) {
        int index = i*cols+j;
        if(i<0||i>=rows||j<0||j>=cols||flag[index]||count(i)+count(j)>threshold) return 0;
        flag[index] = true;
        return helper(threshold,rows,cols,i-1,j,flag)+
               helper(threshold,rows,cols,i+1,j,flag)+
               helper(threshold,rows,cols,i,j-1,flag)+
               helper(threshold,rows,cols,i,j+1,flag)+1;
    }
    int count(int n) {
        int res = 0;
        while(n!=0){
            res += n%10;
            n /= 10;
        }
        return res;
    }
};
```
