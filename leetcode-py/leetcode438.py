from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        ''' method 1 '''
        counter = Counter(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i:i + len(p)]) == counter:
                res.append(i)
        return res

        ''' method 2 
        much more faster than method 1
        time: O(n)
        space: O(n)
        
        我们比较两个 hashmap 理论上来说应该是 O(n)，但是由于本题的 hashmap 最多只会有 26 个字母，所以是 O(1)
        '''
        counter = Counter(p)
        res = []

        tmp = Counter(s[:len(p)])

        for i in range(len(p), len(s)+1):
            if tmp == counter:
                res.append(i-len(p))
            if i == len(s):
                return res

            # modify the tmp
            tmp[s[i-len(p)]] -= 1
            tmp[s[i]] = tmp.get(s[i], 0) + 1
            if tmp[s[i-len(p)]] == 0:
                tmp.pop(s[i-len(p)])
        return res


s = Solution()
s.findAnagrams('abab', 'ab')
