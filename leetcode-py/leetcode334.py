class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        '''先往数组添加了较大数的时候，判断就会失误'''
        # if len(nums)< 3:
        #     return False
        #
        # li = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i] > li[len(li)-1] and nums[i] > nums[i-1]:
        #         li.append(nums[i])
        #     if len(li) >= 3:
        #         return True
        # return False

        '''m2'''
        # if len(nums)< 3:
        #     return False
        #
        # for i in range(1, len(nums)):
        #     li = [nums[i-1]]
        #     for j in range(i, len(nums)):
        #         if nums[j] > nums[j-1] and nums[j] > li[len(li)-1]:
        #             li.append(nums[j])
        #         if len(li) >= 3:
        #             return True
        # return False

        '''m3'''
        '''用 min 行不通'''
        # if len(nums)< 3:
        #     return False
        #
        # for i in range(1, len(nums)):
        #     li = [nums[i-1]]
        #     for j in range(i, len(nums)):
        #         min_num = min(nums[j:len(nums)])
        #         last_num = li[len(li)-1]
        #         if min_num > last_num and nums.index(min_num) > nums.index(last_num):
        #             li.append(min_num)
        #         if len(li) >= 3:
        #             return True
        # return False


        '''m4  leetcode 大神解法，有点小学运算的味道'''
        min_num = middle_num = float('inf')
        for i in nums:
            if i <= min_num:
                min_num = i
            elif i <= middle_num:
                middle_num = i
            else:
                return True
        return False


s = Solution()
print(s.increasingTriplet([1, 2, 3, 4, 5]), 't')
print(s.increasingTriplet([1, 2, 2, 1, 1]), 'f')
print(s.increasingTriplet([1, 2, ]), 'f')
print(s.increasingTriplet([1, 2, 0,1,2,4,312,4,3]), 't')
print(s.increasingTriplet([1, 2,52342,5234,223,4 ]), 't')
print(s.increasingTriplet([5,4,3,2,1]), 'f')
print(s.increasingTriplet([2,1,5,0,3]),'f')
print(s.increasingTriplet([2,5,3,4,5]),'t')
print(s.increasingTriplet([5,1,5,5,2,5,4]),'t')
print(s.increasingTriplet([1,2,3,1,2,1]),'t')