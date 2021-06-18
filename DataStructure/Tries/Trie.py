class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.data
        for c in word:
            current.setdefault(c, {})
            current = current[c]
        current['#'] = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.data
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return '#' in current

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.data
        for c in prefix:
            if c not in current:
                return False
            current = current[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
