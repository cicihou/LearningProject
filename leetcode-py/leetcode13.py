class Solution:

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        di1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        di2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        result = 0

        if s in di2:
            return di2[s]

        for element in di2:
            if element in s:
                result += di2[element]
                s = s.replace(element, '')

        for i in s:
            result += di1[i]
        return result

        '''
        method 2
        '''
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res + roman[s[-1]]
