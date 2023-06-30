class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        
        def dfs(i):
            if i >= len(s):
                res.append(part[::])
                
            for j in range(i, len(s)):
                print(s[i:j+1])
                if self.isPalin(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        
        return res
        
        
    def isPalin(self, word):
        l, r = 0, len(word) -1
        
        while l < r:
            if word[l] == word[r]:
                l+=1
                r-=1
            else:
                return False
            
        return True