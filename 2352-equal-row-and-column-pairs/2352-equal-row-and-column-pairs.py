from collections import defaultdict
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = []
        for i in (grid): r.append([])
        t = defaultdict(int)
        p = defaultdict(int)
        
        for index, row in enumerate(grid):
            
            for currIndex, num in enumerate(row):
                r[currIndex].append(num)
       
                
            if tuple(row) in t: 
                t[tuple(row)] += 1
            else:
                t[tuple(row)] = 1
                
        for val in r:
            if tuple(val) in t: 
                p[tuple(val)] += 1
            else:
                p[tuple(val)] = 1
        print(p)
        print(t)
        count = 0
        for i in p.keys():
            if i in t.keys():
                if 0:
                    count = p[i] * t[i]
                else:
                    count += (p[i] * t[i])
        return count
        