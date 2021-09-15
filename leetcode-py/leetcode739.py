class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        method 1 Brute Force, TLE

        time: O(n^2)
        space: O(n)

        :param temperatures:
        :return:
        '''
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res

        '''
        method 2 monostack
        
        这个写法多练习几遍啊，这是单调栈的纯模板题
        '''
        n = len(temperatures)
        res = [0] * n
        stack = []  # 单调递减的栈，后入栈的元素只允许小于先入栈的元素
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                peek = stack.pop()
                res[peek] = i - peek
            stack.append(i)
        return res
