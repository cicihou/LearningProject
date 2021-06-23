class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        视频：https://www.youtube.com/watch?v=sz1qaKt0KGQ
        backtracking
        '''
        res = []
        path = []

        def backtrack(path, left, right):
            if len(path) == 2 * n:
                res.append(path)
                return
            if left < n:
                path.append('(')
                backtrack(path, left+1, right)
                path.pop()
            if right < left:
                path.append(')')
                backtrack(path, left, right+1)
                path.pop()

        backtrack(path, 0, 0)
        return res
