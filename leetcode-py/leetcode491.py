class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
        backtracking，类似于 lc 78/90
        :param nums:
        :return:
        '''
        res = set()
        path = []

        def backtrack(nums, path, start):
            if len(path) > 1:
                res.add(tuple(path[:]))

            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    backtrack(nums, path, i + 1)
                    path.pop()

        backtrack(nums, path, 0)
        return res
