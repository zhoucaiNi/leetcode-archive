class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1;
        
        arrList = [0,1,2]
        
        for x in range(3, n+1):
            arrList.append(arrList[x -1] + arrList[x-2])
            
        return(arrList[n])