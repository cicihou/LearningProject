class Solution:
    def arrangeWords(self, text: str) -> str:
        '''
        time: O(n)
        space: O(n)
        '''
        words = text.split(' ')
        cache = {}
        for word in words:
            cache.setdefault(len(word), []).append(word)

        res = []
        for k in sorted(cache):
            res += cache[k]
        return ' '.join(res).capitalize()
