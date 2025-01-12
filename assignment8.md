# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by 李冠黎 工学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：



代码：

```python
dic=[[0,1],[1,0],[0,-1],[-1,0]]
cnt=0

m,n=map(int,input().split())
maq=[[0]*(n+2) for _ in range(m+2)]
for _ in range(1,m+1):
    maq[_][1:-1]=list(map(int,input().split()))
for i in range(1,m+1):
    for j in range(1,n+1):
        if maq[i][j]==1:
            for _ in range(4):
                if maq[i+dic[_][0]][j+dic[_][1]]==0:
                    cnt+=1
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-12 17.47.56](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-12 17.47.56.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：



代码：

```python
n=int(input())
che=0
tik=1
o,p=1,n
mtr=[[0]*(n+1) for _ in range(n+1)]
while che!=tik:
    che=tik
    for j in range(o,n-o+1):
        mtr[o][j]=tik
        tik+=1
    for i in range(o,n-o+1):
        mtr[i][p]=tik
        tik+=1
    for j in range(n-o+1,o,-1):
        mtr[p][j]=tik
        tik+=1
    for i in range(n-o+1,o,-1):
        mtr[i][o]=tik
        tik+=1
    o+=1
    p-=1
if n%2!=0:
    mtr[n//2+1][n//2+1]=tik
for _ in range(1,n+1):
    print(*mtr[_][1:])
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-11-12 21.30.37](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-12 21.30.37.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
def boom(x,y,tx,ty):
    if abs(tx-x)<=d and abs(ty-y)<=d:
        return True
    else:
        return False

d=int(input())
n=int(input())
rub=[]
result=[]
for _ in range(n):
    rub.append(list(map(int,input().split())))

mav=0
for i in range(1025):
    for j in range(1025):
        tmp=0
        for w in range(n):
            if boom(i,j,rub[w][0],rub[w][1]):
                tmp+=rub[w][2]
        result.append(tmp)
        mav=max(mav,tmp)
print(result.count(mav),mav)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-13 15.35.19](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-13 15.35.19.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：



代码：

```python
n=int(input())
arr=list(map(int,input().split()))

# 分类讨论只有一个数的情况
if len(arr)==1:
    print(1)
    exit()
    
i=1
cnt=1
pre_dif=arr[1]-arr[0]
while i<n:
    cur_dif=arr[i]-arr[i-1]
    if cur_dif!=0 and pre_dif==0: # 及时更新pre_dif，使其不为0。因为0是不能判断后续单调性的改变的。
        pre_dif=cur_dif
    if cur_dif*pre_dif < 0: # 检测从上一个选出的可以加入摆动数列的数开始，接下来的序列是不是单调的。如果不是（局部单调性改变），则说明找到了下一个可以被选出的数，进入这个if判断
        cnt+=1
        pre_dif=cur_dif # 更新pre_dif代表现在的单调性
    i+=1
    
# 走到这里已经完成了前n-1个数的检索，只剩下末尾的一段单调序列（最短就是最后一项）我们没有选出数
if pre_dif!=0: # 此时只有常数列pre_dif=0。如果不是常数列，易验证末尾的一段单调序列中最后一个数（即最后一项）一定可以被选入，进入这个if判断
    cnt+=1
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-12 20.52.14](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-12 20.52.14.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：



代码：

```python
n=int(input())
arr=list(map(int,input().split()))
cnt=[0]*(10**5+1)
for i in range(n):
    cnt[arr[i]]+=1
dp=[0]*(10**5+2)
dp[1]=cnt[1]
for i in range(2,max(arr)+1):
    dp[i]=max(dp[i-1],dp[i-2]+cnt[i]*i)
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-13 15.44.14](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-13 15.44.14.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：

好难🤯。题解也看不懂……

代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这一周遇到的难题除了田忌赛马就是整数拆分，其他的基本还算顺利。题目真的是越来越难了，有时候看题解也得看好半天。感觉dp和recursion的掌握程度还可以，代码都可以写得正确，就是思路能不能想到的问题了。



