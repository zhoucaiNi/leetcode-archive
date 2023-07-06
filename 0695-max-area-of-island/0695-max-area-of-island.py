class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r,c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or 
                (r,c) in seen or 
                grid[r][c] == 0
            ):
                return 0 
            
            seen.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (
                    (r,c) not in seen and
                    grid[r][c] == 1
                   ):
                    maxArea = max(maxArea, dfs(r,c))
                
        
        
        
            
            
        
        return maxArea