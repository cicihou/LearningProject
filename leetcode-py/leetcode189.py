class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        method 1 Brutal Force
        """
        for i in range(k):
            val = nums.pop()
            nums.insert(0, val)

        '''
        method 2
        Using extra array
        time O(n)
        space O(n)
        '''
        n = len(nums)
        a = [0] * n
        for i in (range(n)):
            a[(i+k) % n] = nums[i]
        nums[:] = a

        '''
        method 3
        build a cycle(similar to a Mobius band), tricky method
        '''
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
