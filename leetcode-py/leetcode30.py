import copy


class Solution:
    def findSubstring(self, s: str, words):
        ''' sliding window
        由于 words 里面的 word 等长
        那么 words 的长 m 以及 word 的长 n 可以组成 m * n
        用这个 window 在 s 中遍历查找即可
        '''
        m = len(words)
        n = len(words[0])
        if len(s) < m * n:
            return []

        words_count = {}
        for w in words:
            words_count[w] = words_count.get(w, 0) + 1

        res = []
        i = 0
        while i + m*n <= len(s):
            tmp = s[i:i+m*n]
            # 注意此处必须是深拷贝
            tmp_words = copy.deepcopy(words_count)

            j = 0
            while j < len(tmp) and tmp[j*n:(j+1)*n] in tmp_words:
                tmp_words[tmp[j*n:(j+1)*n]] -= 1
                j += 1
            counts = tmp_words.values()
            # 注意此处判断条件必须有这两个，才能保证 counts 里面有且只有 0
            if sum(counts) == 0 and len(set(counts)) == 1:
                res.append(i)
            i += 1
        return res


s = Solution()
s.findSubstring('barfoothefoobarman', ["foo","bar"])
s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])
