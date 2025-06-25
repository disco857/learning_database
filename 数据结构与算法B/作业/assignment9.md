# Assignment #9: Huffman, BST & Heap

Updated 1834 GMT+8 Apr 15, 2025

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

### LC222.完全二叉树的节点个数

dfs, https://leetcode.cn/problems/count-complete-tree-nodes/

思路：

两种方法：

1. 先想到的肯定是遍历，简单粗暴
2. 后来想到类似题解的，先确定一个范围，之后二分查找。但当时脑子有点糊涂，没想明白如何找到对应的节点，看了题解恍然大悟，原来还可以二级制产生联系，很妙。

代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return count(root)
        
def count(node):
    if not node:
        return 0 
    return count(node.left)+count(node.right)+1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-16 21.00.39](https://p.ipic.vip/cul7kp.png)



### LC103.二叉树的锯齿形层序遍历

bfs, https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

思路：

不难，只需要来回使用popleft和append，以及pop和appendleft，同时改变左孩子和右孩子的入栈顺序即可恰好实现。相当于一层右进左出，一层左进右出。

代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return zigzag_level_order(root)

def zigzag_level_order(root):
    queue=deque([root])
    result=[]
    tic=0
    while queue:
        cnt=len(queue)
        tmp=[]
        if tic % 2 == 0:
            for _ in range(cnt):
                node=queue.popleft()
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
        else:
            for _ in range(cnt):
                node=queue.pop()
                if node:
                    tmp.append(node.val)
                    queue.appendleft(node.right)
                    queue.appendleft(node.left)
        result.append(tmp)
        tic+=1
    return result[:-1]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-16 20.57.52](https://p.ipic.vip/wci6xi.png)



### M04080:Huffman编码树

greedy, http://cs101.openjudge.cn/practice/04080/

思路：

由于前一天刚写完T22161: 哈夫曼编码树，受到惯性思维影响，直接建树。后来问AI才发现根本不需要，只需要每次合并时都对结果加上两个子节点的权重和即可。

另外才知道必须先heapify才能用heappop、heappush之类的，否则会出错。

代码：

```python
#pylint:skip-file
import heapq

class TreeNode:
    def __init__(self, weight, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

def build_huffman_tree(initial_nodes):
    heapq.heapify(initial_nodes)  # 关键修复：添加堆初始化
    while len(initial_nodes) > 1:
        node1 = heapq.heappop(initial_nodes)
        node2 = heapq.heappop(initial_nodes)
        merged = TreeNode(node1.weight + node2.weight, node1, node2)
        heapq.heappush(initial_nodes, merged)
    return initial_nodes[0] if initial_nodes else None

def calculate(root: TreeNode):
    total = 0
    def traverse(node, depth):
        nonlocal total
        if not node.left and not node.right:
            total += node.weight * depth
            return
        if node.left:
            traverse(node.left, depth + 1)
        if node.right:
            traverse(node.right, depth + 1)
    if root:
        traverse(root, 0)
    return total

n = int(input())
weights = list(map(int, input().split()))
initial_nodes = [TreeNode(w) for w in weights]
print(calculate(build_huffman_tree(initial_nodes)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-16 20.55.19](https://p.ipic.vip/ek46ci.png)



### M05455: 二叉搜索树的层次遍历

http://cs101.openjudge.cn/practice/05455/

思路：



代码：

```python
from collections import deque
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def insert(node,x):
    if not node:
        return TreeNode(x)
    if node.val < x:
        node.right = insert(node.right, x)
    elif node.val > x:
        node.left = insert(node.left, x)
    return node

def build_tree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    for num in nums[1:]:
        insert(root, num)
    return root

def level_order(root):
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return result

nums=list(map(int,input().split()))
root = build_tree(nums)
print(*level_order(root))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-21 11.09.44](https://p.ipic.vip/ml02z5.png)



### M04078: 实现堆结构

手搓实现，http://cs101.openjudge.cn/practice/04078/

类似的题目是 晴问9.7: 向下调整构建大顶堆，https://sunnywhy.com/sfbj/9/7

思路：

掌握堆的三个核心知识：父节点与子节点的索引关系、上滤操作、下滤操作。硬要说第四个的话是如何在O(n)内建堆。

代码：

```python
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def perc_up(self,i):
        while (i-1)//2>=0:
            father=(i-1)//2
            if self.heap[i] < self.heap[father]:
                self.heap[i], self.heap[father] = self.heap[father], self.heap[i]
            else:
                break
            i = father

    def perc_down(self,i):
        while 2*i+1<len(self.heap):
            sm_child=self.get_min_child(i)
            if self.heap[i] > self.heap[sm_child]:
                self.heap[i], self.heap[sm_child] = self.heap[sm_child], self.heap[i]
            else:
                break
            i = sm_child

    def get_min_child(self,i):
        left_child = 2*i+1
        right_child = 2*i+2
        if right_child < len(self.heap):
            if self.heap[left_child] < self.heap[right_child]:
                return left_child
            else:
                return right_child
        else:
            return left_child

    def insert(self,val):
        self.heap.append(val)
        self.perc_up(len(self.heap)-1)

    def remove(self):
        self.heap[0] , self.heap[-1] = self.heap[-1], self.heap[0]
        ans=self.heap.pop()
        self.perc_down(0)
        return ans

    def heapify(self, not_a_heap):
        self.heap = not_a_heap
        for i in range((len(not_a_heap)-1)//2-1,-1,-1):
            self.perc_down(i)

t=int(input())
heap=BinaryHeap()
heap.heapify([])
for _ in range(t):
    token=list(map(int,input().split()))
    if token[0]==1:
        heap.insert(token[1])
    elif token[0]==2:
        print(heap.remove())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-16 20.49.42](https://p.ipic.vip/i9zv9s.png)



### T22161: 哈夫曼编码树

greedy, http://cs101.openjudge.cn/practice/22161/

思路：

难点是读懂题，啥叫合并啊？问了AI才懂。之后就不难了，因为题目中已经把每一步要做什么说明白了。

代码：

```python
#pylint:skip-file
import heapq
class TreeNode:
    def __init__(self,chars,smallest_char,weight,left=None,right=None):
        self.chars = chars
        self.smallest_char = smallest_char
        self.weight = weight
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.chars}, {self.weight})'

    def __lt__(self,other):
        if self.weight != other.weight:
            return self.weight < other.weight
        else:
            return self.smallest_char < other.smallest_char

    def __eq__(self,other):
        return self.weight == other.weight and self.smallest_char == other.smallest_char

    def __gt__(self,other):
        if self.weight != other.weight:
            return self.weight > other.weight
        else:
            return self.smallest_char > other.smallest_char

def build_a_tree(node_list):
    while len(node_list)>1:
        node1 = heapq.heappop(node_list)
        node2 = heapq.heappop(node_list)
        new_node=TreeNode(node1.chars|node2.chars,min(node1.smallest_char,node2.smallest_char),node1.weight+node2.weight)
        new_node.left = min(node1,node2)
        new_node.right = max(node1,node2)
        heapq.heappush(node_list,new_node)
    return node_list[0]

def generate_code_table(path,node):
    global code_table
    if not node.left and not node.right:
        code_table[node.smallest_char] = ''.join(path)
        return
    if node.left:
        generate_code_table(path+['0'],node.left)
    if node.right:
        generate_code_table(path+['1'],node.right)

def encode(context,code_table):
    result=''
    for char in context:
        result += code_table[char]
    return result

def decode(secret,root):
    result=''
    i=0
    cur=root
    while i<len(secret):
        if not cur.left and not cur.right:
            result += cur.smallest_char
            cur=root
        else:
            if secret[i] == '0':
                cur = cur.left
            elif secret[i] == '1':
                cur = cur.right
            i+=1
    result += cur.smallest_char
    return result

n=int(input())
node_list = []
for i in range(n):
    char, weight = input().split()
    node_list.append(TreeNode({char},char,int(weight)))
root = build_a_tree(node_list)
code_table = {}
generate_code_table([],root)
while True:
    try:
        token = input()
        try:
            int(token)
            print(decode(token, root))
        except ValueError:
            print(encode(token,code_table))
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-16 20.47.03](https://p.ipic.vip/ueyuik.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

leetcode周赛因为有事又鸽了。五一一定可以做一次！感觉数算内容好多，但是落实到题面上又没多少，是有的内容不会考吗？比如AVL树









