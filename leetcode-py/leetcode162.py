class Solution(object):
    def findPeakElement(self, nums):
        '''
        method 1
        time O(n)
        '''
        if nums:
            return nums.index(max(nums))
        else:
            return 0

        '''
        method 2
        Time: O(n)
        Intuitive Solution
        '''
        for i in range(1, len(nums)):
            if not nums[i] > nums[i-1]:
                return i-1
        return len(nums) - 1

        '''
        method 3
        binary search

        time O(logN)
        二分查找处理的是有序数列，我们可以将 Nums 视作交替的升序/降序数列。
        
        首先找到中点 mid，
        
        若 mid 正好处于某一个降序序列中（nums[mid] > nums[mid+1]），说明峰值会出现在左边
        因此 r = mid（包括其本身），搜索空间缩小为 [left, mid]
        
        若 mid 正好处于某一个升序序列中（nums[mid] > nums[mid+1]），说明峰值会出现在右边
        因此搜索空间缩小为[mid+1, right]
        
        就这样，我们不断地缩小搜索空间，直到搜索空间中只有一个元素，该元素即为峰值元素
        '''
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
