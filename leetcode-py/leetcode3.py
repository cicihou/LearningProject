class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        method 1 brute force
        time O(n^2)
        space O(n)
        '''
        # count = 0
        # if s == '':
        #     return 0
        #
        # for i, letter in enumerate(s):
        #     li = [letter]
        #     for j in s[i+1:]:
        #         if j not in li:
        #             li.append(j)
        #         else:
        #             break
        #     count = max(count, len(li))
        #
        # return count

        ''' method 2 hash 
        time O(n)
        space O(n)
        '''
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i
        return max_length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
