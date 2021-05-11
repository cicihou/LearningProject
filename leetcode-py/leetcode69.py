''' 二分查找法 '''
class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        if x == 1:
            return 1
        while l <= r:
            # 注意这里最好用整除，不然无法整除的可能会带来 overflow
            # 虽然 python 可以自动处理 BIGINTERGER 的溢出
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1


''' python 就是生产力法 '''
        # from math import sqrt
        # return int(sqrt(x))
