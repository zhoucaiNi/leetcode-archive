class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # even number
        # can't be multiples of each other 
        res = 0
        for l in range(len(nums)):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                i = l
                while (i < len(nums)-1 and nums[i+1] <= threshold and nums[i] % 2 != nums[i + 1] % 2):
                    i+=1

                res = max(res, i-l+1)
            
        return res

