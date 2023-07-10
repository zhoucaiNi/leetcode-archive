class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque()
        seen = set()
        
        def bfs(r,c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in seen
                or rooms[r][c] == -1
            ):
                return
            seen.add((r,c))
            q.append([r,c])
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    seen.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dist += 1
                
                
            
            