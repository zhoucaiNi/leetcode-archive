class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda pair:pair[0])
        
        print(intervals)
        
        for i in range(1, len(intervals)):
            t = intervals[i-1]
            p = intervals[i]
            
            if p[0] < t[1]:
                return False
            
        
        return(True)