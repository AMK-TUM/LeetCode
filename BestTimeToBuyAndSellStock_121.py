class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float('inf')
        profit = 0
        for price in prices:
            if mn > price:
                mn = price
            elif profit < price - mn:
                profit = price - mn

        return profit
