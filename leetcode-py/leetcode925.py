class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        '''
        two pointer,
        虽然是道 easy 但是我自己也写了好久没写出来呀，思路一走偏就偏没影了

        :param name:
        :param typed:
        :return:
        '''
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
        return i == len(name)
