

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        it requires the index difference is lower than k
        abs(i-j) <= k
        we could use a k-size window to look for abs(nums[i]-nums[j]) <= t in this window

        method 1 Brute Force
        time: O(n*k), TLE
        '''
        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

        '''
        method 2 sliding window + bucket sort
        
        对于任意位置 i，我们都希望其下标范围的 [i-k, i] 中找到值范围在 [nums[i]-t, nums[i]+t] 的数中
        
        题解：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/gong-shui-san-xie-yi-ti-shuang-jie-hua-d-dlnv/
        因此我们可以将 数值进行桶排序，把满足要求的 t 值归为一个桶
        由于题目要求的是 diff <= t 以及整除的特性，我们需要将 size 定为 t + 1
        
        如果当前的桶已经存在，说明前面已经有了 [u-t, u+t]范围的数字，返回 True
        除了当前的桶，我们还需要比较相邻的桶，相邻的桶如果存在满足 <= t 的要求，也是一个有效的返回
        
        如果当前的坐标超过了 k-size window，把上一个值从 bucket 中去掉
        
        time: O(n)
        space: O(k)
        '''
        size = t + 1
        def get_bucket_id(u):
            return u // size

        bucket = {}
        for i, u in enumerate(nums):
            idx = get_bucket_id(u)
            if idx in bucket:
                return True
            l, r = idx - 1, idx + 1
            if l in bucket and abs(u - bucket[l]) <= t:
                return True
            if r in bucket and abs(u - bucket[r]) <= t:
                return True

            bucket[idx] = u

            if i >= k:
                map.pop(get_bucket_id(nums[i-k]))

        return False
