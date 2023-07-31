class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, count):        
            if i == len(nums):
                return 1 if count == target else 0 
            
            if (i, count) in dp:
                return dp[(i, count)]
            
            dp[(i, count)] = dfs(i+1, count-nums[i]) + dfs(i+1, count+nums[i])
            
            return dp[(i, count)]
            
        return dfs(0, 0)
            