class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p = '#' + p  # 省去对 len(p) == 1 的特殊处理
        dic = {}
        pre = 1
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i-1]) in [1, -25]:
                pre += 1
            else:
                pre = 1
            dic[p[i]] = max(dic.get(p[i], 0), pre)
        return sum(dic.values())
