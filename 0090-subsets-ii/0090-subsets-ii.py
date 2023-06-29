class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(index, subset):
            # base case
            if index == len(nums):
                res.append(subset[::])
                return
                
            # all subset that include nums[index]
            subset.append(nums[index])
            backtrack(index+1, subset)
            subset.pop()
            
            # all subset that does not include nums[index]
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
                
            backtrack(index + 1, subset)
            
        backtrack(0, [])
        
        return res
            
        