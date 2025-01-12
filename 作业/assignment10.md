# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>李冠黎 工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：



代码：

```python
n=int(input())
dp=[0]*(n+1)
dp[0],dp[1]=1,1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-12-02 08.35.10</u>](https://p.ipic.vip/atpo5i.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：

每次可以跳1-N级其实大大简化了问题，就相当于随便跳，本质上就是把N级台阶分成若干份，那么直接“插板法”实现即可。N级台阶，有N-1个空，每个空都可以选择插或不插。

代码：

```python
n=int(input())
print(2**(n-1))
```



代码运行截图 ==（至少包含有"Accepted"）==

![<u>截屏2024-11-28 17.00.04</u>](https://p.ipic.vip/ezfepb.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：

dp容易想到，难点在于要取模。老是取不对

代码：

```python
t,k=map(int,input().split())
dp=[1]*k+[0]*(10**5+1-k)
for i in range(k,10**5+1):
    dp[i]=(dp[i-k]+dp[i-1])%1000000007
pre_sum=[0]*(10**5+1)
pre_sum[0]=dp[0]
for i in range(1,10**5+1):
    pre_sum[i]=(pre_sum[i-1]+dp[i])%1000000007
for _ in range(t):
    a,b=map(int,input().split())
    print((pre_sum[b]-pre_sum[a-1])%1000000007)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u>截屏2024-11-28 16.57.01</u>](https://p.ipic.vip/pl1gvj.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：

没想到优化的方法，只好遍历了。

之后看了dp，双指针，马拉车，惊叹于马拉车的精妙，但实现逻辑有点复杂，自己写估计很大概率写不对。

代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(string):
            if string==string[::-1]:
                return True
            else:
                return False
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                if check(s[j:j+i]):
                    return s[j:j+i]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![<u><u>截屏2024-12-02 08.25.29</u></u>](https://p.ipic.vip/yrsq4w.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：

总共提交15次，太不容易了，总共耗时2h

前8次RE，对这种输入方式十分不熟练，后来发现不加`sys.setrecursionlimit(300000)`也会RE，希望老师可以讲一下这部分内容。

第9-11次MLE。写dfs从来没遇到MLE，后来慢慢意识到这里MLE就有点TLE的意味。因为dfs每次递归，函数都是要挂起的，这就会占内存，内存超了说明挂起的太多，说明有很多没有必要走的分支。由此想到了加一个记录水位高度的矩阵wat，如果之前水位已经到过更高的位置那么就不用再“淹”了。

第12-14次WA。主要是最后判断搞反了。写红温了。

代码：

```python
def dfs(x,y):
    wat[x][y]=std
    for i in range(4):
        tx=x+dic[i][0]
        ty=y+dic[i][1]
        if check(tx,ty):
            dfs(tx,ty)

def check(x,y):
    if 0<=x<m and 0<=y<n and mtr[x][y]<std and wat[x][y]<std:
        return True
    else:
        return False

dic=[[1,0],[0,1],[-1,0],[0,-1]]

result=[]
import sys
sys.setrecursionlimit(300000)

input=sys.stdin.read
data=input().split()
tic=0
k=int(data[tic])
tic+=1
for _ in range(k):

    m,n=map(int,data[tic:tic+2])
    tic+=2

    mtr=[]
    for _ in range(m):
        mtr.append(list(map(int,data[tic:tic+n])))
        tic+=n

    i,j=map(int,data[tic:tic+2])
    tic+=2
    i,j=i-1,j-1

    p=int(data[tic])
    tic+=1
    wat=[[-1]*n for _ in range(m)]
    for _ in range(p):
        q,r=map(int,data[tic:tic+2])
        tic+=2
        q,r=q-1,r-1

        std=mtr[q][r]
        if mtr[i][j]>std:
            continue

        dfs(q,r)

    if wat[i][j]!=-1:
        result.append('Yes')
    else:
        result.append('No')

print('\n'.join(result))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-26 20.30.37](https://p.ipic.vip/puvsnv.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：



代码：

```python
def bfs(x,y):
    queue=[(x,y)]
    seen.add((x,y))
    step=0
    while queue:
        cnt=len(queue)
        for _ in range(cnt):
            nx,ny=queue.pop(0)
            if nx==q and ny==p:
                return step
            for i in range(4):
                tx = nx + dic[i][0]
                ty = ny + dic[i][1]
                while check(tx,ty):
                    queue.append((tx,ty))
                    seen.add((tx,ty))
                    if tx==q and ty==p:
                        break
                    tx+=dic[i][0]
                    ty+=dic[i][1]
        step+=1
    return 0

def check(x,y):
    if 0<=x<=h+1 and 0<=y<=w+1 and (x,y) not in seen and (mtr[x][y]==' ' or( mtr[x][y]=='X' and x==q and y==p)):
        return True
    else:
        return False

dic=[[-1,0],[1,0],[0,-1],[0,1]]

tic=1
while True:
    w,h=map(int,input().split())
    if {w,h}=={0}:
        break
    mtr= [[' '] * (w + 2)]
    for _ in range(h):
        mtr.append([' ']+list(input())+[' '])
    mtr.append([' ']*(w+2))
    print('Board #'+str(tic)+':')
    tik=1
    while True:
        m,n,p,q=map(int,input().split())
        if {m,n,p,q}=={0}:
            break
        seen=set()
        result=bfs(n,m)
        if result==0:
            print('Pair '+str(tik)+': impossible.')
        else:
            print('Pair ' + str(tik) + ': '+str(result)+" segments.")
        tik+=1
    print()
    tic+=1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-26 19.07.19](https://p.ipic.vip/r70xtg.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

前面的4题都简单，感觉核电站是个很标准的模版题，很多题都可以借鉴。后边bfs和dfs的变体题就不是很简单了，得好好想一想，但还是万变不离其宗。有思路，难点是不写错。

每日选做一直在跟进，感觉良好，就是小精灵不会。



