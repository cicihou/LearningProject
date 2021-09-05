class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        '''
        一个非常巧妙的解法，结合了 stack 和 preorder 的特性

        代码：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/

        preorder 是 根左右，因此我们可以判断左子树是否有效，再判断右子树，再判断根
        从递归的 base case 开始，怎么判断一个节点是叶子结点，当一个节点的两个子节点都是 '#' 的时候，就是叶子结点
        我们把有效的叶子节点使用 "#" 代替。 比如把 4## 替换成 # 。此时，叶子节点会变成空节点！
        递归操作，只要循环的最后，有且只有一个空节点，就表明这棵树是有效的

        :param preorder:
        :return:
        '''
        stack = []
        nodes = preorder.split(',')
        for node in nodes:
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#' != stack[-3]:
                for _ in range(3): stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack[0] == '#'
