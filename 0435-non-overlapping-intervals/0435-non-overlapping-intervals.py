class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair:pair[0])
        prev = None
        print(intervals)
        res = 0
        for start, end in intervals:
            if prev == None:
                prev = [start,end]
            else:
                if start < prev[1]:
                    # print("overlap")
                    res+=1
                    if prev[1] > end:
                        prev = [start,end]
                else:
                    prev = [start,end]
        
        return res
            