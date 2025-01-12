# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>李冠黎 工学院</mark>



**说明：**

1）⽉考： AC<mark>1</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：

核心在只遍历一边就可以找到从任意位置开始往前的最小值

代码：

```python
arr=list(map(int,input().split()))
pre_min=[arr[0]]
for i in range(1,len(arr)):
    pre_min.append(min(pre_min[-1],arr[i]))
ans=0
for i in range(1,len(arr)):
    ans=max(arr[i]-pre_min[i-1],ans)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u><u>截屏2024-12-08 23.28.42</u></u>](https://p.ipic.vip/ryrcfc.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：

看到题目，就开始想5 1 1 2如果1 1一起炸时间就少了的原因。发现这里5很特殊，因为所有鸡排时间之和除以k比5小，说明5永远也炸不完，似乎应该把5一直放在锅里，而1 1没有这样做。顺着这个思路看第一个样例。没有特殊的鸡排，即没有炸不完的。我想到如果炸的时间尽可能长，那如果把所有鸡排都能炸完，那总时间就一定最长了，即所有鸡排时间之和除以k。验证1 1 1样例，的确如此。所以现在的问题是，如果没有特殊鸡排，是否一定能把所有鸡排炸完？

注意到鸡排可以无限分割，只要分的足够细，就可以很“平均”地炸，似乎就可以做到。但是没想到严格证明……



代码：

```python
n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
pre_sum=[arr[0]]
for i in range(1,n):
    pre_sum.append(arr[i]+pre_sum[i-1])

def cook():
    global k
    if arr[-1]>pre_sum[-1]/k:
        arr.pop()
        pre_sum.pop()
        k-=1
        return cook()
    else:
        return pre_sum[-1]/k

print("%.3f" % cook())
```



代码运行截图 ==（至少包含有"Accepted"）==

![<u>截屏2024-12-08 23.21.03</u>](https://p.ipic.vip/kysi4k.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：

双dp。dp[i]表示一定买下第i个物品。dpa是不放回，dpb是放回

代码：

```python
arr=list(map(int,input().split(',')))
n=len(arr)
dpa=[0]*n
dpb=[0]*n
dpb[0]=arr[0]
for i in range(1,n):
    dpb[i]=max(dpb[i-1]+arr[i],arr[i])
dpa[0]=arr[0]
for i in range(1,n):
    if i!=1:
        dpa[i]=max(dpb[i-2]+arr[i],dpa[i-1]+arr[i],arr[i])
    else:
        dpa[i]=max(arr[i],dpa[i-1]+arr[i])
print(max(max(dpa),max(dpb)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u><u>截屏2024-12-06 14.52.03</u></u>](https://p.ipic.vip/n9r87e.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：



代码：

```python
def dfs(buy,k):
    global cur_mey
    if len(buy)==n:
        re=[0]*m
        mey=0
        for i in range(len(buy)):
            re[buy[i]]+=pri[i][buy[i]]
            mey+=pri[i][buy[i]]
        r=mey//300
        mey-=50*r
        for i in range(len(re)):
            mav=0
            for j in range(len(save[i])):
                o=save[i][j].find('-')
                if int(save[i][j][:o])<=re[i]:
                    mav=max(int(save[i][j][o+1:]),mav)
            mey-=mav
        cur_mey=min(cur_mey,mey)
        return
    else:
        for i in range(len(pri[k])):
            if pri[k][i]!=-1:
                buy.append(i)
                dfs(buy,k+1)
                buy.pop()

n,m=map(int,input().split())
pri=[]
for _ in range(n):
    re=[]
    now=list(map(str,input().split()))
    tic=0
    i=0
    while i<len(now):
        if int(now[i][0])-1==tic:
            re.append(int(now[i][2:]))
            tic+=1
            i+=1
        else:
            re.append(-1)
            tic+=1
    while len(re)<m:
        re.append(-1)
    pri.append(re)

save=[]
for _ in range(m):
    save.append(list(map(str,input().split())))
cur_mey=float('inf')
dfs([],0)
print(cur_mey)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u><u>截屏2024-12-09 10.43.17</u></u>](https://p.ipic.vip/4808j7.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：

两个bfs。第一个bfs吞掉一个岛，并把所有它周围能建立长度为1的桥的坐标写入kick中作为初始条件。第二个bfs由初始坐标一步步造桥，直到碰到另一个岛。

代码：

```python
def bfs(x,y):
    global key
    key=False
    mtr[x][y]='-1'
    for i in range(4):
        tx=x+dic[i][0]
        ty=y+dic[i][1]
        if check(tx,ty):
            if mtr[tx][ty]=='0':
                kick.append((tx,ty))
            elif mtr[tx][ty]=='1':
                bfs(tx,ty)

dic=[[-1,0],[1,0],[0,-1],[0,1]]
def check(x,y):
    if 0<=x<m and 0<=y<n:
        return True
    else:
        return False

kick=[]

m=int(input())
mtr=[]
for _ in range(m):
    mtr.append(list(input()))
n=len(mtr[0])
key=True
for i in range(m):
    for j in range(n):
        if mtr[i][j]=='1' and key:
            bfs(i,j)
cnt=1
vis=[[False]*n for _ in range(m)]
for _ in range(len(kick)):
    a,b=kick[_]
    vis[a][b]=True
def pfs():
    global cnt
    while kick:
        tmp=len(kick)
        for _ in range(tmp):
            x,y=kick.pop(0)
            if mtr[x][y]=='1':
                cnt-=1
                return
            for i in range(4):
                tx = x + dic[i][0]
                ty = y + dic[i][1]
                if check(tx, ty) and mtr[tx][ty]!='-1' and vis[tx][ty]==False:
                    kick.append((tx,ty))
                    vis[tx][ty]=True
        cnt+=1
pfs()
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u><u>截屏2024-12-06 14.49.41</u></u>](https://p.ipic.vip/kmjjad.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：

看题解了。最关键的在于把自己前面的人左手上的数的乘积除以自己右手上的数变形为前面的人左手上的数的乘积乘自己左手上的数除以自己左右手的数的乘积。由此greedy就不难想了。

代码：

```python
n=int(input())
a,b=map(int,input().split())
crew=[]
for _ in range(n):
    x,y=map(int,input().split())
    crew.append([x,y,x*y])
crew.sort(key=lambda x: x[2])
crew.insert(0,[a,b,a*b])
cnt=0
mit=crew[0][0]
for i in range(1,len(crew)):
    cnt=max(mit//crew[i][1],cnt)
    mit*=crew[i][0]
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-08 23.24.14</u>](https://p.ipic.vip/twdult.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

月考难度大，个人认为岛屿建桥最简单，也是唯一一道在考场上做出来的题。决战双十一次之，因为在细节上想的太复杂，导致debug用了一些时间，考试结束5分钟后AC。感觉bfs dfs还是最好做的题，不用怎么想，看到就能写，但是一定要保证熟练度，代码不能错。

至于greedy，不想说了，一个赛着一个难……第一题考场上想了20分钟没思路，最后还得看题解，个人认为难度和国王游戏不相上下，全场最难。国王游戏也得看题解。炸鸡排算是自己想出来了，花了不少时间。greedy这种东西想出来才能写，而想出来又是一个有运气成分的过程，并不一定今天的greedy会明天的greedy也就会。想不出来只能放弃。

至于土豪购物确实可惜。一眼就看到了dp，渐渐想到了双dp。但是好紧张，加上不够自信，没写出来状态转移方程。不要先做，除非一眼看穿了，不然先做bfs来点自信。

看来还得练……每日选做都是bfs，得练熟练度，争取不管什么题25min拿下。greedy尽量做吧，上leetcode，能会多少会多少，已经不抱希望了……

