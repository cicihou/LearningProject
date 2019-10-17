class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # li = []

        count = 0
        if s == '':
            return 0

        for i, letter in enumerate(s):
            li = [letter]
            # dic = {}
            for j in s[i+1:]:
                if j not in li:
                    li.append(j)
                else:
                    break
            count = max(count, len(li))

        return count

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
