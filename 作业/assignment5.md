# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by 李冠黎 工学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：

中国剩余定理

代码：

```python
cnt=1
while True:
    x,y,z,w=map(int,input().split())
    if {x,y,z,w}=={-1}:
        break
    M=(x*6*28*33+y*19*23*33+z*2*23*28)%(23*28*33)
    for i in range(5):
        if M+21252*i>w:
            print('Case '+str(cnt)+': the next triple peak occurs in '+str(M+21252*i-w)+' days.')
            break
    cnt+=1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-23 19.39.36](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-23 19.39.36.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：

上来只能买，买就买最便宜的，卖就卖最贵的。卖了一定能买。只剩一个不能卖。

代码：

```python
p=int(input())
wep=input().split()
wep=[int(x) for x in wep]
wep.sort()
a=0
b=0
while p>=wep[0]:
    while p>=wep[0]:
        p-=wep[0]
        a += 1
        wep.pop(0)
        if not wep:
            print(a - b)
            exit()
    if len(wep)>1:
        p+=wep[-1]
        b+=1
        wep.pop(-1)
print(a-b)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-23 19.41.10](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-23 19.41.10.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：

耗时少的先做。

代码：

```python
n=int(input())
kids=list(map(int,input().split()))
no=[]
for i ,kid in enumerate(kids):
    no.append([i,kid])
no.sort(key=lambda x: x[1])
p=[o[0]+1 for o in no]
print(*p)
u=[no[0][1]]
for i in range(1,n-1):
    u.append(no[i][1]+u[-1])
print("%.2f" % (sum(u)/n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-23 16.42.32](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-23 16.42.32.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：



代码：

```python
hmo={'pop':1,'no':2,'zip':3,'zotz':4,'tzec':5,'xul':6,'yoxkin':7,'mol':8,'chen':9,'yax':10,'zac':11,'ceh':12,'mac':13,'kankin':14,'muan':15,'pax':16,'koyab':17,'cumhu':18}
tmo={1:'imix',2:'ik', 3:'akbal', 4:'kan',5:'chicchan', 6:'cimi', 7:'manik', 8:'lamat', 9:'muluk', 10:'ok', 11:'chuen', 12:'eb', 13:'ben', 14:'ix', 15:'mem', 16:'cib', 17:'caban', 18:'eznab', 19:'canac', 0:'ahau'}
n=int(input())
print(n)
for _ in range(n):
    d,m,y=map(str,input().split())
    d=int(d[:-1])
    y=int(y)
    if m=='uayet':
        day=18*20+d+1+y*365
    else:
        day=(hmo[m]-1)*20+d+1+y*365
    print((day-1)%13+1,tmo[day%20],(day-1)//260)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-23 19.43.36](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-23 19.43.36.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

尝试给出证明：

假设从左到右之前已经倒了一些树。到了某一棵树，这棵树可以向左倒，那么它倒与否不会对后面树的情况产生影响。因为无论这棵树倒不倒，它对于后面树的阻碍点都是这个树的坐标位置，即后面的树不能够倒在这棵树的坐标位置左侧。那么假如有两种倒的情况，除了这棵树之外，其他的树的情况都完全相同，那么一定可以使这棵树向左倒来使得总的倒的个数增加1，即如果一棵树能够向左倒，那么让它向左倒‘一定是更优的方法。

如果这棵树不能向左倒，而能够向右倒，那么考察这棵树和其下一棵树。如果下一棵树在向左倒的情况下，这棵树依然能向右倒，那么这棵树是否向右倒不会影响接下来所有的树的情况。依照前面的逻辑，此时向右倒更优。如果下一棵树向左倒，这棵树就不能向右倒；这棵树向右倒，下一棵树就不能向左倒，那么将这两棵树做为整体来看，它们的倒的个数最多只能是1。而不论是哪种情况，对于后面所有树的阻碍点都是第二棵树的坐标位置，即不会影响后面所有树的情况。所以这两棵树的这两种情况是完全一样的，那么不妨就让第一棵树向右倒。综上，如果一棵树不能向左倒，而能够向右倒，那么就让它向右倒，一定最优。

代码：

```python
n=int(input())
tre=[]
for _ in range(n):
    a,b=map(int,input().split())
    tre.append([a,b])
tre.sort(key=lambda x: x[0])
if len(tre)==1:
    print(1)
else:
    now=tre[0][0]
    cnt=2
    for i in range(1,n-1):
        if tre[i][0]-tre[i][1]<=now and tre[i][0]+tre[i][1]<tre[i+1][0]:
            now=tre[i][0]+tre[i][1]
            cnt+=1
        elif tre[i][0]-tre[i][1]>now:
            now=tre[i][0]
            cnt+=1
        else:
            now=tre[i][0]
    print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-22 22.49.04](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-22 22.49.04.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

看了题解才知道本质和进程检测是一样的，真的不容易想到。一直都是想着直接用半径为d的圆覆盖，但这样实际上是没有局部最优方法的，或者说局部最优方法需要分类讨论的很细碎，greedy程序不好写。

代码：

```python
import math
fk=1
while True:
    n,d=map(int,input().split())
    if {n,d}=={0}:
        break
    isl=[]
    for _ in range(n):
        a,b=map(int,input().split())
        if b <= d:
            isl.append([a-math.sqrt(d**2-b**2),a+math.sqrt(d**2-b**2)])
    if len(isl)<n:
        print('Case '+str(fk)+': '+str(-1))
        fk+=1
        input()
        continue
    isl.sort(key=lambda x:x[0])
    cnt=1
    k=isl[0][1]
    for i in range(1,n):
        if isl[i][0]>k:
            cnt+=1
            k=isl[i][1]
        else:
            if isl[i][1]<=k:
                k=isl[i][1]
    print('Case '+str(fk)+': '+str(cnt))
    fk+=1
    input()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-23 19.44.19](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-23 19.44.19.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>



在跟每日选做。目前的题还是比较有挑战性的，平均花费时间在一个小时左右。但是基本上看到都会有思路，有的时候努力做一做是可以AC的，成就感比较大。实在不会做的也不会带着一片空白的大脑去看题解，个人认为是比较好的一种状态。

需要花很长时间来debug的一些小错误近来有所减少。一方面是归功于先在草稿纸上演算；另外一方面，即便题目不会做而看了题解也要有时间再把答案写一遍，这样能够提高语法的熟练度，关键是有时候还不一定能写对呢。
