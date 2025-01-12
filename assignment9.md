# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>李冠黎 工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：

30min，没读清楚题导致的。

第一遍做的时候输出的是有多少块连通区域。第二遍做的时候输出所有连通区域的面积总和。

代码：

```python
#pylint: skip-file
def dfs(x,y):
    global tmp
    tmp+=1
    mtr[x][y]='.'
    for i in range(8):
        tx=x+dic[i][0]
        ty=y+dic[i][1]
        if check(tx,ty):
            dfs(tx,ty)

def check(x,y):
    if 0<=x<n and 0<=y<m and mtr[x][y]=='W':
        return True
    else:
        return False

dic=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    mtr=[list(input()) for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(m):
            if mtr[i][j]=='W':
                tmp=0
                dfs(i,j)
                ans=max(ans,tmp)
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-22 15.36.33](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-22 15.36.33.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：



代码：

```python
seen=set()
def bfs(x,y):
    seen.add((x,y))
    q=[(x,y)]
    step=0
    while q:
        cnt=len(q)
        for _ in range(cnt):
            nx,ny=q.pop(0)
            if mtr[nx][ny]==1:
                return step
            for i in range(4):
                if check(nx+dic[i][0],ny+dic[i][1]):
                    q.append((nx+dic[i][0],ny+dic[i][1]))
                    seen.add((nx+dic[i][0],ny+dic[i][1]))
        step+=1
    return 'NO'

def check(x,y):
    if 0<=x<m and 0<=y<n and mtr[x][y]!=2 and (x,y) not in seen:
        return True
    else:
        return False

dic=[[0,1],[0,-1],[1,0],[-1,0]]

m,n=map(int,input().split())
mtr=[]
for _ in range(m):
    mtr.append(list(map(int,input().split())))

print(bfs(0,0))
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-11-21 23.27.48](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-21 23.27.48.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：



代码：

```python
#pylint: skip-file
def dfs(x,y,k):
    global cnt
    if k==m*n:
        cnt+=1
        return
    for i in range(8):
        tx=x+dic[i][0]
        ty=y+dic[i][1]
        if check(tx,ty):
            vis[tx][ty]=True
            dfs(tx,ty,k+1)
            vis[tx][ty]=False

def check(x,y):
    if 0<=x<m and 0<=y<n and vis[x][y]==False:
        return True
    else:
        return False

dic=[[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
t=int(input())
for _ in range(t):
    cnt=0
    m,n,a,b=map(int,input().split())
    vis = [[False] * n for _ in range(m)]
    vis[a][b]=True
    dfs(a,b,1)
    print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-22 00.21.01](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-22 00.21.01.png)



### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：



代码：

```python
cur_sup=float('-inf')
cur_road=[]
def dfs(x,y,road:list,sup:int):
    global cur_sup
    global cur_road
    if x==n-1 and y==m-1:
        if sup>cur_sup:
            cur_sup=sup
            cur_road=road
    else:
        for i in range(4):
            tx=x+dic[i][0]
            ty=y+dic[i][1]
            if check(tx,ty):
                vis[tx][ty]=True
                dfs(tx,ty,road+[[tx,ty]],sup+mtr[tx][ty])
                vis[tx][ty]=False

dic=[[-1,0],[0,-1],[1,0],[0,1]]

def check(x,y):
    if 0<=x<n and 0<=y<m and vis[x][y]==False:
        return True
    else:
        return False

n,m=map(int,input().split())
mtr=[]
for _ in range(n):
    mtr.append(list(map(int,input().split())))

vis=[[False]*m for _ in range(n)]
vis[0][0]=True
dfs(0,0,[[0,0]],mtr[0][0])
for i in range(len(cur_road)):
    print(cur_road[i][0]+1,cur_road[i][1]+1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-22 10.29.16](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-22 10.29.16.png)





### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：



代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n]+[[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-22 09.53.30](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-22 09.53.30.png)



### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：



代码：

```python
import math
a=int(input())
key=False
def cut(x):
    global key
    x=int(x)
    if int(math.sqrt(x))==math.ceil(math.sqrt(x)) and x!=0:
        key=True
    else:
        tx=str(x)
        for i in range(len(tx)):
            tmp=int(tx[:i+1])
            if int(math.sqrt(tmp))==math.ceil(math.sqrt(tmp)) and tmp!=0:
                cut(tx[i+1:])

cut(a)
if key:
    print('Yes')
else:
    print('No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-22 15.11.38](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-22 15.11.38.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

目前感觉还是greedy最难，dp次之。本次作业的dfs和bfs都是模版题，很快就解决了，之后信心满满地去leetcode上找了一个greedy，直接做麻了。

最近每日选做的题感觉都不是特别难，是不是也和没有greedy有关

