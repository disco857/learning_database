# Assignment #8: 树为主

Updated 1704 GMT+8 Apr 8, 2025

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

### LC108.将有序数组转换为二叉树

dfs, https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

思路：



代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_bst(left, mid - 1)
            node.right = build_bst(mid + 1, right)
            return node
        return build_bst(0,len(nums)-1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-08 23.51.31](https://p.ipic.vip/a7eexc.png)



### M27928:遍历树

 adjacency list, dfs, http://cs101.openjudge.cn/practice/27928/

思路：



代码：

```python
class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.children=[]
        self.father=None

    def set_val(self,val):
        self.val=val

    def add_child(self,other):
        self.children.append(other)

    def set_father(self,other):
        self.father = other

    def __str__(self):
        return str(self.val)

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val

def traverse_tree(node):
    if node is None:
        return []
    all_sorted = sorted(node.children+[node])
    tmp=[]
    for x in all_sorted:
        if x is node:
            tmp.append(x)
        else:
            tmp+=traverse_tree(x)
    return tmp

def find_root(node):
    if node.father is None:
        return node
    else:
        return find_root(node.father)

n=int(input())
check_list={}
node_list=[TreeNode() for i in range(n)]
i=0
for _ in range(n):
    token=list(map(int,input().split()))
    try:
        check_list[token[0]]
    except KeyError:
        check_list[token[0]]=i
        node_list[check_list[token[0]]].set_val(token[0])
        i+=1
    for child in token[1:]:
        try:
            node_list[check_list[token[0]]].add_child(node_list[check_list[child]])
            node_list[check_list[child]].set_father(node_list[check_list[token[0]]])
        except KeyError:
            check_list[child]=i
            node_list[check_list[child]].set_val(child)
            node_list[check_list[token[0]]].add_child(node_list[check_list[child]])
            node_list[check_list[child]].set_father(node_list[check_list[token[0]]])
            i+=1

root = find_root(node_list[0])
ans = traverse_tree(root)
for x in ans:
    print(x,end='\n')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-08 23.52.16](https://p.ipic.vip/gbbfrw.png)



### LC129.求根节点到叶节点数字之和

dfs, https://leetcode.cn/problems/sum-root-to-leaf-numbers/

思路：



代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum_numbers(root)

def find_numbers(node):
    if not node:
        return []
    tmp_left = find_numbers(node.left)
    tmp_right = find_numbers(node.right)
    left_numbers=[]
    right_numbers=[]
    if tmp_left or tmp_right:
        for num in tmp_left:
            left_numbers.append(str(node.val)+num)
        for num in tmp_right:
            right_numbers.append(str(node.val)+num)
        return left_numbers + right_numbers
    else:
        return [str(node.val)]

def sum_numbers(node):
    ans=find_numbers(node)
    if not ans:
        return 0
    else:
        return sum(list(map(int,ans)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-08 23.53.50](https://p.ipic.vip/7f8il4.png)



### M22158:根据二叉树前中序序列建树

tree, http://cs101.openjudge.cn/practice/22158/

思路：



代码：

```python
class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

def build_a_tree(preorder, inorder):
    if len(preorder) == 0:
        return None
    root = TreeNode(preorder[0])
    i=0
    while i<len(inorder) and inorder[i] != root.val:
        i+=1
    root.left = build_a_tree(preorder[1:1+i], inorder[:i])
    root.right = build_a_tree(preorder[i+1:], inorder[i+1:])
    return root

def print_tree(root,level=0):
    if root is None:
        return
    print_tree(root.left,level+1)
    print('   '*level+str(root.val))
    print_tree(root.right,level+1)

def postorder_stack(root):
    white,gray=0,1
    queue=[(root,white)]
    result=[]
    while queue:
        node,color=queue.pop()
        if node:
            if color==gray:
                result.append(node.val)
            else:
                queue.append((node,gray))
                queue.append((node.right,white))
                queue.append((node.left,white))
    return result

# preorder = list(map(int, input().strip().split()))
# inorder = list(map(int, input().strip().split()))
while True:
    try:
        preorder = input()
        inorder = input()
        root = build_a_tree(preorder, inorder)
        print(''.join(postorder_stack(root)))
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-09 00.01.34](https://p.ipic.vip/zn7wdz.png)



### M24729:括号嵌套树

dfs, stack, http://cs101.openjudge.cn/practice/24729/

思路：



代码：

```python
def preorder(tree):
    result=''
    for char in tree:
        if char.isalpha():
            result+=char
    return result

def postorder(tree):
    stack=[]
    result=''
    for char in tree:
        if char.isalpha() or char == '(':
            stack.append(char)
        elif char == ',':
            while stack and stack[-1]!='(':
                result+=stack.pop()
        elif char == ')':
            while stack and stack[-1]!='(':
                result+=stack.pop()
            stack.pop()
            result+=stack.pop()
    while stack:
        result+=stack.pop()
    return result

tree=input().strip()
print(preorder(tree))
print(postorder(tree))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-09 14.32.22](https://p.ipic.vip/g4jwrp.png)



### LC3510.移除最小数对使数组有序II

doubly-linked list + heap, https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/

思路：

看题解才会，总结了几点：

1. 懒删除表面上看是一种减少时间复杂度的手段，实际上是刚需，特别是配合heapq的时候。这是因为heapq在对pop的元素进行操作的时候，往往有“牵连”。但这些牵连的元素无法立刻被处理，因为我们不知道它们在heapq中的位置。我们只好先记录下来，等到之后涉及到该元素是在进行操作。
2. 这段代码没有显式地使用双向链表，是因为在这里双向链表用于实现类似坐标映射的东西。如果我们直接操作nums，从中合并元素，弊端不仅是del的时间复杂度高，而且这会打乱坐标（直接在nums中合并会导致合并位置之后的所有坐标改变，而heapq中的坐标无法更改，导致后续出错）。坐标映射完美解决了这个问题，且非常高效。
3. 为防止越界并进一步统一，坐标映射left和right中添加了哨兵。注意不要漏写相应的判断坐标合法的语句。
4. 以及学到了用相邻严格递减数对的个数来判断整个数列是否单增的方法。

代码：

```python
import heapq
from collections import defaultdict
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        return min_pair_removal(nums)

def min_pair_removal(nums):
    pairs = []
    lazy = defaultdict(int)
    dec=0
    for i in range(len(nums)-1):
        pairs.append((nums[i]+nums[i+1],i))
        if nums[i] > nums[i+1]:
            dec+=1
    heapq.heapify(pairs)

    left=[i for i in range(-1,len(pairs))]
    right=[i for i in range(1,len(pairs)+2)]

    ans=0

    while dec>0:
        ans+=1

        while lazy[pairs[0]]:
            lazy[pairs[0]] -= 1
            heapq.heappop(pairs)

        pair_sum,cur=heapq.heappop(pairs)
        nxt=right[cur]
        nxt2=right[nxt]
        prev=left[cur]

        if nums[cur] > nums[nxt]:
            dec-=1
        if prev>=0:
            if nums[prev] > nums[cur]:
                dec-=1
            lazy[(nums[prev]+nums[cur],prev)]+=1
        if nxt2<len(nums):
            if nums[nxt] > nums[nxt2]:
                dec-=1
            lazy[(nums[nxt]+nums[nxt2],nxt)]+=1

        nums[cur] = pair_sum
        right[cur] = nxt2
        if nxt2<len(nums):
            left[nxt2] = cur
        if prev>=0:
            if nums[prev] > pair_sum:
                dec+=1
            heapq.heappush(pairs,(nums[prev]+pair_sum,prev))
        if nxt2<len(nums):
            if pair_sum > nums[nxt2]:
                dec+=1
            heapq.heappush(pairs,(nums[nxt2]+pair_sum,cur))
    return ans

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-15 23.48.40](https://p.ipic.vip/wg49d4.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

跟进每日选做。每日选做比较简单时会做leetcode每日一题。







