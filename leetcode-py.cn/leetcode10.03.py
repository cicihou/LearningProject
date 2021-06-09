'''
https://leetcode-cn.com/problems/search-rotate-array-lcci/

面试题 10.03. 搜索旋转数组
搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

示例1:

 输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
 输出: 8（元素5在该数组中的索引）

示例2:

 输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
 输出：-1 （没有找到）
提示:
arr 长度范围在[1, 1000000]之间
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2

            # the first half is ordered
            if nums[l] < nums[mid]:
                # target is in the first half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            elif nums[l] > nums[mid]:
                # target is in the second half
                if nums[mid] < target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] == nums[mid]:
                if nums[l] != target:
                    l += 1
                else:
                    # l is the return value now, r = l - 1 will break the loop
                    r = l - 1

        return l if l < len(nums) and nums[l] == target else -1
