class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        time: O(n)
        space: O(n)
        :param nums:
        :return:
        '''
        hashset = {}
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset[num] = None
        return False
