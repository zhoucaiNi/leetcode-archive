class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        interval = {}
        
        for i in range(len(s)):
            if s[i] in interval:
                interval[s[i]] = [interval[s[i]][0], i]
            else:
                interval[s[i]] = [i, i]
                
        
        newList = (list(interval.values()))
        resList = [newList[0]]
        
        # print(newList)
        for start, end in newList:
            if start <= resList[-1][1]:
                resList[-1][1] = max(end, resList[-1][1])
            else:
                resList.append([start,end])
                
        for i in range(len(resList)):
            resList[i] = resList[i][1] - resList[i][0] + 1
            
        return resList
                
        