class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            res.setdefault(''.join(sorted(s)), []).append(s)
        return res.values()
