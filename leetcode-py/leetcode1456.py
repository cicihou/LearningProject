import collections


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ''' sliding window
        time O(n)
        space O(k)
        '''
        vowels = 'aeiou'
        res = 0
        count = 0
        window = collections.deque()
        for i in range(len(s)):
            window.append(s[i])
            if s[i] in vowels:
                count += 1
            if len(window) > k:
                tmp = window.popleft()
                if tmp in vowels:
                    count -= 1
            res = max(res, count)
            # 这里可以再加一个小优化，当 res 达到最大值，提前进行返回
            # if res == k:
            #     return res
        return res
