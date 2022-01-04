class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ''' method 1

        time: O(m+n)，如果算上内置 sort 方法的话应该是 (m+n)*log(m+n)
        space: O(m+n)
        '''
        nums1.extend(nums2)
        nums1.sort()
        mid = len(nums1) // 2
        if len(nums1) % 2:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid-1]) / 2


        ''' method 2
        binary search
        
        code: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
        video: https://www.youtube.com/watch?v=LPFhl65R7ww&t=12s
        
        time: O(log(m+n))
        space: O(1)
        '''
        # TODO


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]), '2.0')
print(s.findMedianSortedArrays([1, 3], []), '2.0')
print(s.findMedianSortedArrays([1, 3, 4, 5], []), '3.5')
