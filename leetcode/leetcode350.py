class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        li = []
        for i in nums1[:]:
            if i in nums2:
                li.append(i)
                nums1.remove(i)
                nums2.remove(i)
        return li


s = Solution()
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(s.intersect(nums1 = [0,0,0], nums2 = [9,4,9,8,4,5,0,1,0]))