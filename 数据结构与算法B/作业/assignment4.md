# Assignment #4: 位操作、栈、链表、堆和NN

Updated 1203 GMT+8 Mar 10, 2025

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

### 136.只出现一次的数字

bit manipulation, https://leetcode.cn/problems/single-number/



<mark>请用位操作来实现，并且只使用常量额外空间。</mark>

1. 任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
2. 任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
3. 与、或、异或运算均满足交换律和结合律

代码：

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result^=num
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-17 16.43.15](https://p.ipic.vip/448fn0.png)



### 20140:今日化学论文

stack, http://cs101.openjudge.cn/practice/20140/



思路：

还是看了题解，总结了几个点：

1. 栈主要是用来等待的。即，遇到某条指令，但是它要被如何操作依赖于它后面的指令，那么可以选择将它先入栈“待一会”，等遍历到后面知道了怎么做之后再利用pop方法回过头处理该指令。这是总原则
2. 很多栈相关的题目都涉及到括号，这其实就是要做匹配，知道一对括号中包括的是那些东西。这时还是可以利用第一条。当遇到左括号时，我们还不知道它对应的右括号在哪里，因此先将它入栈。等到遇到右括号时，再反向往回找一下，进行处理。
3. 栈相关的题目要先大概研究一下给的示例，看看答案和“密文”有什么联系。令我印象深刻的是中序表达式转后序表达式那道题。通过观察转换之后的后序表达式可以发现，数字的顺序不发生改变，而对于每一个运算单元，符号总在最后面。这其实告诉我们：数字是不需要入栈的，因为它们的操作不依赖于它后面的指令。当我们遇到一个数字时，我们可以直接把它append到结果里。只有运算符是需要入栈的，因为我们还不知道该运算符所对应的运算单元在什么地方结束。当我们因某些条件判断该运算单元结束，就可以把符号有序地pop出来，加入结果中。

代码：

```python
code=input()
result=[]
ast=[]
i=0
while i < len(code):
    if code[i]==']':
        while result[-1]!='[':
            ast.append(result.pop())
        result.pop()
        tmp=''
        while ast[-1] in {'0','1','2','3','4','5','6','7','8','9'}:
            tmp+=ast.pop()
        ast*=int(tmp)
        result+=ast[::-1]
        ast=[]
        i+=1
        continue
    result.append(code[i])
    i+=1
print(''.join(result))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-16 21.07.41](https://p.ipic.vip/t3fs29.png)



### 160.相交链表

linked list, https://leetcode.cn/problems/intersection-of-two-linked-lists/



思路：

本题最关键的一点：python默认所有用户创建的类都是可哈希的。python会基于它们的内存地址进行哈希。

代码：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur_a=headA
        A=set()
        while cur_a:
            A.add(cur_a)
            cur_a=cur_a.next
        cur_b=headB
        while cur_b:
            if cur_b in A:
                return cur_b
            cur_b=cur_b.next
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-16 12.16.20](https://p.ipic.vip/8u3hhn.png)



### 206.反转链表

linked list, https://leetcode.cn/problems/reverse-linked-list/



思路：



代码：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        pre,cur=head,head.next
        head.next=None
        while cur:
            tmp=cur.next
            cur.next=pre
            pre,cur=cur,tmp
        return pre
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-16 12.28.06](https://p.ipic.vip/k3jl00.png)



### 3478.选出和最大的K个元素

heap, https://leetcode.cn/problems/choose-k-elements-with-maximum-sum/



思路：

想到上学期月考炒股那道题

代码：

```python
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        import heapq
        n=len(nums1)
        data=[]
        for i in range(n):
            data.append([i,nums1[i],nums2[i]])
        data.sort(key=lambda x:x[1])
        max_k=[]
        s,cur=0,0
        result=[0 for _ in range(n)]
        for i in range(1,n):
            heapq.heappush(max_k,data[i-1][2])
            s+=data[i-1][2]
            if len(max_k)==k+1:
                s-=heapq.heappop(max_k)
            if data[i][1]!=data[i-1][1]:
                cur=s
            result[data[i][0]]=cur
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-18 17.48.57](https://p.ipic.vip/5y71ar.png)



### Q6.交互可视化neural network

https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises

**Your task:** configure a neural network that can separate the orange dots from the blue dots in the diagram, achieving a loss of less than 0.2 on both the training and test data.

**Instructions:**

In the interactive widget:

1. Modify the neural network hyperparameters by experimenting with some of the following config settings:
   - Add or remove hidden layers by clicking the **+** and **-** buttons to the left of the **HIDDEN LAYERS** heading in the network diagram.
   - Add or remove neurons from a hidden layer by clicking the **+** and **-** buttons above a hidden-layer column.
   - Change the learning rate by choosing a new value from the **Learning rate** drop-down above the diagram.
   - Change the activation function by choosing a new value from the **Activation** drop-down above the diagram.
2. Click the Play button above the diagram to train the neural network model using the specified parameters.
3. Observe the visualization of the model fitting the data as training progresses, as well as the **Test loss** and **Training loss** values in the **Output** section.
4. If the model does not achieve loss below 0.2 on the test and training data, click reset, and repeat steps 1–3 with a different set of configuration settings. Repeat this process until you achieve the preferred results.

给出满足约束条件的<mark>截图</mark>，并说明学习到的概念和原理。

![截屏2025-03-18 21.04.02](https://p.ipic.vip/211djd.png)

噪音35%是很容易的，40%却几乎不可能。目前的最好成果是噪音40%训练损失在0.19左右，但测试损失一直在0.25

## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

本周的作业完成的还算轻松，学到了位操作。神经网络很好玩，但是感觉太难了看不懂。逐渐找回手感但是仍有许多不足，如heapq，stack，还有上学期没学的各种sort要多加练习。其实目前的情况是比较两极分化的，难的知识点花很长时间也不一定做对，简单的知识点基本不用思考。接下来打算尽可能参加一场周赛看看水平，也算是一个鞭策吧。







