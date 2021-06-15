class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ''' method 1 '''
        nums1.extend(nums2)
        nums1.sort()
        mid = len(nums1) // 2
        if len(nums1) % 2:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid-1]) / 2


        ''' method 2
        binary search
        https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
        '''
        # TODO


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]), '2.0')
print(s.findMedianSortedArrays([1, 3], []), '2.0')
print(s.findMedianSortedArrays([1, 3, 4, 5], []), '3.5')
