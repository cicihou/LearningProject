class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        method 1 TLE
        这种方法超时了
        :param nums:
        :return:
        '''
        nums.sort()

        def func(nums):
            return nums[0] + nums[1] > nums[2] and abs(nums[0] - nums[1]) < nums[2]

        res = filter(lambda x: x == 1, map(func, combinations(nums, 3)))
        return len([i for i in res])


        '''
        method 2
        
        linear pair
        
        nums 排序后，用三根指针来表示遍历三个数。
            i in [0, len - 2]
            j in [i+1, len-1]
            k in [i+2, len], i+2 会比 j+1 节省时间(j+1 TLE，过不了)
        当 i,j,k 三者指标对应的边满足三角形要求时，k += 1
        当不再满足时，count += k - j - 1 ，得出本次 [i, j] 有多少有效的 k 可以计入 count
        
        time: O(N^2)
        space: O(log N)
        '''
        res = 0
        nums.sort()
        while nums and nums[0] == 0:
            nums.pop(0)

        for i in range(0, len(nums) - 2):
            k = i + 2
            for j in range(i+1, len(nums)-1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1
        return res
