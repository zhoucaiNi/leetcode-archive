class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = set()
        
        for i in nums:
            if i in t:
                return True
            else:
                t.add(i)
        return False
        