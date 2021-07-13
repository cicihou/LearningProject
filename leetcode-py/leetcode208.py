'''
Trie 字典树，前缀树。是一棵多叉树

常用于模糊搜索。基于相同前缀向下分叉，有共同前缀的词越多，效率越高
如果没有或很少相同前缀的词，效率很差

插入：遍历单词，
    1. 若单词对应的字符不在 Trie 上，则在 当前节点的 children 中添加 TrieNode
    2. 若单词相应的字符已经存在 Trie 上，则 count += 1
    注意遍历时所有的 nodes 都要 count += 1
time: O(len(key)), key 是字符串

search：遍历单词，
    1. 若单词对应的字符不在 Trie 上，返回 False
    2. 确认最后一个节点的 count 有值
time: O(len(key))，key 是字符串

startsWith：遍历单词
    1. 若单词对应的字符不在 Trie 上，返回 False
    2. 确认倒数第二个节点的 count 有值
time: O(len(key))，key 是字符串


build a Trie:
space: O(m^n)，m 是字符集中的字符个数，n 是字符串长度

'''


class TrieNode:
    def __init__(self):
        self.count = 0
        self.preCount = 0
        self.children = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
            root.preCount += 1
        root.count += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.count > 0

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.preCount > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
