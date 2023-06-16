class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, lowest = 0, prices[0]
        
        for price in prices:
            temp = price - lowest
            if price < lowest:
                lowest = price
            profit = max(profit, temp)
        return profit
        