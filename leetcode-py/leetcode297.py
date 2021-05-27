'''
递归的图解视频：https://www.youtube.com/watch?v=suj1ro8TIVY

'''


'''
method 1 BFS 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        ans = ''
        while queue:
            cur = queue.pop(0)
            if cur:
                ans += str(cur.val) + ','
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                ans += '#,'
        return ans[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#' or not data:
            return None
        nodes = data.split(',')
        root = TreeNode(nodes[0])

        queue = [root]
        i = 1
        while i < len(nodes) - 1:
            node = queue.pop(0)
            lv = nodes[i]
            rv = nodes[i+1]
            i += 2  # 左右各加 1
            if lv != '#':
                l = TreeNode(lv)
                node.left = l
                queue.append(l)

            if rv != '#':
                r = TreeNode(rv)
                node.right = r
                queue.append(r)
        return root


'''
method 2 dfs + recursion
'''
class CodecDFS:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if not root:
                return '#,'
            return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
        return preorder(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
