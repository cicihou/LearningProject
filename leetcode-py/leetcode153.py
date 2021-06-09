class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        method 1
        binary search

        这个问题实质上就是要找有序数组的最小值
            若 nums[l] < nums[r] 则表示一定就是有序数组，此时返回 nums[l]
            其他的步骤都是为了收缩范围，逼近有序数组
            当 nums[mid] > nums[r]，说明有序数组在左侧，那么旋转过后的最小数组就一定在右侧，收缩左区间 l = mid + 1
            否则，有序数组在右侧，那么 r = mid （注意 不能是 mid - 1），因为旋转数组存在转折点，并不能保证整体有序，mid - 1 可能会漏一个范围点
        '''
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                # 数组达成整体有序，必然是更小的那个数组
                return nums[l]
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

        '''
        method 2 binary search
        比较 nums[mid] 和 nums[0]
            if nums[mid] > nums[0]，在 数组右边搜索
            if nums[mid] < nums[0]，在 数组左边搜索
        核心是为了找到数组的旋转点，因为旋转点必定是最小的那个点
        if nums[mid - 1] > nums[mid]: return nums[mid]
        if nums[mid] > nums[mid + 1]: return nums[mid+1]
        '''
        l = 0
        r = len(nums) - 1

        if len(nums) == 1 or nums[r] > nums[l]:
            return nums[0]

        while l < r:
            mid = l + (r-l)//2

            # 找到旋转点之后，返回旋转点
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
