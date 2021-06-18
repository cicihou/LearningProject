from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ''' tricky internal method '''
        return list(permutations(nums))

    def permute2(self, nums: List[int]) -> List[List[int]]:
        ''' backtracking
        视频：https://www.youtube.com/watch?v=KukNnoN-SoY
        代码，以及回溯的另一种写法：https://github.com/azl397985856/leetcode/blob/master/problems/46.permutations.md
        '''
        res = []
        def backtrack(nums, ans):
            if len(nums) <= 0:
                res.append(ans)
            else:
                for num in nums:
                    # 注意这里需要拷贝，并且不能占用原来的变量名，不然之后的循环会出问题
                    growing_ans = ans[:]
                    growing_ans.append(num)

                    remain = nums[:]
                    remain.remove(num)
                    backtrack(remain, growing_ans)
        backtrack(nums, [])
        return res
