class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        
        patternList = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patternList[pattern].append(word)
        
        
        seen = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q:  
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in patternList[pattern]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            
            res+= 1
            
            
        return 0 