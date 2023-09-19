class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = set()
        
        for num in nums:
            if num in t:
                return True
            else:
                t.add(num)
                
        return False