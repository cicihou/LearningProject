class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        1. 注意维护 diff 需要用两个hash，因为两个 str 之间彼此对应的 pattern 不一定一致
        2. 两个 if 条件的先后性要注意，先维护 hashmap，再判断 False
        time: O(n)
        space: O(1)，需要维护的 pattern 最多不超过 26 个，常数级别
        '''
        if len(s) != len(t):
            return False
        diff_a = {}
        diff_b = {}
        for i, j in zip(s, t):
            if i not in diff_a and j not in diff_b:
                diff_a[i] = j
                diff_b[j] = i
            elif diff_a.get(i) != j or diff_b.get(j) != i:
                return False
        return True
