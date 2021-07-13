'''
lc 208 的变种，search 上略有变化
因为本题支持用 . 表示任意一个字符
'''

class TrieNode:
    def __init__(self):
        self.count = 0
        self.preCount = 0
        self.children = {}


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
            root.preCount += 1
        root.count += 1

    def search(self, word: str) -> bool:
        root = self.root
        for i, ch in enumerate(word):
            if ch == '.':
                words = []
                for k in range(ord('a'), ord('z')+1):
                    words.append(self.search(word[:i] + chr(k) + word[i+1:]))
                return any(words)
            elif ch not in root.children:
                return False
            root = root.children[ch]
        return root.count > 0

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
