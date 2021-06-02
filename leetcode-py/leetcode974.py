class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        prefix sum
        参考 560 的写法
        '''
        count = 0
        s = 0
        prefix_sum = {0: 1}

        for i in range(len(nums)):
            s = (nums[i] + s) % k
            if s in prefix_sum:
                count += prefix_sum[s]
                prefix_sum[s] += 1
            else:
                prefix_sum[s] = 1
        return count


        '''
        method 2
        老实说我也不太理解这个写法：https://www.youtube.com/watch?v=u9m-hnlcydk
        但是能通过，还挺快的
        '''
        counts = [0] * k
        s = 0
        for num in nums:
            s += (num % k + k) % k
            counts[s % k] += 1
        res = counts[0]
        for c in counts:
            res += (c*(c-1)) // 2
        return res
