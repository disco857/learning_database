# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>李冠黎 工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：

10min

代码：

```python
def check(coin,weight,no):
    if coin in state[no][0]:
        if weight=='heavy':
            if state[no][2]=='up':
                return True
            else:
                return False
        else:
            if state[no][2]=='down':
                return True
            else:
                return False
    elif coin in state[no][1]:
        if weight=='heavy':
            if state[no][2]=='down':
                return True
            else:
                return False
        else:
            if state[no][2]=='up':
                return True
            else:
                return False
    else:
        if state[no][2]=='even':
            return True
        else:
            return False

t=int(input())
choices=['heavy','light']
coins=['A','B','C','D','E','F','G','H','I','J','K','L']
for _ in range(t):
    state=[list(map(str,input().split())) for _ in range(3)]
    for coin in coins:
        for choice in choices:
            if check(coin,choice,0) and check(coin,choice,1) and check(coin,choice,2):
                print(coin+' is the counterfeit coin and it is '+choice+'.')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u><u>截屏2024-12-19 17.59.58</u></u>](https://p.ipic.vip/ai6wbf.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：

20min，独立做出，很高兴！但平心而论，没有dp的提示的话很难想到，看起来太像搜索了，但细致一想搜索又不太行。倒是看到题之后的第一反应：如果一条路径的开头连接了更高的点，那么把这个点加上就组成了一条更长的路径，在最后派上了用场。

而落实到代码又需要heapq的辅助。我任取一个点，不能靠把它周边比它小的点的路径长度+1来确定以它结束的路径长度，因为它周边的那些点还没算出来呢。但是高度最低的点是不用算的，肯定是1。先算最低点，之后次低点就能算了，因为所有在它之前的点（的可能）都算过了。如此一来，heapq就出现了。（看了题解发现sort就行了……，被自己蠢到）

代码：

```python
import heapq
dic=[[0,1],[0,-1],[1,0],[-1,0]]
m,n=map(int,input().split())
mrt=[]
mtr=[]
for i in range(m):
    tmp=list(map(int,input().split()))
    mtr.append(tmp)
    for j in range(len(tmp)):
        mrt.append((tmp[j],i,j))
heapq.heapify(mrt)
dp=[[1]*n for _ in range(m)]
while mrt:
    cur,x,y=heapq.heappop(mrt)
    for k in range(4):
        tx,ty=x+dic[k][0],y+dic[k][1]
        if 0<=tx<m and 0<=ty<n and mtr[tx][ty]<cur:
            dp[x][y]=max(dp[x][y],dp[tx][ty]+1)
ans=0
for _ in range(len(dp)):
    ans=max(ans,max(dp[_]))
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![<u><u>截屏2024-12-19 23.33.06</u></u>](https://p.ipic.vip/e1fq2s.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：

25min 普通dfs，只有vis的判断略有区别。

代码：

```python
result='no'
def dfs(x_1,y_1,x_2,y_2):
    global result
    vis[x_1][y_1],vis[x_2][y_2]=True,True
    if mtr[x_1][y_1]==9 or mtr[x_2][y_2]==9:
        result='yes'
        return
    for k in range(4):
        tx_1,ty_1,tx_2,ty_2 = x_1+dic[k][0],y_1+dic[k][1],x_2+dic[k][0],y_2+dic[k][1]
        if 0<=tx_1<n and 0<=ty_1<n and 0<=tx_2<n and 0<=ty_2<n and mtr[tx_1][ty_1]!=1 and mtr[tx_2][ty_2]!=1 and not (vis[tx_1][ty_1] and vis[tx_2][ty_2]):
            dfs(tx_1,ty_1,tx_2,ty_2)

dic=[[0,1],[0,-1],[1,0],[-1,0]]

n=int(input())
mtr=[]
start=[]
for i in range(n):
    arr=list(map(int,input().split()))
    try:
        a,b=i,arr.index(5)
        start.append(a)
        start.append(b)
        arr[b]=0
    except ValueError:
        pass
    try:
        a,b=i,arr.index(5)
        start.append(a)
        start.append(b)
        arr[b]=0
    except ValueError:
        pass
    mtr.append(arr)
vis=[[False]*n for i in range(n)]
x_1,y_1,x_2,y_2=start[0],start[1],start[2],start[3]
dfs(x_1,y_1,x_2,y_2)
print(result)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-20 00.00.51</u>](https://p.ipic.vip/axy6o6.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：

1h。

一开始看到是dp想着和之前做过的题应该没有什么联系，但是越想越发现，有很多很多的漏洞dp没有办法完全弥补。于是又回到了最开始的思路，尝试和之前做过的那道题找联系，就先尝试按照之前的排序方法进行排序。这样排序之后，我们能确保的事情是：一定要尽量把排在前面的数放在最终答案靠前的位置。比如第二个数，第三个数，第四个数可以组成答案，第二个数，第四个数，第三个数也可以组成答案，那么我们要取234；第二个数，第三个数，第四个数可以组成答案，第一个数，第二个数，第三个数也可以组成答案，那么我们要取123。

由此再来看dp就发现之前的漏洞都没有了。对最多j位的情形，我们可以选择是否使用当前数列中的第i一个数，如果不使用这个数，那么就和前i-1个数的情形一样。如果使用的这个数之后，剩下的j-len(number)位在前i-1个数中没有解，那么要么是前i-1个数的解，要么就是单独这个数。如果有解，根据排序，这时候一定要把当前这个数放在最后面才最优，然后和前i-1个数的解取最大值。

代码：

```python
m=int(input())
n=int(input())
arr=list(map(str,input().split()))
arr.sort(key=lambda x:int(x)/(10**len(x)-1),reverse=True)
dp=[0]*(m+1)
for number in arr:
    for j in range(m,len(number)-1,-1):
        if dp[j-len(number)]==0:
            dp[j]=max(dp[j],int(number))
        else:
            dp[j]=max(dp[j],int(str(dp[j-len(number)])+number))
print(max(dp))
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-20 17.38.31</u>](https://p.ipic.vip/ztrigv.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：

2h。好难的题

前面一直在想暴力破解，后来发现得超时。于是思考怎么利用提示，怎么剪枝。其实最后也不算是剪枝。还是从答案倒着想

后来又一直debug。实在不会去看了题解，发现是浅拷贝和深拷贝的问题，之前从来没有遇到过类似的问题。因为之前等号右边貌似都是一个不可变量（如int），这次等号右边大多数时候都是列表，是一个可变量。因此如果右边是一个可变量的话，就要注意这个问题了。

代码：

```python
#小加强版，允许自由设置行数和列数。并且在遇到多解的问题时会算出所有的解。其实还可以再优化，算行和算列是等价的，因此应该算行数和列数中小的那一个，枚举情况数为2**min(m,n)
import copy
result=[]
def dfs(tmp,k):
    global result
    if k==n:
        act=[tmp]+[[0]*n for _ in range(m-1)]
        if calculate(act):
            result.append(copy.deepcopy(act))
        return
    else:
        for i in range(2):
            tmp.append(i)
            dfs(tmp,k+1)
            tmp.pop()

def calculate(act):
    ext=copy.deepcopy(mtr)
    for j in range(n):
        open_light(0,j,act,ext)
    for i in range(m-1):
        act[i+1]=copy.deepcopy(ext[i])
        for j in range(n):
            open_light(i+1,j,act,ext)
    if check(ext):
        return True
    else:
        return False

def check(ext):
    for i in range(m):
        for j in range(n):
            if ext[i][j]==1:
                return False
    return True

def open_light(x,y,act,ext):
    if act[x][y]==1:
        ext[x][y]=abs(ext[x][y]-1)
        for i in range(4):
            tx,ty=x+dic[i][0],y+dic[i][1]
            if 0<=tx<m and 0<=ty<n:
                ext[tx][ty] = abs(ext[tx][ty] - 1)

dic=[[0,1],[0,-1],[1,0],[-1,0]]
m,n=5,6
mtr=[list(map(int,input().split())) for _ in range(m)]

dfs([],0)

for _ in range(len(result)):
    for i in range(len(result[_])):
        print(*result[_][i])
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-18 18.24.19</u>](https://p.ipic.vip/71aa4h.png)



### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：

1.5h 要是没有之前做过的那道题真的想不出来。

看到binary search就想到那道题。可惜已经忘记是怎么做的了，只好回去看了一眼，大概有了思路。只可惜当时就是看得题解，所以现在写依然非常不熟练。总体来说就是一个“试答案”的过程。其实这是非常反直觉的，因为我们日常生活中解决的几乎所有问题都是“求答案”，但这题偏偏要“试答案”。这也告诉我们在之后解决问题时可以走的两条路。值得注意的是，“试答案”要求答案一定是要有范围的。

check函数花费了大量时间，首先在于如何准确的把应该拿掉什么石头表述出来，这里我转化成了应该保留下来什么石头，但是依然非常难搞。最后用到了pre，维护当前留下来的最后一块石头的位置，才算比较清楚的解决了。这个题的另一个关键是它有终点，就是最后一块石头必须要留下来。我在一开始写的时候就已经意识到最后一块留下来的石头和终点之间的距离也需要被纳入考虑，于是写出`if cnt>=n-m and l-pre>=std ：`，但是WA，我在这里停了好久。终于想到漏洞：如果最后一块留下来的石头和终点之间的距离不满足条件，但是我当前留下的石头比最少需要保留的石头的个数，即n-m，多1，那么我可以选择把最后一块石头（终点前的一块）拿掉来符合要求。而这种情况在我之前的判断语句里会被判为不符合。于是加入`cnt>=n-m+1`，成功AC。

代码：

```python
def biq(x,y):
    if x==y:
        return x
    mid=(x+y)//2+1
    if check(mid):
        return biq(mid,y)
    else:
        return biq(x,mid-1)

def check(std):
    cnt=0
    pre=0
    for i in range(n):
        if arr[i]-pre>=std:
            cnt+=1
            pre=arr[i]
    if (cnt>=n-m and l-pre>=std) or cnt>=n-m+1 :
        return True
    else:
        return False

l,n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
print(biq(1,l))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-20 22.46.50</u>](https://p.ipic.vip/q6gy60.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

做的还行，没有出现完全没思路的题，大部分也都是自己写出来的，就是最后几题耗时太长了，不知道有什么好方法。快考试了，在保持每日选做的同时整理cheatsheet，主要是对各种经典算法要足够熟悉，对常用的语法要足够了解。



