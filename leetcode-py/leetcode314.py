# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        当前层的节点坐标若为 (x, y)
        下一层的节点坐标就会是 (x-1, y+1), (x+1, y+1)

        cache 第一层记录 x, 第二层记录 y
        这题跟 987 相似
        '''
        cache = {}

        def dfs(root, x, y):
            if root:
                nx = cache.get(x, {})
                nx[y] = nx.get(y, []) + [root.val]
                cache[x] = nx
                dfs(root.left, x - 1, y + 1)
                dfs(root.right, x + 1, y + 1)

        dfs(root, 0, 0)
        res = []

        for k in sorted(cache):
            tmp = cache[k]
            vertical = []
            for v in sorted(tmp):
                vertical += tmp[v]
            res.append(vertical)
        return res
