class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = {c: set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
                    
        print(adjList)
        
        seen = {}
        res = []
        # POST ORDER
        def dfs(c):
            if c in seen:
                return seen[c]
            
            seen[c] = True
            
            for nei in adjList[c]:
                if dfs(nei):
                    return True
                    
            seen[c] = False
            res.append(c)
            
        
        for c in adjList:
            if dfs(c):
                return ""
            
        
        
        return "".join(res[::-1])
            
                
            
        