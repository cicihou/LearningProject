from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        method 1 backtrack 操作指针
        板子题，常记常复习

        time: 这个挺复杂的，不太懂，大致就是优于 O(N * N!)，但差于 O(N!)
        space: O(N!)
        '''
        res = []
        n = len(nums)
        def backtrack(start):
            if start == n:
                res.append(nums[:])
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return res


        ''' method 2 backtrack，操作两个数组
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


        '''
        method 3 
        tricky internal method 
        '''
        return list(permutations(nums))
