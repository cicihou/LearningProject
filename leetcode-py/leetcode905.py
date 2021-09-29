class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd

        '''
        用 sort 也能做，一行代码
        '''
        return sorted(nums, key=lambda x: x%2 != 0)
