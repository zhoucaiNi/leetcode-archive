class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= 2*(n-1)
        time -= 2*max(0, time-n+1)
        return time+1