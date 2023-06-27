class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            try:
                cur = cur[c]
            except:
                cur[c] = {}
                cur = cur[c]
        cur["."] = "."
        

    def search(self, word: str) -> bool:
        cur = self.root
        word += "."
        for c in word:
            try:
                cur[c]
            except KeyError:
                return False
            cur = cur[c]
            
        return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            try:
                cur[c]
            except KeyError:
                return False
            cur = cur[c]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)