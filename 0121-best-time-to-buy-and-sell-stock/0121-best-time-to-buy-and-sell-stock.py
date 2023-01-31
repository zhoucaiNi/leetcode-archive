class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            if prices[i]-lowest > profit:
                profit = prices[i]-lowest
        return profit