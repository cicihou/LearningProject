'''
题解：https://github.com/azl397985856/leetcode/blob/master/problems/768.max-chunks-to-make-sorted-ii.md

方法一：计数分桶（参考 769）
方法二：单调栈
'''


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        method 1 分桶计数

        分桶计数核心：
        如果两个数组的计数信息是一致的，那么两个数组排序后的结果也是一致的

        因此我们用排序过的数组，跟原本的数组相比较，来判断是否可以分块
        '''
        res = 0
        cache = {}
        cache2 = {}
        for i, j in zip(arr, sorted(arr)):
            cache[i] = cache.get(i, 0) + 1
            cache2[j] = cache2.get(j, 0) + 1
            if cache == cache2:
                res += 1
        return res

        '''
        method 2 分桶计数 - 优化写法
        代码：https://leetcode.com/problems/max-chunks-to-make-sorted-ii/discuss/113465/JavaPython-Easy-and-Straight-Froward
        '''

        res, s1, s2 = 0, 0, 0
        for a, b in zip(arr, sorted(arr)):
            s1 += a
            s2 += b
            res += s1 == s2
        return res

        '''
        method 3
        monostack
        '''
        # TODO
