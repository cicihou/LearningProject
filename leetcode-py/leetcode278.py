# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        Time O(logN)
        space O(1)
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        '''
        similar binary search method
            用 left + (right - left) // 2 进行二分，比用 (left + right) // 2 更好
            因为有些语言用后一种方法会 overflow (python 不会)
        '''
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
