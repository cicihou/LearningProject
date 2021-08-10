class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        method 1
        :param numRows:
        :return:
        '''
        res = []
        for i in range(1, numRows + 1):
            if len(res) < i:
                cur = [1] * i
                if i > 2:
                    last = res[-1]
                    for j in range(1, i - 1):
                        cur[j] = last[j - 1] + last[j]
                res.append(cur)

        return res
