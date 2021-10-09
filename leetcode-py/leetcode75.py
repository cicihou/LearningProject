class Solution(object):
    def sortColors(self, nums):
        ''' method 1 bubble sort

        time: O(n^2)
        space: O(1)
        '''
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

        '''
        method 2 
        
        实质上是 Dutch National Flag 问题
        link: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        
        初始化两个指针 l, r 分别指向最左和最右
        用 cur 遍历：当 nums[cur] 对应的值为 0 时，将 cur 跟 l 交换，右移 cur 和 l 
                    当 nums[cur] 对应的值为 2 时，将 cur 跟 r 交换，左移 r
                    当 nums[cur] 对应的值为 1 时，将 cur 右移即可
        '''
        l = cur = 0
        r = len(nums) - 1
        while cur <= r:
            if nums[cur] == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                cur += 1
                l += 1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            elif nums[cur] == 1:
                cur += 1

        '''
        method 3 internal function
        '''
        from collections import Counter
        return sorted(Counter(nums).elements())


s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0, 0, 2, 2]))
