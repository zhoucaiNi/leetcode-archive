class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            print(n)
            if n == 1:
                return True
            
            seen.add(n)
            temp = 0
            
            for i in str(n):
                temp += int(i) ** 2
            n = temp
                
        return False
                
            