class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # str给定是非空词

        if pattern is None:
            return False
        str_li = str.split(' ')
        if len(pattern) != len(str_li):
            return False
        data = {}
        for i in range(0, len(pattern)):
            data.setdefault(pattern[i], set()).add(str_li[i])
        # if set(data.keys()).symmetric_difference(set(pattern)):
        #     return False
        if len(data.keys()) != len(set(str_li)):
            return False
        for s in data.values():
            if len(s) > 1:
                return False
        return True


s = Solution()
print(s.wordPattern('abba', 'dog cat cat dog'), 't')
print(s.wordPattern("abba", "dog cat cat fish"), 'f')
print(s.wordPattern("aaaa", str="dog cat cat dog"), 'f')
print(s.wordPattern("abba", "dog dog dog dog"), 'f')
