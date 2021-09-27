from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1) or len(set(s2)) < len((set(s1))):
            return False
        counter1 = Counter(s1)
        n = len(s1)
        counter2 = Counter(s2[0:n])
        if counter1 == counter2:
            return True
        else:
            i = n
            while i < len(s2):
                ch = s2[i]
                old = s2[i-n]
                counter2[ch] = counter2.get(ch, 0) + 1
                counter2[old] -= 1
                if counter2[old] == 0:
                    counter2.pop(old)
                if counter1 == counter2:
                    return True
                i += 1
        return False
