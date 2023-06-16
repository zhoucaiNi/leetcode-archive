class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, lowest = 0, None
        
        for price in prices:
            if lowest == None:
                lowest = price
            else:
                temp = price - lowest
                if price < lowest:
                    lowest = price
                profit = max(profit, temp)
        return profit
        