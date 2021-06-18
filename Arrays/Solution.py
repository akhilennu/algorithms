class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()

    def addWord(self, word: str) -> None:
        current = self.data
        for c in word:
            current.setdefault(c, {})
            current = current[c]
        current['#'] = 'END'

    def searchFrom(self, word: str, currentPos: dict) -> bool:
        if(len(word) == 1):
            if(word == '.'):
                for k in currentPos.keys():
                    if('#' in currentPos[k]):
                        return True
                return False
            else:
                return word in currentPos and '#' in currentPos[word]
        base = False
        if(word[0] == '.'):
            for k in currentPos.keys():
                if(k != '#' and self.searchFrom(word[1:], currentPos[k])):
                    return True
            return False
        else:
            if(word[0] in currentPos):
                return self.searchFrom(word[1:], currentPos[word[0]])
            return False

    def search(self, word: str) -> bool:
        current = self.data
        return self.searchFrom(word, current)


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("ran")
wordDictionary.addWord("rune")
wordDictionary.addWord("runner")
wordDictionary.search("runs")
wordDictionary.search("add")
wordDictionary.search("adds")
wordDictionary.search("adder")
wordDictionary.search("addee")
# wordDictionary.search("a")
# print(wordDictionary.search(".ad"))
print(wordDictionary.search("r.n"))
print(wordDictionary.search("ru.n.e"))
print(wordDictionary.search("add"))
print(wordDictionary.search("add."))
print(wordDictionary.search("adde."))
print(wordDictionary.search(".an."))
print(wordDictionary.search("...s"))
print(wordDictionary.search("....e."))
print(wordDictionary.search("......."))
print(wordDictionary.search("..n.r"))


["WordDictionary", "addWord", "addWord", "addWord", "addWord", "addWord", "addWord", "addWord", "addWord",
    "search", "search", "search", "search", "search", "search", "search", "search", "search", "search"]
[[], ["ran"], ["rune"], ["runner"], ["runs"], ["add"], ["adds"], ["adder"], ["addee"], ["r.n"], [
    "ru.n.e"], ["add"], ["add."], ["adde."], [".an."], ["...s"], ["....e."], ["......."], ["..n.r"]]
