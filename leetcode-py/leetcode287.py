class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        method 1: set
        time O(n)
        space O(n)
        '''
        dic = set()
        for i in nums:
            if i not in dic:
                dic.add(i)
            else:
                return i

        '''
        method 2: fast slow pointer
        参考 142 linked list
        time O(n)
        space O(1)
        https://leetcode.com/problems/find-the-duplicate-number/solution/
        这个方法能奏效是因为 constraint ：列表长度必须跟 n + 1 相等
        也就是说，用 n 做 index 不允许发生溢出
            1 <= n <= 105
            nums.length == n + 1
            1 <= nums[i] <= n
        这个想法有点意思
        '''
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast
