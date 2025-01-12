# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>李冠黎 工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：

1h

有提示不难。一开始自己尝试独立想出来，但是最后有点把自己绕进去了。

代码：

```python
def dfs(x,y,k):
    if x//y>=2 or y//x>=2 or x==y:
            return k
    else:
        if x<y:
            tmp=y//x
            return dfs(x,y-x*tmp,k+1)
        else:
            tmp = x // y
            return dfs(x-y*tmp, y, k + 1)

while True:
    a,b=map(int,input().split())
    if {a,b}=={0}:
        break
    if dfs(a,b,1)%2!=0:
        print("win")
    else:
        print("lose")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-12 14.22.22</u>](https://p.ipic.vip/c90y9e.png)



### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：

5min。

之前leetcode螺旋矩阵的题解简洁清晰，推荐！

代码：

```python
n=int(input())
mtr=[list(map(int,input().split())) for i in range(n)]
top,bot,left,right=0,n-1,0,n-1
cnt=0
while top<=bot and left<=right:
    tmp=0
    for i in range(left,right+1):
        tmp+=mtr[top][i]
    for i in range(top+1,bot+1):
        tmp+=mtr[i][right]
    if top < bot :
        for i in range(right-1,left,-1):
            tmp+=mtr[bot][i]
    if left < right :
        for i in range(bot,top,-1):
            tmp+=mtr[i][left]
    cnt=max(cnt,tmp)
    top,bot,left,right=top+1,bot-1,left+1,right-1
print(cnt)
```



代码运行截图 ==（至少包含有"Accepted"）==

![<u>截屏2024-12-12 16.42.12</u>](https://p.ipic.vip/b53jr8.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：

1h

自己很努力地想出来了，但是个人认为这个方法在最坏的情况下，甚至可能达到O(n**3)的时间复杂度。

看了题解感慨如此简洁

代码：

```python
n=int(input())
arr=list(map(int,input().split()))
cnt=0
pre_sum=[0]*n #建立一个类似前缀和的数组，记录到前i杯酒的时候还有多少生命值
ne=[]
if arr[0]>=0:
    pre_sum[0]=arr[0]
    cnt+=1
else:
    ne.append([arr[0],0])
for i in range(1,n):
    if arr[i]>=0:
        pre_sum[i]=pre_sum[i-1]+arr[i] #所有大于等于0的酒肯定能喝，而且为了最优，必须喝
        cnt+=1
    else:
        ne.append([arr[i],i])
        pre_sum[i]=pre_sum[i-1]
ne.sort(key=lambda x:x[0],reverse=True) #最终结果是统计需要喝多少杯，喝-10和-1都算一杯，因此负数的酒里面应该尽量先喝绝对值比较小的。这里给所有负数的酒倒着排序，尝试喝
for i in range(len(ne)):
    if pre_sum[ne[i][1]]+ne[i][0]>=0: #尝试喝一杯负数的酒，如果喝完之后还有生命，继续讨论
        for j in range(ne[i][1],n):
            pre_sum[j]+=ne[i][0] #给之后所有的前缀和都扣除对应的生命值
        if min(pre_sum[ne[i][1]:])<0: #如果之后所有的生命值还都大于等于0，那么确实可以喝。
            for j in range(ne[i][1], n): 
                pre_sum[j] -= ne[i][0] #关键是：如果之后的某个生命值小于零，那么我们就要放弃喝当前这杯酒。原因是：如果我们喝下当前这杯酒，而当前的生命值大于0后面的某个生命值却小于0，那么这中间一定有某一时刻，我们喝下了另一杯负数的酒。否则生命值不会在那一个点出现减小。如果我们不喝当前这杯酒，那么我们就可以喝下那一杯负数的酒，并且因为生命值还大于等于0，就有可能喝下更多的酒。如果我们喝下当前这杯酒，那么我们就不仅不能喝下那一杯负数的酒，后面其他的所有酒我们都喝不了了。喝这杯负数酒和那杯负数酒一换一，并且不喝当前这杯负数酒还可能喝下更多的酒，因此不喝当前这杯酒就不会使结果变坏，greedy出现了！
            continue
        cnt+=1
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-12 16.41.19</u>](https://p.ipic.vip/jck2bv.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：

30min

代码：

```python
pre_min=[]
while True:
    try:
        a=input()
        if a[2]=='s':
            o = a.index(' ')
            if pre_min:
                pre_min.append(min(int(a[o+1:]),pre_min[-1]))
            else:
                pre_min.append(int(a[o+1:]))
        elif a[2]=='n':
            if pre_min:
                print(pre_min[-1])
        elif a[2]=='p':
            if pre_min:
                pre_min.pop()
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-12 14.20.06</u>](https://p.ipic.vip/lb1dos.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：

问了AI，解答了我的很多疑惑。因为发现题解里算法的实现和网上讲的有些区别

代码：

```python
import heapq
def bfs_advance(x,y):
    queue=[(0,x,y)]
    heapq.heapify(queue)
    road[x][y]=0
    while queue:
        step,x,y = heapq.heappop(queue)
        if x==x_0 and y==y_0:
            return step
        for i in range(4):
            tx,ty=x+dic[i][0],y+dic[i][1]
            if check(tx,ty) and road[tx][ty]>step+abs(int(mtr[tx][ty])-int(mtr[x][y])):
                heapq.heappush(queue,(step+abs(int(mtr[tx][ty])-int(mtr[x][y])),tx,ty))
                road[tx][ty]=step+abs(int(mtr[tx][ty])-int(mtr[x][y]))
    return 'NO'

def check(x,y):
    if 0<=x<m and 0<=y<n and mtr[x][y]!='#' :
        return True
    else:
        return False

dic=[[0,1],[0,-1],[-1,0],[1,0]]

m,n,p=map(int,input().split())
mtr=[list(map(str,input().split())) for _ in range(m)]
for _ in range(p):
    a,b,x_0,y_0=map(int,input().split())
    if mtr[a][b]=='#' or mtr[x_0][y_0]=='#':
        print('NO')
        continue
    road=[[float('inf')]*n for _ in range(m)]
    print(bfs_advance(a,b))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-17 16.45.58</u>](https://p.ipic.vip/z2pzza.png)



### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：

1.5h

有坑。因为步数是k的整数倍的时障碍会消失，所以实际上每个节点所面临的情况是随着部署而改变的并不是一成不变的，因此这里每个节点的位置的状态都会变成一个集合，记录着当前步数除以k的余数。只有当集合里有了全部0到k -1这些数之后才可以认为这个节点所面临的所有情况都已经走遍了，这时才可以说不用再走“回头路”，否则都有可能需要重新走到这个节点。

代码：

```python
#pylint:skip-file
def bfs(x,y):
    queue=[(x,y)]
    vis[x][y].add(0)
    global step
    while queue:
        cnt=len(queue)
        for _ in range(cnt):
            nx,ny=queue.pop(0)
            if nx==tx and ny==ty:
                return step
            for i in range(4):
                dx,dy=nx+dic[i][0],ny+dic[i][1]
                if check(dx,dy):
                    queue.append((dx,dy))
                    vis[dx][dy].add((step+1)%k)
        step+=1
    return "Oop!"

dic=[[-1,0],[1,0],[0,-1],[0,1]]

def check(x,y):
    det=(step+1)%k
    if 0<=x<m and 0<=y<n and (det not in vis[x][y]) and (mtr[x][y]!='#' or det==0):
        return True
    else:
        return False

t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    mtr=[]
    for _ in range(m):
        arr = list(input())
        try:
            a,b=_,arr.index('S')
        except ValueError:
            pass
        try:
            tx,ty=_,arr.index('E')
        except ValueError:
            pass
        mtr.append(arr)

    vis=[[set() for _ in range(n)] for _ in range(m)]
    step=0
    print(bfs(a,b))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-12 16.37.38</u>](https://p.ipic.vip/kqmxvw.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

感觉对greedy的掌握情况好一些。dp还没做。变换的迷宫提示我bfs套模版要慎重，这题de上面说的那个bug花了大部分时间。



