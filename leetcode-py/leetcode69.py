''' 二分查找法 '''
class Solution(object):
    def mySqrt(self, x):
        '''
        time O(logN)
        space O(1)
        找 满足 mid ^ 2 <= x < (mid + 1) ^ 2 的值，返回 mid
        若不满足，当 x < mid ^ 2 的时候，将 右指针 r 移到 mid 左边
           其他时候 x > mid ^ 2 的时候，将 左指针 l 移到 mid 右边
        '''
        l, r = 0, x
        if x == 1:
            return 1
        while l <= r:
            # 注意这里最好用整除，不然无法整除的可能会带来 overflow
            # 虽然 python 可以自动处理 BIGINTERGER 的溢出
            mid = l + (r-l)//2
            if mid ** 2 <= x < (mid+1) ** 2:
                return mid
            elif x < mid ** 2:
                r = mid - 1
            else:
                l = mid + 1


        ''' python 就是生产力法 '''
        # from math import sqrt
        # return int(sqrt(x))

        ''' binary seach 
        i.e. 找 ans >= x 时，x 的最小值
        当 l <= r 时，
            mid 是 l + r 的中点
            当 mid ** 2 小于等于 x，mid 可能为 ans，将 l 移到中点右边
            当 mid ** 2 大于 x，将 r 移到中点左边
        '''
        l, r = 0, x
        while l <= r:
            mid = (l+r) // 2
            if mid ** 2 <= x:
                ans = mid
                l = mid + 1
            elif mid ** 2 > x:
                r = mid - 1
        return ans
