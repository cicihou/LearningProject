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

        '''
        method 3 bit manipulation

        每个元素有两种状态，拿或者不拿，那么如果一共有NN个数，那就一共有 2^N 种可能，也就是有这么多个子集（子集包括全集和空集）。
        既然每一个数只有两种状态，那么我们不妨用一个 bit 来表示。这样题中的[1,2,3]，我们可以看成一个三个比特的组合：
            比如 0 0 0 就代表空集，1 1 1 就代表全集， 1 0 0 就代表[1] (可正可反)。
            这样我们就可以进行位操作，0 - 2^n - 1的数的二进制数位为 1 的位置，就把对应的元素填入集合中。
        PS: ((1 << i )& sign) != 0 的意思是用第 i 位是 1 比特与当前 sign 相与，若结果不为 0 就代表 第 i 位 比是 1
        
        time: O(N * 2^N)
        space: O(N)
        '''

        # 1 << len(nums) means 2 ** len(nums)
        res, end = [], 1 << len(nums)
        for sign in range(end):
            subset = []
            for i in range(len(nums)):
                if ((1 << i) & sign) != 0:
                    subset.append(nums[i])
            res.append(subset)
        return res
