class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        
        need = collections.Counter(t)
        missing = len(t)
        
        start, end = 0,0
        l = 0
        for r, char in enumerate(s,1):
            if need[char] > 0:
                missing -=1
            if char in need:
                need[char] -= 1
         
            while missing == 0:
                # print(s[l:r])
                if end ==0 or r-l+1 <= (end-start+1):
                    start, end = l, r
                
                if s[l] in need:
                    need[s[l]] +=1
                    if need[s[l]] > 0:
                        missing += 1
        
                l+=1
                    
                    
        return s[start:end] 
    
                
                
                    
            
        