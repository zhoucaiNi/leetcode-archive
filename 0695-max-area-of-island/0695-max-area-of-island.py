class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       
        
        island = 0
        visit = set()
        highestArea = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r,c):
            if (
                r not in range(rows) or 
                c not in range(cols) or 
                (r,c) in visit or 
                grid[r][c] == 0
            ):
                return 0
            
            visit.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0, -1]]
            totalCount = 0
            for dr, dc in directions:
                totalCount += dfs(dr + r, dc + c)
                
            return totalCount + 1
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    highestArea = max(highestArea, dfs(r, c))
                    
        return highestArea
                
            
        