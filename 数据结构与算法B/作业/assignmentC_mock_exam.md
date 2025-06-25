# Assignment #C: 202505114 Mock Exam

Updated 1518 GMT+8 May 14, 2025

2025 spring, Complied by <mark>李冠黎 工学院</mark>



> **说明：**
>
> 1. **⽉考**：AC<mark>5</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
> 2. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E06364: 牛的选举

http://cs101.openjudge.cn/practice/06364/

思路：



代码：

```python
n,k=map(int,input().split())
cows=[]
for _ in range(n):
    a,b=map(int,input().split())
    cows.append((a,b,_+1))
cows.sort(reverse=True)
cows=cows[:k]
cows.sort(reverse=True,key=lambda x:x[1])
print(cows[0][2])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-14 21.02.39](https://p.ipic.vip/byq40r.png)



### M04077: 出栈序列统计

http://cs101.openjudge.cn/practice/04077/

思路：

难点在读题，题目说的不清楚。譬如“栈顶端的另一侧”，不知道的以为是上面进底下出deque呢。“操作数序列”也没有进行解释。

代码：

```python
#pylint:skip-file
def dfs(path,k,left):
    global cnt
    if k==2*n:
        cnt+=1
        return
    if path!=0:
        dfs(path-1,k+1,left)
    if left>0:
        dfs(path+1,k+1,left-1)

n=int(input())
cnt=0
dfs(0,0,n)
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-14 21.03.00](https://p.ipic.vip/l23t6r.png)



### M05343:用队列对扑克牌排序

http://cs101.openjudge.cn/practice/05343/

思路：

依然是读题。“将卡牌依点数存放入各自的队列之中”并没有说明怎么进队；“对于上面的结果，依次进队后”，上文中有两个“结果”。另外感觉这个题没有卡空间复杂度，不然开字典过不了，还是想复杂了。

代码：

```python
n=int(input())
cards=list(input().split())
dik={i:[] for i in range(1,10)}
for card in cards:
    dik[int(card[1])].append(card)
cards=[]
for i,card_set in dik.items():
    print(f"Queue{i}:{' '.join(card_set)}")
    cards.extend(card_set)

dik={'A':[],'B':[],'C':[],'D':[]}
for card in cards:
    dik[card[0]].append(card)
cards=[]
for i,card_set in dik.items():
    print(f"Queue{i}:{' '.join(card_set)}")
    cards.extend(card_set)
print(*cards)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-14 21.05.28](https://p.ipic.vip/3bfv44.png)



### M04084: 拓扑排序

http://cs101.openjudge.cn/practice/04084/

思路：

纯粹的模版，不用动脑子。难度仅比第一题高。

代码：

```python
import heapq


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = []


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, p):
        if p not in self.vertices:
            self.vertices[p] = Vertex(p)

    def add_edge(self, p, q):
        self.add_vertex(p)
        self.add_vertex(q)
        self.vertices[p].neighbors.append(q)


def topo_order(graph):
    in_degree = {vertex: 0 for vertex in graph.vertices}
    for vertex in graph.vertices:
        for neighbor in graph.vertices[vertex].neighbors:
            in_degree[neighbor] += 1

    queue = [vertex for vertex in graph.vertices if in_degree[vertex] == 0]
    heapq.heapify(queue)
    result = []
    while queue:
        vertex = heapq.heappop(queue)
        for neighbor in graph.vertices[vertex].neighbors:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(queue, neighbor)
        result.append(f"v{vertex}")

    return result


v, a = map(int, input().split())
gh = Graph()
for i in range(v):
    gh.add_vertex(i + 1)
for j in range(a):
    p, q = map(int, input().split())
    gh.add_edge(p, q)

print(*topo_order(gh))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-14 21.08.34](https://p.ipic.vip/hxc41l.png)



### M07735:道路

Dijkstra, http://cs101.openjudge.cn/practice/07735/

思路：

题解完全看不懂。问了AI，写出了自己满意的答案。

dijkstra的两个关键词是“状态”和“目标”，算法就是一个在不同的状态之间更新目标的过程。在传统算法中，状态就是节点，目标就是路径长度。但在这里，当我们到达同一节点，如果花费不相同，那么不能视为同一种状态。由于总花费的限制，不同的当前花费可能使后面的路径选择发生改变，即图的结构发生改变。因此我们必须将节点和当前花费放在一起作为状态，这容易想到使用二维数组实现，`dis[node][cost]`表示目前到达node花费cost的情况下的最短距离。那么目标的更新如何呢？路径的条件和传统算法一致，不过这里可以也必须有小剪枝：当到达下一节点的花费总花费大于k时不再入队。因为在中途已经突破了k的限制，而之后没有路段的cost值为负。另一方面，如果不剪枝，那么各种总花费都会出现，而二维数组`dis[node][cost]`的大小却是有限的，可能出现`IndexError`。

代码：

```python
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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-14 21.00.20](https://p.ipic.vip/5n3v5k.png)



### T24637:宝藏二叉树

dp, http://cs101.openjudge.cn/practice/24637/

思路：

当时考场上写出来这代码觉得自己可帅了。

代码：

```python
def find_treasure(node):
    if 2 * node + 1 >= n:
        return [tree[node], 0]
    left, right = [0, 0], [0, 0]
    if 2 * node + 1 < n:
        left = find_treasure(2 * node + 1)
    if 2 * node + 2 < n:
        right = find_treasure(2 * node + 2)
    take = tree[node] + left[1] + right[1]
    no_take = max(left) + max(right)
    return [take, no_take]


n = int(input())
tree = list(map(int, input().split()))
print(max(find_treasure(0)))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-05-14 21.10.47](https://p.ipic.vip/n3ru4s.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

本次月考不理想，在1小时做完除了T5的所有题后最终依然没有AK。一方面的确对dijkstra比较生疏，另一方面在考场上想到过dfs，但是忘记了剪枝这一dfs的“好伙伴”，否则自己应该能写出来。

还参加了本周的leetcode周赛，遗憾只做出来签到题。第二题着实新奇。乍一看像之前的统计逆序，让人想到归并排序，又有点像交换最少次数获得平衡字符串，使用贪心。在此题上耗费许久，遗憾二者都不是，看了题解才发现是并查集，原来还真和数算关系紧密，这种藏得很深的的确不容易想到。传送门旅游就是二维版本的蛇梯棋。在一维情况下很容易想明白vis和queue中都不需要记录蛇和梯子是否使用过的状态，因为一旦遇到，直接传送就更优，但是二维似乎不是这样。不过根据实践，确实不需要记录，甚至传送门最多使用一次的条件也可以取消。目前还没想明白为什么。

感觉数算的东西广度大，知识杂，巩固熟练度比较难，需要做不少题。还是应该多做点题，细节上才不容易出错。







