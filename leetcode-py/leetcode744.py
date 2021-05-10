class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        '''method 1'''
        # for i, letter in enumerate(letters):
        #     if ord(target) > ord(letter) and ord(target) < ord(letters[i+1]):
        #         return letters[i+1]
        #     elif ord(letter) == ord(target):
        #         if i == len(letters)-1:
        #             return letters[0]
        #         elif letter ==letters[i+1]:
        #             continue
        #         return letters[i+1]
        #     elif ord(target) <= ord(letters[0]) or ord(target) > ord(letters[len(letters)-1]):
        #         return letters[0]
        #     else:
        #         continue

        '''method2'''
        # for i in letters:
        #     if i>target:
        #         return i
        # return letters[0]

        '''method3'''
        for i in letters:
            if ord(i)>ord(target):
                return i
        return letters[0]


letters = ["c", "f", "j"]
solution = Solution()
print(solution.nextGreatestLetter(letters, "a"), "c")
print(solution.nextGreatestLetter(letters, "c"), "f")
print(solution.nextGreatestLetter(letters, "d"), "f")
print(solution.nextGreatestLetter(letters, "g"), "j")
print(solution.nextGreatestLetter(letters, "j"), "c")
print(solution.nextGreatestLetter(letters, "k"), "c")
print(solution.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "e"), "n")

