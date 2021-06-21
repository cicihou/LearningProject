class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        题目要求的 substring 是连续子字符串
        可以画 state space tree 帮助理解
        总之 backtracking 回溯就是 穷举 + 尝试
        '''
        res = []
        path = []

        def isPandrome(l, r):
            # 注意这里的判断回文必须要单独写
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(path, start):
            if start == len(s):
                res.append(path[:])
            else:
                for i in range(start, len(s)):
                    if isPandrome(start, i):
                        # 判断的时候用 start 和 i，因为单个字符也成立
                        # 由于 str slice 的特性，append的时候需要 i + 1 才能取到 s[i] 上的字符
                        path.append(s[start:i + 1])
                        backtrack(path, i + 1)
                        path.pop()

        backtrack(path, 0)
        return res
