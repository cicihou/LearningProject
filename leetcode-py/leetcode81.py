class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        跟 33 完全一致，唯一不同的是在数有重复的时候进行位移

        若 nums[l] <= nums[mid]，说明左半边是有序数组
            那么若 target 在有序数组中，收缩 r
            否则 收缩 l（target 在 另一半）
        另一半同理

        总之就是判断 target 在不在有序数组中
        '''
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # 当 l < mid （index 不想等）但数相等的时候，表示出现了重复的数，将 l 向右位移
            while l < mid and nums[l] == nums[mid]:
                l += 1
            if nums[l] <= nums[mid]:
                # 这边判断 target 的时候就是 跟 l 和 r 沾边的时候要用 =
                # 因为 target != nums[mid]，不然在前面就返回了
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
