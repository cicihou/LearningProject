from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        sliding window
        这道题需要注意的边界条件细节非常多，核心思想就是用 sliding window
        1. 先将 window expand 到 window 中有满足 target 的 size（扩展 right）
        2. 在保证 window 中满足 target 的情况收缩 left
        3. 完成上面两步后，当前的[0,r]窗口最优解就是 [l,r]，但这不一定是全局最优解
           因此在 r < len(s) 的情况下，将 l 向右移一位，重新走 1/2 两步，直到完成循环，确定全局最优解
           
        Note: 需要注意的两步就是，如何计算 required count
        required_count = len(t) 【注意这里是未去重的，如果去重了又是另一种写法】
        当 window 的 count <= target 的 count 时，window 中的 count 每进行一次自增，window 满足条件的值就多了一个，required count -= 1
        当 window 收缩后 的 s[left] 值 < target 的 count 时，每丢失一个，意味着当前 window 不再满足条件，required_count += 1，推出循环
        '''
        target = Counter(t)

        if len(s) < len(t) or len(set(s)) < len(set(t)) or set(s).intersection(set(t)) != set(t):
            return ''

        l = r = 0
        window = {}
        res = ''

        required_count = len(t)

        while r < len(s):
            if s[r] in target:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] <= target[s[r]]:
                    required_count -= 1

            while required_count == 0:
                if s[l] in window:
                    if len(res) == 0 or len(s[l:r+1]) < len(res):
                        # 由于 python [) 的特性，这里要是 [l:r+1]
                        res = s[l:r+1]
                    window[s[l]] -= 1
                    if window[s[l]] < target[s[l]]:
                        required_count += 1
                    if window[s[l]] == 0:
                        window.pop(s[l])
                l += 1
            r += 1
        return res


s = Solution()
print(s.minWindow('ADOBECODEBANC', 'ABC') == 'BANC')
print(s.minWindow('BBHVTFYGIUHBJHVGC', 'BHVTFIUHBJ') == 'BHVTFYGIUHBJ')
print(s.minWindow('AABBBCBBHVTFYGIUHBJHVGC', 'BHVTFIUHBJ') == 'BHVTFYGIUHBJ')
print(s.minWindow('BBHVYGHBJHVGC', 'BHVHBJ') == 'BHVYGHBJ')
