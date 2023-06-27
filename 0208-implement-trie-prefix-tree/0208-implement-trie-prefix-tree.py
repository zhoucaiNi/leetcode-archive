class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie(object):

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.head
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True
            
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.head
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        
        if curr.end:
            return True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.head
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
                
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)