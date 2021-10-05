from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        method 1 backtrack
        很经典的 backtrack 板子题

        time: O(k * (n! / (n-k)!k!) )
        space: O(n! / (n-k)!k!)

        complexity 有点难理解，可以从 state space tree 方面去想，画图理解为什么是factorial
        '''
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return res


        '''
        method 2 math
        '''
        return combinations([num for num in range(1, n+1)], k)
