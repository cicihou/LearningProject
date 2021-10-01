'''
这题题意有点难懂，一个 length 为 n 的二维数组，里面的元素表示坐标系上的点
随意选一个点固定，算出二维数组中有多少种组合方式，能挑出剩下两个点到本点的距离相等

ps: 按照题目的排练组合，同样的点换个顺序也是一种组合方式（这好像公考的排列组合 =-=）
            for c in counter.values():
                res += c * (c-1)
比如说，到本点距离为 3 的点有8个，8 * 7 = 56，也就是说会有 56 个 Boomerangs 的组合方式
'''


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        '''
        method 1 time limit exceed O(n^3)
        '''

        # def get_distance(x, y):
        #     # 只需距离相等，不需要精确的距离，因此不开平方根了
        #     return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        #
        # if len(points) <= 2:
        #     return 0
        # res = 0
        # for i in range(len(points)):
        #     for j in range(len(points)):
        #         if i != j:
        #             for k in range(len(points)):
        #                 if k != i and k != j and get_distance(points[i], points[j]) == get_distance(points[i], points[k]):
        #                     res += 1
        # return res

        ''' method 2
        time: O(N^2)
        space: O(N)
        '''
        def get_distance(x, y):
            # 只需距离相等，不需要精确的距离，因此不开平方根了
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        if len(points) <= 2:
            return 0
        res = 0
        for i in range(len(points)):
            counter = {}
            for j in range(len(points)):
                dis = get_distance(points[i], points[j])
                counter[dis] = counter.get(dis, 0) + 1

            for c in counter.values():
                res += c * (c-1)
        return res
