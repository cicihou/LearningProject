class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        跟 78 一模一样，多了一步排序和去重（一定要排序 不然 tuple(1,2) 和 tuple(2,1) 不会被视为重复）
        '''
        res = set()
        path = []

        def backtrack(nums, path, start):
            # 注意：其实 nums 这个参数不带也行，从头到尾我们也没修改过 nums
            res.add(tuple(path[:]))
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(nums, path, i+1)
                path.pop()

        nums.sort()
        backtrack(nums, path, 0)
        return res
