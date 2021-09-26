import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
今天这一题很有意思，我尽量描述清楚，估计要常常画图 + debug 逐步调试才能理解，方法还是很巧妙的
它实质上是手动用 multidict(multidict) 构造了一个两层的结构，第一层是横坐标，第二层是纵坐标（因此横坐标和纵坐标的会在第二层的list 里）

    3
   / \
  9  20
    /  \
   15   7
   
在 seen 中的得到结构可以理解是
{
    0  : {0: [3], 2: [15]}
    -1 : {1: [9]}
    1  : {1: [20]}
    2  : {2: [7]}
}
第一层的 key 是 横坐标，第二层的 key 是纵坐标
从这个角度来说，题例给的横纵坐标其实跟我们习惯的横纵坐标不太一样，增加了理解的难度

然后，循环从横坐标小的开始，将同一个横坐标的值单独合并成一个 list



需要注意的是，同一层如果横纵坐标相等，第二层的 value 会在同一个 list 里面
在同一个 list 里面的时候，需要排序，因此多一个排序 sorted(seen[x][y])
举例如下，这里面 5 和 6 是同一个横纵坐标

    1
   / \
  2   3
 /\   /\
4  6 5  7

因此 seen 的结构如下
{
    -2 : {2: [4]}
    -1 : {1: [2]}
    0  : {0: [1], 2: [6,5]}
    1  : {1: [3]}
    2  : {2: [7]}
}

time: O(NlogN)，其中 N 为树的节点总数
space: O(N)
'''

class Solution:
    def verticalTraversal(self, root: TreeNode):
        seen = collections.defaultdict(lambda: collections.defaultdict(list))

        def dfs(root, x=0, y=0):
            if not root:
                return
            seen[x][y].append(root.val)
            dfs(root.left, x-1, y+1)
            dfs(root.right, x+1, y+1)

        dfs(root)
        ans = []

        for x in sorted(seen):
            level = []
            for y in sorted(seen[x]):
                level += sorted(seen[x][y])

            ans.append(level)

        return ans


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

s = Solution()
s.verticalTraversal(a)
