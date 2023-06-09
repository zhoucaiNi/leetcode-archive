class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tCount = collections.Counter(s)
        sCount = collections.Counter(t)
        if tCount == sCount:
            return True
        return False
    
        