class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        method 1 从 lc 118 而来，计算出整个 triangle
        :param rowIndex:
        :return:
        '''
        res = []
        for i in range(1, rowIndex+2):
            cur = [1] * i
            if i > 2:
                for j in range(1, i-1):
                    cur[j] = res[-1][j] + res[-1][j-1]
            res.append(cur)
        return res[rowIndex]

        '''
        method 2
        不保存 triangle，只计算最后一行
        '''
        res = []
        for i in range(rowIndex+1):
            if i < 2:
                res.append(1)
            else:
                res = [1] + [res[j] + res[j-1] for j in range(1, i)] + [1]
        return res
