class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        注意 path 添加的必须是深拷贝，以免后面答案添加之后影响到 res 中的 path
        '''
        res = []
        path = []

        def backtrack(nums, path, start):
            # 注意：其实 nums 这个参数不带也行，从头到尾我们也没修改过 nums
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(nums, path, i+1)
                path.pop()

        backtrack(nums, path, 0)
        return res

        '''
        method 2
        '''
        res = [[]]
        for num in nums:
            res += [cur + [num] for cur in res]
        return res
