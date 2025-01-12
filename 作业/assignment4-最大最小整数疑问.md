# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by 李冠黎 工学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：



代码

```python
n,m=map(int,input().split())
tv=list(map(int,input().split()))
tv.sort()
suv=0
for i in range(n):
    if i>=m or tv[i]>0:
        print(-suv)
        exit()
    suv=suv+tv[i]
print(-suv)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-18 22.49.19](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-18 22.49.19.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：



代码

```python
n=int(input())
coi=list(map(int,input().split()))
coi.sort(reverse=True)
suv=[0]*n
suv[0]=coi[0]
for i in range(1,n):
    suv[i]=suv[i-1]+coi[i]
a=suv[-1]/2
for i in range(n):
    if suv[i]>a:
        print(i+1)
        break
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-18 00.03.25](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-18 00.03.25.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：

其实就是每列都要有或者每行都要有。

代码

```python
t=int(input())
for _ in range(t):
    n=int(input())
    row=list(map(int,input().split()))
    col=list(map(int,input().split()))
    a=sum(row)+min(col)*n
    b=sum(col)+min(row)*n
    print(min(a,b))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-17 23.52.17](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-17 23.52.17.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：



代码

```python
import math
n=int(input())
grp=list(map(int,input().split()))
sup=0
a,b,c=0,0,0
for i in range(n):
    if grp[i]==4:
        sup+=1
    elif grp[i]==3:
        c+=1
    elif grp[i]==2:
        b+=1
    elif grp[i]==1:
        a+=1

if b%2==0:
    sup+= b//2+min(a,c)
    if a<c:
        sup+=c-a
    elif a>c:
        sup+=math.ceil((a-c)/4)
elif b%2!=0:
    sup+=math.ceil(b/2)+min(a,c)
    if a<c:
        sup+=c-a
    elif a>c:
        a=a-c
        if a>2:
            sup+=math.ceil((a-2)/4)
print(sup)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-17 23.30.46](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-17 23.30.46.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：

欧拉筛宣传片。

代码

```python
import math

isprime=[True]*(10**6+1)
isprime[1]=False
isprime[0]=False
primes=[]
for i in range(2,10**6+1):
    if isprime[i]:
        primes.append(i)
    for prime in primes:
        if i*prime>=10**6+1:
            break
        isprime[i*prime]=False
        if i%prime==0:
            break

useless=int(input())
numbers=[int(x) for x in input().split()]

for number in numbers:
    root=int(math.sqrt(number))
    if isprime[root] and number==root**2:
        print('YES')
    else:
        print('NO')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-16 23.18.08](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-16 23.18.08.png)



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：

开始时想如何比较能认为898比8987大，这样898就可以放在前面。发现8987之所以要放在后面，是因为最后一个7比898的第一个8小，如果用这两个数拼成一个七位数，那么从左往右的第四位数肯定要放8而不能放7。同理如果是89886和898比，应该是89886除了前面相同的三位，剩下的86比898前两位89小，因此89886就小。而8989这种就比898大。

可以看出如果a的前几位就是另一个数b，那么就从那一位开始截断，把a从那一位开始后面的数和b比较。或者反过来，把b不断循环补充位数，直到和a的位数相同，再比较。即把898补充成8988，8988比8987大，因此898比8987大。

但是如果只补充到与a的位数相同是有问题的。考虑a=33353，b=3335，把b放在a前面形成的数更大，即在比较中b应该比a大。但是如果把b补充一位变成33353，就和a一样，比不出来。因此，补充位数必须要补充到能比出大小为止。在这个例子中，应该补充到a的位数+3，33353333和33353335，可得b比a大。

再举一些例子观察，会发现如果b前几位是相同的，那么要补充的位数就比较多，最多需要补充到（a的位数+b前几位相同的位数）。索性直接补充到a的位数+b的位数。又考虑到我们的程序只获取了最大位数，即a的位数。索性直接补充到a的位数+a的位数。即mav*=2.

（看了题解才想到要×2，之前WA，以上是自己的理解，不知道对不对）

代码

```python
n=int(input())
num=list(map(str,input().split()))
mav=len(num[0])
for i in range(1,n):
    mav=max(mav,len(num[i]))

mav*=2

new=[]
for i in range(n):
    lth=len(num[i])
    k=0
    a=num[i]
    while len(a)<mav:
        a=a+num[i][k%lth]
        k+=1
    new.append([num[i],a])

new.sort(key=lambda x: x[1],reverse=True)
fir=[sub[0] for sub in new]
print(''.join(map(str,fir)),end=' ')
fir.reverse()
print(''.join(map(str,fir)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-18 19.26.34](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-18 19.26.34.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这几天比较忙，每日选做只能跟上一道。之后还是要尽量都完成。

初步掌握了greedy，个人认为本质是局部最优+递归。矩阵的内容不是很难。课件里还有数据类型的内容没有看完。以及有时候一个题会有很多个题解，要静下心来，每一个都研究透还是需要花不少时间的。这部分的时间支出也需要和每日选做部分的时间支出进行一些平衡。

每日选做是在加强已有知识的熟练度，但是看题解很有可能收获到新的方法。目前的想法是每日选做至少完成一道比较难的，剩下的一道用来和看题解做取舍。

