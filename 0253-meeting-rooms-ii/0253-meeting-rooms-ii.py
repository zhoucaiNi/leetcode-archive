class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        
        for iStart, iEnd in intervals:
            start.append(iStart)
            end.append(iEnd)
            
        start.sort()
        end.sort()
    
        count, res = 0,0 
        s, e = 0,0 
        for i in range(len(start)* 2 - 1):
            if  s == len(start) or end[e] <= start[s]:
                e+=1
                count-=1
            else:
                s+=1
                count+=1
                res = max(count, res)         
            
        return res