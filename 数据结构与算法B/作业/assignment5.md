# Assignment #5: 链表、栈、队列和归并排序

Updated 1348 GMT+8 Mar 17, 2025

2025 spring, Complied by <mark>李冠黎 工学院</mark>



> **说明：**
>
> 1. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### LC21.合并两个有序链表

linked list, https://leetcode.cn/problems/merge-two-sorted-lists/

思路：



代码：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val <= list2.val:
                cur=list1
                final=list1
                list1=list1.next
            else:
                cur=list2
                final=list2
                list2=list2.next
        elif list1:
            return list1
        elif list2:
            return list2
        else:
            return

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next                
            cur=cur.next

        while list1:
            cur.next=list1
            list1=list1.next
            cur=cur.next
        while list2:
            cur.next=list2
            list2=list2.next
            cur=cur.next

        return final
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-23 22.01.03](https://p.ipic.vip/9rqnwz.png)



### LC234.回文链表

linked list, https://leetcode.cn/problems/palindrome-linked-list/

<mark>请用快慢指针实现。</mark>



代码：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast:
            fast=fast.next
            slow=slow.next            
            if not fast:
                continue
            fast=fast.next
        compare=head
        a,b=[],[]
        while slow :
            a.append(compare.val)
            b.append(slow.val)
            slow,compare=slow.next,compare.next
        if a==b[::-1]:
            return True
        else:
            return False
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-23 21.22.01](https://p.ipic.vip/ndeer9.png)



### LC1472.设计浏览器历史记录

doubly-lined list, https://leetcode.cn/problems/design-browser-history/

<mark>请用双链表实现。</mark>



代码：

```python
#法一：列表模拟
class BrowserHistory:

    def __init__(self, homepage: str):
        self.loc=0
        self.pages=[homepage]

    def visit(self, url: str) -> None:
        if self.loc==len(self.pages)-1:
            self.pages.append(url)
            self.loc+=1
            return
        self.pages[self.loc+1:]=[url]
        self.loc=len(self.pages)-1

    def back(self, steps: int) -> str:
        self.loc-=min(self.loc,steps)
        return self.pages[self.loc]

    def forward(self, steps: int) -> str:
        self.loc+=min(steps,len(self.pages)-1-self.loc)
        return self.pages[self.loc]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

```python
#法二：双向链表
class dualLink:

    def __init__(self,val,nex=None,prev=None):
        self.val = val
        self.next = nex
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = dualLink(homepage)

    def visit(self, url: str) -> None:
        tmp=dualLink(url)
        self.page.next=tmp
        tmp.prev=self.page
        self.page=tmp

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.page.prev:
                break
            self.page=self.page.prev
        return self.page.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.page.next:
                break
            self.page=self.page.next
        return self.page.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-23 20.54.55](https://p.ipic.vip/p3bib4.png)

![截屏2025-03-23 21.01.48](https://p.ipic.vip/89xppz.png)

### 24591: 中序表达式转后序表达式

stack, http://cs101.openjudge.cn/practice/24591/

思路：



代码：

```python
weight={'+':1,'-':1,'*':2,'/':2,'^':3}
def has_higher_precedence(op1,op2):
    return weight[op1] >= weight[op2]
def infix_to_postfix(expression):
    result=[]
    char=[]
    i=0
    while i<len(expression):
        if expression[i].isdigit() or expression[i]=='.':
            tmp=''
            while i<len(expression) and (expression[i].isdigit() or expression[i]=='.'):
                tmp+=expression[i]
                i+=1
            result.append(tmp)
        else:
            if expression[i]=='(':
                char.append(expression[i])
            elif expression[i]==')':
                while char[-1]!='(':
                    result.append(char.pop())
                char.pop()
            else:
                while char and char[-1]!='(' and has_higher_precedence(char[-1],expression[i]):
                    result.append(char.pop())
                char.append(expression[i])
            i+=1
    while char:
        result.append(char.pop())

    return ' '.join(result)

n=int(input())
for _ in range(n):
    print(infix_to_postfix(input()))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-25 23.18.01](https://p.ipic.vip/tc49c3.png)



### 03253: 约瑟夫问题No.2

queue, http://cs101.openjudge.cn/practice/03253/

<mark>请用队列实现。</mark>



代码：

```python
from collections import deque
while True:
    n,p,m=map(int,input().split())
    if {n,p,m}=={0}:
        break
    kids=deque([i for i in range(p,n+1)]+[i for i in range(1,p)])
    result=[]
    while kids:
        for _ in range(m-1):
            kids.append(kids.popleft())
        result.append(kids.popleft())
    print(','.join(map(str,result)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-23 22.16.20](https://p.ipic.vip/n6w862.png)



### 20018: 蚂蚁王国的越野跑

merge sort, http://cs101.openjudge.cn/practice/20018/

思路：

和求排列的逆序数一样

代码：

```python
# pylint: skip-file
def merge_sort(left,right):
    global inverse_order_number
    if left==right:
        return [ants[left]]
    mid=(left+right)//2
    arr1=merge_sort(left,mid)
    arr2=merge_sort(mid+1,right)
    i,j=0,0
    result=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            result.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            inverse_order_number += len(arr1) - i
            result.append(arr2[j])
            j+=1
    while i<len(arr1):
        result.append(arr1[i])
        i+=1
    while j<len(arr2):
        result.append(arr2[j])
        j+=1
    return result

n=int(input())
ants=[]
for _ in range(n):
    ants.append(int(input()))
ants.reverse()
inverse_order_number=0
merge_sort(0,n-1)
print(inverse_order_number)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-25 23.18.45](https://p.ipic.vip/4yepi5.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

本周作业题目都还行，感觉对链表更加熟练了。但有几个每日选做真的不好做，看题解都要好久。









