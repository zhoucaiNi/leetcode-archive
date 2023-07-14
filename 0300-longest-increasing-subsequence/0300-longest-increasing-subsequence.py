class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # init LIS
        LIS = [1] * len(nums)
                
        # loop 
        for i in range(len(nums) -1 , -1, -1):
            for j in range(i+1, len(nums)):
                # if greater, 
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    
        return max(LIS)
                    
        