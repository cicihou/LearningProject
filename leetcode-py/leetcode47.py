class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        跟 46 题一模一样

        也有另一种去重方式
        nums.sort() 整体排序后
        在循环中跳过前后相同的数字产生的循环，这样同一个数字就只会用一次
        if i > 0 and nums[i] == nums[i-1]:
            continue
        代码：https://github.com/azl397985856/leetcode/blob/master/problems/47.permutations-ii.md

        当然也可以继续 用 permutations internal tool 生成之后去重
        '''
        res = set()

        def backtrack(nums, ans):
            if len(nums) <= 0:
                res.add(tuple(ans))
            else:
                for num in nums:
                    remain = nums[:]
                    remain.remove(num)

                    growing_ans = ans[:]
                    growing_ans.append(num)

                    backtrack(remain, growing_ans)
        backtrack(nums, [])
        return res
