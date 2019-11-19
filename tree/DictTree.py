# 字典树


class TrieDemo:

    def __init__(self):  # 初始化
        self.root = {}
        self.end = -1

    def insert(self, word):  # 插入数据
        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
                curNode = curNode[c]

        curNode[self.end] = True

    def search(self, word):  # 查询
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]

        if not self.end in curNode:
            return False

        return True

    def startsWith(self, prefix):
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]

        return True


'''
下面是测试代码
'''
trie = TrieDemo()

trie.insert("something")
trie.insert("somebody")
trie.insert("somebody1")
trie.insert("somebody3")
print(trie.search("key"))
print(trie.search("somebody3"))
print(trie.startsWith('some'))
