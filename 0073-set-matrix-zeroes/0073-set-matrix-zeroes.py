class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        seen = set()
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0 and (i, j) not in seen :
                    k = 0
                    newI, newJ = i, j
                    while k < len(directions):
                        r,c = directions[k][0], directions[k][1]
                        newI, newJ = newI + r, newJ + c
                        if (newI not in range(row) or 
                            newJ not in range(col)):
                            newI, newJ = i,j
                            k+=1
                        else:
                            if matrix[newI][newJ] != 0:
                                seen.add((newI, newJ))
                                matrix[newI][newJ] = 0