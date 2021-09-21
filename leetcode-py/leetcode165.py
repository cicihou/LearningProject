from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        method 1 字符串操作

        小数点表示小版本，小版本前面 0 的位数不影响版本号的大小

        time: O(n+m)
        space: O(n+m)
        '''
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            i1, i2 = int(v1), int(v2)
            if i1 > i2: return 1
            if i1 < i2: return -1
        return 0

        '''
        method 2 two-pointer
        
        代码：https://leetcode-cn.com/problems/compare-version-numbers/solution/bi-jiao-ban-ben-hao-by-leetcode-solution-k6wi/
        '''
        # TODO
