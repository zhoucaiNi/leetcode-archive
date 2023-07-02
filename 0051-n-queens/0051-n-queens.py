class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        # r + c
        posDiagonal = set()
        # r - c
        negDiagonal = set()
        
        res = []
        board = [["."] * n for i in range(n)]
        
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDiagonal or (r-c) in negDiagonal:
                    continue
                    
                cols.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                board[r][c] = "Q"
                
                dfs(r+1)
                
                cols.remove(c)
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
                board[r][c] = "."
                
        dfs(0)
            
        return res
                
                