class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        method 1

        time: O(nlogn)
        space: O(1)
        '''
        return sorted(s) == sorted(t)

        '''
        method 2
        
        time: O(n)
        space: O(n)
        '''
        cache1 = {}
        cache2 = {}
        for ch1, ch2 in zip_longest(s, t):
            cache1[ch1] = cache1.get(ch1, 0) + 1
            cache2[ch2] = cache2.get(ch2, 0) + 1
        return cache1 == cache2
