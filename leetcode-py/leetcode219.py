class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        method1: hashmap
        time: O(n)
        space: O(n)
        '''
        hashset = {}
        for i in range(len(nums)):
            if nums[i] in hashset and abs(hashset[nums[i]] - i) <= k :
                return True
            else:
                hashset[nums[i]] = i
        return False

        '''
        method 2 sliding window
        '''
        # TODO
