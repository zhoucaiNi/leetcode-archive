class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        seen = {}
        
        for i in range(len(s)):
            
            if s[i] not in seen:
                res = max(res, i-left + 1)
            else:
                if seen[s[i]] < left:
                    res = max(res, i-left + 1)
                else:
                    left = seen[s[i]] + 1
                    
            seen[s[i]] = i
            
        return res
                    