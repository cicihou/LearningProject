class Solution:
    def fib(self, n: int) -> int:
        '''
        本题跟 70 题一模一样！
        本题方法还有很多，详见：https://leetcode.com/problems/fibonacci-number/solution/

        method 1 直接递归，不会超时
        '''
        if n in [0, 1]:
            return n
        return self.fib(n-1) + self.fib(n-2)

        '''
        method 2 memoize
        '''
        if n in [0, 1]:
            return n
        nums = [0, 1]
        for i in range(2, n+1):
            nums.append(nums[i-1] + nums[i-2])
        return nums[-1]
