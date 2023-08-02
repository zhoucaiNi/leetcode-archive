class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i :[] for i in range(1, n+1)} # [target, time]
        
        for source, target, time in times:
            adjList[source].append([target, time])
        # print(adjList)
        seen = set()
        minHeap=[(0,k)]
        res = 0
        while minHeap:
            w1, h1 = heapq.heappop(minHeap)
            if h1 in seen:
                continue
            seen.add(h1)
            res = w1
            
            for target, time in adjList[h1]:
                print(target)
                heapq.heappush(minHeap, (time + w1, target))
                
        # print(seen)
        return res if len(seen) == n else -1
                
        