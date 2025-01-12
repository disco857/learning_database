# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by 李冠黎 工学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：

移动n个盘子的步骤是：

1.把n-1个盘子从A移到B

2.把最大的盘子，即第n个盘子从A移到C

3.把n-1个盘子从B移到C

如果我们已经有把n-1个盘子从A移到C的步骤，那么1就是把这些步骤中的B换为C，C换为B。3就是把这些步骤中的A换为B，B换为A。

代码：

```python
def step_number(x):
    if x==1:
        return 1
    else:
        return 2*step_number(x-1)+1

def step_order(x):
    if x==1:
        return ['A','C']
    else:
        bor={'B':'C','C':'B','A':'A'}
        byd={'A':'B','B':'A','C':'C'}
        return [bor[_] for _ in step_order(x-1)]+['A','C']+[byd[_] for _ in step_order(x-1)]

n=int(input())
result=step_order(n)
print(step_number(n))
for i in range(0,len(result),2):
    print(result[i]+'->'+result[i+1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-30 23.06.53](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-30 23.06.53.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：

没用回溯，自己写的。

以3为例。

123 132 一组，是把1放在最前面，然后把剩下的数，即23进行全排列放在后面。

213 231一组，同理，把2拿出来。

312 321一组，把3拿出来。

所以n的全排列就是依次把1到n拿出来，然后把剩下的数的全排列放在它的后面。

有递归，把格式改对花了大部分时间。

代码：

```python
def ara(arr):
    if len(arr) == 1:
        return [str(arr[0])+' ']
    else:
        result=[]
        for i in range(len(arr)):
             result.extend([str(arr[i])+' '+_ for _ in ara(arr[:i] + arr[i+1:])])
        return result

n=int(input())
ans=ara([x for x in range(1,n+1)])
for i in ans:
    print(i[:-1])
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-31 23.48.50](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-31 23.48.50.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：



代码：

```python
k=int(input())
dp=[0]*k
arr=list(map(int,input().split()))
dp[0]=1
for i in range(1,k):
    mav =0
    for j in range(i):
        if arr[j]>=arr[i]:
            mav=max(mav,dp[j])
    dp[i]=mav+1
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-30 10.00.18](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-30 10.00.18.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：



代码：

```python
N,B=map(int,input().split())
dp=[[0]*(B+1) for _ in range(N+1)]
pri=[0]+list(map(int,input().split()))
wei=[0]+list(map(int,input().split()))
for i in range(1,N+1):
    for j in range(1,B+1):
        if wei[i]<=j:
            dp[i][j]=max(dp[i-1][j],pri[i]+dp[i-1][j-wei[i]])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[N][B])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-29 23.49.37](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-29 23.49.37.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：

至尊brute force之力！！！

代码：

```python
def ara(arr): #全排列生成器
    if len(arr) == 1:
        return [str(arr[0])]
    else:
        result=[]
        for i in range(len(arr)):
             result.extend([str(arr[i])+_ for _ in ara(arr[:i] + arr[i+1:])])
        return result

def check(arr): #筛选器
    p=len(arr)
    for i in range(p):
        for j in range(1,p+1):
            if i-j<0 or int(arr[i])+j>p:
                break
            if int(arr[i-j])==(int(arr[i])+j):
                return False
        for j in range(1,p+1):
            if i+j>p-1 or int(arr[i])-j<1:
                break
            if int(arr[i+j])==(int(arr[i])-j):
                return False
        for j in range(1,p+1):
            if i-j<0 or int(arr[i])-j<1:
                break
            if int(arr[i-j])==(int(arr[i])-j):
                return False
        for j in range(1,p+1):
            if i+j>p-1 or int(arr[i])+j>p:
                break
            if int(arr[i+j])==int(arr[i])+j:
                return False
    return True

n=int(input())
ans=ara([x for x in range(1,n+1)])
uio=[] #整合在一个列表里输出
for pos in ans:
    if check(pos):
        uio.append(pos)
print(uio)

```



```python
ans=['15863724', '16837425', '17468253', '17582463', '24683175', '25713864', '25741863', '26174835', '26831475', '27368514', '27581463', '28613574', '31758246', '35281746', '35286471', '35714286', '35841726', '36258174', '36271485', '36275184', '36418572', '36428571', '36814752', '36815724', '36824175', '37285146', '37286415', '38471625', '41582736', '41586372', '42586137', '42736815', '42736851', '42751863', '42857136', '42861357', '46152837', '46827135', '46831752', '47185263', '47382516', '47526138', '47531682', '48136275', '48157263', '48531726', '51468273', '51842736', '51863724', '52468317', '52473861', '52617483', '52814736', '53168247', '53172864', '53847162', '57138642', '57142863', '57248136', '57263148', '57263184', '57413862', '58413627', '58417263', '61528374', '62713584', '62714853', '63175824', '63184275', '63185247', '63571428', '63581427', '63724815', '63728514', '63741825', '64158273', '64285713', '64713528', '64718253', '68241753', '71386425', '72418536', '72631485', '73168524', '73825164', '74258136', '74286135', '75316824', '82417536', '82531746', '83162574', '84136275']
t=int(input())
for _ in range(t):
    print(ans[int(input())-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-01 20.42.44](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-01 20.42.44.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：

看了题解才知道类比小偷背包。之前雷达安装也是，得看题解才能想起来进程检测。

这种包装不同、内核相同的题目的迁移能力需要提升。

代码：

```python
n,a,b,c=map(int,input().split())
dp=[[0]*(n+1) for _ in range(4)]
wei=[0,a,b,c]
pri=[0,1,1,1]
for i in range(1,4):
    for j in range(1,n+1):
        if wei[i]<=j:
            if dp[i][j-wei[i]]==0 and wei[i]!=j:
                dp[i][j]=max(dp[i-1][j],0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - wei[i]] + pri[i])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[3][n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-30 09.59.07](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-30 09.59.07.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

感觉dp题构造无后效性的状态是最难的。公共子序列是个特例，个人感觉状态转移方程不好想（不好证明其正确性）。

回溯算法基本理解，但是还是不能熟练写出。看了胡杨讲八皇后的视频，第一次知道函数后面的括号里可以塞一大堆东西，感觉还没完全理解（主要是和以往认知冲突，认为函数后面就是自变量）。

每日选做在跟进，简单的dp可以拿下（如漂亮区间），但是篮球练习依然失败了。



