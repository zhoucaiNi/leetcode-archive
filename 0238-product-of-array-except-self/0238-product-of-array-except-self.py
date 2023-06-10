class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        index = None
        product = 1
        for n in range(len(nums)):
            if nums[n] == 0:
                count +=1
                index = n
            else:
                product = product * nums[n]
            
            if count == 2:
                return [0] * len(nums)
     
                
                
        
        if count == 1:
            res = [0] * len(nums)
            res[index] = product
            return res
            
        res = []
        for n in (nums):
            res.append(int(product / n))
            
        return res
            
            
            
            
        