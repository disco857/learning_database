# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by 李冠黎 工学院



**说明：**

1）⽉考： AC3 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：



代码：

```python
n=int(input())
arr=[]
arr_p=[]
for _ in range(n):
    a,b=map(str,input().split())
    b=int(b)
    if b>=60:
        arr.append([a,b,_])
    else:
        arr_p.append([a,b,_])
arr.sort(key=lambda x:(-x[1],x[2]))
# print(arr)
for _ in range(len(arr)):
    print(arr[_][0])
for _ in range(len(arr_p)):
    print(arr_p[_][0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-08 19.39.24](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-08 19.39.24.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：



代码：

```python
n,x,y=map(int,input().split())
mtr_a=[[0]*n for _ in range(n)]
mtr_b=[[0]*n for _ in range(n)]
for _ in range(x):
    a,b,c=map(int,input().split())
    mtr_a[a][b]=c
for _ in range(y):
    a,b,c=map(int,input().split())
    mtr_b[a][b]=c
for i in range(n):
    for j in range(n):
        k=0
        for _ in range(n):
            k+=mtr_a[i][_]*mtr_b[_][j]
        if k!=0:
            print(i,j,k)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-11-08 19.38.40](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-08 19.38.40.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：



代码：

```python
o=int(input())
for _ in range(o):
    n,m,b=map(int,input().split())
    skl=[]
    for _ in range(n):
        t,x=map(int,input().split())
        skl.append([t,x])
    skl.sort(key=lambda x:(x[0],-x[1]))
    u=skl[0][0]
    k=0
    y=True
    for i in range(n):
        if skl[i][0]!=u:
            k=0
            u=skl[i][0]
        if k<m:
            b-=skl[i][1]
            k+=1
            if b<=0:
                print(skl[i][0])
                y=False
                break
    if y:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-08 19.38.23](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-08 19.38.23.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：

必须使用滚动dp优化，否则MLE

代码：

```python
n,m=map(int,input().split())
arr=list(map(int,input().split()))
dp=[0]+[float('inf')]*m
for j in range(n):
    for i in range(arr[j],m+1):
        dp[i]=min(dp[i-arr[j]]+1,dp[i])
if dp[-1]>10*10000:
    print(-1)
else:
    print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-08 19.37.03](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-08 19.37.03.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：



代码：

```python
ans={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90,'thousand':1000,'million':10**6,'hundred':100}
num=list(map(str,input().split()))
o=1
if num[0]=='negative':
    o=-1
    del num[0]

cnt=0
re=0
for i in range(len(num)):
    if num[i]=='thousand' or num[i]=='million':
        re+=cnt*ans[num[i]]
        cnt=0
        continue
    if num[i]=='hundred':
        cnt*=100
    else:
        cnt+=ans[num[i]]
print(o*(cnt+re))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-08 19.36.18](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-08 19.36.18.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：



代码：

```python
n=int(input())
act=[]
for _ in range(n):
    a,b=map(int,input().split())
    act.append([a,b])
act.sort()
dp=[0]*n
dp[0]=1
for i in range(1,n):
    mav=0
    for j in range(i):
        if act[j][1]<act[i][0]:
            mav=max(mav,dp[j])
    dp[i]=mav+1
print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-08 19.35.55](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-11-08 19.35.55.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

机考炸裂。第一题就改了好几遍，最后才想到一个sort就搞定。不会一维dp导致第四题做了40多分钟没做出来。第五题想的太复杂，一直纠结怎么用thousand、million给输入切片，然后还要一个一个切片分别计算。不曾想到直接一个一个单词看就行了，遇到thousand、million就把计算的结果乘以相应的倍数加上去。第六题考场上一看N=10000以为正常dp肯定超时了没敢做。下来没想到其他方法，本着只能试试的想法很快写了一个正常dp直接ac了？？？！！！

总结下来就是模版题没拿到手，做每日选做的方法得改改。以后得接受看题解，光靠自己想效率太低了。还有就是考场上一定冷静！！！相信题目不会太复杂。机房的电脑用着不太顺手，得想办法适应，或许下次提前一点过去敲几下（？）

