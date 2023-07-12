class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1,1 
        
        for n in nums:
            
            tmp = curMax * n 
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(curMin * n, n, tmp)
            res = max(curMax, res)
            
        return res