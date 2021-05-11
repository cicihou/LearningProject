class Solution:
    def shortestToChar(self, s: str, c: str):
        # method 1 find c_position and calculate the distance
        # res = []
        # zero_point = []
        # for i in range(len(s)):
        #     if s[i] == c:
        #         res.append(0)
        #         zero_point.append(i)
        #     else:
        #         res.append(float('inf'))
        # for i in range(len(res)):
        #     for j in zero_point:
        #         if i != j:
        #             res[i] = min(res[i], abs(i-j))
        # return res

        # method 2 find c_position and calculate the distance
        # make it simple and fast
        # attention: c_position save index, don't use range(len()) in it
        c_position = [i for i in range(len(s)) if s[i] == c]
        return [min([abs(c-i) for c in c_position]) for i in range(len(s))]



s = Solution()
print(s.shortestToChar('loveleetcode', 'e'))
print(s.shortestToChar('aaab', 'b'))
