class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[ float("inf") ] * (len(word2) + 1) for i in range(len(word1) + 1)]
        #  r o s _
        # h
        # o
        # r
        # s
        # e
        # |
        for i in range(len(word2)+1):
            cache[len(word1)][i] = len(word2) - i
       
        for j in range(len(word1)+1):
            cache[j][len(word2)] = len(word1) - j
            
        # print(cache)
        
        for i in range(len(word1) - 1, -1,-1):
            for j in range(len(word2)- 1, -1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
                    
        print(cache)
        
        return cache[0][0]