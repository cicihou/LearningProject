class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle and not haystack:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

'''
注意空字符串会判定成存在于任意字符串
>>> "" in "a"
True
>>> "a".index("")
0
'''
