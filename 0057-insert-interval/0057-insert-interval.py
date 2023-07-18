class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in  range(len(intervals)):
            newStart, newEnd = newInterval[0], newInterval[1]
            start, end = intervals[i][0], intervals[i][1]
            if newEnd < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newStart > end:
                res.append(intervals[i])
            else:
                newInterval = [min(newStart, start), max(newEnd,end)]
                
        res.append(newInterval)
        
        return res
        