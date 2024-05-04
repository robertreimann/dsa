class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    # Useful for autocomplete, spell checking etc.
    # Search time complexity: O(n), can better than hashmap because of no collisions.
    # Insert time complexity: O(n)
    # Space: O(n)
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def starts_with(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

