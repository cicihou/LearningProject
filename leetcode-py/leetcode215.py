class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)-k]

        '''
        heap
        python 中的 heapq 就是小顶堆
        https://leetcode-solution.cn/solutionDetail?type=3&id=77&max_id=2
        '''
        size = len(nums)
        h = []
        for index in range(k):
            heapq.heappush(h, nums[index])

        for index in range(k, size):
            if nums[index] > h[0]:
                heapq.heapreplace(h, nums[index])
        return h[0]

        '''
        method 3 heap 的更加简单的写法
        '''
        heapify(nums)
        x = len(nums) - k
        for _ in range(x):
            heappop(nums)
        else:
            return heappop(nums)


# 第kth大，非去重
s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], k=2), 5)
print(s.findKthLargest([-1, -1], k=2), -1)
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)
print(s.findKthLargest([2,1], 2), 1)
