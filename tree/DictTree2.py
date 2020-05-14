# 字典树

class TrieNode2:

    def __init__(self):
        self.childs = dict()  # 构建字典
        self.is_leaf = False

    def insert(self, word: str):
        curr = self
        for char in word:
            if char not in curr.childs:
                curr.childs[char] = TrieNode2()
            curr = curr.childs[char]
        curr.is_leaf = True

    def search(self, word: str):
        curr = self
        for char in word:
            if char not in curr.childs:
                return False
            curr = curr.childs[char]
        return curr.is_leaf


'''
下面是测试代码
'''
trie = TrieNode2()

trie.insert("anything")
trie.insert("anybody")
trie.insert("anybody1")
trie.insert("anybody3")
print(trie.search("key"))  # ->False
print(trie.search("anybody1"))  # ->True
