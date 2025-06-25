# Assignment #D: 图 & 散列表

Updated 2042 GMT+8 May 20, 2025

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

### M17975: 用二次探查法建立散列表

http://cs101.openjudge.cn/practice/17975/

<mark>需要用这样接收数据。因为输入数据可能分行了，不是题面描述的形式。OJ上面有的题目是给C++设计的，细节考虑不周全。</mark>

```python
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
```



思路：

恶心哦。不仅是输入数据恶心，还可能出现重复的数字。

代码：

```python
def H(key):
    global seen
    i=0
    tmp=1
    start=key%m
    p=start
    while table[p] and table[p]!=key:
        if i>0:
            i-=tmp
        else:
            i+=tmp
        tmp+=1
        p=(start+i*abs(i))%m
    table[p]=key
    return p

import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
nums = [int(i) for i in data[index:index+n]]
table=[None]*m
ans=[H(num) for num in nums]
print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-27 16.23.38](https://p.ipic.vip/u1kolw.png)



### M01258: Agri-Net

MST, http://cs101.openjudge.cn/practice/01258/

思路：

使用并查集检查两个点之间是否已经连通，若已连通，则不需要再连，跳过这条边。

代码：

```python
class UnionFind:
    def __init__(self,size):
        self.parents={i:i for i in range(size)}
        self.ranks={i:0 for i in range(size)}

    def find(self,x):
        if self.parents[x]!=x:
            self.parents[x]=self.find(self.parents[x])
        return self.parents[x]

    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx!=rooty:
            if self.ranks[rootx]>self.ranks[rooty]:
                self.parents[rooty]=rootx
            elif self.ranks[rootx]<self.ranks[rooty]:
                self.parents[rootx]=rooty
            else:
                self.parents[rooty]=rootx
                self.ranks[rootx]+=1

while True:
    try:
        n=int(input())
        uf=UnionFind(n)
        graph=[list(map(int,input().split())) for i in range(n)]
        queue=[]
        for i in range(n):
            for j in range(i+1,n):
                queue.append((graph[i][j],i,j))
        queue.sort(reverse=True)
        i=0
        ans=0
        while i<n-1:
            weight,p,q=queue.pop()
            if uf.find(p)==uf.find(q):
                continue
            ans+=weight
            uf.union(p,q)
            i+=1
        print(ans)
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-27 16.22.14](/Users/liguanli/Library/Application Support/typora-user-images/截屏2025-05-27 16.22.14.png)



### M3552.网络传送门旅游

bfs, https://leetcode.cn/problems/grid-teleportation-traversal/

思路：



代码：

```python
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        from collections import deque
        from collections import defaultdict
        def bfs(start, end):
            a,b=start
            c,d=end
            queue=deque([(a,b,0)])
            vis={(a,b)}
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
                nx,ny,step=queue.popleft()
                if nx==c and ny==d:
                    return step
                for i in range(4):
                    tx,ty=nx+dic[i][0],ny+dic[i][1]
                    if check(tx,ty) and (tx,ty) not in vis:
                        queue.append((tx,ty,step+1))
                        vis.add((tx,ty))
                        if matrix[tx][ty]!='.':
                            for t in portal_list[matrix[tx][ty]]:
                                tx1, ty1 = t
                                if tx1 == tx and ty1 == ty:
                                    continue
                                else:
                                    if (tx1, ty1) not in vis:
                                        queue.append((tx1, ty1, step+1))
                                        vis.add((tx1, ty1))
            return -1
        
        dic=[[0,1],[0,-1],[1,0],[-1,0]]
        
        def check(x,y):
            if 0<=x<m and 0<=y<n and matrix[x][y]!='#':
                return True
            return False

        m,n=len(matrix),len(matrix[0])
        portal_list=defaultdict(list)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]!='#' and matrix[i][j]!='.':
                    portal_list[matrix[i][j]].append((i,j))
        
        return bfs((0,0),(m-1,n-1))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-27 16.21.44](https://p.ipic.vip/8yhv79.png)



### M787.K站中转内最便宜的航班

Bellman Ford, https://leetcode.cn/problems/cheapest-flights-within-k-stops/

思路：

和普通的bellman-ford有一个区别。在经典版本中，做k次循环可以保证找完所有长度不超过k的路径，但是不能保证没找到过长度大于k的路径。原因是在一次循环里可能先更新了之前的节点紧接着就更新该节点的邻居，这样就利用了之前节点的更新，使得一次循环里找的路程大于1，找过的路径变长。而在这里，必须保证找且只找长度不超过k的路径，因此就是要防止在同一次循环中利用更新过的节点信息，即第k次循环利用的信息都必须只能是前面k-1循环的信息。

代码：

```python
import heapq
class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def __str__(self):
        return str(self.key)

class Graph(object):
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,p):
        if p not in self.vertices:
            self.vertices[p] = Vertex(p)

    def add_edge(self,p,q,weight):
        self.add_vertex(p)
        self.add_vertex(q)
        self.vertices[p].neighbors[q] = weight

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def bellman_fold(graph, start, end,k):
            dis={vertex:float('inf') for vertex in graph.vertices}
            dis[start] = 0
            for _ in range(k+1):
                pre_dis=deepcopy(dis)
                for vertex in graph.vertices:
                    for neighbor,weight in graph.vertices[vertex].neighbors.items():
                        if pre_dis[vertex]+weight<dis[neighbor]:
                            dis[neighbor] = pre_dis[vertex]+weight
            if dis[end]!=float('inf'):
                return dis[end]
            else:
                return -1

        gh=Graph()
        for i in range(n):
            gh.add_vertex(i)
        for flight in flights:
            gh.add_edge(flight[0],flight[1],flight[2])
        return bellman_fold(gh,src,dst,k)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-27 16.15.33](https://p.ipic.vip/k44omr.png)



### M03424: Candies

Dijkstra, http://cs101.openjudge.cn/practice/03424/

思路：

把题目翻译成最短路径问题是最有趣的部分，关键是“差额最小的要求是最重要的”，差额更大的要求必须服从更小的。但是题面表述似乎有一点问题。按照最终答案的理解，就是N比1最多多多少，不考虑1比N最多多多少。否则要算两遍取最大值。

代码：

```python
import heapq

def dijkstra(graph,start,end):
    dis={i:float('inf') for i in range(n+1)}
    dis[start]=0
    queue=[(0,start)]
    heapq.heapify(queue)
    while queue:
        cur_dis,cur_node=heapq.heappop(queue)
        if cur_node==end:
            return cur_dis
        if cur_dis>dis[cur_node]:
            continue
        for neighbor,weight in graph[cur_node]:
            n_dis=cur_dis+weight
            if n_dis<dis[neighbor]:
                dis[neighbor]=n_dis
                heapq.heappush(queue,(n_dis,neighbor))
    return -1

n,m=map(int,input().split())
kids=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    kids[a].append((b,c))

ans=dijkstra(kids,1,n)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-27 15.53.41](https://p.ipic.vip/emzl3e.png)



### M22508:最小奖金方案

topological order, http://cs101.openjudge.cn/practice/22508/

思路：

明显的拓扑排序。大体上讲，队伍被分成很多层，每层发同一数量奖金。一开始入度就为零的队伍在最底层，他们谁都没赢，发最低的奖金。把这些队伍和其对应的边删除后，剩下入度为零的队伍只赢了在最底层的队伍，在倒数第二层，发第二低的奖金……

代码：

```python
from collections import deque
class Vertex:
    def __init__(self,key):
        self.key=key
        self.neighbors=[]

class Graph:
    def __init__(self):
        self.vertices={}

    def add_vertex(self,p):
        if p not in self.vertices:
            self.vertices[p]=Vertex(p)

    def add_edge(self,p,q):
        self.add_vertex(p)
        self.add_vertex(q)
        self.vertices[p].neighbors.append(q)

def prize(graph):
    in_degrees={vertex:0 for vertex in graph.vertices}
    for vertex in graph.vertices:
        for neighbor in graph.vertices[vertex].neighbors:
            in_degrees[neighbor]+=1

    cnt=0
    mon=0
    queue=deque([vertex for vertex in graph.vertices if in_degrees[vertex]==0])
    while queue:
        tmp=len(queue)
        for _ in range(tmp):
            vertex=queue.popleft()
            cnt+=mon
            for neighbor in graph.vertices[vertex].neighbors:
                in_degrees[neighbor]-=1
                if in_degrees[neighbor]==0:
                    queue.append(neighbor)
        mon+=1
    return cnt+len(graph.vertices)*100

n,m=map(int,input().split())
gh=Graph()
for i in range(n):
    gh.add_vertex(i)

for _ in range(m):
    a,b=map(int,input().split())
    gh.add_edge(b,a)

print(prize(gh))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-27 15.59.02](https://p.ipic.vip/96wnkp.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

又因为各种ddl停了几天每日选做，慢慢赶上来了。这周印象最深的题是零数组变换，差分和前缀和的方法竟然怎么也想不到，得看答案。但这三个题又综合地考察了多个知识点，值得一做。另外，很多图的题不一定非要按照模版定义Vertex类和Graph类，按需使用邻接表或者邻接矩阵或者像subway那道题直接使用了一个trail列表都是有可能的。

cheating sheet要开始准备了。感觉内容会非常多，毕竟数算模版太多了









