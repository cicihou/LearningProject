class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' method 1
        API calling, O(n)
        '''
        if target in nums:
            return nums.index(target)
        else:
            return -1

        ''' method 2
        Binary Search, O(logN)
        
        若 nums[l] <= nums[mid]，说明左半边是有序数组
            那么若 target 在有序数组中，收缩 r
            否则 收缩 l（target 在 另一半）
        另一半同理
        
        总之就是判断 target 在不在有序数组中
        '''
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[right]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
