class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = maxp = 0

        for right in range(len(prices)):
            maxp = max(maxp,prices[right] - prices[left])
            if(prices[right]<prices[left]):
                left = right
        return maxp
