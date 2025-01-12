## 语法

```python
original_class = set(range(1, n + 1))
remaining_set = set(remaining_children)
missing_children = sorted(original_class - remaining_set)
```

Python中的集合可以做+或-，取并集或补集

```python
print(" ".join(map(str, missing_children)))
```

join方法：`str.join( )` 表示把( )中的元素之间用str分隔开

```python
str[a:b+1]=[x]*(b-a+1)
```

`[x]*(b-a+1)`可以创建一个长度为b-a+1，里面的元素全是x的列表。这个语句是将某个字符串中第a个到第b个之间（包括a和b）的所有元素全变成x（用全是x的列表替换原有的列表）。

```python
data = [[int(x) for x in input().split()] for i in range(N)]
def take_second(n) :
    return n[1]
data.sort(key = take_second)
```

data是一个列表，其中的每个元素都是一个小列表。这段代码让data中的小列表按照每个小列表中的第二个元素进行从小到大排序。

```python
result=[s.replace('15','F') for s in result]
```

如果一个列表中的元素都是字符串，可以把某一个元素全部替换成另一个元素。

这句代码把列表result中所有15替换成了F。

```python
from functools import lru_cache
```

lru_cache是一个来自于functools的装饰器，可以把函数的返回值缓存起来，当函数下一次遇到同样的输入时，将直接从缓存中调用返回值，而不必重复计算。

用法：在def语句的上一行写`@lru_cache(maxsize=None)`，`maxsize`参数指定缓存的空间上限，`None`即没有限制。

lru_cache是独立的。如果有多个函数都要分别存储结果，那么每个函数前面都要写@lru_cache.

```python
data=[]
data.append(5)
```

```python
seen=set()
seen.add(5)
seen.remove(7)
```

列表添加用`append`，集合添加用`add`，集合有`remove`方法

在集合中查找一个元素的时间复杂度大部分时候接近O(1)，但因为列表中的元素是有序的，在列表中查找的时间复杂度绝大部分时候比集合中大。

列表是不可哈希的，而元组是可哈希的，前提是元组中的元素都是可哈希的。这就意味着如果一个列表中的元素是小列表，那么可以把这些小列表变成元组，然后利用set来快速去重。

```python
print("%.3f" % result)
```

对`result`取三位小数

```python
a=List.find(",")
b=List.index(",")
```

`find`和`index`都可以查找某个字符所在的位置。不同是`find` 在找不到字符时返回 `-1`，而 `index` 会抛出异常。

### ASCII码

![截屏2024-12-10 16.00.25](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-12-10 16.00.25.png)

### heapq

1. **`heapq.heappush(heap, item)`**：
   - 将 `item` 添加到堆 `heap` 中，并保持堆的性质。
2. **`heapq.heappop(heap)`**：
   - 从堆 `heap` 中弹出并返回最小的元素，同时保持堆的性质。
3. **`heapq.heapify(x)`**：
   - 将列表 `x` 转换为堆，这是一个原地操作。
4. **`heapq.heappushpop(heap, item)`**：
   - 先将 `item` 推入堆中，然后弹出并返回堆中的最小元素。这比单独调用 `heappush` 和 `heappop` 更高效。
5. **`heapq.heapreplace(heap, item)`**：
   - 弹出并返回堆中的最小元素，然后将 `item` 推入堆中。这个操作保证了堆的大小不变。
6. **`heapq.nsmallest(n, iterable, key=None)`**：
   - 返回 `iterable` 中最小的 `n` 个元素。如果提供了 `key` 函数，则根据 `key` 的结果进行比较。
7. **`heapq.nlargest(n, iterable, key=None)`**：
   - 返回 `iterable` 中最大的 `n` 个元素。如果提供了 `key` 函数，则根据 `key` 的结果进行比较。

### sys相关语句

```python
import sys
sys.setrecursionlimit(1 << 30)  # 递归深度限制为2**30
```

```python
import sys
input=sys.stdin.read
data=input().split()  # 一般输入都是以空格隔开的
print(data)
```

### 全排列

```python
import itertools
for item in itertools.product('AB', repeat=2):  # 生成笛卡尔积
    print(item)  # ('A', 'A')\n('A', 'B')\n('B', 'A')\n('B', 'B')
for item in itertools.product('AB', '12'):
    print(item)  # ('A', '1')\n('A', '2')\n('B', '1')\n('B', '2')
result = list(permutations([1,2,3]，))  # [(1, 2, 3), (1, 3, 2), ……];生成全排列
```

### 普通字典

1. 访问元素

- **通过键访问**：直接使用方括号 `[]` 访问字典中的值。

```python
value = my_dict['a']  # 返回 1
```

- **`get()` 方法**：安全地访问键对应的值，如果键不存在则返回默认值（可选）。

```python
value = my_dict.get('d', 0)  # 如果 'd' 不存在，返回 0
```

2. 添加或修改元素

- **直接赋值**：使用方括号 `[]` 添加新键值对或更新现有键的值

```python
my_dict['d'] = 4  # 添加新的键值对
my_dict['a'] = 10  # 更新已有的键值对
```

3. 删除元素

- **`pop()` 方法**：移除指定键的项并返回其值，如果键不存在可以指定默认返回值。

```python
value = my_dict.pop('a')  # 移除键 'a' 并返回其值
```

- **`popitem()` 方法**：无参数，随机移除并返回一个键值对（在 Python 3.7+ 中按插入顺序移除最后一个项）。

```python
key, value = my_dict.popitem()
```

- **`del` 语句**：直接删除指定键的项。

```python
del my_dict['b']
```

4. 检查键是否存在

- **`in` 关键字**：检查字典中是否包含某个键。

```python
if 'a' in my_dict:
    print("Key 'a' exists")
```

5. 获取所有键、值或键值对

- **`keys()` 方法**：返回字典中所有键的视图对象。

```
keys = my_dict.keys()
```

- **`values()` 方法**：返回字典中所有值的视图对象。

```python
values = my_dict.values()
```

- **`items()` 方法**：返回字典中所有键值对的视图对象。

```python
items = my_dict.items()
```

6. 更新字典

- **`update()` 方法**：使用另一个字典或键值对序列更新当前字典。

```python
my_dict.update({'e': 5, 'f': 6})
# 或者
my_dict.update(e=5, f=6)
```

### defaultdict

`defaultdict` 是 Python 的 `collections` 模块中提供的一个类，它是字典（`dict`）的一个子类，具有默认值的功能。当你访问一个不存在的键时，它会自动为该键生成一个默认值，而不是抛出 `KeyError`。这在处理计数、分组等场景时非常有用。

```python
from collections import defaultdict

ldict = defaultdict(int)
rdict = defaultdict(int)
```

- **`defaultdict(int)`**：创建了一个 `defaultdict` 对象，其默认工厂函数是 `int`。这意味着如果你访问一个不存在的键，它会自动调用 `int()` 函数来生成默认值，而 `int()` 返回的是 `0`。
- **`ldict` 和 `rdict`**：这两个变量分别指向两个不同的 `defaultdict` 实例，它们的行为相同，即当访问不存在的键时返回 `0`。

### bfs注意事项

1.如果需要多次使用（多个case），记得每次都要初始化`seen`集合，即bfs的执行代码前不要忘了`seen=set()`

2.如果要计算步数，那么每次都要把这一层的点都pop完毕。`step+=1`一定要写在弹出的for循环之后，而不是遍历dic的for循环之后。

3.计算步数不要忘记不能到达的情况。不要忘记在bfs函数的最后写上`return 0`（或者相应的表示无解的量）

```python
def bfs(x,y):
    queue=[(x,y)]
    seen.add((x,y))
    step=0
    while queue:
        cnt=len(queue)
        for _ in range(cnt):
            nx,ny=queue.pop(0)
            if nx==target_x and ny==target_y:
                return step
            for i in range(4):
                tx = nx + dic[i][0]
                ty = ny + dic[i][1]
                if check(tx,ty):
                    queue.append((tx,ty))
                    seen.add((tx,ty))
        step+=1 #一个tab的事
    return 0 #注意要写
```

### dijkstra示例

```python
# 胡睿诚	174ms

import heapq
m, n, p = map(int, input().split())
info = []
for _ in range(m):
    info.append(list(input().split()))
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dijkstra(start_r, start_c, end_r, end_c):
    pos = []
    dist = [[float('inf')] * n for _ in range(m)]
    if info[start_r][start_c] == '#':
        return 'NO'
    dist[start_r][start_c] = 0
    heapq.heappush(pos, (0, start_r, start_c))
    while pos:
        d, r, c = heapq.heappop(pos)
        if r == end_r and c == end_c:
            return d
        h = int(info[r][c])
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n and info[nr][nc] != '#':
                if dist[nr][nc] > d + abs(int(info[nr][nc]) - h):
                    dist[nr][nc] = d + abs(int(info[nr][nc]) - h)
                    heapq.heappush(pos, (dist[nr][nc], nr, nc))
    return 'NO'


for _ in range(p):
    x, y, z, w = map(int, input().split())
    print(dijkstra(x, y,z,w))
```

### dfs示例：八皇后

```python
def backtrack(path=[],i=0,col_selected=[],z_diag=set(),f_diag=set()):
    if i==n:
        result.append(path)
        return
    for j in range(n):
        if j not in col_selected and i-j not in z_diag and i+j not in f_diag:
            backtrack(path+[j+1],i+1,col_selected+[j],z_diag|{i-j},f_diag|{i+j})

result=[]
n=8
```

### 康托展开

```python
import math
m=int(input())
for _ in range(m):
    n, k = map(int,input().split())
    arr=list(map(int,input().split()))

    x=0
    cdd = [int(x) + 1 for x in range(n)]
    i=1
    for dig in arr:
        p=cdd.index(dig)
        x+=p*math.factorial(n-i)
        del cdd[p]
        i+=1

    x_new=(x+k)%math.factorial(n)

    cdd = [int(x) + 1 for x in range(n)]
    result=[]
    i=1
    while cdd:
        result.append(cdd[x_new//(math.factorial(n-i))])
        del cdd[x_new // (math.factorial(n - i))]
        x_new = x_new%(math.factorial(n - i))
        i+=1

    print(*result)
```

用全局变量不要忘记`# pylint: skip-file`

## 算法优化

如果给一个列表，其中元素都是整数。求从第m个到第n个的和时，最常见的是这么写：

```python
print(sum(data[m:n+1]))
```

但如果有很多组m,n，求很多组和的时候，这种方法很容易超时。因为对n个数求和，python实际上是一个一个加，每一步是O(1)，合起来是O(n)。很多组的时间复杂度非常高。

这里的关键是有很多数据浪费了。比如我们先求第1个到第20个的和，我们会从第1个加到第20个。如果我们接下来求第1个到第5个的和，我们要重新加一遍。但实际上在之前从第1个加到第20个的过程中，程序是算出来过前5个的和的，因为程序是一个一个加的。如果我们能把之前加和中的一些结果储存，后面需要的时候直接调用，就减少了重复计算，这种浪费就会减少。

```python
def prefix_sums(data):
  prefix_sums=[0]*(len(data)+1)
  for i in range(1,len(data)+1):
    prefix_sums[i]=prefix_sums[i-1]+data[i-1]
  return prefix_sums
```

这段代码的时间复杂度为O(len(data))，但它把加和每一步的结果都储存在`prefix_sums`对应的位置中，即前n个数的和就是`pfefix_sums[n]`。这样仅需一次全面的加和，我们就已经获取到后面计算所需要的全部信息。

这时计算从第m个到第n个的和时，只需：

```python
print(prefix_sums[n]-prefix_sums[m-1])
```

一步搞定！这种方法在(m,n)组数越多的时候越有效。

### 双指针

用于列表，指针就是形如list[x]的东西。双指针通常用于需要获取列表中两个位置的元素，且这些位置还是随着程序的进行而变化的时候。需要注意的是，两个指针并不一定是指向两个列表，同一个列表也是有可能的。

例1:两个列表的两个指针

给定两个升序的正整数序列A和B，将它们合并成一个新的升序序列并输出。每个序列的元素不大于10**6。

```python
n,m=map(int,input().split())
A=[int(x) for x in input().split()]
A.append(10**7)
B=[int(x) for x in input().split()]
B.append(10**7)
a=0
b=0
result=[]
while a<n or b<m:
    if A[a]<=B[b]:
        result.append(A[a])
        a+=1
    else:
        result.append(B[b])
        b+=1
print(*result)
```

