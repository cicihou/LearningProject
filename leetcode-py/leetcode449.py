'''
把 lc 297 的答案抄了一遍
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def preorder(root):
            if not root:
                return '#,'
            return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)

        return preorder(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data or data == '#':
            return
        nodes = data.split(',')

        def preorder(i):
            if i >= len(nodes) or nodes[i] == '#':
                return i, None
            root = TreeNode(nodes[i])
            j, root.left = preorder(i + 1)
            k, root.right = preorder(j + 1)
            return k, root

        return preorder(0)[1]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
