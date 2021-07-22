class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        '''
        method 1
        找到 左半边最大值 会小于 右半边最小值的数组分界点，并且这个数组的左半边要尽可能小

        创建两个数组，一个存数组遍历从左起的左半边最大值，一个存数组遍历从右起的右半边最小值
        找到 第一个 leftMax[i-1] <= rightMin[i] 的交界点，返回 i

        https://leetcode.com/problems/partition-array-into-disjoint-intervals/solution/

        time: O(n), 3n is n
        space: O(n), 2n is n
        '''
        leftMax = [nums[0]]
        rightMin = [nums[-1]]
        for num in nums[1:]:
            leftMax.append(max(num, leftMax[-1]))
        for num in nums[len(nums) - 2::-1]:
            rightMin.insert(0, min(num, rightMin[0]))
        print(leftMax, rightMin)
        for i in range(1, len(nums)):
            if leftMax[i - 1] <= rightMin[i]:
                return i


        '''
        method 2 two-pass solution
        https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/197987/Python-solutions-3-passes-greater-2-passes-greater-1-pass-straight-forward
        
        用变量代替 leftMax 数组
        
        建立 right 数组
        将 minRight 逐个添加进 right 数组
        
        遍历数组时，动态获取 leftMax 并 判断 left <= right[i+1]
        '''
        right = [nums[-1]] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            right[i] = min(right[i+1], nums[i])

        left = 0
        for i in range(len(nums)-1):
            left = max(left, nums[i])
            if left <= right[i+1]:
                return i+1
