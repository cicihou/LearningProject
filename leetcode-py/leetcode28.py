'''
注意空字符串会判定成存在于任意字符串
>>> "" in "a"
True
>>> "a".index("")
0
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        method 1 internal function
        '''
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 or needle not in haystack:
            return -1
        return haystack.index(needle)

        '''
        method 2 Brutal Force
        
        time: O(m*n)
        space: O(1)
        '''
        if not needle:
            return 0
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        for i in range(0, m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

        '''
        method 3
        RK Algorithm（Rabin–Karp Algorithm/Rolling Hash）滚动哈希
        
        计算 needle 的 ord 值，
        
        先计算出和 needle 长度一致的哈希值，也就是 haystack[:len(needle)] 的哈希值。
        然后我们需要移动窗口，每次移动一格。 这样哈希值仅需要减去左侧移除窗口的值和右侧移入窗口的值即可。
        滚动过程发现哈希值和 needle 的哈希值一致，则说明找到了，直接返回。
        到最后都没有找到，则返回 -1。
        
        https://www.youtube.com/watch?v=qQ8vS2btsxI
        https://www.youtube.com/watch?v=BQ9E-2umSWc
        
        time: 若 hash function 选的差，冲突多，则最坏是(NM)，一般情况是O(N+M)
        space: O(1)
        '''
        # TODO

        '''
        method 4
        KMP Algorithm 
        https://leetcode-solution.cn/solutionDetail?type=3&id=76&max_id=2
        
        KMP：O(N+M)
        KMP：O(M)
        '''
        if len(needle) == 0:
            return 0
        i = 0
        j = 0

        def kmp(pattern):
            next = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                if pattern[i] == pattern[j]:
                    j += 1
                    next[i] = j
                else:
                    while j > 0 and pattern[j] != pattern[i]:
                        j = next[j-1]
                    if pattern[i] == pattern[j]:
                        j += 1
                        next[i] = j
            return next

        nxt = kmp(needle)
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = nxt[j-1]
                else:
                    i += 1
            if j == len(needle):
                return i-j
        return -1
