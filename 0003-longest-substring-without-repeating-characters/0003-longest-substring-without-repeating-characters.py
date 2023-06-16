class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left, res = 0, 0
        
        for i in range(len(s)):
            if s[i] not in seen:
                print(s[i],"not in see")
                print(i - left + 1)
                res = max(res, i - left + 1)
            else:
                if seen[s[i]] < left:
                    res = max(res, i - left + 1)
                else:
                    left = seen[s[i]] + 1
            seen[s[i]] = i
            
        return res 
        