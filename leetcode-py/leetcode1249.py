class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        1. stack 记录 () 的 index 位置，remove 记录需要移除的 index，二者并集就是需要去掉的 index
        2. 遇到 ( 时入栈，遇到 ) 时 出栈；stack 为空的时候，遇到 ) 直接放进 remove
        3. 所有需要移除的 index 直接从字符串中去掉

        time: O(n), stack.append && pop is O(1),
                    adding to a set and checking if an item is in a set: O(1)
        space: O(n)
        '''
        stack = []
        remove = set()
        for i, ch in enumerate(s):
            if ch in '()':
                if ch == '(':
                    stack.append(i)
                elif not stack:
                    remove.add(i)
                else:
                    stack.pop()
        remove = remove.union(set(stack))
        res = ''
        for i, ch in enumerate(s):
            if i not in remove:
                res += ch
        return res
