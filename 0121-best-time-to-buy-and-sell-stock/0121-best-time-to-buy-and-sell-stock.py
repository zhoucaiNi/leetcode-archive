class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        lowest = prices[0]
        for i in prices:
            if i < lowest:
                lowest = i
                
            if i - lowest > profit:
                profit = i - lowest
                
        return profit
            
            
            