# Assignment #A: Graph starts

Updated 1830 GMT+8 Apr 22, 2025

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

### M19943:图的拉普拉斯矩阵

OOP, implementation, http://cs101.openjudge.cn/practice/19943/

要求创建Graph, Vertex两个类，建图实现。

思路：

易漏初始化所有点。对于题目中已经给出节点数和具体节点名称，建议直接写上。不要误认为在add_edge方法中有核验就不需提前建立节点。因为有些节点有可能没有边，因此它们不会在后续建立边的操作中被实现。

代码：

```python
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def __hash__(self):
        return hash(self.name)

    # def add_neighbor(self, name):
    #     if isinstance(name, Vertex):
    #         self.neighbors.add(name)
    #     else:
    #         self.neighbors.add(Vertex(name))


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = Vertex(name)

    def add_edge(self, name1, name2):
        if name1 not in self.vertices:
            self.add_vertex(name1)
        if name2 not in self.vertices:
            self.add_vertex(name2)
        self.vertices[name1].neighbors.add(self.vertices[name2])
        self.vertices[name2].neighbors.add(self.vertices[name1])


def laplace_matrix(graph):
    size = len(graph.vertices)
    D = [[0 for y in range(size)] for x in range(size)]
    A = [[0 for y in range(size)] for x in range(size)]
    for vertex in graph.vertices.values():
        D[vertex.name][vertex.name] = len(vertex.neighbors)

    for vertex in graph.vertices.values():
        for neighbor in vertex.neighbors:
            A[vertex.name][neighbor.name] = 1

    L = [[D[x][y] - A[x][y] for y in range(size)] for x in range(size)]
    return L


n, m = map(int, input().split())
graph = Graph()
for name in range(n):
    graph.add_vertex(name)
for _ in range(m):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

L = laplace_matrix(graph)
for _ in range(len(L)):
    print(*L[_])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-24 21.28.29](https://p.ipic.vip/ca16mh.png)



### LC78.子集

backtracking, https://leetcode.cn/problems/subsets/

思路：



代码：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        def dfs(path,k):
            if k==n:
                result.append(path)
                return
            dfs(path+[nums[k]],k+1)
            dfs(path,k+1)

        dfs([],0)
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-24 20.25.16](https://p.ipic.vip/ncpu8r.png)



### LC17.电话号码的字母组合

hash table, backtracking, https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

思路：



代码：

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
          
        code={1:[],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

        n=len(digits)
        result=[]
        def dfs(path,i):
            if i==n:
                result.append(path)
                return
            for alpha in code[int(digits[i])]:
                dfs(path+alpha,i+1)
        dfs('',0)
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-29 17.38.27](https://p.ipic.vip/bw4spl.png)



### M04089:电话号码

trie, http://cs101.openjudge.cn/practice/04089/

思路：



代码：

```python
def is_consistent(phone_numbers):
    trie={}
    for number in phone_numbers:
        cur=trie
        for digit in number:
            pre=cur
            try:
                cur=cur[digit]
            except KeyError:
                cur[digit]={}
                cur=cur[digit]
            if cur == 'end':
                return "NO"
        if cur:
            return "NO"  # 易漏。如果没有这一个判断，则需要把号码按长度排序，从短到长处理。
        pre[number[-1]]='end'
    return "YES"

t=int(input())
for _ in range(t):
    n=int(input())
    phone_list=[]
    for _ in range(n):
        phone_list.append(input())
    print(is_consistent(phone_list))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-24 21.40.44](https://p.ipic.vip/0i1u7k.png)



### T28046:词梯

bfs, http://cs101.openjudge.cn/practice/28046/

思路：

学习到利用“词桶”建图的方法，本质是按照边分类。感觉不是很熟练

代码：

```python
from collections import defaultdict
from collections import deque


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = set()

    def __str__(self):
        return (
                str(self.key)
                + ' connected to: '
                + str([x.key for x in self.neighbors])
        )

    def __repr__(self):
        return f"Vertex({self.key})"

    def __hash__(self):
        return hash(self.key)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def add_edge(self, vert1, vert2):
        if vert1 not in self.vertices:
            self.add_vertex(vert1)
        if vert2 not in self.vertices:
            self.add_vertex(vert2)
        self.vertices[vert1].neighbors.add(self.vertices[vert2])
        self.vertices[vert2].neighbors.add(self.vertices[vert1])


def build_graph(words):
    buckets = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            buckets[word[:i] + '_' + word[i + 1:]].append(word)

    graph = Graph()
    for edge in buckets.keys():
        for i, word1 in enumerate(buckets[edge]):
            for word2 in buckets[edge][i + 1:]:
                graph.add_edge(word1, word2)

    return graph


def bfs(graph, start, end):
    queue = deque([(graph.vertices[start], [start])])
    visited = {graph.vertices[start]}
    while queue:
        vertex, path = queue.popleft()
        if vertex.key == end:
            return ' '.join(path)
        for neighbor in vertex.neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor.key]))
                visited.add(neighbor)
    return 'NO'


n = int(input())
words = []
for i in range(n):
    words.append(input())

graph = build_graph(words)
start, end = input().split()
print(bfs(graph, start, end))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-29 17.39.58](https://p.ipic.vip/5j4y6m.png)



### T51.N皇后

backtracking, https://leetcode.cn/problems/n-queens/

思路：

之前那个视频讲的真好

代码：

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        dfs(n,[],0,set(),set(),set(),result)
        ans=[]
        for case in result:
            tmp=[]
            for loco in case:
                tmp.append('.'*loco+'Q'+'.'*(n-1-loco))
            ans.append(tmp)
        return ans

def dfs(n,path,i,seen_col,seen_ziga,seen_zigb,result):
    if i==n:
        result.append(path)
        return
    for j in range(n):
        if j not in seen_col and i-j not in seen_ziga and i+j not in seen_zigb:
            dfs(n,path+[j],i+1,seen_col|{j},seen_ziga|{i-j},seen_zigb|{i+j},result)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-29 17.29.57](https://p.ipic.vip/v499ac.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

期中周在明天的考试后终于结束，五一可以学一学数算了。目前绝大部分算法都已经了解，接下来要提高熟练度。对于少部分较难的内容（比如这次的词桶）目前不知道有什么办法，感觉也不好系统学习。









