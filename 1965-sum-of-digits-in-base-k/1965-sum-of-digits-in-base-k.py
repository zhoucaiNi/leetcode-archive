class Solution:
    def sumBase(self, n: int, k: int) -> int:
        rSum = 0
        while (n>0):
            print((n % k))
            rSum += (n % k)
            n = n // k 

        return rSum