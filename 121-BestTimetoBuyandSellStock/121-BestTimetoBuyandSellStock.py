class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxp =0

        for price in prices:
            minp = min(minp,price)

            price = price - minp

            maxp = max(maxp,price)
        
        return maxp

        