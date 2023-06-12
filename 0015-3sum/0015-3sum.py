class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        
        for i, a in enumerate(nums):
            if a > 0:
                break
#           to reduce redundency
            if i > 0 and a == nums[i - 1]:
                continue
                
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.add((a, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    
        return res
        