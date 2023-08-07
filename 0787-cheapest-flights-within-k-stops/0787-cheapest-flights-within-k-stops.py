class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList= {i: [] for i in range(n)} 
        
        for start, end, price in flights:
            adjList[start].append([end, price])

        print(adjList)
        minHeap = []
        for i in range(len(adjList[src])):
            minHeap.append([adjList[src][i][1], adjList[src][i][0]])
                
        print(minHeap)
        res = float("inf")
        seen = set()
        while k >= 0:

            t = len(minHeap)
            newList = []
            for i in range(t):
                # print(minHeap)
                totalCost, curr = heapq.heappop(minHeap)
                # print(totalCost, curr)
                if curr == dst:     
                    res = min(res, totalCost)

                if (totalCost, curr) in seen:
                    continue
                
                seen.add((totalCost, curr))
                for i in range(len(adjList[curr])):
                    if totalCost + adjList[curr][i][1] < res:
                        newList.append([totalCost + adjList[curr][i][1], adjList[curr][i][0]])
                    
            for l in newList:
                heapq.heappush(minHeap, l)
                
            k-=1
                
        return res if res != float("inf") else -1
            
            
            
            
            
            
            
        
        
        