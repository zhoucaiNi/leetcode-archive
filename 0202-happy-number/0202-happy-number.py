class Solution:
    def isHappy(self, n: int) -> bool:
        b =set()
        b.add(n)

        while n != 1:
            t = str(n)
            tSum = 0
            
            for i in range(len(t)):
                tSum += int(t[i])**2

            if tSum in b:
                return False
            else:
                b.add(tSum)
            n = tSum

        return True


        