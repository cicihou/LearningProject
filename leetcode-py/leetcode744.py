class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        '''method 1 
        Disgusting and ugly to state the edge case. 
        In this solution, it ignores the str is ordered
        
        I write it in 2019.5 and I will not delete it for reminding me, dont write smelly code. It's hard to make it out now, even for myself.
        '''
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


        '''method2 linear compare'''

        for i in letters:
            if i>target:
                return i
        return letters[0]


        '''method3 binary search'''

        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return letters[l % len(letters)]


letters = ["c", "f", "j"]
solution = Solution()
print(solution.nextGreatestLetter(letters, "a"), "c")
print(solution.nextGreatestLetter(letters, "c"), "f")
print(solution.nextGreatestLetter(letters, "d"), "f")
print(solution.nextGreatestLetter(letters, "g"), "j")
print(solution.nextGreatestLetter(letters, "j"), "c")
print(solution.nextGreatestLetter(letters, "k"), "c")
print(solution.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "e"), "n")
