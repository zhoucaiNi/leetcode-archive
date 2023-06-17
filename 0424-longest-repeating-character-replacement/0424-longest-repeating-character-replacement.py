class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, count= 0, {}
        res = 0
        maxf = 0
        for r in range(len(s)):
            # check for condition
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            
            if (r - l + 1 - maxf) > k:
                count[s[l]] -= 1
                if not count[s[l]]:
                    count.pop(s[l])
                l+=1
                
            res = max(res, r - l + 1)

        return res 
    
      
                
    
        