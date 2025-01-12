# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==李冠黎 工学院==



**说明：**

1）Oct⽉考： AC6==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：

通过ASCII码实现位移。

代码

```python
k = int(input())
s = input()
k=k%26
result=[]
for i in range(len(s)):
    a=ord(s[i])
    if 65<=a<=90:
        if a-k<65:
            a= a-k+26
        else:
            a-=k
        result.append(chr(a))
    else:
        if a-k<97:
            a= a-k+26
        else:
            a-=k
        result.append(chr(a))
print(''.join(result))
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-12 11.53.37](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-12 11.53.37.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：



代码

```python
a,b=map(str,input().split())
print(int(a[:2])+int(b[:2]))
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-12 11.54.06](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-12 11.54.06.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：

直接翻译。不过最后一位字符和数字不是相等地对应的，得找出通项公式，有点恶心。

代码

```python
n=int(input())
for i in range(n):
    number=input()
    if number[17]!='X':
        if (7*int(number[0])+9*int(number[1])+10*int(number[2])+5*int(number[3])+8*int(number[4])+4*int(number[5])+2*int(number[6])+1*int(number[7])+6*int(number[8])+3*int(number[9])+7*int(number[10])+9*int(number[11])+10*int(number[12])+5*int(number[13])+8*int(number[14])+4*int(number[15])+2*int(number[16])) % 11 == (-int(number[17])+12)%11:
            print('YES')
        else:
            print('NO')
    else:
        if (7*int(number[0])+9*int(number[1])+10*int(number[2])+5*int(number[3])+8*int(number[4])+4*int(number[5])+2*int(number[6])+1*int(number[7])+6*int(number[8])+3*int(number[9])+7*int(number[10])+9*int(number[11])+10*int(number[12])+5*int(number[13])+8*int(number[14])+4*int(number[15])+2*int(number[16]))% 11 == 2:
            print('YES')
        else:
            print('NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-12 11.54.37](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-12 11.54.37.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：



代码

```python
n=int(input())
while n>1:
    if n%2==0:
        b=int(n/2)
        print(str(n)+'/2='+str(b))
        n=b
    else:
        b=3*n+1
        print(str(n)+'*3+1='+str(b))
        n=b
print('End')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-12 11.56.03](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-12 11.56.03.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：

不会字典，成功拉出屎山代码。

##### 代码

```python
num=input()
fq = [str(x) for x in range(10)]
evil =['IV','IX',"XL",'XC','CD','CM']
result=[]
if num[0] in fq:
    num = int(num)
    if num==4:
        print('IV')
    elif num==9:
        print('IX')
    elif num==40:
        print('XL')
    elif num==90:
        print('XC')
    elif num==400:
        print('CD')
    elif num==900:
        print('CM')
    else:
        m= num//1000
        num-=(num//1000)*1000
        result.append(m*'M')
        if num>=900:
            result.append('CM')
            num-=900

        d = num // 500
        num -= (num // 500) * 500
        result.append(d * 'D')
        if num>=400:
            result.append('CD')
            num-=400

        c = num // 100
        num -= (num // 100) * 100
        result.append(c*'C')

        if num >= 90:
            result.append('XC')
            num -= 90
        l = num // 50
        num -= (num // 50) * 50
        result.append(l * 'L')

        if num >= 40:
            result.append('XL')
            num -= 40

        x = num // 10
        num -= (num // 10) * 10
        result.append(x*'X')
        if num >= 9:
            result.append('IX')
            num -= 9
        v = num // 5
        num -= (num // 5) * 5
        result.append(v*'V')
        if num >= 4:
            result.append('IV')
            num -= 4

        i = num
        result.append(i*'I')
        print(''.join(result))
else:
    i=0
    while i<=len(num)-1:
        if i<=len(num)-2 and num[i:i+2] in evil:
            result.append(num[i:i+2])
            i+=2
        else:
            result.append(num[i])
            i+=1
    cnt=0
    for _ in result:
        if _=='I':
            cnt+=1
        elif _=='V':
            cnt+=5
        elif _=='X':
            cnt+=10
        elif _=='L':
            cnt+=50
        elif _=='C':
            cnt+=100
        elif _=='D':
            cnt+=500
        elif _=='M':
            cnt+=1000
        elif _=='IV':
            cnt+=4
        elif _=='IX':
            cnt+=9
        elif _=='XL':
            cnt+=40
        elif _=='XC':
            cnt+=90
        elif _ == 'CD':
            cnt += 400
        elif _=='CM':
            cnt+=900
    print(cnt)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-12 11.57.38](/Users/liguanli/Library/Application Support/typora-user-images/截屏2024-10-12 11.57.38.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：



代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

感觉难度已经明显上升，每日选做在尽量跟上，但是每道题目都要花更多的时间。有时候也会出现因为粗心而导致一个小地方出错，需要花很长的时间来debug的情况，之后要多注意。先用草稿纸验算，思路清晰之后再写代码，避免出现的类似的问题。

目前对算法一无所知，排队的解析看了半天没看懂，会继续努力。









