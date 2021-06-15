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
        much more faster than method 1'''
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
