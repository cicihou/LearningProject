class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        method 1 brute force
        time O(n^2)
        space O(n)
        '''
        count = 0
        if s == '':
            return 0

        for i, letter in enumerate(s):
            li = [letter]
            j = i + 1
            while j < len(s) and s[j] not in li:
                li.append(s[j])
                j += 1
            count = max(count, len(li))

        return count


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


        ''' method 3 sliding window
        Time O(N)
        Space O(N)
        
        https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation

        1. If s[r] not in seen, we can keep increasing the window size by moving right pointer
            if s[r] not in seen:
            output = max(output,r-l+1)

        2. There are two cases if s[r] in seen:
            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            case2: s[r] is not inside the current window, we can keep increase the window
            
        只有 s[r] in seen and seen[s[r]] >= l 时，需要移动窗口：l = seen[s[r]] + 1
        其它时候，都表示当前窗口没有遇到重复，可以继续自增
        '''
        l = r = 0
        seen = {}
        res = 0
        while r < len(s):
            if s[r] not in seen:
                res = max(res, r-l+1)
            else:
                # 坐标点 l, r，seen[s[r]],
                # [l, r] 表示当前 window，当 seen[s[r]] >= l 时，表示 s[r] 在 window 之中
                # seen[s[r]] 就是 s[r] 上一次出现的 index
                if seen[s[r]] >= l:
                    l = seen[s[r]] + 1
                else:
                    res = max(res, r-l+1)
            seen[s[r]] = r
            r += 1
        return res


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
