# Assignment #7: 20250402 Mock Exam

Updated 1624 GMT+8 Apr 2, 2025

2025 spring, Complied by <mark>李冠黎 工学院</mark>



> **说明：**
>
> 1. **⽉考**：AC?<mark>2</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
> 2. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E05344:最后的最后

http://cs101.openjudge.cn/practice/05344/



思路：



代码：

```python
class ListNode:
    def __init__(self,val,nex=None,pre=None):
        self.val=val
        self.nex=nex
        self.pre=pre

    def __str__(self):
        return str(self.val)

n,k=map(int,input().split())
people=[ListNode(i+1) for i in range(n)]
for i in range(n-1):
    people[i].nex=people[i+1]
    people[i+1].pre=people[i]
people[-1].nex=people[0]
people[0].pre=people[-1]
result=[]
cur=people[-1]
while cur!=cur.nex:
    for _ in range(k):
        cur=cur.nex
    result.append(cur.val)
    cur.pre.nex,cur.nex.pre=cur.nex,cur.pre
print(*result[:-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-08 23.46.13](https://p.ipic.vip/kiz7db.png)



### M02774: 木材加工

binary search, http://cs101.openjudge.cn/practice/02774/



思路：

自己想到了二分查找

代码：

```python
def binary_search(left,right):
    if left==right:
        return left
    mid=(left+right+1)//2
    if check(mid):
        return binary_search(mid,right)
    else:
        return binary_search(left,mid-1)

def check(x):
    cnt=0
    for log in logs:
        cnt+=log//x
    if cnt>=k:
        return True
    else:
        return False

n,k=map(int,input().split())
logs=[]
for _ in range(n):
    logs.append(int(input()))

print(binary_search(0,sum(logs)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-08 23.33.31](https://p.ipic.vip/gyzmil.png)



### M07161:森林的带度数层次序列存储

tree, http://cs101.openjudge.cn/practice/07161/



思路：

尝试了函数封装的代码，感觉清爽了一些

代码：

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

    def add_child(self, child):
        self.children.append(child)

def postorder_recursion(root):
    if root is None:
        return []
    tmp = []
    for child in root.children:
        tmp.extend(postorder_recursion(child))
    tmp += [root.data]
    return tmp

def postorder_stack(root):
    white, gray = 0, 1
    queue = [(root, white)]
    result = []
    while queue:
        node, color = queue.pop()
        if node:
            if color == gray:
                result.append(node.data)
            else:
                queue.append((node, gray))
                for child in node.children[::-1]:
                    queue.append((child, white))
    return result

def build_a_tree(node_list, degree_list):
    p, q = 0, 1
    while p < len(node_list):
        for _ in range(degree_list[p]):
            node_list[p].add_child(node_list[q])
            q += 1
        p += 1
    return node_list[0]

n = int(input())
ans = []
for _ in range(n):
    tree = list(input().split())
    node_list = [TreeNode(tree[i]) for i in range(0, len(tree), 2)]
    degree_list = [int(tree[i]) for i in range(1, len(tree), 2)]
    ans += postorder_stack(build_a_tree(node_list, degree_list))
print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-02 19.34.01](https://p.ipic.vip/6w7p0m.png)



### M18156:寻找离目标数最近的两数之和

two pointers, http://cs101.openjudge.cn/practice/18156/



思路：



代码：

```python
target=int(input())
nums=sorted(list(map(int,input().split())))
def find_sum():
    left,right=0,len(nums)-1
    dif=float('inf')
    cur=nums[0]+nums[-1]
    tmp=0
    ans=[]
    while left < right:
        cur = nums[left] + nums[right]
        if abs(cur-target)==dif:
            if tmp != cur:
                ans.append(cur)
        elif abs(cur-target) < dif:
            dif = abs(cur-target)
            ans=[cur]
        tmp=cur
        if tmp < target:
            left+=1
        elif tmp > target:
            right-=1
        else:
            return cur
    return min(ans)
print(find_sum())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-08 23.32.27](/Users/liguanli/Library/Application Support/typora-user-images/截屏2025-04-08 23.32.27.png)



### M18159:个位为 1 的质数个数

sieve, http://cs101.openjudge.cn/practice/18159/



思路：

bisect就能过了。一开始想的是把所有输入排序，之后输出。但是没搞定序号映射。

代码：

```python
# is_prime=[True for i in range(10003)]
# primes=[]
# is_prime[0]=False
# is_prime[1]=False
# for i in range(2, 10003):
#     if is_prime[i]:
#         primes.append(i)
#     for prime in primes:
#         if i*prime >= 10003:
#             break
#         is_prime[i*prime] = False
#         if i%prime==0:
#             break
# uses=[]
# for prime in primes:
#     if prime%10==1:
#         uses.append(prime)
# print(uses)

import bisect
uses=[11, 31, 41, 61, 71, 101, 131, 151, 181, 191, 211, 241, 251, 271, 281, 311, 331, 401, 421, 431, 461, 491, 521, 541, 571, 601, 631, 641, 661, 691, 701, 751, 761, 811, 821, 881, 911, 941, 971, 991, 1021, 1031, 1051, 1061, 1091, 1151, 1171, 1181, 1201, 1231, 1291, 1301, 1321, 1361, 1381, 1451, 1471, 1481, 1511, 1531, 1571, 1601, 1621, 1721, 1741, 1801, 1811, 1831, 1861, 1871, 1901, 1931, 1951, 2011, 2081, 2111, 2131, 2141, 2161, 2221, 2251, 2281, 2311, 2341, 2351, 2371, 2381, 2411, 2441, 2521, 2531, 2551, 2591, 2621, 2671, 2711, 2731, 2741, 2791, 2801, 2851, 2861, 2971, 3001, 3011, 3041, 3061, 3121, 3181, 3191, 3221, 3251, 3271, 3301, 3331, 3361, 3371, 3391, 3461, 3491, 3511, 3541, 3571, 3581, 3631, 3671, 3691, 3701, 3761, 3821, 3851, 3881, 3911, 3931, 4001, 4021, 4051, 4091, 4111, 4201, 4211, 4231, 4241, 4261, 4271, 4391, 4421, 4441, 4451, 4481, 4561, 4591, 4621, 4651, 4691, 4721, 4751, 4801, 4831, 4861, 4871, 4931, 4951, 5011, 5021, 5051, 5081, 5101, 5171, 5231, 5261, 5281, 5351, 5381, 5431, 5441, 5471, 5501, 5521, 5531, 5581, 5591, 5641, 5651, 5701, 5711, 5741, 5791, 5801, 5821, 5851, 5861, 5881, 5981, 6011, 6091, 6101, 6121, 6131, 6151, 6211, 6221, 6271, 6301, 6311, 6361, 6421, 6451, 6481, 6491, 6521, 6551, 6571, 6581, 6661, 6691, 6701, 6761, 6781, 6791, 6841, 6871, 6911, 6961, 6971, 6991, 7001, 7121, 7151, 7211, 7321, 7331, 7351, 7411, 7451, 7481, 7541, 7561, 7591, 7621, 7681, 7691, 7741, 7841, 7901, 7951, 8011, 8081, 8101, 8111, 8161, 8171, 8191, 8221, 8231, 8291, 8311, 8431, 8461, 8501, 8521, 8581, 8641, 8681, 8731, 8741, 8761, 8821, 8831, 8861, 8941, 8951, 8971, 9001, 9011, 9041, 9091, 9151, 9161, 9181, 9221, 9241, 9281, 9311, 9341, 9371, 9391, 9421, 9431, 9461, 9491, 9511, 9521, 9551, 9601, 9631, 9661, 9721, 9781, 9791, 9811, 9851, 9871, 9901, 9931, 9941]
t=int(input())
for _ in range(t):
    a=int(input())
    ans=uses[:bisect.bisect_left(uses,a)]
    print(f"Case{_+1}:")
    if ans:
        print(*ans)
    else:
        print('NULL')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-08 23.32.43](https://p.ipic.vip/c77d0d.png)



### M28127:北大夺冠

hash table, http://cs101.openjudge.cn/practice/28127/



思路：



代码：

```python
from collections import defaultdict
correct_question=defaultdict(set)
submit_cnt=defaultdict(int)
m=int(input())
for _ in range(m):
    school, question, state=input().split(',')
    submit_cnt[school]+=1
    if state=='yes':
        correct_question[school]|={question}

ans=[]
for school in submit_cnt:
    try:
        ans.append((school,len(correct_question[school]),submit_cnt[school]))
    except KeyError:
        ans.append((school,0, submit_cnt[school]))
ans.sort(key=lambda x :(-x[1],x[2],x[0]))
for i in range(min(len(ans),12)):
    print(f'{i+1} {ans[i][0]} {ans[i][1]} {ans[i][2]}')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2025-04-02 19.01.32](https://p.ipic.vip/8h8s92.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

月考难









