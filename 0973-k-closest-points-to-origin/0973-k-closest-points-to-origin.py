class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make a minHeap of size k 
        pts = []
        for x,y in points:
            distance = ((x ** 2) + (y ** 2))
            pts.append([distance,x,y])
        
        # iterate thry all the points and add to heap 
        res = []
        heapq.heapify(pts)
        for n in range(k):
            distance, x,y = heapq.heappop(pts)
            res.append([x,y])
        # return the one at the top 
        
        return res