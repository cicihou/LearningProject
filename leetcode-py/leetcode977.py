class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        跟 lc 88 一模一样

        two-pointer 记录负数和正数的交界
        （pos 是最小的正数所在index, neg 是最大的负数所在的 index）
        note: pos != len(nums) - 1，否则全是负数的时候，会在最后一次循环 overflow
        [-1,-2], if our statement is pos < len(nums)
        nums[0] < 0 and 0 < 2, pos = 1
        nums[1] < 0 and 1 < 2, pos = 2
        nums[2] 这时候就产生了 overflow


        if neg == -1：说明数组没有负数
        if pos == len(nums): 说明数组没有正数
        else: 有正有负，我们通过比较绝对值的大小来确定正数和负数谁的 square 大

        time: O(N)
        space: O(N)
        '''
        res = []
        pos = 0
        while nums[pos] < 0 and pos < len(nums) - 1:
            pos += 1
        neg = pos - 1
        while len(res) < len(nums):
            if neg == -1:
                res.append(nums[pos] ** 2)
                pos += 1
            elif pos == len(nums):
                res.append(nums[neg] ** 2)
                neg -= 1
            elif abs(nums[pos]) < abs(nums[neg]):
                res.append(nums[pos] ** 2)
                pos += 1
            else:
                res.append(nums[neg] ** 2)
                neg -= 1
        return res

        '''
        method 2
        
        time: O(NlogN)
        space: O(N)
        '''
        return sorted(x**2 for x in nums)
