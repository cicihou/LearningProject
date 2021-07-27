# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        method 1
        dfs
        '''
        res = []
        def dfs(root, level):
            if len(res) < level:
                res.append([])
            if root:
                res[level-1].append(root.val)
                dfs(root.left, level+1)
                dfs(root.right, level+1)
        dfs(root, 1)
        ans = []
        for levels in res:
            if levels:
                ans.append(levels[-1])
        return ans

        '''
        method 2
        bfs
        '''
        q = collections.deque([(root, 1)])

        res = []
        while q:
            root, level = q.popleft()
            if level > len(res):
                res.append([])
            if root:
                res[level - 1].append(root.val)
                q.append((root.left, level + 1))
                q.append((root.right, level + 1))

        ans = []
        for levels in res:
            if levels:
                ans.append(levels[-1])
        return ans
