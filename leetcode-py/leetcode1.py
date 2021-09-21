class Solution:
    def twoSum(self, nums, target: int) -> list:
        '''
        method 1 brute force
        time O(n^2)
        space O(1)
        '''
        for i in range(len(nums)):
            for j in range(min(i + 1, len(nums) - 1)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]


        '''
        method 2 hashmap
        time O(n)
        space O(n)
        '''
        dic = {}
        for i in range(len(nums)):
            if not nums[i] in dic:
                dic[target - nums[i]] = i
            else:
                return [i, dic[nums[i]]]


        '''
        method 3 two-pointer
        https://leetcode.com/problems/two-sum/discuss/662/Python-dictionary-and-two-pointer-solutions.
        '''
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        l, r = 0, len(nums)-1
        while l < r:
            cur = nums[l][1] + nums[r][1]
            if cur == target:
                return [nums[l][0], nums[l][0]]
            elif cur > target:
                r -= 1
            elif cur < target:
                l += 1


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
