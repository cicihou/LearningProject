class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        bubble sort
        冒泡排序
        TLE
        :param nums:
        :return:

        time: O(n^2)
        space: O(1)
        '''
        for j in range(len(nums)-1, 0, -1):
            for i in range(j):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

        '''
        merge sort
        归并排序
        
        time: O(nlogn)
        '''

        def merge_sort(l):
            if len(l) <= 1:
                return l
            i = len(l) // 2
            left = merge_sort(l[:i])
            right = merge_sort(l[i:])
            return merge(left, right)

        def merge(left, right):
            l, r = 0, 0
            res = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            res += left[l:] or right[r:]
            return res

        return merge_sort(nums)
