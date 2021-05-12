import re


class Solution:
    def decodeString(self, s: str) -> str:
        ''' stack method1 一个不太干净漂亮的栈
         这里的时间复杂度 time complexity 最坏结果是 O(n^2)
         '''
        # stack = []
        # for i in s:
        #     if i == ']':
        #         volume = ''
        #         tmp = ''
        #         while stack:
        #             val = stack.pop()
        #             if val == '[':
        #                 # integer 范围可以是 [0, 300] ，因此这里需要再进行一个小的循环
        #                 while stack:
        #                     a = stack.pop()
        #                     if a.isdigit():
        #                         volume = a + volume
        #                     else:
        #                         stack.append(a)
        #                         break
        #                 break
        #             # 这里注意拼接时最好能直接按原有顺序来；不要如果拼接时逆序，进栈的时候倒转
        #             # 由于拼好的数组也会多次进栈，如果是奇数次进栈，字符顺序就会有问题
        #             tmp = val + tmp
        #         stack.append(int(volume) * tmp)
        #     else:
        #         stack.append(i)
        # return ''.join(stack)

        ''' method 2 to make it more elegant '''
        # stack = []
        # curNum = 0
        # curString = ''
        # for i in s:
        #     if i == '[':
        #         stack.append(curString)
        #         stack.append(curNum)
        #         curString = ''
        #         curNum = 0
        #     elif i == ']':
        #         num = stack.pop()
        #         prevString = stack.pop()
        #         curString = prevString + curString * num
        #     elif i.isdigit():
        #         curNum = curNum * 10 + int(i)
        #     else:
        #         curString += i
        # return curString


s = Solution()
print(s.decodeString('3[a]2[bc]') == 'aaabcbc')
print(s.decodeString('3[a2[c]]') == 'accaccacc')
print(s.decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef')
print(s.decodeString('abc3[cd]xyz') == 'abccdcdcdxyz')
print(s.decodeString('1[f2[zy]1[ac]]') == "fzyzyac")
print(s.decodeString('10[et]'), "etetetetetetetetetet")
