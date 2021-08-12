class Solution:
    def reverseWords(self, s: str) -> str:
        words = [w for w in s.split(' ') if w]
        return ' '.join(words[::-1])
