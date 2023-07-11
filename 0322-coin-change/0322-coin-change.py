class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [amount + 1] * (amount + 1)
        
        res[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    res[a] = min(res[a], 1+ res[a-c])
        
        return res[amount] if res[amount] != (amount + 1) else -1
            
                
            
        