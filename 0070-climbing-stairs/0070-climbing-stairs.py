class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        first = 1
        second = 2
        i = 3
        while i <= n:
            third = first + second
            first = second
            second = third
            i+=1
        return second