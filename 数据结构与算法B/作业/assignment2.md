# Assignment #2: 深度学习与大语言模型

Updated 2204 GMT+8 Feb 25, 2025

2025 spring, Complied by <mark>李冠黎 工学院</mark>



**作业的各项评分细则及对应的得分**

| 标准                                 | 等级                                                         | 得分 |
| ------------------------------------ | ------------------------------------------------------------ | ---- |
| 按时提交                             | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分  | 1 分 |
| 源码、耗时（可选）、解题思路（可选） | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于2个：0分 | 1 分 |
| AC代码截图                           | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于：0分 | 1 分 |
| 清晰头像、PDF文件、MD/DOC附件        | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
| 学习总结和个人收获                   | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分 | 1 分 |
| 总得分： 5                           | 总分满分：5分                                                |      |
>
> 
>
> **说明：**
>
> 1. **解题与记录：**
>       - 对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>    
>2. **课程平台与提交安排：**
> 
>   - 我们的课程网站位于Canvas平台（https://pku.instructure.com ）。该平台将在第2周选课结束后正式启用。在平台启用前，请先完成作业并将作业妥善保存。待Canvas平台激活后，再上传你的作业。
> 
>       - 提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>3. **延迟提交：**
> 
>   - 如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
> 
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### 18161: 矩阵运算

matrices, http://cs101.openjudge.cn/practice/18161



思路：

顺便练习OOP，实现了一个矩阵类。考虑到欧拉范数和行和范数的等价性，且欧拉范数因为太多乘方和开方对性能和精度不友好，选择了实现行和范数。

感觉矩阵求行列式，求逆对我来说还是太复杂了，以后有机会再写。

另外之前看视频刷到过最近又有论文把做矩阵乘法需要的乘法次数进一步降低，没那个能力实现了，只使用了最基本的矩阵乘法。

代码：

```python
class Matrix:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.data=[[0 for _ in range(col)] for _ in range(row)]

    def set_value(self,row,col,val):
        self.data[row][col]=val

    def get_value(self,row,col):
        if 0<=row<self.row and 0<=col<self.col:
            return self.data[row][col]
        else:
            raise IndexError('The index of row or column is out of range')

    def __add__(self,other):
        if isinstance(other,Matrix):
            if self.row==other.row and self.col==other.col:
                result=Matrix(self.row,self.col)
                for i in range(self.row):
                    for j in range(self.col):
                        result.set_value(i,j,self.data[i][j]+other.data[i][j])
                return result
            else:
                raise ValueError('The two matrices cannot be added together')
        else:
            raise TypeError('Only two matrices can be added together')

    def __sub__(self,other):
        if isinstance(other,Matrix):
            if self.row==other.row and self.col==other.col:
                result = Matrix(self.row, self.col)
                for i in range(self.row):
                    for j in range(self.col):
                        result.set_value(i, j, self.data[i][j] - other.data[i][j])
                return result
            else:
                raise ValueError('The two matrices cannot be subtracted')
        else:
            raise TypeError('Only two matrices can be subtracted')

    def __mul__(self,other):
        if isinstance(other,Matrix):
            if self.col==other.row:
                p=self.col
                result=Matrix(self.row,other.col)
                for i in range(self.row):
                    for j in range(other.col):
                        tmp=0
                        for k in range(p):
                            tmp+=self.data[i][k]*other.data[k][j]
                        result.set_value(i,j,tmp)
                return result
            else:
                raise ValueError('The two matrices cannot be multiplied')
        else:
            raise TypeError('Only two matrices can be multiplied')

    def __str__(self):
        return '\n'.join(' '.join(map(str,row)) for row in self.data)

    def transpose(self):
        result=Matrix(self.col,self.row)
        for i in range(self.row):
            for j in range(self.col):
                result.set_value(j,i,self.data[i][j])
        return result

    def __lt__(self,other):
        return norm(self)<norm(other)

def norm(x):
    if isinstance(x,(int,float)):
        return abs(x)
    elif isinstance(x,Matrix):
        max_sum=0
        for i in range(x.row):
            tmp=0
            for j in range(x.col):
                tmp+=abs(x.data[i][j])
            max_sum=max(max_sum,tmp)
        return max_sum
    else:
        raise TypeError('Unsupported type for norm calculation')


r,c=map(int,input().split())
A=Matrix(r,c)
for i in range(r):
    col=list(map(int,input().split()))
    for j in range(c):
        A.set_value(i,j,col[j])

r,c=map(int,input().split())
B=Matrix(r,c)
for i in range(r):
    col=list(map(int,input().split()))
    for j in range(c):
        B.set_value(i,j,col[j])

r,c=map(int,input().split())
C=Matrix(r,c)
for i in range(r):
    col=list(map(int,input().split()))
    for j in range(c):
        C.set_value(i,j,col[j])

try:
    print(A*B+C)
except ValueError:
    print('Error!')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-08 17.49.23](https://p.ipic.vip/3dgdia.png)



### 19942: 二维矩阵上的卷积运算

matrices, http://cs101.openjudge.cn/practice/19942/




思路：



代码：

```python
m,n,p,q=map(int,input().split())
A=[list(map(int,input().split())) for i in range(m)]
B=[list(map(int,input().split())) for i in range(p)]
result=[[0 for _ in range(n+1-q)] for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        tmp=0
        for x in range(p):
            for y in range(q):
                tmp+=B[x][y]*A[x+i][y+j]
        result[i][j]=tmp

for _ in range(len(result)):
    print(*result[_])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-08 18.11.12](https://p.ipic.vip/sz12iv.png)



### 04140: 方程求解

牛顿迭代法，http://cs101.openjudge.cn/practice/04140/

请用<mark>牛顿迭代法</mark>实现。

因为大语言模型的训练过程中涉及到了梯度下降（或其变种，如SGD、Adam等），用于优化模型参数以最小化损失函数。两种方法都是通过迭代的方式逐步接近最优解。每一次迭代都基于当前点的局部信息调整参数，试图找到一个比当前点更优的新点。理解牛顿迭代法有助于深入理解基于梯度的优化算法的工作原理，特别是它们如何利用导数信息进行决策。

> **牛顿迭代法**
>
> - **目的**：主要用于寻找一个函数 $f(x)$ 的根，即找到满足 $f(x)=0$ 的 $x$ 值。不过，通过适当变换目标函数，它也可以用于寻找函数的极值。
> - **方法基础**：利用泰勒级数的一阶和二阶项来近似目标函数，在每次迭代中使用目标函数及其导数的信息来计算下一步的方向和步长。
> - **迭代公式**：$ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} $ 对于求极值问题，这可以转化为$ x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} $，这里 $f'(x)$ 和 $f''(x)$ 分别是目标函数的一阶导数和二阶导数。
> - **特点**：牛顿法通常具有更快的收敛速度（尤其是对于二次可微函数），但是需要计算目标函数的二阶导数（Hessian矩阵在多维情况下），并且对初始点的选择较为敏感。
>
> **梯度下降法**
>
> - **目的**：直接用于寻找函数的最小值（也可以通过取负寻找最大值），尤其在机器学习领域应用广泛。
> - **方法基础**：仅依赖于目标函数的一阶导数信息（即梯度），沿着梯度的反方向移动以达到减少函数值的目的。
> - **迭代公式**：$ x_{n+1} = x_n - \alpha \cdot \nabla f(x_n) $ 这里 $\alpha$ 是学习率，$\nabla f(x_n)$ 表示目标函数在 $x_n$ 点的梯度。
> - **特点**：梯度下降不需要计算复杂的二阶导数，因此在高维空间中相对容易实现。然而，它的收敛速度通常较慢，特别是当目标函数的等高线呈现出椭圆而非圆形时（即存在条件数大的情况）。
>
> **相同与不同**
>
> - **相同点**：两者都可用于优化问题，试图找到函数的极小值点；都需要目标函数至少一阶可导。
> - **不同点**：
>   - 牛顿法使用了更多的局部信息（即二阶导数），因此理论上收敛速度更快，但在实际应用中可能会遇到计算成本高、难以处理大规模数据集等问题。
>   - 梯度下降则更为简单，易于实现，特别是在高维空间中，但由于只使用了一阶导数信息，其收敛速度可能较慢，尤其是在接近极值点时。
>



代码：

```python
import re
def root_finder(start,time):
    x_0=start
    y_0=function(start)
    k=derivative(start)
    if k==0:
        return None
    output= -y_0/k+x_0
    if abs(output-start)<10**-9 or time>=100:
        return output
    else:
        return root_finder(output,time+1)

def function(x):
    return x**3-5*x**2+10*x-80

def derivative(x):
    return 3*x**2-10*x+10

# ans=[]
# for i in range(-10,10):
#     ans.append(root_finder(i,0))
# print(ans)

print('%.9f'%root_finder(10,0))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-11 17.55.28](https://p.ipic.vip/yfop9y.png)



### 06640: 倒排索引

data structures, http://cs101.openjudge.cn/practice/06640/



思路：



代码：

```python
from collections import defaultdict
n=int(input())
check=defaultdict(set)
for t in range(1,n+1):
    token=list(map(str,input().split()))
    for _ in range(1,int(token[0])+1):
        check[token[_]].add(t)
m=int(input())
for _ in range(m):
    word=input()
    if word in check:
        print(*sorted(check[word]))
    else:
        print('NOT FOUND')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-08 18.39.07](https://p.ipic.vip/dj0jfu.png)



### 04093: 倒排索引查询

data structures, http://cs101.openjudge.cn/practice/04093/



思路：



代码：

```python
n=int(input())
check={}
all_docu=set()
for i in range(n):
    index_list=input().split()
    check[i]=set(map(int,index_list[1:]))
    all_docu=all_docu|check[i]
m=int(input())
for _ in range(m):
    token=input().split()
    result=all_docu
    for i in range(n):
        if token[i]=='1':
            result=result.intersection(check[i])
        elif token[i]=='-1':
            result=result.difference(check[i])
    if result:
        print(*sorted(result))
    else:
        print('NOT FOUND')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-08 18.33.07](https://p.ipic.vip/o8zn4c.png)



### Q6. Neural Network实现鸢尾花卉数据分类

在http://clab.pku.edu.cn 云端虚拟机，用Neural Network实现鸢尾花卉数据分类。

参考链接，https://github.com/GMyhf/2025spring-cs201/blob/main/LLM/iris_neural_network.md

![截屏2025-03-11 23.44.02](https://p.ipic.vip/wz0ydb.png)

好难

目前只实现了anaconda的安装

## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

数算太难了！！！



