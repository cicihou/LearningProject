class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        linear + hashmap
        time O(n)
        space O(n)
        '''
        res = set()

        dic = {k:None for k in nums1}
        for i in nums2:
            if i in dic:
                res.add(i)
        return list(res)


        '''
        two pointer + sort
        time O(n)
        space O(1)
        '''

        res = set()
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        pointer1 = pointer2 = 0
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums2[pointer2] > nums1[pointer1]:
                pointer1 += 1
            elif nums2[pointer2] < nums1[pointer1]:
                pointer2 += 1
            else:
                res.add(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1
        return list(res)
