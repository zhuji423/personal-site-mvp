---
title: "创建队列"
description: "PY deque、heapq"
date: "2026-04-27"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\05_algorithm_backup\\ku_backup_20260427\\08_PYdequeheapq.md"
---
PY deque、heapq

### deque（双端队列）
标准队列 queue.Queue：

```
from queue import Queue

q = Queue()
q.put(1)    # 入队 (后端添加)
q.put(2)
item = q.get()  # 出队 (前端移除)，返回1
```
双端队列 collections.deque：

```
from collections import deque

# 创建队列
q = deque()

# 添加元素到队尾
q.append(1)
q.append(2)
q.append(3)

q.append(4)
q.remove(4)

# 添加元素到队头
q.appendleft(0)

# 获取队列大小
print(f"队列中有 {len(q)} 个元素")  # 输出: 4

# 取出队头元素
item = q.popleft()
print(f"取出队头元素: {item}")  # 输出: 0

# 取出队尾元素
item = q.pop()
print(f"取出队尾元素: {item}")  # 输出: 3

# 检查队列是否为空
if len(q) == 0:
    print("队列为空")
else:
    print("队列不为空")  # 输出: 队列不为空
```
应用：

###### 广度优先搜索（BFS）
```
from collections import deque

def bfs(graph, start):
    """
    广度优先搜索函数
    :param graph: 图的邻接表表示（字典形式）
    :param start: 起始节点
    :return: 无返回值，直接打印访问顺序
    """
    visited = set()          # 已访问节点的集合
    queue = deque([start])   # 使用队列存储待访问节点

    while queue:  # 当队列不为空时继续搜索
        node = queue.popleft()  # 取出队列中的第一个节点
        if node not in visited:
            print(node, end=" ")  # 访问当前节点
            visited.add(node)     # 将当前节点标记为已访问

            # 将当前节点的所有未访问邻居节点加入队列
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# 示例用法
if __name__ == "__main__":
    # 图的邻接表表示
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("广度优先搜索（BFS）结果：")
    bfs(graph, 'A')  # 从节点 'A' 开始进行 BFS
 # A B C D E F 
```
###### 拓扑排序
```
from collections import deque

def topological_sort(graph):
    # 统计每个节点的入度
    in_degree = {node: 0 for node in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # 初始化队列，将所有入度为 0 的节点加入队列
    queue = deque([node for node in graph if in_degree[node] == 0])
    sorted_nodes = []  # 存储拓扑排序的结果

    # 开始拓扑排序
    while queue:
        u = queue.popleft()  # 取出一个入度为 0 的节点
        sorted_nodes.append(u)  # 加入排序结果

        # 遍历 u 的邻居，减少它们的入度
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:  # 如果入度变为 0，加入队列
                queue.append(v)

    # 如果排序结果包含所有节点，则返回排序结果；否则说明图中有环
    if len(sorted_nodes) == len(graph):
        return sorted_nodes
    else:
        return "图中有环，无法进行拓扑排序！"

# 示例图（邻接表表示）
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# 进行拓扑排序
result = topological_sort(graph)

# 输出结果
print("拓扑排序结果:")
print(result)
# 拓扑排序结果:
# ['A', 'B', 'C', 'D', 'E']
```
示例图：

```
A → B
↓   ↓
C → D → E
```
### heapq（优先队列）
`heapq` 是 Python 中的一个内置模块，提供了堆队列算法的实现，也称为优先队列。堆是一种特殊的二叉树结构，满足以下性质：

* 父节点的值总是小于或等于其子节点的值（最小堆）。
* 父节点的值总是大于或等于其子节点的值（最大堆）。

`heapq` 模块默认实现的是**最小堆**，即堆顶元素始终是最小的元素。

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
```
如果需要实现最大堆，可以通过对元素取反来实现。例如，插入 `10` 时，实际插入 `-10`。

###### Dijkstra算法（最短路径）
```
import heapq

def dijkstra(graph, start):
    # 初始化距离字典，所有节点的距离设置为无穷大
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 源节点到自身的距离为 0
    priority_queue = [(0, start)]  # 优先队列，存储 (距离, 节点)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果当前距离大于已知距离，跳过
        if current_distance > distances[current_node]:
            continue

        # 遍历邻居节点
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 如果找到更短的路径，更新距离并加入优先队列
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 示例图（邻接表表示）
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 从节点 'A' 开始计算最短路径
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# 输出结果
print(f"从节点 {start_node} 到其他节点的最短路径:")
for node, distance in shortest_paths.items():
    print(f"到节点 {node} 的最短距离: {distance}")
    
# 从节点 A 到其他节点的最短路径:
# 到节点 A 的最短距离: 0
# 到节点 B 的最短距离: 1
# 到节点 C 的最短距离: 3
# 到节点 D 的最短距离: 4
```
###### Prim算法（最小生成树MST）普里姆算法
```
import heapq

def prim(graph, start):
    # 初始化
    mst = []  # 存储最小生成树的边
    visited = set()  # 记录已访问的节点
    priority_queue = []  # 优先队列，存储 (权重, 当前节点, 父节点)

    # 从起始节点开始
    heapq.heappush(priority_queue, (0, start, None))  # (权重, 当前节点, 父节点)

    while priority_queue:
        weight, current_node, parent = heapq.heappop(priority_queue)

        # 如果节点已访问，跳过
        if current_node in visited:
            continue

        # 标记节点为已访问
        visited.add(current_node)

        # 如果父节点不为空，将边加入最小生成树
        if parent is not None:
            mst.append((parent, current_node, weight))

        # 遍历当前节点的邻居
        for neighbor, edge_weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))

    return mst

# 示例图（邻接表表示）
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 从节点 'A' 开始计算最小生成树
start_node = 'A'
mst = prim(graph, start_node)

# 输出结果
print("最小生成树的边:")
for u, v, w in mst:
    print(f"边 {u} - {v}, 权重: {w}")
# 最小生成树的边:
# 边 A - B, 权重: 1
# 边 B - C, 权重: 2
# 边 C - D, 权重: 1
```
示例图：

```
A --1-- B
|     / |
4   2   5
| /     |
C --1-- D
```
###### 霍夫曼编码
```
import heapq
from collections import Counter


# 定义霍夫曼树的节点类
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # 字符
        self.freq = freq  # 频率
        self.left = None  # 左子节点
        self.right = None  # 右子节点

    # 定义比较方法，用于堆排序
    def __lt__(self, other):
        return self.freq < other.freq


# 构建霍夫曼树
def build_huffman_tree(text):
    # 统计字符频率
    frequency = Counter(text)

    # 使用优先队列（最小堆）存储节点
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # 构建霍夫曼树
    while len(heap) > 1:
        # 取出频率最小的两个节点
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # 创建一个新节点，频率为两个子节点频率之和
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # 将新节点放回堆中
        heapq.heappush(heap, merged)

    # 返回霍夫曼树的根节点
    return heap[0]


# 生成霍夫曼编码表
def build_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return

    # 如果当前节点是叶子节点，则存储其编码
    if root.char is not None:
        huffman_codes[root.char] = current_code
        return

    # 递归处理左子树和右子树
    build_huffman_codes(root.left, current_code + "0", huffman_codes)
    build_huffman_codes(root.right, current_code + "1", huffman_codes)


# 打印霍夫曼树
def print_huffman_tree(node, prefix="", is_left=True):
    if node is not None:
        print(prefix, "├── " if is_left else "└── ", node.char if node.char else f"Freq: {node.freq}", sep="")
        # 递归打印左子树和右子树
        print_huffman_tree(node.left, prefix + ("│   " if is_left else "    "), True)
        print_huffman_tree(node.right, prefix + ("│   " if is_left else "    "), False)


# 霍夫曼编码
def huffman_encode(text):
    if not text:
        return "", None

    # 构建霍夫曼树
    root = build_huffman_tree(text)
    print("霍夫曼树:")
    print_huffman_tree(root)

    # 生成霍夫曼编码表
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)
    print("霍夫曼编码表:", huffman_codes)

    # 对文本进行编码
    encoded_text = "".join([huffman_codes[char] for char in text])

    return encoded_text, root


# 霍夫曼解码
def huffman_decode(encoded_text, root):
    if not encoded_text:
        return ""

    decoded_text = []
    current_node = root

    # 遍历编码文本，根据霍夫曼树解码
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        # 如果到达叶子节点，则记录字符并回到根节点
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root

    return "".join(decoded_text)


# 测试
if __name__ == "__main__":
    text = "hello world"
    print("原始文本:", text)

    # 编码
    encoded_text, huffman_tree = huffman_encode(text)
    print("编码结果:", encoded_text)

    # 解码
    decoded_text = huffman_decode(encoded_text, huffman_tree)
    print("解码结果:", decoded_text)

    # 原始文本: hello world
    # 霍夫曼树:
    # ├── Freq: 11
    # │   ├── Freq: 4
    # │   │   ├── Freq: 2
    # │   │   │   ├── e
    # │   │   │   └── d
    # │   │   └── Freq: 2
    # │   │       ├── r
    # │   │       └── w
    # │   └── Freq: 7
    # │       ├── l
    # │       └── Freq: 4
    # │           ├── o
    # │           └── Freq: 2
    # │               ├── h
    # │               └──  
    # 霍夫曼编码表: {'e': '000', 'd': '001', 'r': '010', 'w': '011', 'l': '10', 'o': '110', 'h': '1110', ' ': '1111'}
    # 编码结果: 11100001010110111101111001010001
    # 解码结果: hello world
```
###### 
### 刷题小写法
###### 存在/全部/过滤
```
nums = [1, 5, 3, 2]
# 全部元素>4
res = all(i > 4 for i in nums)
print(res)
# False

# 存在元素>4
res = any(i > 4 for i in nums)
print(res)
# True

# 只保留满足函数func
def func(x):
   return x > 4
res = list(filter(lambda x: func(x), nums))
print(res)
# [5]
```
###### 随机
```
import random

# 返回 [a, b] 之间的随机整数（包含 a 和 b）
a = random.randint(1, 78)
print(a)

# 从序列中随机选取一个元素
lst = [{'a': 1}, {'b': 2}]
res = random.choice(lst)
print(res)  # {'b': 2}

# 按权重随机选择
lst = ["A", "B", "C"]
weights = [10, 30, 60]  # 权重越高，被选中的概率越大，总和不必为1
res = random.choices(lst, weights=weights, k=10)  # 选择10次
print(res)  # 输出 "A", "B" 或 "C"，概率分别为 10%, 30%, 60%
# ['C', 'B', 'C', 'B', 'B', 'C', 'C', 'C', 'B', 'C']
```
###### 极小值极大值
|极小值|极大值|
|-|-|
|a = float('-inf')  # 初始化为负无穷
print(a)  # 输出: -inf|a = float('inf')  # 初始化为无穷
print(a)  # 输出: inf|

###### 初始化矩阵
|矩阵大小|code|
|-|-|
|1 * 5|a = [0] * 5
# [0, 0, 0, 0, 0]|
|3 * 5|a = [[0] * 5 for _ in range(3)]
# [[0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0]]|

###### 取整
```
# 四舍五入
rounded = round(0.5)
print(rounded) 

import math
# 向上取整
math.ceil(0.5)  # 输出：1
# 向上下取整
math.floor(0.5)  # 输出：0

# 截断取整 直接去掉小数部分，返回整数部分
# 正数截断（相当于 math.floor）
print(math.trunc(3.7))  # 输出：3
print(math.trunc(0.5))  # 输出：0
# 负数截断（相当于 math.ceil）
print(math.trunc(-3.7))  # 输出：-3
print(math.trunc(-0.5))  # 输出：0
```
###### 反向遍历
```
a = [1, 4, 2]
for i in a[::-1]:
    print(i, end = ' ')
# 2 4 1 

a = [1, 4, 2]
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=' ')
# 2 4 1
```

