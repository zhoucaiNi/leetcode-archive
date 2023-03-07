class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        t = collections.defaultdict(int)

        for i in nums:
            if i in t:
                return True
            t[i] = 1
        return False
    


        