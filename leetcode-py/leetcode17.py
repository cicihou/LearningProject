class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        hashmap + backtrack
            hashmap 维护每个数字对应的所有可能字母
            每次取电话号码的一位数字，获得该数字对应的所有可能的字母，将其中的一个字母插入到已有的字母排列后面
            直到处理完电话号码中的所有数字，即得到一个完整的字母排列
            然后进行回退操作，遍历其余的字母排列

        '''
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        path = []

        if not digits:
            return []

        def backtrack(n):
            if n == len(digits):
                res.append(''.join(path))
            else:
                digit = digits[n]
                for letter in keyboard[digit]:
                    path.append(letter)
                    backtrack(n+1)
                    path.pop()
        backtrack(0)
        return res
