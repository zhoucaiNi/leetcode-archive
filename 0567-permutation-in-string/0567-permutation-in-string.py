from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        s1Count, s2Count = defaultdict(int), defaultdict(int)
        
        l, r = 0, len(s1)-1
        if len(s2) < len(s1):
            return False
        
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
            
        
        while r < len(s2)-1:
            if s1Count == s2Count:
                return True
            else:
                if s2Count[s2[l]] == 1:
                    s2Count.pop(s2[l])
                else:
                    s2Count[s2[l]]-=1
                l+=1
                r+=1
                s2Count[s2[r]] += 1
        print(s1Count)
        print(s2Count)
        return s1Count == s2Count
                
            
        
        
        