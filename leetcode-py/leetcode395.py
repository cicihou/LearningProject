from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        method 1 Brute Force
        Time Limit Exceeded

        time O(n^2)
        Space O(1)
        '''
        def is_valid(counts):
            for i in counts:
                if 0 < i < k:
                    return False
            return True

        if not s or k > len(s):
            return 0

        n = len(s)
        res = 0
        for start in range(n):
            counts = [0] * 26
            for end in range(start, n):
                counts[ord(s[end]) - ord('a')] += 1
                if is_valid(counts):
                    res = max(res, end-start+1)
        return res


        ''' 
        method 2
        brilliant divide and conquer
        '''
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))
        return len(s)


        '''
        method 3
        sliding window
        https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/1041531/Python-Sliding-Window-Solution
        '''
        # TODO


s = Solution()
s.longestSubstring('aaabb', 3)
s.longestSubstring('aaanfjkebnfued', 2)
s.longestSubstring('bbaaacbd', 3)
