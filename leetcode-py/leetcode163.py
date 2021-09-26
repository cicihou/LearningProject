class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                res.append([nums[i - 1] + 1, nums[i] - 1])

        if len(nums) > 0:
            res.insert(0, [lower, nums[0] - 1])
            res.append([nums[-1] + 1, upper])
        else:
            res.append([lower, upper])

        ans = []
        for r in res:
            # if r[0] == r[1]:
            #     ans.append(str(r[0]))
            # elif r[1] > r[0]:
            #     ans.append(str(r[0]) + '->' + str(r[1]))
            if r[1] >= r[0]:
                ans.append('->'.join(str(i) for i in sorted(list(set(r)))))
        return ans
