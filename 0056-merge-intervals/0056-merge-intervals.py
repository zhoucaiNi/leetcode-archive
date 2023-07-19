class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair:pair[0])
        res = [intervals[0]]
        
        for start, end in intervals:
            prevEnd = res[-1][1]
            
            if start <= prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])
                
        return res
            
        