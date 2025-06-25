# Assignment #B: 图为主

Updated 2223 GMT+8 Apr 29, 2025

2025 spring, Complied by <mark>李冠黎 工学院</mark>



> **说明：**
>
> 1. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E07218:献给阿尔吉侬的花束

bfs, http://cs101.openjudge.cn/practice/07218/

思路：

最纯良的bfs

代码：

```python
from collections import deque


def bfs(x0, y0, tx, ty):
    queue = deque([(x0, y0, 0)])
    vis = {(x0, y0)}
    while queue:
        x, y, step = queue.popleft()
        if x == tx and y == ty:
            return step
        for i in range(4):
            nx, ny = x + dic[i][0], y + dic[i][1]
            if check(nx, ny) and (nx, ny) not in vis:
                queue.append((nx, ny, step + 1))
                vis.add((nx, ny))
    return 'oop!'


def check(x, y):
    if 0 <= x < m and 0 <= y < n and mtr[x][y] != '#':
        return True
    else:
        return False


dic = [[1, 0], [0, 1], [-1, 0], [0, -1]]

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    a, b, c, d = 0, 0, 0, 0
    mtr = []
    for i in range(m):
        row = list(input())
        try:
            a, b = i, row.index('S')
        except ValueError:
            pass
        try:
            c, d = i, row.index('E')
        except ValueError:
            pass
        mtr.append(row)

    print(bfs(a, b, c, d))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-01 19.31.49](https://p.ipic.vip/uqnvb0.png)



### M3532.针对图的路径存在性查询I

disjoint set, https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/

思路：

实际上由于nums的单调递增条件太强，根本不需要什么并查集，直接并查集反而会超时。

代码：

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parents=[_ for _ in range(n)]
        for i in range(1,n):
            if abs(nums[i]-nums[i-1]) <= maxDiff:
                parents[i]=parents[i-1]

        result=[]
        for pairs in queries:
            result.append(parents[pairs[0]]==parents[pairs[1]])
        return result

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-01 19.30.10](https://p.ipic.vip/jpzrl0.png)



### M22528:厚道的调分方法

binary search, http://cs101.openjudge.cn/practice/22528/

思路：



代码：

```python
import math
def binary_search(left,right):
    # if left == right:
    #     return left
    # mid=(left+right)//2
    # if check(mid):
    #     return binary_search(left,mid)
    # else:
    #     return binary_search(mid+1,right)

    while left != right:
        mid = (left+right) // 2
        if check(mid):
            right=mid
        else:
            left=mid+1
    return left

def check(x):
    x=x/1000000000
    if x*std+1.1**(x*std)>=85:
        return True
    else:
        return False

nums=list(map(float,input().split()))
nums.sort(reverse=True)
std=nums[max(math.ceil(len(nums)*0.6)-1,0)]
print(binary_search(1,1000000000))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-06 23.35.21](https://p.ipic.vip/z6r6td.png)



### Msy382: 有向图判环 

dfs, https://sunnywhy.com/sfbj/10/3/382

思路：

学到很多，dfs, kahn, rec_stack等等

代码：

```python
from collections import deque
class Vertex:
    def __init__(self,key):
        self.key = key
        self.neighbors = []

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)

    def add_edge(self, key1, key2):
        self.add_vertex(key1)
        self.add_vertex(key2)
        self.vertices[key1].neighbors.append(self.vertices[key2])

def kahn(graph):
    in_degree = {key: 0 for key in graph.vertices}
    for key in graph.vertices:
        for neighbor in graph.vertices[key].neighbors:
            in_degree[neighbor.key] += 1

    queue = deque([key for key in in_degree if in_degree[key] == 0])
    topo_order = []
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.vertices[vertex].neighbors:
            in_degree[neighbor.key] -= 1
            if in_degree[neighbor.key] == 0:
                queue.append(neighbor.key)
        topo_order.append(vertex)

    if len(topo_order) != len(graph.vertices):
        return True
    else:
        return False

n,m = map(int, input().split())
gh = Graph()
for i in range(n):
    gh.add_vertex(i)

for _ in range(m):
    a,b = map(int, input().split())
    gh.add_edge(a,b)

if kahn(gh):
    print('Yes')
else:
    print('No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-06 23.34.00](https://p.ipic.vip/rsnmih.png)



### M05443:兔子与樱花

Dijkstra, http://cs101.openjudge.cn/practice/05443/

思路：



代码：

```python
import heapq


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, key, weight):
        self.neighbors[key] = weight


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)

    def add_edge(self, key1, key2, weight):
        self.add_vertex(key1)
        self.add_vertex(key2)
        self.vertices[key1].add_neighbor(key2, weight)
        self.vertices[key2].add_neighbor(key1, weight)


def dijkstra(start, end, graph):
    if start not in graph.vertices or end not in graph.vertices:
        return []
    dis = {vertex: float('inf') for vertex in graph.vertices.keys()}
    pre = {vertex: None for vertex in graph.vertices.keys()}
    dis[start] = 0
    queue = [(0, start)]
    heapq.heapify(queue)
    while queue:
        cur_dis, cur_vertex = heapq.heappop(queue)
        if cur_vertex == end:
            path = []
            cur = end
            while cur:
                path.append(cur)
                cur = pre[cur]
            path = path[::-1]
            result = []
            for i in range(len(path) - 1):
                result.append(path[i])
                result.append('->(')
                result.append(graph.vertices[path[i]].neighbors[path[i + 1]])
                result.append(')->')
            result.append(path[-1])
            return result

        if cur_dis > dis[cur_vertex]:
            continue
        for neighbor, weight in graph.vertices[cur_vertex].neighbors.items():
            nxt_dis = weight + cur_dis
            if nxt_dis < dis[neighbor]:
                dis[neighbor] = nxt_dis
                pre[neighbor] = cur_vertex
                heapq.heappush(queue, (nxt_dis, neighbor))
    return []


graph = Graph()
p = int(input())
for _ in range(p):
    graph.add_vertex(input())
q = int(input())
for _ in range(q):
    a, b, c = map(str, input().split())
    graph.add_edge(a, b, int(c))
r = int(input())
for _ in range(r):
    a, b = map(str, input().split())
    print(''.join(map(str, dijkstra(a, b, graph))))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-06 23.36.23](https://p.ipic.vip/fk01t4.png)



### T28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/

思路：

学习到warnsdoff算法，即在所有的下一步选择中，先走后续可以选择的路径数量最少的那一条。

考虑极限情况，在一个迷宫中有一个分叉口，路径A有着繁多的后续可能路径，一眼望不到头，路径B后续路径只有一条，一眼望到尽头。由于问题一定有解，因此有三种情况：路径A正确路径B不正确、路径A不正确路径B正确、路径A和路径B均正确。

均正确的情况显然应先走B。对于路径A正确的情况，如果我们选择先走路径A，当然是正确的。但是如果我们选择先走B，由于B一眼就能看到尽头，因此我们非常快速就能知道我们选择的路径是错的，从而走上路径A，这并没有带来多大的时间损失。而当路径B正确时，如果我们选择先走B，当然是正确的。但如果我们选择先走A，由于A后续的可能性繁多，我们需要花费极大的时间成本才能知道A是错误的，最终选择走上路径B。比较来看，路径B试错的时间成本更低。

综合三种情况来看，因为我们在实际问题中不可能先知道到底哪条路径是正确的，我们应该时刻选择先走B，即后续路尽可能性较少的路径。

代码：

```python
def count_moves(x, y):
    cnt = 0
    for dx, dy in dic:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
            cnt += 1
    return cnt


def dfs(x, y, k):
    if k == n ** 2:
        return True
    moves = []
    for dx, dy in dic:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
            moves.append((nx, ny))
    moves.sort(key=lambda move: count_moves(move[0], move[1]))
    for move in moves:
        vis[move[0]][move[1]] = True
        if dfs(move[0], move[1], k + 1):
            return True
        vis[move[0]][move[1]] = False
    return False


dic = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

n = int(input())
a, b = map(int, input().split())
vis = [[False] * n for _ in range(n)]
vis[a][b] = True
if dfs(a, b, 1):
    print('success')
else:
    print('fail')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-02 22.35.36](https://p.ipic.vip/mitael.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

感觉dijkstra用的比较少还挺难，每次做之前都要大概复习一下。有向图和无向图环的判定都已经搞定了，但是似乎有向图混杂无向图的判断就很难了？









