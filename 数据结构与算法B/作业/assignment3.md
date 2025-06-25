# Assignment #3: 惊蛰 Mock Exam

Updated 1641 GMT+8 Mar 5, 2025

2025 spring, Complied by <mark>李冠黎 工学院</mark>



> **说明：**
>
> 1. **惊蛰⽉考**：AC<mark>5</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
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

### E04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015



思路：

3)'@'之后至少要有一个'.'，并且'@'不能和'.'直接相连

没有考虑到@前面有.导致WA。但个人认为题目也有描述不严谨的问题，直接把后面半句列为第四点不就好了吗？

代码：

```python
while True:
    try:
        add=input()
        try:
            p=add.index('@')
            n=add.count('@')
            try:
                q=add[p:].index('.')+p
                if q==p+1 or add[0] in {'@','.'} or add[-1] in {'@','.'} or n!=1 or add[p-1]=='.':
                    print('NO')
                else:
                    print('YES')
            except ValueError:
                print('NO')
        except ValueError:
            print('NO')
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-11 17.25.48](https://p.ipic.vip/qebp8r.png)



### M02039: 反反复复

implementation, http://cs101.openjudge.cn/practice/02039/



思路：

由于是走S形。还原的时候可以考虑两两一组，这样每一组的位置就都是确定的，

代码：

```python
col=int(input())
code=input()
row=len(code)//col
result=[]
for j in range(0,col):
    result.append(code[j])
    for i in range(col*2+j,len(code),col*2):
        result.append(code[i-1-2*j])
        result.append(code[i])
    if row%2==0:
        result.append(code[-1-j])
print(''.join(result))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-11 17.27.08](https://p.ipic.vip/uefii2.png)



### M02092: Grandpa is Famous

implementation, http://cs101.openjudge.cn/practice/02092/



思路：



代码：

```python
from collections import defaultdict
while True:
    record=defaultdict(int)
    n,m=map(int,input().split())
    if {n,m}=={0}:
        break
    for _ in range(n):
        arr=list(map(int,input().split()))
        for player in arr:
            record[player]+=1
    second=sorted(list(record.values()),reverse=True)[1]
    result=[]
    for player,count in record.items():
        if count==second:
            result.append(player)
    result.sort()
    print(*result)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-11 17.27.59](https://p.ipic.vip/0cdh2n.png)



### M04133: 垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/



思路：

之前计概点题，遍历只有20个的垃圾而不是所有位置这种反向思考的解题方式很巧妙。

代码：

```python
from collections import defaultdict
bomb=defaultdict(int)
d=int(input())
n=int(input())
for _ in range(n):
    x,y,i=map(int,input().split())
    for tx in range(max(0,x-d),min(x+d+1,1025)):
        for ty in range(max(0,y-d),min(y+d+1,1025)):
            bomb[(tx,ty)] += i
max_amt=max(bomb.values())
max_cnt=0
for px,py in bomb:
    if bomb[(px,py)]==max_amt:
        max_cnt+=1
print(max_cnt,max_amt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-11 17.28.19](/Users/liguanli/Library/Application Support/typora-user-images/截屏2025-03-11 17.28.19.png)



### T02488: A Knight's Journey

backtracking, http://cs101.openjudge.cn/practice/02488/



思路：



代码：

```python
def dfs(path,k,seen):
    global result
    if k==p*q:
        tmp=[]
        for x,y in path:
            tmp.append(chr(65+y))
            tmp.append(f'{x + 1}')
        result.append(''.join(tmp))
        return
    nx,ny=path[-1]
    for i in range(8):
        tx,ty=nx+dic[i][0],ny+dic[i][1]
        if 0<=tx<p and 0<=ty<q and (tx,ty) not in seen:
            dfs(path+[(tx,ty)],k+1,seen|{(tx,ty)})
    return

dic=[[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]

n=int(input())
for _ in range(n):
    print(f'Scenario #{_+1}:')
    p,q=map(int,input().split())
    result=[]
    dfs([(0,0)],1,{(0,0)})
    if result:
        result.sort()
        print(result[0])
    else:
        print('impossible')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-11 17.29.16](https://p.ipic.vip/7u9azm.png)



### T06648: Sequence

heap, http://cs101.openjudge.cn/practice/06648/



思路：

拼尽全力无法战胜

复制一个AI的

代码：

```python
import heapq

def merge_two_sorted_arrays(R, S, n):
    heap = []
    visited = set()
    
    initial_sum = R[0] + S[0]
    heapq.heappush(heap, (initial_sum, 0, 0))
    visited.add((0, 0))
    
    result = []
    for _ in range(n):
        current_sum, i, j = heapq.heappop(heap)
        result.append(current_sum)
        
        if i + 1 < len(R) and (i+1, j) not in visited:
            sum_val = R[i+1] + S[j]
            heapq.heappush(heap, (sum_val, i+1, j))
            visited.add((i+1, j))
            
        if j + 1 < len(S) and (i, j+1) not in visited:
            sum_val = R[i] + S[j+1]
            heapq.heappush(heap, (sum_val, i, j+1))
            visited.add((i, j+1))
    
    return result

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    
    T = int(input[ptr])
    ptr += 1
    
    for _ in range(T):
        m = int(input[ptr])
        n = int(input[ptr+1])
        ptr += 2
        
        arrays = []
        for _ in range(m):
            arr = list(map(int, input[ptr:ptr+n]))
            ptr += n
            arr.sort()
            arrays.append(arr)
        
        if m == 0:
            print()
            continue
        
        R = arrays[0]
        if m == 1:
            res = R[:n]
            print(' '.join(map(str, res)))
            continue
        
        for i in range(1, m):
            S = arrays[i]
            new_R = merge_two_sorted_arrays(R, S, n)
            R = new_R
        
        print(' '.join(map(str, R)))

if __name__ == "__main__":
    main()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2025-03-11 16.16.50](https://p.ipic.vip/5ss0x6.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

本次月考迟到10分钟，调试电脑10分钟，算下来一个小时AC了前面五道题。但无奈苯人确实水平不高，怎么想也没有解决第六题，要开始重视heapq了。其实知道最后一题是heapq，但是不会，这是因为对heapq的理解浅薄导致的。只会单一地使用其功能——返回最小值，但是一旦heapq成为整个执行逻辑的一部分是九想不出来了。之前候选人追踪和中位数查询也都没有做出来。需要加强练习，先从看懂题解开始。再慢慢总结，找一些题。也许会和dp，bfs这种类似，同一类题目都有着相似的特征？









