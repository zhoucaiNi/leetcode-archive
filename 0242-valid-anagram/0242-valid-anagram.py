class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if collections.Counter(s) == collections.Counter(t):
            return True
        return False
    
        