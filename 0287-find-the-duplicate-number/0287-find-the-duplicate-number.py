class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t= set()
        
        for i in nums:
            if i in t:
                return i
            else:
                t.add(i)