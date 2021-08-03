from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        method 1 hashmap
        :param nums:
        :return:
        '''
        counter = Counter(nums)
        most_common = counter.most_common(1)[0][0]
        res = [most_common]
        for i in range(1, len(nums)+1):
            if i not in counter:
                res.append(i)
                return res

        '''
        method 2 array
        
        time: O(N)
        space: O(N)
        '''
        n = len(nums)
        array = [0] * n

        for num in nums:
            array[num - 1] += 1
        return [array.index(2) + 1, array.index(0) + 1]
