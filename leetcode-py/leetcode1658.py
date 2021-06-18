class Solution:
    def minOperations(self, nums, x: int) -> int:
        '''
        sliding window
        time: O(n)
        space: O(1)

        实质上是 find the maximum subarray.
        题目要求用最小的操作截取出左右两段的数，使其和 == x
        相当于找到最长的连续子数组，使其和为 target = sum(nums) - x
                由于找的子数组务必是连续，所以可以使用 window，进行一次遍历
                当 window 中的值 > target 时，将 left 向右移动
                当 window 中的值 < target 时，将 right 向右移动
            right 走到终点后，全部满足 sum(window) == target 中，找到 window 的 max_length
        这样找到最长的连续子数组，用 len(nums) - window_mac_length 得到的就是最短的要操作的结果
        '''
        target = sum(nums) - x
        if target < 0:
            return -1
        elif target == 0:
            # 这里的剪枝成立是因为 constraints nums[i] > 0
            return len(nums)

        l = total = res = 0
        for i in range(len(nums)):
            total += nums[i]
            while total > target:
                total -= nums[l]
                l += 1
            if total == target:
                res = max(res, i - l + 1)
        return len(nums) - res if res > 0 else -1


s = Solution()
s.minOperations([1,1,4,2,3], 5)
s.minOperations([3,2,20,1,1,3], 10)
