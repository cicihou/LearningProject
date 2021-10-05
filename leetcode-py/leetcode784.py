class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''
        每次碰到字母，分出两个分支，并且在上一分支的基础上循环，为上面的每条支线，都加上两个结果
        time: O(N * 2**N)
        space: O(N * 2**N)
        '''
        res = [[]]
        for ch in s:
            n = len(res)
            if ch.isalpha():
                for i in range(n):
                    res.append(res[i][:])
                    res[i].append(ch.lower())
                    res[i+n].append(ch.upper())
            else:
                for i in range(n):
                    res[i].append(ch)
        return map(''.join, res)
