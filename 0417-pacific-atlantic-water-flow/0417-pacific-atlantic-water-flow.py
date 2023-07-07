class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r,c, visit, prevHeight):
            if ((r,c) in visit or 
                r not in range(ROWS) or 
                c not in range(COLS) or 
                heights[r][c] < prevHeight):
                    return 
                
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
                
        # left and right  
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS -1, atl, heights[r][COLS-1])
            
        # top and bottom
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])
        
        for i in list(pac):
            if i in atl:
                res.append(i)
                
        return res
        