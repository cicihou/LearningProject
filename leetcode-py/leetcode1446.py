class Solution:
    def maxPower(self, s: str) -> int:
        '''
        method 1
        brute force
        worst time O(n^2)
        '''
        # count = 1
        # for i in range(1, len(s)):
        #     j = 1
        #     if s[i] == s[i - 1]:
        #         while i < len(s) and s[i] == s[i - 1]:
        #             i += 1
        #             j += 1
        #     count = max(count, j)
        # return count

        '''
        method 2
        one pass
        time O(n)
        '''
        count = 0
        max_count = 0
        prev = None
        for cur in s:
            if cur == prev:
                count += 1
            else:
                count = 1
                prev = cur
            max_count = max(max_count, count)
        return max_count
