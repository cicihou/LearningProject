import re


class Solution:
    def decodeString(self, s: str) -> str:
        ''' stack method1
         这里的时间复杂度 time complexity 最坏结果是 O(n^2)

         21.09.12 在原有基础上做了个优化，把栈改的更加简洁漂亮了
         第一个 while 处理字符串，第二个 while 处理 数字
         '''
        stack = []
        for i in s:
            if i == ']':
                volume = ''
                tmp = ''

                while stack[-1] != '[':
                    val = stack.pop()

                    # 这里注意拼接时最好能直接按原有顺序来；不要如果拼接时逆序，进栈的时候倒转
                    # 由于拼好的数组也会多次进栈，如果是奇数次进栈，字符顺序就会有问题
                    tmp = val + tmp
                stack.pop()
                while stack and stack[-1].isdigit():
                    a = stack.pop()
                    volume = a + volume
                stack.append(int(volume) * tmp)
            else:
                stack.append(i)
        return ''.join(stack)


        ''' method 2 to make it more elegant 
        
        由于测试用例的变化，这个 在 isdigit() 上面的写法有错，因为 testcase 存在 100[leetcode] 这样连续两位都是 0 的数字
        '''
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
