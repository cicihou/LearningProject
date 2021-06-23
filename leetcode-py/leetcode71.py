class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for p in path:
            if p not in ['.', '', '/', '..']:
                stack.append(p)
            elif p in ['..'] and stack:
                stack.pop()
        return '/' + '/'.join(stack)


s = Solution()
s.simplifyPath('/../')
