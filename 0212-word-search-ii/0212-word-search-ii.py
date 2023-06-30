class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.isWord = True
        
    def removeWord(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        
        t = TrieNode()
        
        for w in words:
            t.addWord(w)
        
        res, path = set(), set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
            r == ROWS or c == COLS or
            (r,c) in path or
            board[r][c] not in node.children or
            node.children[board[r][c]].refs < 1):
                return 
            
            path.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.isWord:
                node.isWord = False
                res.add(word)
                t.removeWord(word)
                
            
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            
            path.remove((r,c))
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, t, "")
                
        return list(res)
            
            
        