class Solution:
    def countBits(self, n: int) -> List[int]:
        def hamminglength(t):
            res = 0
            while t:
                res += t % 2
                t = t >> 1
            return res
        res = []
        for i in range(n+1):
            res.append(hamminglength(i))
            
        return res