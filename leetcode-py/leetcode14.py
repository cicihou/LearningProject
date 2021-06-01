class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        pre1 = list(strs[0])
        for s in strs[1:]:
            for _ in range(len(pre1)):
                temp = ''.join(pre1)
                if s.startswith(temp):
                    break
                pre1.pop()
            if not pre1:
                return ''
        return ''.join(pre1)


s = Solution()
print(s.longestCommonPrefix(["dog", "racecar", "car"]), '')
print(s.longestCommonPrefix(["flower","flow","flight"]), 'fl')
