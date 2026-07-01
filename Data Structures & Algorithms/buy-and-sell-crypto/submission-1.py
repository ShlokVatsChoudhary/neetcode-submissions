class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        maxp = 0

        for right in range(left+1,n):
            maxp = max(maxp,prices[right] - prices[left])
            if(prices[right]<prices[left]):
                left = right
        return maxp
