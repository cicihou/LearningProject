from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        time: O(n)
        space: O(n)
        '''
        res = defaultdict(lambda: 0)
        for num in nums:
            res[num] += 1
        return [k for k, v in res.items() if v == 1]

        '''
        method 2 bit manipulation
        time: O(n)
        space: O(1)
        
        xor 的性质
        0 xor 1 = 1
        1 xor 1 = 0
        0 xor 0 = 0
        1 xor 0 = 1
        
        两个数不同的时候，xor 结果为1， 两个数相同，xor 为 0
        
        a xor b = b xor a
        a xor a = 0
        
        题目中，有且仅有两个数出现一次。我们将数组分为两部分，进行分治
        
        '''
        xor = 0
        for num in nums:
            xor ^= num

        mask = 1
        while mask & xor == 0:
            mask *= 2

        res = [0, 0]
        for num in nums:
            if num & mask == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
