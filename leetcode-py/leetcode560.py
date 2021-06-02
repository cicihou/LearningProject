class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        method 1 brute force
        time limit exceed
        '''
        # count = 0
        # for i in range(len(nums)):
        #     s = nums[i]
        #     if s == k:
        #         count += 1
        #     for j in range(i + 1, len(nums)):
        #         s += nums[j]
        #         if s == k:
        #             count += 1
        # return count

        '''
        method 2
        prefix sum 前缀和 via hash map
        过程如下：
            1. 将 数组 累计的和 算出来
            2. e.g. 数组 [3, 4,  7,  2, -3,  1,  4,  2]
 从左遍历 累计求和的结果为 [3, 7, 14, 16, 13, 14, 18, 20], 
            这种解法 left-sum，又称为 prefix sum
          if i != 0, sum[i, j] = left_sum[j] - left_sum[i-1]
          if i == 0, sum[i, j] = left_sum[j]
        但是光是这样还是需要在前缀和中进行 O(n^2) 的遍历，因为 i,j 可以是任何位置
            for i in range(len(prefix_sum)):
                for j in range(len(prefix_sum)):
                    if i == 0 and left_sum[j] == k:
                        count += 1
                    elif left_sum[j] - left_sum[i-1] == k:
                        count += 1

        那么如何将其优化成 O(n) 呢？
        初始化 hashmap，k-v 存储的是前缀和的值以及它们出现的次数
        进行一次遍历
        当 前缀和[current] - k 对应的值在 hashmap 中已经存在的时候，就表示表示当前存在一个前缀和的子数组
        比如说 [2, -2 , 0], k = 0，前缀和是 prefix_sum = [2, 0, 0]，
            prefix_sum[0] 的时候，{2: 1}
            prefix_sum[1] 的时候，{0: 1}
            prefix_sum[2] 的时候，{0: 2}
        
        注意一下这个 count += 1 逻辑   
            1.
            当前缀和 == k 的时候，count += 1
            
            2.             
            当 前缀和 减去 前一个数 为 k 的时候 -> 
            当 前缀和 - k 为前一个数当值时 -> 
            当 前缀和 -k 的值已经存在于 hashmap 中的时候，则 count += prefix_sum[s-k]
            
            note:
            prefix[s] 每个循环自增 1

        （想不明白的时候可以看一下这个视频 https://www.youtube.com/watch?v=HbbYPQc-Oo4）
        '''
        count = 0
        prefix_sum = {}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s == k:
                count += 1
            if s-k in prefix_sum:
                count += prefix_sum[s-k]
            prefix_sum[s] = prefix_sum.get(s, 0) + 1
        return count


s = Solution()
print(s.subarraySum(nums=[1, 1, 1], k=2))
