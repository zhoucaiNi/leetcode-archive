class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = set()
        s.add(0)
        target = sum(nums) / 2
        for i in range(len(nums)-1, -1,-1):
            dP = set()
            for j in s:
                if j + nums[i] == target:
                    return True
                
                dP.add(j+nums[i])
                dP.add(j)
            s = dP
        return False
            
        