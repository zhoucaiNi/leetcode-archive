class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            try:
                cur = cur[c]
            except:
                cur[c] = {}
                cur = cur[c]
        cur["word"] = {}
            

    def search(self, word: str) -> bool:
        cur = self.root
        
        def dfs(index, root):
            cur = root
            if index < len(word):
                if word[index] == ".":
                    for key in cur:
                        if dfs(index + 1, cur[key]):
                            return True
                    return False
                
                if word[index] not in cur:
                    return False
                    
            if index == len(word):
                if "word" in cur:
                    return True
                else:
                    return False
            cur = cur[word[index]]
            return dfs(index + 1, cur)
    
        return dfs(0, cur)
                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)