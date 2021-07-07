class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        跟 lc 88 一模一样
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
