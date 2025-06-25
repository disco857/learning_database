class TrieNode:
    def __init__(self, ):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.is_end = True

    def search(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        if cur_node.is_end:
            return True
        else:
            return False

    def starts_with(self, prefix):
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return True


tr = Trie()
tr.insert("apple")
tr.insert("Macbook")
tr.insert("application")
