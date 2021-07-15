'''
https://leetcode-cn.com/problems/multi-search-lcci/

给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。

示例：

输入：
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
提示：

0 <= len(big) <= 1000
0 <= len(smalls[i]) <= 1000
smalls的总字符数不会超过 100000。
你可以认为smalls中没有重复字符串。
所有出现的字符均为英文小写字母。


由于这道题的时间复杂度要求不高，也可以直接 indexof 暴力遍历之后求出解法

Trie 做法如下所示：

Time：O(n * m)，n = len(big)， m = len(smalls)
Space：O(m * k)，k = max(len(smalls[i])), 即 k 是 smalls 中最长字符串的长度

'''

import collections
from typing import List


class Trie:
    def __init__(self, words):
        self.d = {}
        for word in words:
            t = self.d
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['end'] = word

    def search(self, s):
        t = self.d
        res = []
        for w in s:
            if w not in t:
                break
            t = t[w]
            if 'end' in t:
                res.append(t['end'])
        return res


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie = Trie(smalls)
        hit = collections.defaultdict(list)

        for i in range(len(big)):
            matches = trie.search(big[i:])
            for word in matches:
                hit[word].append(i)
        res = []
        for word in smalls:
            res.append(hit[word])
        return res


s = Solution()
s.multiSearch( "mississippi", ["is","ppi","hi","sis","i","ssippi"])
