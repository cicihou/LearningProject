class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # the first-two-IF-condition is to decrease time when boundary condition
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if needle not in haystack:
            return -1
        return haystack.index(needle)
