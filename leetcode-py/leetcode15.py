class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        method 1 brute force, time limit exceed
        不可用的解法
        '''
        # if len(nums) <= 2:
        #     return
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if i != j != k and nums[i] + nums[j] + nums[k] == 0:
        #                 tripet = sorted([nums[i], nums[j], nums[k]])
        #                 if tuple(tripet) not in res:
        #                     res.append(tuple(tripet))
        # return [list(r) for r in res]


        ''' method 2 hash, from 2-sum solution'''
        if len(nums) <= 2:
            return
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            dic = {}
            target = -nums[i]
            for j in range(1+i, len(nums)):
                if not nums[j] in dic:
                    dic[target - nums[j]] = j
                else:
                    # 不需要用 sort, 由于我们前面排序过，这里必然是 nums[i] < dic[target - nums[j]] < nums[j]
                    res.add(tuple([nums[i], -nums[i]-nums[j], nums[j]]))
        return map(list, res)


        ''' method 3 
        
        https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated
        将 数根据 负数、0、正数分成三个区间，分别遍历处理
        '''
