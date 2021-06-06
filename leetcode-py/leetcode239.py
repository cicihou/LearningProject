class Solution:
    def maxSlidingWindow(self, nums, k):
        ''' method 1 brute force, TimeLimitExceed now'''
        if not nums:
            return []
        res = []
        for i in range(len(nums)):
            if i + k <= len(nums):
                res.append(max(nums[i:i+k]))
        return res

        ''' method 2 deque 
        单调队列 + 滑动窗口，只存储符合要求的单调递增元素
        time complexity O(n)  n 是数组长度
        space complexity O(k)  k 是参数
        '''
        q = collections.deque()
        ans = []
        for i in range(len(nums)):

            # 将deque[-1] 对应的值和 nums[i] 比较，
            # 保证 deque[-1] 中的 index 始终是对应的最大的元素
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # 保证 deque 中的第一个元素始终是 sliding window 里面的数
            while q and i - q[0] >= k:
                q.popleft()

            q.append(i)
            # 保证 res 添加的是 sliding window 生成后，对应的 deque 中最大的元素
            # 经过前面两个 while，q 中有且只有最大的元素
            # 注意 q 里面存的只是 index，
            if i >= k - 1:
                ans.append(nums[q[0]])
            return ans

s = Solution()
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
