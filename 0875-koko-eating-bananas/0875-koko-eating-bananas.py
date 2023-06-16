class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = max(piles)
        
        while l <= r:
            mid = l + ((r-l) // 2)
            # mid = (l+r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if totalTime <= h:
                res = min(res, mid)
                r = mid -1
            else:
                l = mid +1
                
        return res