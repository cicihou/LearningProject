class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        跟 153 大致类似
        本质也是在找旋转点
        '''
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # nums[mid] > nums[r] 表示有序数组在左边，旋转点在右侧，收缩左空间范围到 mid
            if nums[mid] > nums[r]:
                l = mid + 1
            # nums[mid] <= nums[r] 表示有序数组在右边，旋转点在左边
            else:
                # 若最右边的点和中间的点不相等，收缩 r 到中间点 mid
                if nums[r] != nums[mid]:
                    r = mid
                # 若最右边点和中间点相等是，r -= 1, 缩小一个值，to handle duplicate
                # 这里用 nums[l] 来判断， l += 1 效果也一样的，总之就是跳过重复的值
                else:
                    r -= 1
        return nums[l]
