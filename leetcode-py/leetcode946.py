class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        '''
        method 1
        将 pushed 不停的入栈，当入栈的值 == popped 的头时，pushed 和 popped 同时去掉这个值
        bool 结果就看最后的 pushed 结果全部入栈时，popped 能不能把所有的数消耗完

        ！！！这一题有一个很重要的条件就是 pushed 和 popped 的值不会重复，是具有唯一性的，因此 pushed 和 popped 的值肯定能对应上
        :param pushed:
        :param popped:
        :return:
        '''
        # stack = []
        # for i in range(len(pushed)):
        #     stack.append(pushed[i])
        #     if stack[-1] == popped[0]:
        #         stack.pop()
        #         popped.pop(0)
        #         while stack:
        #             if stack[-1] == popped[0]:
        #                 stack.pop()
        #                 popped.pop(0)
        #             else:
        #                 break
        # return len(stack) == len(popped) == 0

        ''' method 2 将 popped 弹出来的这个过程简化成 index，不再实际操作 popped 这个数组
        leetcode 上大部分人用的也是这个写法 =-= 只是我一开始没看太明白
        顺便把 method 1 的while 条件简化一下，不需要显式的推出，上一版写的不好
        '''
        stack = []
        index = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            if stack[-1] == popped[index]:
                stack.pop()
                index += 1
                while stack and stack[-1] == popped[index]:
                    stack.pop()
                    index += 1
        return len(stack) == 0


        ''' method 3 能否不用 stack 这个中间栈变量，全部用index 完成？'''
        # TODO


        ''' method 4 一次循环，遍历 popped 数组
        指针 i 遍历 pushed，每次入栈时 += 1，指针 j 遍历 popped，出栈时 += 1
        1. 当 栈 不存在的时候，移动 pushed 指针，入栈, i += 1
        2. 当 栈 存在的时候，若 stack.peek == popped[j]，j++，注意 j 从 0 开始，只有这一个入口自增
        当 整个循环完成并推出，说明 出栈的个数 == len(popped)，就是 True
        若循环中，出现不满足 条件 1 和 2 就是 False
        这个方法节约空间，但并不节约时间；了解即可
        '''
        # stack = []
        # i = j = 0
        # while j < len(popped):
        #     if stack and stack[-1] == popped[j]:
        #         stack.pop()
        #         j += 1
        #     elif i < len(pushed):
        #         stack.append(pushed[i])
        #         i += 1
        #     else:
        #         return False
        # return True




s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]), 1)
print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]), 0)
print(s.validateStackSequences([2,1,0], [1,2,0]), 1)
print(s.validateStackSequences([0,2,1], [0,1,2]), 1)