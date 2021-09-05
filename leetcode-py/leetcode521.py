class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        '''
        一共有三种情况
        1. a == b, 那么 return -1
        2. len(a) == len(b)，此时 a!= b，那么这两个中任意的 str 都可视作最长的不相等子序列
        3. len(a) != len(b)，此时 max(len(a), len(b)) 的就是最长的不相等子序列
        '''
        if a == b:
            return -1
        return max(len(a), len(b))
