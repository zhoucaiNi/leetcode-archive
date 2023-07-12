class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        
        left, right = 0 , k-1
        currV = 0
        
        for n in s[left:right]:
            if n in "aeiou":
                currV += 1
        
        while left <= len(s)-k:
 
            if left != 0:
                if s[left-1] in "aeiou":
                    currV -= 1
                
            if s[right] in "aeiou":
                    currV += 1
                    
            left+=1
            right+=1
                
            res = max(res, currV)
            
            
            
        return res