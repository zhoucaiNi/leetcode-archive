class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = collections.deque(((0, 1), (1, 0), (0,-1), (-1, 0)))
        # right, down, left, up
        
        seen = set()
        i,j = 0,0
        ROW, COL = len(matrix), len(matrix[0])
        totalCount = ROW * COL
        count = 1
        print(totalCount)
        res = [matrix[i][j]]
        seen.add((i,j))
        currDirection = directions.popleft()
        
        while count < totalCount:
            newR, newC = i + currDirection[0], j + currDirection[1]
            # print(newR, newC)
            # print(res)
            if (newR,newC) in seen or newR not in range(ROW) or newC not in range(COL):
                directions.append(currDirection)
                currDirection = directions.popleft()
            else:
                i = newR
                j = newC
                res.append(matrix[i][j])
                seen.add((i,j))
                count+=1
            
                
        return res
            