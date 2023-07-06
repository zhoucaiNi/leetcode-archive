class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        print(nums)
        res = None
        for i in range(k):
            res = heapq.heappop(nums)
            
        return -res