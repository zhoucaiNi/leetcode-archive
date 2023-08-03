class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {} # (rol, col) -> longestIncreasingPath
        
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        R = len(matrix)
        C = len(matrix[0])
        
        def dfs(row, col):
            res = 1
            if (row,col) in dp:
                return dp[(row, col)]
            
            for r, c in directions:
                newR, newC = row + r, col + c
                # print(newR, newC)
                if not (newR >= R or
                    newC >= C or 
                    newR < 0 or 
                    newC < 0 or 
                    matrix[newR][newC] <= matrix[row][col]):
                    res = max(dfs(newR, newC) + 1, res)
                    
            # print("wtf")
            dp[(row,col)] = res
            return res
                    
        for i in range(R):
            for j in range(C):
                # print(i,j)
                dfs(i,j)
        print(dp)
        return max(dp.values())
            
            
            
        