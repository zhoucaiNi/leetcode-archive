class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[N-1][N-1], N-1,N-1 ]]
        seen = set()
        directions = [[0,1], [1,0], [-1,0],[0,-1]]
        res = 0
        
        while minHeap:
            depth, row, col = heapq.heappop(minHeap)
            if row == 0 and col == 0:
                return max(depth,res)
            print(depth)
            res = max(res, depth)
            for r, c in directions:
                newR, newC = row+r, col+c
                if ((newR,newC) in seen 
                    or newR >= N
                    or newC >= N
                    or newR < 0
                    or newC < 0):
                    continue
                    
                seen.add((newR, newC))
                heapq.heappush(minHeap, [grid[newR][newC],newR, newC])
        
        