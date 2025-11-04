# Last updated: 11/4/2025, 10:05:19 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxp =0

        for price in prices:
            minp = min(minp,price)

            price = price - minp

            maxp = max(maxp,price)
        
        return maxp

        