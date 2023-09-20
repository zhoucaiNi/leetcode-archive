class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestValue = prices[0]
        
        for price in prices:
            if price < lowestValue:
                lowestValue = price
     
            profit = price - lowestValue
            if profit > maxProfit:
                maxProfit = profit
                    
        return maxProfit
                
            