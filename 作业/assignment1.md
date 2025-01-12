# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==李冠黎 工学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：

题目直接翻译，三个不是闰年的条件满足其一（or），即可判定不是。

##### 代码

```python
year=int(input())
if year%4!=0 or (year%100==0 and year%400!=0) or year%3200==0:
    print('N')
else:
    print('Y')
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-09-20 15.59.48](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-09-20 15.59.48.png)



### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：

先判断是不是有解：鸡2兔4，可见脚一定是偶数

动物最少就是兔尽量多，但如果脚数不能被4整除即不能全是兔，则必有一只鸡。例如22，最少是5兔1鸡。除以4向上取整可以解决。

动物最多全是鸡。

##### 代码

```python
feet=int(input())
if feet%2==0:
    print(-(-feet//4),end=' ')
    print(feet//2)
else:
    print('0 0')
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-09-20 16.09.18](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-09-20 16.09.18.png)



### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：

如果至少有一边长度是偶数，那么可以铺满（平行于偶数边铺）

如果两边m n都是奇数，那么(m-1)*(n-1)区域一定可以铺满，剩下一行一列铺。只有交叉格铺不到。因此总铺面积为 m*n-1

##### 代码

```python
str=input()
size=str.split()
s=int(size[0])*int(size[1])
print(s//2)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-20 16.13.34](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-09-20 16.13.34.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：

要求必须覆盖，长和宽均向上取整即可。

##### 代码

```python
n, m, a=map(int, input().split())
print((-n//a)*(-m//a))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-20 16.21.55](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-09-20 16.21.55.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：

直接比较字符串

##### 代码

```python
a=input().lower()
b=input().lower()
if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-20 17.16.56](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-09-20 17.16.56.png)



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：

直接翻译，检测三个数的和是不是大于等于2.

##### 代码

```python
x=input()
x=int(x)
number=0
for 傻逼 in range(1,x+1):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if a+b+c>1:
        number=1+number
    else:
        number=number
print(number)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-24 15.41.32](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-09-24 15.41.32.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

做了24fall每日选做的一些题。在这段时间中学习了很多能使代码简洁的写法，比如map( ), [int(x) for x in input.split( )]等。



