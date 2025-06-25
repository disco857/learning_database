## 模版和例题

### bfs

```python
# 网格传送门旅游
from collections import deque
from collections import defaultdict


def bfs(start, end):
    a, b = start
    c, d = end
    queue = deque([(a, b, 0)])
    vis = {(a, b)}
    if matrix[a][b] != '.':
        for t in portal_list[matrix[a][b]]:
            tx1, ty1 = t
            if tx1 == a and ty1 == b:
                continue
            else:
                if (tx1, ty1) not in vis:
                    queue.append((tx1, ty1, 0))
                    vis.add((tx1, ty1))
    while queue:
        nx, ny, step = queue.popleft()
        if nx == c and ny == d:
            return step
        for i in range(4):
            tx, ty = nx + dic[i][0], ny + dic[i][1]
            if check(tx, ty) and (tx, ty) not in vis:
                queue.append((tx, ty, step + 1))
                vis.add((tx, ty))
                if matrix[tx][ty] != '.':
                    for t in portal_list[matrix[tx][ty]]:
                        tx1, ty1 = t
                        if tx1 == tx and ty1 == ty:
                            continue
                        else:
                            if (tx1, ty1) not in vis:
                                queue.append((tx1, ty1, step + 1))
                                vis.add((tx1, ty1))
    return -1


dic = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def check(x, y):
    if 0 <= x < m and 0 <= y < n and matrix[x][y] != '#':
        return True
    return False


m, n = 2, 4
matrix = ["..C.", "C.A."]
portal_list = defaultdict(list)
for i in range(m):
    for j in range(n):
        if matrix[i][j] != '#' and matrix[i][j] != '.':
            portal_list[matrix[i][j]].append((i, j))

print(bfs((0, 0), (m - 1, n - 1)))

```

```python
# Robot
from collections import deque

def bfs(x0, y0, direction):
    queue = deque()
    seen = set()
    queue.append((x0, y0, direction, 0))
    seen.add((x0, y0, direction))

    while queue:
        x, y, direction, depth = queue.popleft()

        # 如果到达目标位置，返回深度
        if x == tx and y == ty:
            return depth

        # 当前方向对应的索引
        tmp = directions[direction]

        # 尝试向右转
        new_direction_right = directions[(tmp + 1) % 4]
        if (x, y, new_direction_right) not in seen:
            queue.append((x, y, new_direction_right, depth + 1))
            seen.add((x, y, new_direction_right))

        # 尝试向左转
        new_direction_left = directions[(tmp - 1) % 4]
        if (x, y, new_direction_left) not in seen:
            queue.append((x, y, new_direction_left, depth + 1))
            seen.add((x, y, new_direction_left))

        # 沿当前方向前进最多三步
        for i in range(3):
            nx, ny = x + dic[direction][i][0], y + dic[direction][i][1]

            # 检查新位置是否合法
            if check(nx, ny):
                if (nx, ny, direction) not in seen:
                    queue.append((nx, ny, direction, depth + 1))
                    seen.add((nx, ny, direction))
            else:
                break

    # 如果无法到达目标位置，返回 -1
    return -1


# 定义方向映射
directions = {'north': 0, 'east': 1, 'south': 2, 'west': 3,
              0: 'north', 1: 'east', 2: 'south', 3: 'west'}

# 定义每个方向的移动偏移量
dic = {
    'west': [[0, -1], [0, -2], [0, -3]],
    'east': [[0, 1], [0, 2], [0, 3]],
    'south': [[1, 0], [2, 0], [3, 0]],
    'north': [[-1, 0], [-2, 0], [-3, 0]]
}

# 检查位置是否合法
def check(x, y):
    if (0 <= x < M and 0 <= x - 1 < M and
        0 <= y < N and 0 <= y - 1 < N and
        {mtr[x][y], mtr[x][y - 1], mtr[x - 1][y], mtr[x - 1][y - 1]} == {0}):
        return True
    else:
        return False


# 主程序
while True:
    M, N = map(int, input().split())
    if {M, N} == {0}:
        break

    # 初始化地图
    mtr = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        mtr[i] = list(map(int, input().split()))

    # 读取起点、终点和初始方向
    a, b, tx, ty, r = input().split()
    tx, ty = int(tx), int(ty)

    # 调用 BFS 并输出结果
    print(bfs(int(a), int(b), r))
```



### Bellman-ford

```python
# LC787.K站中转内最便宜的航班
from copy import deepcopy


class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def __str__(self):
        return str(self.key)


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, p):
        if p not in self.vertices:
            self.vertices[p] = Vertex(p)

    def add_edge(self, p, q, weight):
        self.add_vertex(p)
        self.add_vertex(q)
        self.vertices[p].neighbors[q] = weight


def bellman_fold(graph, start, end, k):
    dis = {vertex: float('inf') for vertex in graph.vertices}
    dis[start] = 0
    for _ in range(k + 1):
        pre_dis = deepcopy(dis)
        for vertex in graph.vertices:
            for neighbor, weight in graph.vertices[vertex].neighbors.items():
                if pre_dis[vertex] + weight < dis[neighbor]:
                    dis[neighbor] = pre_dis[vertex] + weight
    if dis[end] != float('inf'):
        return dis[end]
    else:
        return -1


gh = Graph()
n = 4
for i in range(n):
    gh.add_vertex(i)
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
for flight in flights:
    gh.add_edge(flight[0], flight[1], flight[2])
print(bellman_fold(gh, 0, 3, 1))

```



### Floyd_warshall

Floyd-Warshall适用于加权图（包括负权重边，但不包含负权重环），并且能够在O(|V|^3)的时间复杂度内计算出任意两点间的最短路径，其中|V|是图中顶点的数量。

```python
def floyd_warshall(graph):
    """
    graph: 邻接矩阵表示的图，graph[i][j] 表示从 i 到 j 的权重，若无直接边则为 float('inf')
    返回一个矩阵 dist，其中 dist[i][j] 表示从 i 到 j 的最短路径长度
    """
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    # 动态规划阶段
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 检查负权重环
    for i in range(V):
        if dist[i][i] < 0:
            print("Graph contains a negative-weight cycle")
            return None

    return dist

# 示例用法
inf = float('inf')
graph = [
    [0, 3, inf, 5],
    [2, 0, inf, 4],
    [inf, 1, 0, inf],
    [inf, inf, 2, 0]
]

result = floyd_warshall(graph)
if result is not None:
    for row in result:
        print(row)
```

Floyd-Warshall算法非常适合于以下场景：

- 当你需要知道图中所有节点对之间的最短路径时。
- 图中可能存在负权重边，但不存在负权重环的情况下。
- 对于稠密图或者当边的数量接近于|V|^2时，Floyd-Warshall比执行|V|次Dijkstra算法更加高效。



### Dijkstra

```python
# 03424. Candies
import heapq


def dijkstra(graph, start, end):
    dis = {i: float('inf') for i in range(n + 1)}
    dis[start] = 0
    queue = [(0, start)]
    heapq.heapify(queue)
    while queue:
        cur_dis, cur_node = heapq.heappop(queue)
        if cur_node == end:
            return cur_dis
        if cur_dis > dis[cur_node]:
            continue
        for neighbor, weight in graph[cur_node]:
            n_dis = cur_dis + weight
            if n_dis < dis[neighbor]:
                dis[neighbor] = n_dis
                heapq.heappush(queue, (n_dis, neighbor))
    return -1


n, m = map(int, input().split())
kids = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    kids[a].append((b, c))

ans = dijkstra(kids, 1, n)
print(ans)

```

```python
# 道路
import heapq
from collections import defaultdict


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = defaultdict(list)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, p):
        if p not in self.vertices:
            self.vertices[p] = Vertex(p)

    def add_edge(self, p, q, weight, money):
        self.add_vertex(p)
        self.add_vertex(q)
        self.vertices[p].neighbors[q].append((weight, money))


def dijkstra(graph, start, end):
    dis = {(vertex, m): float('inf') for vertex in graph.vertices for m in range(k + 1)}
    dis[(start, 0)] = 0
    queue = [(0, start, 0)]
    heapq.heapify(queue)
    while queue:
        cur_dis, vertex, cur_money = heapq.heappop(queue)
        if cur_dis > dis[(vertex, cur_money)]:
            continue
        for neighbor, infos in graph.vertices[vertex].neighbors.items():
            for info in infos:
                weight, money = info
                n_dis = cur_dis + weight
                n_money = cur_money + money
                if n_money > k:
                    continue
                if n_dis < dis[(neighbor, n_money)]:
                    dis[(neighbor, n_money)] = n_dis
                    heapq.heappush(queue, (n_dis, neighbor, n_money))
    ans = min(dis[(end, i)] for i in range(k + 1))
    return ans if ans != float('inf') else -1


k = int(input())
n = int(input())
r = int(input())
gh = Graph()
for i in range(n):
    gh.add_vertex(i + 1)
for _ in range(r):
    a, b, c, d = map(int, input().split())
    gh.add_edge(a, b, c, d)
print(dijkstra(gh, 1, n))

```



### 欧拉筛

```python
N=int(input('检索多少范围内的质数：'))
isprime=[True]*(N)
isprime[1]=False
isprime[0]=False
primes=[]
for i in range(2,N):
    if isprime[i]:
        primes.append(i)
    for prime in primes:
        if i*prime>=N:
            break
        isprime[i*prime]=False
        if i%prime==0:
            break
```



### 二叉树的中序遍历

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
```



### 并查集

```python
class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)]

    def __str__(self):
        return str(self.parent)

    def find(self,p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self,p,q):
        root_p = self.find(p)
        root_q = self.find(q)
        if self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        elif self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        else:
            self.parent[root_p] = root_q
            self.rank[root_q] += 1

    def is_connected(self,p,q):
        return self.find(p) == self.find(q)

    def num_of_sets(self):
        return sum(self.parent[i] == i for i in range(len(self.parent)))

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
n=len(isConnected)
uf = UnionFind(n)
for i in range(n):
    for j in range(i+1,n):
        if isConnected[i][j]==1:
            uf.union(i,j)
print(uf.num_of_sets())
```



### dfs

剪枝： **Warnsdorff 启发式策略**（Warnsdorff's Rule）它的核心思想是：每次选择下一步中可选走法最少的方向。即对于每一个候选位置 `(nx, ny)`，统计它下一步还能走到多少个未访问的位置。然后按这个数量排序，先尝试那些“未来选择少”的位置。



```python
from functools import lru_cache
```

lru_cache是一个来自于functools的装饰器，可以把函数的返回值缓存起来，当函数下一次遇到同样的输入时，将直接从缓存中调用返回值，而不必重复计算。

用法：在def语句的上一行写`@lru_cache(maxsize=None)`，`maxsize`参数指定缓存的空间上限，`None`即没有限制。

lru_cache是独立的。如果有多个函数都要分别存储结果，那么每个函数前面都要写@lru



用全局变量不要忘记`# pylint: skip-file`



### KMP

```python
""""
compute_lps 函数用于计算模式字符串的LPS表。LPS表是一个数组，
其中的每个元素表示模式字符串中当前位置之前的子串的最长前缀后缀的长度。
该函数使用了两个指针 length 和 i，从模式字符串的第二个字符开始遍历。
"""
def compute_lps(pattern):
    """
    计算pattern字符串的最长前缀后缀（Longest Proper Prefix which is also Suffix）表
    :param pattern: 模式字符串
    :return: lps表
    """

    m = len(pattern)
    lps = [0] * m  # 初始化lps数组
    length = 0  # 当前最长前后缀长度
    for i in range(1, m):  # 注意i从1开始，lps[0]永远是0
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]  # 回退到上一个有效前后缀长度
        if pattern[i] == pattern[length]:
            length += 1
        lps[i] = length

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    lps = compute_lps(pattern)
    matches = []

    # 在 text 中查找 pattern
    j = 0  # 模式串指针
    for i in range(n):  # 主串指针
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]  # 模式串回退
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - j + 1)  # 匹配成功
            j = lps[j - 1]  # 查找下一个匹配

    return matches


text = "ABABABABCABABABABCABABABABC"
pattern = "ABABCABAB"
index = kmp_search(text, pattern)
print("pos matched：", index)
# pos matched： [4, 13]

```



### Trie

```python
class TrieNode:
    def __init__(self,key=None):
        self.key=key
        self.children={}
        self.is_end = False

    def __hash__(self):
        return hash(self.key)

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        cur_node=self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode(char)
            cur_node = cur_node.children[char]
        cur_node.is_end=True

    def search(self,word):
        cur_node=self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node=cur_node.children[char]
        if cur_node.is_end:
            return True
        else:
            return False

    def startsWith(self,prefix):
        cur_node=self.root
        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node=cur_node.children[char]
        return True
```



### ASCII码

![截屏2024-12-10 16.00.25](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-12-10 16.00.25.png)

### 二进制运算

我们先看一些简单的例子来理解这些运算符的作用。

###### 1. 按位与：`&`

```python
a = 5   # 二进制: 0b101
b = 3   # 二进制: 0b011
print(a & b)  # 结果: 1 (0b001)
```

只有两个位都为1，结果才是1。

------

###### 2. 按位或：`|`

```python
a = 5   # 0b101
b = 3   # 0b011
print(a | b)  # 结果: 7 (0b111)
```

只要一个位为1，结果就是1。

------

###### 3. 按位异或：`^`

```python
a = 5   # 0b101
b = 3   # 0b011
print(a ^ b)  # 结果: 6 (0b110)
```

对应位不同则为1，相同则为0。

------

###### 4. 按位取反：`~`

```python
a = 5   # 0b0000...0101
print(~a)     # 结果: -6
```

因为 Python 使用的是 **补码形式** 表示负数，所以 `~x = -x - 1`。

------

###### 5. 左移运算：`<<`

```python
a = 1p
print(a << 1)  # 输出 2
print(a << 2)  # 输出 4
```

左移 n 位 ≈ 乘以 2**n

------

###### 6. 右移运算：`>>`

```python
a = 8
print(a >> 1)  # 输出 4
print(a >> 2)  # 输出 2
```

右移 n 位 ≈ 整数除以 2**n，向负无穷方向取整（带符号扩展）