class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        hashmap
        '''
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] in dic:
                return [dic[numbers[i]], i+1]
            else:
                dic[target - numbers[i]] = i + 1

        '''
        two pointer
        '''
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]
