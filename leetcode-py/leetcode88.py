from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        two-pointer，逆向双指针，从 nums1 的尾部开始，这样无需额外的空间
        time: O(n)
        space: O(1)
        """
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return
        p1 = m - 1
        p2 = n - 1
        for i in range(len(nums1) - 1, -1, -1):
            if p1 == -1:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[i] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
