---
title: "检查索引越界"
description: "数据结构基础 python"
date: "2026-04-28"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\05_algorithm_backup\\ku_backup_20260427\\11_数据结构基础python.md"
---
数据结构基础 python

### 数组（顺序存储）
连续的内存空间，存在数据搬移和扩缩容的问题

#### 静态数组
##### **静态数组实现动态数组**
* 自动扩缩容：
    * 当数组元素个数达到底层静态数组的容量上限时，扩容为原来的 2 倍；
    * 当数组元素个数缩减到底层静态数组的容量的 1/4 时，缩容为原来的 1/2。

* 索引越界的检查：索引index < size 和插入 index <= size
* 删除元素谨防内存泄漏



```
class MyArrayList:

    def __init__(self, init_capacity=1):
        self.data = [None] * init_capacity
        self.size = 0

    def add_last(self, e):
        cap = len(self.data)

        if self.size == cap:
            self._resize(2 * cap)

        self.data[self.size] = e
        self.size += 1

    def add(self, index, e):
        # 检查索引越界
        self._check_position_index(index)

        cap = len(self.data)
        if self.size == len(self.data):
            self._resize(2 * cap)

        # 搬移数据 data[index..] -> data[index+1..]
        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]

        # 插入新元素
        self.data[index] = e
        self.size += 1

    def add_first(self, e):
        self.add(0, e)

    def remove_last(self):
        if self.size == 0:
            raise Exception("Array is empty")

        cap = len(self.data)
        # 可以缩容，节约空间
        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_val = self.data[self.size - 1]
        # 删除最后一个元素
        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_val

    def remove(self, index):
        # 检查索引越界
        self._check_element_index(index)

        cap = len(self.data)
        # 可以缩容，节约空间
        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_val = self.data[index]

        # 搬移数据 data[index+1..] -> data[index..]
        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]

        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_val

    def remove_first(self):
        return self.remove(0)

    def get(self, index):
        # 检查索引越界
        self._check_element_index(index)

        return self.data[index]

    def set(self, index, element):
        # 检查索引越界
        self._check_element_index(index)
        # 修改数据
        old_val = self.data[index]
        self.data[index] = element
        return old_val

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _resize(self, new_cap):
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = temp

    def _check_element_index(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index: {}, Size: {}".format(index, self.size))

    def _check_position_index(self, index):
        if not 0 <= index <= self.size:
            raise IndexError("Index: {}, Size: {}".format(index, self.size))


if __name__ == "__main__":
    arr = MyArrayList(init_capacity=3)

    # 添加 5 个元素
    for i in range(1, 6):
        arr.add_last(i)
        print(arr.data)
    # [1, None, None]
    # [1, 2, None]
    # [1, 2, 3]
    # [1, 2, 3, 4, None, None]
    # [1, 2, 3, 4, 5, None]

    arr.remove(3)
    arr.add(1, 9)
    arr.add_first(100)
    print(arr.data)
    # [100, 1, 9, 2, 3, 5]
    print(arr.remove_last())  # 5
    print(arr.data)
    # [100, 1, 9, 2, 3, None]
```
#### 动态数组
```
# python使用动态数组，不用显式指定数组大小，会根据实际存储的元素数量自动扩缩容
arr = []

for i in range(10):
    # 在末尾追加元素，时间复杂度 O(1)
    arr.append(i)

# 在中间插入元素，时间复杂度 O(N)
arr.insert(2, 666)

# 在头部插入元素，时间复杂度 O(N)
arr.insert(0, -1)

# 删除末尾元素，时间复杂度 O(1)
arr.pop()

# 删除中间元素，时间复杂度 O(N)
arr.pop(2)

# 根据索引查询元素，时间复杂度 O(1)
a = arr[0]

# 根据索引修改元素，时间复杂度 O(1)
arr[0] = 100

# 根据元素值查找索引，时间复杂度 O(N)
index = arr.index(666)
```
#### 环形数组
利用求模（余数）运算，将普通数组变成逻辑上的环形数组，实现** O(1)时间在数组头部增删元素**。

数组：

```
[1, 2, 3, _, _, _]
```
在数组头部删除元素 1：仅仅把元素 1 的位置标记为空，但并不做数据搬移。

```
[_, 2, 3, _, _, _]
```
在数组头部增加元素 4 和元素 5：当头部没有位置添加新元素时，它转了一圈，把新元素加到尾部了。

```
[4, 2, 3, _, _, 5]
```
环形数组的关键在于，它维护了两个指针 start 和 end，start 指向第一个有效元素的索引，end 指向最后一个有效元素的下一个位置索引。当 start, end 超出边界通过求模运算 % 让它们转一圈到数组头部或尾部继续工作，这样就实现了环形数组的效果。

```
class CycleArray:

    def __init__(self, init_capacity=1):
        self.data = [None] * init_capacity
        # start 指向第一个有效元素的索引，闭区间
        self.start = 0
        # end 指向最后一个有效元素的下一个位置索引，开区间
        self.end = 0
        # 数组中有效元素的数量
        self.size = 0

    def _resize(self, new_cap):
        cap = len(self.data)
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[(self.start + i) % cap]
        self.data = temp

        # 重置 start 和 end 指针
        self.start = 0
        self.end = self.size

    # 在数组头部添加元素，时间复杂度 O(1)
    def add_first(self, val):
        cap = len(self.data)
        if self.size == cap:
            self._resize(cap * 2)

        # start 指向第一个，新增 左移后赋值
        self.start = self.last_index(self.start)
        self.data[self.start] = val
        self.size += 1

    # 删除数组头部元素，时间复杂度 O(1)
    def remove_first(self):
        if self.size == 0:
            raise Exception("Array is empty")

        # start 指向第一个，删除 赋值后右移
        self.data[self.start] = None
        self.start = self.next_index(self.start)
        self.size -= 1

        cap = len(self.data)
        # 可以缩容，节约空间
        if self.size > 0 and self.size == cap // 4:
            self._resize(cap // 2)

    # 在数组尾部添加元素，时间复杂度 O(1)
    def add_last(self, val):
        cap = len(self.data)
        if self.size == cap:
            self._resize(cap * 2)

        # end 指向最后一位的下一位，新增 赋值后右移
        self.data[self.end] = val
        self.end = self.next_index(self.end)
        self.size += 1

    # 删除数组尾部元素，时间复杂度 O(1)
    def remove_last(self):
        if self.size == 0:
            raise Exception("Array is empty")

        # end 指向最后一位的下一位，删除 左移后赋值
        self.end = self.last_index(self.end)
        last_value = self.data[self.end]
        self.data[self.end] = None
        self.size -= 1

        cap = len(self.data)
        # 可以缩容，节约空间
        if self.size > 0 and self.size == cap // 4:
            self._resize(cap // 2)

        return last_value

    # 获取数组头部元素，时间复杂度 O(1)
    def get_first(self):
        if self.size == 0:
            raise Exception("Array is empty")
        return self.data[self.start]

    # 获取数组尾部元素，时间复杂度 O(1)
    def get_last(self):
        if self.size == 0:
            raise Exception("Array is empty")
        # end 指向最后一位的下一位，需要左移
        return self.data[self.last_index(self.end)]

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def last_index(self, index):
        cap = len(self.data)
        return (index - 1 + cap) % cap

    def next_index(self, index):
        cap = len(self.data)
        return (index + 1) % cap


if __name__ == "__main__":
    arr = CycleArray(3)

    # 添加 5 个元素
    for i in range(1, 6):
        arr.add_last(i)
        print(arr.data)
    # [1, None, None]
    # [1, 2, None]
    # [1, 2, 3]
    # [1, 2, 3, 4, None, None]
    # [1, 2, 3, 4, 5, None]

    arr.add_first(100)
    print(arr.data)
    # [1, 2, 3, 4, 5, 100]
    print(arr.remove_last())  # 5
    print(arr.get_first())  # 4
    print(arr.data)  # 100
    # [1, 2, 3, 4, None, 100]

```
双端队列使用的环形数组，python常规的a=[]使用的动态数组

### 单/双链表
链表优点：不需要一整块连续的内存空间存储元素，提高内存的利用效率，链表的节点不需要挨在一起；不需要考虑扩缩容和数据搬移的问题。

* **链表的优势**：头部插入/删除高效（O(1)），适合频繁动态调整的场景（如栈、队列的实现）。
* **链表的劣势**：随机访问效率低（O(n)），不适合需要频繁按索引操作的场景（此时数组更优）。
* **双链表优化**：通过维护前驱和后继指针，某些操作（如尾部删除）可优化到 O(1)，但会增加内存开销。

#### 单链表
**单链表操作**

```
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 输入一个数组，转换为一条单链表，时间复杂度 O(N)
def create_linkedlist(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    p = head
    for i in arr[1:]:
        p.next = ListNode(i)
        p = p.next

    return head


def print_linkedlist(head):
    if not head:
        print('None')
        return

    p = head
    while p:
        print(p.val, end=' ')
        p = p.next
    print()


# 1、创建单链表，时间复杂度O(N)
head = create_linkedlist([1, 2, 3, 4, 5])
print_linkedlist(head)

# 2、在单链表头部插入新元素，时间复杂度O(1)
# 在单链表头部插入一个新节点 0
cur = head
head = ListNode(0)
head.next = cur
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5
print_linkedlist(head)

# 3、在单链表尾部插入新元素，时间复杂度O(N)  注意边界条件
# 在单链表尾部插入一个新节点 6
if not head:
    head = ListNode(6)
else:
    p = head
    # 先走到链表的最后一个节点
    while p.next:
        p = p.next
    # 现在 p 就是链表的最后一个节点
    p.next = ListNode(6)
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
print_linkedlist(head)

# 4、在单链表中间插入新元素，时间复杂度O(N)
# 在第 3 个节点后面插入一个新节点 66
p = head
for _ in range(2):
    if not p:
        raise Exception('invalid index')
    p = p.next
# 此时 p 指向第 3 个节点
tmp = p.next
p.next = ListNode(66)
p.next.next = tmp
# 现在链表变成了 0 -> 1 -> 2 -> 66 -> 3 -> 4 -> 5 -> 6
print_linkedlist(head)

# 5、在单链表中删除一个节点，时间复杂度O(N)
# 删除第 5 个节点，要操作前驱节点
if not head:
    raise Exception('empty linkedlist')
else:
    p = head
    for _ in range(3):
        if not p:
            raise Exception('invalid index')
        p = p.next
    # 此时 p 指向第 4 个节点，即要删除节点的前驱节点
    node = p.next
    p.next = node.next
    # 把要删除的节点从链表中摘除
    node.next = None
# 现在链表变成了 0 -> 1 -> 2 -> 66 -> 4 -> 5 -> 6
print_linkedlist(head)

# 6、在单链表尾部删除元素，时间复杂度O(N)
# 删除尾节点
p = head
if not p:
    raise Exception('empty linkedlist')
# 如果链表只有一个节点，直接删除
if not p.next:
    head = None
else:
    # 否则，遍历到倒数第二个节点
    # 找到倒数第二个节点
    while p.next.next:
        p = p.next
    # 此时 p 指向倒数第二个节点
    # 把尾节点从链表中摘除
    p.next = None
# 现在链表变成了 0 -> 1 -> 2 -> 66 -> 4 -> 5
print_linkedlist(head)

# 7、在单链表头部删除元素，时间复杂度O(1)
# 删除头结点
if not head:
    raise Exception('empty linkedlist')
else:
    node = head
    head = node.next
    # 从链表中删去
    node.next = None
# 现在链表变成了 1 -> 2 -> 66 -> 4 -> 5
print_linkedlist(head)

```
##### **实现单链表 虚拟头节点**
虚拟头节点是单链表实现的常用技巧，尤其在需要频繁插入/删除的场景下能大幅提升代码可维护性。虚拟尾节点在双链表中更常见，单链表一般无需使用。

```
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def add_first(self, e):
        head = ListNode(e)
        head.next = self.head.next
        self.head.next = head
        self.size += 1

    def add_last(self, e):
        # 找到最后一个节点
        p = self.head
        while p.next:
            p = p.next

        p.next = ListNode(e)
        self.size += 1

    def add(self, index, e):
        if index < 0 or index > self.size:
            return

        # 找到index的前一个节点
        p = self.get_node(index - 1)

        tmp = p.next
        p.next = ListNode(e)
        p.next.next = tmp

        self.size += 1

    def remove_first(self):
        if self.size == 0:
            raise Exception("empty linked list")

        node = self.head.next
        self.head.next = node.next

        # 断开链接
        node.next = None

        self.size -= 1
        return node.val

    def remove_last(self):
        if self.size == 0:
            raise Exception("empty linked list")

        p = self.head
        # 找到倒数第二个节点
        while p.next.next:
            p = p.next

        node = p.next
        p.next = None

        # 断开链接
        node.next = None

        self.size -= 1
        return node.val

    def remove(self, index):
        if index < 0 or index >= self.size:
            return

        # 找到index的前一个节点
        p = self.get_node(index - 1)

        node = p.next
        p.next = node.next

        # 断开链接
        node.next = None

        self.size -= 1
        return node.val

    def get_first(self):
        if self.size == 0:
            raise Exception("empty linked list")
        return self.head.next.val

    def get_last(self):
        if self.size == 0:
            raise Exception("empty linked list")
        return self.get(self.size - 1)

    def get(self, index):
        if self.size == 0:
            raise Exception("empty linked list")

        if index < 0 or index >= self.size:
            raise IndexError("Index: {}, Size: {}".format(index, self.size))

        # 找到index节点
        p = self.get_node(index)

        return p.val

    def get_node(self, index):
        p = self.head
        for _ in range(index + 1):
            p = p.next
        return p

    def set(self, index, e):
        if index < 0 or index >= self.size:
            raise IndexError("Index: {}, Size: {}".format(index, self.size))

        # 找到index节点
        p = self.get_node(index)

        old_val = p.val
        p.val = e
        return old_val

    def print_linkedlist(self):
        p = self.head
        while p.next:
            print(p.next.val, end=" ")
            p = p.next
        print()


if __name__ == "__main__":
    list = MyLinkedList()
    list.add_first(1)
    list.add_first(2)
    list.add_last(3)
    list.add_last(4)
    list.print_linkedlist()
    # 2 1 3 4
    list.add(2, 5)
    list.print_linkedlist()
    # 2 1 5 3 4

    print(list.remove_first())  # 2
    # 1 5 3 4
    print(list.remove_last())  # 4
    # 1 5 3
    print(list.remove(1))  # 5
    # 1 3
    list.print_linkedlist()

    print(list.get_first())  # 1
    print(list.get_last())  # 3

    print(list.get(1))  # 3
    list.print_linkedlist()
    # 1 3

```
#### 双链表
**双链表操作**

```
class DoublyListNode:
    def __init__(self, x, next=None, prev=None):
        self.val = x
        self.next = next
        self.prev = prev


# 创建一条双链表
def create_doublylinkedlist(arr):
    if not arr:
        return None, None

    head = DoublyListNode(arr[0])
    p = head
    for i in arr[1:]:
        node = DoublyListNode(i)
        p.next = node
        node.prev = p
        p = p.next

    return head, p


def print_doublylinkedlist(head):
    if not head:
        print('None')
        return

    # 从头节点向后遍历双链表
    print('正向遍历：')
    p = head
    tail = None
    while p:
        print(p.val, end=' ')
        tail = p
        p = p.next
    print()

    p = tail
    # 从尾节点向前遍历双链表
    print('反向遍历：')
    while p:
        print(p.val, end=' ')
        p = p.prev
    print('\n')


# 1、创建单链表，时间复杂度O(N)
head, tail = create_doublylinkedlist([1, 2, 3, 4, 5])
print_doublylinkedlist(head)

# 2、在双链表头部插入新元素，时间复杂度O(1)
# 在双链表头部插入新节点 0
node = DoublyListNode(0)
node.next = head
head.prev = node
head = node
print_doublylinkedlist(head)
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5

# 3、在双链表尾部插入新元素，时间复杂度O(1)
if not head:
    head = DoublyListNode(6)
    tail = head
else:
    # 先走到链表的最后一个节点
    p = tail
    # 在双链表尾部插入新节点 6
    node = DoublyListNode(6)
    tail.next = node
    node.prev = tail
    # 更新尾节点引用
    tail = node
print_doublylinkedlist(head)
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

# 4、在双链表中间插入新元素，时间复杂度O(N)
# 在第 3 个节点后面插入一个新节点 66
p = head
for _ in range(2):
    if not p:
        raise Exception('invalid index')
    p = p.next
# 此时 p 指向第 3 个节点
node = DoublyListNode(66)
node.next = p.next
p.next = node
node.prev = p
node.next.prev = node
print_doublylinkedlist(head)
# 现在链表变成了 0 -> 1 -> 2 -> 66 -> 3 -> 4 -> 5 -> 6

# 5、在双链表中删除一个节点，时间复杂度O(N)
# 删除第 4 个节点
if not head:
    raise Exception('empty linkedlist')
else:
    # 先找到第 3 个节点
    p = head
    for i in range(2):
        if not p:
            raise Exception('invalid index')
        p = p.next
    # p 指向第 3 个节点
    node = p.next
    p.next = node.next
    node.next.prev = p
    # 把要删除的节点从链表中摘除
    node.next = None
    node.prev = None
print_doublylinkedlist(head)
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

# 6、在双链表头部删除元素，时间复杂度O(1)
# 删除头节点
if not head:
    raise Exception('empty linkedlist')
if not p.next:
    head = None
    tail = None
else:
    node = head
    head = node.next
    head.prev = None
    # 清理已删除节点的指针
    node.next = None
    node.prev = None
print_doublylinkedlist(head)
# 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5 -> 6

# 7、在双链表尾部删除元素，时间复杂度O(1)
# 删除尾节点
if not head:
    raise Exception('empty linkedlist')
# 找到尾结点
p = tail
# 把尾节点从链表中摘除
p.prev.next = None
p.prev = None
print_doublylinkedlist(head)
# 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5

```
##### **实现双链表 虚拟头尾节点**
```
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    # 虚拟头尾节点
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_first(self, e):
        node = ListNode(e)
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        self.size += 1

    def add_last(self, e):
        node = ListNode(e)
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node
        self.size += 1

    def add(self, index, e):
        if index < 0 or index > self.size:
            return

        # 找到index的前一个节点
        p = self.get_node(index - 1)
        node = ListNode(e)
        node.next = p.next
        node.next.prev = node
        p.next = node
        node.prev = p

        self.size += 1

    def remove_first(self):
        if self.size == 0:
            raise Exception("empty linked list")

        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head

        # 断开链接
        node.next = None
        node.prev = None

        self.size -= 1
        return node.val

    def remove_last(self):
        if self.size == 0:
            raise Exception("empty linked list")

        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail

        # 断开链接
        node.next = None
        node.prev = None

        self.size -= 1
        return node.val

    def remove(self, index):
        if index < 0 or index >= self.size:
            return

        # 找到index的前一个节点
        p = self.get_node(index - 1)

        node = p.next
        p.next = node.next
        node.next.prev = p

        # 断开链接
        node.next = None
        node.prev = None

        self.size -= 1
        return node.val

    def get_first(self):
        if self.size == 0:
            raise Exception("empty linked list")
        return self.head.next.val

    def get_last(self):
        if self.size == 0:
            raise Exception("empty linked list")
        return self.tail.prev.val

    def get(self, index):
        if self.size == 0:
            raise Exception("empty linked list")

        if index < 0 or index >= self.size:
            raise IndexError("Index: {}, Size: {}".format(index, self.size))

        # 找到index节点
        p = self.get_node(index)

        return p.val

    def get_node(self, index):
        p = self.head
        for _ in range(index + 1):
            p = p.next
        return p

    def set(self, index, e):
        if index < 0 or index >= self.size:
            raise IndexError("Index: {}, Size: {}".format(index, self.size))

        # 找到index节点
        p = self.get_node(index)

        old_val = p.val
        p.val = e
        return old_val

    def print_linkedlist(self):
        # 从头节点向后遍历双链表
        print('正向遍历：')
        p = self.head.next
        tail = None
        while p and p != self.tail:  # 当p不是虚拟尾节点时
            print(p.val, end=' ')
            tail = p
            p = p.next
        print()

        # 从尾节点向前遍历双链表
        print('反向遍历：')
        p = self.tail.prev
        while p and p != self.head:  # 当p不是虚拟头节点时
            print(p.val, end=' ')
            p = p.prev
        print('\n')


if __name__ == "__main__":
    list = DoublyLinkedList()
    list.add_first(1)
    list.add_first(2)
    list.add_last(3)
    list.add_last(4)
    list.print_linkedlist()
    # 2 1 3 4

    list.add(2, 5)
    list.print_linkedlist()
    # 2 1 5 3 4

    print(list.remove_first())  # 2
    list.print_linkedlist()  # 1 5 3 4

    print(list.remove_last())  # 4
    list.print_linkedlist()  # 1 5 3
    print(list.remove(1))  # 5
    list.print_linkedlist()  # 1 3

    print(list.get_first())  # 1
    print(list.get_last())  # 3
    print(list.get(1))  # 3

```
#### 跳表（了解）
已知索引节点的增删改查是O(1)，增删查改元素所需的时间复杂度O(N) 花在查找上，有2种方法降低时间复杂度：

* 借助键值映射，用 O(1)的时间直接拿到目标节点，参考哈希链表（LinkedHashMap）
* 跳表（Skip List），用额外的空间记录额外的信息，时间复杂度优化到 O(logN)  

普通单链表：

```
index  0  1  2  3  4  5  6  7  8  9
node   a->b->c->d->e->f->g->h->i->j
```
跳表：

```
indexLevel   0-----------------------8-----10
indexLevel   0-----------4-----------8-----10
indexLevel   0-----2-----4-----6-----8-----10
indexLevel   0--1--2--3--4--5--6--7--8--9--10
nodeLevel    a->b->c->d->e->f->g->h->i->j->k
```
增加了多层索引，每向上一层，索引节点的数量减少一半

计算机的两种存储方式，顺序存储（数组）和链式存储（链表），之后的所有数据结构都是基于这两种存储方式。

### 队列/栈
队列和栈都是「操作受限」的数据结构：**队列只能在一端插入元素，另一端删除元素；栈只能在某一端插入和删除元素**。更准确些，队列只允许在队尾插入元素，在队头删除元素，栈只允许在栈顶插入元素，从栈顶删除元素。

![](/personal-site-mvp/img/doc-placeholder.svg "")
```
# 队列的基本 API
class MyQueue:

    # 向队尾插入元素，时间复杂度 O(1)
    def push(self, e):
        pass

    # 从队头删除元素，时间复杂度 O(1)
    def pop(self):
        pass

    # 查看队头元素，时间复杂度 O(1)
    def peek(self):
        pass

    # 返回队列中的元素个数，时间复杂度 O(1)
    def size(self):
        pass

# 栈的基本 API
class MyStack:
    
    # 向栈顶插入元素，时间复杂度 O(1)
    def push(self, e):
        pass
    
    # 从栈顶删除元素，时间复杂度 O(1)
    def pop(self):
        pass
    
    # 查看栈顶元素，时间复杂度 O(1)
    def peek(self):
        pass
    
    # 返回栈中的元素个数，时间复杂度 O(1)
    def size(self):
        pass
```
#### 栈
##### 数组实现栈
```
# 用数组作为底层数据结构实现栈
class MyArrayStack:
    def __init__(self):
        self.list = []

    # 向栈顶加入元素，时间复杂度 O(1)
    def push(self, e):
        self.list.append(e)

    # 从栈顶弹出元素，时间复杂度 O(1)
    def pop(self):
        return self.list.pop()

    # 查看栈顶元素，时间复杂度 O(1)
    def peek(self):
        return self.list[-1]

    # 返回栈中的元素个数，时间复杂度 O(1)
    def size(self):
        return len(self.list)
```
##### 链表实现栈
```
from collections import deque

# 用链表作为底层数据结构实现栈
class MyLinkedStack:
    def __init__(self):
        self.list = deque()

    # 向栈顶加入元素，时间复杂度 O(1)
    def push(self, e):
        self.list.append(e)

    # 从栈顶弹出元素，时间复杂度 O(1)
    def pop(self):
        return self.list.pop()

    # 查看栈顶元素，时间复杂度 O(1)
    def peek(self):
        return self.list[-1]

    # 返回栈中的元素个数，时间复杂度 O(1)
    def size(self):
        return len(self.list)

```
#### 队列
##### 数组实现队列
```
class MyArrayQueue:
    def __init__(self):
        self.arr = CycleArray()

    def push(self, t):
        self.arr.add_last(t)

    def pop(self):
        return self.arr.remove_first()

    def peek(self):
        return self.arr.get_first()

    def size(self):
        return self.arr.size()
```
##### 链表实现队列
```
from collections import deque

# 用链表作为底层数据结构实现队列
class MyLinkedQueue:
    def __init__(self):
        self.list = deque()

    # 向队尾插入元素，时间复杂度 O(1)
    def push(self, e):
        self.list.append(e)

    # 从队头删除元素，时间复杂度 O(1)
    def pop(self):
        return self.list.popleft()

    # 查看队头元素，时间复杂度 O(1)
    def peek(self):
        return self.list[0]

    # 返回队列中的元素个数，时间复杂度 O(1)
    def size(self):
        return len(self.list)
```
##### 标准队列 queue.Queue
```
from queue import Queue

q = Queue()
q.put(1)    # 入队 (后端添加)
q.put(2)
item = q.get()  # 出队 (前端移除)，返回1
```
##### 双端队列 collections.deque
```
from collections import deque

# 创建队列
q = deque()

# 添加元素到队尾
q.append(1)
q.append(2)
q.append(3)

# 添加元素到队头
q.appendleft(0)

# 获取队列大小
print(len(q))  # 4

# 取出队头元素
item = q.popleft()  #  0

# 取出队尾元素
item = q.pop()  # 3
```
### 哈希表
```
# 哈希表伪码逻辑
class MyHashMap:

    def __init__(self):
        self.table = [None] * 1000

    # 增/改，复杂度 O(1)
    def put(self, key, value):
        index = self.hash(key)
        self.table[index] = value

    # 查，复杂度 O(1)
    def get(self, key):
        index = self.hash(key)
        return self.table[index]

    # 删，复杂度 O(1)
    def remove(self, key):
        index = self.hash(key)
        self.table[index] = None

    # 哈希函数，把 key 转化成 table 中的合法索引
    # 时间复杂度必须是 O(1)，才能保证上述方法的复杂度都是 O(1)
    def hash(self, key):
        # ...
        pass
```
#### 哈希函数
把 key 转化成 table 中的合法索引，性能很关键

**哈希特性**

* 哈希不变性：哈希值在对象生命周期内保持不变
* 哈希与相等性：如果 a == b，则 hash(a) == hash(b)，反过来不一定成立（哈希冲突是允许的）
* 不可变性与哈希：只有不可变对象可以是可哈希的
    * 可哈希：int, float, str, tuple, frozenset
    * 不可哈希：list, dict, set
    * Python 为不同内置类型提供了专门的哈希函数：
        * **整数**：直接使用整数值（除非是-1，会被特殊处理）
        * **浮点数**：基于 IEEE 754 浮点表示计算
        * **字符串**：使用 SipHash（Python 3.3 之前使用 FNV 算法，容易受到哈希碰撞攻击）
        * **元组**：基于其元素的哈希值组合计算



#### 哈希冲突
哈希冲突指两个不同的 key 通过哈希函数得到了相同的索引，解决哈希冲突：

![重点关注开放寻址法](/personal-site-mvp/img/doc-placeholder.svg "重点关注开放寻址法")
##### **拉链法**
哈希表的底层数组并不直接存储 `value` 类型，而是存储一个链表，当有多个不同的 `key` 映射到了同一个索引上，这些 `key -> value` 对儿就存储在这个链表中

```
class HashTable:
    def __init__(self, initial_size=10, load_factor=0.7):
        """初始化哈希表
        Args:
            initial_size: 初始哈希表大小
            load_factor: 触发扩容的负载因子阈值
        """
        self.size = initial_size
        self.load_factor = load_factor
        self.count = 0  # 记录当前元素数量
        self.table = [[] for _ in range(self.size)]  # 使用列表的列表实现拉链法

    def _hash(self, key):
        """哈希函数：计算键的哈希值"""
        return hash(key) % self.size

    def _resize(self, new_size):
        """调整哈希表大小"""
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        # 重新插入所有元素
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        """插入键值对"""
        # 检查是否需要扩容
        if self.count / self.size >= self.load_factor:
            self._resize(self.size * 2)  # 扩容为原来的两倍

        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        # 检查键是否已存在
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # 更新现有键的值
                return
        bucket.append((key, value))  # 添加新键值对
        self.count += 1

    def get(self, key):
        """获取键对应的值"""
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)  # 键不存在时抛出异常

    def remove(self, key):
        """删除键值对"""
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1

                # 可选：如果元素太少，可以缩容
                if self.size > 10 and self.count / self.size < 0.2:
                    self._resize(max(10, self.size // 2))
                return
        raise KeyError(key)  # 键不存在时抛出异常

    def __setitem__(self, key, value):
        """支持使用 ht[key] = value 语法"""
        self.put(key, value)

    def __getitem__(self, key):
        """支持使用 value = ht[key] 语法"""
        return self.get(key)

    def __delitem__(self, key):
        """支持使用 del ht[key] 语法"""
        self.remove(key)

    def __str__(self):
        """打印哈希表内容"""
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table) if bucket)


# 测试代码
if __name__ == "__main__":
    # 使用小初始大小测试扩容
    ht = HashTable(initial_size=3, load_factor=0.7)

    print("初始空哈希表:")
    print(ht)

    # 添加键值对
    print("\n添加元素:")
    ht.put("apple", 10)
    ht.put("banana", 20)
    print("添加apple(10)和banana(20)后:")
    print(ht)

    # 触发扩容
    print("\n触发扩容:")
    ht.put("orange", 30)
    ht["grape"] = 40  # 使用 __setitem__ 语法
    print("添加orange(30)和grape(40)后(已扩容):")
    print(ht)
    print(f"当前哈希表大小: {ht.size}")

    # 获取值
    print("\n获取值:")
    print("apple:", ht.get("apple"))
    print("banana:", ht["banana"])  # 使用 __setitem__ 语法

    # 更新值
    ht["banana"] = 25
    print("\n更新后的banana值:", ht["banana"])

    # 删除键
    del ht["orange"]
    print("\n删除orange后的哈希表:")
    print(ht)

    # 测试异常处理
    try:
        print(ht["nonexistent"])
    except KeyError as e:
        print(f"\n键错误: {e} 不存在")
```
##### **线性探查法**（**开放寻址法**）
一个 `key` 发现算出来的 `index` 值已经被别的 `key` 占了，那么它就去 `index + 1` 的位置看看，如果还是被占了，就继续往后找，直到找到一个空的位置为止。

* 环形数组技巧：确保所有槽位都能被探查到、避免数组越界
* 删除操作复杂性：
    * 数据搬移避免空洞
    * 占位符标记删除（大多数情况）， 可通过定期重新哈希(rehashing)来清理标记


|特性|数据搬移法|占位符标记法|
|-|-|-|
|实现复杂度|高|低|
|删除时间复杂度|O(n)|O(1)|
|空间效率|高（无额外标记）|低（需要存储标记）|
|查找性能|稳定|可能下降（需跳过标记）|
|适合场景|小规模数据或删除不频繁|大规模数据或删除频繁|

```
class HashTable:
    def __init__(self, initial_size=10, load_factor=0.7):
        """初始化哈希表
        Args:
            initial_size: 初始哈希表大小
            load_factor: 触发扩容的负载因子阈值
        """
        self.size = initial_size
        self.load_factor = load_factor
        self.count = 0  # 记录当前元素数量
        self.table = [None] * self.size  # 使用None表示空槽位
        self.DELETED = object()  # 删除标记对象

    def _hash(self, key):
        """哈希函数：计算键的哈希值"""
        return hash(key) % self.size

    def _resize(self, new_size):
        """调整哈希表大小"""
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0

        # 重新插入所有有效元素（跳过DELETED标记）
        for item in old_table:
            if item is not None and item is not self.DELETED:
                self.put(item[0], item[1])
        print(f"Resized to {self.size}")

    def _find_slot(self, key):
        """查找键对应的槽位或可插入的槽位
        返回：(槽位索引, 是否找到键)
        """
        hash_key = self._hash(key)

        # 线性探查（使用环形数组技巧）
        for i in range(self.size):
            current = (hash_key + i) % self.size  # 环形处理
            item = self.table[current]

            if item is None or item is self.DELETED:
                # 找到空槽或已删除槽位，可以插入
                return current, False
            elif item[0] == key:
                # 找到键
                return current, True

        # 表已满（理论上不会执行到这里，因为有扩容机制）
        raise Exception("Hash table is full")

    def put(self, key, value):
        """插入键值对"""
        # 检查是否需要扩容
        if self.count / self.size >= self.load_factor:
            self._resize(self.size * 2)  # 扩容为原来的两倍

        index, found = self._find_slot(key)

        if found:
            # 键已存在，更新值
            self.table[index] = (key, value)
        else:
            # 插入新键值对
            self.table[index] = (key, value)
            self.count += 1

    def get(self, key):
        """获取键对应的值"""
        index, found = self._find_slot(key)
        if found:
            return self.table[index][1]
        raise KeyError(key)  # 键不存在时抛出异常

    def remove(self, key):
        """删除键值对"""
        index, found = self._find_slot(key)
        if found:
            self.table[index] = self.DELETED  # 标记为已删除
            self.count -= 1

            # 可选：如果元素太少，可以缩容
            if self.size > 10 and self.count / self.size < 0.2:
                self._resize(max(10, self.size // 2))
        else:
            raise KeyError(key)  # 键不存在时抛出异常

    def __setitem__(self, key, value):
        """支持使用 ht[key] = value 语法"""
        self.put(key, value)

    def __getitem__(self, key):
        """支持使用 value = ht[key] 语法"""
        return self.get(key)

    def __delitem__(self, key):
        """支持使用 del ht[key] 语法"""
        self.remove(key)

    def __str__(self):
        """打印哈希表内容"""
        items = []
        for i, item in enumerate(self.table):
            if item is not None and item is not self.DELETED:
                items.append(f"{i}: {item} - {hash(item[0]) % self.size}")
            elif item is self.DELETED:
                items.append(f"{i}: <DELETED>")
            else:
                items.append(f"{i}: <EMPTY>")
        return "\n".join(items)


# 测试代码
if __name__ == "__main__":
    # 使用小初始大小测试扩容
    ht = HashTable(initial_size=3, load_factor=0.7)

    print("初始空哈希表:")
    print(ht)

    # 添加键值对
    print("\n添加元素:")
    ht.put("apple", 10)
    ht.put("banana", 20)
    print("添加apple(10)和banana(20)后:")
    print(ht)

    # 触发扩容
    print("\n触发扩容:")
    ht.put("orange", 30)
    ht["grape"] = 40  # 使用 __setitem__ 语法
    print("添加orange(30)和grape(40)后(已扩容):")
    print(ht)
    print(f"当前哈希表大小: {ht.size}")

    # 获取值
    print("\n获取值:")
    print("apple:", ht.get("apple"))
    print("banana:", ht["banana"])  # 使用 __setitem__ 语法

    # 更新值
    ht["banana"] = 25
    print("\n更新后的banana值:", ht["banana"])

    # 删除键
    del ht["orange"]
    print("\n删除orange后的哈希表:")
    print(ht)

    # 测试异常处理
    try:
        print(ht["nonexistent"])
    except KeyError as e:
        print(f"\n键错误: {e} 不存在")

```
##### 扩容和负载因子
拉链法和线性探查法虽然能解决哈希冲突的问题，但是它们会导致性能下降。因为：1 哈希函数设计的不好，多个key映射到了同一个索引（编程语言标准库大佬已经优化好了，没啥改进空间） ；2 哈希表装太满，为了避免太满，引入负载因子 ，当哈希表负载因子达到阈值时，哈希表会扩容。

负载因子  =  key-value 对的数量 / 哈希表底层数组的容量

|语言/实现|默认负载因子|扩容策略|
|-|-|-|
|Python|2/3 (~0.67)|容量×4（小表）或×2（大表）|
|Java HashMap|0.75|容量×2|

#### 哈希集合
哈希集合主要通过 `set` 类型实现，`set` 是一个无序的、不重复的元素集合，基于哈希表实现。

```
# 创建空集合
empty_set = set()

# 创建带有初始元素的集合
fruits = {'apple', 'banana', 'orange'}
numbers = set([1, 2, 3, 4, 5])  # 从列表创建

# 添加元素
fruits = {'apple', 'banana'}
fruits.add('orange')       # 添加单个元素
fruits.update(['kiwi', 'mango'])  # 添加多个元素

# 删除
fruits.remove('banana')    # 如果元素不存在会引发KeyError
fruits.discard('banana')  # 如果元素不存在不会报错
popped = fruits.pop()     # 随机删除并返回一个元素
fruits.clear()            # 清空集合

# 集合运算
a = {1, 2, 3}
b = {2, 3, 4}
# 并集
union = a | b  # 或 a.union(b)
# 交集
intersection = a & b  # 或 a.intersection(b)
# 差集
difference = a - b  # 或 a.difference(b)  # 1
# 对称差集（仅在其中一个集合中的元素）
symmetric_diff = a ^ b  # 或 a.symmetric_difference(b)  # 1，4
```
#### 哈希链表
哈希表中的 `key` 是无序的，结合链表的优点，使**键的遍历顺序就是键的插入顺序**

Python 3.7+ 中普通 `dict` 也保持插入顺序，`OrderedDict` 提供了 `move_to_end()` 等额外方法。插入、查找、删除、获取最旧的时间复杂度都是O(1)，应用于需要快速访问又需要维护顺序的场景：

* **LRU 缓存**：最近最少使用缓存淘汰算法
* **有序字典**：需要维护插入顺序的字典
* **撤销操作**：维护操作历史记录
* **消息队列**：需要维护顺序的消息处理



```
from collections import OrderedDict

# 创建有序字典
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 从普通字典创建（Python 3.7+保留顺序）
d = {'a': 1, 'b': 2, 'c': 3}
od = OrderedDict(d)

# 指定的键移动到字典的一端
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od.move_to_end('a')     # 移动到末尾
# OrderedDict([('b', 2), ('c', 3), ('a', 1)])
od.move_to_end('c', last=False)  # 移动到开头
# OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# 移除并返回一个键值对
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od.popitem()      # 返回 ('c', 3)
od.popitem(last=False)  # 返回 ('a', 1)
```
|特性|OrderedDict|普通字典 (Python 3.7+)|
|-|-|-|
|保持插入顺序|是|是|
|相等性考虑顺序|是|否|
|move_to_end()方法|有|无|
|popitem(last=False)|支持|不支持|
|内存占用|稍高|较低|

##### 实现LRU缓存
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
        self.ord.remove(key)  # 也可以用OrderedDict就不用定义ord了
        self.ord.append(key)
        return self.data.get(key)


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.data and len(self.data) == self.capacity:
                # 满了
                del_key = self.ord.popleft()
                del self.data[del_key]
        
        if key in self.data:
            self.ord.remove(key)
        self.data[key] = value
        self.ord.append(key)
```
### 二叉树
常见类型：

|类型|描述|图例|备注|
|-|-|-|-|
|完全二叉树|满的|![](/personal-site-mvp/img/doc-placeholder.svg "")|总节点数 = 2^ n - 1|
|满二叉树|二叉树的每一层的节点都紧凑靠左排列，且除了最后一层，其他每层都必须是满的:完全二叉树的左右子树也是完全二叉树完全二叉树的左右子树中，至少有一棵是满二叉树|![](/personal-site-mvp/img/doc-placeholder.svg "")|父子节点的索引存在明显的规律完全二叉树可以用数组来存储，不需要真的构建链式节点线段树、二叉堆|
|二叉搜索树（Binary Search Tree，简称 BST）|左子树的每个节点的值都要小于这个节点的值，右子树的每个节点的值都要大于这个节点的值|    7
   / \
  4   9
 / \   \
1   5   10|方便搜索|
|平衡二叉树（Balanced Binary Tree）|「每个节点」的左右子树的高度差不超过 1||假设平衡二叉树中共有 N个节点，那么平衡二叉树的高度是 O(log N)|
|自平衡二叉树|在增删二叉树节点时，对树的结构进行一些调整，使得树始终是平衡的保持树的平衡性，最关键的就是「旋转」操作||红黑树，一种自平衡的二叉搜索树|

表示：

```
    1
   / \
  2   3
 /   / \
4   5   6
```


```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```


邻接表：

```
tree = {
    1: [2, 3],
    2: [4],
    3: [5, 6]
}
```
#### 遍历
DFS（深度优先搜索，Depth-First Search）常用来寻找**所有路径**，而 BFS（广度优先搜索）通常用于寻找**最短路径**

##### 递归遍历（DFS）
**DFS **常用来寻找所有路径，DFS 会尽可能深地探索一条路径，直到无法继续深入，然后回溯并尝试其他分支。

```
# 基本的二叉树节点
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树的递归遍历框架
def traverse(root: TreeNode):
    if root is None:
        return
    traverse(root.left)
    traverse(root.right)
```
递归遍历二叉树节点的顺序是固定的，但是有三个关键位置，在不同位置插入代码，会产生不同的效果。

###### 前/中/后序遍历
前序位置的代码会在进入节点时立即执行；中序位置的代码会在左子树遍历完成后，遍历右子树之前执行；后序位置的代码会在左右子树遍历完成后执行

```
# 二叉树的遍历框架
def traverse(root):
    if root is None:
        return
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置
```
##### 层序遍历（BFS ）
**BFS **常用来寻找最短路径

* **DFS** 可能会沿着一条路径无限深入，尤其在存在环路或无限分支时，无法保证最短路径。
* **BFS** 的层级遍历特性天然适合最短路径问题。逐层扩展，保证首次到达即最短

```
    1
   / \
  2   3
 /   / \
4   5   6
```
层序遍历使用 **队列** 按层级顺序遍历节点

```
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    if root is None:
        return

    result = []
    q = deque([root])

    while q:
        cur = q.popleft()
        result.append(cur.val)

        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return result

# 构造二叉树：
#       1
#      /  \
#     2    4
#    / \
#   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)

print(bfs(root))
# [1, 2, 4, 5, 6]
```
写法1：最简单，每次把队头元素拿出来，然后把它的左右子节点加入队列

缺点：无法知道当前节点在第几层，比方收集每一层的节点，或者计算二叉树的最小深度等等

```

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# 构造二叉树：
#       1
#      /  \
#     2    4
#    / \
#   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)

print(bfs(root))
# 输出：[[1], [2, 4], [5, 6]]
```
写法2：最常用的层序遍历写法

无权图，二叉树中每个节点的深度，其实就是从根节点到这个节点的路径权重和

```
class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth  # 路径权重和

def bfs(root):
    if root is None:
        return
    q = deque()
    # 根节点的路径权重和是 1
    q.append(State(root, 1))

    while q:
        cur = q.popleft()
        # 访问 cur 节点，同时知道它的路径权重和
        print(f"depth = {cur.depth}, val = {cur.node.val}")

        # 把 cur 的左右子节点加入队列
        if cur.node.left is not None:
            q.append(State(cur.node.left, cur.depth + 1))
        if cur.node.right is not None:
            q.append(State(cur.node.right, cur.depth + 1))
```
写法3：扩展写法，假如路径的权重不是1，让每个节点自己负责维护自己的路径权重和

扩展性更好，带有权重的场景属于图结构算法，在Dijkstra中会用到

#### 多叉树
|二叉树|多叉树|
|-|-|
|class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right|class Node:
    def __init__(self, val: int):
        self.val = val
        self.children = []|

**递归遍历**

```
def preorder_traversal(root: Node) -> list[int]:
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)  # 前序位置
        for child in node.children:
            dfs(child)  # 递归访问子节点
        # result.append(node.val)  # 后序位置
    
    dfs(root)
    return result
```
**层序遍历**

```
from collections import deque


class Node:
    def __init__(self, val: int):
        self.val = val
        self.children = []


def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            current_level.append(node.val)
            # 将该节点的所有子节点加入队列
            for child in node.children:
                queue.append(child)

        result.append(current_level)

    return result


# 构造多叉树：
#        1
#      / | \
#     2  3  4
#    / \
#   5   6
root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]

print(bfs(root))
# 输出：[[1], [2, 3, 4], [5, 6]]
```
#### 二叉搜索树 BST
适用于需要有序键值对的场景，如范围查询、排名统计等。

```
class TreeNode:
    """树节点类，表示二叉搜索树中的一个节点"""

    def __init__(self, key, value):
        self.key = key  # 键，用于比较和查找
        self.value = value  # 值，与键关联的数据
        self.left = None  # 左子节点
        self.right = None  # 右子节点
        self.size = 1  # 以该节点为根的子树中的节点总数


class MyTreeMap:
    """基于二叉搜索树实现的键值对映射"""

    def __init__(self):
        self.root = None  # 根节点

    def __len__(self):
        """返回树中元素的数量"""
        return self._size(self.root)

    def _size(self, node):
        """返回节点的子树大小"""
        return node.size if node else 0

    def is_empty(self):
        """检查树是否为空"""
        return self.root is None

    # ---------- 增/改操作 ---------- 复杂度 O(logN)
    def put(self, key, value):
        """插入键值对（如果键已存在则更新值）"""
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        """递归辅助方法：在子树中插入键值对"""
        if node is None:
            return TreeNode(key, value)

        if key == node.key:  # 键已存在，更新值
            node.value = value
        elif key < node.key:  # 向左子树插入
            node.left = self._put(node.left, key, value)
        else:  # 向右子树插入
            node.right = self._put(node.right, key, value)

        # 更新子树大小
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    # ---------- 查询操作 ---------- 复杂度 O(logN)
    def get(self, key):
        """根据键查找值，若键不存在则返回None"""
        return self._get(self.root, key)

    def _get(self, node, key):
        """递归辅助方法：在子树中查找键"""
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    def contains_key(self, key):
        """检查键是否存在"""
        return self.get(key) is not None

    # ---------- 删除操作 ---------- 复杂度 O(logN)
    def remove(self, key):
        """删除指定键的节点"""
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        """递归辅助方法：在子树中删除键"""
        if node is None:
            return None

        if key < node.key:  # 目标在左子树
            node.left = self._remove(node.left, key)
        elif key > node.key:  # 目标在右子树
            node.right = self._remove(node.right, key)
        else:  # 找到目标节点
            if node.left is None:  # 只有右子节点或无子节点
                return node.right
            elif node.right is None:  # 只有左子节点
                return node.left
            else:  # 有两个子节点
                # 找到右子树的最小节点替代当前节点
                min_node = self._find_min(node.right)
                node.key, node.value = min_node.key, min_node.value
                node.right = self._delete_min(node.right)

        # 更新子树大小
        if node:
            node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _delete_min(self, node):
        """删除子树中的最小节点"""
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _find_min(self, node):
        """找到子树中的最小节点"""
        while node.left is not None:
            node = node.left
        return node

    # ---------- 最小/最大键操作 ---------- 复杂度 O(logN)
    def find_min(self):
        """查找并返回最小键"""
        if self.root is None:
            return None
        min_node = self._find_min(self.root)
        return min_node.key

    def find_max(self):
        """查找并返回最大键"""
        if self.root is None:
            return None
        return self._find_max(self.root).key

    def _find_max(self, node):
        """找到子树中的最大节点"""
        while node.right is not None:
            node = node.right
        return node

    # ---------- 排名相关操作 ---------- 复杂度 O(logN)
    def select(self, k):
        """
        查找排名为k的键（0-based）
        排名k表示有k个键比它小
        """
        if k < 0 or k >= len(self):
            raise IndexError("index out of range")
        node = self._select(self.root, k)
        return node.key

    def _select(self, node, k):
        """递归辅助方法：在子树中查找排名为k的节点"""
        if node is None:
            return None

        left_size = self._size(node.left)
        if k < left_size:  # 在左子树中
            return self._select(node.left, k)
        elif k > left_size:  # 在右子树中
            return self._select(node.right, k - left_size - 1)
        else:  # 找到目标节点
            return node

    def rank(self, key):
        """
        查找键key的排名（0-based）
        返回小于key的键的数量
        """
        return self._rank(self.root, key)

    def _rank(self, node, key):
        """递归辅助方法：计算键的排名"""
        if node is None:
            return 0

        if key < node.key:  # 在左子树中
            return self._rank(node.left, key)
        elif key > node.key:  # 在右子树中
            return 1 + self._size(node.left) + self._rank(node.right, key)
        else:  # 找到键
            return self._size(node.left)

    # ---------- 有序键集合操作 ---------- 复杂度 O(N)
    def keys(self):
        """返回所有键的有序集合"""
        keys = []
        self._inorder_traversal(self.root, keys)
        return keys

    def _inorder_traversal(self, node, keys):
        """中序遍历辅助方法"""
        if node is None:
            return
        self._inorder_traversal(node.left, keys)
        keys.append(node.key)
        self._inorder_traversal(node.right, keys)


# 构造测试树
tree = MyTreeMap()
keys = [5, 3, 7, 2, 4, 6, 8]
for k in keys:
    tree.put(k, f"value-{k}")

# 测试基本功能
print("===== 基本功能测试 =====")
print(f"树的大小: {len(tree)}")
print(f"查找键5的值: {tree.get(5)}")
print(f"查找不存在的键1: {tree.get(1)}")
print(f"是否包含键3: {tree.contains_key(3)}")
print(f"是否包含键10: {tree.contains_key(10)}")

# 测试最小/最大键
print("\n===== 最小/最大键测试 =====")
print(f"最小键: {tree.find_min()}")
print(f"最大键: {tree.find_max()}")

# 测试排名相关
print("\n===== 排名相关测试 =====")
print("键的排名:")
for k in sorted(keys):
    print(f"  {k} 的排名: {tree.rank(k)}")

print("\n按排名查找键:")
for i in range(len(keys)):
    print(f"  排名{i}的键: {tree.select(i)}")

# 测试删除
print("\n===== 删除测试 =====")
tree.remove(3)
print("删除后是否包含键3:", tree.contains_key(3))
print("删除后键的集合:", tree.keys())

# 测试所有键
print("\n===== 所有键测试 =====")
print("所有键(有序):", tree.keys())

# 边界测试
print("\n===== 边界测试 =====")
print("空树的最小键:", MyTreeMap().find_min())
print("空树的最大键:", MyTreeMap().find_max())
print("空树的键集合:", MyTreeMap().keys())

try:
    print("\n尝试查找超出范围的排名:")
    tree.select(100)
except IndexError as e:
    print(f"  捕获到预期异常: {e}")
```
普通二叉搜索树最关键的问题是它不会自动对树进行平衡，特殊的情况下（插入有序键值对）会退化成链表，增删查改的时间复杂度退化为 O(N)。

#### 红黑树
红黑树是自平衡的二叉搜索树，它的树高在任何时候都能保持在 O(logN)（完美平衡），这样就能保证增删查改的时间复杂度都是 O(logN)

![](/personal-site-mvp/img/doc-placeholder.svg "")
特点：

* 每个节点是红色或黑色** “非红即黑”**
* 根节点是黑色，所有叶子节点（NIL节点）是黑色 **“首尾全黑”**
* 红色节点的两个子节点都是黑色（不能有连续的红色节点）** “红子双黑”**
* 从任一节点到其每个叶子节点的所有路径都包含相同数目的黑色节点 **“路径等黑”**

**查找**跟二叉平衡树的查找无异

**插入**操作包括两部分工作：一查找插入的位置；二插入红节点后自平衡。红黑树总是通过旋转和变色达到自平衡：

![对p左旋 右旋](/personal-site-mvp/img/doc-placeholder.svg "对p左旋 右旋")
修复右倾红链接: 左黑右红

**左旋：**以某个结点作为旋转结点，拎起其右子结点变为旋转结点的父结点，右子结点的左子结点变为旋转结点的右子结点。

```
def rotate_left(self, h):
    """左旋转"""
    print("rotate_left")
    x = h.right
    h.right = x.left
    x.left = h
    x.color = h.color
    h.color = RED
    return x
```
修复连续两个左红链接：左红左左红

**右旋：**以某个结点作为旋转结点，拎起其左子结点变为旋转结点的父结点，左子结点的右子结点变为旋转结点的左子结点。

```
def rotate_right(self, h):
    """右旋转"""
    print("rotate_right")
    x = h.left
    h.left = x.right
    x.right = h
    x.color = h.color
    h.color = RED
    return x
```
处理两个子节点都是红链接：左红右红

**颜色翻转**：

```
def flip_colors(self, h):
    """颜色翻转"""
    print("flip_colors")
    h.color = not h.color
    h.left.color = not h.left.color
    h.right.color = not h.right.color
```


```
# 定义节点颜色常量
RED = True
BLACK = False


class RBNode:
    """红黑树节点类"""

    def __init__(self, key, value, color=RED):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = color  # 新节点默认为红色


class RedBlackTree:
    """红黑树实现"""

    def __init__(self):
        self.root = None

    def is_red(self, node):
        """检查节点是否为红色"""
        return node is not None and node.color == RED

    def rotate_left(self, h):
        """左旋转"""
        print("rotate_left")
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x

    def rotate_right(self, h):
        """右旋转"""
        print("rotate_right")
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def flip_colors(self, h):
        """颜色翻转"""
        print("flip_colors")
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def put(self, key, value):
        """插入键值对"""
        self.root = self._put(self.root, key, value)
        self.root.color = BLACK  # 根节点始终为黑色

    def _put(self, h, key, value):
        """递归插入辅助方法"""
        if h is None:
            return RBNode(key, value, RED)  # 新节点总是红色

        # 标准BST插入
        if key < h.key:
            h.left = self._put(h.left, key, value)
        elif key > h.key:
            h.right = self._put(h.right, key, value)
        else:
            h.value = value  # 键已存在，更新值

        # 修复右倾红链接
        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        # 修复连续两个左红链接
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        # 处理两个子节点都是红链接的情况
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)

        return h

    def get(self, key):
        """查找键对应的值(非递归实现)"""
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.value
        return None

    def __str__(self):
        """返回红黑树的字符串表示，格式如：
            5黑
           /   \
          3红   7红
        """
        if self.root is None:
            return "空树"
        lines = self._build_tree_string(self.root)
        return "\n".join(lines)

    def _build_tree_string(self, node):
        """递归构建树的字符串表示"""
        if node is None:
            return []

        # 获取节点颜色
        color = "红" if self.is_red(node) else "黑"
        node_str = f"{node.key}{color}"

        # 叶子节点直接返回
        if node.left is None and node.right is None:
            return [node_str]

        # 递归构建左右子树的字符串
        left_lines = self._build_tree_string(node.left)
        right_lines = self._build_tree_string(node.right)

        # 计算左右子树宽度
        left_width = max(len(line) for line in left_lines) if left_lines else 0
        right_width = max(len(line) for line in right_lines) if right_lines else 0

        # 构建当前节点的字符串表示
        new_lines = []
        # 第一行：当前节点，居中显示
        node_line = node_str.center(left_width + right_width + 2)
        new_lines.append(node_line)

        # 第二行：连接线
        if left_lines or right_lines:
            connector_line = ""
            if left_lines:
                connector_line += "/".rjust(left_width)
            else:
                connector_line += " " * left_width

            connector_line += " " * len(node_str)

            if right_lines:
                connector_line += "\\".ljust(right_width)
            else:
                connector_line += " " * right_width

            new_lines.append(connector_line)

        # 合并左右子树的字符串
        max_lines = max(len(left_lines), len(right_lines))
        for i in range(max_lines):
            left_line = left_lines[i] if i < len(left_lines) else " " * left_width
            right_line = right_lines[i] if i < len(right_lines) else " " * right_width
            combined_line = left_line + " " * len(node_str) + right_line
            new_lines.append(combined_line)

        return new_lines


if __name__ == "__main__":
    rbt = RedBlackTree()
    # 测试数据调整为能产生红色节点的序列
    keys = [43, 45, 49, 56, 58, 60, 64, 68, 72]
    for k in keys:
        rbt.put(k, f"value-{k}")

    print("红黑树结构:")
    print(rbt)
    # 红黑树结构:
    #            56黑            
    #         /   \              
    #   45黑           68黑      
    #   /   \             /   \  
    # 43黑   49黑     60红      72黑
    #               /   \        
    #             58黑   64黑     

    print("\n插入66:")
    rbt.put(66, f"value-{66}")
    print(rbt)
    # 插入66:
    # rotate_left
    #              56黑             
    #         /   \                 
    #   45黑             68黑       
    #   /   \                /   \  
    # 43黑   49黑       60红       72黑
    #               /   \           
    #             58黑    66黑       
    #                     /         
    #                   64红    

    print("\n插入65:")
    rbt.put(65, f"value-{65}")
    print(rbt)
    # 插入65:
    # rotate_left
    # rotate_right
    # flip_colors
    # rotate_left
    # rotate_right
    # flip_colors
    # rotate_left
    #               65黑               
    #                     /   \        
    #         56红              68黑   
    #         /   \             /   \  
    #   45黑        60黑      66黑   72黑
    #   /   \       /   \              
    # 43黑   49黑   58黑   64黑    

    print("\n插入70:")
    rbt.put(70, f"value-{70}")
    print(rbt)
    # 插入70:
    #                 65黑                
    #                     /   \           
    #         56红                68黑    
    #         /   \             /   \     
    #   45黑        60黑      66黑    72黑 
    #   /   \       /   \             /   
    # 43黑   49黑   58黑   64黑         70红   

    print("\n查找测试:")
    print("key 60:", rbt.get(60))

```
**AVL树：**AVL树（Adelson-Velsky和Landis树）是最早发明的自平衡二叉搜索树。它通过维护**平衡因子**（左右子树高度差不超过1）来保证树的平衡性，确保最坏情况下查找、插入和删除操作的时间复杂度都是O(log n)。

|特性|AVL树|红黑树|
|-|-|-|
|平衡严格度|严格平衡（高度差≤1）|宽松平衡（最长路径≤2倍最短路径）|
|性能|查找：AVL树更快（因为更平衡）|插入/删除：红黑树更快（旋转操作更少）|
|适用场景|查找密集型（如数据库索引）|增删频繁（如语言库的Map/Set实现）|

#### Trie/字典树/前缀树
Trie 树是一种针对字符串进行特殊优化的数据结构，又被叫做字典树、前缀树。是多叉树结构的延伸。

```
class TrieNode:
    def __init__(self):
        self.children = {}  # 子节点字典
        self.is_end = False  # 标记是否为单词结尾


class Trie:
    def __init__(self):
        self.root = TrieNode()  # 根节点
        self.word_count = 0  # 单词计数

    def insert(self, word: str) -> None:
        """插入单词到字典树"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if not node.is_end:  # 避免重复计数，有可能插入的单词已经存在于字典树中
            self.word_count += 1
        node.is_end = True

    def search(self, word: str) -> bool:
        """搜索单词是否在字典树中"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """检查是否有单词以给定前缀开头"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word: str) -> None:
        """从字典树中删除单词"""

        def _delete_helper(node, word, index):
            # 递归终止条件：到达单词末尾
            if index == len(word):
                if not node.is_end:
                    return False  # 单词不存在
                    
                node.is_end = False
                self.word_count -= 1
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False  # 单词不存在

            should_delete_child = _delete_helper(node.children[char], word, index + 1)

            # 若子节点可删除，则清理当前节点的子节点
            if should_delete_child:
                del node.children[char]
                # 当前节点是否可被父节点删除？（无子节点且非单词结尾）
                return len(node.children) == 0 and not node.is_end

            return False

        _delete_helper(self.root, word, 0)

    def get_all_words(self) -> list:
        """获取字典树中所有单词"""
        words = []
        self._dfs(self.root, '', words)
        return words

    def autocomplete(self, prefix: str) -> list:
        """返回所有以给定前缀开头的单词"""
        node = self.root
        # 先遍历到前缀的最后一个节点
        for char in prefix:
            if char not in node.children:
                return []  # 前缀不存在，返回空列表
            node = node.children[char]

        # 从当前节点开始收集所有单词
        words = []
        self._dfs(node, prefix, words)
        return words

    def _dfs(self, node, current_word, words):
        """从当前节点开始收集所有单词"""
        if node.is_end:
            words.append(current_word)
        for char, child_node in node.children.items():
            self._dfs(child_node, current_word + char, words)

    def longest_common_prefix(self) -> str:
        """返回字典树中所有单词的最长公共前缀"""
        if not self.root.children:
            return ""

        prefix = []
        node = self.root
        # 当节点只有一个子节点且不是单词结尾时，继续向下
        while len(node.children) == 1 and not node.is_end:
            char = list(node.children.keys())[0]
            prefix.append(char)
            node = node.children[char]
        return "".join(prefix)


if __name__ == "__main__":
    trie = Trie()

    # 插入测试单词
    test_words = ["apple", "app", "application", "banana", "ball", "bat"]
    for word in test_words:
        trie.insert(word)

    print("=== autocomplete 测试 ===")
    print("前缀 'app':", trie.autocomplete("app"))  # ['app', 'apple', 'application']
    print("前缀 'ba':", trie.autocomplete("ba"))  # ['banana', 'ball', 'bat']
    print("前缀 'x':", trie.autocomplete("x"))  # []
    print("前缀 'appl':", trie.autocomplete("appl"))  # ['apple', 'application']

    print("\n=== longest_common_prefix 测试 ===")
    print("当前Trie的最长公共前缀:", trie.longest_common_prefix())  # "" (因为'app'和'ba'开头不同)

    # 测试只有共同前缀的情况
    trie2 = Trie()
    trie2.insert("apple")
    trie2.insert("app")
    trie2.insert("application")
    print("\n只有'app'开头的Trie的最长公共前缀:", trie2.longest_common_prefix())  # "app"

    # 测试空Trie
    trie3 = Trie()
    print("空Trie的最长公共前缀:", trie3.longest_common_prefix())  # ""

    # 测试单单词Trie
    trie4 = Trie()
    trie4.insert("hello")
    print("单单词Trie的最长公共前缀:", trie4.longest_common_prefix())  # "hello"

```
#### 二叉堆/优先级队列
二叉堆（Binary Heap）是一种特殊的**完全二叉树：**

* 除了最后一层，其他层都是完全填满的，最后一层的节点尽可能靠左排列
* **可以用数组存储**：由于是完全二叉树，可以用**数组**高效存储，无需指针，对于索引 `i` 的节点：
    * **父节点**：`parent(i) = (i - 1) // 2`
    * **左子节点**：`left_child(i) = 2i + 1`
    * **右子节点**：`right_child(i) = 2i + 2`


最小堆

```
        1
       / \
      3   2
     / \ / \
    5  4 6  7
```
最大堆

```
        7
       / \
      5   6
     / \ / \
    3  4 2  1
```
二叉堆的主要操作就两个：下沉和 上浮，用以维护二叉堆的性质。

|操作|时间复杂度|说明|
|-|-|-|
|插入（Insert）|O(log n)|插入到末尾，然后上浮（`sift_up`）|
|删除堆顶（Extract）|O(log n)|移除堆顶，用最后一个元素替换，然后下沉（`sift_down`）|
|查看堆顶（Peek）|O(1)|直接返回 `heap[0]`|
|构建堆（Build Heap）|O(n)|从无序数组构建堆（Floyd算法）|
|堆排序（Heap Sort）|O(n log n)|先建堆，再逐个提取|

```
class BinaryHeap:
    def __init__(self, heap_type='min'):
        """
        初始化二叉堆
        :param heap_type: 'min'表示最小堆，'max'表示最大堆
        """
        self.heap = []
        self.heap_type = heap_type

    def parent(self, index):
        """返回父节点的索引"""
        return (index - 1) // 2

    def left_child(self, index):
        """返回左子节点的索引"""
        return 2 * index + 1

    def right_child(self, index):
        """返回右子节点的索引"""
        return 2 * index + 2

    def compare(self, a, b):
        """比较函数，根据堆类型决定比较方式"""
        if self.heap_type == 'min':
            return a < b
        else:
            return a > b

    def insert(self, value):
        """插入元素"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        """上浮操作"""
        while index > 0 and self.compare(self.heap[index], self.heap[self.parent(index)]):
            # 交换当前节点与父节点
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract(self):
        """提取堆顶元素"""
        if not self.heap:
            return None

        root = self.heap[0]
        # 将最后一个元素移到堆顶
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # 下沉堆顶元素
        self._sift_down(0)
        return root

    def _sift_down(self, index):
        """下沉操作"""
        min_max_index = index

        left = self.left_child(index)
        if left < len(self.heap) and self.compare(self.heap[left], self.heap[min_max_index]):
            min_max_index = left

        right = self.right_child(index)
        if right < len(self.heap) and self.compare(self.heap[right], self.heap[min_max_index]):
            min_max_index = right

        if index != min_max_index:
            # 交换当前节点与更小/更大的子节点
            self.heap[index], self.heap[min_max_index] = self.heap[min_max_index], self.heap[index]
            self._sift_down(min_max_index)

    def peek(self):
        """查看堆顶元素但不移除"""
        return self.heap[0] if self.heap else None

    def size(self):
        """返回堆的大小"""
        return len(self.heap)

    def is_empty(self):
        """判断堆是否为空"""
        return len(self.heap) == 0

    def build_heap(self, array):
        """从一个数组构建堆"""
        self.heap = array.copy()
        # 从最后一个非叶子节点开始下沉 时间复杂度是O(n) 而不是O(nlogn)
        for i in range(len(self.heap) // 2, -1, -1):
            self._sift_down(i)

    def __str__(self):
        return str(self.heap)


# 测试代码
if __name__ == "__main__":
    # 最小堆测试
    min_heap = BinaryHeap('min')
    data = [3, 1, 6, 5, 2, 4]
    for num in data:
        min_heap.insert(num)

    print("最小堆:", min_heap)
    print("提取元素:")
    while not min_heap.is_empty():
        print(min_heap.extract(), end=" ")
    print()

    # 最大堆测试
    max_heap = BinaryHeap('max')
    max_heap.build_heap(data)
    print("\n最大堆:", max_heap)
    print("提取元素:")
    while not max_heap.is_empty():
        print(max_heap.extract(), end=" ")
```
主要应用：

* **优先队列（Priority Queue）**
    * 最小堆：每次取优先级最高的元素（最小值）
    * 最大堆：每次取优先级最高的元素（最大值）

* **堆排序（Heap Sort）**
    * 利用最大堆进行升序排序
    * 利用最小堆进行降序排序

* **Dijkstra算法（最短路径）**
    * 用最小堆优化查找最小距离的节点

* **Huffman编码（数据压缩）**
    * 用最小堆构建最优前缀码树


##### 优先级队列 heapq
```
import heapq

# 创建一个列表
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 将列表转换为堆
heapq.heapify(data)
print(f"堆化后的列表: {data}")  # 输出: [1, 1, 2, 3, 3, 9, 4, 6, 5, 5, 5]
#         1
#       /   \
#      1     2
#     / \   / \
#    3   3 9   4
#   / \ / \
#  6  5 5  5

# 添加元素到堆
heapq.heappush(data, 0)
print(f"添加元素后的堆: {data}")  # 输出: [0, 1, 2, 3, 1, 9, 4, 6, 5, 5, 5, 3]

# 弹出最小元素
min_item = heapq.heappop(data)
print(f"弹出最小元素: {min_item}")  # 输出: 弹出最小元素: 0

# 获取堆中的最小元素
min_item = data[0]
print(f"堆中的最小元素: {min_item}")  # 输出: 堆中的最小元素: 1

# 获取前 3 个最大元素
largest = heapq.nlargest(3, data)
print(f"前 3 个最大元素: {largest}")  # 输出: 前 3 个最大元素: [9, 6, 5]

# 获取前 3 个最小元素
smallest = heapq.nsmallest(3, data)
print(f"前 3 个最小元素: {smallest}")  # 输出: 前 3 个最小元素: [1, 1, 2]

# 创建一个空的优先级队列
priority_queue = []

# 添加元素 (优先级, 元素)
heapq.heappush(priority_queue, (2, 'code'))
heapq.heappush(priority_queue, (1, 'eat'))
heapq.heappush(priority_queue, (3, 'sleep'))

# 弹出优先级最高的元素
print(heapq.heappop(priority_queue))  # 输出: (1, 'eat')
print(heapq.heappop(priority_queue))  # 输出: (2, 'code'))
print(heapq.heappop(priority_queue))  # 输出: (3, 'sleep'))

# 实现最大堆，可以通过存储负值来模拟
max_priority_queue = []

# 添加元素 (优先级取负数实现最大堆, 元素)
heapq.heappush(max_priority_queue, (-2, 'code'))   # 优先级2
heapq.heappush(max_priority_queue, (-1, 'eat'))    # 优先级1
heapq.heappush(max_priority_queue, (-3, 'sleep'))  # 优先级3

# 弹出优先级最高的元素（注意恢复原始优先级值）
priority, item = heapq.heappop(max_priority_queue)
print(-priority, item)  # 输出: 3 sleep
priority, item = heapq.heappop(max_priority_queue)
print(-priority, item)  # 输出: 2 code
priority, item = heapq.heappop(max_priority_queue)
print(-priority, item)  # 输出: 1 eat
```
#### 线段树
线段树是一种二叉树数据结构，用于高效处理区间查询和区间更新操作。

叶子节点是数组中的元素，非叶子节点就是索引区间（线段）的汇总信息

![数据插入](/personal-site-mvp/img/doc-placeholder.svg "数据插入")
![数据修改](/personal-site-mvp/img/doc-placeholder.svg "数据修改")
简单实现区间查询与单点更新：

```
class SegmentTree:
    def __init__(self, data, default=0, func=lambda a, b: a + b):
        """
        初始化线段树（支持懒更新）

        参数:
            data: 初始数据数组
            default: 默认值（根据操作类型选择）
            func: 区间操作函数（求和、最小值、最大值等）

        示例:
            区间求和：func=lambda a, b: a + b, default=0
            区间最小值：func=min, default=float('inf')
            区间最大值：func=max, default=-float('inf')
        """
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = 1
        while self._size < self._len:
            self._size <<= 1  # 扩展到最接近的2的幂

        # 初始化线段树数组和懒标记数组
        self._tree = [self._default] * (2 * self._size)
        self._lazy = [None] * (2 * self._size)  # 用于存储未下传的更新

        # 将原始数据填充到叶子节点
        self._tree[self._size:self._size + self._len] = data[:]

        # 构建内部节点
        for i in range(self._size - 1, 0, -1):
            self._tree[i] = self._func(
                self._tree[2 * i],
                self._tree[2 * i + 1]
            )

    def __len__(self):
        return self._len

    def update(self, pos, value):
        """更新单个位置的值(0-based)，兼容懒更新机制"""
        if pos < 0 or pos >= self._len:
            raise IndexError("Position out of range")

        # 转换为区间更新[pos, pos+1)
        self._update_range(1, 0, self._size, pos, pos + 1, value)

    def _push_down(self, node, node_left, node_right):
        """下传懒标记到子节点"""
        if self._lazy[node] is not None:
            mid = (node_left + node_right) // 2

            # 更新左子树
            left_node = 2 * node
            self._tree[left_node] = self._lazy[node] * (mid - node_left)
            self._lazy[left_node] = self._lazy[node]

            # 更新右子树
            right_node = 2 * node + 1
            self._tree[right_node] = self._lazy[node] * (node_right - mid)
            self._lazy[right_node] = self._lazy[node]

            # 清除当前节点的标记
            self._lazy[node] = None

    def _update_range(self, node, node_left, node_right, l, r, value):
        """内部方法：更新区间[l, r)的值"""
        if r <= node_left or node_right <= l:
            return  # 完全不相关区间

        if l <= node_left and node_right <= r:
            # 完全包含的区间，更新当前节点并设置懒标记
            self._tree[node] = value * (node_right - node_left)
            self._lazy[node] = value
            return

        # 部分重叠区间，需要下传标记
        self._push_down(node, node_left, node_right)

        mid = (node_left + node_right) // 2
        self._update_range(2 * node, node_left, mid, l, r, value)
        self._update_range(2 * node + 1, mid, node_right, l, r, value)

        # 更新当前节点
        self._tree[node] = self._func(
            self._tree[2 * node],
            self._tree[2 * node + 1]
        )

    def update_range(self, l, r, value):
        """更新区间[l, r)的值(左闭右开)"""
        if l < 0 or r > self._len:
            raise IndexError("Update range out of bounds")
        self._update_range(1, 0, self._size, l, r, value)

    def _query_range(self, node, node_left, node_right, l, r):
        """内部方法：查询区间[l, r)的值"""
        if r <= node_left or node_right <= l:
            return self._default  # 完全不相关区间

        if l <= node_left and node_right <= r:
            return self._tree[node]  # 完全包含的区间

        # 部分重叠区间，需要下传标记
        self._push_down(node, node_left, node_right)

        mid = (node_left + node_right) // 2
        left_val = self._query_range(2 * node, node_left, mid, l, r)
        right_val = self._query_range(2 * node + 1, mid, node_right, l, r)

        return self._func(left_val, right_val)

    def query_range(self, l, r):
        """查询区间[l, r)的值(左闭右开)"""
        if l < 0 or r > self._len:
            raise IndexError("Query range out of bounds")
        return self._query_range(1, 0, self._size, l, r)

    def update_point(self, pos, value):
        """更新单个位置的值(0-based)"""
        if pos < 0 or pos >= self._len:
            raise IndexError("Position out of range")
        # 转换为区间更新[pos, pos+1)
        self.update_range(pos, pos + 1, value)

    def __repr__(self):
        return f"SegmentTree({[self.query_range(i, i + 1) for i in range(self._len)]})"


if __name__ == "__main__":
    # 区间求和
    data = [1, 4, 2, 3, 1, 6, 5]
    st = SegmentTree(data, default=0, func=lambda a, b: a + b)
    print(st.query_range(1, 3))  # 4 + 2 = 6

    # 单点更新
    st.update(2, 5)  # 将 data[2] 从 2 改为 5
    print(st.query_range(1, 3))  # 4 + 5 = 9

    # 区间更新
    st.update_range(1, 4, 2)  # 将[1,4)的值全部设为2
    print(st.query_range(0, 6))  # 1 + 2 + 2 + 2 + 1 + 6 = 14

    # 区间最小值
    data = [3, 1, 4, 2, 5]
    min_st = SegmentTree(data, default=float('inf'), func=min)
    print(min_st.query_range(1, 4))  # min(1, 4, 2) = 1

```
### 图论
#### 图的表示结构
|特性|邻接矩阵|邻接表|
|-|-|-|
|空间复杂度|O(V^2)|O(V+E)|
|查询边 `(u, v)` 是否存在|O(1)|O(deg⁡(u))|
|遍历所有邻居|O(V)|O(deg⁡(u))|
|适用场景|稠密图|稀疏图|
|修改图结构|较慢（需调整矩阵大小）|较快|
|表示方式，以无向无权图举例0 —— 1
| \  |
|  \ |
3 —— 2|adj_matrix = [
    [0, 1, 1, 1],  # 0 连接 1, 2, 3
    [1, 0, 1, 0],  # 1 连接 0, 2
    [1, 1, 0, 1],  # 2 连接 0, 1, 3
    [1, 0, 1, 0]   # 3 连接 0, 2
]|adj_list = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}|

##### 邻接矩阵
适用于**稠密图**（边数接近顶点数的平方），空间复杂度：*O*(V^2)（V 是顶点数）

```

class GraphAdjMatrix:
    def __init__(self, directed=False, weighted=False):
        """初始化邻接矩阵图"""
        self.directed = directed
        self.weighted = weighted

        self.adj_matrix = []
        self.vertex_index = {}
        self.index_vertex = {}
        self.next_index = 0

    def add_vertex(self, vertex):
        """添加顶点"""
        if vertex not in self.vertex_index:
            self.vertex_index[vertex] = self.next_index
            self.index_vertex[self.next_index] = vertex
            self.next_index += 1

            # 扩展邻接矩阵
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * len(self.vertex_index))

    def add_edge(self, src, dest, weight=1):
        """添加边（可指定权重和是否为有向图）"""
        self.add_vertex(src)
        self.add_vertex(dest)

        src_idx = self.vertex_index[src]
        dest_idx = self.vertex_index[dest]

        self.adj_matrix[src_idx][dest_idx] = weight
        if not self.directed:
            self.adj_matrix[dest_idx][src_idx] = weight

    def get_vertices(self):
        """获取所有顶点（返回顶点索引列表）"""
        return list(self.vertex_index.keys())

    def get_edges(self):
        """获取所有边（可指定是否返回有向边）"""
        edges = []
        for src_idx, row in enumerate(self.adj_matrix):
            for dest_idx, weight in enumerate(row):
                if weight != 0:
                    src = self.index_vertex[src_idx]
                    dest = self.index_vertex[dest_idx]
                    if self.weighted:
                        edges.append((src, dest, weight))
                    else:
                        edges.append((src, dest))
        return edges

    def get_neighbors(self, vertex):
        """获取顶点的邻居"""
        if vertex not in self.vertex_index:
            return []

        neighbors = []
        idx = self.vertex_index[vertex]
        for i, weight in enumerate(self.adj_matrix[idx]):
            if weight != 0:
                neighbor = self.index_vertex[i]
                if self.weighted:
                    neighbors.append((neighbor, weight))
                else:
                    neighbors.append(neighbor)
        return neighbors

    def print_graph(self):
        """打印邻接矩阵"""
        print("邻接矩阵表示:")
        print("   " + "  ".join(str(v) for v in self.vertex_index.keys()))
        for i, row in enumerate(self.adj_matrix):
            print("{} {}".format(self.index_vertex[i], row))


# 无向无权图
g = GraphAdjMatrix()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()
# 邻接矩阵表示:
#    0  1  2  3
# 0 [0, 1, 1, 1]
# 1 [1, 0, 1, 0]
# 2 [1, 1, 0, 1]
# 3 [1, 0, 1, 0]
print(g.get_vertices())  
# [0, 1, 2, 3]
print(g.get_edges())
# [(0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (2, 0), (2, 1), (2, 3), (3, 0), (3, 2)]
print(g.get_neighbors(0))
# [1, 2, 3]

# 有向加权图
g = GraphAdjMatrix(directed=True, weighted=True)
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'D', 7)
g.print_graph()
# 邻接矩阵表示:
#    A  B  C  D
# A [0, 5, 3, 0]
# B [0, 0, 0, 2]
# C [0, 0, 0, 7]
# D [0, 0, 0, 0]

# 获取顶点和边
print(g.get_vertices())
# ['A', 'B', 'C', 'D']
print(g.get_edges())
# [('A', 'B', 5), ('A', 'C', 3), ('B', 'D', 2), ('C', 'D', 7)]

# 获取邻居
print(g.get_neighbors('A'))  # [('B', 5), ('C', 3)]
```
##### 邻接表
适用于**稀疏图**（边数远小于顶点数的平方），空间复杂度：*O*(*V*+*E*)（V是顶点数，E是边数）

```
class GraphAdjList:
    def __init__(self, directed=False, weighted=False):
        """初始化邻接矩阵图"""
        self.directed = directed
        self.weighted = weighted

        self.adj_list = {}
        self.vertices = set()

    def add_vertex(self, vertex):
        """添加顶点"""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.vertices.add(vertex)

    def add_edge(self, src, dest, weight=1):
        """添加边（可指定权重和是否为有向图）"""
        self.add_vertex(src)
        self.add_vertex(dest)

        if self.weighted:
            self.adj_list[src].append((dest, weight))
            if not self.directed:
                self.adj_list[dest].append((src, weight))
        else:
            self.adj_list[src].append(dest)
            if not self.directed:
                self.adj_list[dest].append(src)

    def get_vertices(self):
        """获取所有顶点（返回顶点索引列表）"""
        return list(self.vertices)

    def get_edges(self):
        """获取所有边（可指定是否返回有向边）"""
        edges = []
        for src in self.adj_list:
            for edge in self.adj_list[src]:
                if self.weighted:
                    dest, weight = edge
                    edges.append((src, dest, weight))
                else:
                    edges.append((src, edge))
        return edges

    def get_neighbors(self, vertex):
        """获取顶点的邻居"""
        if vertex not in self.adj_list:
            return []
        return self.adj_list[vertex]

    def print_graph(self):
        """打印邻接表"""
        print("邻接表表示:")
        for vertex in sorted(self.adj_list.keys()):
            print("{} -> {}".format(vertex, self.adj_list[vertex]))


# 无向无权图
g = GraphAdjList()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()
# 邻接表表示:
# 0 -> [1, 2, 3]
# 1 -> [0, 2]
# 2 -> [0, 1, 3]
# 3 -> [0, 2]
print(g.get_vertices())
# [0, 1, 2, 3]
print(g.get_edges())
# [(0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (2, 0), (2, 1), (2, 3), (3, 0), (3, 2)]
print(g.get_neighbors(0))
# [1, 2, 3]

# 有向加权图
g = GraphAdjList(directed=True, weighted=True)
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'D', 7)
g.print_graph()
# 邻接表表示:
# A -> [('B', 5), ('C', 3)]
# B -> [('D', 2)]
# C -> [('D', 7)]
# D -> []

# 获取顶点和边
print(g.get_vertices())
# ['A', 'B', 'C', 'D']
print(g.get_edges())
# [('A', 'B', 5), ('A', 'C', 3), ('B', 'D', 2), ('C', 'D', 7)]
# 获取邻居
print(g.get_neighbors('A'))  
# [('B', 5), ('C', 3)]
```
#### 图结构的 DFS/BFS 遍历
类似树的遍历，但图结构中可能存在环，所以需要标记遍历过的节点，避免遍历函数在环中死循环。

```
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # 深度优先遍历所有节点
    def dfs_all_nodes(self):
        visited = set()

        def dfs(node, visited):
            visited.add(node)
            print(node, end=' ')

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        for node in list(self.graph):
            if node not in visited:
                dfs(node, visited)

    # 广度优先遍历所有节点
    def bfs_all_nodes(self):
        visited = set()
        for node in list(self.graph):
            if node not in visited:
                queue = deque([node])
                visited.add(node)

                while queue:
                    current = queue.popleft()
                    print(current, end=' ')

                    for neighbor in self.graph[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

    # 深度优先遍历所有边
    def dfs_all_edges(self):
        visited_nodes = set()  # 记录访问过的节点
        visited_edges = set()  # 记录访问过的边

        def dfs(node):
            visited_nodes.add(node)
            for neighbor in self.graph[node]:
                edge = (node, neighbor)
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    print(f"边: {edge}")
                if neighbor not in visited_nodes:
                    dfs(neighbor)

        for node in list(self.graph):
            if node not in visited_nodes:
                dfs(node)

    # 广度优先遍历所有边
    def bfs_all_edges(self):
        visited_edges = set()  # 记录已访问的边
        for node in list(self.graph):
            for neighbor in self.graph[node]:
                edge = (node, neighbor)
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    print(f"边: {edge}")


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(4, 5)  # 不连通的部分

    print("DFS遍历所有节点:")
    g.dfs_all_nodes()
    # 输出: 0 1 2 3 5 4

    print("\nBFS遍历所有节点:")
    g.bfs_all_nodes()
    # 输出: 0 1 5 2 3 4

    print("\nDFS遍历所有边:")
    g.dfs_all_edges()
    # 输出:
    # 边: (0, 1)
    # 边: (1, 2)
    # 边: (2, 0)
    # 边: (2, 3)
    # 边: (3, 3)
    # 边: (0, 5)
    # 边: (4, 5)

    print("\nBFS遍历所有边:")
    g.bfs_all_edges()
    # 输出:
    # 边: (0, 1)
    # 边: (0, 5)
    # 边: (1, 2)
    # 边: (2, 0)
    # 边: (2, 3)
    # 边: (3, 3)
    # 边: (4, 5)
```
#### 并查集
并查集 (Disjoint Set Union, DSU) 用于高效解决**无向图的连通性问题**，可以在 O(1)时间内合并两个连通分量，在 O(1)时间内查询两个节点是否连通，在 O(1)时间内查询连通分量的数量

![连通分量8](/personal-site-mvp/img/doc-placeholder.svg "连通分量8")
核心原理：

* **权重数组：**每个节点存储其 父节点，初始时 parent[i] = i（每个节点是自己的父节点）。通过递归查找 find(x)，可以找到 x 的 根节点（代表整个连通分量）。
* **路径压缩：**优化 find(x) 操作：在查找过程中，将路径上的所有节点直接指向根节点，使树变扁平。
* **按秩合并：**优化 union(x, y) 操作：总是将 较小的树 合并到 较大的树 下，避免树退化成链表。

```

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.count = n  # 初始连通分量数

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return  # 已连通
        # 按秩合并
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        self.count -= 1  # 连通分量减少

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_count(self):
        return self.count  # O(1) 查询连通分量数


# 创建一个大小为5的并查集
dsu = DSU(5)
print(dsu.get_count())  # 5

# 初始状态：每个元素都是自己的父节点
print(dsu.parent)  # [0, 1, 2, 3, 4]
print(dsu.rank)    # [0, 0, 0, 0, 0]

# 合并操作
dsu.union(0, 1)
print(dsu.parent)  # [0, 0, 2, 3, 4]
print(dsu.rank)    # [1, 0, 0, 0, 0]
dsu.union(3, 2)
print(dsu.parent)  # [0, 0, 3, 3, 4]
print(dsu.rank)    # [1, 0, 0, 1, 0]
print(dsu.get_count())  # 3

# 检查连接
print(dsu.is_connected(0, 1))  # True
print(dsu.is_connected(0, 2))  # False

# 再次合并
dsu.union(1, 3)
print(dsu.parent)  # [0, 0, 3, 0, 4]
print(dsu.rank)    # [2, 0, 0, 1, 0]
print(dsu.get_count())  # 2
print(dsu.is_connected(0, 2))  # True
print(dsu.is_connected(0, 4))  # False

# 查询连通分量数
print(dsu.get_count())  # 2

```





