class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # method 1 list iteration
        # return [int(j) for j in str(int(''.join([str(i) for i in num])) + k)]

        # method 2, same as method 1, use for-loop explicitly to analyze the complexity
        # as following, the time complexity is O(n)
        # the space complexity is O(1)
        res = []
        for i in num:
            res.append(str(i))
        res = str(int(''.join(res)) + k)
        res = [int(i) for i in res]
        return res
