class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        island = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            
            direction = [[0,1], [0,-1], [1,0], [-1,0]]
            while q:
               
                row,col = q.popleft()
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    # print((r,c))
                    if (r in range(ROWS) and 
                        c in range(COLS) and 
                        grid[r][c] == "1" and
                        (r,c) not in visited):
                            q.append((r,c))
                            visited.add((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    # print(visited)
                    island += 1
                    
        return island
    
        
                    
                    
                
        
        