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


        '''
        binary search
        time O(nlogn)
        遍历数组，target - 当前遍历的值，就是需要寻找的值
        用二分在当前数组的右侧寻找另一个满足条件的值
        
        二分 在本题 并不是优解
        '''
