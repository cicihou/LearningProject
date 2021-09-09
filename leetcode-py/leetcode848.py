class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)
        counts = []
        for i in range(len(shifts)):
            if i >= 1:
                total -= shifts[i-1]
            counts.append(total % 26)
        res = ''
        for ch, count in zip(s, counts):
            res += chr((ord(ch) + count) % 97 % 26 + 97)
        return res
