# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        method 1 recursion
        time: O(N)
        space: O(logN)

        注意先判断 not p and not q 这个比较狭窄的条件，再判断 False 对应的比较宽的条件
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        '''
        method 2 iteration + queue
        
        time: O(N)
        space: O(logN)
        '''
        def same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        # FIFO via queue + breadth travel
        queue = [(p, q)]
        while queue:
            p, q = queue.pop(0)
            if not same(p, q):
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True

        '''
        method 3 some oneline solutions, cool!
        https://leetcode.com/problems/same-tree/discuss/32729/Shortest%2Bsimplest-Python
        '''
