class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjList = { i: [] for i in range(N)}
        for i in range(N):
            x, y = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                distance = abs(x2 - x) + abs(y2 -y)
                adjList[i].append([distance, j])
                adjList[j].append([distance, i])
        
        seen = set()
        minH = [[0,0]]
        res = 0
        
        while len(seen) < N:
            cost, i = heapq.heappop(minH)
            if i in seen:
                continue
                
            res+=cost
            seen.add(i)
            for neiCost, nei in adjList[i]:
                heapq.heappush(minH, [neiCost, nei])
        
        
        return res