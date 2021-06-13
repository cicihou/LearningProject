class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        BF
        the same to 349
        """
        li = []
        for i in nums1[:]:
            if i in nums2:
                li.append(i)
                nums1.remove(i)
                nums2.remove(i)
        return li


        '''
        method 2
        two pointer + sort
        the same to 349 
        '''
        nums1.sort()
        nums2.sort()

        p1 = p2 = 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res


        '''
        method 3 hashmap
        '''
        res = []
        dic = {}
        for i in nums1:
            dic[i] = dic.get(i, 0) + 1
        for j in nums2:
            if j in dic and dic[j] > 0:
                res.append(nums2[j])
                dic[j] -= 1
        return res


s = Solution()
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(s.intersect(nums1 = [0,0,0], nums2 = [9,4,9,8,4,5,0,1,0]))
