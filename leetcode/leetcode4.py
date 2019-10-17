class Solution:
    def findMedianSortedArrays(self, nums1,nums2):
        if not nums1 or not nums2:
            if not nums1:
                nums1 = nums2
        else:
            nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 0:
            print(nums1[len(nums1) // 2 - 1],111)
            print(nums1[len(nums1) // 2],111)
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        else:
            return nums1[len(nums1) // 2]


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]), '2.0')
print(s.findMedianSortedArrays([1, 3], []), '2.0')
print(s.findMedianSortedArrays([1, 3, 4, 5], []), '3.5')