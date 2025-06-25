# Assignment #6: 回溯、树、双向链表和哈希表

Updated 1526 GMT+8 Mar 22, 2025

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

### LC46.全排列

backtracking, https://leetcode.cn/problems/permutations/

思路：



代码：

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N=len(nums)
        result=[]
        def arrange(path,k,seen):
            if k==N:
                result.append(path)
                return
            for num in nums:
                if num not in seen:
                    arrange(path+[num],k+1,seen|{num})
        
        arrange([],0,set())
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-29 11.52.10](https://p.ipic.vip/1omjm9.png)



### LC79: 单词搜索

backtracking, https://leetcode.cn/problems/word-search/

思路：



代码：

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(k, seen ,cur_x, cur_y):
            if k == n:
                return True
            for i in range(4):
                nx, ny = cur_x + dic[i][0], cur_y + dic[i][1]
                if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in seen and board[nx][ny] == word[k]:
                    seen.add((nx,ny))
                    if dfs(k + 1, seenx, ny):
                        return True
                    seen-={(nx,ny)}
            return False

        dic = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        M, N= len(board),len(board[0])
        n=len(word)
        seen=set()
        for i in range(M):
            for j in range(N):
                if board[i][j]==word[0]:
                    if dfs(1,i,j):
                        return True
        return False
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-30 23.49.31](https://p.ipic.vip/rr9fmh.png)



### LC94.二叉树的中序遍历

dfs, https://leetcode.cn/problems/binary-tree-inorder-traversal/

思路：

这题一开始下意识用bfs的写法pop(0)出问题了。后来想到这里不是什么先后关系，是必须要把左子树处理完再处理节点，因此压入左子树，也应该先弹出左子树，否则左子树就处理了一层就到后面去了。

代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        WHITE, GRAY = 0, 1
        queue = [(root, WHITE)]
        result = []
        while queue:
            node, color = queue.pop()
            if node:
                if color == GRAY:
                    result.append(node.val)
                else:
                    queue.append((node.right, WHITE))
                    queue.append((node, GRAY))
                    queue.append((node.left, WHITE))
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-04-01 23.37.08](https://p.ipic.vip/wfpbqf.png)

### LC102.二叉树的层序遍历

bfs, https://leetcode.cn/problems/binary-tree-level-order-traversal/

思路：



代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result=[]
        while queue:
            cnt=len(queue)
            tmp=[]
            for i in range(cnt):
                node=queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp)
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-29 14.41.35](https://p.ipic.vip/a5mpr5.png)



### LC131.分割回文串

dp, backtracking, https://leetcode.cn/problems/palindrome-partitioning/

思路：



代码：

```python
#法一：纯粹dfs
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def dfs(path, start,result):
            if start == len(s):
                result.append(path)
                return
            for end in range(start, len(s)):
                if s[start:end + 1] == s[start:end + 1][::-1]:
                    dfs(path + [s[start:end + 1]], end + 1,result)

        result=[]
        dfs([], 0,result)
        return result
```

```python
#法二：dp预处理+dfs
class Solution:
    def partition(self, s: str) -> List[List[str]]:
      
        n=len(s)
        dp=[[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
        for j in range(2,n):
            for i in range(n-j):
                if s[i] == s[i + j]:
                    dp[i][i + j] = dp[i + 1][i + j - 1]

        def dfs(path,start,result):
            if start==n:
                result.append(path)
            for end in range(start,n):
                if dp[start][end]:
                    dfs(path+[s[start:end+1]],end+1,result)

        result=[]
        dfs([],0,result)
        return result
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-31 16.54.39](https://p.ipic.vip/y6dvwr.png)



### LC146.LRU缓存

hash table, doubly-linked list, https://leetcode.cn/problems/lru-cache/

思路：



代码：

```python
class ListNode:

    def __init__(self,key,pre=None,nex=None):
        self.key = key
        self.pre = pre
        self.nex = nex

    def __str__(self):
        return f'Node {self.key}'

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = {}
        self.latest = None
        self.longest = None

    def get(self, key: int) -> int:
        try:
            ans=self.data[key][0]
            tmp=self.data[key][1]
            if self.latest!=tmp:
                tmp.nex.pre=tmp.pre
                if tmp.pre:
                    tmp.pre.nex=tmp.nex
                else:
                    self.longest=tmp.nex
                self.latest.nex=tmp
                tmp.pre=self.latest
                tmp.nex=None
                self.latest=tmp
            return ans
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            self.data[key][0]=value
            self.get(key)
            return
        except KeyError:
            tmp=ListNode(key)
            self.data[key]=[value,tmp]
            if self.latest:
                self.latest.nex=tmp
                tmp.pre=self.latest
            else:
                self.longest=tmp
            self.latest=tmp
            if len(self.data)>self.cap:
                del self.data[self.longest.key]
                self.longest.nex.pre=None
                self.longest=self.longest.nex

    def __str__(self):
        result = "{"
        for key, value in self.data.items():
            node_str = str(value[1])  # 使用 ListNode 的 __str__ 方法
            result += f"{key}: [{value[0]}, {node_str}], "
        if result.endswith(", "):
            result = result[:-2]
        result += "}"
        return result

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-03-29 11.52.56](https://p.ipic.vip/f0b25j.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

对树的理解更加熟练，但是感觉一些递归函数的逻辑自己还是不能完全写出，容易出现重复检查，冗余检查（一般情况下就讨论if node即可作为终止条件，但有时候总写不出来，反而讨论一些node.left，node.right之类的东西，归根结底是对隐式检查不熟练）的情况。把之前自己总结的关于stack的理论应用于括号嵌套二叉树这道题，20分钟实现了没有建树的解法，还是小有成就感的。

另外，今天因为02788:二叉树的一个小问题疯狂debug一个多小时，又有了最开始学计概的感觉。思维还是要缜密啊。
