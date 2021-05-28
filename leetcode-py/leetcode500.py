class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {'qwertyuiop', 'asdfghjkl', 'zxcvbnm'}
        res = {}
        for word in words:
            count = 0
            for d in dic:
                if set(word.lower()).issubset(set(d)):
                    count += 1
            res.setdefault(count, []).append(word)
        return res.get(1, [])
