class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        # method 1
        # if len(a) != len(b) or set(a) != set(b):
        #     return False
        # if a == b:
        #     # if A and B are equal
        #     # return if we have at least 1 repetitive character in the list
        #     return len(a) - len(set(a)) >= 1
        # else:
        #     diff = [(i, j) for i, j in zip(a, b) if i != j]
        #     return len(diff) == 2 and diff[0] == diff[1][::-1]

        # method 2
        if len(a) != len(b):
            return False
        if a == b:
            # if a equals to b, the str a must have repetitive letter
            # so that it's a buddy string that can exchange one letter
            return len(set(a)) < len(a)
        # find the index of different letter
        # the volume of index must be 2
        index = []
        for i in range(len(a)):
            if a[i] != b[i]:
                index.append(i)
            if len(index) > 2:
                return False
        if len(index) != 2:
            return False
        return a[index[0]] == b[index[1]] and b[index[0]] == a[index[1]]


s = Solution()
print(s.buddyStrings('ab', 'ba'), True)
print(s.buddyStrings('ab', 'ab'), False)
print(s.buddyStrings('aa', 'aa'), True)
print(s.buddyStrings('aaaaaaabc', 'aaaaaaacb'), True)
print(s.buddyStrings('abcd', 'badc'), False)
print(s.buddyStrings('aaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaa'), True)
print(s.buddyStrings('bag', 'gab'), True)
print(s.buddyStrings('abcaa', 'abcbb'), False)
print(s.buddyStrings('abcccc', 'abcddd'), False)
print(s.buddyStrings('abab', 'abab'), True)
print(s.buddyStrings('abab', 'baba'), False)
print(s.buddyStrings('abac', 'abad'), False)