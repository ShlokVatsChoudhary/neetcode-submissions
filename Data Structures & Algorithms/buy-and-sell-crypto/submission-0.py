class Solution:
    from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
            
        left = 0
        maxp = 0
        
        for i in range(1, n):
            if prices[i] < prices[left]:
                left = i
            else:
                maxp = max(maxp, prices[i] - prices[left])
                
        return maxp