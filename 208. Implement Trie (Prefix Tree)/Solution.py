# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.children[""] = TrieNode()


    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return "" in current_node.children

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Solution using 2 sets instead of tree
class Trie2:
    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        pref = ""
        for i in word[:-1]:
            pref+=i
            self.prefixes.add(pref)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes or prefix in self.words


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)